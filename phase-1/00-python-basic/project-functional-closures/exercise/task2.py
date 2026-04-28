# ### Task 2：闭包与作用域（Day 1-2）

# - [ ] 写一个函数，它返回另一个函数——内部函数使用外部函数的参数。调用它，验证闭包确实"记住了"外层的变量
# - [ ] 搜索 Python 的作用域规则 LEGB（Local -> Enclosing -> Global -> Built-in）。**思考**：和 JS 的作用域链相比，Python 的作用域查找有什么不同？为什么 Python 需要 `nonlocal` 和 `global` 关键字，而 JS 不需要？
# - [ ] 实现一个 `make_counter()` 函数——返回一个函数，每次调用计数 +1 并返回当前值。你需要用到 `nonlocal`，否则会报错。想想为什么
# - [ ] 在循环中创建闭包：用循环创建 5 个函数，每个函数应该打印自己的序号。直接写，观察结果是否符合预期。**思考**：如果结果不对，这和 JS 中 `var` 在循环中的经典陷阱是同一个问题吗？怎么修？
# - [ ] 实现一个 `make_logger(prefix)` —— 返回一个函数，调用时输出带前缀的日志
# - [ ] **关键理解**：装饰器 `@decorator` 的语法糖本质就是 `func = decorator(func)`。现在你能解释为什么装饰器需要是"接受函数、返回函数"的闭包了吗？

# 📚 **Key docs**: [Python 作用域与命名空间](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces) | [nonlocal 语句](https://docs.python.org/3/reference/simple_stmts.html#the-nonlocal-statement)
# > 作用域文档在"类"章节里（因为类也涉及命名空间），重点读 LEGB 查找顺序的描述；nonlocal 文档很短但精确

#### Task2.1
def outside():
    outside_a = 2
    def inside(num):
        return num * outside_a
    return inside

print(outside()(2))
# [AI 批注] ✅ 标准闭包写法：inside 引用了 outside 的局部变量 outside_a，
# 即使 outside 已经返回，outside_a 也被 inside 这个函数对象"记住"了。
# 可以打印 outside().__closure__ 看看，会发现里面装着一个 cell，cell.cell_contents 就是 2。
# 这个 cell 对象就是 Python 实现闭包的底层机制。


#### Task2.2
# 先说相同点：Python 和 JS 的作用域链都是从内向外探索的
# 不同点：
    # JS 还有块级作用域（let / const 声明的变量都是优先生效于函数内 / for / if 等 `{}` 内，块级作用域外无法访问）
    # 赋值差异：如果在作用域内对作用域外一个同名的变量进行赋值，对于 JS 来说会修改外层变量，对于 Python 来说是相当于在内层作用域新建一个变量
    # Python 有个比较特别的类作用域：方法内部查找变量时，会跳过所在类的作用域，直接从 Enclosing 或 Global 找。

# 所以 Python 为了在内层修改外层的变量, 就引入了 `nonlocal` 和 `global` 关键字
# [AI 批注] 📝 分点逐项点评：
#
# 1. "Python 和 JS 都是从内向外探索作用域链" ✅ 正确，方向一致。
#
# 2. "JS 有块级作用域，Python 没有" ✅ 正确，但可以更精确：
#    Python 根本没有块级作用域——for/if/while/with 都不会创建新作用域。
#    所以下面这段 Python 代码不报错：
#        for i in range(3): pass
#        print(i)   # i 还在！值是 2
#    在 JS 里用 let 写就是 ReferenceError。
#
# 3. "赋值差异" ⚠️ 描述方向对了，但 JS 那一侧不准确：
#    JS 中 `x = 5`（不带 let/const/var）——如果作用域链上能找到 x，会"沿链上溯"修改最近的那个；
#    如果找不到，在非严格模式会创建一个全局变量（严格模式直接报错）。
#    JS 中 `let x = 5`——总是在当前块新建变量。
#    所以更精确地说：Python 默认行为是"赋值即新建"，需要显式 `nonlocal/global` 才能修改外层；
#    JS 默认行为是"赋值即沿链查找已有变量并修改"，需要 `let/const/var` 才能新建。
#    两种语言其实是默认行为相反，所以谁需要"逃生关键字"不一样。
#
# 4. "类作用域会被方法跳过" ✅ 这一点非常加分，是很深的细节。
#    经典反例：
#        class A:
#            x = 1
#            def f(self): return x   # NameError！不是 self.x 的话查不到 x
#    很多 Python 老手都会在这里踩坑。
#
# 5. "所以 Python 引入 nonlocal/global" ✅ 结论正确。
#    补一句：JS 不需要这两个关键字，正是因为 JS 的赋值默认行为本身就是"修改外层"，
#    它需要的是反方向的 let/const 来"切断"这个默认行为。两边其实是对称的。

#### Task2.3
def make_counter():
    counter = 0
    def inner():
        nonlocal counter
        counter = counter + 1
        return counter
    return inner

counter_func = make_counter()
print(counter_func())
print(counter_func())
print(counter_func())
# [AI 批注] ✅ 标准答案。
# 想想为什么不加 nonlocal 会报 UnboundLocalError——
# 因为 Python 编译期就决定了变量归属：函数体里只要出现 `counter = ...`，
# Python 就把 counter 标记为局部变量，那么 `counter + 1` 这一步读取的是
# 一个还没被赋值的局部变量，所以报错。nonlocal 的作用是告诉编译器：
# "别把它当成局部变量，去 enclosing 作用域绑定"。
#
# 💡 思考延伸：换种写法你也可以不用 nonlocal——把 counter 装进一个可变对象里：
#     counter = [0]    # 或 {}、自定义类
#     def inner():
#         counter[0] += 1   # 这里没有给 counter 这个名字赋值，是修改它指向的列表
# 这种写法实际上是 Python 2 时代没有 nonlocal 时的常见 hack，
# 现在不推荐，但能帮你理解"重新绑定 vs 修改对象"是两件不同的事。

#### Task2.4
# def make_func_array():
#     return [lambda: index for index in range(5)]

# print([make_func_array()[index]() for index in range(5)])
# will print: [4,4,4,4,4]

def make_func_array():
    def make_index(i):
        return lambda: i
    return [make_index(index) for index in range(5)]

print([make_func_array()[index]() for index in range(5)])
# [AI 批注] ✅ 已修正。这一版完全到位：
#   - make_index(i) 返回 `lambda: i`——每次调用 make_index 都创建一个新的局部 i，
#     lambda 通过闭包捕获到的是这个全新的 cell，互不干扰。
#   - 列表里现在装的是 5 个函数，调用时分别拿到 0,1,2,3,4。
# 这就是上面提示里的"方法 B"——用工厂函数为每次迭代制造独立绑定。
#
# 💡 想再加深一步？把这一版和默认参数版对比一下：
#       return [lambda i=index: i for index in range(5)]
# 同样能跑出正确结果，但机制不同：
#   - 工厂函数版：靠"函数调用产生新作用域"来隔离 i
#   - 默认参数版：靠"默认值在函数定义时求值并存进函数对象"来固定值
# 两者都能修好这个 bug，但底层路径不一样。能讲清楚这两种区别，
# 闭包的心智模型就真的扎实了。
#
# 顺便看一眼底层验证：把 make_index(0).__closure__[0].cell_contents 打出来，
# 你会看到 0；再看 make_index(3).__closure__[0].cell_contents，是 3。
# 这就是 5 个独立 cell 的直接证据。

#### Task2.5
def make_logger(prefix):
    def custom_logger(text):
        print(f"{prefix}: {text}")
    return custom_logger

custom_logger = make_logger("[TEST]")

custom_logger("Hello World!")
# [AI 批注] ✅ 简洁正确，prefix 被闭包捕获、复用，是工厂函数的标准范式。
# ⚠️ 一个小风格点：外层变量名建议不要和返回的函数同名。
# 你这里 `custom_logger = make_logger("[TEST]")` 的左侧名字
# 正好是函数内部的 inner 名 `custom_logger`，能跑但容易让读者误以为
# 在引用同一个东西。改成 `info = make_logger("[INFO]")` 这种语义化的
# 名字会更清晰——这其实就是 logger 工厂的真实用法。
#
# 💡 延伸：如果让你支持 `logger.info()` / `logger.error()` 这种带级别的调用，
# 你会怎么改造 make_logger？这其实就走向"对象 + 方法 = 闭包 + 多函数"的对照点了。

#### Task2.6
# Answer: 因为本质就是装饰器里面的局部变量增强了函数的一些能力
# [AI 批注] ⚠️ 答到了"增强能力"这一层，但还没回答到结构性的问题。
# 题目问的是：为什么装饰器必须是"接受函数、返回函数"的闭包？
# 关键推导链：
#   `@decorator` 等价于 `func = decorator(func)`
#   ↓
#   左边 `func` 是一个名字，重新赋值后业务代码还会继续 `func(...)` 调用它
#   ↓
#   所以 `decorator(func)` 的返回值必须是 callable（要能像函数一样被调用）
#   ↓
#   而要在调用时既执行原逻辑、又附加新行为，就需要一个新函数把原 func 包起来
#   ↓
#   这个新函数要"记住"原 func（避免被覆盖），就必须用闭包捕获原 func
#
# 所以"接受函数"是因为要拿到原函数，"返回函数"是因为返回值必须能继续被当函数调用，
# "闭包"是把原函数封存起来的唯一机制。三者缺一不可。
# 用你自己的话再写一版试试，别怕啰嗦——能讲清楚这一段，
# 你下一章学装饰器就是降维打击。
#
# 💡 延伸到 Agent 框架：LangChain 的 `@tool` 装饰器收到你的函数后，
# 会读取它的 docstring、签名、类型注解，然后返回一个增强对象——
# 这个对象记着原函数（闭包捕获），还多挂了 schema、参数校验、日志等能力。
# `@tool` 之所以能"零侵入"地把普通函数变成 Agent 可调用的工具，靠的就是这个套路。


# ============================================================
# [AI 批注] 📊 整体评价（第 2 轮 review）
# ============================================================
#
# 完成度：★★★★★ (5/5)  ← 上轮 4/5
# - Task 2.4 已修正，6 个子任务全部完成且 Task 2.4 选用了正确的工厂函数路径。
#
# 代码质量：★★★★☆ (4/5)
# - 闭包写法干净。
# - Task 2.5 中外层变量名和内层函数名相同的小瑕疵仍未处理（非阻塞性）。
#
# 理解深度：★★★★☆ (4/5)
# - Task 2.4 这次切中了循环闭包陷阱的核心——通过工厂函数为每次迭代造出独立绑定。
# - Task 2.2 关于 JS 赋值规则的精确度，本轮未更新。
# - Task 2.6 关于装饰器结构性论证的展开，本轮未更新。
#
# 仍可优化的事项：
# 1. 🟡 Task 2.6：补完结构性论证（接受函数 / 返回函数 / 闭包，三者各自的必要性）。
# 2. 🟡 Task 2.2：把 JS 赋值规则补精确（区分有无 let/var、严格模式）。
# 3. 🟢 Task 2.5：外层变量改名，模拟真实日志工厂用法。
# 4. 🟢 选做：对比 Task 2.4 的"工厂函数版"和"默认参数版"两种修法的底层差异。
# 5. 🟢 选做：打印 __closure__ 和 cell_contents，亲眼验证闭包机制。
#
# 总评：核心概念（闭包、nonlocal、循环闭包陷阱）已经掌握，可以进入 Task 3 函数管道了。
# Task 2.6 的结构性论证建议在写 Task 3 之前补上，因为接下来很快会用到装饰器思维。