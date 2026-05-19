---
name: grill-with-docs
description: Grill 会话——用现有领域模型挑战你的计划,锐化术语,同步把决定写进文档(CONTEXT.md, ADRs)。当用户想用项目已有的语言和已记录的决策对计划做压力测试时使用。
---

> 原文:[skills/engineering/grill-with-docs/SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md)

<what-to-do>

**穷追猛打地审问我**,对这个计划的每个方面都问到位,直到我们达成共识。沿着设计树的每条分支走下去,一个个解决决策之间的依赖。**每个问题都给出你推荐的答案**。

**一次问一个问题**,等我对当前问题反馈完再继续。

**如果一个问题可以靠探索代码库回答,就先去探索代码库**,不要问我。

</what-to-do>

<supporting-info>

## 领域感知(Domain awareness)

探索代码库时,也要找现有文档:

### 文件结构

大部分仓库只有一个 context:

```
/
├── CONTEXT.md
├── docs/
│   └── adr/
│       ├── 0001-event-sourced-orders.md
│       └── 0002-postgres-for-write-model.md
└── src/
```

如果根目录有 `CONTEXT-MAP.md`,说明仓库有多个 context。这份 map 指向每个 context 的位置:

```
/
├── CONTEXT-MAP.md
├── docs/
│   └── adr/                          ← 系统级决策
├── src/
│   ├── ordering/
│   │   ├── CONTEXT.md
│   │   └── docs/adr/                 ← context 内部决策
│   └── billing/
│       ├── CONTEXT.md
│       └── docs/adr/
```

**懒加载创建文件**——有东西要写的时候再建。没 `CONTEXT.md` 就在第一个术语被定义时创建;没 `docs/adr/` 就在第一份 ADR 需要时创建。

## 会话进行中

### 用术语表挑战

用户用了一个跟 `CONTEXT.md` 现有语言冲突的词,立刻指出来。"你的术语表把 'cancellation' 定义成 X,但你刚说的好像是 Y——到底是哪个?"

### 锐化模糊语言

用户用了含糊或被滥用的词,提一个精确的"规范词"。"你说 'account'——你指的是 Customer 还是 User?这是两个不同的概念。"

### 用具体场景压测

讨论领域关系时,**用具体场景做压力测试**。编造一些场景去触发边界条件,逼用户对概念之间的边界说清楚。

### 与代码交叉印证

用户说了某个东西是怎么工作的,**去看代码同不同意**。发现矛盾就摆出来:"你的代码取消的是整个 Order,但你刚说支持部分取消——以哪个为准?"

### 现场更新 CONTEXT.md

一个术语一被定义,**立刻**更新 `CONTEXT.md`。不要攒着批量做——发生时就抓下来。用 [CONTEXT-FORMAT.md](./CONTEXT-FORMAT.md) 的格式。

`CONTEXT.md` **不应该有任何实现细节**。不要把 `CONTEXT.md` 当 spec、当草稿、当实现决策仓库。**它只是术语表,仅此而已**。

### 谨慎提议 ADR

只有三个条件**全部**满足时才提议建 ADR:

1. **难以回滚** — 以后改主意的成本是实质的
2. **没上下文就难以理解** — 未来读者会想"他们当初为啥这么干?"
3. **是真权衡的结果** — 当时有真正的备选,你出于具体理由选了一个

任何一个不满足,就不要建 ADR。用 [ADR-FORMAT.md](./ADR-FORMAT.md) 的格式。

</supporting-info>
