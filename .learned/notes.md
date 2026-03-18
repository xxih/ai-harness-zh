# Notes

## 2026-03-18 skill 分发与默认落点

### Note: 区分默认记录目录与仓库实现细节

- 内容：在收敛通用 skill 的仓库强绑定表述时，不能把所有路径都一刀切删掉。像 `.research/`、`.quality/`、`.learned/` 这类目录不是“因为当前仓库先约定了才顺手保留”，而是这些 research / quality / learning skill 本来就需要有默认记录落点；当前仓库之所以有这些目录，是因为真实在使用这些 skill。真正该去掉的是 `src/...`、`targets/...`、`nanospec`、领域分层、分发副本路径等实现层细节。
- 证据：`nanospec/20260318-写skill的skill/alignment.md` 中 2026-03-18 的三次对齐记录；提交 `92a6ad0` 与后续修正提交 `6eb4429`
- 下一步：`promote-later`
