# Project: 本地知识库（Mini RAG） — 学习资源

## 核心文档（必读）

1. **[ChromaDB 官方文档](https://docs.trychroma.com/)** — 学习 ChromaDB 的核心概念（Collection、Document、Embedding）和 API 用法

2. **[文本切分策略综述](https://docs.langchain.com/docs/modules/data_connection/document_loaders/file_directory)** — 理解不同 Chunk 策略的优缺点，学习如何选择合适的切分方式

3. **[RAG 架构与最佳实践](https://docs.anthropic.com/docs/guides/retrieval-augmented-generation)** — 理解完整的 RAG 流程：加载 → 切分 → 向量化 → 检索 → 生成

## 按 Task 的推荐阅读

### Task 1 — 文档加载与切分

- **[CharacterTextSplitter 实现](https://docs.langchain.com/docs/modules/data_connection/document_transformers/text_splitters/character_text_splitter)** — 学习按固定字符数切分的实现方式和参数（chunk_size、chunk_overlap）
- **[递归字符切分](https://docs.langchain.com/docs/modules/data_connection/document_transformers/text_splitters/recursive_character_text_splitter)** — 理解按段落/标题切分的优势，如何保留文档结构信息
- **[语义切分的思路](https://github.com/gkamradt/LLMTest_CrewAI/blob/main/Semantic_Search.ipynb)** — 学习基于语义相似度的切分方式，什么时候应该合并或拆分句子

### Task 2 — 向量存储

- **[ChromaDB 快速开始](https://docs.trychroma.com/getting-started)** — 学习如何创建 Collection、添加文档、搜索、管理元数据
- **[Metadata 存储最佳实践](https://docs.trychroma.com/usage-guide)** — 理解如何记录 chunk 的来源文件、位置信息，便于后续溯源
- **[FAISS 与 ChromaDB 对比](https://www.pinecone.io/learn/vector-database/)** — 了解两个库的 API 设计差异、性能特点，选择合适的向量存储方案

### Task 3 — 检索与问答

- **[RAG 的检索阶段](https://docs.anthropic.com/docs/guides/retrieval-augmented-generation)** — 重点学习如何将检索到的 context 注入 prompt，设计合理的 prompt 模板
- **[处理"知识库中无答案"的情况](https://docs.anthropic.com/docs/guides/system-prompts)** — 通过 System Prompt 指导 LLM 在不确定时说"我不知道"，避免幻觉
- **[引用溯源机制](https://github.com/anthropic-ai/anthropic-cookbook)** — 学习如何在生成的答案中标注信息来源，提高可信度

### Task 4 — 评估与优化

- **[检索评估指标](https://en.wikipedia.org/wiki/Evaluation_measures_(information_retrieval))** — 理解 Recall@K、Precision、NDCG 等指标，如何量化检索质量
- **[Query 改写技巧](https://arxiv.org/abs/2305.14283)** — 学习如何用 LLM 改写用户问题，使其更适合向量检索（如：展开缩写、补充上下文）
- **[混合检索与 Reranking](https://arxiv.org/abs/2210.11035)** — 理解为什么结合向量检索和关键词检索能提升效果，什么时候需要 Reranking
- **[Recall-Oriented Understudy for Gisting Evaluation (ROUGE)](https://github.com/google-research/google-research/tree/master/rouge)** — 学习如何评估 LLM 生成内容的质量

## 延伸资源（可选）

- **[LangChain RAG 教程](https://github.com/langchain-ai/langchain)** — 参考开源 Agent 框架的 RAG 实现，学习生产级的代码组织
- **[多模态 RAG](https://docs.anthropic.com/docs/guides/vision)** — 深入学习，如何处理包含图片/表格的文档
- **[知识图谱增强 RAG](https://arxiv.org/abs/2310.03025)** — 前沿方向，了解如何用结构化知识改进 RAG 效果
- **[PDF 文档智能解析](https://github.com/unstructured-io/unstructured)** — 学习如何处理复杂的 PDF 格式，保留表格、图像等结构信息
