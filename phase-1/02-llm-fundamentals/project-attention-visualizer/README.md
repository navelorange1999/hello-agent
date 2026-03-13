# Project: Attention 可视化器

## 为什么做这个项目？

Self-Attention 是 Transformer 的灵魂。理解 Attention 不是为了让你训练模型，而是为了在 Agent 开发中做出更好的决策——比如理解为什么 LLM 有时会"忽略"prompt 中间的指令（Lost in the Middle 问题），或者为什么长上下文窗口并不总是越大越好。

---

## 项目目标

从数学层面理解 Self-Attention 并可视化：

1. 手动实现 Scaled Dot-Product Attention 的计算
2. 可视化注意力权重矩阵（哪些 token 在"关注"哪些 token）
3. 用预训练模型提取真实的 attention 权重并可视化
4. 探索多头注意力（Multi-Head Attention）每个头关注的模式

---

## 任务拆解

### Task 1：手动计算 Attention（Day 1）

- [ ] 阅读 "The Illustrated Transformer"，理解 Q、K、V 矩阵的含义
- [ ] 用 NumPy 手动实现：给定 Q、K、V 矩阵，计算 Attention 输出
- [ ] 公式：`Attention(Q,K,V) = softmax(QK^T / √d_k) × V`
- [ ] 用 3-4 个 token 的小例子，手动算出每一步的数值
- [ ] **笔记**：为什么要除以 √d_k？不除会怎样？

### Task 2：Attention 矩阵可视化（Day 2）

- [ ] 用 matplotlib 绘制 attention 权重的热力图
- [ ] 输入一个简单句子，观察每个 token 对其他 token 的注意力分布
- [ ] 对比不同句子结构下的 attention 模式（如主语-谓语-宾语 vs 倒装句）
- [ ] **思考**：在 Agent 的 system prompt 中，为什么把重要指令放在开头和结尾比放中间更有效？

### Task 3：预训练模型的真实 Attention（Day 2-3）

- [ ] 使用 Hugging Face `transformers` 加载一个小模型（如 `bert-base-uncased` 或 `gpt2`）
- [ ] 提取模型处理文本时每一层的 attention 权重
- [ ] 可视化不同层的 attention 模式差异
- [ ] 观察：浅层 attention 和深层 attention 关注的内容有什么不同？
- [ ] **推荐工具**：试试 `bertviz` 库进行交互式可视化

### Task 4：Multi-Head 分析（Day 3-4）

- [ ] 可视化同一层中不同 attention head 的关注模式
- [ ] 尝试识别：有没有专门关注"语法关系"的 head？有没有关注"位置距离"的 head？
- [ ] 了解位置编码（Positional Encoding）的作用——去掉它会怎样？
- [ ] **笔记**：总结 Attention 机制对 Agent Prompt 设计的实际启示

---

## 验收标准

- [ ] 能手动完成一个 4 token 句子的 attention 计算（不用代码辅助）
- [ ] 生成至少 3 张有意义的 attention 热力图
- [ ] 能解释：为什么 LLM 会出现"Lost in the Middle"现象？这和 attention 有什么关系？
- [ ] 能解释 Multi-Head Attention 的价值——为什么一个 head 不够？

## 延伸思考

> Claude 3.5 的上下文窗口是 200K tokens。这意味着 attention 矩阵是 200K × 200K 的。想想这对计算量意味着什么？这就是为什么各种"高效 Attention"方案（如 Flash Attention、Sliding Window Attention）这么重要。
