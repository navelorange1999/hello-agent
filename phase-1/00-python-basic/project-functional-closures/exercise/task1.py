# ### Task 1：函数是一等公民（Day 1）

# - [ ] 把一个函数赋值给变量、放进列表、当参数传递给另一个函数。如果你对这些操作感觉"理所当然"，很好——说明 JS 的经验在迁移。但注意下一步的差异
# - [ ] 用 lambda 写几个简单的匿名函数。**思考**：JS 的箭头函数可以有多行函数体，Python 的 lambda 只能写一个表达式——这个限制意味着什么？Python 程序员怎么处理需要多行逻辑的场景？
# - [ ] 用 Python 的内置高阶函数 `map()`、`filter()`、`sorted(key=...)` 处理数据。注意 `map(fn, iterable)` 和 JS `arr.map(fn)` 的参数顺序差异
# - [ ] 搜索并使用 `functools.reduce`。**思考**：为什么 Python 把 `reduce` 放进了 `functools` 而不是作为内置函数？这背后是一种什么设计哲学？

# 📚 **Key docs**: [函数式编程 HOWTO](https://docs.python.org/3/howto/functional.html) | [functools 模块](https://docs.python.org/3/library/functools.html)
# > HOWTO 的前三节讲清了 Python 函数式编程的定位和边界；functools 重点看 reduce 和 partial

#### Task1.1
def add(a,b):
    return a + b

def sub(a, b):
    return a - b

my_func = add
print(my_func(1, 2))


print([func(1,2) for func in[add, sub]])
# [AI 批注] ✅ 已修正：[func(1,2) for func in [add, sub]] —— "函数放进 list 并调用"这个场景完成了。
#   而且用推导式写法非常 Pythonic。输出 [3, -1] 正好展示了"同一个容器里装着不同行为的函数"这个核心感觉。
#   🔸 小提示：后续"当参数传递给另一个函数"的场景已经由 Task1.3 的 map/filter 实际覆盖了
#      （map(lambda, arr) 就是把 lambda 当参数传给 map），所以 Task1.1 现在三个维度都够了。
#   🔸 代码风格微调：for func in[add, sub] —— "in" 和 "[" 之间按 PEP 8 应该有个空格：
#      for func in [add, sub]。小事但养成 linter 习惯。
#
# [AI 批注] ✅ 已修正：把 sum 改成了 add，my_func 命名也清晰。以后遇到任何想用 sum/list/dict/id/type/filter/map
#   当变量名的冲动，都要停一下——这个习惯你已经建立起来了。

#### Task1.2
add = lambda a,b: a + b
print(add(1, 2))
# lambda 都是尽量一行，然后一些简单的逻辑，涉及多行的复杂逻辑还是使用 def 定义函数
# [AI 批注] ✅ 结论方向对了：lambda 只能写表达式，多行逻辑用 def。
#
# [AI 批注] ✅ 已修正：lambda 现在返回 a + b（纯函数），不再是为 print 副作用存在。
#   这是 lambda 的正确用法。
#
# [AI 批注] 💡 设计意图补充：PEP 8 作者 Guido 希望 lambda 保持"小而纯"——
#   一旦需要多行/赋值/if-else 分支，就应该命名它（用 def）。命名本身是文档。
#   这是 Python "Explicit is better than implicit" 哲学的体现。
#
# [AI 批注] ⚠️ 新问题：add = lambda a,b: a + b 覆盖了 Task1.1 里的 def add。
#   这不是内置遮蔽，但同样不好——你在 Task1.1 补的 apply(add, 3, 4) 能工作，只是因为 Task1.2 在它之后执行。
#   如果有人把顺序颠倒，apply(add, ...) 会调用 lambda 版本。
#   这揭示了一个更普遍的规律：Python 的模块是顺序执行的脚本，同名变量会被后来者覆盖，没有"作用域隔离"保护。
#   建议：每个 Task 用独立的名字（add_v1 / add_lambda），或者把每个 Task 包进 def demo_task_1_2(): ... 里。
#   后者是"用函数作用域做隔离"——其实已经在走向闭包的思路了。

#### Task1.3
arr = [3, 5, 4, 2, 0, 8]
print(list(map(lambda item: item * 2, arr)))
print(list(filter(lambda item: item % 2 == 0, arr)))
print(sorted(arr, reverse=True))
# map / filter 都是最开始设计的接口，现在跟推崇 sorted 这种设计形式，然后现在社区都用推导式来代替 map 和 filter
# [AI 批注] ✅ map / filter / sorted 三个都用对了，也观察到了一个关键现象——社区倾向推导式。
#
# [AI 批注] ✅ 已修正：去掉了冗余的 key=lambda item: item，现在是干净的 sorted(arr, reverse=True)。
#   顺便记住这个反向知识：什么时候 key 是必需的——按属性/派生值排序时。
#   例如 sorted(words, key=len) 按长度、sorted(users, key=lambda u: u.age) 按年龄。
#
# [AI 批注] 📝 你写的笔记里有两个点值得展开：
#   1) "map/filter 是最开始设计的接口，现在更推崇 sorted 这种设计形式"——这个说法需要澄清。
#      map/filter/sorted 其实是同时代的设计，不是新旧替代关系。
#      真正的差异是：sorted 用 key= 关键字参数，意图清晰；map/filter 只接受一个 callable，
#      当 callable 逻辑稍复杂时可读性下降，这才是推导式胜出的原因。
#   2) "社区都用推导式代替 map/filter"——方向对，但不是全部。什么时候 map/filter 仍然更好？
#      想一想：如果你手上已经有一个现成的函数对象（比如 str.upper），你会怎么写？
#        map(str.upper, words)  vs  [s.upper() for s in words]
#      前者更短、更声明式；后者多了一对方括号和变量名 s。这是 map 仍然存活的生态位。
#      （在 Agent 框架里很常见：你有一堆 tool 函数，用 map 把它们应用到数据上。）
#
# [AI 批注] 💡 JS ↔ Python 参数顺序差异（题目提到的）：
#   JS:     arr.map(fn)           → 方法调用，数据是 this
#   Python: map(fn, iterable)     → 自由函数，函数在前，数据在后
#   这个"函数在前"的顺序和函数式语言（Haskell、Clojure）一致，方便做 curry 和 compose——
#   下一个 Task 你会实现 pipe/compose，到时候会体会到这个设计的价值。


#### Task1.4
from functools import reduce
print(reduce(lambda x,y: x - y, [1,2,3,4,5], 100))
# Python 推崇一眼就能看出在干什么，但是 reduce 可以做很多逻辑，需要人去阅读 reduce 里的 function 具体是什么逻辑，如果还有 initial value 还要叠加 initial value 的影响。
# 所以将 reduce 放在 functools 里，希望大家能尽量用简洁的内置函数，如果实在要用就从 functools 里导入
# [AI 批注] ✅ 输出 85 (= 100-1-2-3-4-5)，逻辑对。reduce(fn, iterable, initial) 的语义也抓准了。


# ============================================================
# [AI 批注] 📊 整体评价（三次 review）
# ============================================================
#
# 完成度：★★★★★ (5/5)  ← 从 4/5 提升
# - Task1.1 三个维度（赋值 / 放 list / 当参数）都覆盖了 ✅
# - 用推导式装载函数，写法 Pythonic
#
# 代码质量：★★★★☆ (4/5)
# - 主要问题都改完了
# - 唯一遗留：Task1.2 的 add = lambda 仍然覆盖了 Task1.1 的 def add（见上方批注）
# - 小风格：for func in[add, sub] 缺一个空格
#
# 理解深度：★★★★☆ (4/5)
#
# 还剩下的 2 件事：
# 1. 🟡 Task1.2 避免 add 覆盖 Task1.1 的 add——用不同名字（add_lambda），
#    或把每个 Task 包进 def 里做作用域隔离（这个隔离思路正好是 Task 2 闭包的前奏）。
# 2. 🟢 可选：笔记补 JS↔Python 参数顺序差异 + reduce 空 iterable 的 TypeError 陷阱。
#
# 收尾状态良好，可以直接进 Task 2 闭包了——Task 2 会让你真正体会到"作用域隔离"为什么重要。
#
# [AI 批注] 📝 你对"为什么 reduce 被放进 functools"的理解方向是对的，我帮你把这个故事讲完整——这是 Python 设计哲学里非常有名的一段：
#   1) Python 2 时代 reduce 是内置函数。
#   2) Python 3 把它移到了 functools。这是 Guido 本人的决定，他的原话大意是：
#      "90% 的 reduce 用法都能用更清晰的 sum/any/all/max/min 或一个简单的 for 循环替代；
#       剩下 10% 的 reduce，读者需要花时间在脑中模拟才能理解。"
#   3) 移到 functools 不是"禁用"，而是给它一个更合适的位置——告诉读者："这是进阶工具，用的时候要谨慎"。
#
#   这对应 Python 的核心价值观（import this 里的 Zen）：
#     - Readability counts.
#     - There should be one-- and preferably only one --obvious way to do it.
#     - Explicit is better than implicit.
#
#   实战建议：
#     求和 → sum(iterable)
#     判断 → any(...) / all(...)
#     极值 → max(...) / min(...)
#     以上都不行 → for 循环 + 累加变量
#     最后才 → reduce
#
# [AI 批注] 💡 有个值得你思考的问题：你写的 reduce(lambda x,y: x-y, [1,2,3,4,5], 100) 如果换成不带 initial value，
#   会发生什么？reduce 的 initial value 省略规则你研究过吗？
#   （提示：空列表 + 无 initial 会抛 TypeError，这是 reduce 的一个坑）