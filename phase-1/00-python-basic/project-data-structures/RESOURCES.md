# P0-1 数据处理 CLI 工具 — 学习资源

## 核心文档（必读）

1. **[Python 数据结构教程](https://docs.python.org/3/tutorial/datastructures.html)**
   重点：§5.1 列表方法、§5.3 元组与序列、§5.4 集合、§5.5 字典。这是你建立 Python 数据结构心智模型的起点。

2. **[内置类型参考](https://docs.python.org/3/library/stdtypes.html)**
   工具书，不用通读。当你需要查某个方法的确切行为时来这里（例如 dict.get 的默认值机制）。

3. **[Python for JavaScript Developers](https://www.valentinog.com/blog/python-for-js/)**
   快速对照指南，帮你把 JS 经验映射到 Python。适合在开始前花 20 分钟扫一遍。

## 按 Task 的推荐阅读

### Task 1 — 数据类型
- [序列类型 (list, tuple, range)](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) — 注意通用序列操作和可变序列操作的区别
- [集合类型](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset) — 重点看集合运算的操作符形式

### Task 2 — 推导式与解包
- [列表推导式 §5.1.3](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) — 从简单到嵌套，循序渐进
- [PEP 3132 — 扩展解包](https://peps.python.org/pep-3132/) — 星号表达式 `*rest` 的设计动机

### Task 3 — 文件 I/O
- [csv 模块](https://docs.python.org/3/library/csv.html) — 重点看 DictReader
- [json 模块](https://docs.python.org/3/library/json.html) — 对比 load/loads、dump/dumps 的区别
- [pathlib](https://docs.python.org/3/library/pathlib.html) — Basic use 小节 + 路径操作
- [格式化字符串语法](https://docs.python.org/3/library/string.html#formatspec) — 工具书，按需查阅

### Task 4 — CLI 整合
- [argparse 教程](https://docs.python.org/3/howto/argparse.html) — 从简到繁的渐进式教程，跟着走
- [sorted() HOWTO](https://docs.python.org/3/howto/sorting.html) — 深入理解 key 参数和排序稳定性

## 延伸资源（可选）

- [Fluent Python, Ch.2 — An Array of Sequences](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/) — 如果你想深入理解 Python 序列类型的设计哲学
- [Real Python — Reading and Writing CSV Files](https://realpython.com/python-csv/) — 比官方文档更友好的 CSV 教程
