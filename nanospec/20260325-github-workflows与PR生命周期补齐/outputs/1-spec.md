# 规格说明：20260325-github-workflows与PR生命周期补齐

## 背景

当前仓库已经有本地 `git-workflows`、质量工作流和多 agent 编排能力，但针对 GitHub 远端 PR 生命周期的正式资产仍然缺位。本轮 staged 改动已经开始补这一层：新增 `github-workflows` 包、补充对应研究、并重新划分相关包边界。

由于这些改动此前没有对应的 nanospec 文档，当前需要先把任务意图和交付口径落盘，再执行提交。

## 目标

本任务需要为当前 staged 改动补齐 nanospec 工作面，至少回答四件事：

1. 为什么要新增 `packages/github-workflows/`。
2. 这个包与 `git-workflows`、`quality-workflows`、`agent-orchestration` 的职责边界是什么。
3. 这波研究文档与 `.learned` 更新分别在支持什么。
4. 当前提交的产物集合是什么。

## 交付范围

### 1. GitHub / PR 生命周期包

需要确认并记录 `packages/github-workflows/` 的定位。

成功标志：

- `packages/github-workflows/README.md` 明确说明这是远端 PR 生命周期包。
- 至少包含 `pr-lifecycle` 与 `merge-conflict-resolution` 两个 skill。
- 存在对应 `targets/codex/` 分发副本。

验收证据：

- `packages/github-workflows/README.md`
- `packages/github-workflows/skills/pr-lifecycle/SKILL.md`
- `packages/github-workflows/skills/merge-conflict-resolution/SKILL.md`
- `packages/github-workflows/targets/codex/`

### 2. 包边界调整

需要确认现有工作流包的职责切分。

成功标志：

- `packages/git-workflows/README.md` 明确只覆盖本地 branch / worktree 生命周期。
- `packages/quality-workflows/README.md` 明确仍负责质量判断，不承接远端 PR 动作。
- 根 `README.md` 与 `packages/README.md` 已将 `github-workflows` 纳入分类说明。

验收证据：

- `README.md`
- `packages/README.md`
- `packages/git-workflows/README.md`
- `packages/quality-workflows/README.md`

### 3. 研究与学习沉淀

需要说明研究记录和 `.learned` 更新是本轮改动的一部分。

成功标志：

- `.research/` 下新增文档能解释这波包设计的原料来源。
- `.learned/rules.md` 与 `.learned/support.md` 更新能说明 README 读者视角与 AI Harness 总览写法的长期规则 / 支撑卡。
- 文档中不把 `.learned` 误写成当前包的实现部分。

验收证据：

- `.research/claude-code-custom-agents-best-practices.md`
- `.research/pr-review-merge-gap-analysis.md`
- `.research/reference-pr-review-skills-note.md`
- `.learned/rules.md`
- `.learned/support.md`

### 4. NanoSpec 文档补齐

需要为这一波 staged 改动补齐 nanospec 容器。

成功标志：

- `brief.md`、`outputs/1-spec.md`、`outputs/2-plan.md`、`outputs/3-tasks.md` 已填写。
- 文档能覆盖当前 staged 改动，而不是泛泛描述未来计划。

验收证据：

- `nanospec/20260325-github-workflows与PR生命周期补齐/brief.md`
- `nanospec/20260325-github-workflows与PR生命周期补齐/outputs/1-spec.md`
- `nanospec/20260325-github-workflows与PR生命周期补齐/outputs/2-plan.md`
- `nanospec/20260325-github-workflows与PR生命周期补齐/outputs/3-tasks.md`

## 非目标

- 不在本任务里补全真正的 `gh` / MCP 执行面。
- 不在本任务里实现 hooks、doctor、CI 修复运行时。
- 不重新设计 staged 里的 package 内容，只记录并提交当前这波改动。

## 约束

- 文档应准确反映当前 staged 产物，不替未来未实现能力背书。
- `github-workflows` 与 `git-workflows`、`quality-workflows` 的边界必须清楚，避免 README 再次失真。
