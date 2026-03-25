# 20260325-github-workflows与PR生命周期补齐

背景：

- 当前暂存区包含一整波与 GitHub / PR 生命周期相关的改动，但还没有对应的 `nanospec` 任务容器。
- 这波改动不仅新增了 `packages/github-workflows/`，还补了多份调研材料，并同步调整了仓库 README、包边界说明与 `.learned` 沉淀。
- 用户要求先把“这一波改动”落到 nanospec 文档，再执行 commit。

目标：

- 为当前已暂存的 GitHub / PR 生命周期相关改动补齐 nanospec 中间文档。
- 明确这波改动的范围、边界、交付物与与现有 package 的职责分工。
- 在补齐任务文档后，提交当前暂存区改动。

范围：

- 新增 `packages/github-workflows/` 包及其 Codex target 镜像。
- 补充 `.research/` 下与 Claude Code custom agents、PR / review / merge gap、参考 skill 映射相关的研究记录。
- 更新 `README.md`、`packages/README.md`、`packages/git-workflows/README.md`、`packages/quality-workflows/README.md` 的边界说明。
- 保留并提交本轮相关的 `.learned/rules.md`、`.learned/support.md` 更新。

约束：

1. 不重写这波 staged 改动的产品方向，只补齐与其一致的 nanospec 文档。
2. 文档默认使用中文，代码、路径、API 名称、协议关键字保持原文。
3. `github-workflows` 负责远端 PR 生命周期，不吞并本地 git 生命周期或质量判断内核。
