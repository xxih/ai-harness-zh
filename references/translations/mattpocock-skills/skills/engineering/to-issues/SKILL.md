---
name: to-issues
description: 用示踪弹垂直切片把 plan、spec 或 PRD 拆成项目 issue tracker 上可独立认领的 issue。当用户想把 plan 转成 issue、建实现工单,或把工作拆成多个 issue 时使用。
---

# To Issues

> 原文:[skills/engineering/to-issues/SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-issues/SKILL.md)

把 plan 用**垂直切片(示踪弹)**拆成可独立认领的 issue。

Issue tracker 和 triage 标签词表应该已经提供给你了——没有的话跑 `/setup-matt-pocock-skills`。

## 流程

### 1. 采集上下文

直接用对话里已有的内容。如果用户传了 issue 引用(编号、URL、路径)作为参数,**从 issue tracker 取它的完整正文和评论**。

### 2. 探索代码库(可选)

如果你还没探索过代码库,做一次。Issue 标题和描述应该用项目领域术语表的词汇,并尊重你正在动的区域的 ADR。

### 3. 起草垂直切片

把 plan 拆成**示踪弹**式的 issue。每个 issue 都是一条**穿过所有集成层、端到端的薄垂直切片**,**不是**单层的水平切片。

切片可以是 'HITL' 或 'AFK'。HITL 切片需要人介入,例如架构决策或设计评审。AFK 切片不需要人介入就能实现并合并。**能 AFK 就别 HITL**。

<垂直切片规则>
- 每个切片提供一条窄但**完整**的路径,穿过每一层(schema、API、UI、tests)
- 完成的切片可以单独演示或验证
- **多个薄切片**优于**少个厚切片**
</垂直切片规则>

### 4. 让用户来挑

把拆解方案作为编号列表展示。每个切片显示:

- **标题**:简短描述性名称
- **类型**:HITL / AFK
- **被阻塞于**:必须先完成的其它切片(如有)
- **覆盖的 user stories**:本切片对应哪些 user story(如果原材料有)

问用户:

- 颗粒度感觉对吗?(太粗 / 太细)
- 依赖关系对吗?
- 哪些切片该合或该再拆?
- HITL / AFK 标记对吗?

**迭代到用户批准**为止。

### 5. 发布 issue 到 tracker

每个通过的切片发一条新 issue。用下面的模板。这些 issue 视为 AFK 就绪,**用正确的 triage 标签发布**(除非另有指示)。

**按依赖顺序发布**(blocker 先发),这样你可以在 "Blocked by" 字段里引用真实的 issue 编号。

<issue 模板>
## Parent

引用 issue tracker 上的父 issue(原材料是已有 issue 才写,否则省略本节)。

## What to build

简洁描述这个垂直切片。**描述端到端行为,不要逐层描述实现**。

避免具体文件路径或代码片段——它们很快会过时。**例外**:如果原型产出了一段比散文更精确编码决策的代码(状态机、reducer、schema、类型形状),内联进来,简短说明它来自原型。**只留决策密度高的部分**——不是可运行 demo,只是关键片段。

## Acceptance criteria

- [ ] 标准 1
- [ ] 标准 2
- [ ] 标准 3

## Blocked by

- 引用阻塞工单(如有)

如无阻塞,写 "None - 可立刻开始"。

</issue 模板>

**不要**关或修改任何父 issue。
