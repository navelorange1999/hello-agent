# Project: 类型安全的配置系统

## 为什么做这个项目？

Agent 系统有大量配置：模型名称、温度参数、最大 token 数、API key、工具列表……这些配置如果用 `dict` 随意传递，很容易出现拼写错误、类型错误、缺失字段等问题，而且要到运行时才能发现。

**Pydantic + 类型标注** 是当前 Agent 生态中处理配置和数据校验的标准方案。LangChain、CrewAI、Anthropic SDK 都在大量使用。

---

## 项目目标

构建一个 Agent 配置管理系统：

1. 用 Pydantic 定义多层嵌套的配置模型
2. 支持从 YAML/JSON 文件加载配置
3. 自动校验、类型转换和默认值填充
4. 支持环境变量覆盖敏感配置（如 API Key）
5. 配置变更时自动通知（Observer 模式）

---

## 任务拆解

### Task 1：Pydantic 基础建模（Day 1）

- [ ] 定义一个 `LLMConfig` 模型（model_name, temperature, max_tokens 等）
- [ ] 定义一个 `ToolConfig` 模型（name, enabled, timeout 等）
- [ ] 定义顶层 `AgentConfig`，嵌套包含 LLM 和 Tool 配置列表
- [ ] 体验 Pydantic 的自动校验：传入错误类型看看报什么错
- [ ] **对比**：`dataclass` vs `TypedDict` vs `Pydantic BaseModel`，各自的适用场景

### Task 2：文件加载与序列化（Day 1-2）

- [ ] 实现从 YAML 文件加载配置并解析为 Pydantic 模型
- [ ] 实现从 JSON 文件加载
- [ ] 实现将当前配置导出为 YAML/JSON
- [ ] 加入 `pydantic.Field` 的 description，使配置自带文档
- [ ] **思考**：Pydantic 的 `model_json_schema()` 输出的 JSON Schema 和 OpenAI Function Calling 的参数 schema 有什么关系？

### Task 3：环境变量与敏感信息（Day 2）

- [ ] 使用 Pydantic Settings 从环境变量读取 API Key
- [ ] 实现配置优先级：环境变量 > 配置文件 > 默认值
- [ ] 在 `__repr__` 中自动隐藏敏感字段（不打印 API Key）
- [ ] **笔记**：Agent 项目中如何安全管理密钥？了解 `.env` + `python-dotenv` 的实践

### Task 4：配置热更新与通知（Day 2-3）

- [ ] 实现一个 `ConfigManager` 类，支持运行时修改配置
- [ ] 用 Observer 模式：配置变更时通知所有订阅者
- [ ] 实现配置 diff：对比两个配置版本的差异
- [ ] **延伸**：如果一个正在运行的 Agent 的 temperature 被动态修改了，Agent 应该怎么响应？

---

## 验收标准

- [ ] 配置文件有一个字段拼错或类型错误时，加载阶段就能报出清晰的错误
- [ ] API Key 从环境变量读取，打印配置时不会泄露
- [ ] 能生成配置的 JSON Schema（这就是 Function Calling 参数定义的原理）
- [ ] 能向别人解释：为什么 Agent 框架都用 Pydantic 而不是普通 dict？

## 延伸思考

> 去看看 Anthropic Python SDK 的源码中是怎么定义 Message、Tool、Content 等数据结构的。你会发现它们全是 Pydantic 模型。理解了这个，你就理解了 SDK 的骨架。
