# Project: Embedding 实验场 — 学习资源

## 核心文档（必读）

1. **[OpenAI Embedding API 文档](https://platform.openai.com/docs/guides/embeddings)** — 学习 `text-embedding-3-small` 模型、向量维度、API 调用方式

2. **[向量相似度度量方法](https://en.wikipedia.org/wiki/Cosine_similarity)** — 理解余弦相似度、欧氏距离、点积的数学原理和适用场景

3. **[scikit-learn 降维指南](https://scikit-learn.org/stable/modules/manifold.html)** — 学习 PCA 和 t-SNE 的原理、参数调优，用于向量空间可视化

## 按 Task 的推荐阅读

### Task 1 — Embedding 初体验

- **[OpenAI Embedding API](https://platform.openai.com/docs/guides/embeddings)** — 重点学习如何调用 API 获取向量、理解返回向量的维度和含义
- **[向量的基本概念](https://en.wikipedia.org/wiki/Cosine_similarity)** — 直观理解向量、维度、语义空间的概念

### Task 2 — 相似度计算与排序

- **[Cosine Similarity vs Euclidean Distance](https://stats.stackexchange.com/questions/136232/how-do-you-decide-whether-to-use-the-euclidean-or-manhattan-distance)** — 理解为什么余弦相似度在高维空间中更适合文本相似度计算
- **[向量点积与相似度](https://en.wikipedia.org/wiki/Dot_product)** — 理解点积为什么能衡量相似度、与余弦相似度的关系

### Task 3 — 向量空间可视化

- **[PCA 原理与实现](https://scikit-learn.org/stable/modules/decomposition.html#pca)** — 学习如何用 PCA 将 1536 维向量降到 2D，保留主要方差
- **[t-SNE 可视化指南](https://scikit-learn.org/stable/modules/manifold.html#t-sne)** — 理解 t-SNE 相比 PCA 的优势（非线性降维、聚类可视化）；参数 perplexity 的调优
- **[Matplotlib 散点图和 Plotly 交互式绘图](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html)** — 学习如何标注数据点、添加图例、制作高质量可视化

### Task 4 — Embedding 模型对比

- **[OpenAI vs Sentence-Transformers](https://www.sbert.net/)** — 对比不同 Embedding 模型的效果差异、性能、成本
- **[检索评估指标：Recall@K](https://en.wikipedia.org/wiki/Evaluation_measures_(information_retrieval)#Recall)** — 学习如何量化检索质量，评估不同模型的优劣
- **[多语言和跨语言 Embedding](https://www.sbert.net/docs/training/multilingual.html)** — 理解多语言 Embedding 的局限性、跨语言检索的挑战

## 延伸资源（可选）

- **[向量数据库选型指南](https://www.pinecone.io/learn/vector-database/)** — 了解不同向量数据库的特点，为后续 RAG 项目做准备
- **[Embedding 的局限性](https://arxiv.org/abs/2310.14318)** — 学术论文，深入理解 Embedding 在否定、长文本等场景的失效原因
- **[OpenAI Embedding 最佳实践](https://platform.openai.com/docs/guides/embeddings/best-practices)** — 官方建议，如何编写文本以获得更好的 Embedding 效果
