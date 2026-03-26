# ai-harness-zh

`ai-harness-zh` 是一个以中文维护的 AI Harness 研究与沉淀工作区。

可以先用一句很粗暴但有效的话理解 `AI Harness`：它就是除了 LLM 外的一切。凡是把模型变成可稳定工作的 coding agent 所需的外壳和运行机制，例如 prompt、角色分工、skills、commands、hooks、rules、工具接入、上下文注入、记忆、计划与执行流程、验证机制、权限与运行约束，基本都属于 harness。

但并不是整套 harness 都由我们控制。对大多数 coding agent 来说，真正能被用户放进仓库、长期定制和分发的，通常是 agent 暴露出来的那些扩展口子，例如 `AGENTS.md`、`SKILL.md`、commands、hooks / plugins、rules、MCP 配置、target 包和配套文档。

这个仓库关心的正是这部分“可定制的 Harness”。这里会先在 `references/translations/` 中汇总、翻译和整理社区里成熟且有代表性的 harness 资产，再把适合长期维护的 workflow、prompt、skill、command、agent 和 target 提炼、重组并沉淀为自有 package，统一整理在 `packages/<package>/`。换句话说，这里既在看成熟 harness 已经做到哪里，也在补普通开发者日常裸用 Claude Code 一类工具时通常缺失的那一层。

## 成熟 harness 一般已经做到什么

如果只看当前仓库，很容易把 harness 理解成 prompt + skill 的整理工作。但对大多数日常开发者来说，平时其实常常只是裸用 Claude Code 这类工具；而成熟 harness 通常已经把更多能力做成系统，其中有不少正是普通使用者日常还没有系统化补齐的部分。

| 类别                       | 成熟 harness 常见做法                                                                                                                                                                                                                                  | 我们仓库当前已有能力                                                                                              | 普通开发者通常还没有系统化补齐的部分                                                                                   |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| 需求澄清与方案化           | `superpowers` 会把 `brainstorming`、`writing-plans` 串成明确前置流程；`brainstorming` 先收敛需求，`writing-plans` 再生成细任务计划。                                                                                                                   | `packages/nanospec/` 提供任务容器与中间文档规范，`packages/spec-driven/` 提供 spec-driven 工作流。                | 自动触发的前置流程、分段审批体验、从 spec 到 plan 的强约束串联仍主要靠 prompt 纪律，而不是平台级工作流。               |
| 执行编排与隔离             | `superpowers` 的 `subagent-driven-development`、`using-git-worktrees` 已经把子 agent 执行和隔离工作区做成常规流程；`oh-my-opencode` 进一步把 `delegate_task`、`background-agent` 做成运行时原语。                                                      | `packages/agent-orchestration/` 已沉淀多 agent 协作与委派编排方法；`packages/git-workflows/` 已覆盖 worktree 建立、分支收尾与清理流程。 | 结构化委派协议、后台任务状态机、会话续跑和真正的平台运行时还没有在仓库里落成。                                          |
| 质量门禁与验收             | `superpowers` 的 `test-driven-development`、`requesting-code-review`、`verification-before-completion` 把 TDD、评审、完成前验证串成闭环；`everything-claude-code` 还有 `/quality-gate`、`/security-scan`、`plankton-code-quality` 这类更强的质量入口。 | `packages/quality-workflows/` 已有 `quality-tdd`、`quality-verify`、`quality-review`、`quality-review-feedback`；`packages/github-workflows/` 开始承接远端 PR / comments / checks / merge 生命周期。 | 自动触发的质量 hooks、阻塞式 gate、安全扫描接入、写码后即时修复链路，还没有做成平台约束。                              |
| 搜索、代码理解与上下文治理 | `everything-claude-code` 有 `search-first`；`oh-my-opencode` 不只做 grep，还把 `lsp`、`ast-grep`、`directory-readme-injector`、`context-injector` 做进工具链和注入链路。                                                                               | `packages/search-first/` 已覆盖“先搜索再实现”的工作流，`packages/codex-base/` 提供基础 target 侧配置。            | 语义级代码工具接入、目录级上下文自动注入、压缩后的状态恢复、运行时上下文治理目前还没有完整实现。                       |
| 学习沉淀与上下文压缩       | `everything-claude-code` 已经把 `continuous-learning-v2`、`strategic-compact` 做成长期学习和上下文压缩能力。                                                                                                                                           | `packages/learning-evolution/` 已经覆盖学习信号识别、分流与沉淀；`packages/session-workflows/` 提供显式 session handoff；`packages/nanospec/` 提供任务过程落盘。 | 自动提取、置信度评分、压缩时机治理、压缩后恢复策略，还没有形成一套运行时闭环。                                         |
| 平台适配、规则与运行时治理 | `everything-claude-code` 同时维护 Codex、OpenCode、Cursor、Claude Code 侧的 hooks、rules、commands、MCP 和测试；`oh-my-opencode` 还有大量治理型 hooks，例如 `todo-continuation-enforcer`、`tool-output-truncator`、`edit-error-recovery`。             | `packages/codex-base/` 是当前仓库的 Codex 基线 target，其他 package 也已有 `targets/codex/` 分发副本。            | 跨平台 target、真正可运行的 hooks / plugins、安装与 doctor、回归测试、失败恢复和自愈治理，还基本停留在参考与拆解阶段。 |

## 这个仓库的价值

- 把外部成熟 harness 拆成可理解、可比较、可复用的能力层，而不是只收集零散 prompt
- 聚焦 coding agent 已经暴露出的定制入口，沉淀成可直接分发的 package
- 在中文语境下完成筛选、重写与结构化整理，让这些 Harness 资产更适合长期维护与团队复用

## 推荐先参考的 harness

如果你想理解“一个成熟的 AI coding harness 长什么样”，建议优先看下面三个对象：

| 参考对象                                  | 推荐原因                                                                                                                                                                                                                                                                         |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `references/repos/everything-claude-code` | 这是一个覆盖面很完整的全栈 harness 参考，包含 agents、skills、commands、hooks、rules、MCP 与多平台适配，还明确覆盖了 Codex、OpenCode、Cursor 等平台。像 `/harness-audit`、`/quality-gate`、`continuous-learning-v2`、`search-first` 都很适合拿来对照我们当前还缺哪些系统层能力。 |
| `references/repos/superpowers`            | 这是一个很清晰的 skill-first workflow 参考，把 `brainstorming`、`writing-plans`、`test-driven-development`、`requesting-code-review`、`subagent-driven-development` 串成一条强约束工程流程。适合理解怎样把方法论做成可触发、可复用的 skill 体系。                                |
| `references/repos/oh-my-opencode`         | 这类参考更值得从运行时内核角度阅读：`delegate_task`、`background-agent`、`directory-readme-injector`、`context-injector`、LSP / AST 工具链和治理型 hooks 都比较完整。适合理解 prompt 之外的编排、治理和工具层设计。                                                              |

如果只想先看一类：

- 想看完整系统，先看 `everything-claude-code`
- 想看最小工作流怎么落成 skill，先看 `superpowers`
- 想看运行时编排和治理设计，先看 `oh-my-opencode`

## 仓库里有什么

- `packages/`
  - 当前仓库自有资产的主入口
- `references/repos/`
  - 外部参考仓库；供 AI 读取，不纳入当前仓库 git 管理
- `references/translations/`
  - 外部 prompt 的中文翻译资料；属于参考材料，不作为分发 package 维护
- `scripts/`
  - 仓库级自动化脚本，例如 target 同步脚本
- `.learned/`、`.quality/`、`.research/`
  - 默认记录目录
- `.session/`
  - 本地 session handoff 文档目录；默认不纳入 git 管理
- `.nanospec/`、`nanospec/`
  - NanoSpec 任务容器与当前任务指针

## 当前 packages

### 工作流

- `packages/nanospec/`：NanoSpec 任务容器规范与中间文档流程
- `packages/spec-driven/`：spec-driven 工作流能力
- `packages/search-first/`：先搜索、再实现的工作流能力
- `packages/session-workflows/`：显式 session 收尾、handoff 与换窗口续跑
- `packages/local-development-workflows/`：本地开发默认主线与 local review 触发规则
- `packages/agent-orchestration/`：多 agent 协作与委派编排
- `packages/git-workflows/`：git worktree 建立、分支收尾与清理流程
- `packages/github-workflows/`：GitHub PR、review comments、checks、merge 与冲突处理流程

### 资产治理与沉淀

- `packages/writing-skills/`：skill 资产编写与重构能力
- `packages/learning-evolution/`：学习信号识别、资产演化与配套的默认注入上下文

### 内容生产

- `packages/content-writing/`：平台无关的内容写作内核

### 质量工作流

- `packages/quality-workflows/`：TDD、验证、评审与评审反馈等质量资产

### 平台适配

- `packages/codex-base/`：仓库维护的 Codex 基线 target 包

更多包内说明可直接查看 `packages/README.md` 和各 package 自己的 `README.md`。

## 一个 package 通常长什么样

常见结构如下：

- `README.md`
  - 说明包的边界、组成和维护方式
- `skills/`、`agents/`、`commands/`
  - 包的 source 资产
- `_AGENTS.md`
  - 包级搭配上下文载体；只有确实需要时才保留
  - 除协作型资产外，正文默认独立成立，单独写清用途、记录条件、写入位置、写入内容和默认动作
- `targets/<tool>/`
  - 面向具体工具的 target 包
- `references/`
  - 属于该包的参考资料、研究记录或附属文档

不是每个 package 都需要这些目录；只保留完成该主题所需的最小结构即可。

## Codex target 同步

面向 Codex 的 target 分发默认通过脚本同步：

```bash
python3 scripts/sync_codex_targets.py
python3 scripts/sync_codex_targets.py nanospec learning-evolution
```

脚本会把 package source 侧的 `skills/`、`agents/`、`commands/`、`_AGENTS.md` 镜像到对应的 `packages/<package>/targets/codex/`，但不会覆盖 target 侧手写的运行时文件，例如 `README.md`、`.codex/`。

## 外部参考资料

需要引入外部仓库时，统一放在 `references/repos/` 下；例如 `oh-my-opencode`、`everything-claude-code`、`superpowers`。

如果是外部 prompt 的中文翻译或整理材料，则放在 `references/translations/`，不要混进当前仓库自有 package。
