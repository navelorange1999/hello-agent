# 03 · API 调用实践

> Agent 的"手"就是 API 调用。不管你的架构设计多精妙，最终都要通过 API 和 LLM 通信。
> 流式输出、错误重试、并发管理——这些是 Agent 稳定运行的保障。

## 学习目标

完成本章后，你应该能回答：

1. OpenAI 和 Anthropic 的 API 在消息格式上有什么核心区别？
2. 流式输出（Streaming）的原理是什么？为什么 Agent 需要它？
3. 生产环境中，API 调用的重试、超时、降级策略应该怎么设计？

## 包含项目

| 序号 | 项目 | 核心知识点 | 预计耗时 |
|------|------|-----------|---------|
| P1 | [终端聊天 CLI](./project-chat-cli/) | SDK 基础、消息格式、多轮对话管理 | 2-3 天 |
| P2 | [流式输出 UI](./project-streaming-ui/) | SSE 协议、流式解析、实时渲染 | 2-3 天 |
| P3 | [弹性 API 客户端](./project-resilient-client/) | 重试策略、熔断、降级、连接池 | 3-4 天 |

## 推荐阅读顺序

1. Anthropic — [Messages API Reference](https://docs.anthropic.com/en/api/messages)
2. OpenAI — [Chat Completions API](https://platform.openai.com/docs/api-reference/chat)
3. Anthropic — [Streaming Messages](https://docs.anthropic.com/en/api/messages-streaming)
4. Microsoft — [Retry Pattern (Cloud Design Patterns)](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry)
