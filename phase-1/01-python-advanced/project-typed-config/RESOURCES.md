# Project: 类型安全的配置系统 — 学习资源

## 核心文档（必读）

1. **[Pydantic v2 官方文档](https://docs.pydantic.dev/)** — BaseModel 定义、校验、序列化的核心 API
2. **[Python 类型标注 (typing 模块)](https://docs.python.org/3/library/typing.html)** — Optional、List、Dict 等类型标注的用法
3. **[dataclasses vs Pydantic 对比](https://docs.python.org/3/library/dataclasses.html)** — 理解不同数据结构工具的适用场景

---

## 按 Task 的推荐阅读

### Task 1 — Pydantic 基础建模（Day 1）
- **[Pydantic BaseModel 基础](https://docs.pydantic.dev/latest/concepts/models/)** — 定义模型、字段校验、默认值设置
- **[Pydantic 字段验证](https://docs.pydantic.dev/latest/concepts/fields/)** — 使用 `Field()` 添加约束、描述、示例
- **[嵌套模型与列表](https://docs.pydantic.dev/latest/concepts/models/#nested-models)** — 实现多层配置结构（AgentConfig 包含 LLMConfig 列表）

### Task 2 — 文件加载与序列化（Day 1-2）
- **[Pydantic JSON 序列化](https://docs.pydantic.dev/latest/concepts/json_schema/)** — `model_dump()` 导出、`model_json_schema()` 生成 JSON Schema
- **[Python json 模块](https://docs.python.org/3/library/json.html)** — 读写 JSON 文件
- **[Python YAML 支持](https://docs.python.org/3/library/configparser.html)** — 加载 YAML 配置文件的方法（使用第三方库 PyYAML）

### Task 3 — 环境变量与敏感信息（Day 2）
- **[Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)** — 从环境变量读取配置、优先级管理
- **[os.environ 访问环境变量](https://docs.python.org/3/library/os.html#os.environ)** — Python 与系统环境变量的交互
- **[SecretStr 隐藏敏感信息](https://docs.pydantic.dev/latest/concepts/types/#secret-types)** — 打印配置时自动脱敏 API Key

### Task 4 — 配置热更新与通知（Day 2-3）
- **[观察者模式（Observer Pattern）](https://docs.python.org/3/howto/descriptor.html)** — 实现配置变更订阅通知的设计模式
- **[dict.diff 和对象对比](https://docs.python.org/3/library/difflib.html)** — 计算两个配置版本的差异
- **[__repr__ 和 __str__ 自定义](https://docs.python.org/3/reference/datamodel.html#object.__repr__)** — 控制对象的字符串表示，隐藏敏感字段

---

## 延伸资源（可选）

- **[Python 属性装饰器 @property](https://docs.python.org/3/library/functions.html#property)** — 在配置类中实现只读或计算属性
- **[Pydantic 自定义校验器](https://docs.pydantic.dev/latest/concepts/validators/)** — 超越基础类型检查，实现复杂的业务规则验证
- **[Pydantic 配置类 Config](https://docs.pydantic.dev/latest/api/config/)** — 控制模型的序列化行为、冻结字段等高级特性
- **[JSON Schema 规范](https://json-schema.org/)** — 深入理解 Pydantic 生成的 Schema 如何映射到 Function Calling 参数定义
