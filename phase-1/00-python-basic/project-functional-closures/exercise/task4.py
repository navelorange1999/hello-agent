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
from pathlib import Path, PurePath
from itertools import chain, islice, groupby

root = Path(__file__).parent

csv_file_path = root / "assets" / "task4_students.csv"


#### Task4.1
def iter_foreach(arr):
    for index in range(len(arr)):
        yield arr[index]

def foreach(arr):
     for index in range(len(arr)):
        return arr[index]
    
for item in iter_foreach(["A", "B", "C"]):
    print(item)

for item in foreach(["D", "C"]):
    print(item)

# [AI 批注] ⚠️ iter_foreach 可以更 Pythonic
# `for index in range(len(arr)): yield arr[index]` 是从 JS 迁移过来的"翻译腔"。
# Python 里直接 `for item in arr: yield item`——根本不需要 index。
# 下次写迭代时先问自己：我真的需要下标吗？

# [AI 批注] ❌ foreach 函数有逻辑 bug
# `return` 写在 for 循环内部，第一次迭代就退出了——所以只返回 arr[0]，循环根本没跑完。
# 题目想让你对比"返回 list 的普通函数 vs yield 的生成器"，但你的"普通版本"既没返回 list、
# 也没遍历完。思考：要返回所有元素，应该用什么累积？什么时候 return？
# 另外，第 28 行缩进比第 29 行多了一个空格（5 vs 4），Python 不报错但风格不一致。

# [AI 批注] ⚠️ 题目要求"对比返回值类型"，但你只 print 了元素
# 加一句 `print(type(iter_foreach(["A"])), type(foreach(["A"])))` 看输出：
# 一个是 `<class 'generator'>`，另一个是 `<class 'str'>`（修正后应该是 `<class 'list'>`）。
# 这才是题目想让你"看见"的差异。

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
data = [i * 2 for i in range(1000)]                                                                                                                       
current, peak = tracemalloc.get_traced_memory()
print(current, peak)
tracemalloc.stop()
del data

tracemalloc.start()                                                                                                                               
gen = (i * 2 for i in range(1000))                                                                                                                      
current, peak = tracemalloc.get_traced_memory()
print(current, peak)
tracemalloc.stop()
del gen

# [AI 批注] ⚠️ 数据量太小，而且生成器没被消费
# 1) 题目说"非常大的数据量" —— 1000 太小了。试试 `range(10_000_000)`，list 会涨到几百 MB，
#    生成器仍然几百字节。这种数量级差距才能让你"感受"到惰性的价值。
# 2) 关键洞察：生成器只占 ~400B，是因为它根本没被消费过。如果你 `list(gen)` 把它消费一遍，
#    内存会和 list 推导式一样。**生成器省的是"同时驻留"的内存，不是"总处理量"**。
#    试一下：`for _ in gen: pass`，再测一次峰值——你会发现峰值并不会涨多少（每次只留一个值）。

#### Task4.3

def read_csv():
    with open(csv_file_path, 'r', encoding='utf-8', newline= '') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar= '"')
        for row in csv_reader:
            yield row

for row in read_csv():
    print(row)

# [AI 批注] ✅ with + yield 的惰性 CSV 读取模式正确
# 文件一行读一行，内存里始终只保留当前行——这正是题目要的"10GB 文件也能处理"的方案。

# [AI 批注] ⚠️ 两个可以更进一步的点
# 1) `yield` 在 `with` 块里，意味着只要消费者还在迭代，文件就保持打开。如果消费者中途 break
#    又不让生成器被 GC，文件可能短暂泄漏。搜索关键词：
#    "generator with statement file leak" / "contextlib.closing"。生产代码常见 footgun。
# 2) `read_csv()` 硬编码了路径，无法复用。改成 `def read_csv(path):` 才是惰性读取器的标准签名。
#    顺便：`PurePath` 在第 14 行被 import 但全文没用到，可以删掉。

#### Task4.4
for item in chain(
    "ABC", "DEF"
):
    print(item)


for item in islice(
    ("ABC", "DEF"),
    1
):
    print(item)

for item in groupby(
    ("ABC", "DEF")
):
    print(item)

# [AI 批注] ⚠️ chain 演示对了，但 islice 和 groupby 的例子没体现"杀手级"用途
# - chain ✅：把多个可迭代对象拼成一个。
# - islice 的真正价值：**生成器/无穷迭代器无法用 `[:n]` 切片**，islice 是唯一办法。
#   试试：`from itertools import count; list(islice(count(), 5))` —— 从无穷计数器里取 5 个。
#   你现在的例子 `islice(("ABC", "DEF"), 1)` 用普通切片也能做，没体现 islice 的存在意义。
# - groupby 的真正价值：按 key 分组**连续相邻**的元素（注意：不会自动排序！）。
#   试试 `[(k, list(g)) for k, g in groupby([1,1,2,2,1,1])]` —— 你会看到 1 出现两次（不连续就分两组）。
#   想正确分组要么先排序，要么传 `key=` 参数。
#   还有：你的例子里没消费 grouper（那个 `<itertools._grouper object>`），所以看不到组内元素，
#   要 `list(g)` 才能展开。

# [AI 批注] ❌ 题目要求"它们分别解决什么问题？"，你没写答案
# 用一两句话总结这三个工具的应用场景，写下来才会真正记住。这种"思考题"是题目设计的核心，
# 不是可选项。

#### Task4.5
def pipe(*functions, value):
   for func in functions:
        yield func(value)


add_one = lambda x: x + 1
double  = lambda x: x * 2

f = list(pipe(add_one, double, value = 2))
print(f)

# [AI 批注] ❌ 这不是 pipe —— 重大概念错误
# 你的输出是 [3, 4] = [add_one(2), double(2)]，每个函数都拿到同一个 value=2。
# 但 pipe 的核心定义是："前一个函数的输出作为后一个函数的输入"，应该是 double(add_one(2)) = 6。
# 思考：循环里要怎么改才能让 value 一步步被替换？提示：每次 yield 之前更新 value。
# 修正后输出应该是 [3, 6]：先 add_one(2)=3，再 double(3)=6，每一步都 yield 中间结果。

# [AI 批注] 💡 题目说的"惰性版 pipe"其实有两种理解，都值得想一想
# 1) 修正后这种：每步 yield 中间结果，消费者可以逐步推进——单值流过的管道。
# 2) 更进阶：每个函数本身是生成器变换（接收迭代器、返回迭代器），
#    比如 `lambda gen: (x*2 for x in gen)`。整条流水线处理无穷数据，单个元素从头流到尾，
#    这才是真正的"流式"管道（类似 Unix pipeline `cat | grep | sort`）。
#    Task 3 的 pipe 是接收单个值，这里你可以挑战一下"迭代器→迭代器"形式。

#### Task4.6
# Answer:
# Python 常用于做大数据集的处理，所以对大数据集处理时的性能会有比较严格的要求。而 JS 更偏向操作网页 DOM，需要数据返回新的内存地址，避免操作旧地址

# [AI 批注] ❌ 答案方向不准确，把几个不同的概念混在了一起
# 1) "Python 常用于大数据所以要惰性" —— 倒因为果。惰性求值是 Python 通用的迭代抽象（Python 3
#    里 range/map/filter/zip 全部惰性化），不是为了"大数据"专门设计的。
# 2) "JS 数组方法返回新数组是为了避免操作旧地址" —— 把不可变性（immutability）和惰性（laziness）
#    混淆了。JS `.map().filter()` 立刻物化是 **eager 求值**；返回新数组是 **immutability** 的
#    函数式编程习惯，和 DOM 操作没有直接关系。
#
# 真正的权衡是 lazy vs eager：
# - 惰性（Python iterator/generator）：内存恒定 O(1)、能处理无穷序列、但只能消费一次、
#   没有 `len()`、调试更难。
# - 急切（JS Array）：可重复迭代、能链式 `.map().filter()`、有 `.length`，
#   但内存 O(n)、不能处理无穷序列。
#
# JS 也有惰性版本：Iterator 协议、generator function、新提案的 Iterator Helpers
# （`Array.prototype` 是 eager，迭代器是 lazy）。Python 也有 eager 版本（list 推导式）。
# 选哪种取决于：是否需要重复遍历？数据是否能放进内存？是否需要中间链式调用？
#
# 一个具体例子：100GB 日志，Python `for line in open(path)` 内存恒定；
# JS `fs.readFileSync(path).split('\n')` 直接 OOM——必须用流（lazy）才行。


# ============================================================
# [AI 批注] 📊 整体评价
# ============================================================
#
# 完成度：★★★☆☆ (3/5)
# - 4.1: 主体可运行但 foreach 函数有 bug，类型对比没做
# - 4.2: 实验跑通但数据量过小、生成器未消费导致对比不充分
# - 4.3: ✅ 基本完成
# - 4.4: chain/islice/groupby 都跑通了但例子没体现核心用途，文字回答缺失
# - 4.5: ❌ pipe 实现错误（值没传递）
# - 4.6: 答案存在概念混淆
#
# 代码质量：★★★☆☆ (3/5)
# - 整体能跑、结构清晰
# - 有几处"JS 翻译腔"（range(len(arr))）和未使用的 import（PurePath）
# - 第 28 行有缩进不一致（虽然不报错）
#
# 理解深度：★★☆☆☆ (2/5)
# - 抓住了"惰性 = 按需计算 + 省内存"的表层
# - 但对生成器机制（暂停-恢复）、惰性 vs 不可变性的区分、islice/groupby 的核心用途
#   都还没穿透到位
#
# 需要修正的几件事（按优先级）：
# 1. 🔴 Task 4.5 pipe 没在传递值——修正后再跑一次，确认输出是 [3, 6] 而不是 [3, 4]
# 2. 🔴 Task 4.6 答案概念混淆——重写一版，把 lazy vs eager 和 mutable vs immutable 分开
# 3. 🟡 Task 4.1 foreach 函数的 return-in-loop bug，顺便补上类型对比的 print
# 4. 🟡 Task 4.4 补上 islice/groupby 的"为什么需要它"的文字答案
# 5. 🟡 Task 4.2 把数据量改大（10_000_000），并消费一次生成器看真实内存
# 6. 🟢 Task 4.3 把 read_csv 改成接收 path 参数；删除未用的 PurePath import
# 7. 🟢 Task 4.5 挑战：试试"迭代器→迭代器"形式的真正流式 pipe