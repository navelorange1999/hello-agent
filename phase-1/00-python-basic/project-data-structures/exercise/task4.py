# ### Task 4：整合——构建 CLI 数据工具（Day 2-3）

# - [ ] 用 `sys.argv` 或 `argparse` 模块接收命令行参数。先用 `sys.argv` 手动解析，再重构为 `argparse`——感受框架和手动实现的差异
# - [ ] 实现以下功能：加载数据文件、按条件过滤行、按某列排序、对某列做统计（最小/最大/平均/计数）、取前 N 名
# - [ ] 用格式化字符串输出整齐的表格。**思考**：你有没有发现 Python 的 `sorted()` 函数用 `key` 参数来定义排序规则？这个模式在 Python 中到处都是——为什么？
# - [ ] **笔记**：总结一个"Python 数据处理常用套路"（读文件 → 解析 → 推导式转换 → 格式化输出）

# 📚 **Key docs**: [argparse 教程](https://docs.python.org/3/howto/argparse.html) | [sorted() 内置函数](https://docs.python.org/3/library/functions.html#sorted)
# > argparse 教程按"从简到繁"组织，跟着它的节奏走就好；sorted 的 key 参数是 Python 的核心设计模式，仔细看

#### Task4.1
##### use sys.argv
import sys
import csv


filepath = sys.argv[1] if len(sys.argv) > 1 else None
command = sys.argv[2] if len(sys.argv) > 2 else None
column = sys.argv[3].split("--")[1] if len(sys.argv) > 3 else None
operation = sys.argv[4].split(":")[0]  if len(sys.argv) > 4 else None
value = sys.argv[4].split(":")[1]  if len(sys.argv) > 4 else None
    

with open(filepath, newline='') as csv_file:
    students = list(csv.DictReader(csv_file))

student_keys = list(students[0].keys())

def operation_transform(operation, source, target):
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
            return source == target
        
def calculate_transform(operation, table: list, column: str):
    match operation:
        case "min":
            return sorted(table, key=lambda s: s[column])[0]
        case "max":
            return sorted(table, key=lambda s: s[column], reverse=True)[0]
        case "count":
            return len(table)
        case "average":
            return sum([int(row.get(column)) for row in table]) / len(table)
            

def formatted_students_csv(students):
    for student_key in student_keys:
        print(f"{student_key:<20}", end = "")
    print()

    for row in students:
        for student_key in student_keys:
            print(f"{row.get(student_key):<20}", end = "")
        print()

match command:
    case 'list':
        print(formatted_students_csv(students))
    case 'sort':
        print(formatted_students_csv(students=sorted(students, key=lambda s: s[column], reverse=True)))
    case 'filter':
        print(formatted_students_csv(students=[student for student in students if operation_transform(operation, student.get(column), value)]))
    case 'calculate':
        print(calculate_transform(operation, students, column))
    case 'top':
        print(formatted_students_csv(students=sorted(students, key=lambda s: s[column], reverse=True)[0:int(value)]))


##### use argparse
import argparse

parser = argparse.ArgumentParser()
parser.parse_args()