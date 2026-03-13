# 04 · 向量数据库入门

> Agent 要有"记忆"和"知识"，就需要向量数据库。
> RAG（检索增强生成）是当前最实用的 Agent 知识能力方案，而向量数据库是 RAG 的心脏。

## 学习目标

完成本章后，你应该能回答：

1. 文本 Embedding 是怎么把语义转化为向量的？为什么语义相近的文本向量也相近？
2. 向量相似度搜索的原理是什么？余弦相似度和欧氏距离有什么区别？
3. Chunk 策略（怎么切分文档）为什么对 RAG 质量影响巨大？
4. FAISS、Chroma、Pinecone 分别适合什么场景？

## 包含项目

| 序号 | 项目 | 核心知识点 | 预计耗时 |
|------|------|-----------|---------|
| P1 | [Embedding 实验场](./project-embedding-playground/) | Embedding 模型、相似度计算、可视化 | 3-4 天 |
| P2 | [本地知识库](./project-local-knowledge-base/) | 文档切分、向量存储、检索问答 | 4-5 天 |

## 推荐阅读顺序

1. OpenAI — [Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)
2. Pinecone — [What are Vector Embeddings?](https://www.pinecone.io/learn/vector-embeddings/)
3. LangChain — [Text Splitters](https://python.langchain.com/docs/concepts/text_splitters/)
4. ChromaDB — [Getting Started](https://docs.trychroma.com/getting-started)
