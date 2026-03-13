# 00 · Python 基础（面向 JS/TS 开发者）

> 你已经会编程了，这里不讲"什么是变量"。
> 目标是让你用最短路径掌握 Python 的核心语法和惯用法，为 01 章的高级特性打好地基。

## 学习目标

完成本章后，你应该能回答：

1. Python 的 list/dict/set/tuple 和 JS 的 Array/Object/Set 有什么本质区别？什么时候该用哪个？
2. Python 的闭包和高阶函数怎么用？为什么说理解闭包是理解装饰器的前提？
3. Python 的 class 和 JS class 有哪些关键差异？`self`、魔术方法、多继承分别解决了什么问题？
4. Python 的模块/包系统和 Node.js 的 import/require 有什么不同？虚拟环境为什么是必须的？

## 前置知识映射

你已经熟悉 JS/TS，下面这些对照关系可以加速你的理解。但要注意：**表面相似的概念往往有微妙差异**——这些差异正是本章项目要你亲手发现的。

关键差异领域（不给答案，在项目中体会）：

- 变量声明 vs 直接赋值
- Array vs list + tuple（为什么 Python 需要两种？）
- Object/Map vs dict
- 箭头函数 vs lambda 的能力差距
- class 的 this 隐式绑定 vs self 显式传递
- npm + node_modules vs pip + venv
- TypeScript 编译时检查 vs Python 类型标注的运行时行为

## 包含项目

| 序号 | 项目 | 核心知识点 | 预计耗时 |
|------|------|-----------|---------|
| P0-1 | [数据处理 CLI 工具](./project-data-structures/) | list/dict/set/tuple, 推导式, 解包, 切片, 文件 I/O | 2-3 天 |
| P0-2 | [函数式工具集](./project-functional-closures/) | 函数作为一等公民, 闭包, 高阶函数, lambda, 生成器 | 2-3 天 |
| P0-3 | [任务管理器](./project-oop-modules/) | class, 继承, 魔术方法, 模块/包, 异常处理, venv/pip | 2-3 天 |

## 环境准备（Day 0）

在开始项目之前，你需要搞定开发环境。这些你应该能自己搞定：

1. 安装 Python 3.11+，在终端确认版本号
2. 创建一个虚拟环境并激活它（搜索 `python -m venv`）
3. 配置编辑器的 Python 支持（推荐 VS Code + Pylance 扩展）
4. 写一个 hello.py，确认能正常运行

## 推荐阅读

1. [Python for JavaScript Developers](https://www.valentinog.com/blog/python-for-js/) — 快速对照指南
2. Python 官方教程 — [数据结构](https://docs.python.org/3/tutorial/datastructures.html)
3. Python 官方教程 — [类](https://docs.python.org/3/tutorial/classes.html)
4. Real Python — [Python Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/)
