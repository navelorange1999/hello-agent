# ### Task 2：魔术方法与继承（Day 1-2）

# - [ ] 实现 `__str__` 和 `__repr__`，让 `print(task)` 和在 REPL 里直接输入 `task` 显示不同的内容。**思考**：为什么 Python 要区分 `str` 和 `repr`？它们各自的目标受众是谁？
# - [ ] 实现 `__eq__`，让两个标题相同的 Task 被认为是相等的。然后尝试把 Task 放进 set——会发生什么？你需要额外实现什么？
# - [ ] 创建一个 `TaskList` 类，实现 `__len__`、`__getitem__`、`__iter__`，让它支持 `len()`、下标访问和 for 循环。**思考**：这就是 Python 的"鸭子类型"——只要实现了对应的魔术方法，你的对象就能像内置类型一样使用。这和 JS 的 Symbol.iterator 有什么异同？
# - [ ] 创建 `UrgentTask` 子类继承 `Task`，添加 deadline 属性，覆盖显示方法。使用 `super()` 调用父类的 `__init__`
# - [ ] 搜索 Python 的多继承和 MRO（方法解析顺序）。**思考**：JS 不支持多继承是因为"菱形问题"，Python 用 C3 线性化解决了这个问题——但多继承在实践中推荐使用吗？

# 📚 **Key docs**: [数据模型 — 特殊方法](https://docs.python.org/3/reference/datamodel.html#special-method-names) | [super() 函数](https://docs.python.org/3/library/functions.html#super)
# > 数据模型文档是 Python 魔术方法的完整参考，先看 __str__/__repr__/__eq__/__hash__ 相关部分；super 文档配合 MRO 一起理解


#### Task2.1
# __str__ / __repr__ —— 验证 print(task) vs repr(task) 输出不同


#### Task2.2
# __eq__ + __hash__ —— 试 set([task_a, task_b])，观察发生了什么


#### Task2.3
# TaskList：__len__ / __getitem__ / __iter__
# 验证 len(tl) / tl[0] / for t in tl: 都能用


#### Task2.4
# UrgentTask(Task)：用 super().__init__(...) 调用父类，加 deadline


#### Task2.5
# 多继承实验：写两个 mixin，看 MRO（__mro__ 或 ClassName.mro()）
# 思考：什么时候多继承 < 组合（composition）？

##### Answer:
# 1) __str__ vs __repr__ 的目标受众：
# 2) 只实现 __eq__ 不实现 __hash__ 时，set 会怎样？
# 3) Python 鸭子类型 vs JS Symbol.iterator 的异同：
# 4) 多继承在实践中是否推荐？为什么？
