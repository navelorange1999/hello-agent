# Project: Tokenizer 探索器

## 为什么做这个项目？

Agent 开发中你会频繁遇到这些问题："为什么我的 prompt 超了 token 限制？""为什么同样的内容中文就贵得多？""怎么估算一次调用的成本？"这些问题的答案都在 Tokenizer 里。

---

## 项目目标

构建一个交互式 Tokenizer 分析工具：

1. 可视化不同文本被 tokenize 后的结果
2. 对比不同模型的 tokenizer 差异（GPT-4 vs Claude vs 开源模型）
3. 分析不同语言的 token 效率
4. 实现一个 token 成本计算器

---

## 任务拆解

### Task 1：理解 BPE 算法（Day 1）

- [ ] 阅读 Hugging Face Tokenizers 文档，理解 BPE（Byte Pair Encoding）的原理
- [ ] 手动在纸上模拟 BPE 的合并过程（取一个简单的英文句子）
- [ ] 用 `tiktoken`（OpenAI 的 tokenizer 库）将一段文本 tokenize
- [ ] 将 token ID 解码回文本，观察 token 的边界在哪里
- [ ] **笔记**：BPE 为什么是"子词"级别的？和字符级、词级 tokenization 相比优势在哪？

### Task 2：多模型 Tokenizer 对比（Day 1-2）

- [ ] 安装 `tiktoken`（GPT 系列）和 `transformers`（开源模型）
- [ ] 对同一段文本，分别用 GPT-4、Claude（通过 API 计数）、LLaMA 的 tokenizer 处理
- [ ] 对比 token 数量差异，制作对比表格
- [ ] 测试：同一段话的中文版 vs 英文版 vs 日文版，token 数差多少？
- [ ] **思考**：为什么不同模型的 tokenizer 不一样？这对 Agent 开发有什么实际影响？

### Task 3：Token 可视化工具（Day 2-3）

- [ ] 用 Python 实现一个 CLI 工具：输入文本，输出每个 token 用不同颜色标注
- [ ] 显示每个 token 对应的 ID 和解码文本
- [ ] 支持统计总 token 数和估算 API 调用成本
- [ ] 加入特殊 token 的识别和标注（如 `<|endoftext|>`）
- [ ] **延伸**：用 `rich` 库做终端美化输出，或用 `streamlit` 做 Web 界面

### Task 4：成本计算与优化（Day 3）

- [ ] 实现成本计算器：输入文本 + 模型名 → 输出预估费用
- [ ] 收集主流模型的定价信息，做成配置表
- [ ] 分析：同样的 prompt，怎么改写能减少 token 数但不影响效果？
- [ ] **笔记**：总结 Agent 开发中控制 token 成本的实用技巧

---

## 验收标准

- [ ] 能快速判断一段文本在 GPT-4 和 Claude 下分别消耗多少 token
- [ ] 能解释为什么中文消耗更多 token，以及这对 Agent 的成本意味着什么
- [ ] 能向别人解释 BPE 算法的核心思想（不需要数学推导，但要说清楚直觉）

## 延伸思考

> Agent 在 Multi-turn 对话中，Context Window 是有限的。如果你的 Agent 有 10 轮对话历史 + 5 个工具描述 + RAG 检索结果，怎么在有限的 token 预算内管理这些信息？
