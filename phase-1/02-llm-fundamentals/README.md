# 02 · LLM 核心概念

> 不理解 LLM 的工作原理，写 Agent 就像不懂发动机原理就改装赛车。
> 这一章不是要你从零训练模型，而是建立足够的直觉来做出正确的工程决策。

## 学习目标

完成本章后，你应该能回答：

1. Transformer 的 Self-Attention 机制在做什么？为什么它比 RNN 更适合处理长文本？
2. Tokenization 是怎么影响 LLM 行为的？为什么中文 token 数往往比英文多？
3. Temperature、Top-p 这些参数到底在控制什么？什么场景该用什么值？
4. 什么是好的 Prompt？为什么 Few-shot 比 Zero-shot 效果好？

## 包含项目

| 序号 | 项目 | 核心知识点 | 预计耗时 |
|------|------|-----------|---------|
| P1 | [Tokenizer 探索器](./project-tokenizer-explorer/) | BPE 算法、token 计数、多语言差异 | 2-3 天 |
| P2 | [Attention 可视化器](./project-attention-visualizer/) | Self-Attention 计算、注意力矩阵、位置编码 | 3-4 天 |
| P3 | [Prompt 实验室](./project-prompt-lab/) | Prompt 模板、Few-shot、CoT、参数调优 | 3-4 天 |

## 推荐阅读顺序

1. Jay Alammar — [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
2. Andrej Karpathy — [Let's build GPT: from scratch, in code](https://www.youtube.com/watch?v=kCc8FmEb1nY)（强烈推荐）
3. Hugging Face — [NLP Course Chapter 2: Tokenizers](https://huggingface.co/learn/nlp-course/chapter2/4)
4. OpenAI — [Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
