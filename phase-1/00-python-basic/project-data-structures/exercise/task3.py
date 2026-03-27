### Task 3：文件 I/O 与字符串处理（Day 2）

# - [ ] 用 `with` 语句读写文本文件。**思考**：`with` 和 JS 的 `try/finally` 解决的是同一个问题吗？`with` 的优势在哪里？
# - [ ] 用 `csv` 模块读取一个 CSV 文件，将其转换为字典列表。对比 `csv.reader` 和 `csv.DictReader` 的使用场景
# - [ ] 用 `json` 模块完成 JSON 的读取和写入。和 JS 的 `JSON.parse`/`JSON.stringify` 在 API 上有什么不同？
# - [ ] 用 f-string 格式化输出一个对齐的表格（固定列宽、数字右对齐）。搜索 f-string 的格式化语法（比如 `{value:>10.2f}` 这种）
# - [ ] 用 `pathlib.Path` 处理文件路径——拼接、判断存在、获取文件名。**思考**：为什么 Python 社区推荐 `pathlib` 而不是字符串拼接路径？

# 📚 **Key docs**: [csv 模块](https://docs.python.org/3/library/csv.html) | [pathlib 模块](https://docs.python.org/3/library/pathlib.html) | [格式化字符串语法](https://docs.python.org/3/library/string.html#formatspec)
# > csv 文档重点看 DictReader 的例子；pathlib 看 Basic use 小节就够用；格式化语法是工具书，按需查
from pathlib import Path, PurePath
import csv
import json

root = Path(__file__).parent


#### Task3.1
txt_file_path = root / "assets" / "task3_text_file.txt"
print("txt_file_path:", txt_file_path)

# read + write
with open(txt_file_path, 'r+') as text_file:
    content = text_file.read()
    print(content)
    text_file.writelines('\nHello Python!')
    content = text_file.read()
    print(content)
# [AI 批注] ✅ 已修正：'r+' 模式写法已规范化（上轮是 '+r'）。
# ⚠️ 但上轮指出的两个实际问题仍然存在：
#
# 1. 第二次 text_file.read() 仍然返回空字符串（文件指针在末尾）——这个没改。
#    如果想读到写入后的完整内容，需要先 text_file.seek(0) 把指针移回开头。
#
# 2. 脚本幂等性问题仍在。你的 txt 文件现在已经有 33 行 "Hello Python!" 了，
#    每跑一次就多一行。建议写到单独的输出文件（和你 Task 3.3 的改法一样）。

# 思考：
# try-catch 只是 with 能力的一部分，with 不仅仅可以用来处理异常，还能用来处理异步事务（例如数据库连接）
# with 本质是一个上下文管理器，只要这个 context 有 __enter__ 和 __exit__ 方法，都可以使用 with 来进行资源的进入和退出操作
# [AI 批注] 📝 思考题（未修改，上轮批注仍有效）：
# - __enter__/__exit__ 的理解 ✅
# - 术语问题仍在："try-catch" 应为 "try/except"（Python）或题目所问的 "try/finally"；
#   "异步事务"不准确，with 是同步的，async with 才是异步的。
# - 这些是小瑕疵，不影响核心理解，但建议顺手改一下。

#### Task3.2
csv_file_path = root / 'assets' / 'task3_csv_file.csv'
print("csv_file_path:", csv_file_path)

with open(csv_file_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar= '"')
    # [AI 批注] ✅ quotechar 正确。
    csv_reader_list = []
    for row in csv_reader:
        csv_reader_list.append(row)


    # ??? how to do this?
    # how to make it like `DictReader`
    print([dict(zip(csv_reader_list[0], csv_reader_list[rowIndex]))
           for rowIndex in range(len(csv_reader_list)) if rowIndex != 0
           ])
    # [AI 批注] ✅ zip 版本正确且 Pythonic。

    print([{csv_reader_list[0][keyIndex]: csv_reader_list[rowIndex][keyIndex] for keyIndex in range(len(csv_reader_list[0]))}
           for rowIndex in range(len(csv_reader_list)) if rowIndex != 0
           ])
    # [AI 批注] ✅ 字典推导式版本也正确。


with open(csv_file_path, newline='') as csv_file:
    print(list(csv.DictReader(csv_file)))
# [AI 批注] ✅ 简洁。

# 需要输出字典列表时用 DictReader. 需要获取特定行或者列时可以用 reader，需要按行输出或者按列输出时也可以用 reader
# [AI 批注] ✅ 对比总结到位，上轮批注的补充可以参考但不是必须修改的。


#### Task3.3
json_file_path = root / 'assets' / 'task3_json_file.json'
with open(json_file_path, 'r') as json_file_str:
    # [AI 批注] ✅ 文件模式规范。
    obj = json.load(json_file_str)
    print(json.dumps(obj, indent=2))

with open(root / 'assets' / 'task3_json_file_output.json', 'w') as json_file_w:
    obj['glossary']['title'] = "Hello World!"
    json.dump(obj, json_file_w, indent=2)
# [AI 批注] ✅ 已修正（三处）：
# 1. 写入到独立的输出文件 task3_json_file_output.json，不再修改源数据 ✅
# 2. 使用 json.dump() 直接写入文件对象，而非 json.dumps() + write() ✅
# 3. 源 JSON 文件已恢复原始内容 ✅

# Answer:
# Python 带 s 的版本和 JS parse/stringify 类似，都是对字符串操作
# 不带 s 的版本是对文件进行操作
# [AI 批注] ✅ 已修正：回答了思考题。核心区分（s = string, 无 s = file object）正确。
# 💡 可以再深想一步：为什么 Python 要做这个区分而 JS 不需要？
# 提示：JS 的 JSON.parse/stringify 只处理字符串，文件读写由另外的 API（fs 模块）负责；
# 而 Python 的 json 模块把"序列化"和"I/O"两个关注点合并在了同一个模块里，
# 所以需要用 s 后缀来区分。这其实是两种语言设计哲学的差异。

#### Task3.4
with open(csv_file_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar= '"')
    for row in csv_reader:
        for colIndex in range(len(row)):
            print(f"{row[colIndex]:<{(colIndex + 1) * 15}}", end = "")
        print()
# [AI 批注] ✅ 已修正：改用了 f-string 语法，核心练习点完成了。
# ⚠️ 还有一个小问题：列宽 (colIndex + 1) * 15 导致第一列 15、第二列 30、第三列 45，
# 递增列宽在视觉上不太合理。固定列宽（比如统一 25）或根据数据实际宽度设定会更好。
# 另外题目提到"数字右对齐"，Phone 列可以试试 f"{value:>15}" 的右对齐效果。
# 这是 🟢 级别的改进，不是必须的。


### Task3.5
print("root.exists()", root.exists())
print("root.name", root.name)
print("csv file suffix", PurePath(root, 'task3_csv_file.csv').suffix)
# [AI 批注] ✅ pathlib 基本 API 覆盖了。
# 💡 小建议：PurePath 换成 Path 或直接用 / 运算符会更一致（和你前面的代码风格统一）。

# Answer:
# 使用 pathlib 除了操作方便之外，代码链式看起来直观之外。最重要的就是跨平台的兼容性。
# [AI 批注] ✅ 已修正：回答了思考题。跨平台兼容性是最核心的点，答对了。
# "操作方便"和"链式直观"也对，不过更准确的说法是：pathlib 提供了面向对象的路径操作
# （Path 是对象，不是字符串），所以你能用 / 运算符、.parent、.suffix 这些方法，
# 而字符串拼接只能用 os.path.join() 这种函数式调用。


# ============================================================
# [AI 批注] 📊 整体评价（第三轮）
# ============================================================
#
# 完成度：★★★★★ (5/5)
# - Task 3.1 ✅ 读写都有，思考笔记有
# - Task 3.2 ✅ 两种转 dict 写法正确，DictReader 简洁，对比总结有
# - Task 3.3 ✅ 读写都有，写到独立输出文件，用了 json.dump()，思考题回答了
# - Task 3.4 ✅ 改用了 f-string，输出了真实表格
# - Task 3.5 ✅ pathlib API 使用了，思考题回答了
#
# 代码质量：★★★★☆ (4/5)
# - 核心逻辑全部正确 ✅
# - json 写入改进到位（dump + 独立文件） ✅
# - 扣分项：txt 文件仍被反复追加（幂等性问题），列宽递增不太合理
#
# 理解深度：★★★★☆ (4/5)
# - 所有思考题都回答了，核心概念把握正确 ✅
# - json load/loads 区分理解到位 ✅
# - pathlib 跨平台兼容性理解到位 ✅
# - 扣分项：with 思考题的术语瑕疵（try-catch vs try/finally）未修正
#
# 剩余改进（均为 🟢 级别，不阻塞进入下一个 task）：
# 1. 🟢 Task 3.1 写入改为独立输出文件，解决幂等性问题
# 2. 🟢 Task 3.1 思考题术语微调：try-catch → try/finally
# 3. 🟢 Task 3.4 列宽优化 + 数字列右对齐
