# Project: 装饰器工具注册框架 — 学习资源

## 核心文档（必读）

1. **[装饰器官方文档](https://docs.python.org/3/glossary.html#term-decorator)** — 理解装饰器的定义和语法糖本质
2. **[functools 模块](https://docs.python.org/3/library/functools.html)** — 重点学习 `@wraps` 保留函数元信息
3. **[inspect 模块](https://docs.python.org/3/library/inspect.html)** — 获取函数签名、参数、文档字符串

---

## 按 Task 的推荐阅读

### Task 1 — 装饰器基础（Day 1）
- **[函数装饰器详解](https://docs.python.org/3/glossary.html#term-decorator)** — 从最简单的包装函数开始，理解闭包和函数作用域
- **[functools.wraps 保留元信息](https://docs.python.org/3/library/functools.html#functools.wraps)** — 为什么需要 `@wraps`，不用会怎样
- **[参数化装饰器](https://docs.python.org/3/faq/programming.html#what-are-decorators)** — 装饰器的参数化实现：三层嵌套函数的设计

### Task 2 — 工具注册器（Day 1-2）
- **[inspect.signature 获取函数签名](https://docs.python.org/3/library/inspect.html#inspect.signature)** — 提取参数名、类型标注、默认值
- **[`__name__` 和 `__doc__` 属性](https://docs.python.org/3/library/stdtypes.html#definition.__doc__)** — 函数的元信息提取和保留
- **[字典作为注册表](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)** — 用 dict 存储和管理工具

### Task 3 — 参数校验层（Day 2）
- **[inspect.Parameter 和类型检查](https://docs.python.org/3/library/inspect.html#inspect.Parameter)** — 获取参数的类型标注并进行校验
- **[isinstance() 类型检查](https://docs.python.org/3/library/functions.html#isinstance)** — 运行时验证参数类型
- **[异常处理与错误消息](https://docs.python.org/3/library/exceptions.html)** — 自定义异常类传递清晰的校验错误

### Task 4 — 工具路由器（Day 3）
- **[asyncio.iscoroutinefunction 检测异步函数](https://docs.python.org/3/library/asyncio-task.html#asyncio.iscoroutinefunction)** — 区分同步与异步工具
- **[inspect.iscoroutinefunction 替代方案](https://docs.python.org/3/library/inspect.html#inspect.iscoroutinefunction)** — 检测协程函数的另一种方式
- **[time.perf_counter 精确计时](https://docs.python.org/3/library/time.html#time.perf_counter)** — 测量函数执行耗时

---

## 延伸资源（可选）

- **[typing 模块与类型标注](https://docs.python.org/3/library/typing.html)** — 深入理解 Type Hints 和泛型编程
- **[类方法装饰器 @classmethod 和 @staticmethod](https://docs.python.org/3/library/functions.html#classmethod)** — 装饰器在类中的应用
- **[property 装饰器](https://docs.python.org/3/library/functions.html#property)** — 属性与方法的装饰器实现
- **[json.dumps 序列化](https://docs.python.org/3/library/json.html#json.dumps)** — 将工具元信息序列化为 JSON Schema 格式
