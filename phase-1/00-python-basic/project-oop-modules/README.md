# Project: 任务管理器

## 为什么做这个项目？

AI Agent 框架（LangChain、CrewAI 等）的源码里到处都是类：`BaseAgent`、`BaseTool`、`BaseMessage`。如果你不理解 Python 的 class、继承和魔术方法，阅读这些框架源码就会很痛苦。同时，Python 的模块/包系统和 Node.js 差异很大，这个项目帮你把这些坑提前踩一遍。

---

## 项目目标

构建一个命令行任务管理器，通过这个项目掌握：

1. Python 的 class 定义、继承、魔术方法
2. 异常处理的 Python 惯用法
3. 模块和包的组织方式
4. 虚拟环境和依赖管理

---

## 任务拆解

### Task 1：Python 的 class（Day 1）

- [ ] 定义一个 `Task` 类，包含标题、优先级、完成状态、创建时间。**思考**：JS 的 constructor 里用 `this.x = x`，Python 的 `__init__` 里用 `self.x = x`——看起来一样，但 `self` 必须显式写成第一个参数，这个设计选择背后的理由是什么？（搜索 "explicit self in Python"）
- [ ] 给 Task 类添加实例方法（标记完成、修改优先级）、一个类方法（从字典创建 Task）、一个静态方法（校验标题格式）。**思考**：JS class 里只有 static 和普通方法两种，Python 多了一个 `@classmethod`——它解决了什么问题？什么场景必须用 classmethod 而不是 staticmethod？
- [ ] 用 `@property` 实现一个计算属性（例如：任务已存在的天数）。对比 JS 的 getter/setter，使用体验有什么不同？
- [ ] 尝试给属性名加 `_` 前缀和 `__` 前缀，从外部访问它们。**思考**：Python 没有 `private` 关键字，用命名约定来表达可见性——你觉得这是优点还是缺点？

📚 **Key docs**: [类教程](https://docs.python.org/3/tutorial/classes.html) | [property()](https://docs.python.org/3/library/functions.html#property)
> 类教程是 Python 面向对象的入门必读，重点看 §9.3 初识类 和 §9.4 补充说明；property 文档看描述符协议的简要说明

### Task 2：魔术方法与继承（Day 1-2）

- [ ] 实现 `__str__` 和 `__repr__`，让 `print(task)` 和在 REPL 里直接输入 `task` 显示不同的内容。**思考**：为什么 Python 要区分 `str` 和 `repr`？它们各自的目标受众是谁？
- [ ] 实现 `__eq__`，让两个标题相同的 Task 被认为是相等的。然后尝试把 Task 放进 set——会发生什么？你需要额外实现什么？
- [ ] 创建一个 `TaskList` 类，实现 `__len__`、`__getitem__`、`__iter__`，让它支持 `len()`、下标访问和 for 循环。**思考**：这就是 Python 的"鸭子类型"——只要实现了对应的魔术方法，你的对象就能像内置类型一样使用。这和 JS 的 Symbol.iterator 有什么异同？
- [ ] 创建 `UrgentTask` 子类继承 `Task`，添加 deadline 属性，覆盖显示方法。使用 `super()` 调用父类的 `__init__`
- [ ] 搜索 Python 的多继承和 MRO（方法解析顺序）。**思考**：JS 不支持多继承是因为"菱形问题"，Python 用 C3 线性化解决了这个问题——但多继承在实践中推荐使用吗？

📚 **Key docs**: [数据模型 — 特殊方法](https://docs.python.org/3/reference/datamodel.html#special-method-names) | [super() 函数](https://docs.python.org/3/library/functions.html#super)
> 数据模型文档是 Python 魔术方法的完整参考，先看 __str__/__repr__/__eq__/__hash__ 相关部分；super 文档配合 MRO 一起理解

### Task 3：异常处理（Day 2）

- [ ] 用 `try/except/else/finally` 处理常见错误。**注意**：Python 的 try 有 `else` 分支——它在没有异常时执行。**思考**：JS 的 try/catch 没有 else，Python 为什么加了这个？把"正常逻辑"放在 else 里和放在 try 里有什么区别？
- [ ] 定义自定义异常类（例如 `TaskNotFoundError`）。搜索 Python 异常的继承体系，理解为什么自定义异常要继承 `Exception` 而不是 `BaseException`
- [ ] 搜索 EAFP 和 LBYL 两种编程风格。**思考**：JS 社区倾向于"先检查再操作"（LBYL），Python 社区倾向于"先操作，出错再处理"（EAFP）——为什么？这两种风格各有什么性能和可读性上的权衡？
- [ ] 用 `with` 语句管理文件操作中的资源释放。回顾 P0-1 中使用的 `with`，现在深入理解它背后的上下文管理器协议（`__enter__` 和 `__exit__`）
- [ ] 给任务管理器添加完整的错误处理：文件不存在、JSON 格式错误、任务未找到——每种情况抛出不同的异常

📚 **Key docs**: [错误和异常教程](https://docs.python.org/3/tutorial/errors.html) | [with 语句上下文管理器](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement) | [内置异常层级](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
> 错误教程从头到尾读一遍，特别注意 else 子句；异常层级图谱帮你理解为什么自定义异常继承 Exception

### Task 4：模块化与打包（Day 2-3）

- [ ] 把你的单文件代码重构为多文件包结构。你需要搞清楚：`__init__.py` 是什么？和 Node.js 的 `index.js` 有什么相似和不同？
- [ ] 实验 import 的各种形式：绝对导入、相对导入、从包导入、从模块导入特定名称。**思考**：当你写 `from models import Task` 时，Python 是怎么找到 `models` 这个模块的？搜索 Python 的模块搜索路径
- [ ] 在 `__init__.py` 中使用 `__all__` 控制 `from package import *` 的行为
- [ ] 用 `pip install` 安装一个第三方包（例如 `click`，用来美化 CLI）。然后用 `pip freeze > requirements.txt` 记录依赖。**思考**：和 Node.js 的 `package.json` + `package-lock.json` 相比，Python 的依赖管理方案有什么不足？你听说过 `poetry` 或 `uv` 吗？
- [ ] 理解 `if __name__ == "__main__":` 这个惯用法——它解决了什么问题？
- [ ] 把任务管理器做成可以用 `python -m your_package` 运行的形式，支持 add、list、done、stats 等子命令

📚 **Key docs**: [模块教程](https://docs.python.org/3/tutorial/modules.html) | [Python 打包用户指南](https://packaging.python.org/en/latest/tutorials/packaging-projects/) | [venv 模块](https://docs.python.org/3/library/venv.html)
> 模块教程重点读 §6.4 包（Packages）和 §6.4.1 从包中导入；打包指南帮你理解 Python 项目的标准结构

---

## 验收标准

- [ ] 能定义 class，使用 `__init__`、`self`、继承、`super()`，不看文档就能写出来
- [ ] 能实现至少 3 个魔术方法，让自定义对象支持内置操作
- [ ] 能正确使用 try/except 处理不同类型的异常
- [ ] 能把代码组织成多文件的包结构，import 不报错
- [ ] 能创建虚拟环境、安装依赖、生成 requirements.txt
- [ ] 能向别人解释 Python class 和 JS class 的 3 个关键差异

## 延伸思考

> LangChain 的 `BaseTool` 类要求子类必须实现 `_run()` 方法——如果你不实现，实例化时就会报错。这是用什么机制实现的？搜索 Python 的 `abc.ABC` 和 `@abstractmethod`。如果你的 Task 基类也要强制子类实现某个方法（比如 `estimate_time()`），你会怎么设计？试着用伪代码描述这个结构。
