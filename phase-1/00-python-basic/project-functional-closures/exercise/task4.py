# ### Task 4：生成器与惰性求值（Day 2-3）

# - [ ] 写一个普通函数和一个使用 `yield` 的生成器函数，对比它们的返回值类型。**思考**：生成器的返回值为什么不是一个 list？"惰性"意味着什么？
# - [ ] 对比列表推导式和生成器表达式（方括号 vs 圆括号）的内存占用。用一个非常大的数据量来测试——观察内存差异
# - [ ] 实现一个惰性文件读取器：逐行读取大文件，每次只在内存中保留一行。**思考**：如果文件有 10GB，一次性读入内存会怎样？你的生成器方案为什么能处理？
# - [ ] 搜索并实验 `itertools` 中的 `chain`、`islice`、`groupby`。它们分别解决什么问题？
# - [ ] 实现一个惰性版的 pipe：用生成器串联多个处理步骤，让整个管道都是惰性求值的
# - [ ] **思考**：Python 的 `range()`、`map()`、`filter()` 返回的都是惰性对象而不是列表。这和 JS 的设计选择（Array 方法返回新 Array）有什么权衡？

# 📚 **Key docs**: [生成器教程](https://docs.python.org/3/tutorial/classes.html#generators) | [itertools 模块](https://docs.python.org/3/library/itertools.html) | [生成器表达式](https://docs.python.org/3/tutorial/classes.html#generator-expressions)
# > 生成器教程很短但讲清了核心；itertools 是工具箱，先看 chain/islice/groupby 三个就够
import csv
import tracemalloc
from pathlib import Path
from itertools import chain, islice, groupby, count

root = Path(__file__).parent

csv_file_path = root / "assets" / "task4_students.csv"


#### Task4.1
def iter_foreach(arr):
    for item in arr: yield item

def foreach(arr):
    result = []
    for item in arr: 
        result.append(item)
    return result

print(list(iter_foreach(["A", "B", "C"])))
print(list(foreach(["D", "C"])))
print(type(iter_foreach('A')), type(foreach('A')))

# [AI 批注] ✅ 已修正：iter_foreach 改成 `for item in arr: yield item`，去掉了 index
# [AI 批注] ✅ 已修正：foreach 用 result 列表累积后返回，逻辑正确
# [AI 批注] ✅ 已修正：补上了 `type()` 对比，输出 `<class 'generator'> <class 'list'>`，
#                     题目要求的"看见类型差异"达到了。

# [AI 批注] 💡 一个小风格提醒
# 第 33 行 `print(list(foreach(["D", "C"])))` 里的 `list()` 是冗余的——foreach 已经返回 list。
# 直接 `print(foreach(["D", "C"]))` 即可。这种"双重保险"是从 JS 写惯了 `Array.from(...)` 带过来的，
# 在 Python 里看到 list 包 list 通常是一个小信号。

##### Answer:
# 生成器的返回值为什么不是一个 list？"惰性"意味着什么？
# 核心目标：不要一次性把所有结果都算出来，而是在需要的时候再计算。
# 带来的好处：减少内存占用

# [AI 批注] ⚠️ 答案方向对，但还能更具体
# 你抓住了"按需计算 + 省内存"两个点，很好。但还可以补一层机制层面的理解：
# 生成器返回的是 `<generator object>`，它本身不存数据；每次外部 `next()` 才执行到下一个 yield，
# 然后函数"暂停"住，局部变量、PC 都被保留——这就是惰性的实现机制。
# 这个"暂停-恢复"能力，正是 async/await 的基础——后面学异步时会再次见到。

#### Task4.2
tracemalloc.start()                                                                                                                               
data = [i * 2 for i in range(10_000_000)]                                                                                                                       
current, peak = tracemalloc.get_traced_memory()
print(current, peak)
tracemalloc.stop()
del data

tracemalloc.start()                                                                                                                               
gen = (i * 2 for i in range(10_000_000)) 
list(gen)                                                                                                                     
current, peak = tracemalloc.get_traced_memory()
print(current, peak)
tracemalloc.stop()
del gen

# [AI 批注] ✅ 已修正（部分）
# 1) ✅ 数据量改成 10_000_000，输出对比是 ~390MB vs 400B——百万倍差距，效果非常震撼。
# 2) ⚠️ 但生成器还是没被消费过，所以"同时驻留 vs 总处理量"这层洞察还没验证到。
#    建议补一个第三组实验：
#    ```
#    tracemalloc.start()
#    gen2 = (i * 2 for i in range(10_000_000))
#    for _ in gen2: pass   # 把生成器消费一遍
#    print(tracemalloc.get_traced_memory())
#    tracemalloc.stop()
#    ```
#    你会看到峰值也只是几百字节左右——这才是生成器真正的"省内存"含义：
#    不是数据没被处理，而是同一时刻只有一个值在内存里。

#### Task4.3
def read_csv(path):
    with open(path, 'r', encoding='utf-8', newline= '') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar= '"')
        for row in csv_reader:
            yield row

g = read_csv(csv_file_path)
print(next(g))
g.close()

# [AI 批注] ✅ 已修正
# - read_csv 接收 path 参数 ✅
# - 删掉了未使用的 PurePath import ✅
# - 还主动用 `g.close()` 显式关闭生成器——刚好回应了"消费者中途停止时文件可能泄漏"的隐藏问题，
#   这是个 thoughtful 的处理。

# [AI 批注] 💡 顺手一个观察
# 你这次的 demo 改成 `next(g)` + `g.close()`，只读了第一行就关掉——能验证"惰性"特性
# （没有把整个文件加载进来），但失去了原版 `for row in read_csv(...)` 那种"一行行流过"的演示效果。
# 两种风格各有侧重：手动 next/close 适合调试和精确控制；for-loop 适合实际数据处理。
# 真实代码里更常见的是后者（迭代到底，Python 会在生成器结束时自动调用 close）。

#### Task4.4
print(list(chain("ABC", "DEF")))
# 应用场景：传入多个可迭代对象时合并成一个

print(list(islice(count(),2)))
# 应用场景：可以对长度未知可迭代对象进行分片截取


print([(k, list(g)) for k, g in groupby([2,3,4,5,5,1,1])])
# 应用场景：对可迭代对象进行分组

# [AI 批注] ✅ 已修正
# - islice(count(), 2) ✅ 用了无穷迭代器，体现了 islice 的核心价值（普通切片做不到）
# - groupby 例子 [2,3,4,5,5,1,1] + list(g) ✅ 展示了"按连续相邻元素分组"的特性，组内元素也展开了
# - 三个工具都补上了"应用场景"文字答案 ✅

# [AI 批注] ⚠️ groupby 的应用场景描述还可以更精确
# 你写的"对可迭代对象进行分组"还差关键一笔——必须强调**连续相邻**。
# 你的例子里输入是 [2,3,4,5,5,1,1]，5 和 1 都是相邻的所以正常分组；但如果换成 [2,1,2,1,1]，
# 你会得到 4 组（2/1/2/1+1）而不是 2 组（2+2 / 1+1+1）。
# 这是 groupby 最常见的踩坑点——把"连续相邻"四个字加进应用场景描述里，
# 以后用之前就会自动想到"要不要先 sort"。

#### Task4.5
def pipe(*functions, value):
   result = value
   for func in functions:
        result = func(result)
        yield result


add_one = lambda x: x + 1
double  = lambda x: x * 2

f = list(pipe(add_one, double, value = 2))
print(f)

# [AI 批注] ✅ 已修正
# 现在每步 `result = func(result)` 然后 yield，输出是 [3, 6]——pipe 的核心语义对了！
# 这就是真正的"惰性 pipe"：调用者通过 next() 一步步推进，每步都能拿到中间结果。
# 注意一个细节：你保留了原始 value 不变（用 result 作为累积变量），这是好习惯——
# 哪怕在生成器内部，不要污染参数本身，能让函数更可预测。

# [AI 批注] 💡 题目说的"惰性版 pipe"其实有两种理解，都值得想一想
# 1) 修正后这种：每步 yield 中间结果，消费者可以逐步推进——单值流过的管道。
# 2) 更进阶：每个函数本身是生成器变换（接收迭代器、返回迭代器），
#    比如 `lambda gen: (x*2 for x in gen)`。整条流水线处理无穷数据，单个元素从头流到尾，
#    这才是真正的"流式"管道（类似 Unix pipeline `cat | grep | sort`）。
#    Task 3 的 pipe 是接收单个值，这里你可以挑战一下"迭代器→迭代器"形式。

#### Task4.6
# Answer:
# 从 lazy vs eager 思考
# Python iterator/generator 内存恒定，能处理无穷序列
# 真正的权衡是 lazy vs eager：
# - lazy（Python iterator/generator）：内存恒定 O(1)、能处理无穷序列、但只能消费一次。
# - eager 就是一次性把数据全部计算完，然后放在内存中可以反复消费
# 所以是 lazy 还是 eager 取决于应用场景：数据量未知，内存有限使用 lazy，数据量有限，需要反复访问则使用 eager

# [AI 批注] ✅ 已修正：核心概念分离对了
# 你这次抓住了关键的概念切换：从"Python 大数据 vs JS DOM"（错的因果链），
# 切换到了"lazy vs eager"（对的轴）。这一步的进步是这次 review 里最大的——
# 一旦你能用 lazy/eager 这个轴去看，后面学异步迭代、Reactive 流、Rust 的 Iterator
# 都会顺着同一个心智模型展开。

# [AI 批注] 💡 还能补两个细节，让答案更完整
# 1) 题目本来问的是"Python 这种设计 vs JS 的 Array 设计有什么权衡" —— 你回答了 lazy/eager
#    的本质，但没回到 JS 这一侧做对比。可以补一句：JS 的 Array.prototype 默认 eager
#    （`.map().filter()` 立刻物化），但 JS 也有 lazy 版本（迭代器协议、generator function、
#    Iterator Helpers 提案）；并不是"语言天生 lazy/eager"，而是默认选择不同。
# 2) eager 还有一个常被忽略的优点：**链式调用更直观**（`arr.map().filter().reduce()`
#    一行写完）。lazy 在 Python 里如果想链式，要么靠生成器表达式套娃，要么用 `pipe()`
#    这种工具。所以选哪种除了"内存/无穷序列"外，**API 人体工学**也是一个考量。
#
# 一个落地例子：100GB 日志，Python `for line in open(path)` 内存恒定；
# JS `fs.readFileSync(path).split('\n')` 直接 OOM——必须用流（Node Stream / async iterator）才行。
# 这个例子说明：连"DOM 语言"的 JS 在面对大数据时也必须切到 lazy 模式，所以"语言用途"不是根本原因，
# **数据规模和访问模式**才是。


# ============================================================
# [AI 批注] 📊 整体评价（第三轮 review）
# ============================================================
#
# 完成度：★★★★☆ (4.5/5)
# - 4.1: ✅ 完成
# - 4.2: ⚠️ 数据量已改大，但生成器消费实验仍未补
# - 4.3: ✅ 完成
# - 4.4: ✅ 例子和文字答案都补全了，groupby 还差"连续相邻"四个字
# - 4.5: ✅ 完成
# - 4.6: ✅ 概念轴已切换到 lazy vs eager（这次的关键进步）
#
# 代码质量：★★★★☆ (4/5)
# - 整体干净
# - 小残留：第 33 行 `list(foreach(...))` 冗余 list
#
# 理解深度：★★★★☆ (4/5)
# - lazy vs eager 已经成为你看待迭代/求值问题的心智模型——这是真正穿透到本质了
# - pipe 修正 + 显式 close 都体现了对"惰性求值机制"的掌握
# - 还差一层：JS 一侧的对比、eager 在链式 API 上的人体工学优势——属于细节而非概念盲区
#
# 剩余清单（全是优化项，没有概念性错误了）：
# 1. 🟡 Task 4.2 补一段"消费生成器后再测内存"的实验，验证"同时驻留"的含义
# 2. 🟢 Task 4.6 补一句 JS 一侧的对比 + eager 在链式 API 上的人体工学优势
# 3. 🟢 Task 4.4 把"连续相邻"加进 groupby 的应用场景描述
# 4. 🟢 Task 4.1 第 33 行去掉冗余的 list()
# 5. 🟢 Task 4.5 挑战：试试"迭代器→迭代器"形式的真正流式 pipe（可选）
#
# 总评：这一轮把 4.5 和 4.6 这两个红色项都消除了，是质的飞跃。
# 剩下的全是 polish 级别，可以直接进入下一个项目（装饰器）了。