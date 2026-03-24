# everything-claude-code 中文翻译

## 当前范围

- 来源仓库：`/Users/xxih/workspace/my-everything-claude-code`
- canonical 对照：`references/repos/everything-claude-code`
- 当前已汇总：`README.zh-CN.md` 与 `docs/zh-CN/**`
- 当前额外保留：`docs/zh-CN/codex-mcp-servers-guide.md`（仅在本机已翻译仓库中存在）

## 当前同步状态

- 2026-03-23 已将 `references/repos/everything-claude-code` 快进到最新 upstream `main`
- 当前 canonical HEAD：`bacc585b877b4426627d1cc478e1f1e5eb0c4f94`
- 当前中文镜像仍来自较早的本机译稿导入，不等同于 canonical 最新状态
- 已确认 2026-03-13 之后的 upstream 变更命中了当前翻译覆盖范围，包括 `README.md`、`commands/orchestrate.md` 以及多份 `docs/zh-CN/**` 对应源文件，因此当前中文镜像应视为“待补同步”，不能直接当作最新译稿使用

## 汇总说明

- 这批内容不是本仓库重新翻译，而是直接复用你本机已有的 ECC 中文译稿
- 目录保持原仓库相对路径，方便后续逐文件对照 upstream
- `manifest.json` 记录本次导入所依据的本机仓库 commit，以及当前 canonical 参考仓库 commit

## 后续同步建议

1. 先以 `references/repos/everything-claude-code` 的当前 HEAD 为基线，筛出当前翻译覆盖范围内被 upstream 改动的源文件
2. 优先回收最新、最完整的本机 ECC 中文译稿；若该副本仍落后 upstream，则按命中文件补翻
3. 完成中文同步后，再更新 `manifest.json` 的 `source.head_commit`、`canonical_reference.head_commit` 与对应 `source_sha256`
4. 若某个中文文件只是本机补充稿，不要误记成逐段翻译
