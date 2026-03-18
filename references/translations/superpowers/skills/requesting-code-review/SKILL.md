---
name: requesting-code-review
description: 当你完成任务、实现重要功能，或准备合并前需要确认结果满足要求时使用
---

# 请求代码评审

派发 `superpowers:code-reviewer` subagent，在问题扩散前先把它们拦下来。reviewer 只拿到你精心构造的评审上下文，**绝不继承你的会话历史**。这样 reviewer 会聚焦在产物本身，而不是你的思路过程，同时也能保留你的上下文用于继续推进工作。

**核心原则：**尽早 review，经常 review。

## 何时请求评审

**必须请求：**
- 在 subagent-driven development 中，每完成一个任务后
- 完成重要功能后
- 合并到 main 之前

**可选但很有价值：**
- 卡住时（需要新的视角）
- 重构前（先拿一个基线判断）
- 修完复杂 bug 后

## 如何请求

**1. 获取 git SHA：**
```bash
BASE_SHA=$(git rev-parse HEAD~1)  # or origin/main
HEAD_SHA=$(git rev-parse HEAD)
```

**2. 派发 code-reviewer subagent：**

使用 Task 工具，类型为 `superpowers:code-reviewer`，并填写 `code-reviewer.md` 模板。

**占位字段：**
- `{WHAT_WAS_IMPLEMENTED}` - 你刚刚实现了什么
- `{PLAN_OR_REQUIREMENTS}` - 它本来应该做到什么
- `{BASE_SHA}` - 起始 commit
- `{HEAD_SHA}` - 结束 commit
- `{DESCRIPTION}` - 简短摘要

**3. 处理反馈：**
- 立即修复 Critical 问题
- 继续前先修复 Important 问题
- Minor 问题可以记录到后面再处理
- 如果 reviewer 错了，要基于技术理由反驳

## 示例

```
[刚完成 Task 2：添加 verification 函数]

你：我先请求一次代码评审，再继续往下做。

BASE_SHA=$(git log --oneline | grep "Task 1" | head -1 | awk '{print $1}')
HEAD_SHA=$(git rev-parse HEAD)

[派发 superpowers:code-reviewer subagent]
  WHAT_WAS_IMPLEMENTED: conversation index 的校验与修复函数
  PLAN_OR_REQUIREMENTS: docs/superpowers/plans/deployment-plan.md 中的 Task 2
  BASE_SHA: a7981ec
  HEAD_SHA: 3df7661
  DESCRIPTION: 新增 verifyIndex() 和 repairIndex()，覆盖 4 类问题

[subagent 返回]
  Strengths: 架构清晰，测试真实
  Issues:
    Important: 缺少进度指示
    Minor: 报告间隔里存在 magic number (100)
  Assessment: Ready to proceed

你：[修复进度指示]
[继续 Task 3]
```

## 与工作流的集成

**Subagent-Driven Development：**
- 每个任务后都 review
- 在问题叠加前先发现
- 修完再进入下一个任务

**Executing Plans：**
- 每一批（3 个任务）后 review 一次
- 拿到反馈，处理后继续

**Ad-Hoc Development：**
- 合并前 review
- 卡住时 review

## 红旗

**绝不要：**
- 因为“很简单”就跳过 review
- 忽略 Critical 问题
- 带着未修复的 Important 问题继续推进
- 对有效的技术反馈强行争辩

**如果 reviewer 错了：**
- 用技术理由反驳
- 展示能证明行为正确的代码或测试
- 必要时请求澄清

模板见：`requesting-code-review/code-reviewer.md`
