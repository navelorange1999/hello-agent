# Project: 数据处理 CLI 工具

## 为什么做这个项目？

作为 JS 开发者，你习惯了用 Array 的 map/filter/reduce 处理数据。Python 有自己的一套更 Pythonic 的方式——推导式（comprehension）、解包（unpacking）、切片（slicing）。在 AI Agent 开发中，你会频繁处理 API 返回的 JSON 数据（提取字段、过滤结果、聚合信息），这个项目训练的正是这些技能。

---

## 项目目标

构建一个命令行数据处理工具，能够：

1. 读取 CSV 和 JSON 文件中的结构化数据
2. 对数据进行过滤、排序、聚合统计
3. 以格式化表格形式输出结果
4. 通过命令行参数选择不同的操作

---

## 任务拆解

### Task 1：Python 数据类型速通（Day 1）

- [ ] 创建一个学生成绩数据集（字典列表），用 list 的各种方法对它增删改查
- [ ] 用 dict 的 `.get()` 方法安全地访问可能不存在的键——和 JS 的 `obj?.key` 有什么不同？
- [ ] 创建一个 tuple，尝试修改它的元素，观察报错信息。**思考**：Python 为什么需要一个不可变的 list？在什么场景下不可变性是优势？
- [ ] 用 set 对数据去重，用集合运算（交集、并集、差集）找出两个班级的共同学生
- [ ] 实验 list 的切片语法——正向切片、反向切片、步长切片。对比 JS 的 `Array.slice()`，Python 的切片多了什么能力？
- [ ] **笔记**：写一份"JS vs Python 数据类型"速查对照，标注你觉得最容易混淆的 3 个点

📚 **Key docs**: [Python 数据结构教程](https://docs.python.org/3/tutorial/datastructures.html) | [内置类型参考](https://docs.python.org/3/library/stdtypes.html)
> 先通读教程的 5.1-5.5 小节建立整体印象，遇到具体方法时再查内置类型参考

### Task 2：推导式与解包（Day 1-2）

- [ ] 用列表推导式实现：从成绩数据中筛选出 80 分以上的学生姓名。然后用 JS 的等价写法实现同样功能，对比两者的简洁度
- [ ] 用条件推导式和嵌套推导式分别解决：展平一个二维列表、从字典列表中提取特定字段
- [ ] 用字典推导式将一个 `{name: score}` 字典的 key 和 value 互换。**思考**：如果有重复的 value 会怎样？
- [ ] 实验解包赋值：交换两个变量、从列表中取首尾元素、用星号表达式收集剩余元素。对比 JS 的解构赋值，有什么异同？
- [ ] **思考**：推导式和 `map()`/`filter()` 都能做数据转换。Pythonic 的选择标准是什么？什么时候推导式更好，什么时候用 map？

📚 **Key docs**: [推导式教程 §5.1.3](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) | [PEP 274 — 字典推导式](https://peps.python.org/pep-0274/)
> 教程讲用法，PEP 讲设计动机——理解"为什么这样设计"比记住语法更重要

### Task 3：文件 I/O 与字符串处理（Day 2）

- [ ] 用 `with` 语句读写文本文件。**思考**：`with` 和 JS 的 `try/finally` 解决的是同一个问题吗？`with` 的优势在哪里？
- [ ] 用 `csv` 模块读取一个 CSV 文件，将其转换为字典列表。对比 `csv.reader` 和 `csv.DictReader` 的使用场景
- [ ] 用 `json` 模块完成 JSON 的读取和写入。和 JS 的 `JSON.parse`/`JSON.stringify` 在 API 上有什么不同？
- [ ] 用 f-string 格式化输出一个对齐的表格（固定列宽、数字右对齐）。搜索 f-string 的格式化语法（比如 `{value:>10.2f}` 这种）
- [ ] 用 `pathlib.Path` 处理文件路径——拼接、判断存在、获取文件名。**思考**：为什么 Python 社区推荐 `pathlib` 而不是字符串拼接路径？

📚 **Key docs**: [csv 模块](https://docs.python.org/3/library/csv.html) | [pathlib 模块](https://docs.python.org/3/library/pathlib.html) | [格式化字符串语法](https://docs.python.org/3/library/string.html#formatspec)
> csv 文档重点看 DictReader 的例子；pathlib 看 Basic use 小节就够用；格式化语法是工具书，按需查

### Task 4：整合——构建 CLI 数据工具（Day 2-3）

- [ ] 用 `sys.argv` 或 `argparse` 模块接收命令行参数。先用 `sys.argv` 手动解析，再重构为 `argparse`——感受框架和手动实现的差异
- [ ] 实现以下功能：加载数据文件、按条件过滤行、按某列排序、对某列做统计（最小/最大/平均/计数）、取前 N 名
- [ ] 用格式化字符串输出整齐的表格。**思考**：你有没有发现 Python 的 `sorted()` 函数用 `key` 参数来定义排序规则？这个模式在 Python 中到处都是——为什么？
- [ ] **笔记**：总结一个"Python 数据处理常用套路"（读文件 → 解析 → 推导式转换 → 格式化输出）

📚 **Key docs**: [argparse 教程](https://docs.python.org/3/howto/argparse.html) | [sorted() 内置函数](https://docs.python.org/3/library/functions.html#sorted)
> argparse 教程按"从简到繁"组织，跟着它的节奏走就好；sorted 的 key 参数是 Python 的核心设计模式，仔细看

---

## 验收标准

- [ ] 能熟练使用 list/dict/set/tuple 及其常用方法，不查文档就能写出来
- [ ] 能自然地用推导式代替简单的 for 循环
- [ ] 能用 `with` + `csv`/`json` 模块读写文件
- [ ] 能用 f-string 做格式化输出
- [ ] 能向别人解释 Python 数据结构和 JS 对应物的 3 个关键差异

## 延伸思考

> 如果你要解析 OpenAI API 的 JSON 响应，提取所有 `tool_calls` 里的函数名和参数，你会怎么设计数据处理流程？试着用推导式写出伪代码。这种"解析 API 响应 → 提取关键字段"的模式，在 Agent 开发中每天都会用到。
