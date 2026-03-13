# Project: 终端聊天 CLI

## 为什么做这个项目？

这是你第一次真正和 LLM API 交互。通过构建一个终端聊天工具，你会理解 LLM API 的消息格式、角色系统、多轮对话的上下文管理——这些是所有 Agent 的通信基础。

---

## 项目目标

构建一个功能完整的终端聊天工具：

1. 支持与 Anthropic Claude API 进行多轮对话
2. 正确管理对话历史（message 列表的维护）
3. 支持 System Prompt 自定义
4. 支持基础命令（清空历史、切换模型、保存对话等）

---

## 任务拆解

### Task 1：API 初体验（Day 1）

- [ ] 注册 Anthropic API 并获取 API Key
- [ ] 安装 `anthropic` Python SDK
- [ ] 发送第一条消息，理解 Request/Response 的完整结构
- [ ] 打印完整的 response 对象，弄清每个字段的含义（id, content, model, usage 等）
- [ ] **笔记**：对比 Anthropic 和 OpenAI 的消息格式差异（role 类型、content 结构）

### Task 2：多轮对话管理（Day 1-2）

- [ ] 实现对话历史的维护：每轮把 user 和 assistant 消息都追加到列表中
- [ ] 理解 API 的无状态特性：每次请求都要发送完整的对话历史
- [ ] 实现上下文窗口管理：当历史太长时的截断策略
- [ ] 测试：故意发送很长的对话历史，观察 token 用量和费用变化
- [ ] **思考**：Agent 在执行 10 步任务时，对话历史会膨胀得很快。你会怎么控制？

### Task 3：System Prompt 与角色（Day 2）

- [ ] 实现 System Prompt 的设置和切换
- [ ] 测试不同 System Prompt 对模型行为的影响
- [ ] 实现 `/system <prompt>` 命令来动态修改 System Prompt
- [ ] 尝试设计一个 "代码助手" 角色的 System Prompt
- [ ] **思考**：为什么 Agent 的 System Prompt 通常很长且结构化？回顾你在 Prompt 实验室的发现

### Task 4：CLI 交互完善（Day 2-3）

- [ ] 实现命令系统：`/clear`（清空历史）、`/save`（保存对话为 JSON）、`/load`（加载历史对话）
- [ ] 实现 `/model <name>` 命令切换模型
- [ ] 添加 token 用量统计和单次对话的费用估算
- [ ] 处理各种异常：API Key 无效、网络超时、Rate Limit 等
- [ ] **延伸**：实现对话的 Markdown 导出功能

---

## 验收标准

- [ ] 能流畅地与 Claude 进行多轮对话，上下文正确保持
- [ ] 对话历史过长时有合理的处理策略
- [ ] 能清晰解释 API 的消息格式、计费方式和限制
- [ ] 异常情况下（网络断开、Key 过期）不会 crash

## 延伸思考

> 你现在做的这个 CLI 就是最简单的 "Agent"——只是它还没有工具调用能力。想想看，如果要让它能搜索网页、读写文件，你需要在现有架构上增加什么？
