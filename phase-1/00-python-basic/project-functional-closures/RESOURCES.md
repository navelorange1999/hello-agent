# P0-2 函数式工具集 — 学习资源

## 核心文档（必读）

1. **[函数式编程 HOWTO](https://docs.python.org/3/howto/functional.html)**
   Python 官方对函数式编程的定位说明。重点读前三节：迭代器、生成器、内置函数。这篇文档会帮你理解 Python 不是一门纯函数式语言——它是怎么选择性地采纳函数式特性的。

2. **[functools 模块](https://docs.python.org/3/library/functools.html)**
   重点关注 `reduce`、`partial`、`lru_cache`、`wraps`。其中 `wraps` 在 01 章的装饰器项目中会大量使用。

3. **[itertools 模块](https://docs.python.org/3/library/itertools.html)**
   Python 的迭代器工具箱。本项目只需掌握 `chain`、`islice`、`groupby`，但浏览一遍全部函数能让你知道"有哪些现成的轮子"。

## 按 Task 的推荐阅读

### Task 1 — 一等公民函数
- [lambda 表达式](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions) — 注意文档中对 lambda 限制的说明
- [内置函数 map/filter](https://docs.python.org/3/library/functions.html#map) — 看返回值类型（是迭代器，不是列表）

### Task 2 — 闭包与作用域
- [作用域与命名空间](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces) — 虽然在"类"章节里，但这是理解 LEGB 的最好材料
- [nonlocal 语句](https://docs.python.org/3/reference/simple_stmts.html#the-nonlocal-statement) — 短小精悍，搭配 global 语句一起读
- [PEP 3104 — nonlocal 语句](https://peps.python.org/pep-3104/) — 想深入了解 nonlocal 为什么被引入的设计背景

### Task 3 — 函数管道
- [*args 和 **kwargs](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists) — 实现 pipe 和 compose 的基础
- [functools.reduce](https://docs.python.org/3/library/functools.html#functools.reduce) — 你可以用 reduce 来实现 pipe
- [functools.lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache) — 自己实现 memoize 后，对照官方版本看差距

### Task 4 — 生成器
- [生成器](https://docs.python.org/3/tutorial/classes.html#generators) + [生成器表达式](https://docs.python.org/3/tutorial/classes.html#generator-expressions) — 官方教程的两小节，简洁清晰
- [yield 表达式](https://docs.python.org/3/reference/expressions.html#yield-expressions) — 更完整的参考，包括 send() 和 throw()
- [itertools — chain/islice/groupby](https://docs.python.org/3/library/itertools.html) — 先掌握这三个

## 延伸资源（可选）

- [David Beazley — Generator Tricks for Systems Programmers](http://www.dabeaz.com/generators/) — 经典演讲，展示生成器在真实场景中的威力
- [Guido van Rossum on why reduce was removed from builtins](https://www.artima.com/weblogs/viewpost.jsp?thread=98196) — 理解 Python 对函数式编程的取舍
