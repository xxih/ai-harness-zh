# everything-claude-code 中文翻译

## 当前范围

- 基线仓库：`references/repos/everything-claude-code`
- 当前镜像：`README.zh-CN.md` 与 `docs/zh-CN/**`
- 当前额外保留：`docs/zh-CN/codex-mcp-servers-guide.md`

## 当前同步状态

- 2026-03-28 已按 `references/repos/everything-claude-code` 当前 `main` HEAD 全量回收内置中文文件
- 当前 canonical HEAD：`bacc585b877b4426627d1cc478e1f1e5eb0c4f94`
- 当前翻译不再以旧的本机工作副本为新鲜度基线，而是直接镜像 canonical 副本中的 `README.zh-CN.md` 与 `docs/zh-CN/**`

## 本地适配

- 上游 `docs/zh-CN/AGENTS.md` 在当前仓库落为 `docs/zh-CN/_AGENTS.md`，以满足仓库内对 `AGENTS.md` 的约束
- `docs/zh-CN/codex-mcp-servers-guide.md` 仍是当前仓库自有的中文补充文档，不对应 upstream 英文源文件
- 对于 upstream 仅提供中文稿、未提供英文源文件的条目，`manifest.json` 会记为 `source: null`

## 维护说明

- 后续继续以 `references/repos/everything-claude-code` 为唯一对照基线
- 每次同步后同时更新 `manifest.json` 中的 `head_commit`、文件列表与 `source_sha256`
- 若 upstream 新增 `docs/zh-CN/**` 文件，默认一并纳入当前镜像范围
