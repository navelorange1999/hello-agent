# Project: 异步网页爬虫 — 学习资源

## 核心文档（必读）

1. **[asyncio 官方文档](https://docs.python.org/3/library/asyncio.html)** — 重点理解事件循环、协程、任务调度机制
2. **[asyncio.gather() 和 asyncio.create_task()](https://docs.python.org/3/library/asyncio-task.html)** — 并发执行的两种方式及差异
3. **[asyncio.Semaphore](https://docs.python.org/3/library/asyncio-sync.html#semaphore)** — 并发控制的核心工具

---

## 按 Task 的推荐阅读

### Task 1 — 理解事件循环（Day 1）
- **[asyncio 事件循环基础](https://docs.python.org/3/library/asyncio-eventloop.html)** — 了解 `asyncio.run()` 和事件循环的生命周期
- **[asyncio.gather() vs create_task() 对比](https://docs.python.org/3/library/asyncio-task.html#creating-tasks)** — 区分"等待所有结果"与"后台调度"
- **[await 关键字](https://docs.python.org/3/library/asyncio.html#awaitable-objects)** — 理解为什么 await 必须在异步函数中使用

### Task 2 — 异步 HTTP 请求（Day 1-2）
- **[asyncio 网络编程](https://docs.python.org/3/library/asyncio-protocol.html)** — 异步 I/O 的底层原理
- **[asyncio.Semaphore 信号量](https://docs.python.org/3/library/asyncio-sync.html#semaphore)** — 如何限制并发数避免资源耗尽
- **[asyncio.TimeoutError 异常处理](https://docs.python.org/3/library/asyncio.html#asyncio.timeout)** — 优雅处理超时和错误

### Task 3 — 链接解析与递归爬取（Day 2-3）
- **[asyncio 队列与集合](https://docs.python.org/3/library/asyncio-queue.html)** — 用 Queue 实现 BFS 爬取的待处理列表
- **[set 去重机制](https://docs.python.org/3/library/stdtypes.html#set)** — 维护已访问链接集合，避免重复爬取
- **[正则表达式提取 URL](https://docs.python.org/3/library/re.html)** — 从 HTML 中解析链接的核心工具

### Task 4 — 异步文件写入与整合（Day 3-4）
- **[asyncio 任务取消与清理](https://docs.python.org/3/library/asyncio-task.html#creating-tasks)** — 优雅处理中断（KeyboardInterrupt）和任务清理
- **[json 模块](https://docs.python.org/3/library/json.html)** — 序列化爬取结果为 JSON 格式
- **[异步上下文管理器 async with](https://docs.python.org/3/library/asyncio.html#context-managers)** — 异步资源管理的最佳实践

---

## 延伸资源（可选）

- **[asyncio 调试模式](https://docs.python.org/3/library/asyncio.html#debug-mode)** — 使用 `asyncio.run(debug=True)` 诊断常见的异步编程错误
- **[asyncio 性能优化](https://docs.python.org/3/library/asyncio.html#performance)** — 理解事件循环在高并发场景下的表现
- **[concurrent.futures 对比](https://docs.python.org/3/library/concurrent.futures.html)** — 线程池 vs 异步的适用场景
