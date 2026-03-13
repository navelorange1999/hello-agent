# Project: 流式输出 UI — 学习资源

## 核心文档（必读）

1. **[Anthropic Streaming 官方文档](https://docs.anthropic.com/docs/guides/streaming)** — 必读，理解 Server-Sent Events (SSE) 格式、所有事件类型及其含义

2. **[Server-Sent Events (SSE) 规范](https://html.spec.whatwg.org/multipage/server-sent-events.html)** — W3C 标准，理解 SSE 的底层协议和事件格式

3. **[FastAPI 流式响应指南](https://fastapi.tiangolo.com/advanced/streaming-responses/)** — 学习如何在后端转发 Anthropic 的流式响应

## 按 Task 的推荐阅读

### Task 1 — 理解 SSE 协议

- **[Anthropic SDK - Streaming API](https://docs.anthropic.com/docs/guides/streaming)** — 重点学习 `stream()` 方法、事件类型列表（message_start、content_block_delta、content_block_stop、message_stop 等）
- **[SSE 事件格式详解](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events)** — 理解 `id:`、`event:`、`data:` 等字段含义，为解析事件做准备

### Task 2 — 终端流式渲染

- **[Python asyncio 流处理](https://docs.python.org/3/library/asyncio.html#tasks)** — 学习如何异步迭代 Anthropic 流式事件，避免阻塞 UI
- **[Terminal Output 最佳实践](https://docs.anthropic.com/docs/guides/streaming)** — 理解如何逐字符输出、处理 Ctrl+C 中断、提取 usage 信息

### Task 3 — Web 流式界面

- **[FastAPI SSE 端点实现](https://fastapi.tiangolo.com/advanced/streaming-responses/)** — 学习如何在 FastAPI 中创建 SSE 端点，转发 Anthropic 流式数据
- **[JavaScript EventSource API](https://developer.mozilla.org/en-US/docs/Web/API/EventSource)** — 理解前端如何接收 SSE 事件，实时渲染流式内容

### Task 4 — 流式进阶：Tool Use 事件

- **[Anthropic Tool Use 指南](https://docs.anthropic.com/docs/guides/tool-use)** — 重点关注流式模式下 tool_use 事件的处理，与非流式模式的事件序列差异
- **[Streaming with Tool Use](https://docs.anthropic.com/docs/guides/streaming#tool-use-streaming)** — 理解 `content_block_start`（type=tool_use）事件的含义，如何在流式过程中识别工具调用

## 延伸资源（可选）

- **[Anthropic Cookbook - 流式示例](https://github.com/anthropic-ai/anthropic-cookbook)** — 查看官方流式实现示例，特别是结合 Tool Use 的场景
- **[WebSocket vs SSE 对比](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)** — 理解为什么 Agent 界面更常用 SSE 而不是 WebSocket
