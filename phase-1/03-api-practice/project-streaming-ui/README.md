# Project: 流式输出 UI

## 为什么做这个项目？

用过 ChatGPT 或 Claude，你会注意到回复是"一个字一个字蹦出来"的，而不是等全部生成完才显示。这就是流式输出（Streaming）。对 Agent 来说，流式输出不只是用户体验的优化——它还允许 Agent 在生成过程中做出中间判断和干预。

---

## 项目目标

构建一个支持流式输出的聊天界面：

1. 使用 Anthropic Streaming API 接收逐步生成的内容
2. 解析 Server-Sent Events (SSE) 中的不同事件类型
3. 实现 Token 级别的实时渲染
4. 支持流式过程中的取消操作

---

## 任务拆解

### Task 1：理解 SSE 协议（Day 1）

- [ ] 阅读 Anthropic Streaming 文档，理解 SSE 的基本格式
- [ ] 用 Anthropic SDK 的 stream 模式发送一个请求
- [ ] 打印每个 event 的原始数据，弄清事件类型：`message_start`, `content_block_delta`, `message_stop` 等
- [ ] 记录一次完整流式响应的所有事件序列
- [ ] **笔记**：画出流式响应的事件时序图

### Task 2：终端流式渲染（Day 1-2）

- [ ] 实现逐字符输出到终端（不换行，实时追加）
- [ ] 正确处理 `content_block_delta` 中的文本片段拼接
- [ ] 在流结束后提取完整的 usage 信息
- [ ] 实现 Ctrl+C 优雅中断：停止接收但保留已生成的内容
- [ ] **思考**：为什么 Agent 框架中，流式输出对 Tool Calling 的处理特别复杂？

### Task 3：Web 流式界面（Day 2-3）

- [ ] 用 FastAPI（或 Flask）搭建一个简单的后端
- [ ] 实现 SSE 端点：将 Anthropic 的流式响应转发给前端
- [ ] 用简单的 HTML + JavaScript 实现前端流式渲染（EventSource API）
- [ ] 支持多轮对话的界面展示
- [ ] **延伸**：加入 "正在输入..." 的打字机效果指示器

### Task 4：流式进阶——Tool Use 事件（Day 3）

- [ ] 阅读 Anthropic 文档中 Streaming 与 Tool Use 结合的部分
- [ ] 理解流式响应中 `content_block_start`（type=tool_use）事件的含义
- [ ] 模拟一个带 tool_use 的流式场景，观察事件序列的变化
- [ ] **笔记**：在流式模式下，Agent 怎么知道 LLM 想要调用工具？事件序列和非流式模式有什么不同？

---

## 验收标准

- [ ] 终端和 Web 界面都能实现逐字输出效果
- [ ] 能正确解析所有 SSE 事件类型并做出相应处理
- [ ] 流式过程中可以取消，不会残留未处理的连接
- [ ] 能解释：流式输出在 Agent 架构中的角色和挑战

## 延伸思考

> Claude Code（你正在使用的这个工具）就是一个典型的流式 Agent。它一边生成文本一边决定是否调用工具。想想这背后的流式事件处理有多复杂。
