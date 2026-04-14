# ### Task 4：整合——构建 CLI 数据工具（Day 2-3）

# - [x] 用 `sys.argv` 或 `argparse` 模块接收命令行参数。先用 `sys.argv` 手动解析，再重构为 `argparse`——感受框架和手动实现的差异
# - [x] 实现以下功能：加载数据文件、按条件过滤行、按某列排序、对某列做统计（最小/最大/平均/计数）、取前 N 名
# - [x] 用格式化字符串输出整齐的表格。**思考**：你有没有发现 Python 的 `sorted()` 函数用 `key` 参数来定义排序规则？这个模式在 Python 中到处都是——为什么？
# - [x] **笔记**：总结一个"Python 数据处理常用套路"（读文件 → 解析 → 推导式转换 → 格式化输出）

# 📚 **Key docs**: [argparse 教程](https://docs.python.org/3/howto/argparse.html) | [sorted() 内置函数](https://docs.python.org/3/library/functions.html#sorted)
# > argparse 教程按"从简到繁"组织，跟着它的节奏走就好；sorted 的 key 参数是 Python 的核心设计模式，仔细看

#### Task4.1
import csv

##### use sys.argv
import sys

# filepath = sys.argv[1] if len(sys.argv) > 1 else None
# command = sys.argv[2] if len(sys.argv) > 2 else None
# column = sys.argv[3].split("--")[1] if len(sys.argv) > 3 else None
# operation = sys.argv[4].split(":")[0]  if len(sys.argv) > 4 else None
# value = sys.argv[4].split(":")[1]  if len(sys.argv) > 4 else None
# [AI 批注] ✅ sys.argv 手动解析版本保留了，能看到 len() 守卫和手动 split 的写法。
# 和下面 argparse 版本对比，能体会到框架帮你省了多少防御性代码。

##### use argparse
import argparse

parser = argparse.ArgumentParser(description='load csv and operate it')

parser.add_argument("filepath", type=str, help='file path')
parser.add_argument("command", choices=['list', 'sort', 'filter', 'calculate', 'top'], help="Support command")
parser.add_argument("--column", "-c", type=str, help="CSV column")
parser.add_argument("--operation", "-op", choices=['gt', 'gte', 'lt', 'lte', 'eq', "ne", "min", "max", "count", "average"], default=None)
parser.add_argument("--value", "-v", type=int)

args = parser.parse_args()
# [AI 批注] ✅ argparse 定义规范：有 choices 限制合法值、type 指定类型、help 提示。
# 💡 小建议：-op 这个短选项不太标准，通常短选项是单字母（如 -o）。
#    不过这不影响功能，只是惯例。

filepath = args.filepath
command = args.command
column = args.column
operation = args.operation
value = args.value


with open(filepath, newline='') as csv_file:
    students = list(csv.DictReader(csv_file))
# [AI 批注] ✅ csv.DictReader 用法简洁，和 task3 学到的一致。

student_keys = list(students[0].keys())

def operation_transform(operation, source_str, target_str):
    source = int(source_str)
    target = int(target_str)

    match operation:
        case "gt":
            return source > target
        case "lt":
            return source < target
        case "gte":
            return source >= target
        case "lte":
            return source <= target
        case "eq":
            return source == target
        case "ne":
            return source != target
# [AI 批注] ✅ 已修正（两处）：
# 1. ne 改为 != ✅
# 2. 类型转换移入函数内部（source_str/target_str → int），调用方不需要操心类型了 ✅
# 💡 函数名建议：operation_transform → compare，更直观地表达「比较」的语义。

def calculate_transform(operation, table: list, column: str):
    match operation:
        case "min":
            return min(table, key=lambda s: s[column])
        case "max":
            return max(table, key=lambda s: s[column])
        case "count":
            return len(table)
        case "average":
            return sum([int(row.get(column)) for row in table]) / len(table)
# [AI 批注] ⚠️ min/max 的类型问题还在：key=lambda s: s[column] 比较的是字符串，
#    字典序下 "9" > "85"（因为 '9' > '8'），会导致取极值结果错误。
#    需要改为 key=lambda s: int(s[column])。
# ✅ average 的 int() 转换做对了——同样的手法套到 min/max 就行。

def formatted_students_csv(students):
    for student_key in student_keys:
        print(f"{student_key:<20}", end = "")
    print()

    for row in students:
        for student_key in student_keys:
            print(f"{row.get(student_key):<20}", end = "")
        print()
# [AI 批注] ✅ f-string 格式化表格输出，固定列宽 20，和 task3.4 学到的技能衔接上了。
# 💡 进阶：数字列可以用 :>20 右对齐会更专业，不过这是 🟢 级别的改进。

match command:
    case 'list':
        formatted_students_csv(students)
    case 'sort':
        formatted_students_csv(students=sorted(students, key=lambda s: int(s[column]), reverse=True))
    case 'filter':
        formatted_students_csv(students=[student for student in students if operation_transform(operation, student.get(column), value)])
    case 'calculate':
        print(calculate_transform(operation, students, column))
    case 'top':
        formatted_students_csv(students=sorted(students, key=lambda s: int(s[column]), reverse=True)[0:int(value)])
# [AI 批注] ✅ 已修正（两处）：
# 1. 去掉了 formatted_students_csv 外层多余的 print()，不再输出 None ✅
# 2. filter 的类型问题已由 operation_transform 内部处理 ✅
# ⚠️ sort/top 的 key=lambda s: s[column] 仍然是字符串比较，需要改为 int(s[column])。
#    例如当前 sort math 的结果：Jack(96) > Mia(93) > Alice(92) > ... 看起来对，
#    但如果有个分数是 "9"，它会排在 "85" 前面。加上 int() 更安全：
#    sorted(students, key=lambda s: int(s[column]), reverse=True)


#### Answer
##### sys.argv 需要自己处理参数格式，判断类型，判空处理，而且使用时也没有任何提示。
# [AI 批注] ✅ 对 sys.argv vs argparse 差异的总结准确。
# 补充一点：argparse 还自动生成 --help 输出，并在参数不合法时给出友好错误信息——
# 这些你用 sys.argv 都得自己写。

##### sorted 类似 js 里的 map / filter ... sorted 表示在做什么，而里面的 key 函数，表示要怎么做
# [AI 批注] ✅ 方向对了，但可以更精确。sorted 和 map/filter 的相似点是「都接受函数作为参数」（高阶函数）。
# 更关键的设计模式是「策略分离」：
# - sorted() 负责排序算法（怎么排）
# - key 函数负责提取比较依据（按什么排）
# 这比 JS 的 arr.sort((a, b) => a.score - b.score) 更简洁——
# 你只需要说「按 score」，不需要自己写比较逻辑。
# Python 的 min(key=)、max(key=)、itertools.groupby(key=) 全都用这个模式。


# ============================================================
# [AI 批注] 📊 Task 4 评价（第二轮）
# ============================================================
#
# 完成度：★★★★★ (5/5)
# - sys.argv 手动解析 → argparse 重构，演进过程完整 ✅
# - 五个命令全部实现：list / sort / filter / calculate / top ✅
# - f-string 格式化表格输出 ✅
# - 两道思考题都有回答 ✅
#
# 代码质量：★★★★☆ (4/5)  ↑ 从 3/5 提升
# - argparse 定义规范、match/case 路由清晰、推导式用得自然 ✅
# - 上轮三个 🔴 已修复：ne 逻辑 ✅、filter 类型转换 ✅、多余 print() ✅
# - 类型转换的修法很好：把 int() 放进 operation_transform 内部，让调用方无感 ✅
# - 扣分项：
#   1. ⚠️ sort/top 的 sorted(key=lambda s: s[column]) 仍是字符串比较
#   2. ⚠️ calculate 的 min/max 同上
#
# 理解深度：★★★★☆ (4/5)
# - sys.argv vs argparse 的对比理解到位 ✅
# - sorted(key=) 的高阶函数模式有感知，方向对 ✅
# - 整个 task4 把前三个 task 的技能（csv.DictReader、f-string、推导式）整合起来了 ✅
#
# 剩余修复（⚠️ 级别，当前数据碰巧结果正确，但逻辑有隐患）：
# 1. ⚠️ sort/top：key=lambda s: int(s[column])
# 2. ⚠️ min/max：key=lambda s: int(s[column])
#
# 可选改进（🟢 级别）：
# 1. 🟢 函数名 operation_transform → compare
# 2. 🟢 数字列右对齐 :>20
# 3. 🟢 短选项 -op → -o