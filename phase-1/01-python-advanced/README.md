# 01 · Python 高级特性

> 为什么先学这个？因为 AI Agent 的核心实现依赖 async 并发、装饰器模式和类型系统。
> 不掌握这些，后面写 Agent 代码会处处碰壁。

## 学习目标

完成本章后，你应该能回答：

1. `async/await` 和多线程有什么本质区别？事件循环是怎么调度协程的？
2. 装饰器的本质是什么？为什么 LangChain 用 `@tool` 装饰器来定义工具？
3. 类型标注在大型项目中解决了什么问题？`TypedDict`、`Generic`、`Protocol` 分别用在什么场景？

## 包含项目

| 序号 | 项目 | 核心知识点 | 预计耗时 |
|------|------|-----------|---------|
| P1 | [异步爬虫](./project-async-crawler/) | async/await, aiohttp, asyncio.gather, 信号量控制 | 3-4 天 |
| P2 | [装饰器框架](./project-decorator-framework/) | 装饰器、闭包、functools、元编程 | 2-3 天 |
| P3 | [类型安全配置系统](./project-typed-config/) | TypedDict, Pydantic, Generic, dataclass | 2-3 天 |

## 推荐阅读顺序

1. Python 官方文档 — [Coroutines and Tasks](https://docs.python.org/3/library/asyncio-task.html)
2. Real Python — [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
3. Python 官方文档 — [typing 模块](https://docs.python.org/3/library/typing.html)
4. Pydantic 官方文档 — [Getting Started](https://docs.pydantic.dev/latest/)
