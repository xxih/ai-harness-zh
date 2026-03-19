# ai-harness-zh

`ai-harness-zh` 是一个以中文维护的 AI harness 工作区。仓库先汇总、翻译并持续同步外部主流 AI harness 的核心 prompt 资产，再把稳定可复用的方法沉淀为适合个人长期使用的 AI harness 源资产、内部资产包与分发适配。

## 仓库定位

- 优先维护 `references/translations/` 中的外部 AI harness 中文翻译与同步元数据
- 持续跟踪 `references/repos/` 中的 upstream 仓库，并定期检查是否需要更新翻译
- 在 `src/` 中保留真正跨主题、跨 target 共享的核心源资产
- 在 `packages/` 中收纳已经具备独立主题边界、但仍属于当前仓库的资产包
- 通过 `targets/` 与 `packages/*/targets/` 为具体工具生成分发快照，避免直接把平台细节写死在共享源资产里

## 目录约定

- `src/README.md`
  - 说明 `src/` 共享源资产层的布局
- `packages/README.md`
  - 说明仓库内独立主题资产包的定位
- `targets/README.md`
  - 说明共享 target 适配层的约定
- `src/domains/<domain>/skills/<name>/SKILL.md`
  - 领域内的共享 skill 源资产
- `src/domains/<domain>/agents/<name>.md`
  - 领域内的共享独立 agent prompt
- `packages/<package>/_AGENTS.md`
  - 包级搭配上下文载体；只有在确实需要默认注入上下文时才存在
- `packages/<package>/skills/`、`packages/<package>/agents/`
  - 包内独立资产
- `packages/<package>/targets/<tool>/`
  - 包内自带的 tool-specific target 包
- `.learned/`、`.quality/`、`.research/`
  - 当前仓库默认记录落盘目录
- `references/`
  - 仓库内参考资料入口，包含说明文档、本地外部仓库与中文翻译目录

## 当前资产分类

### 1. 共享源资产

#### 工作流

- `src/domains/workflow/skills/nanospec/`
- `src/domains/workflow/skills/spec-driven/`
- `src/domains/workflow/skills/search-first/`
- `src/domains/workflow/skills/agent-orchestration/`

#### 资产治理

- `src/domains/asset-governance/skills/writing-skills/`

### 2. 仓库内独立主题资产包

- `packages/learning-capture/`
  - `learning-capture` skill 与配套 `_AGENTS.md` 搭配上下文
- `packages/quality-workflows/`
  - `quality-tdd`、`quality-verify`、`quality-review`、`quality-review-feedback` 与 `quality-code-reviewer`

### 3. 共享分发适配

#### Codex

- `targets/codex/skills/agent-orchestration/`
- `targets/codex/skills/nanospec/`
- `targets/codex/skills/search-first/`
- `targets/codex/skills/spec-driven/`
- `targets/codex/skills/writing-skills/`
- `targets/codex/.codex/config.toml`
- `targets/codex/.codex/agents/*.toml`

### 4. 包内 target 包

- `packages/learning-capture/targets/codex/`
- `packages/quality-workflows/targets/codex/`

## 当前调整

- `learning-capture` 与其配套 `_AGENTS.md` 已从领域层提到 `packages/learning-capture/`
- 四个 `quality-*` 与 `quality-code-reviewer` 已从 `src/domains/quality/` 提到 `packages/quality-workflows/`
- `quality-router` 已删除
- 根级 `targets/codex/` 只保留共享资产的 Codex 分发快照；包级 target 则在各自 `packages/*/targets/` 维护

## 外部参考仓库

需要参考其他仓库时，统一放到 `references/repos/` 下。

- 这里适合存放外部仓库的 clone 或软链接，例如 `oh-my-opencode`、`everything-claude-code`、`superpowers`
- `references/repos/` 只用于外部参考仓库，不承载当前仓库自己的真实资产
- 外部核心 prompt 的中文翻译与同步元数据放到 `references/translations/`
- 具体使用约定见 `references/README.md` 和 `references/translations/README.md`
