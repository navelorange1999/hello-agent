# ### Task 1：Python 数据类型速通（Day 1）

# - [ ] 创建一个学生成绩数据集（字典列表），用 list 的各种方法对它增删改查
# - [ ] 用 dict 的 `.get()` 方法安全地访问可能不存在的键——和 JS 的 `obj?.key` 有什么不同？
# - [ ] 创建一个 tuple，尝试修改它的元素，观察报错信息。**思考**：Python 为什么需要一个不可变的 list？在什么场景下不可变性是优势？
# - [ ] 用 set 对数据去重，用集合运算（交集、并集、差集）找出两个班级的共同学生
# - [ ] 实验 list 的切片语法——正向切片、反向切片、步长切片。对比 JS 的 `Array.slice()`，Python 的切片多了什么能力？
# - [ ] **笔记**：写一份"JS vs Python 数据类型"速查对照，标注你觉得最容易混淆的 3 个点

# 📚 **Key docs**: [Python 数据结构教程](https://docs.python.org/3/tutorial/datastructures.html) | [内置类型参考](https://docs.python.org/3/library/stdtypes.html)
# > 先通读教程的 5.1-5.5 小节建立整体印象，遇到具体方法时再查内置类型参考

#### Task1.1
students_grades = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
]

# Append new student
students_grades.append({
    "name": "Demo",
    "grade": 63
})

print("Append a student:", students_grades)

# Remove a student
students_grades.remove({"name": "Alice", "grade": 85})

print("Remove a student:", students_grades)

# [AI 批注] ⚠️ list.remove() 是按值匹配的，这里你硬编码了完整的字典字面量来删除。
# 实际开发中这很脆弱——如果 Alice 的字典多了一个字段（比如 "age": 20），这行就会
# 抛 ValueError。更 Pythonic 的做法是用列表推导式过滤：
#   students_grades = [s for s in students_grades if s["name"] != "Alice"]
# 或者先找到 index 再 pop。建议你试试这两种写法对比一下。

# Pop
pop_result = students_grades.pop()
print("Pop from students_grades:", pop_result, students_grades)

# Find and Update
update_index = students_grades.index(
    {"name": "Bob", "grade": 92}
)
students_grades[update_index]['grade'] = 100

# [AI 批注] ⚠️ 和上面 remove 同样的问题：index() 也是按完整值匹配。
# 如果 Bob 的 grade 已经被改过，这行就找不到了。更稳健的做法：
#   update_index = next(i for i, s in enumerate(students_grades) if s["name"] == "Bob")
# 这个 pattern 在处理 API 返回的 JSON 数据时非常常见，值得练一练。

print("Update", update_index, students_grades)


index_0_age = students_grades[0].get('age')
print('Index 0 student age:', index_0_age)

# [AI 批注] ✅ .get() 的基本用法正确。但题目要求的是深入对比 .get() 和 JS obj?.key 的不同，
# 这里只用了一行代码演示。建议补充：
# 1. .get() 可以指定默认值：students_grades[0].get('age', 0) — JS 的 ?? 运算符才能做到类似效果
# 2. .get() 只能用在 dict 上，而 JS 的 ?. 可以用在任何对象/数组上
# 3. 演示一下不用 .get() 直接 students_grades[0]['age'] 会抛 KeyError — 这和 JS 返回 undefined 是核心差异


#### Task1.2
# JS 可以链式调用: object?.a?.b?.c
# Python 虽然也可以但是有点长：object.get('a', {}).get('b',{}).get('c', {})

# JS 这个语法糖对所有类型都生效，例如：[1,2,3]?.[0] "abcd"?.[0], 即使在不支持的类型也不会抛错，例如：null?.[0] true?.['a']
# Python .get() 只对字典类型生效

# [AI 批注] ✅ 分析到位，抓住了两个核心差异：链式调用的冗长度和类型适用范围。
# 补充几个可以更深入的点：
# 1. Python 3.10+ 有 match/case 语法，但仍然没有原生的 optional chaining
# 2. 社区常见替代方案：try/except KeyError（EAFP 风格），或者用 reduce + .get()
# 3. 也可以提一下第三方库 glom 或 jmespath，它们专门解决深层嵌套访问问题
# 4. 你写的 .get('c', {}) 最后一层其实应该给真正的默认值而不是 {}，否则拿到的是空字典而不是 None


#### Task1.3
tuple_rgb = (0.1, 0.6, 0.7)

# tuple_rgb[0] = 0.2
# throw TypeError: 'tuple' object does not support item assignment

# tuple 不可以变是浅层的, 如果 tuple 里包含了深层结构(可 hash 的类型)，深层结构是可变的
tuple_obj = ([1,2], [3,4])
tuple_obj[0][0] = 0

# [AI 批注] ❌ 概念性错误：这里说的"可 hash 的类型"恰恰写反了。
# list 是「不可 hash」的（unhashable），但它是「可变的」（mutable）。
# tuple 的浅层不可变意味着你不能改变 tuple 的引用指向（不能让 tuple_obj[0] 指向另一个对象），
# 但如果引用指向的对象本身是可变的（比如 list），那个对象的内容可以变。
# 正确表述：tuple 里如果包含了可变对象（mutable，如 list/dict/set），
# 这些可变对象的内容仍然可以修改。hashable 和 mutable 是两个不同的概念，
# 虽然通常不可变对象才是 hashable 的，但不能混用这两个术语。

print(tuple_obj) # ([0, 2], [3, 4])

# 从业务场景理解 tuple 和 list 的不同
# list 是一组相同类型数据的集合
# tuple 可以是一组不同数据类型，但是业务逻辑相关的集合，例如：(location, job, age)
# tuple 也可以作为对象的 key，例如 {(x,y): city}

# [AI 批注] ✅ 很好的理解角度！tuple 作为 "heterogeneous record" vs list 作为 "homogeneous sequence"
# 是一个重要的语义区分。tuple 可以做 dict key 这一点也抓到了。
# 补充：这也是为什么 Python 后来引入了 NamedTuple — 给 tuple 的每个位置加上名字，
# 让 (37.7749, -122.4194) 变成 Point(lat=37.7749, lng=-122.4194)，可读性大幅提升。

# 从代码层面理解 tuple 和 list 的不同
# 除了上述最明显的 tuple 不可变之外，最大的不同还是性能问题
# list 是可以动态删减的，所以 list 的长度会在内存中声明的远比使用的多
# tuple 是固定分配地址长度的

# [AI 批注] ✅ 方向正确，tuple 确实比 list 更轻量。
# 更精确地说：list 使用 over-allocation 策略（预分配额外空间以支持 append 的 amortized O(1)），
# 而 tuple 是精确分配。此外 CPython 还会缓存小 tuple 对象以复用内存（tuple 的 free list 机制），
# 这是 list 没有的优化。可以用 sys.getsizeof() 实际对比一下：
#   import sys
#   print(sys.getsizeof((1,2,3)))  # 64
#   print(sys.getsizeof([1,2,3]))  # 88 (or similar, depends on platform)


#### Task1.4
class_1 = {
    "Tom",
    "Jerry"
}

class_2 = {
    "Tom",
    "HelloKitty"
}

print(class_1 & class_2)
print(class_1 - class_2)
print(class_1 | class_2)

# [AI 批注] ✅ 集合运算的基本用法正确。但题目要求的是「用 set 对数据去重」+ 集合运算。
# 这里缺少了去重的演示——建议从 students_grades 出发，比如：
#   all_names = ["Tom", "Jerry", "Tom", "Alice", "Jerry"]
#   unique_names = set(all_names)  # 去重
# 另外，这里只演示了 &、-、| 三个运算符，可以补充 ^ (对称差集)，
# 以及方法调用形式 .intersection()/.difference()/.union() 和运算符形式的区别：
# 方法形式接受任何 iterable，运算符形式两边都必须是 set。
# 还有一个常见的实际用途没体现：用 set 做 O(1) 的成员检测 — "Tom" in class_1，
# 这比 list 的 O(n) 快很多，在处理大数据集时差异很大。


#### Task1.5
list_1 = [0,1,2,3,4,5]
print(list_1[0:1])   # [0]
print(list_1[-3:-1]) # [3, 4]

print(list_1[-1]) # 5
print(list_1[-1:]) # [5]

print(list_1[0:-1:2]) # [0,2,4]
print(list_1[::2]) # [0,2,4]

print(list_1[-1:0:-2]) # [5,3,1]
print(list_1[::-2]) # [5,3,1]

print(list_1)

# Python 的切片比 JS 的 Array.slice 多了 step 的能力，可以跳段切片

# [AI 批注] ✅ 切片语法的各种变体都覆盖了，包括负索引和步长，练得很扎实。
# 可以再补充几个 Python 切片独有的强大用法：
# 1. 切片赋值（JS 完全没有的能力）：
#    list_1[1:3] = [10, 20, 30]  # 可以替换为不同长度的序列！
# 2. 切片删除：del list_1[::2]  # 删除所有偶数索引的元素
# 3. 切片是浅拷贝：list_copy = list_1[:]  # 等价于 list_1.copy()
# 4. 字符串也支持切片："hello"[::-1] == "olleh"  # 反转字符串的经典写法
# 总结部分的「跳段切片」说法准确但不够全面，step 不只是跳着取，负 step 还能实现反向遍历。


#### Task1.6
# 印象最深的三个差异点：
# Python 没有 switch 语句，但是可以使用字典语法进行类似的逻辑操作
# Python 访问对象上的 key，访问到不存在的 key 是会报错的，不像 js 会返回 undefined
# Python 是不会进行类型推断的，例如 Python 虽然可以和 JS 那样 "1" + "2" = "12", 但是 JS 可以两个不同的基础类型进行相加的 "1" + 1 = "11",

# [AI 批注] 📝 逐条点评：
#
# 第1点 ⚠️：Python 3.10+ 已经有了 match/case（结构化模式匹配），它比 JS 的 switch 还强大。
# 不过你说的用字典做分发确实是 Python 3.10 之前的经典 pattern，这个认知没问题。
#
# 第2点 ✅：这是一个非常关键的差异，抓得好。dict['missing_key'] 抛 KeyError 而
# JS 返回 undefined — 这直接影响了两个语言的编码风格（Python 倾向 EAFP，JS 倾向 LBYL）。
#
# 第3点 ⚠️：措辞不太准确。这里说的不是"类型推断"，而是"隐式类型转换/强制类型转换"
# （type coercion）。JS 的 "1" + 1 = "11" 是因为 JS 有隐式类型转换规则，
# 而 Python 不做这种隐式转换，会直接抛 TypeError。
# "类型推断"（type inference）是另一个概念，指的是编译器/解释器自动推断变量类型，
# 比如 TypeScript 的 `let x = 1` 推断 x 为 number。Python 其实也有类型推断（在 mypy 中）。
#
# 另外，这三个差异偏向「语言通用特性」而非题目要求的「数据类型」差异。
# 建议补充更贴合数据结构的对比，比如：
# - JS 的 Object 既是 map 又是对象，Python 的 dict 就是 dict（职责单一）
# - JS 没有 tuple，Python 的 tuple 解决了不可变序列的需求
# - Python 的 set 是内置一等公民，JS 的 Set 是后来加的，API 风格很不同


# ============================================================
# [AI 批注] 📊 整体评价
# ============================================================
#
# 完成度：★★★☆☆ (3/5)
# - Task 1 的 6 个子任务全部涉及了，但部分子任务深度不足
# - Task 2/3/4 尚未开始（推导式、文件 I/O、CLI 工具整合）
#
# 代码质量：★★★☆☆ (3/5)
# - 代码能正确运行，输出符合预期
# - 但 remove() 和 index() 用了硬编码字典匹配，实际项目中很脆弱
# - 缺少按条件查找/更新的更 Pythonic 写法（列表推导式、next+enumerate 等）
#
# 理解深度：★★★★☆ (4/5)
# - tuple vs list 的理解角度很好（语义差异 + 性能差异）
# - .get() vs ?. 的对比抓住了核心点
# - 有一个概念性错误需要修正（hashable vs mutable 混淆）
# - 「类型推断」和「隐式类型转换」的术语混用需注意
#
# 建议下一步：
# 1. 修正 Task1.3 中 hashable/mutable 的概念错误
# 2. 补充 Task1.1 中更 Pythonic 的查找/删除写法
# 3. Task1.6 的笔记补充更贴合「数据类型」的差异点
# 4. 继续推进 Task 2（推导式与解包）— 这是 Python 最核心的 idiom 之一
