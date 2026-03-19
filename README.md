# ai-harness-zh

`ai-harness-zh` 是一个以中文维护的 AI harness 工作区。现在它主要扮演**索引仓 + 共享源资产仓**：能独立运行、独立安装、独立演进的能力，优先直接拆成单独 repo，当前仓库只保留索引、研究、翻译和仍值得共享的工具无关资产。

## 当前仓库角色

1. 跟踪 `references/repos/` 中的外部与本地拆出 repo
2. 维护 `references/translations/` 中的中文翻译与同步元数据
3. 在 `src/` 中保留仍然跨 target 共享的核心源资产
4. 在 `targets/` 中保留仍然需要的薄分发快照
5. 通过 `.research/`、`.quality/`、`.learned/` 保留研究、质量与学习记录

## 当前分类

### 1. 参考 repo / 已拆独立 repo

- `references/repos/oh-my-opencode`
- `references/repos/everything-claude-code`
- `references/repos/superpowers`
- `references/repos/agency-agents`
- `references/repos/claudeception`
- `references/repos/learning-capture`
  - 从当前仓库拆出的单主题 repo：手工学习沉淀能力 + 配套 AGENTS 上下文
- `references/repos/quality-workflows`
  - 从当前仓库拆出的单主题 repo：四个 quality skill + 独立 reviewer agent

### 2. 当前仍保留的共享源资产

#### 工作流

- `src/domains/workflow/skills/nanospec/`
- `src/domains/workflow/skills/spec-driven/`
- `src/domains/workflow/skills/search-first/`
- `src/domains/workflow/skills/agent-orchestration/`

#### 资产治理

- `src/domains/asset-governance/skills/writing-skills/`

### 3. 当前仍保留的 target 包

#### Codex

- `targets/codex/skills/agent-orchestration/`
- `targets/codex/skills/nanospec/`
- `targets/codex/skills/search-first/`
- `targets/codex/skills/spec-driven/`
- `targets/codex/skills/writing-skills/`
- `targets/codex/.codex/config.toml`
- `targets/codex/.codex/agents/*.toml`

`learning-capture` 与 `quality-workflows` 的 Codex target 包已随各自独立 repo 拆走，不再继续挂在当前总仓。

## 拆分原则

以下情况，优先拆成单主题 repo：

- 已经能被单独安装、单独运行、单独分发
- 强绑定某个工具或平台运行时
- 需要自己的 hooks、settings、scripts、README、验证链路和发布节奏
- 用户理解它时，更像一个独立产品 / 包，而不是总仓的一部分

以下情况，继续留在当前仓库：

- 仍然是工具无关、跨 target 共享的核心 prompt 资产
- 仍然处于研究、翻译、吸收、抽象阶段
- 只是某个独立 repo 的索引、研究记录或最小映射说明

## 目录入口

- `references/README.md`
  - 参考 repo 与翻译资产的约定
- `src/README.md`
  - 共享源资产的边界与毕业规则
- `targets/README.md`
  - target 包的边界与升格规则
- `targets/codex/README.md`
  - 当前总仓保留的 Codex target 包说明
- `.research/standalone-repo-split.md`
  - 本次拆仓记录
