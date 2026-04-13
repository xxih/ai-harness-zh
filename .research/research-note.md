# 2026-04-14 reference 翻译巡检记录

## 背景

- 任务：日常巡检 `references/repos/` 中各参考仓库，检查本地中文翻译是否缺漏，并在当前可用快照上补齐缺口。
- 限制：当前运行环境无法访问 GitHub，`git fetch --all --prune` 对所有 reference 仓库均失败，因此本次只能基于本地已有副本完成审阅与翻译。

## 本地对照结论

- `agency-agents`
  - `manifest` 记录的 22 份翻译与本地 `main@6254154` 全部对齐。
  - 但 `integrations/*/README.md` 实际共有 11 份，本地仅翻译了 6 份，缺 `README.md`、`antigravity/README.md`、`gemini-cli/README.md`、`opencode/README.md`、`windsurf/README.md`。
- `superpowers`
  - 本地 `main` 已到 `8ea3981`，`manifest` 仍停留在旧 commit `7e51643`。
  - 当前已覆盖的 `skills/*/SKILL.md` 共 14 份，哈希无漂移，无新增缺口。
- `get-shit-done`
  - 本地 `main` 已到 `d7d88ae`，`manifest` 仍停留在旧 commit `1421dc0`。
  - 当前已覆盖的 `README.zh-CN.md`、`docs/zh-CN/**` 范围内哈希无漂移，无新增缺口。
- 其余已纳入 `manifest` 的 repo
  - `agency-agents`、`alirezarezvani-claude-skills`、`byheaven-skills`、`claudeception`、`everything-claude-code`、`gstack`、`happy-claude-skills`：本地 snapshot 与已记录翻译哈希一致。
  - `oh-my-opencode` 原先保留“外部 source 路径 + 当前仓库 canonical 副本”的双基线结构；后续已改为统一指向仓库内 `references/repos/oh-my-opencode`。

## 候选实现清单

- 本地翻译说明：
  - `references/translations/README.md`
  - `references/translations/agency-agents/README.md`
- 待补翻源文件：
  - `references/repos/agency-agents/integrations/README.md`
  - `references/repos/agency-agents/integrations/antigravity/README.md`
  - `references/repos/agency-agents/integrations/gemini-cli/README.md`
  - `references/repos/agency-agents/integrations/opencode/README.md`
  - `references/repos/agency-agents/integrations/windsurf/README.md`
- 状态对照：
  - `references/translations/agency-agents/manifest.json`
  - `references/translations/superpowers/manifest.json`
  - `references/translations/get-shit-done/manifest.json`

## 决策

- 结论：`adapt`
- 原因：
  - 仓库已经有 `manifest.json` + repo 级 `README.md` 的翻译同步机制，不需要另建工具。
  - 这次缺口属于既有范围的自然扩展，直接沿用现有目录结构和记录方式补齐最合适。
  - 对 `superpowers` 与 `get-shit-done`，只需在确认哈希未漂移后更新 `head_commit`，不需要重写译文。
