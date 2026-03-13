# Project: Prompt 实验室

## 为什么做这个项目？

Prompt Engineering 不是"玄学"，而是有方法论的工程实践。对于 Agent 开发者来说，System Prompt 的质量直接决定了 Agent 的行为边界和可靠性。这个项目让你用实验的方式，建立对 Prompt 设计的系统性理解。

---

## 项目目标

构建一个 Prompt 实验与评估框架：

1. 设计一套 Prompt 模板体系（System / User / Few-shot）
2. 对同一任务用不同 Prompt 策略进行 A/B 实验
3. 量化评估不同 Prompt 的效果差异
4. 探索 Temperature、Top-p 等参数对输出的影响

---

## 任务拆解

### Task 1：Prompt 基础实验（Day 1）

- [ ] 选定一个任务（推荐：文本分类或信息提取）
- [ ] 对同一任务分别写出：Zero-shot、One-shot、Few-shot prompt
- [ ] 准备 20 条测试数据，分别用三种 prompt 测试，记录准确率
- [ ] 制作对比表格，量化三种策略的效果差异
- [ ] **笔记**：Few-shot 的 example 选择和排列顺序会影响结果吗？设计实验验证

### Task 2：Chain-of-Thought 实验（Day 2）

- [ ] 选定一个推理任务（推荐：数学应用题或逻辑推理）
- [ ] 对比：直接回答 vs 加 "Let's think step by step" vs 手写推理链示例
- [ ] 测试 CoT（Chain-of-Thought）在不同难度问题上的效果差异
- [ ] 尝试 "Self-Consistency"：同一问题生成多次取多数票
- [ ] **思考**：Agent 的 ReAct 模式（Reasoning + Acting）和 CoT 有什么关系？

### Task 3：参数空间探索（Day 2-3）

- [ ] 固定一个 prompt，把 temperature 从 0 调到 1.5，每个值测试 10 次
- [ ] 观察并记录：输出的多样性、准确性、"创造力"如何变化
- [ ] 同样方式测试 top_p 参数
- [ ] 测试 max_tokens 限制对输出质量的影响
- [ ] **制表**：什么场景用什么参数？建立你自己的"参数选择速查表"

### Task 4：Prompt 模板系统（Day 3-4）

- [ ] 设计一个 Prompt 模板引擎（用 Jinja2 或 f-string）
- [ ] 支持变量插入、条件渲染、Few-shot 示例动态注入
- [ ] 实现 System Prompt + User Prompt + Assistant Prefill 的三层结构
- [ ] 为同一个 Agent 能力（如"网页总结"）设计 3 个不同的 prompt 版本
- [ ] 建立一个简单的评估脚本：自动运行多个 prompt 版本，比较输出
- [ ] **延伸**：了解 Anthropic 推荐的 Prompt 最佳实践，和你的实验结论对比

---

## 验收标准

- [ ] 有一份包含至少 20 条数据的实验结果表格
- [ ] 能用数据说明 Zero-shot vs Few-shot vs CoT 的效果差异
- [ ] 有自己总结的"参数选择速查表"
- [ ] 能向别人解释：给一个新任务，你会怎么系统地设计和迭代 prompt？

## 延伸思考

> Agent 的 System Prompt 通常很长（几百到几千字），包含角色定义、行为规则、工具说明、输出格式等。你觉得这些内容的排列顺序重要吗？怎么验证？
