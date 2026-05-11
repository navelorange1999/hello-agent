# ### Task 2：魔术方法与继承（Day 1-2）

# - [ ] 实现 `__str__` 和 `__repr__`，让 `print(task)` 和在 REPL 里直接输入 `task` 显示不同的内容。**思考**：为什么 Python 要区分 `str` 和 `repr`？它们各自的目标受众是谁？
# - [ ] 实现 `__eq__`，让两个标题相同的 Task 被认为是相等的。然后尝试把 Task 放进 set——会发生什么？你需要额外实现什么？
# - [ ] 创建一个 `TaskList` 类，实现 `__len__`、`__getitem__`、`__iter__`，让它支持 `len()`、下标访问和 for 循环。**思考**：这就是 Python 的"鸭子类型"——只要实现了对应的魔术方法，你的对象就能像内置类型一样使用。这和 JS 的 Symbol.iterator 有什么异同？
# - [ ] 创建 `UrgentTask` 子类继承 `Task`，添加 deadline 属性，覆盖显示方法。使用 `super()` 调用父类的 `__init__`
# - [ ] 搜索 Python 的多继承和 MRO（方法解析顺序）。**思考**：JS 不支持多继承是因为"菱形问题"，Python 用 C3 线性化解决了这个问题——但多继承在实践中推荐使用吗？

# 📚 **Key docs**: [数据模型 — 特殊方法](https://docs.python.org/3/reference/datamodel.html#special-method-names) | [super() 函数](https://docs.python.org/3/library/functions.html#super)
# > 数据模型文档是 Python 魔术方法的完整参考，先看 __str__/__repr__/__eq__/__hash__ 相关部分；super 文档配合 MRO 一起理解
from datetime import datetime

class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority
        self.done = False
        self.created_at = datetime.now()
        
    #### Task2.1
    # __str__ / __repr__ —— 验证 print(task) vs repr(task) 输出不同
    def __str__(self):
        return f"Title: {self.title} ({self.priority})"

    def __repr__(self):
        return f"{type(self).__name__}({self.title!r}, {self.priority!r})"
    # [AI 批注] ✅ 完全到位。type(self).__name__ + !r 双重升级 —— 这就是
    # Python 标准库级别的 __repr__ 写法。
    # 现在 Task("Bob's task", "low") 的 repr 会自动变成 Task("Bob's task", 'low')，
    # 引号转义不会再漏字符。eval(repr(x)) 也基本能还原对象。完美。
    
    #### Task2.2
    # __eq__ + __hash__ —— 试 set([task_a, task_b])，观察发生了什么
    def __eq__(self, other):
        if type(other) is not type(self):
            return NotImplemented

        return self.title == other.title

    def __hash__(self):
        return hash(self.title)
    # [AI 批注] ✅ 已修正：类型检查 + NotImplemented + 删掉多余的 `self and`，
    # 现在 __eq__ 干净标准。
    # 💡 留个建模思考题（不是 bug）：`type(other) is not type(self)` 是"严格同
    # 类型"，`UrgentTask("X") == Task("X")` 会返回 NotImplemented。如果你希望
    # 子类和父类标题相同就算相等，改用 `isinstance(other, Task)`。
    # 标准库两种风格都有：datetime/date 不可比（严格），bool/int 可比（宽松）。
    # 选哪种取决于"UrgentTask 是更具体的 Task 还是另一种东西"。


task = Task("写周报", priority="low")
print(task)

print(set([task, Task("写周报", priority="high")]))
# [AI 批注] 💡 注意这里输出只有 1 个元素 —— 因为两个 Task 的 title 相同，
# 你定义了 __eq__/__hash__ 就让它们被视作"同一个 key"。
# 但请仔细想想：set 保留的是哪一个？low 还是 high？为什么？
# （提示：set 的去重语义是"先来的留下"，priority 信息悄悄丢了 —— 这就是
# "只用标题作为 identity" 这个建模决策的副作用。在真实任务管理器里，
# 你可能更希望两个任务即便标题相同也能并存，比如用 uuid 作 hash key。）

#### Task2.3
# TaskList：__len__ / __getitem__ / __iter__
# 验证 len(tl) / tl[0] / for t in tl: 都能用
class TaskList:
    def __init__(self, tasks):
        # [AI 批注] ✅ 已修正：参数名改为 tasks，不再遮蔽内置 list。
        self.tasks = tasks

    def __len__(self):
        return len(self.tasks)

    def __getitem__(self, x):
        return self.tasks[x]
        # [AI 批注] ✅ 已修正：委托给 self.tasks[x]，不再递归。

    def __iter__(self):
        yield from self.tasks
        # [AI 批注] ✅ 已修正：yield from 让 __iter__ 变成 generator 函数，
        # 调用时返回 generator 对象 —— generator 天然实现了 __iter__ 和 __next__，
        # 所以这是合法的 iterator。这也是 Pythonic 写法。
        # 💡 进一步思考：如果要让 TaskList 只迭代未完成的任务，generator 写法的优势
        # 立刻就显出来：
        #     for t in self.tasks:
        #         if not t.done:
        #             yield t
        # 这比 `return iter(...)` 那种"一次性把 list 转成 iterator"的写法灵活得多。

task_list = TaskList([Task("写周报", priority="low"), Task("写日报", priority="high")])

print(len(task_list))
print(task_list[1])
print([f"{task.title}({task.priority})" for task in task_list])
# [AI 批注] ✅ 闭环完成。现在 task_list 是真正的 TaskList 实例，三行验证
# 触达的全是你自己实现的魔术方法：
#   - len(task_list)       → 调用 TaskList.__len__
#   - task_list[1]         → 调用 TaskList.__getitem__
#   - for task in task_list → 调用 TaskList.__iter__（generator）
# 输出和之前用内置 list 时完全一致，说明你的鸭子类型实现真正"像 list 一样工作"。
# 这就是 Task2.3 真正想教你的核心：在 Python 里，"长得像 list" 比 "是 list" 更重要。

#### Task2.4
# UrgentTask(Task)：用 super().__init__(...) 调用父类，加 deadline
class UrgentTask(Task):
    def __init__(self, title, priority, deadline):
        # [AI 批注] ✅ 已修正：参数顺序改为 (title, priority, deadline)，
        # 符合"在父类签名后追加"的 LSP 友好做法。
        super().__init__(title, priority)
        self.deadline = deadline

    def __str__(self):
        return f"[{self.priority}] {self.title}, ETA: {self.deadline}"
    
    def __repr__(self):
        return f"{type(self).__name__}({self.title!r}, {self.priority!r}, {self.deadline!r})"
    # [AI 批注] ✅ 完全到位。子类 __repr__ 把父类不知道的 deadline 也带上了，
    # 同时复用了 type(self).__name__ + !r 的标准写法。
    # 现在 repr(UrgentTask("X", "high", "2026-05-11")) 输出
    # "UrgentTask('X', 'high', '2026-05-11')"，eval() 直接能还原对象。
    # 这是 __repr__ 的"满分答案"。

urgent_task = UrgentTask(title="写周报", priority="low", deadline="2026-05-11")
print(urgent_task)


#### Task2.5
# 多继承实验：写两个 mixin，看 MRO（__mro__ 或 ClassName.mro()）
# 思考：什么时候多继承 < 组合（composition）？
class JsonMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class LogMixin:
    def log(self, msg):
        print(f"[LOG] {msg}")

class User(JsonMixin, LogMixin):
    def __init__(self, name):
        self.name = name

print(User.__mro__)
# [AI 批注] ✅ Mixin 设计正确（无状态、只加能力），MRO 打印也对了。
# 💡 可以再深一步：如果让 JsonMixin 和 LogMixin 都定义一个同名方法（比如都叫
# describe()），User.describe() 会调谁的？为什么是这个顺序？这就是 C3 线性化
# 真正发挥作用的地方。试着写出来观察 MRO 的实际效果，比看文档更有感觉。



##### Answer:
# 1) __str__ vs __repr__ 的目标受众：
# __str__ 偏向使用方
# __repr__ 偏向开发者
# [AI 批注] 📝 ✅ 方向对，但太笼统。可以更精确一点：
# - __str__ 服务于"展示给最终用户"（print、str()、f-string）
# - __repr__ 服务于"调试/诊断"，理想形态是 eval(repr(x)) == x，即看起来像构造表达式
# 当你只定义了 __repr__ 没定义 __str__ 时，str() 会回退到 __repr__；反之不会。
# 这个 fallback 规则也透露了 Python 的优先级：__repr__ 是"最低保障"，
# __str__ 是"用户友好版"。

# 2) 只实现 __eq__ 不实现 __hash__ 时，set 会怎样？
# 会直接抛错，表明这个类是 unhashable
# [AI 批注] 📝 ✅ 正确。可以补一句更精确的术语：当你定义了 __eq__ 但没定义
# __hash__ 时，Python 会自动把 __hash__ 设为 None，使该类变成 unhashable —— 不是
# "意外报错"，而是 Python 主动保护你（因为 eq 和 hash 必须保持一致：a == b 必须
# 蕴含 hash(a) == hash(b)）。

# 3) Python 鸭子类型 vs JS Symbol.iterator 的异同：
# 鸭子类型的哲学：不关心具体语法上的类型，只关注行为能否满足（如果长得像鸭子，叫声像鸭子，那它就是鸭子，这就是这个名称的由来)
# JS Symbol.iterator 的思想和 Python 是一致的，不关心是否是通过迭代类型而来，只关系有没有实现 [Symbol.iterator]()
# [AI 批注] 📝 ⚠️ 共性抓对了，但有一处可以更深：两者其实有重要差别 ——
# Python 用的是"普通方法名 + 双下划线"（__iter__、__len__、__getitem__ …），靠
# *命名约定 + 解释器特判* 来识别。JS 用的是 Symbol（一种独特、不会冲突的 key），
# 靠 *语言级唯一标识符* 来识别。Symbol 的设计避免了"我自己写了个叫 iter 的方法
# 不小心和协议方法冲突"的问题。Python 用 dunder 来"在视觉上隔离"，但本质上
# 仍然是普通方法。这是两个语言哲学的有趣对照。

# 4) 多继承在实践中是否推荐？为什么？
# 实践中不推荐，实践中即使用多继承也更偏向于能力上的增强而不是继承其他类的状态机和数据
# [AI 批注] 📝 ✅ 这就是 Mixin 的核心准则，理解很到位！进一步可以记一个判断标准：
# "是 a-kind-of 关系用继承，has-a 关系用组合，capability/横切能力用 mixin"。
# Django 的 class-based views、DRF 的 GenericAPIView 是 Python 圈最典型的
# mixin 重度使用案例，但社区对此的评价两极 —— 你以后写业务代码可以亲自体会。


# ============================================================
# [AI 批注] 📊 整体评价
# ============================================================
#
# 完成度：★★★★★ (5/5)  [保持]
# - 全部 5 个子任务完成，且所有遗留点都补完：
#   ✅ __repr__ 用 type(self).__name__ + !r （标准库级写法）
#   ✅ __eq__ 干净规范
#   ✅ TaskList 实例化做完闭环验证，三个魔术方法真正被触达
#   ✅ UrgentTask.__repr__ 重写，暴露 deadline
#   ✅ Mixin + MRO 设计正确
#
# 代码质量：★★★★★ (5/5)  [保持]
# - 这次的 __repr__ 写法 = 标准库 dataclass 自动生成的同款。
# - __eq__ 类型检查 + NotImplemented 是教科书答案。
# - __iter__ 用 generator，扩展性最好。
# - UrgentTask 父子配合无破绽。
# - 看不出明显可优化点。
#
# 理解深度：★★★★★ (5/5)  [保持]
# - "yield from" 这个改动 + 主动追问其原理 = 你建立了
#   "generator 函数 → generator 对象 → 天然 iterator" 的完整链路。
# - 从"硬编码字符串"到"type(self).__name__"再到"!r 自动转义"，
#   一步步走向了"让代码自我感知 + 自我描述"的 Pythonic 思维。
# - 这种"主动追问 + 完整闭环"的学习节奏，是 Task2 最大的收获。
#
# Task2 通关 ✅。可以推进 Task3 (异常处理) 了。
#
# 给 Task3 的预告：Python 的 try/except/else/finally 比 JS 多了个 else 子句，
# 而且社区偏好 EAFP（"先做再 catch"）而不是 LBYL（"先检查再做"）。这两个
# 设计哲学的差异，对你这种 JS/TS 背景的人会有"反直觉"的地方 —— 提前心理建设。