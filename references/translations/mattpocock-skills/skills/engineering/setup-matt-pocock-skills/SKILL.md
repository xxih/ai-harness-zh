---
name: setup-matt-pocock-skills
description: 在 AGENTS.md/CLAUDE.md 里建一个 `## Agent skills` 块,并在 docs/agents/ 下生成 issue tracker(GitHub / GitLab / 本地 markdown)、triage 标签词表、领域文档布局,供 engineering skill 读取。第一次用 `to-issues`、`to-prd`、`triage`、`diagnose`、`tdd`、`improve-codebase-architecture`、`zoom-out` 之前跑——或者这些 skill 看起来缺 issue tracker / triage 标签 / 领域文档上下文时也跑。
disable-model-invocation: true
---

# Setup Matt Pocock's Skills

> 原文:[skills/engineering/setup-matt-pocock-skills/SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/setup-matt-pocock-skills/SKILL.md)

为 engineering skill 假设存在的"每仓库配置"搭骨架:

- **Issue tracker** —— issue 住在哪里(默认 GitHub;本地 markdown 也开箱即用)
- **Triage 标签** —— 五个规范 triage 角色对应的字符串
- **领域文档** —— `CONTEXT.md` 和 ADR 住在哪里,以及读取规则

这是一个**提示驱动**的 skill,不是确定性脚本。**先探索,展示发现,确认,再写**。

## 流程

### 1. 探索

看当前仓库的起点状态。**读已有的东西,不要假设**:

- `git remote -v` 和 `.git/config` —— 是 GitHub 仓库吗?哪个?
- 根目录 `AGENTS.md` 和 `CLAUDE.md` —— 存在吗?是否已经有 `## Agent skills` 节?
- 根目录 `CONTEXT.md` 和 `CONTEXT-MAP.md`
- `docs/adr/` 以及 `src/*/docs/adr/`
- `docs/agents/` —— 之前是否跑过这个 skill?
- `.scratch/` —— 已使用本地 markdown issue tracker 约定的迹象

### 2. 呈现发现,提问

总结存在什么、缺什么。然后**一次一节**带用户走完三个决策——展示一节,拿用户答案,再下一节。**别一次性把三个都丢出来**。

**假设用户不懂这些术语**。每节先用短解释:这是什么、这些 skill 为什么需要它、选不同会怎样。然后给选项和默认值。

**Section A —— Issue tracker**

> 解释:"issue tracker" 是本仓库的 issue 住的地方。`to-issues`、`triage`、`to-prd`、`qa` 这些 skill 都会向它读写——它们要知道是该调 `gh issue create`、写一个 `.scratch/` 下的 markdown 文件、还是按你描述的其它工作流走。**选你实际追踪这个仓库工作的地方**。

默认姿态:这些 skill 是为 GitHub 设计的。`git remote` 指向 GitHub 就提议 GitHub。指向 GitLab(`gitlab.com` 或自托管)就提议 GitLab。否则(或用户偏好)给出:

- **GitHub** —— issue 住在仓库的 GitHub Issues(用 `gh` CLI)
- **GitLab** —— 住在仓库的 GitLab Issues(用 [`glab`](https://gitlab.com/gitlab-org/cli) CLI)
- **本地 markdown** —— issue 是本仓库 `.scratch/<feature>/` 下的文件(适合单人项目或没远端的仓库)
- **Other**(Jira、Linear 等)—— 让用户用一段话描述工作流;skill 会把它存为自由散文

**Section B —— Triage 标签词表**

> 解释:`triage` skill 处理新来的 issue 时,会沿一个状态机推进——需要评估、等报告人、AFK ready、需要人来做、不修。它需要打**和你实际配置匹配**的标签字符串。如果你的仓库已经用了别的标签名(例如 `bug:triage` 而不是 `needs-triage`),在这里映射,这样 skill 打对的标签而不是建重复。

五个规范角色:

- `needs-triage` —— 维护者需要评估
- `needs-info` —— 等报告人
- `ready-for-agent` —— 已完整规格化,AFK ready(agent 无需人类上下文就能拿起)
- `ready-for-human` —— 需要人来实现
- `wontfix` —— 不修

默认:每个角色的字符串等于它的名字。**问用户要不要覆盖**。如果 issue tracker 没有现有标签,默认值就够。

**Section C —— 领域文档**

> 解释:某些 skill(`improve-codebase-architecture`、`diagnose`、`tdd`)会读 `CONTEXT.md` 学项目领域语言,读 `docs/adr/` 看历史架构决策。它们要知道仓库有**一个**全局 context 还是**多个**(例如 monorepo 分 frontend/backend),这样才能去对的地方找。

确认布局:

- **单 context** —— 根目录一份 `CONTEXT.md` + `docs/adr/`。大部分仓库是这样。
- **多 context** —— 根目录 `CONTEXT-MAP.md` 指向每个 context 的 `CONTEXT.md`(通常是 monorepo)。

### 3. 确认 + 让用户编辑

把草稿给用户看:

- 要加到 `CLAUDE.md` / `AGENTS.md` 里(看第 4 步选择规则)的 `## Agent skills` 块
- `docs/agents/issue-tracker.md`、`docs/agents/triage-labels.md`、`docs/agents/domain.md` 的内容

写之前让他们编辑。

### 4. 写

**选要编辑的文件**:

- 有 `CLAUDE.md`:改它
- 没 `CLAUDE.md` 但有 `AGENTS.md`:改它
- 两个都没:问用户建哪个——**别自己定**

**`CLAUDE.md` 已存在时永远不要再建 `AGENTS.md`**(反之亦然)——永远改已存在的那一份。

如果选中的文件已经有 `## Agent skills` 块,**原地更新**,别追加重复块。不要覆盖用户对周边节的编辑。

块:

```markdown
## Agent skills

### Issue tracker

[一行话总结 issue 追踪在哪]. 见 `docs/agents/issue-tracker.md`.

### Triage labels

[一行话总结标签词表]. 见 `docs/agents/triage-labels.md`.

### Domain docs

[一行话总结布局 —— "single-context" 或 "multi-context"]. 见 `docs/agents/domain.md`.
```

然后写三份文档文件,用本 skill 目录里的种子模板作起点:

- [issue-tracker-github.md](./issue-tracker-github.md) —— GitHub issue tracker
- [issue-tracker-gitlab.md](./issue-tracker-gitlab.md) —— GitLab issue tracker
- [issue-tracker-local.md](./issue-tracker-local.md) —— 本地 markdown issue tracker
- [triage-labels.md](./triage-labels.md) —— 标签映射
- [domain.md](./domain.md) —— 领域文档读取规则 + 布局

对 "other" issue tracker,根据用户描述从零写 `docs/agents/issue-tracker.md`。

### 5. 完成

告诉用户 setup 完成了,以及哪些 engineering skill 现在会读这些文件。**提醒他们可以后续直接编辑 `docs/agents/*.md`**——只在想切换 issue tracker 或从零开始时才需要重跑本 skill。
