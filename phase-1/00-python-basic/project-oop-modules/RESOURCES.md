# P0-3 任务管理器 — 学习资源

## 核心文档（必读）

1. **[类教程](https://docs.python.org/3/tutorial/classes.html)**
   Python 面向对象的入门教程。重点：§9.3 初识类（__init__、self）、§9.4 补充说明（继承、多继承）、§9.5 继承。这是建立 Python OOP 心智模型的最好起点。

2. **[数据模型 — 特殊方法名称](https://docs.python.org/3/reference/datamodel.html#special-method-names)**
   Python 魔术方法的完整参考。不需要全部读完——先掌握 __str__、__repr__、__eq__、__hash__、__len__、__getitem__、__iter__，其他按需查阅。

3. **[模块教程](https://docs.python.org/3/tutorial/modules.html)**
   重点读 §6.4 包（Packages），理解 __init__.py 和导入机制。

## 按 Task 的推荐阅读

### Task 1 — Python class
- [类教程 §9.3](https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes) — __init__、self、实例变量 vs 类变量
- [property()](https://docs.python.org/3/library/functions.html#property) — 理解描述符协议的简化版
- [classmethod vs staticmethod](https://docs.python.org/3/library/functions.html#classmethod) — 两个文档放在一起对比读

### Task 2 — 魔术方法与继承
- [数据模型 §3.3.1 基本定制](https://docs.python.org/3/reference/datamodel.html#basic-customization) — __repr__、__str__、__eq__、__hash__ 在这里
- [数据模型 §3.3.7 容器模拟](https://docs.python.org/3/reference/datamodel.html#emulating-container-types) — __len__、__getitem__、__iter__
- [super()](https://docs.python.org/3/library/functions.html#super) — 搭配 MRO 一起理解
- [Python's super() considered super!](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/) — Raymond Hettinger 的经典博客，深入理解 super 和 MRO

### Task 3 — 异常处理
- [错误和异常教程](https://docs.python.org/3/tutorial/errors.html) — 从头到尾读，特别注意 else 子句
- [内置异常层级](https://docs.python.org/3/library/exceptions.html#exception-hierarchy) — 理解为什么自定义异常要继承 Exception
- [with 语句](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement) — 上下文管理器协议
- [Python 术语表 — EAFP](https://docs.python.org/3/glossary.html#term-EAFP) — 官方对 EAFP 编程风格的定义

### Task 4 — 模块化与打包
- [模块教程 §6.4 包](https://docs.python.org/3/tutorial/modules.html#packages) — __init__.py、相对导入
- [模块搜索路径](https://docs.python.org/3/tutorial/modules.html#the-module-search-path) — 理解 Python 如何找到你的模块
- [venv 模块](https://docs.python.org/3/library/venv.html) — 虚拟环境的官方文档
- [Python 打包指南](https://packaging.python.org/en/latest/tutorials/packaging-projects/) — 标准项目结构

## 延伸资源（可选）

- [abc 模块 — 抽象基类](https://docs.python.org/3/library/abc.html) — 延伸思考题的答案在这里，但先自己想
- [Fluent Python, Ch.11 — Interfaces: From Protocols to ABCs](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/) — 深入理解 Python 的接口设计哲学
- [Real Python — Python Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/) — 比官方文档更友好的 venv 教程
