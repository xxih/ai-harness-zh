---
name: improve-codebase-architecture
description: 借助 CONTEXT.md 领域语言和 docs/adr/ 决策,在代码库里找"加深模块"的机会。当用户想改善架构、找重构机会、合并紧耦合模块,或让代码库更可测、对 AI 更易导航时使用。
---

# Improve Codebase Architecture(改善代码库架构)

> 原文:[skills/engineering/improve-codebase-architecture/SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/improve-codebase-architecture/SKILL.md)

把架构摩擦摆出来,**提出加深机会**——把浅模块变成深模块的重构。**目标是可测试 + AI 易导航**。

## 词表

**每条建议都精确使用这些术语**。一致的语言就是这个 skill 的全部要点——别漂到 "component"、"service"、"API"、"boundary"。完整定义见 [LANGUAGE.md](LANGUAGE.md)。

- **Module(模块)** —— 任何有接口 + 实现的东西(函数、类、包、切片)。
- **Interface(接口)** —— 调用方为用这个模块必须知道的一切:类型、不变量、错误模式、顺序、配置。**不只是类型签名**。
- **Implementation(实现)** —— 内部代码。
- **Depth(深度)** —— 接口上的杠杆:小接口背后藏了大量行为。**深** = 高杠杆。**浅** = 接口几乎和实现一样复杂。
- **Seam(接缝)** —— 接口所在的位置;**不修改原地代码就能改变行为**的地方。(用这个,不用 "boundary"。)
- **Adapter(适配器)** —— 在 seam 上满足接口的具体物件。
- **Leverage(杠杆)** —— 调用方从深度中获得的东西。
- **Locality(局部性)** —— 维护者从深度中获得的东西:变更、bug、知识集中在一处。

关键原则(完整列表见 [LANGUAGE.md](LANGUAGE.md)):

- **删除测试**:想象删掉这个模块。如果复杂度消失了,它就是个透传。如果复杂度在 N 个调用方那里重新冒出来,它就是在干活。
- **接口就是测试表面**。
- **一个适配器 = 假想的 seam。两个适配器 = 真实的 seam**。

这个 skill 受项目领域模型**启发**。领域语言给好的 seam 取名;ADR 记录的决策**不该被本 skill 重新打官司**。

## 流程

### 1. 探索

**先**读项目领域术语表和你要动的区域的 ADR。

**然后**用 Agent 工具 `subagent_type=Explore` 走代码库。**别守着死板启发**——有机地探索,记下你感到摩擦的地方:

- 哪里理解一个概念需要在很多小模块间跳?
- 哪些模块是**浅的**——接口几乎和实现一样复杂?
- 哪里把纯函数抽出来只是为了可测试,但真 bug 藏在"怎么被调"里(没有 **locality**)?
- 哪些紧耦合模块在 seam 处漏?
- 代码库哪些部分没测试,或者很难通过当前接口测?

对怀疑是浅的东西**用删除测试**:删了之后复杂度会**集中**还是**移位**?**"集中"才是你要的信号**。

### 2. 摆出候选

用编号列表摆"加深机会"。每个候选:

- **Files** —— 涉及哪些文件 / 模块
- **Problem** —— 当前架构为什么造成摩擦
- **Solution** —— 用大白话描述要改什么
- **Benefits** —— 用 **locality** 和 **leverage** 解释,也说测试会怎么改善

**领域用 CONTEXT.md 词汇,架构用 [LANGUAGE.md](LANGUAGE.md) 词汇**。如果 `CONTEXT.md` 定义了 "Order",就说"Order 接收模块"——不是 "FooBarHandler",也不是 "Order service"。

**ADR 冲突**:候选与已有 ADR 冲突时,**只在摩擦真的大到值得重开 ADR 时摆出来**。明确标记(如 _"与 ADR-0007 矛盾——但值得重开,因为……"_)。**别列出 ADR 禁止的所有理论上的重构**。

**先不要提议接口**。问用户:"你想探索哪一个?"

### 3. Grilling 循环

用户挑了候选后,进入 grilling 对话。和他一起走设计树——约束、依赖、加深后模块的形状、seam 背后是什么、哪些测试能存活。

**决策成形时副作用同步发生**:

- **加深后的模块要命名为一个 `CONTEXT.md` 里没有的概念?** 把它加到 `CONTEXT.md`——和 `/grill-with-docs` 同款纪律(见 [CONTEXT-FORMAT.md](../grill-with-docs/CONTEXT-FORMAT.md))。文件不存在就懒创建。
- **对话中锐化了一个模糊术语?** 立刻更新 `CONTEXT.md`。
- **用户用一个承重理由否决了候选?** 提议建 ADR,框架是:_"要不要我把这个记成 ADR,这样以后架构评审不会再提同样建议?"_ **只在那个理由对未来的探索者真的"避免重复建议"承重时才提**——跳过临时理由("现在不值得")和自明理由。见 [ADR-FORMAT.md](../grill-with-docs/ADR-FORMAT.md)。
- **想探索加深后模块的备选接口?** 见 [INTERFACE-DESIGN.md](INTERFACE-DESIGN.md)。
