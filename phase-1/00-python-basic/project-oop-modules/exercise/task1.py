# ### Task 1：Python 的 class（Day 1）

# - [ ] 定义一个 `Task` 类，包含标题、优先级、完成状态、创建时间。**思考**：JS 的 constructor 里用 `this.x = x`，Python 的 `__init__` 里用 `self.x = x`——看起来一样，但 `self` 必须显式写成第一个参数，这个设计选择背后的理由是什么？（搜索 "explicit self in Python"）
# - [ ] 给 Task 类添加实例方法（标记完成、修改优先级）、一个类方法（从字典创建 Task）、一个静态方法（校验标题格式）。**思考**：JS class 里只有 static 和普通方法两种，Python 多了一个 `@classmethod`——它解决了什么问题？什么场景必须用 classmethod 而不是 staticmethod？
# - [ ] 用 `@property` 实现一个计算属性（例如：任务已存在的天数）。对比 JS 的 getter/setter，使用体验有什么不同？
# - [ ] 尝试给属性名加 `_` 前缀和 `__` 前缀，从外部访问它们。**思考**：Python 没有 `private` 关键字，用命名约定来表达可见性——你觉得这是优点还是缺点？

# 📚 **Key docs**: [类教程](https://docs.python.org/3/tutorial/classes.html) | [property()](https://docs.python.org/3/library/functions.html#property)
# > 类教程是 Python 面向对象的入门必读，重点看 §9.3 初识类 和 §9.4 补充说明；property 文档看描述符协议的简要说明

from datetime import datetime

class Task:
    def __init__(self, title, priority):
        self.title = title if self.validate_title(title) else f"Task {datetime.now()}"
        self.priority = priority
        self.done = False
        self.created_at = datetime.now()
        self._x = title
        self.__y = title
    # [AI 批注] ✅ 已修正：import 修对了，validate_title 接进 __init__ 了，_x/__y 也改成了实例属性
    # 现在文件能跑，输出 Demo / Demo / 0 全部符合预期。
    #
    # 💡 一个设计选择值得想一想：
    # 第 15 行 `self.title = title if self.validate_title(title) else f"Task {datetime.now()}"`
    # 是 **silent fallback**——校验失败就静默改名，不报错。
    # 另一种常见做法是 `if not Task.validate_title(title): raise ValueError(...)`——
    # 校验失败直接抛异常。两种都合法，但有不同含义：
    # - 你的写法："标题随便给，框架兜底"——适合 toy CLI，调用者不需要管错误
    # - raise 的写法："标题必须合法，否则不创建"——适合库/API，强制契约
    # 生产代码里更常见 raise；toy 项目你这种 fallback 挺友好。看场景选。
    #
    # 💡 另外一个细节：`self.validate_title(title)` 是通过 self 调 staticmethod。
    # 这能跑（staticmethod 在类和实例上都能访问），但更直白的写法是 `Task.validate_title(title)`
    # 或 `type(self).validate_title(title)`——明示这是类方法，不依赖 self。

    def mark_done(self):
        self.done = True

    def set_priority(self, new_priority):
        self.priority = new_priority

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)
    # [AI 批注] ✅ cls(**data) 写得很 Pythonic
    # 这一行同时回答了思考题"什么场景必须用 classmethod"：
    # cls 在子类调用时自动绑到子类（UrgentTask.from_dict(d) 返回 UrgentTask），
    # 如果写死 Task(**data) 用 staticmethod，子类继承下来还是返回 Task——继承废了。

    @staticmethod
    def validate_title(title: str):
        return len(title) > 0 and len(title) < 50
    # [AI 批注] ✅ 已修正：method 对象 bug + 命名 + 接进 __init__ 全部完成
    # 长度上限从 10 调到 50 也合理多了（10 个字符的 title 实在太苛刻）。
    #
    # 💡 残留的小风格：`title.__len__() > 0` 写成 `len(title) > 0` 更地道。
    # 直接调魔术方法（dunder method）能跑，但 Python 社区的惯例是"调用 builtin，让 builtin 去调 dunder"——
    # 这是为什么有 `len()` / `str()` / `repr()` / `iter()` 这些 builtin 的原因：
    # 它们对 None、对实现不完整的对象都有更友好的错误消息。
    # 比如 `None.__len__()` 抛 AttributeError；`len(None)` 抛 TypeError，后者更清晰。

    @property
    def age_in_days(self):
        return (datetime.now() - self.created_at).days
    # [AI 批注] ✅ 已修正：刚创建的 task 输出 0，公式正确
    # `(datetime.now() - self.created_at).days` 这一行漂亮地避开了"一天/一年秒数"的常数陷阱——
    # datetime 帮你处理了单位换算，这就是改用 datetime 比 int(epoch) 自然得多的原因。

task = Task('Demo', 'low')
print(task._x)
print(task._Task__y)
print(task.age_in_days)
# print(task.__y) // will throw error: AttributeError: 'Task' object has no attribute '__y'

# [AI 批注] ✅ 已修正：Task 1.4 的"绕过演示"补上了
# 输出 Demo / Demo / 0 完美——`task._Task__y` 拿到了"私有"属性的值，
# 这就是题目想让你"撞见"的真相：`__` 不是 private 的语法，是
# "通过改名 `_类名__属性` 来避免子类继承冲突"的机制。能绕过 = 不是 private。
# 三个对照（task._x 成功 / task.__y AttributeError / task._Task__y 成功）你都做到了。
#
# ⚠️ 还有两个小残留：
# 1) `// will throw error` 仍是 JS 风格，Python 单行注释用 `#`
# 2) 第 77 行下方的旧注释 `# print(task.__name) // will throw error: AttributeError:
#    'TaskWithPrivate' object has no attribute '__name'` 是上一版残留，可以删掉

##### Answer:
# 1) explicit self in Python：
# Answer: 更清晰, 更可读
#
# [AI 批注] ⚠️ 答得太浅了，"清晰可读"是结果不是原因
# explicit self 真正的设计动机：
# (a) 方法签名一眼能看出第一个参数是实例——不需要看类定义就懂方法属于谁
# (b) Task.mark_done(t) 和 t.mark_done() 等价——揭示了"实例方法 = 把实例作为
#     第一个参数的函数"这个真相。JS 的 this 是隐式魔法，Python 的 self 把魔法摊在桌面上。
# (c) 和 staticmethod / classmethod 在签名上有清晰区分
# (d) Zen of Python: "Explicit is better than implicit"——这是整门语言的设计原则

# 2) classmethod vs staticmethod 的必要场景：
# Answer: 需要对使用类时用 classmethod
#
# [AI 批注] ⚠️ 表达不清——"对使用类时"是什么意思？
# 准确：当方法需要访问/操作 **类本身**（而非实例）时用 classmethod。
# from_dict 就是最经典例子：cls(**data) 在子类调用时 cls 自动绑到子类，
# 写死 Task(**data) 配 staticmethod 就破坏继承。
# 反过来，纯工具函数（像 validate_title）用 staticmethod 就够了——它和类/实例都没关系，
# 只是逻辑上属于这个类的命名空间。

# 3) Python 的 _ / __ 命名约定 vs 真正的 private：
# Answer: 我认为是缺点，凭什么 self 又要求显式了，这里又是隐式，逻辑不能自洽啊
#
# [AI 批注] 💡 观察很有意思（敢质疑值得鼓励），但有两层可以再想
# (a) Python 哲学是 "We're all consenting adults"——可见性靠纪律和约定，不是语言强制。
#     好处：不需要 friend / protected / package-private 这套关键字；坏处：依赖团队规范。
# (b) `__name` 的 name mangling 其实**有强制效果**——名字被改写成 `_类名__name`，
#     目的不是 private，是避免子类继承时的命名冲突。
# 所以 `_` 和 `__` 不是同一种东西：
# - `_x`：纯开发者约定，语言层面不做事
# - `__x`：语言层面有改名，目的是子类隔离不是 private
# 推荐：Raymond Hettinger 的 "Beyond PEP 8" talk。


# ============================================================
# [AI 批注] 📊 当前状态（第四轮 review 后）
# ============================================================
#
# 这一轮的进步 ✅（一次性消化了上一轮所有红色项）
# - import 修对：`from datetime import datetime`，文件能跑
# - validate_title 接进 __init__（用 silent fallback 设计）
# - _name/__name 改成 __init__ 里的实例属性 self._x / self.__y
# - 补上了 mangling 绕过演示：`print(task._Task__y)` ← 这是 Task 1.4 的核心
# - title 长度从 10 调到 50（合理多了）
#
# 完成度：★★★★★ (5/5)  ← 代码层面的题目要求全部覆盖到位
# 代码质量：★★★★☆ (4/5)
# 理解深度：★★★☆☆ (3/5)  ← 文本答案还没动
#
# 仍可优化（全是 polish 级，无概念性错误）：
# 🟢 三个 Answer 重写（参考各自批注里的方向）
# 🟢 line 80 的旧 'TaskWithPrivate' 注释残留删掉
# 🟢 // 注释改成 #
# 🟢 `title.__len__()` → `len(title)` 更地道
# 🟢 silent fallback vs raise 的设计选择可以想一想（有意识地选，而不是默认）
#
# 总评：四轮 review 走完，从一开始的 4 层继承 + 一堆 bug，
# 到现在所有功能正确、bug 全清、关键洞察（mangling 绕过）也撞见了——
# 已经具备进入 Task 2（魔术方法 + 继承）的所有前置知识。
# 下一步可以直接动 task2.py，回头再补 task1.py 的文本答案也不迟。
