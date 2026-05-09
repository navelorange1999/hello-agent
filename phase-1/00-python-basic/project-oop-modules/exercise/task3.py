# ### Task 3：异常处理（Day 2）

# - [ ] 用 `try/except/else/finally` 处理常见错误。**注意**：Python 的 try 有 `else` 分支——它在没有异常时执行。**思考**：JS 的 try/catch 没有 else，Python 为什么加了这个？把"正常逻辑"放在 else 里和放在 try 里有什么区别？
# - [ ] 定义自定义异常类（例如 `TaskNotFoundError`）。搜索 Python 异常的继承体系，理解为什么自定义异常要继承 `Exception` 而不是 `BaseException`
# - [ ] 搜索 EAFP 和 LBYL 两种编程风格。**思考**：JS 社区倾向于"先检查再操作"（LBYL），Python 社区倾向于"先操作，出错再处理"（EAFP）——为什么？这两种风格各有什么性能和可读性上的权衡？
# - [ ] 用 `with` 语句管理文件操作中的资源释放。回顾 P0-1 中使用的 `with`，现在深入理解它背后的上下文管理器协议（`__enter__` 和 `__exit__`）
# - [ ] 给任务管理器添加完整的错误处理：文件不存在、JSON 格式错误、任务未找到——每种情况抛出不同的异常

# 📚 **Key docs**: [错误和异常教程](https://docs.python.org/3/tutorial/errors.html) | [with 语句上下文管理器](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement) | [内置异常层级](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
# > 错误教程从头到尾读一遍，特别注意 else 子句；异常层级图谱帮你理解为什么自定义异常继承 Exception


#### Task3.1
# try / except / else / finally 完整四件套
# 思考：把"正常逻辑"放在 try 里 vs else 里，差别在哪？（提示：异常的捕获范围）


#### Task3.2
# 自定义异常 TaskNotFoundError，继承 Exception
# 思考：为什么不能继承 BaseException？（提示：BaseException 还包括 KeyboardInterrupt / SystemExit）


#### Task3.3
# EAFP vs LBYL：写两个版本读取嵌套字典
# - LBYL：if "key" in d and "subkey" in d["key"]: ...
# - EAFP：try: d["key"]["subkey"] except KeyError: ...
# 思考：竞态条件下哪种更安全？


#### Task3.4
# 自己写一个 Context Manager（用 class + __enter__/__exit__，或者 @contextmanager）
# 比如：一个计时器、一个临时切换工作目录的工具


#### Task3.5
# 给任务管理器接上完整错误处理：FileNotFoundError / JSONDecodeError / TaskNotFoundError 各自的处理路径

##### Answer:
# 1) try 的 else 分支解决了什么问题？
# 2) 为什么自定义异常要继承 Exception 而不是 BaseException？
# 3) EAFP vs LBYL 的权衡（性能 / 可读性 / 并发安全性）：
# 4) 上下文管理器协议（__enter__/__exit__）和 try/finally 的关系：
