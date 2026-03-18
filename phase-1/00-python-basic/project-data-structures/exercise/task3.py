### Task 3：文件 I/O 与字符串处理（Day 2）

# - [ ] 用 `with` 语句读写文本文件。**思考**：`with` 和 JS 的 `try/finally` 解决的是同一个问题吗？`with` 的优势在哪里？
# - [ ] 用 `csv` 模块读取一个 CSV 文件，将其转换为字典列表。对比 `csv.reader` 和 `csv.DictReader` 的使用场景
# - [ ] 用 `json` 模块完成 JSON 的读取和写入。和 JS 的 `JSON.parse`/`JSON.stringify` 在 API 上有什么不同？
# - [ ] 用 f-string 格式化输出一个对齐的表格（固定列宽、数字右对齐）。搜索 f-string 的格式化语法（比如 `{value:>10.2f}` 这种）
# - [ ] 用 `pathlib.Path` 处理文件路径——拼接、判断存在、获取文件名。**思考**：为什么 Python 社区推荐 `pathlib` 而不是字符串拼接路径？

# 📚 **Key docs**: [csv 模块](https://docs.python.org/3/library/csv.html) | [pathlib 模块](https://docs.python.org/3/library/pathlib.html) | [格式化字符串语法](https://docs.python.org/3/library/string.html#formatspec)
# > csv 文档重点看 DictReader 的例子；pathlib 看 Basic use 小节就够用；格式化语法是工具书，按需查