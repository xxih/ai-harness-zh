# 内部资产包

`packages/` 是当前仓库自有资产的主组织入口。

默认原则：

- 能单独理解、单独分发、单独运行的能力，优先直接做成 package
- 分类关系交给 README 组织，不再依赖 `domains` 目录分层
- package 可以同时包含 source 资产、target 包、包内参考资料与搭配上下文

## 包结构

常见目录：

- `README.md`
- `skills/`、`agents/`、`commands/`
- `_AGENTS.md`
- `targets/<tool>/`
- `references/`

不是每个包都必须拥有全部目录；只保留完成该主题所需的最小结构。

## 当前包清单

### 工作流

- `packages/nanospec/`
- `packages/spec-driven/`
- `packages/search-first/`
- `packages/session-workflows/`
- `packages/agent-orchestration/`
- `packages/git-workflows/`
- `packages/github-workflows/`

### 资产治理与沉淀

- `packages/writing-skills/`
- `packages/learning-evolution/`

### 内容生产

- `packages/content-writing/`

### 质量工作流

- `packages/quality-workflows/`

### 平台适配

- `packages/codex-base/`
