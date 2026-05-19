# Interface Design(接口设计)

> 原文:[INTERFACE-DESIGN.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/improve-codebase-architecture/INTERFACE-DESIGN.md)

当用户想为某个加深候选探索备选接口时,用这个**并行子 agent**模式。基于 Ousterhout 的 "Design It Twice"——你的第一个想法不太可能是最佳的。

使用 [LANGUAGE.md](LANGUAGE.md) 的词表——**module**、**interface**、**seam**、**adapter**、**leverage**。

## 流程

### 1. 框出问题空间

派 sub-agent 之前,先写一段**面向用户**的"问题空间"说明:

- 任何新接口必须满足的约束
- 它会依赖什么、依赖属于哪个类别(见 [DEEPENING.md](DEEPENING.md))
- 一段粗略的示意代码草图来锚定约束 —— **不是方案,只是把约束变具体**

把这给用户看,**然后立刻进 Step 2**。**用户边读边想,子 agent 在并行干活**。

### 2. 派子 agent

并行派 3+ 个子 agent。**每个必须产出一份"截然不同"的加深模块接口**。

每个子 agent 用单独的技术 brief(文件路径、耦合细节、来自 [DEEPENING.md](DEEPENING.md) 的依赖类别、seam 背后是什么)。这份 brief 和 Step 1 的"面向用户的问题空间说明"**独立**。**每个 agent 给一个不同设计约束**:

- Agent 1:"**最小化接口**——最多 1-3 个入口。每个入口最大杠杆。"
- Agent 2:"**最大化灵活性**——支持多种用例和扩展。"
- Agent 3:"**为最常见的调用方优化**——把默认情况做到 trivial。"
- Agent 4(如适用):"**围绕 ports & adapters 设计跨 seam 依赖**。"

Brief 里**同时包含** [LANGUAGE.md](LANGUAGE.md) 词表 **和** CONTEXT.md 词表,这样每个子 agent 命名都和架构语言 + 项目领域语言一致。

每个子 agent 输出:

1. 接口(类型、方法、参数 —— 加上不变量、顺序、错误模式)
2. 使用示例,展示调用方怎么用
3. 实现在 seam 背后藏了什么
4. 依赖策略 + 适配器(见 [DEEPENING.md](DEEPENING.md))
5. 权衡 —— 杠杆高在哪、薄在哪

### 3. 呈现 + 比较

**逐个呈现**设计,让用户消化,然后**用散文比较**。从 **depth**(接口处的杠杆)、**locality**(变更集中点)、**seam 放置**对比。

比较完**给出你自己的推荐**:你认为哪个最强、为什么。如果几个设计的元素能合体,**提议混合体**。**要有立场**——用户想要强烈的判断,不是菜单。
