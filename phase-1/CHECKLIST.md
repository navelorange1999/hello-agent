# Phase 1 · 基础能力 — 总任务清单

> 预计总耗时：7-10 周 | 14 个项目 | 56 个 Task
> 建议按章节顺序推进，每章内的项目也建议按顺序完成

---

## 进度总览

| 章节 | 项目数 | 状态 |
|------|--------|------|
| 00 Python 基础（JS→Python） | 3 个项目 / 12 Tasks | ⬜ 未开始 |
| 01 Python 高级特性 | 3 个项目 / 12 Tasks | ⬜ 未开始 |
| 02 LLM 核心概念 | 3 个项目 / 12 Tasks | ⬜ 未开始 |
| 03 API 调用实践 | 3 个项目 / 12 Tasks | ⬜ 未开始 |
| 04 向量数据库入门 | 2 个项目 / 8 Tasks | ⬜ 未开始 |

---

## 00 · Python 基础（约 1 周）

### P0-1 数据处理 CLI 工具
- [ ] Task 1: 数据类型速通 — list/dict/set/tuple 对比 JS 对应物
- [ ] Task 2: 推导式与解包 — 列表/字典/集合推导式、解构赋值
- [ ] Task 3: 文件 I/O 与字符串 — with 语句、csv/json 模块、f-string、pathlib
- [ ] Task 4: 整合 CLI 工具 — argparse、数据过滤排序聚合、格式化输出

### P0-2 函数式工具集
- [ ] Task 1: 一等公民函数 — lambda、map/filter/sorted、functools.reduce
- [ ] Task 2: 闭包与作用域 — LEGB 规则、nonlocal、make_counter、循环闭包陷阱
- [ ] Task 3: 函数管道 — 自实现 map/filter/reduce、pipe/compose、memoize
- [ ] Task 4: 生成器 — yield、惰性求值、生成器表达式、itertools

### P0-3 任务管理器
- [ ] Task 1: Python class — __init__/self、classmethod/staticmethod、@property、可见性约定
- [ ] Task 2: 魔术方法与继承 — __str__/__repr__/__eq__/__len__/__getitem__、继承、MRO
- [ ] Task 3: 异常处理 — try/except/else/finally、自定义异常、EAFP vs LBYL、上下文管理器
- [ ] Task 4: 模块化与打包 — 包结构、import 机制、venv/pip、__name__ == "__main__"

---

## 01 · Python 高级特性（约 1-2 周）

### P1 异步网页爬虫
- [ ] Task 1: 理解事件循环 — 手动创建事件循环并运行协程
- [ ] Task 2: 异步 HTTP 请求 — aiohttp + Semaphore 并发控制
- [ ] Task 3: 链接解析与递归爬取 — BFS + visited 集合 + 深度限制
- [ ] Task 4: 异步文件写入与整合 — aiofiles + 优雅退出

### P2 装饰器工具注册框架
- [ ] Task 1: 装饰器基础 — 计时器、带参装饰器、functools.wraps
- [ ] Task 2: 工具注册器 — ToolRegistry + 自动元信息提取
- [ ] Task 3: 参数校验层 — inspect.signature + 类型校验
- [ ] Task 4: 工具路由器 — 名称路由、同步/异步支持、调用日志

### P3 类型安全配置系统
- [ ] Task 1: Pydantic 基础建模 — 嵌套模型、自动校验
- [ ] Task 2: 文件加载与序列化 — YAML/JSON 加载、JSON Schema 生成
- [ ] Task 3: 环境变量与敏感信息 — Pydantic Settings、密钥安全
- [ ] Task 4: 配置热更新与通知 — Observer 模式、配置 diff

---

## 02 · LLM 核心概念（约 2-3 周）

### P4 Tokenizer 探索器
- [ ] Task 1: 理解 BPE 算法 — 手动模拟合并、tiktoken 使用
- [ ] Task 2: 多模型 Tokenizer 对比 — GPT-4 vs Claude vs LLaMA
- [ ] Task 3: Token 可视化工具 — CLI 彩色标注、ID 映射
- [ ] Task 4: 成本计算与优化 — 定价表、token 节省技巧

### P5 Attention 可视化器
- [ ] Task 1: 手动计算 Attention — NumPy 实现 QKV 矩阵运算
- [ ] Task 2: Attention 矩阵可视化 — matplotlib 热力图
- [ ] Task 3: 预训练模型的真实 Attention — Hugging Face 模型 + bertviz
- [ ] Task 4: Multi-Head 分析 — 不同 head 的关注模式

### P6 Prompt 实验室
- [ ] Task 1: Prompt 基础实验 — Zero/One/Few-shot 对比
- [ ] Task 2: Chain-of-Thought 实验 — CoT + Self-Consistency
- [ ] Task 3: 参数空间探索 — Temperature / Top-p 系统实验
- [ ] Task 4: Prompt 模板系统 — Jinja2 模板 + 自动评估

---

## 03 · API 调用实践（约 2 周）

### P7 终端聊天 CLI
- [ ] Task 1: API 初体验 — Anthropic SDK、Request/Response 结构
- [ ] Task 2: 多轮对话管理 — 历史维护、上下文窗口、截断策略
- [ ] Task 3: System Prompt 与角色 — 动态角色切换
- [ ] Task 4: CLI 交互完善 — 命令系统、token 统计、异常处理

### P8 流式输出 UI
- [ ] Task 1: 理解 SSE 协议 — 事件类型、完整事件序列
- [ ] Task 2: 终端流式渲染 — 逐字输出、中断处理
- [ ] Task 3: Web 流式界面 — FastAPI SSE + 前端 EventSource
- [ ] Task 4: 流式进阶 — Tool Use 事件解析

### P9 弹性 API 客户端
- [ ] Task 1: 重试策略 — 指数退避 + Jitter
- [ ] Task 2: 熔断器模式 — 三态状态机
- [ ] Task 3: 多模型 Fallback — 优先级列表 + 格式转换层
- [ ] Task 4: 可观测性与成本追踪 — metrics 聚合、限流器

---

## 04 · 向量数据库入门（约 2 周）

### P10 Embedding 实验场
- [ ] Task 1: Embedding 初体验 — API 调用、余弦相似度
- [ ] Task 2: 相似度计算与排序 — 三种度量对比
- [ ] Task 3: 向量空间可视化 — PCA/t-SNE 降维、聚类观察
- [ ] Task 4: Embedding 模型对比 — 跨模型评估、局限性分析

### P11 本地知识库（Mini RAG）— 🎓 毕业项目
- [ ] Task 1: 文档加载与切分 — 多策略对比、overlap
- [ ] Task 2: 向量存储 — ChromaDB + metadata + 增量更新
- [ ] Task 3: 检索与问答 — RAG 流程、引用溯源
- [ ] Task 4: 评估与优化 — Recall@K、Query 改写、Reranking

---

## 阶段完成检查

Phase 1 完成后，确认你能做到以下所有事项：

- [ ] 能熟练使用 Python 的核心数据结构和惯用法
- [ ] 能用闭包和高阶函数组合数据处理流程
- [ ] 能熟练使用 async/await 处理并发 I/O
- [ ] 能用装饰器实现工具注册模式（这是 Agent 框架的核心）
- [ ] 能解释 Transformer Attention 的核心直觉
- [ ] 能评估 Token 消耗并估算 API 成本
- [ ] 能独立设计并迭代 Prompt
- [ ] 能完成 API 的流式调用和错误处理
- [ ] 能构建一个基础的 RAG 问答系统
- [ ] 有一份自己写的学习笔记（不是复制粘贴的）

**全部完成后，你就具备了进入 Phase 2（Agent 框架与模式）的基础。**
