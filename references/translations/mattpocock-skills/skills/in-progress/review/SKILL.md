---
name: review
description: 沿两条轴评审从某固定点(commit、branch、tag、merge-base)起的变更——Standards(代码是否遵循本仓库编码规范?)+ Spec(代码是否匹配对应 issue/PRD 的要求?)。两路评审作为并行 sub-agent 跑,结果并排呈现。当用户想评审一条分支、PR、WIP 改动,或说"review since X"时使用。
---

# Review

> 原文:[skills/in-progress/review/SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/in-progress/review/SKILL.md)

对 `HEAD` 与用户给的固定点之间的 diff 做**双轴评审**:

- **Standards** —— 代码是否符合本仓库的成文编码规范?
- **Spec** —— 代码是否忠实实现了对应 issue / PRD / spec?

两条轴作为**并行 sub-agent** 跑,**互相不污染上下文**,然后本 skill 汇总。

Issue tracker 应该已经提供给你了——`docs/agents/issue-tracker.md` 缺失就跑 `/setup-matt-pocock-skills`。

## 流程

### 1. 固定那个"起点"

**用户说的就是起点**——commit SHA、分支名、tag、`main`、`HEAD~5` 等等。**别有立场,原样透传**。用户没指定就问:"对照什么评?分支、commit,还是 `main`?" **拿到之前不动**。

把 diff 命令记下来:`git diff <fixed-point>...HEAD`(**三个点,这样比较的是 merge-base**)。也记下 commit 列表:`git log <fixed-point>..HEAD --oneline`。

### 2. 找 spec 来源

按这个顺序找原始 spec:

1. commit 信息里的 issue 引用(`#123`、`Closes #45`、GitLab `!67` 等)——通过 `docs/agents/issue-tracker.md` 的工作流取。
2. 用户作为参数传的路径。
3. `docs/`、`specs/` 或 `.scratch/` 下与分支名/功能匹配的 PRD/spec 文件。
4. 都没找到就问用户。如果说没有,**Spec sub-agent 会跳过并报告 "no spec available"**。

### 3. 找 standards 来源

仓库里任何文档化"代码该怎么写"的东西。常见位置:

- `CLAUDE.md`、`AGENTS.md`
- `CONTRIBUTING.md`
- `CONTEXT.md`、`CONTEXT-MAP.md`、各 context 的 `CONTEXT.md`
- `docs/adr/`(架构决策也是规范)
- `.editorconfig`、`eslint.config.*`、`biome.json`、`prettier.config.*`、`tsconfig.json`(**机器强制的规范**——记一下,但**别重复检查工具已经检查的东西**)
- 仓库根或 `docs/` 下任何 `STYLE.md`、`STANDARDS.md`、`STYLEGUIDE.md` 之类

把文件清单收齐。**Standards sub-agent 会读它们**。

### 4. 并行派两个 sub-agent

发**一条消息含两个 `Agent` 工具调用**。两个都用 `general-purpose` subagent。

**Standards sub-agent prompt** —— 含:

- 完整 diff 命令 + commit 列表
- 第 3 步找到的 standards 来源文件清单
- Brief:"读规范文档。然后读 diff。**逐文件/逐 hunk**报告 diff 违反成文规范的地方。**引用规范**(文件 + 规则)。**区分硬违规和判断题**。**跳过工具能强制的**。400 字以内。"

**Spec sub-agent prompt** —— 含:

- diff 命令 + commit 列表
- spec 的路径或取到的内容
- Brief:"读 spec。然后读 diff。报告:(a) spec 要求但缺失或部分实现的;(b) diff 里没被要求的行为(scope creep);(c) 看起来已实现但实现错了的。**每条发现引用 spec 行**。400 字以内。"

spec 缺失就**跳过 Spec sub-agent**,在最终报告里注明。

### 5. 汇总

两份报告分别放在 `## Standards` 和 `## Spec` 标题下,**原样或轻清理**。**不要合并或重排发现** —— 两条轴故意分开,这样用户能独立看。

末尾**一行总结**:每轴的发现总数,以及最糟的一条(如有)。

## 为什么两条轴

一次变更可以**一条过另一条没过**:

- 严格遵循所有规范但实现了错的东西 → **Standards 过,Spec 不过**
- 完全做了 issue 要求的但破坏了项目惯例 → **Spec 过,Standards 不过**

**分开报告,避免一条掩盖另一条**。
