# Project: 弹性 API 客户端 — 学习资源

## 核心文档（必读）

1. **[Anthropic 错误处理与重试](https://docs.anthropic.com/docs/guides/rate-limiting)** — 理解可重试错误（429、5xx）与不可重试错误（401、400）的区别

2. **[指数退避与 Jitter 模式](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/)** — AWS 经典博文，理解为什么需要 Jitter 避免"惊群效应"

3. **[熔断器模式（Circuit Breaker）](https://martinfowler.com/bliki/CircuitBreaker.html)** — Martin Fowler 经典文章，理解三个状态（Closed、Open、Half-Open）的设计意图

## 按 Task 的推荐阅读

### Task 1 — 重试策略

- **[Exponential Backoff with Jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/)** — 重点关注 Jitter 的几种实现方式（full jitter vs equal jitter），理解它如何分散请求时间
- **[Anthropic Rate Limiting](https://docs.anthropic.com/docs/guides/rate-limiting)** — 学习 429 和 529 状态码的含义，什么样的重试策略对 Anthropic API 最合适

### Task 2 — 熔断器模式

- **[Circuit Breaker Pattern](https://martinfowler.com/bliki/CircuitBreaker.html)** — 必读，理解三个状态的转移条件、冷却时间的作用
- **[熔断器实现案例](https://github.com/pybreaker/pybreaker)** — 参考 pybreaker 库的实现，学习如何跟踪失败次数和状态转移

### Task 3 — 多模型 Fallback

- **[Anthropic vs OpenAI 消息格式](https://docs.anthropic.com/docs/overview)** — 学习不同 API 的消息格式差异，为 Fallback 时的格式转换做准备
- **[Model Fallback 架构](https://cloud.google.com/architecture/patterns-for-resilient-applications)** — 理解如何设计优先级列表、什么时候触发 Fallback、如何记录 Fallback 日志

### Task 4 — 可观测性与成本追踪

- **[分布式追踪与 Request ID](https://www.w3.org/TR/trace-context/)** — 学习如何用 request_id 追踪调用链，便于调试
- **[Token Bucket 限流器](https://en.wikipedia.org/wiki/Token_bucket)** — 理解如何实现并发限流，保护 API 配额；对比 Sliding Window 的优缺点

## 延伸资源（可选）

- **[Resilience4j - Java 弹性库](https://resilience4j.readme.io/)** — 参考业界成熟的弹性设计，即使是 Java 库也能学到架构思想
- **[LangChain ChatAnthropic 实现](https://github.com/langchain-ai/langchain)** — 查看开源 Agent 框架在可靠性方面的实现细节
- **[Prometheus 监控指标](https://prometheus.io/docs/concepts/metric_types/)** — 学习如何定义可监控的指标（Gauge、Counter、Histogram），为后续接入监控系统做准备
