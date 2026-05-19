---
name: to-prd
description: 把当前对话上下文转成 PRD,发布到项目 issue tracker。当用户想从当前上下文生成 PRD 时使用。
---

> 原文:[skills/engineering/to-prd/SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-prd/SKILL.md)

这个 skill 接受**当前对话上下文 + 代码库理解**,产出一份 PRD。**不要面试用户**——就把你已经知道的东西综合成 PRD。

Issue tracker 和 triage 标签词表应该已经提供给你了——没有的话跑 `/setup-matt-pocock-skills`。

## 流程

1. 如果还没探索过仓库,先探索一下,了解代码库现状。**整份 PRD 都用项目领域术语表的词汇**,并尊重你正在动的区域的 ADR。

2. 草拟为完成这个实现需要构建或修改的**主要模块**。**主动找深模块的机会**——可以隔离测试的、稳定的简单接口。

深模块(相对于浅模块)是指:在一个简单、可测、很少变的接口背后封装了大量功能。

跟用户确认这些模块是否符合预期。确认他们希望为哪些模块写测试。

3. 用下面模板写 PRD,然后发到项目 issue tracker。**打上 `ready-for-agent` triage 标签**——不需要再 triage。

<PRD 模板>

## Problem Statement

**从用户视角**描述用户面临的问题。

## Solution

**从用户视角**描述对问题的解决方案。

## User Stories

一份**很长的**编号 user stories 列表。每条 user story 的格式:

1. As an <actor>, I want a <feature>, so that <benefit>

<user-story 例子>
1. As a mobile bank customer, I want to see balance on my accounts, so that I can make better informed decisions about my spending
</user-story 例子>

这份列表应该**极其详尽**,覆盖功能的所有方面。

## Implementation Decisions

实现决策清单。可以包括:

- 要构建/修改的模块
- 这些模块要修改的接口
- 来自开发者的技术澄清
- 架构决策
- Schema 变更
- API 合同
- 具体交互

**不要**包含具体文件路径或代码片段。它们可能很快过时。

**例外**:如果原型产出了一段比散文更精确编码决策的代码(状态机、reducer、schema、类型形状),把它内联在对应决策里,简短说明它来自原型。**只留决策密度高的部分**——不是可运行 demo,只是关键片段。

## Testing Decisions

测试决策清单。包括:

- 什么算好测试(只测外部行为,不测实现细节)
- 哪些模块会被测
- 测试的 prior art(代码库里已有的类似测试)

## Out of Scope

不在本 PRD 范围内的事。

## Further Notes

关于这个功能的其它笔记。

</PRD 模板>
