# Prompt 实验室 — 学习资源

## 核心文档（必读）
1. **[Anthropic 官方 Prompt 工程指南](https://docs.anthropic.com/en/docs/build-a-chatbot)** — System Prompt 设计最佳实践、多轮对话管理、以及输出格式控制

2. **[Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903)** — Wei et al. 的经典论文，证明推理链提示能显著提升模型推理能力

3. **[Few-Shot In-Context Learning 概述](https://arxiv.org/abs/2005.14165)** — Brown et al. 的 GPT-3 论文，系统讲解 few-shot learning 的机制和最佳实践

## 按 Task 的推荐阅读

### Task 1 — Prompt 基础实验
- **[Zero-shot vs Few-shot 对比研究](https://huggingface.co/blog/few-shot-learning-gpt-3-and-inference-api)** — 实证分析不同 shot 数量对任务性能的影响
- **[Prompt 模板设计最佳实践](https://docs.anthropic.com/en/docs/build-a-chatbot#system-prompts)** — Anthropic 推荐的结构化 prompt 写法，包括清晰指令和边界定义
- **[Example 顺序的影响](https://arxiv.org/abs/2105.14165)** — Zhao et al. 的研究，证明 few-shot example 的选择和排列顺序显著影响结果

### Task 2 — Chain-of-Thought 实验
- **[Chain-of-Thought Prompting 完整指南](https://arxiv.org/abs/2201.11903)** — 详细讲解 "Let's think step by step" 如何激发逐步推理能力
- **[Self-Consistency 提升方法](https://arxiv.org/abs/2203.11171)** — Wang et al. 的论文，通过多次采样和多数投票改善推理准确率
- **[ReAct: Agent 的推理与行动](https://arxiv.org/abs/2210.03629)** — 结合 CoT 和工具调用的范式，理解 Agent 如何进行推理和决策

### Task 3 — 参数空间探索
- **[Temperature 参数详解](https://docs.anthropic.com/en/docs/build-a-chatbot#parameters)** — 理解 temperature 如何控制输出的随机性和多样性
- **[Top-p（核采样）与 Top-k](https://huggingface.co/blog/how-to-generate#select-tokens-with-controllable-randomness)** — 对比不同采样策略对生成质量的影响
- **[Max_tokens 与输出截断](https://docs.anthropic.com/en/docs/build-a-chatbot#parameters)** — 探讨长度限制对任务完成度和输出质量的影响

### Task 4 — Prompt 模板系统与评估
- **[Jinja2 模板引擎教程](https://jinja.palletsprojects.com/)** — 学习用模板语言实现动态 prompt 生成和条件渲染
- **[Anthropic Prompt 最佳实践全面指南](https://docs.anthropic.com/en/docs/build-a-chatbot)** — 包括系统 prompt 结构、角色定义、工具描述格式等实践建议
- **[Prompt 评估框架设计](https://arxiv.org/abs/2311.07590)** — Gao et al. 的研究，如何系统地评估和量化 prompt 质量

## 延伸资源（可选）
- **[In-Context Learning 的机制研究](https://arxiv.org/abs/2202.12837)** — Min et al. 深入探讨 few-shot learning 如何工作，出人意料的发现
- **[System 1 vs System 2 Prompt](https://arxiv.org/abs/2206.07682)** — Kirkpatrick et al. 的研究，对应快速直觉和慢速推理的 prompt 策略
- **[Prompt Injection 防御](https://docs.anthropic.com/en/docs/build-a-chatbot#preventing-prompt-injection)** — Agent 开发中保护 system prompt 的安全实践
- **[Agent System Prompt 的长期优化](https://anthropic.com/news/extended-thinking)** — 理解为什么 Agent 的 system prompt 会随着能力增强而演化
