# 2026-04-15 agency-agents 翻译巡检

## 问题

需要按 `references/translations/README.md` 的口径，检查 `references/repos/*` 的本地基线与中文翻译覆盖是否存在缺口，并补齐本轮新增或已变动的核心翻译资产。

## 候选来源

- 本地翻译规则：`references/translations/README.md`
- 当前覆盖记录：`references/translations/agency-agents/manifest.json`
- 本地 source 基线：`references/repos/agency-agents`
- 其他 reference 仓库：`references/repos/*`

## 研究结论

- 网络受限，无法执行 `git pull --ff-only origin main/master`；本轮只能以各 reference 仓库当前本地 HEAD 作为对照基线。
- `agency-agents` 是本轮最明确的真实变更点：`manifest.json` 记录的 `head_commit` 落后于本地 `references/repos/agency-agents` 的 HEAD，且变更落在已翻译范围内。
- `agency-agents` 在 `integrations/README.md` 中新增了 `Kimi Code` 与 `Qwen Code` 两个入口，并新增 `integrations/kimi/README.md`、`integrations/qwen/README.md` 两份 README，属于实际翻译缺口。
- 同一批变更还包含若干已覆盖文件的小范围英文改动，主要是把固定数量描述改成 “full Agency roster”，以及把 `Data Analytics Reporter` 更名为 `Analytics Reporter`。
- `gstack` 出现大量 hash 不匹配，但本地 reference 工作树干净，说明更像是旧 manifest hash 口径问题；本轮不在没有新增缺口证据的前提下大面积重翻。
- `get-shit-done` 与 `oh-my-opencode` 的 manifest 采用了非严格逐段镜像口径，本轮不把它们误判为新增翻译缺口。

## 决策

- `adapt`
- 复用既有 `agency-agents` 翻译结构，只补新增 `kimi/qwen` README，并同步已覆盖文档中的小范围更新。

## 已执行动作

- 新增：
  - `references/translations/agency-agents/integrations/kimi/README.md`
  - `references/translations/agency-agents/integrations/qwen/README.md`
- 更新：
  - `references/translations/agency-agents/integrations/README.md`
  - `references/translations/agency-agents/integrations/{aider,antigravity,claude-code,cursor,opencode,windsurf}/README.md`
  - `references/translations/agency-agents/strategy/{QUICKSTART.md,nexus-strategy.md}`
  - `references/translations/agency-agents/strategy/playbooks/{phase-3-build.md,phase-6-operate.md}`
  - `references/translations/agency-agents/manifest.json`

## 下一步

- 后续自动化继续先尝试拉取远端；若网络仍受限，继续显式记录“当前仅按本地 HEAD 巡检”的前提。
- 下一轮优先复查 `agency-agents` 是否又新增 integration README 或 strategic docs。
