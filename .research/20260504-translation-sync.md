# 2026-05-04 翻译巡检记录

## 背景

- 自动化目标：更新 `references/repos/*`，检查 `references/translations/*` 是否缺漏，并补齐必要译稿。
- 当前环境网络受限，所有 `git fetch` / `git pull` 都无法连到 GitHub，因此本次只能基于本地 `references/repos/*` 现有工作副本做离线巡检。

## fetch 结果

以下参考仓库均尝试过 `fetch origin <branch>`，但都因网络受限失败：

- `agency-agents`
- `alirezarezvani-claude-skills`
- `byheaven-skills`
- `claudeception`
- `everything-claude-code`
- `get-shit-done`
- `gstack`
- `happy-claude-skills`
- `oh-my-opencode`
- `superpowers`

本地可用基线仍为当前 checkout 的分支 HEAD：

- `agency-agents`: `783f6a72bfd7f3135700ac273c619d92821b419a`
- `alirezarezvani-claude-skills`: `f567c61def3fb86046d7242b4bf27fceb63ad8b4`
- `byheaven-skills`: `a4e1b724b6aa52856f2cbfd3648c7cb4b084b3da`
- `claudeception`: `62dbb91d1183a866b5cf40079265c825b2695843`
- `everything-claude-code`: `e0ddb331f67bb5ddabeaf4874a28d54f4b3b836e`
- `get-shit-done`: `8b94f0370dcf8873a12ef2e6831cc5a133ddef42`
- `gstack`: `7e96fe299b085010fb2e34d9c4fbfc7e44b617e1`
- `happy-claude-skills`: `a10594619987450e3ae426d55c1860eafe12500e`
- `oh-my-opencode`: `a5db86ee1593cdf6379db9400ddce5ee783c9f5d`
- `superpowers`: `917e5f53b16b115b70a3a355ed5f4993b9f8b73d`

## manifest 巡检结论

### 已与本地参考仓库对齐

以下目录的 `manifest.json` 中 `source.head_commit` 与本地参考仓库 HEAD 一致，且抽样/脚本检查未发现额外缺口：

- `agency-agents`
- `alirezarezvani-claude-skills`
- `byheaven-skills`
- `claudeception`
- `everything-claude-code`
- `happy-claude-skills`
- `superpowers`

### get-shit-done

- `manifest.json` 已纳入 `docs/skills/discovery-contract.md`
- 当前已有对应中文译稿：`references/translations/get-shit-done/docs/skills/discovery-contract.md`
- 根仓库存在未提交翻译改动：
  - `references/translations/get-shit-done/README.md`
  - `references/translations/get-shit-done/README.zh-CN.md`
  - `references/translations/get-shit-done/manifest.json`
  - `references/translations/get-shit-done/docs/skills/discovery-contract.md`
- 参考仓库 `references/repos/get-shit-done` 自身还有未跟踪目录：
  - `docs/superpowers/`
  - `get-shit-done/commands/`
- 这两处未跟踪目录尚未纳入当前翻译范围，本次未扩 scope。

### oh-my-opencode

- `manifest.json` 已修正为以本地 `master` 为巡检分支，并记录 `origin/HEAD` 指向 `dev`
- 当前根仓库已有未提交改动：`references/translations/oh-my-opencode/manifest.json`

### gstack

- `manifest.json` 的 `source.head_commit` 与本地 HEAD 一致，但按 `source_sha256` 对比时发现大范围漂移
- 已确认当前根仓库已有未提交改动：
  - `references/translations/gstack/CLAUDE.md`
  - `references/translations/gstack/README.zh-CN.md`
  - `references/translations/gstack/manifest.json`
- 仍待继续同步的 source 条目很多，至少包括：
  - 根文档：`ARCHITECTURE.md`、`BROWSER.md`、`CONTRIBUTING.md`、`docs/skills.md`、`SKILL.md`
  - 多个子 skill：`autoplan/`、`benchmark/`、`browse/`、`codex/`、`cso/`、`design-*`、`office-hours/`、`plan-*`、`qa/`、`review/`、`ship/` 等
  - review 支撑文档：`review/design-checklist.md` 与 `review/specialists/*.md`
- 由于本次 worktree 中已存在进行中的 `gstack` 译稿修改，且剩余漂移范围较大，本次未继续覆盖式改写，避免把半完成工作与新审阅混在一起。

## 建议下一步

1. 在可联网环境下重新执行一次 fetch，确认本地参考仓库是否已落后 upstream。
2. 优先收口 `gstack`：
   - 先明确今天要同步的最小子集
   - 完成对应中文文件后，再批量刷新 `manifest.json` 的 `source_sha256`
3. 若要继续扩 `get-shit-done` 覆盖范围，先判断 `docs/superpowers/` 与 `get-shit-done/commands/` 是否属于“长期复用的核心 prompt 资产”。
