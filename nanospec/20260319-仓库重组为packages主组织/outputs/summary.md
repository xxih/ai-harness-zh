# 总结：仓库重组为 packages 主组织

## 1. 本轮交付

- 去掉了 `src/` 与根级 `targets/` 这两层旧主入口。
- 把可单独理解、单独分发的能力收敛到 `packages/`，包括：
  - `agent-orchestration`
  - `nanospec`
  - `search-first`
  - `spec-driven`
  - `writing-skills`
  - `learning-capture`
  - `quality-workflows`
  - `codex-base`
- 保留 `references/translations/` 作为翻译资料入口，不把翻译资产做成 package。
- 新增 `scripts/sync_codex_targets.py`，把 Codex target 镜像改成脚本同步。

## 2. 关键决策

- package-first 只作用于可分发资产层，不覆盖 `.nanospec/`、`nanospec/`、`.learned/`、`.quality/`、`.research/`、`scripts/` 等仓库基础设施。
- `references/repos/` 继续承载外部参考仓库。
- `references/translations/` 继续承载中文翻译资料，因为这类内容不是当前要分发出去的包。
- Codex target 脚本只同步 source 侧镜像内容，不覆盖 target 侧手写 runtime 文件，例如 `README.md`、`.codex/`。

## 3. 验证证据

- 目录结构：根目录已只保留 `packages/`、`references/`、`scripts/` 与任务/记录目录。
- 翻译入口：`references/translations/` 已恢复，`packages/upstream-translations/` 已移除。
- 脚本运行：`python3 scripts/sync_codex_targets.py` 已成功执行。
- 文档更新：`README.md`、`AGENTS.md`、`packages/README.md`、`references/README.md` 与各包 README 已同步到新口径。

## 4. 剩余风险

- 历史 NanoSpec 旧任务文档仍会提到 `src/domains/*`、根级 `targets/` 等旧结构；本轮未追溯改写旧任务记录。
- `quality-workflows/references/quality-agent-landscape.md` 这类内部参考文档仍保留部分旧路径语境；如后续要继续复用，可再单开任务清理。

## 5. 后续建议

- 如果后续出现新的 target 平台，继续沿用“包内 source + 包内 target + 根级脚本同步”的模式。
- 如果 Codex target 同步规则继续增多，可以再补一个 manifest，让脚本支持更细粒度的 include / exclude。
