### Task 2：推导式与解包（Day 1-2）

# - [ ] 用列表推导式实现：从成绩数据中筛选出 80 分以上的学生姓名。然后用 JS 的等价写法实现同样功能，对比两者的简洁度
# - [ ] 用条件推导式和嵌套推导式分别解决：展平一个二维列表、从字典列表中提取特定字段
# - [ ] 用字典推导式将一个 `{name: score}` 字典的 key 和 value 互换。**思考**：如果有重复的 value 会怎样？
# - [ ] 实验解包赋值：交换两个变量、从列表中取首尾元素、用星号表达式收集剩余元素。对比 JS 的解构赋值，有什么异同？
# - [ ] **思考**：推导式和 `map()`/`filter()` 都能做数据转换。Pythonic 的选择标准是什么？什么时候推导式更好，什么时候用 map？

# 📚 **Key docs**: [推导式教程 §5.1.3](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) | [PEP 274 — 字典推导式](https://peps.python.org/pep-0274/)
# > 教程讲用法，PEP 讲设计动机——理解"为什么这样设计"比记住语法更重要


#### Task2.1
student_list = [{
    "name": "Ada",
    "grade": 91
}, {
    "name": "Bob",
    "grade": 84
}, {
    "name": "Cindy",
    "grade": 77
 }]

print([student['name'] for student in student_list if student['grade'] > 80])

# [AI 批注] ✅ 已修正。现在正确提取了姓名，filter + map 一步到位，这就是推导式的优势。

# JS belike:
# student_list.filter(s => s.grade > 80);
# 为什么我觉得 JS 更简洁？因为 filter 是封装好的吗？应该用 for 循环的写法对比简洁程度？

# [AI 批注] 💡 你的直觉问得很好。JS 的 .filter() 看起来简洁是因为它只做了「筛选」这一步。
# 但如果 JS 要同时筛选+提取字段，就变成了：
#   student_list.filter(s => s.grade > 80).map(s => s.name)
# 而 Python 推导式一行就能做：
#   [s['name'] for s in student_list if s['grade'] > 80]
# 真正的简洁度对比应该是：「完成同一个完整任务」需要多少代码。
# 推导式把 filter + map 合到一个表达式里了，这就是它的优势。

# let filtered_student_list = []
# for(s of student_list) {
#     if(s.grade > 80) {
#         filtered_student_list.push(s)
#     }
# }

#### Task2.2
matrix = [
    [1,3,5,7],
    [2,4,6,8]
]

flatten_matrix = []

for row in matrix:
    for col in row:
        flatten_matrix.append(col)

print(flatten_matrix)
print([col for row in matrix for col in row])

# [AI 批注] ✅ 嵌套推导式的展平写法正确，也保留了 for 循环对照，很好的学习方式。

student_name_list = []
for s in student_list:
    student_name_list.append(s.get('name'))
print(student_name_list)
print([s.get('name') for s in student_list])

# [AI 批注] ✅ 已修正，两者都提取 'name'，对照清晰。
# 小建议：题目还提到了「条件推导式」，这里只有提取没有过滤条件。
# 可以再加一行带 if 的版本，同时展示条件推导式和字段提取：
#   [s['name'] for s in student_list if s['grade'] >= 80]

#### Task2.3
print([{
   value: key
} for s in student_list for key,value in s.items()])

scores = {"Ada": 91, "Bob": 84, "Cindy": 77}
print({value:key for key,value in scores.items()})

# [AI 批注] ✅ 已补充 scores 字典的互换，现在题目要求的核心用法覆盖到了。
# 上面那个 student_list 的嵌套推导式可以保留作为额外练习，但注意它生成的是
# 「单键字典的列表」而非一个互换后的字典，语义上和下面的 scores 互换是不同的操作。

person = {
    'name': "Ada",
    "age": 17,
    "grade": 17,
}

print({value: key for key, value in person.items()}) # if has same key, last key will overwrite behind key (same JS)

# [AI 批注] ✅ 重复 value 的实验和结论都正确。

#### Task2.4
num_list = [
    0,1,2,3,4,5
]
num_list[0],num_list[5] = num_list[5], num_list[0]

# [AI 批注] ✅ 两个问题都修正了：
# 1. 变量名从 `list` 改为 `num_list`，不再覆盖内置函数
# 2. 交换写法改为 Pythonic 的 tuple swap，去掉了多余的列表包装

print(num_list) # [5,1,2,3,4,0]

# remove first and last, expect: [1,2,3,4]

[first, *center, last] = num_list
print(first, center, last) # 5 [1,2,3,4] 0

# [AI 批注] ✅ 星号表达式用法正确。

[first, *center, last] = {
    "a": 1,
    "b": 2,
    "c": 3
}
print(first, center, last)  # a ['b'] c
# 为什么解构的是 key？如何像 JS 那样解构对象？

# [AI 批注] 💡 好问题！解构的是 key 是因为：对 dict 做迭代默认遍历的就是 key。
# for x in {"a": 1} 拿到的是 "a"，解包同理。
#
# 至于「如何像 JS 那样按名字解构」：
# 1. Python 没有 JS 的 const {name, age} = person 这种语法
# 2. 最接近的替代方案是 operator.itemgetter：
#      from operator import itemgetter
#      name, age = itemgetter('name', 'age')(person)
# 3. 或者直接多次取值：
#      name, age, grade = person['name'], person['age'], person['grade']
# 4. 如果用 dataclass 或 NamedTuple，就可以用属性访问：person.name
# 5. Python 3.10+ 的 match/case 支持 mapping pattern，可以实现类似效果：
#      match person:
#          case {"name": name, "age": age}:
#              print(name, age)

# 我认为 Python 和 JS 解构赋值最大的区别是 JS 只能直接结构到最后，但是 Python 可以选取中间截断解构

# [AI 批注] ✅ 这个观察是对的，但可以更全面：
# Python vs JS 解构的核心差异其实有三个：
# 1. ✅ 你说的：Python 的 * 可以在任意位置，JS 的 ...rest 只能在最后
# 2. 🔴 JS 支持按名字解构对象 {name, age} = obj，Python 不支持
# 3. 🔴 JS 解构支持默认值 {name = "unknown"} = obj，Python 的序列解包不支持
# 所以不是说 Python 的解构「更好」，而是各有所长——
# Python 的序列解包更灵活，JS 的对象解构更方便。


#### Task2.5
# 我认为逻辑复杂的时候用 map 这类的内置函数会让代码可读性更高
# 如果逻辑简单用推导式则更方便，也更易读

# [AI 批注] ⚠️ 这个结论和 Python 社区的共识相反，建议重新理解一下：
#
# Python 社区的准则是「推导式优先」：
# - 推导式更好：需要同时 filter + transform 时，或者需要字典/集合推导时
#   例：[x*2 for x in nums if x > 0]
#   对比：list(map(lambda x: x*2, filter(lambda x: x > 0, nums)))  # 丑
#
# - map 更好：已有现成函数（不需要写 lambda）时
#   例：map(int, ["1", "2", "3"])  比  [int(x) for x in ["1", "2", "3"]] 更简洁
#
# 一句话：能用推导式就用推导式，除非 map 配合已有函数更自然。


# ============================================================
# [AI 批注] 📊 Task 2 修订后评价
# ============================================================
#
# 完成度：★★★★☆ (4/5)
# - 5 个子任务全部覆盖
# - Task2.1 筛选姓名 ✅ 已修正
# - Task2.3 补充了 scores 字典互换 ✅ 已修正
# - Task2.4 变量名和交换写法 ✅ 已修正
# - Task2.2 的条件推导式可以再补一行带 if 的版本
# - Task2.5 的结论还需要修正
#
# 代码质量：★★★★☆ (4/5)
# - 上一轮的三个主要问题都已修正
# - 代码整体清晰可读
#
# 理解深度：★★★★☆ (4/5)
# - 对 dict 解包、重复 value 覆盖、Python vs JS 解构差异的理解都很好
# - Task2.5 的 map vs 推导式判断还需校准
#
# 剩余待改：
# 1. 🟡 Task2.5 把结论改过来（推导式优先，map 只在有现成函数时更自然）
# 2. 🟢 Task2.2 可选补一行条件推导式
