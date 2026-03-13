# Tokenizer 探索器 — 学习资源

## 核心文档（必读）
1. **[Hugging Face Tokenizers 官方文档](https://huggingface.co/docs/tokenizers)** — 深入理解 BPE 算法原理和各种 tokenization 方法的权衡

2. **[OpenAI tiktoken GitHub](https://github.com/openai/tiktoken)** — GPT 模型使用的 tokenizer 实现，包括使用示例和编码细节

3. **[OpenAI API Pricing Documentation](https://openai.com/pricing/gpt-4)** — 了解不同模型的 token 定价，为成本计算器提供基准数据

## 按 Task 的推荐阅读

### Task 1 — 理解 BPE 算法
- **[Byte Pair Encoding (BPE) 概述](https://huggingface.co/docs/tokenizers/algorithms/bpe)** — 从 Hugging Face Tokenizers 文档学习 BPE 的步骤和合并过程
- **[tiktoken 官方示例](https://github.com/openai/tiktoken#usage)** — 学会使用 tiktoken 库进行 tokenize 和 decode 操作
- **[子词分词 vs 字符级/词级](https://huggingface.co/course/chapter2/4)** — 对比三种 tokenization 方式的优缺点，理解为什么 BPE 是默认选择

### Task 2 — 多模型 Tokenizer 对比
- **[Hugging Face transformers 快速开始](https://huggingface.co/docs/transformers/quicktour)** — 学会加载不同开源模型的 tokenizer（如 LLaMA、BERT）
- **[tiktoken 支持的模型列表](https://github.com/openai/tiktoken#models)** — 了解 GPT 系列模型对应的 encoding 标准
- **[Claude 官方 API 文档 - Token 计数](https://docs.anthropic.com/en/api/tokens)** — 查看通过 API 计算 Claude token 数的方法

### Task 3 — Token 可视化工具
- **[Rich 库文档](https://rich.readthedocs.io/)** — 学习在终端中实现彩色和格式化输出，美化 tokenizer 可视化
- **[Streamlit 官方教程](https://docs.streamlit.io/)** — 如果选择 Web 界面，Streamlit 是快速原型开发的最佳选择
- **[特殊 token 识别](https://github.com/openai/tiktoken#special-tokens)** — 理解 `<|endoftext|>` 等特殊 token 的作用和识别方法

### Task 4 — 成本计算与优化
- **[主流 LLM 模型定价汇总](https://www.cerebras.net/blog/a-guide-to-llm-pricing-decoder-only-models/)** — 参考多个模型的最新定价结构
- **[Prompt 优化技巧](https://docs.anthropic.com/en/docs/build-a-chatbot#managing-tokens)** — 了解减少 token 消耗的实用策略，包括 prompt 压缩和缓存
- **[Agent 中的 Context Window 管理](https://arxiv.org/abs/2312.10997)** — Lost in the Middle 论文，理解长上下文中的 token 管理问题

## 延伸资源（可选）
- **[Unicode 和 UTF-8 基础](https://en.wikipedia.org/wiki/UTF-8)** — 深入理解字节编码对 tokenization 的影响，特别是多语言支持
- **[SentencePiece 文档](https://github.com/google/sentencepiece)** — 学习另一种流行的 tokenization 方法，用于多语言模型
- **[Token 效率对比：中英日文](https://blog.yenniejun.com/p/all-that-is-string-matching-prefix)** — 实证研究不同语言的 token 消耗差异
- **[Agent 成本优化案例](https://www.anthropic.com/research/prompt-caching)** — Anthropic 的 Prompt Caching 如何在实践中降低成本
