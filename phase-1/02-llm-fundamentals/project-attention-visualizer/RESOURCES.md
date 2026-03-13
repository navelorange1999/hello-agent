# Attention 可视化器 — 学习资源

## 核心文档（必读）
1. **[Attention Is All You Need](https://arxiv.org/abs/1706.03762)** — Transformer 的原始论文，Self-Attention 机制的数学基础和 Scaled Dot-Product Attention 公式

2. **[The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)** — 用可视化直观解释 Q、K、V 矩阵和 attention 计算过程，强烈推荐作为入门

3. **[Hugging Face Transformers 文档 - Attention](https://huggingface.co/docs/transformers/glossary#attention-head)** — 多头注意力和位置编码的实现细节

## 按 Task 的推荐阅读

### Task 1 — 手动计算 Attention
- **[The Illustrated Transformer 中的 Q、K、V 讲解](https://jalammar.github.io/illustrated-transformer/#queries-keys-and-values)** — 通过图解理解 Query、Key、Value 的角色和含义
- **[Attention Is All You Need 中的公式推导](https://arxiv.org/pdf/1706.03762.pdf)** — 逐步推导 `Attention(Q,K,V) = softmax(QK^T / √d_k) × V`，理解每一项的作用
- **[√d_k 的重要性：缩放因子解释](https://stackoverflow.com/questions/55994486/why-do-we-scale-attention-by-1-sqrt-dk)** — 理解为什么缩放对梯度流稳定性至关重要

### Task 2 — Attention 矩阵可视化
- **[Matplotlib 热力图绘制](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html)** — 学习用 `imshow()` 和 `seaborn.heatmap()` 绘制 attention 权重矩阵
- **[Lost in the Middle: 位置偏差问题](https://arxiv.org/abs/2307.03172)** — 论文深入分析为什么中间信息被忽视，与 attention 机制的关系
- **[Prompt 设计中的位置效应](https://www.anthropic.com/research/claude-3-5-sonnet)** — 实证指导：重要指令应放在开头或结尾的原因

### Task 3 — 预训练模型的真实 Attention
- **[Hugging Face transformers - 提取 attention 权重](https://huggingface.co/docs/transformers/v4.39.1/en/main_classes/output#transformers.BaseModelOutput)** — 学会从模型输出中获取 `attentions` 张量
- **[BertViz 交互式可视化库](https://github.com/jessevig/bertviz)** — 功能强大的 attention 可视化工具，支持多种模型和可视化方式
- **[不同层的语义差异](https://jalammar.github.io/illustrated-gpt2/#part-2-the-gpt-2-ssl-language-model)** — 理解浅层关注句法特征，深层关注语义关系的现象

### Task 4 — Multi-Head 分析与位置编码
- **[Multi-Head Attention 的价值](https://jalammar.github.io/illustrated-transformer/#multi-headed-attention)** — 为什么多个 head 能捕捉不同的关系类型（语法、语义、位置等）
- **[位置编码（Positional Encoding）](https://arxiv.org/abs/1706.03762#page=6)** — 理解绝对位置编码和相对位置编码的差异及其重要性
- **[Rotary Position Embedding](https://arxiv.org/abs/2104.09864)** — 现代模型（LLaMA、GPT-4）采用的位置编码方法，更好地支持外推

## 延伸资源（可选）
- **[Flash Attention：高效注意力算法](https://arxiv.org/abs/2205.14135)** — 理解为什么需要优化 attention，特别是在长序列场景
- **[Sliding Window Attention](https://arxiv.org/abs/2204.14198)** — Llama 2 采用的局部 attention 策略，减少计算复杂度
- **[Attention 的演进历程](https://arxiv.org/abs/2403.01781)** — 综述论文，对比各种 attention 变体和优化方案
- **[在线 Transformer 可视化工具](https://transformer-circuits.pub/)** — Anthropic 的 Circuit 可视化工具，深入理解神经网络的内部工作机制
