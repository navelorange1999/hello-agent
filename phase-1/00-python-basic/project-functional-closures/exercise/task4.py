# ### Task 4：生成器与惰性求值（Day 2-3）

# - [ ] 写一个普通函数和一个使用 `yield` 的生成器函数，对比它们的返回值类型。**思考**：生成器的返回值为什么不是一个 list？"惰性"意味着什么？
# - [ ] 对比列表推导式和生成器表达式（方括号 vs 圆括号）的内存占用。用一个非常大的数据量来测试——观察内存差异
# - [ ] 实现一个惰性文件读取器：逐行读取大文件，每次只在内存中保留一行。**思考**：如果文件有 10GB，一次性读入内存会怎样？你的生成器方案为什么能处理？
# - [ ] 搜索并实验 `itertools` 中的 `chain`、`islice`、`groupby`。它们分别解决什么问题？
# - [ ] 实现一个惰性版的 pipe：用生成器串联多个处理步骤，让整个管道都是惰性求值的
# - [ ] **思考**：Python 的 `range()`、`map()`、`filter()` 返回的都是惰性对象而不是列表。这和 JS 的设计选择（Array 方法返回新 Array）有什么权衡？

# 📚 **Key docs**: [生成器教程](https://docs.python.org/3/tutorial/classes.html#generators) | [itertools 模块](https://docs.python.org/3/library/itertools.html) | [生成器表达式](https://docs.python.org/3/tutorial/classes.html#generator-expressions)
# > 生成器教程很短但讲清了核心；itertools 是工具箱，先看 chain/islice/groupby 三个就够

#### Task4.1


#### Task4.2


#### Task4.3


#### Task4.4


#### Task4.5


#### Task4.6
