# ### Task 4：模块化与打包（Day 2-3）

# - [ ] 把你的单文件代码重构为多文件包结构。你需要搞清楚：`__init__.py` 是什么？和 Node.js 的 `index.js` 有什么相似和不同？
# - [ ] 实验 import 的各种形式：绝对导入、相对导入、从包导入、从模块导入特定名称。**思考**：当你写 `from models import Task` 时，Python 是怎么找到 `models` 这个模块的？搜索 Python 的模块搜索路径
# - [ ] 在 `__init__.py` 中使用 `__all__` 控制 `from package import *` 的行为
# - [ ] 用 `pip install` 安装一个第三方包（例如 `click`，用来美化 CLI）。然后用 `pip freeze > requirements.txt` 记录依赖。**思考**：和 Node.js 的 `package.json` + `package-lock.json` 相比，Python 的依赖管理方案有什么不足？你听说过 `poetry` 或 `uv` 吗？
# - [ ] 理解 `if __name__ == "__main__":` 这个惯用法——它解决了什么问题？
# - [ ] 把任务管理器做成可以用 `python -m your_package` 运行的形式，支持 add、list、done、stats 等子命令

# 📚 **Key docs**: [模块教程](https://docs.python.org/3/tutorial/modules.html) | [Python 打包用户指南](https://packaging.python.org/en/latest/tutorials/packaging-projects/) | [venv 模块](https://docs.python.org/3/library/venv.html)
# > 模块教程重点读 §6.4 包（Packages）和 §6.4.1 从包中导入；打包指南帮你理解 Python 项目的标准结构

# 注：本任务的产物是一个独立的 package 目录结构（不是单文件），
# 建议在本目录旁边创建 `task_manager/` 这样的包文件夹，本文件只用来记录笔记和答案。


#### Task4.1
# 重构成包结构。建议形态：
# task_manager/
#   __init__.py
#   models.py        # Task / UrgentTask / TaskList
#   storage.py       # 读写 JSON
#   exceptions.py    # TaskNotFoundError 等
#   __main__.py      # 让 python -m task_manager 可运行
# 思考：__init__.py vs Node 的 index.js —— 异同点？


#### Task4.2
# 实验四种 import 形态，记录每一种的报错/成功条件：
# - import task_manager
# - from task_manager import models
# - from task_manager.models import Task
# - from .models import Task   （相对导入，只能在包内部用）
# 思考：sys.path 是什么？为什么直接跑 task_manager/models.py 里的相对导入会报 ImportError？


#### Task4.3
# 在 __init__.py 里写 __all__ = [...]，然后 from task_manager import *，验证只导出了你列出的名字


#### Task4.4
# 装一个第三方包（推荐 click 或 rich）
# 命令记录：
#   python -m venv .venv
#   source .venv/bin/activate
#   pip install click
#   pip freeze > requirements.txt
# 思考：requirements.txt 没有锁定传递依赖的精确版本，poetry/uv 用 lock file 解决了这个问题


#### Task4.5
# 在 models.py / __main__.py 里加 if __name__ == "__main__": 块，
# 思考：单独运行 python models.py vs from task_manager import models 时，__name__ 各是什么？


#### Task4.6
# 让 python -m task_manager add "买菜" 能跑通
# 子命令：add / list / done <id> / stats
# 提示：__main__.py 是 entry point；click.group() / argparse 都能做子命令

##### Answer:
# 1) __init__.py vs Node index.js 的异同：
# 2) Python 的模块搜索路径（sys.path 的组成）：
# 3) requirements.txt vs package-lock.json 的差距：
# 4) if __name__ == "__main__" 解决的问题：
# 5) 延伸思考（来自 README）：abc.ABC + @abstractmethod 如何强制子类实现方法？
