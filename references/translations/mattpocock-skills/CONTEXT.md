# CONTEXT.md(中文翻译)

> 原文:[CONTEXT.md](https://github.com/mattpocock/skills/blob/main/CONTEXT.md)

# Matt Pocock Skills

一套被 Claude Code 加载的 agent skill(slash 命令 + 行为)合集。Skills 按"桶"分类,由 `/setup-matt-pocock-skills` 生成的"每仓库配置"消费。

## 术语(Language)

**Issue tracker(问题追踪器)**
托管仓库 issue 的工具——GitHub Issues、Linear、本地 `.scratch/` markdown 约定,或类似的东西。`to-issues`、`to-prd`、`triage`、`qa` 这些 skill 都会向它读写。
**避免说**:backlog manager、backlog backend、issue host

**Issue(问题)**
**Issue tracker** 里追踪的一个工作单元——bug、任务、PRD,或 `to-issues` 产出的一个 slice。
**避免说**:ticket(只在引用外部系统时才用)

**Triage role(triage 角色)**
triage 过程中贴在 **Issue** 上的状态机标签(例如 `needs-triage`、`ready-for-afk`)。每个角色通过 `docs/agents/triage-labels.md` 映射到 **Issue tracker** 里真实的标签字符串。

## 关系

- 一个 **Issue tracker** 装很多个 **Issue**
- 一个 **Issue** 同时只挂一个 **Triage role**

## 标记的歧义点

- "backlog" 之前同时被用来指"承载 issue 的*工具*"和"工具里的*工作量本体*"——已解决:工具叫 **Issue tracker**,"backlog"不再作为领域术语使用。
- "backlog backend" / "backlog manager"——已解决:合并为 **Issue tracker**。
