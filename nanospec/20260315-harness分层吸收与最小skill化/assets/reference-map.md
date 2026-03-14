# 参考仓库能力地图

## 1. 仓库定位

| 仓库 | 主导价值 | 适合吸收的内容 | 暂不直接吸收的内容 |
| --- | --- | --- | --- |
| `everything-claude-code` | 大而全的技能、命令、agent、rules 资产库 | 单一意图 skill、评估观念、研究/检索模式、持续验证模式 | 全量 rules、平台安装方式、重命令体系、语言矩阵扩张 |
| `superpowers` | 强流程约束的工程工作流 | brainstorm / plan / review / debug 这类流程骨架 | worktree 前置、强制 subagent 流程、重度实现阶段约束 |
| `oh-my-opencode` | 运行时编排与工具系统总成 | 技能按需加载、能力分层、agent 类别映射等设计思想 | 多模型编排、内建 MCP、Hashline、tmux、hooks、CLI 体系 |

## 2. 按能力层分组

### A. 任务流转层

- 代表来源：`superpowers/skills/brainstorming`、`superpowers/skills/writing-plans`
- 价值：把“先澄清、再规格、再计划、再执行”固化为稳定节奏
- 当前仓库现状：已有 `nanospec`，这层已经有基础骨架
- 吸收建议：只吸收可补足 `nanospec` 的轻量方法，不重复造一个新流程系统

### B. 研究检索层

- 代表来源：`everything-claude-code/skills/search-first`、`iterative-retrieval`
- 价值：在写代码前先查本地实现、测试、外部方案，且在大仓库中用渐进检索降低上下文浪费
- 当前仓库现状：缺少专门服务 coding 任务的 research-before-coding skill
- 吸收建议：优先级高，适合最先做成最小 skill

### C. 质量保障层

- 代表来源：`everything-claude-code/skills/verification-loop`，`superpowers/requesting-code-review`、`test-driven-development`
- 价值：把代码改动从“自我感觉完成”变成“测试先行 + 机械验证 + 独立评审”的闭环
- 当前仓库现状：已有 `eval-harness` 适合做资产评估，但缺 coding 改动后的通用验证 skill
- 吸收建议：不要逐个复刻 `verification-loop`、`requesting-code-review`、`test-driven-development`，而要把三者压缩成一条更小的质量链路

### D. 资产治理层

- 代表来源：`everything-claude-code/skills/skill-stocktake`、`continuous-learning`
- 价值：控制 skill 重复、过期、碎片化，并沉淀有效模式
- 当前仓库现状：随着 skill 数量增加，这层会很快变重要
- 吸收建议：先做“盘点/合并建议”类能力，再考虑自动学习

### E. 运行时基础设施层

- 代表来源：`oh-my-opencode` 的 hooks、MCP、agent 分类、安装体系；`everything-claude-code` 的 hooks/rules/agents
- 价值：让 harness 更自动、更强大
- 当前仓库现状：与当前“沉淀最小 prompt 资产”的目标不匹配
- 吸收建议：暂缓，只保留设计启发，不进入第一波落地

## 3. 最小 skill 吸收准则

一个候选能力只有同时满足以下条件，才进入当前仓库：

1. 对应单一用户意图，而不是一整套大流程。
2. 不依赖特定平台运行时特性也能成立，或能优雅降级。
3. 能产出清晰、可落盘的仓库产物，而不是只存在于会话行为里。
4. 能定义最小 eval，至少能做规则或代码级校验。
5. 与现有 `nanospec`、`eval-harness` 不重复，而是补位。

## 4. 第一波建议吸收方向

### 4.1 `search-first`

- 来源：`search-first` + `iterative-retrieval`
- 作用：在写新功能、修 bug、引依赖、抽象工具前，先检索本地实现、测试和外部方案
- 目标：降低重复造轮子和闭门造车成本

### 4.2 `coding-quality-loop`

- 来源：`test-driven-development`、`verification-loop`、`requesting-code-review`
- 作用：覆盖实现时约束、改动后验证、独立审查三个控制点
- 目标：压缩成单 skill 入口，并通过阶段路由模拟 commands 式易用性

### 4.3 `skill-stocktake` 或同类治理 skill

- 来源：`skill-stocktake`
- 作用：定期扫描本仓库已有 `skills/`、`commands/`、`evals/`，发现重叠、过时、过宽泛资产
- 目标：作为后续治理能力，而不是第一波 coding 技能

## 5. 明确延后项

- 多 agent 编排与强依赖 subagent 的执行流程
- hooks 驱动的自动学习与自动注入
- 平台专属安装脚本、插件系统、市场分发
- 多模型路由、tmux、Hashline、内建 MCP 体系

这些内容不是没价值，而是与当前仓库阶段不匹配。
