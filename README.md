# ai-harness-zh

`ai-harness-zh` 是一个以中文维护的 AI harness 工作区。仓库默认采用 package-first 组织：能单独理解、单独分发、单独运行的能力，优先直接做成 `packages/<package>/`，分类关系交给 README 来组织，而不是再塞进 `domains` 分层。

## 仓库定位

- 在 `packages/` 中维护当前仓库自有资产
- 把单主题能力做成可独立演进的 package 与 target 包
- 通过脚本同步 package source 与 Codex target，减少手工分发成本
- 在 `references/repos/` 中保留外部参考仓库，供 AI 读取但不纳入当前仓库 git 管理
- 在 `references/translations/` 中保留外部 prompt 中文翻译资产；这类资料不属于分发 package

## 根目录约定

- `packages/`
  - 当前仓库自有资产的主组织入口
- `references/repos/`
  - 外部参考仓库目录；不承载当前仓库自己的真实资产
- `references/translations/`
  - 外部 prompt 中文翻译资产；属于参考资料，不是分发 package
- `scripts/`
  - 仓库级自动化脚本，例如 Codex target 同步脚本
- `.learned/`、`.quality/`、`.research/`
  - 默认记录目录
- `.nanospec/`、`nanospec/`
  - NanoSpec 任务容器与当前任务指针

## package 分类

### 工作流

- `packages/nanospec/`
- `packages/spec-driven/`
- `packages/search-first/`
- `packages/agent-orchestration/`

### 资产治理与沉淀

- `packages/writing-skills/`
- `packages/learning-capture/`

### 质量工作流

- `packages/quality-workflows/`

### 平台适配

- `packages/codex-base/`

## package 结构约定

常见结构：

- `README.md`
  - 说明包边界、组成和维护方式
- `skills/`、`agents/`、`commands/`
  - 包的 source 资产
- `_AGENTS.md`
  - 包级搭配上下文载体；仅在确有需要时存在
- `targets/<tool>/`
  - 面向具体工具的 target 包
- `references/`
  - 属于该包的参考资料、研究记录或附属文档

## Codex target 同步

Codex target 分发默认通过脚本同步：

```bash
python3 scripts/sync_codex_targets.py
python3 scripts/sync_codex_targets.py nanospec learning-capture
```

脚本会把 package source 侧的 `skills/`、`agents/`、`commands/`、`_AGENTS.md` 镜像到对应 `packages/<package>/targets/codex/`，但不会覆盖 target 侧手写的 `README.md`、`.codex/` 等运行时文件。

## 外部参考仓库

需要参考其他仓库时，统一放在 `references/repos/` 下。

- 这里适合存放外部仓库的 clone 或软链接，例如 `oh-my-opencode`、`everything-claude-code`、`superpowers`
- `references/repos/` 只用于外部参考仓库，不承载当前仓库自己的真实资产
- 当前仓库自己的中文翻译资产保留在 `references/translations/`
