# ### Task 3：异常处理（Day 2）

# - [ ] 用 `try/except/else/finally` 处理常见错误。**注意**：Python 的 try 有 `else` 分支——它在没有异常时执行。**思考**：JS 的 try/catch 没有 else，Python 为什么加了这个？把"正常逻辑"放在 else 里和放在 try 里有什么区别？
# - [ ] 定义自定义异常类（例如 `TaskNotFoundError`）。搜索 Python 异常的继承体系，理解为什么自定义异常要继承 `Exception` 而不是 `BaseException`
# - [ ] 搜索 EAFP 和 LBYL 两种编程风格。**思考**：JS 社区倾向于"先检查再操作"（LBYL），Python 社区倾向于"先操作，出错再处理"（EAFP）——为什么？这两种风格各有什么性能和可读性上的权衡？
# - [ ] 用 `with` 语句管理文件操作中的资源释放。回顾 P0-1 中使用的 `with`，现在深入理解它背后的上下文管理器协议（`__enter__` 和 `__exit__`）
# - [ ] 给任务管理器添加完整的错误处理：文件不存在、JSON 格式错误、任务未找到——每种情况抛出不同的异常

# 📚 **Key docs**: [错误和异常教程](https://docs.python.org/3/tutorial/errors.html) | [with 语句上下文管理器](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement) | [内置异常层级](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
# > 错误教程从头到尾读一遍，特别注意 else 子句；异常层级图谱帮你理解为什么自定义异常继承 Exception

from datetime import datetime
import time
from pathlib import Path, PurePath
import csv
import json


#### Task3.1
# try / except / else / finally 完整四件套
# 思考：把"正常逻辑"放在 try 里 vs else 里，差别在哪？（提示：异常的捕获范围）
def divide(x, y):
    try:
        result = x / y
        # print(undefined_var)
    except ZeroDivisionError:
        print("division by zero!")
    except TypeError:
        print("unsupported operand type(s)")
    except Exception:
        print("Exception")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)

divide(2, 0)

divide("2", "1")

# [AI 批注] ✅ 已修正 —— print(undefined_var) 注释掉后，divide(2,1) 正确走到 else 分支：
#   result is 2.0
#   executing finally clause
#   division by zero!
#   executing finally clause
#   unsupported operand type(s)
#   executing finally clause
# 这就是 else 分支的核心价值：把"成功路径"的代码隔离出来，让 except 只兜住
# "被保护的可能出错的那一行"。把实验对比的观察补到答题区 #1 会更扎实。


#### Task3.2
# 自定义异常 TaskNotFoundError，继承 Exception
# 思考：为什么不能继承 BaseException？（提示：BaseException 还包括 KeyboardInterrupt / SystemExit）
class TaskNotFoundError(Exception):
    pass

try:
    raise TaskNotFoundError("TEST")
except TaskNotFoundError:
    print("catch TaskNotFoundError")

# [AI 批注] ✅ 已修正 —— class 体改回 `pass`，并补了一个 raise/except 小测试，
# 输出："catch TaskNotFoundError"。这说明自定义异常已经具备最小可用形态。
# 💡 进阶思考（不用现在做）：如果想让异常携带更多上下文（比如 task_id），
# 标准做法是重写 __init__(self, task_id) 并调 super().__init__(f"...{task_id}")，
# 这样 str(e) 才能给出有意义的信息。等做完 Task 3.5 顶层处理时会用得到。

#### Task3.3
# EAFP vs LBYL：写两个版本读取嵌套字典
# - LBYL：if "key" in d and "subkey" in d["key"]: ...
# - EAFP：try: d["key"]["subkey"] except KeyError: ...
# 思考：竞态条件下哪种更安全？
d = {
    "key": {
        "sub_key": "Hello World!"
    }
}

d1 = {
    "key": {}
}

d2 = {}

if "key" in d and "sub_key" in d["key"]: 
    print(d["key"]['sub_key'])
else:
    print("LBYL: Missing key")
try:
    print(d["key"]['sub_key'])
except KeyError:
    print("EAFP: Missing key")

if "key" in d1 and "sub_key" in d1["key"]: 
    print(d1["key"]['sub_key'])
else:
    print("LBYL: Missing key")
try:
    print(d1["key"]['sub_key'])
except KeyError:
    print("EAFP: Missing key")


if "key" in d2 and "sub_key" in d2["key"]: 
    print(d2["key"]['sub_key'])
else:
    print("LBYL: Missing key")

try:
    print(d2["key"]['sub_key'])
except KeyError:
    print("EAFP: Missing key")

# [AI 批注] ✅ 已修正 —— LBYL 和 EAFP 都补齐了 else / except 分支。当前输出：
#   Hello World!        ← LBYL on d  (命中)
#   Hello World!        ← EAFP on d  (命中)
#   LBYL: Missing key   ← LBYL on d1 (else 分支)
#   EAFP: Missing key   ← EAFP on d1 (KeyError caught)
#   LBYL: Missing key   ← LBYL on d2 (else 分支)
#   EAFP: Missing key   ← EAFP on d2 (KeyError caught)
# 现在两种风格的对照很干净——每个场景两种风格都给出明确反馈。
#
# [AI 批注] 💡 第三种 Pythonic 写法值得动手试一下：d.get("key", {}).get("sub_key")
#   - 试试在 d2 上跑，看返回什么；
#   - 再造一个 d3 = {"key": "not a dict"}，看 .get 链怎么炸——
#     这就是 .get 默认值的陷阱（中间层不是 dict 会 AttributeError）。
# 这次实验观察的 EAFP/LBYL 性能与并发权衡，可以汇总到答题区 #3。


#### Task3.4
# 自己写一个 Context Manager（用 class + __enter__/__exit__，或者 @contextmanager）
# 比如：一个计时器、一个临时切换工作目录的工具
class ContextManager:
    def __enter__(self):
        self.now = datetime.now()
        return self

    def __exit__(self, exc_type, exc, tb):
        print(f"loaded: {datetime.now() - self.now}")
        print(exc_type, exc, tb)
        return True


with ContextManager() as CM:
    time.sleep(1)
    raise ValueError("boom")


# [AI 批注] ✅ 已修正（上一稿的 ⚠️ 标错了）—— raise 和 return True 都已经激活。
# 实测输出（相当于"实验 C"）：
#   loaded: 0:00:01.002492
#   <class 'ValueError'> boom <traceback object at 0x...>
# 这一次同时观察到了两个关键事实：
#   1) __exit__ 收到了 (ValueError, ValueError("boom"), tb) —— 三个参数与异常一一对应；
#   2) return True 把异常"吞掉"了 —— with 块外的代码继续运行，程序没崩。
#
# [AI 批注] 💡 现在差最后一个对照实验（不用改代码，脑子里推一下就行）：
#   - 如果把 return True 改成 return False（或 return None / 不写 return）：
#     __exit__ 仍然会被调用、清理逻辑仍然会执行，但异常会**继续向上抛**，
#     调用方还得自己 try/except。
#   - 这就是 __exit__ 返回值的"语义开关"：True = 吞，False/None = 透传。
#   - 真实工程里默认应该返回 False —— 沉默吞异常是隐藏 bug 的常见手法。
# 把这条"返回值控制异常是否透传"的结论也补进答题区 #4。

#### Task3.5
# 给任务管理器接上完整错误处理：FileNotFoundError / JSONDecodeError / TaskNotFoundError 各自的处理路径
class TaskManager:
    def get_task(self, filename: str, task_id: str):
        root = Path(__file__).parent
        file_path = root / 'assets' / filename
        try:
            with open(file_path, "r", newline='') as csv_file:
                try:
                    data = list(csv.DictReader(csv_file))
                except csv.Error:
                    print("csv Error")
                else:
                    try:
                        task = self.find_task(task_id, data)
                    except TaskNotFoundError:
                        print("TaskNotFound")
                    else:
                        print(task)
                        return task

        except FileNotFoundError:
            print(f'Not found: {filename}')

    def find_task(self, id, tasks):
        result = next((task for task in tasks if task["task_id"] == id), None)
        if result is None:
            raise TaskNotFoundError
        else:
            return result
 
            

TaskManager().get_task('task3_csv_file.csv', "1")


# [AI 批注] ✅ 已修正（4 项全部）—— 上次提的 4 个打磨点都改完了：
#   1) except csv.Error      ← 异常类型与读的格式（CSV）对齐了
#   2) result is None         ← 身份比较，符合 PEP 8
#   3) return task            ← find_task 现在能把 task 还给调用方
#   4) except TaskNotFoundError ← get_task 内部接住了，999 用例不再崩
# 实测三种失败路径都不崩：
#   - id="1"   → 返回 {'task_id': '1', ...}
#   - id="999" → 打印 "TaskNotFound"，返回 None
#   - 文件缺失 → 打印 "Not found: nope.csv"，返回 None
#
# [AI 批注] 💡 但还有一处值得思考的设计裂缝（不算 bug，是分层问题）：
#   现在三种失败的"反馈方式"都是 `print + 隐式 return None`。这导致：
#   - 调用方拿到 None 之后，**分不清是哪一种失败**（没文件？没这条记录？格式错？）
#   - get_task 假设了"我的失败应该被打印到 stdout"——它在 Web/定时任务里就尴尬了
#
#   题目第 5 条说的"各自的处理路径"，更地道的分层是：
#     - get_task：只负责读+查，**异常原样向上抛**
#         （FileNotFoundError、csv.Error、TaskNotFoundError 都不 except）
#     - 调用层（main / CLI 入口）：try / except 三段，**调用方决定怎么报错**
#         try:    task = mgr.get_task(...)
#         except FileNotFoundError:  ...
#         except csv.Error:          ...
#         except TaskNotFoundError:  ...
#         else:    # 成功路径，调用方拿到 task
#
#   不用现在重写，但下次写"业务函数 / 表现层"分离时，记住这条经验。
#
# [AI 批注] 💡 顺手一个细节：raise TaskNotFoundError 可以带上 id —— raise TaskNotFoundError(id)。
#   这样 str(e) 会包含 id，traceback 里能看到"哪个 id 没找到"，调试更友好。


##### Answer:
# 1) try 的 else 分支解决了什么问题？
# except 没有兜住
# [AI 批注] 📝 ⚠️ 方向沾边但说得太含糊，而且术语错了（"expect" → "except"）。
# 更准确的表述应该围绕"作用域"和"意图"：
#   - 没有 else 的写法里，把"成功后才该做的事"塞进 try，
#     这些代码抛出的异常会被同一个 except 错误地兜住——掩盖真实的 bug 来源；
#   - else 的语义是"try 没出异常时执行"，把它和"被保护的可能出错的代码"分开，
#     **缩小 except 的捕获范围**，让异常处理只针对你预期的失败点。
# 关键词：异常作用域（exception scope）、意图清晰（intent clarity）。

# 2) 为什么自定义异常要继承 Exception 而不是 BaseException？
# 因为 BaseException 有一些系统异常，例如 sys.exit
# [AI 批注] 📝 ✅ 方向对了，但可以更精确：
#   - BaseException 是所有异常的根，下面挂着 KeyboardInterrupt（Ctrl+C）、
#     SystemExit（sys.exit() 触发）、GeneratorExit 这些"控制流"异常；
#   - 通用的 `except Exception:` 不会捕获它们，这是**故意**设计的——
#     这样用户按 Ctrl+C 才能可靠地中断程序、sys.exit 才能可靠地退出；
#   - 如果你的自定义异常继承 BaseException，调用方写 `except Exception:`
#     就漏掉了它，违反"我的业务异常应该被业务层兜住"的预期。
# 小练习：跑一段 `try: ... except Exception: ...` 然后在 try 里 Ctrl+C，看看会发生什么。

# 3) EAFP vs LBYL 的权衡（性能 / 可读性 / 并发安全性）：
# Answer:
# 性能：EAFP 性能比 LBYL 好，因为 LBYL 会去多访问一次判断是否存在
# 可读性：EAFP 更线性，LBYL 很容易写出一堆 if else
# 并发安全性: EAFP 在并发的场景下更可靠，异常场景可以被 catch 住，而 LBYL 并发场景下容易出现判断时有问题，但是同时并发下又对有问题的资源进行了访问

# [AI 批注] 📝 已填写，三个维度的方向都对了，逐条点评：
#   ✅ 可读性："EAFP 更线性 / LBYL 容易写出一堆 if else" —— 准确，
#      happy path 一眼能看完是 EAFP 的核心可读性优势。
#   ✅ 并发安全：抓住了 LBYL 的 TOCTOU（time-of-check / time-of-use）窗口 ——
#      "判断时 OK，访问时已经被改了"，这是 LBYL 在多线程 / 多进程 / 文件系统
#      场景下的根本问题。术语补一下：这叫 **race condition**，更精确的子类型是
#      check-then-act / TOCTOU。
#   ⚠️ 性能：方向反了一半。"LBYL 会多访问一次判断" 这句话在"成功路径"上确实成立
#      （多一次 `in` / hash 查找），但 EAFP 的代价不在"访问"上，而在"异常抛出"上 ——
#      CPython 抛一个异常要构造 traceback、回溯栈帧，单次开销远大于一次 hash 查找。
#      所以更准确的权衡是：
#        - 如果"miss 是罕见的"（happy path 占 99%）→ EAFP 更快（成功路径零开销）；
#        - 如果"miss 是常态"（happy path 占 50% 以下）→ LBYL 更快（避免频繁抛异常）；
#        - 极端例子：用 try/except 当 if 用 → 极慢。
# 一句话总结："EAFP 性能比 LBYL 好" 这句话本身要加前提条件，不是无条件成立。

# 4) 上下文管理器协议（__enter__/__exit__）和 try/finally 的关系：
# Answer: try/finally 是基本语法，而 __enter__/__exit__ 是编程协议


# [AI 批注] 📝 ✅ 方向对了，但太抽象了 —— "语法 vs 协议" 这个对比没说出**为什么**协议层更好用。
# 建议补完整：
#   - **关系**：with 语法**底层就是** try/finally 的语义化封装。等价展开：
#       with cm as x:           ≈   x = cm.__enter__()
#           BODY                     try:    BODY
#                                    except:
#                                        if not cm.__exit__(type, val, tb): raise
#                                    else:   cm.__exit__(None, None, None)
#   - **为什么要造一层协议**：
#       1) 复用 —— 清理逻辑写一次（__exit__），所有调用方 `with` 一下就拿到；
#          而 try/finally 是"每次都要重抄一遍 finally 块"。
#       2) 嵌套 —— `with A(), B(), C():` 自动按 LIFO 释放，try/finally 嵌套三层
#          会变成意大利面。
#       3) 异常感知 —— __exit__(exc_type, exc, tb) 能拿到异常信息**并决定吞不吞**
#          （返回 True/False，参考 Task 3.4 的实验），try/finally 做不到"看一眼
#          异常再决定怎么办"，只能"无论如何都执行 finally"。
#   - **一句话**：try/finally 解决"清理一定会跑"，上下文管理器解决"清理逻辑可以
#     被打包、复用、嵌套、感知异常"。

# ============================================================
# [AI 批注] 📊 整体评价（第三次 review）
# ============================================================
#
# ⚠️ 再次致歉 —— 上一稿评价里写 "Task 3.4 实验 B/C 未跑、答题区 #3/#4 仍空白"
# 这三点全标错了：你早就把 raise + return True 都激活了（相当于实验 C），
# 答题区 #3 / #4 也都填了内容。这次按现状重新打分。
#
# 完成度：★★★★★ (5/5)  ↑ 从 4/5
# - Task 3.1 ~ 3.5 全部完成且实测通过
# - 答题区 4 条全部填写，方向都对（精度有改进空间，见各条批注）
#
# 代码质量：★★★★☆ (4/5)
# - Task 3.5 的异常处理细节打磨彻底，run 起来三种失败路径都不崩
# - Task 3.4 的 with + raise + return True 三件套完整观察到了
# - 剩下的是"业务函数 vs 表现层"的分层设计观（见 Task 3.5 💡 批注）
#
# 理解深度：★★★★☆ (4/5)
# - else 分支 / EAFP-LBYL / __exit__ 异常感知 / 自定义异常继承体系，都用实验落地了
# - 答题区主要差在**精度**：
#     #1 太短（建议补"缩小 except 捕获范围"）
#     #3 性能维度反了一半（EAFP 的成本是异常抛出，不是访问）
#     #4 抽象但缺"为什么造这一层"（复用 / 嵌套 / 异常感知三个好处）
# - 这种"方向对、精度待打磨"的状态，恰好是从"会写"过渡到"会讲"的阶段
#
# 下一步建议（轻量打磨，不用大改）：
# 1. 🟢 把答题区 #1 / #3 / #4 按对应批注的方向再精化一遍
#       （重点是术语：exception scope、TOCTOU race condition、context manager protocol）
# 2. 🟢 Task 3.5 的"业务层抛、表现层兜"分层思路，下次写新模块时实践一次
# 3. 🟢 进入 Task 4 之前，可以把 Task 3.4 的 __exit__ 等价 try/finally 展开
#       自己手抄一遍，作为"我已经吃透 with 协议"的收尾仪式
#
# 这份 Task 3 已经达到"可以合并、可以进入下一阶段"的状态了。👏
