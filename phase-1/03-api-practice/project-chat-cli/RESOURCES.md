# Project: 终端聊天 CLI — 学习资源

## 核心文档（必读）

1. **[Anthropic API 概览](https://docs.anthropic.com/docs/overview)** — 了解 Anthropic 与其他 LLM API 的消息格式区别（特别是 role 类型和 content 结构）

2. **[Anthropic Python SDK 文档](https://github.com/anthropic-ai/anthropic-python)** — 学习 `Anthropic` 客户端初始化和基础 API 调用方式

3. **[OpenAI API 对比参考](https://platform.openai.com/docs/guides/chat-completions)** — 对标学习，加深对不同 API 设计哲学的理解

## 按 Task 的推荐阅读

### Task 1 — API 初体验

- **[Anthropic API - 发送消息](https://docs.anthropic.com/docs/guides/basic-requests)** — 重点关注 Request 和 Response 的完整结构，理解每个字段的含义（message id、content、model、usage 等）
- **[API 计费与 Token 计算](https://docs.anthropic.com/docs/about/pricing)** — 理解 input/output token 如何计算，对应的成本

### Task 2 — 多轮对话管理

- **[Anthropic API - 多轮对话](https://docs.anthropic.com/docs/guides/multi-turn-conversations)** — 学习如何维护消息历史列表、什么时候应该截断、上下文窗口限制
- **[Token 计数指南](https://docs.anthropic.com/docs/guides/token-counting)** — 理解如何估算单次对话的 token 消耗，设计合理的截断策略

### Task 3 — System Prompt 与角色

- **[System Prompts 最佳实践](https://docs.anthropic.com/docs/guides/system-prompts)** — 学习为什么 Agent 的 System Prompt 通常很长且结构化，如何有效编写
- **[提示词工程基础](https://docs.anthropic.com/docs/guides/prompt-optimization)** — 理解不同 System Prompt 对模型行为的影响机制

### Task 4 — CLI 交互完善

- **[错误处理与速率限制](https://docs.anthropic.com/docs/guides/rate-limiting)** — 学习处理 API Key 无效、Rate Limit（429）、超时等异常场景
- **[异步编程与超时控制](https://docs.anthropic.com/docs/guides/async-requests)** — 理解如何实现请求级的超时控制和优雅中断

## 延伸资源（可选）

- **[Anthropic Cookbook - 聊天示例](https://github.com/anthropic-ai/anthropic-cookbook)** — 查看官方示例代码，学习生产级的 CLI 实现细节
- **[Claude 模型对比表](https://docs.anthropic.com/docs/models/overview)** — 了解不同模型的能力差异、token limit、成本，为切换模型功能做准备
