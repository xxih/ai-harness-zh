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

# 2026-05-08 reference 翻译巡检记录

## 背景

- 任务：继续巡检 `references/repos/` 中各参考仓库的本地快照，检查中文翻译是否缺漏，并补齐可直接补齐的缺口。
- 限制：当前运行环境仍无法访问 GitHub。`git fetch --all --prune` 对所有 reference 仓库都失败：
  - `agency-agents` 使用 SSH，`github.com:22` 被阻断。
  - 其余大多走 HTTPS，但当前环境尝试连 `127.0.0.1:7897` 代理失败。
- 额外观察：仓库根工作区存在用户改动 `plugins/workbench/skills/grill-me/SKILL.md`，本轮未触碰。

## 本地对照结论

- 已有 translation roots：`agency-agents`、`alirezarezvani-claude-skills`、`byheaven-skills`、`claudeception`、`everything-claude-code`、`get-shit-done`、`gstack`、`happy-claude-skills`、`oh-my-opencode`、`superpowers`。
- 参考仓库但尚未建 translation root：`openspec`。本轮未新开范围。
- `agency-agents`、`alirezarezvani-claude-skills`、`byheaven-skills`、`claudeception`、`everything-claude-code`、`happy-claude-skills`、`superpowers` 的已记账条目与本地 repo HEAD 对齐。
- `get-shit-done` 的 `manifest` 口径里混用了“已翻译目标路径”和“严格 source 对照条目”，脚本级缺项主要是记账口径问题，不代表正文缺文件。
- `oh-my-opencode` 仍保留“中文资产不是逐段对照翻译”的记账方式，不能直接按 source hash 审计。
- `gstack` 有两类信号：
  - 本地缺少 7 份高相关中文文档：3 份 `docs/*` 与 4 份 `openclaw/*`。
  - 已纳入 `manifest` 的既有范围里，仍有 56 份 source hash 漂移，说明旧译文后续还需要继续人工同步。

## 候选实现清单

- 说明与记账：
  - `references/translations/README.md`
  - `references/translations/gstack/README.md`
  - `references/translations/gstack/manifest.json`
- 待补翻源文件：
  - `references/repos/gstack/docs/ADDING_A_HOST.md`
  - `references/repos/gstack/docs/OPENCLAW.md`
  - `references/repos/gstack/docs/REMOTE_BROWSER_ACCESS.md`
  - `references/repos/gstack/openclaw/agents-gstack-section.md`
  - `references/repos/gstack/openclaw/gstack-full-CLAUDE.md`
  - `references/repos/gstack/openclaw/gstack-lite-CLAUDE.md`
  - `references/repos/gstack/openclaw/gstack-plan-CLAUDE.md`

## 决策

- 结论：`adapt`
- 原因：
  - `gstack` 已经有稳定的翻译目录和 `manifest` 记账机制，直接沿用最合理。
  - 本轮最明确的“缺漏”是尚未收录的 OpenClaw / host onboarding / remote browser 文档，适合先补齐范围。
  - 既有 `gstack` 大量 source hash 漂移说明仍有存量债务，但本轮无法在同一 turn 内安全补完 56 份，先记录并收敛增量缺口更稳妥。
