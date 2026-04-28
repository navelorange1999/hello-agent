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


#### Task3.2


#### Task3.3


#### Task3.4


#### Task3.5


#### Task3.6
