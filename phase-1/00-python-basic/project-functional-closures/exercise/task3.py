# ### Task 3：构建函数管道（Day 2）

# - [ ] 从零实现 `my_map(fn, iterable)`——不使用内置 `map`，手动迭代并应用函数
# - [ ] 从零实现 `my_filter(fn, iterable)` 和 `my_reduce(fn, iterable, initial)`
# - [ ] 实现 `pipe(*functions)`——接收任意数量的函数，返回一个新函数，依次从左到右执行所有传入的函数。**思考**：管道里前一个函数的输出是后一个函数的输入，怎么保证类型兼容？
# - [ ] 实现 `compose(*functions)`——和 pipe 方向相反，从右到左执行
# - [ ] 用你的 pipe 组合一个数据处理流程：过滤活跃用户 -> 提取姓名 -> 排序。**思考**：pipe 和 compose 各自适合什么场景？在数据处理管道中你更倾向用哪个？为什么？
# - [ ] **挑战**：实现一个 `memoize(fn)` 缓存函数——对相同参数返回缓存结果而不重复计算。你需要考虑：用什么数据结构存缓存？参数不可哈希怎么办？

# 📚 **Key docs**: [functools.lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache) | [*args 和 **kwargs](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists)
# > 先自己实现 memoize，然后再读 lru_cache 看官方是怎么做的——对比你的方案和官方的差距；*args 是实现 pipe 的关键

#### Task3.1
def my_map(fn, iterable):
    return [fn(item) for item in iterable]

print(my_map(lambda item: f"Add Prefix: {item}", [1, 2, 3]))
# [AI 批注] ✅ 简洁正确。列表推导是 Pythonic 的写法。
# 💡 进阶思考：内置 map() 返回的是迭代器（lazy），你的实现返回 list（eager）。
#    在大数据场景下两者性能差异很大——可以查一下 generator expression
#    `(fn(item) for item in iterable)`，看看怎么改造成 lazy 版本。

#### Task3.2
def my_filter(fn, iterable):
    arr = []
    for item in iterable:
        if fn(item):
            arr.append(item)
    return arr
# [AI 批注] ✅ 已修正（缩进统一为 4 空格）。

print(my_filter(lambda item: item % 2 == 0, [1, 2, 3, 4]))

def my_reduce(fn, iterable, initial):
    result = initial
    for item in iterable:
        result = fn(result, item)
    return result
# [AI 批注] ✅ 三参数 reduce 的标准实现。
# 💡 思考：如果不传 initial（即两参数版本），iterable 为空时该返回什么？
#    functools.reduce 的处理方式是抛 TypeError——可以查一下源码看为什么这样设计。

print(my_reduce(
    lambda acc, current: acc + current,
    [1, 2, 3, 4],
    10
))

#### Task3.3
def pipe(*functions):
    def output(value):
        result = value
        for func in functions:
            result = func(result)
        return result
    return output
# [AI 批注] ✅ 闭包 + *args 的经典组合，结构清晰。
# ✅ 已修正：`input` → `value`，避免遮蔽内置。
# 💡 思考：题目问「怎么保证类型兼容？」——你这个实现完全没做类型检查。
#    那么是谁来保证？答案：调用者。这就是函数式编程「约定优于检查」的哲学，
#    类型兼容靠组合时的设计责任，而不是运行时校验。如果想加静态检查，
#    可以查一下 `typing.Callable` 和 PEP 612 的 ParamSpec。

add_one = lambda x: x + 1
double  = lambda x: x * 2

f = pipe(add_one, double)
print(f(3))  # excepted: 8

#### Task3.4
def compose(*functions):
    count = len(functions)
    def output(input):
        result = input
        for index in range(len(functions)):
            result = functions[count - index - 1](result)
        return result
    return output
# [AI 批注] ⚠️ 结果对，但实现绕了远路。你在用「正向索引 + 算术反转」模拟反向遍历，
#    Python 已经给了更直接的工具：
#      - `for func in reversed(functions):`  ← 直接反向迭代
#      - `functions[::-1]`                    ← 切片反转
#    本质上 compose 就是 pipe 的反向版，最优雅的写法是复用：
#      `return pipe(*reversed(functions))`
#    一行搞定。这就是函数式编程「组合大于重复实现」的精髓。
# 💡 思考：题目问「pipe 和 compose 各自适合什么场景？」
#    - pipe：数据处理流水线（filter → map → sort），符合从左到右的阅读顺序
#    - compose：数学风格的函数组合 f(g(h(x)))，更接近代数表达
#    实际工程里 pipe 用得更多（人类阅读友好），compose 在 FP 语言里常见。

add_one = lambda x: x + 1
double  = lambda x: x * 2

f = compose(add_one, double)
print(f(3))  # excepted: 7

#### Task3.5
users = [                                                                                                                                       
      {"name": "Charlie", "active": True},                                                                                                          
      {"name": "Alice",   "active": True},                                                                                                          
      {"name": "Bob",     "active": False},                                                                                                         
      {"name": "Eve",     "active": True},                                                                                                          
      {"name": "Dave",    "active": False},                                                                                                         
      {"name": "Frank",   "active": True},                                                                                                          
  ]

# 期望输出：["Alice", "Charlie", "Eve", "Frank"]
print(pipe(
    lambda x: my_filter(lambda user: user.get("active") == True, x),
    lambda x: my_map(lambda user: user["name"], x),
    lambda x: sorted(x)
)(users))
# [AI 批注] ❌ 输出对不上题目要求。
#    期望：["Alice", "Charlie", "Eve", "Frank"]            （字符串列表）
#    实际：[{'name': 'Alice'}, {'name': 'Charlie'}, ...]    （字典列表）
#
#    问题在 my_map 里：你写的是 `{"name": user.get("name")}`——把 name
#    取出来又包回字典里了。题目是「提取姓名」，应该直接返回字符串：
#        lambda user: user["name"]
#
#    顺带几个细节：
#    ⚠️ `user.get("active") == True` → 直接 `user.get("active")` 即可，
#       Python 里 `if x == True` 是反模式（等价于 `if x` 但多此一举，
#       且对 `1 == True` 这种边界值行为不一致）。
#    ⚠️ 排序在最后一步，但如果先排序再 map，sorted 处理的对象更小（字符串
#       比较比 dict.get 快）——思考：哪些操作的顺序可以换？换了之后性能
#       差异有多大？这是流水线优化的常见话题。

#### Task3.6
call_count = 0

def add_func(a, b):
    global call_count
    call_count += 1
    print(f"call_count: {call_count}")
    return a + b

def memo(fn):
    cache = {}

    def cached_fn(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        
        cache_result = cache.get(key)
        # if hit cache, return result
        if key in cache:
            return cache_result
            # else calculate and add result to cache
        else:
           result = fn(*args, **kwargs)
           cache[key] = result
           return cache[key]
    return cached_fn
# [AI 批注] ✅✅✅ 第三轮：核心 bug 全部修复，结构干净利落！
#
# ✅ Bug 1（key 碰撞）：args tuple 直接当 key，无碰撞
# ✅ Bug 2（None 污染）：`if key in cache:` 用对了
# ✅ Bug 3（kwargs 支持）：`frozenset(kwargs.items())` 顺序无关
# ✅ 新 Bug A（args+kwargs 互斥）：合并成 (args, frozenset(...)) 解决
# ✅ 新 Bug B（无参 NameError）：合并方案天然解决
# ✅ kwargs 啰嗦写法：直接 `frozenset(kwargs.items())`，简洁
# ✅ `*args, **kwargs` 空格规范：修了
#
# 现在这个 memo 已经是工程可用的版本了。👏
#
# ─────────── 还能再优化的两个小细节 ───────────
#
# 🟢 优化 1：`cache_result = cache.get(key)` 这行冗余
#    既然下面用 `if key in cache:` 判断，命中时直接 `return cache[key]` 就行：
#        if key in cache:
#            return cache[key]
#        result = fn(*args, **kwargs)
#        cache[key] = result
#        return result
#    省一次 dict 查找，且去掉 if/else 显得更线性。
#
# 🟢 优化 2：return cache[key] 也可以直接 return result
#    cache[key] 刚被赋值为 result，多查一次哈希表没意义。
#
# ─────────── 没处理但可以思考的设计问题 ───────────
#
# ⚠️ 不可哈希参数：`cached_fn([1,2,3])` 仍会抛 TypeError。
#    思考方向（无标准答案）：
#      - 方案 A：try/except，不可哈希时直接调用不缓存
#      - 方案 B：用 repr(args) 当 key（牺牲性能换通用性）
#      - 方案 C：让它崩——这是 functools.lru_cache 的选择
#    现在去读 functools.lru_cache 的 _make_key 源码，对比你的方案——
#    你会发现官方处理得比你简单：用 `tuple(sorted(kwargs.items()))` 而不是
#    frozenset（顺序敏感），并用 `_HashedSeq` 类缓存哈希值（性能优化）。
#    思考：为什么官方选顺序敏感？什么场景下你的 frozenset 方案更合适？

cached_add = memo(add_func)

print(cached_add(11, 2))
print(cached_add(1, 12))

print(cached_add(a=2, b=1))
print(cached_add(b=1, a=2))


# [AI 批注] ✅ 测试用例覆盖核心场景：
#    call_count: 1 → 13   args=(11,2)
#    call_count: 2 → 13   args=(1,12)，验证旧 key 碰撞 bug 已修
#    call_count: 3 → 3    a=2,b=1，第一次
#                  3      b=1,a=2，frozenset 顺序无关 → 缓存命中 ✅
#
# 还可以补的几个用例（自选）：
#    # args + kwargs 混用
#    print(cached_add(1, 2))         # call_count++
#    print(cached_add(1, 2, c=99))   # 不同签名，应该 call_count++（不会撞缓存了 ✅）
#
#    # 无参调用（旧版会 NameError，现在能跑）
#    @memo
#    def now(): return 42
#    print(now()); print(now())   # 第二次命中缓存
#
#    # None 返回值不污染缓存
#    @memo
#    def returns_none(x): return None
#    returns_none(1); returns_none(1)   # fn 只被调用一次
#
# 现在去读 functools.lru_cache 的 _make_key 源码——你会发现官方用
# `tuple(sorted(kwargs.items()))` 而不是 frozenset。思考为什么。


# ============================================================
# [AI 批注] 📊 整体评价（第 3 轮 review）
# ============================================================
#
# 完成度：★★★★★ (5/5) ↑
# - 6 个核心子任务全部完成，输出全部符合预期 ✅
# - memo 的所有硬 bug 都修了，工程可用
# - 不可哈希参数的设计权衡未实现，但这是开放题
#
# 代码质量：★★★★☆ (4/5) 持平
# - memo 主结构现在干净利落，args+kwargs 合并方案优雅 ✅
# - pipe / my_filter / my_reduce / my_map：标准 Pythonic 写法
# - 还能小优化：`cache_result = cache.get(key)` 冗余、return 可以省一次查找
# - 没修的小事：Task 3.4 compose 仍可简化、Task 3.5 `== True` 反模式
#
# 理解深度：★★★★★ (5/5) ↑
# - 「frozenset 解决顺序无关」的认知突破 ✅
# - 「(k,v) tuple 打包保留对应关系」想通了 ✅
# - 「args 和 kwargs 是同一次调用的两部分」也理解到位了 ✅
# - 闭包 + 高阶函数 + 不可变容器选型，整套体系闭环
#
# ─────────── 剩下的可选优化 ───────────
#
# 1. 🟢 Task 3.6：删掉冗余的 cache_result，逻辑更线性
# 2. 🟢 Task 3.5：`user.get("active") == True` → `user.get("active")`
# 3. 🟢 Task 3.4：compose 简化成 `return pipe(*reversed(functions))`
# 4. 🟢 Task 3.6：去读 functools.lru_cache 的 _make_key 源码，
#    对比你的方案——尤其注意官方用 `tuple(sorted(kwargs.items()))`
#    而不是 frozenset，思考顺序敏感 vs 顺序无关的工程取舍
#
# ─────────── 已修正的项 ✅ ───────────
# - Task 3.2：缩进统一
# - Task 3.3：`input` → `value`
# - Task 3.5：my_map 返回字符串
# - Task 3.6 全部硬 bug：key 碰撞、None 污染、kwargs 支持、
#   args+kwargs 互斥、无参 NameError、kwargs 啰嗦、空格规范
#
# 推荐延伸：
# - 读 functools.lru_cache 源码的 _make_key、_HashedSeq、kwd_mark
# - 思考：lru_cache 的 maxsize（LRU 淘汰）你的 memo 没做——什么场景需要？
#   提示：长期运行的服务里，无界缓存会变成内存泄漏
# - 进阶：functools.cache vs lru_cache(maxsize=None) 的实现差异
#
# 总结：从第 1 轮的「思路对但实现处处是坑」到第 3 轮的「工程可用」——
# 你完整经历了一个工具函数从原型到健壮的过程。
# 这种「自己踩坑、修坑、再读官方对比」的循环，比直接抄 lru_cache 学到的
# 多 10 倍。下一步建议挑战：给你的 memo 加上 maxsize（LRU 淘汰），
# 自然会引出 OrderedDict / 双向链表 / dict 的插入顺序保留等知识点。