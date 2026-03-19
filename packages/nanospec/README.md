# nanospec 包

这个包承载 NanoSpec 任务容器规范与 spec-driven 工作中间文档流程。

## 组成

- `skills/nanospec/`
  - `nanospec` skill source
- `targets/codex/`
  - `nanospec` 的 Codex target 包

## 维护方式

- 先更新 `skills/nanospec/`
- 再运行 `python3 scripts/sync_codex_targets.py nanospec`
