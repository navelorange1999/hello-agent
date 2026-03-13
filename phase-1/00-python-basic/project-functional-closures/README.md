# Project: 函数式工具集

## 为什么做这个项目？

01 章的装饰器项目是整个 Agent 学习路径的关键——LangChain 的 `@tool`、FastAPI 的 `@app.get()` 都是装饰器。而装饰器的本质就是**闭包 + 高阶函数**。如果你不理解"函数可以返回函数"和"闭包如何捕获变量"，装饰器对你来说就是黑魔法。这个项目帮你在进入装饰器之前，彻底搞懂 Python 的函数式编程基础。

---

## 项目目标

构建一套函数式数据处理工具集，包含：

1. 自己从零实现的 map、filter、reduce
2. 一个管道（pipeline）系统，支持链式数据处理
3. 一个缓存/记忆化函数
4. 一组生成器工具，理解 Python 的惰性求值

---

## 任务拆解

### Task 1：函数是一等公民（Day 1）

- [ ] 把一个函数赋值给变量、放进列表、当参数传递给另一个函数。如果你对这些操作感觉"理所当然"，很好——说明 JS 的经验在迁移。但注意下一步的差异
- [ ] 用 lambda 写几个简单的匿名函数。**思考**：JS 的箭头函数可以有多行函数体，Python 的 lambda 只能写一个表达式——这个限制意味着什么？Python 程序员怎么处理需要多行逻辑的场景？
- [ ] 用 Python 的内置高阶函数 `map()`、`filter()`、`sorted(key=...)` 处理数据。注意 `map(fn, iterable)` 和 JS `arr.map(fn)` 的参数顺序差异
- [ ] 搜索并使用 `functools.reduce`。**思考**：为什么 Python 把 `reduce` 放进了 `functools` 而不是作为内置函数？这背后是一种什么设计哲学？

📚 **Key docs**: [函数式编程 HOWTO](https://docs.python.org/3/howto/functional.html) | [functools 模块](https://docs.python.org/3/library/functools.html)
> HOWTO 的前三节讲清了 Python 函数式编程的定位和边界；functools 重点看 reduce 和 partial

### Task 2：闭包与作用域（Day 1-2）

- [ ] 写一个函数，它返回另一个函数——内部函数使用外部函数的参数。调用它，验证闭包确实"记住了"外层的变量
- [ ] 搜索 Python 的作用域规则 LEGB（Local → Enclosing → Global → Built-in）。**思考**：和 JS 的作用域链相比，Python 的作用域查找有什么不同？为什么 Python 需要 `nonlocal` 和 `global` 关键字，而 JS 不需要？
- [ ] 实现一个 `make_counter()` 函数——返回一个函数，每次调用计数 +1 并返回当前值。你需要用到 `nonlocal`，否则会报错。想想为什么
- [ ] 在循环中创建闭包：用循环创建 5 个函数，每个函数应该打印自己的序号。直接写，观察结果是否符合预期。**思考**：如果结果不对，这和 JS 中 `var` 在循环中的经典陷阱是同一个问题吗？怎么修？
- [ ] 实现一个 `make_logger(prefix)` —— 返回一个函数，调用时输出带前缀的日志
- [ ] **关键理解**：装饰器 `@decorator` 的语法糖本质就是 `func = decorator(func)`。现在你能解释为什么装饰器需要是"接受函数、返回函数"的闭包了吗？

📚 **Key docs**: [Python 作用域与命名空间](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces) | [nonlocal 语句](https://docs.python.org/3/reference/simple_stmts.html#the-nonlocal-statement)
> 作用域文档在"类"章节里（因为类也涉及命名空间），重点读 LEGB 查找顺序的描述；nonlocal 文档很短但精确

### Task 3：构建函数管道（Day 2）

- [ ] 从零实现 `my_map(fn, iterable)`——不使用内置 `map`，手动迭代并应用函数
- [ ] 从零实现 `my_filter(fn, iterable)` 和 `my_reduce(fn, iterable, initial)`
- [ ] 实现 `pipe(*functions)`——接收任意数量的函数，返回一个新函数，依次从左到右执行所有传入的函数。**思考**：管道里前一个函数的输出是后一个函数的输入，怎么保证类型兼容？
- [ ] 实现 `compose(*functions)`——和 pipe 方向相反，从右到左执行
- [ ] 用你的 pipe 组合一个数据处理流程：过滤活跃用户 → 提取姓名 → 排序。**思考**：pipe 和 compose 各自适合什么场景？在数据处理管道中你更倾向用哪个？为什么？
- [ ] **挑战**：实现一个 `memoize(fn)` 缓存函数——对相同参数返回缓存结果而不重复计算。你需要考虑：用什么数据结构存缓存？参数不可哈希怎么办？

📚 **Key docs**: [functools.lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache) | [*args 和 **kwargs](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists)
> 先自己实现 memoize，然后再读 lru_cache 看官方是怎么做的——对比你的方案和官方的差距；*args 是实现 pipe 的关键

### Task 4：生成器与惰性求值（Day 2-3）

- [ ] 写一个普通函数和一个使用 `yield` 的生成器函数，对比它们的返回值类型。**思考**：生成器的返回值为什么不是一个 list？"惰性"意味着什么？
- [ ] 对比列表推导式和生成器表达式（方括号 vs 圆括号）的内存占用。用一个非常大的数据量来测试——观察内存差异
- [ ] 实现一个惰性文件读取器：逐行读取大文件，每次只在内存中保留一行。**思考**：如果文件有 10GB，一次性读入内存会怎样？你的生成器方案为什么能处理？
- [ ] 搜索并实验 `itertools` 中的 `chain`、`islice`、`groupby`。它们分别解决什么问题？
- [ ] 实现一个惰性版的 pipe：用生成器串联多个处理步骤，让整个管道都是惰性求值的
- [ ] **思考**：Python 的 `range()`、`map()`、`filter()` 返回的都是惰性对象而不是列表。这和 JS 的设计选择（Array 方法返回新 Array）有什么权衡？

📚 **Key docs**: [生成器教程](https://docs.python.org/3/tutorial/classes.html#generators) | [itertools 模块](https://docs.python.org/3/library/itertools.html) | [生成器表达式](https://docs.python.org/3/tutorial/classes.html#generator-expressions)
> 生成器教程很短但讲清了核心；itertools 是工具箱，先看 chain/islice/groupby 三个就够

---

## 验收标准

- [ ] 能手写一个闭包，并解释它是如何捕获外层变量的
- [ ] 能解释 `nonlocal` 的作用和必要性
- [ ] 能实现 pipe/compose，并用它们组合数据处理流程
- [ ] 能创建生成器函数并解释惰性求值的优势
- [ ] 能清晰地说出：装饰器为什么本质上是一个接受函数并返回函数的闭包

## 延伸思考

> 在 AI Agent 框架中，工具注册（`@tool`）就是一个装饰器。当你写 `@tool` 修饰一个函数时，框架做了什么？它接收你的原始函数，用闭包包装它（添加元信息、参数校验），然后返回增强后的版本。你能用伪代码描述这个过程吗？这个理解将直接帮助你完成 01 章的装饰器项目。
