# ai-harness-zh

`ai-harness-zh` 是一个以中文维护的 AI harness 工作区。

这里首先在 `references/translations/` 中汇总、翻译和整理社区里专业、热门且具有代表性的核心 prompt 资产，作为持续研究和吸收的参考基础。

在此基础上，仓库会把适合长期维护的 workflow、prompt、skill、command、agent 和 target 进一步提炼、重组并沉淀为自有资产，统一整理在 `packages/<package>/`，形成可复用、可分发、可持续演进的 package。

## 这个仓库的价值

- 汇总并翻译社区中专业、热门且被反复验证的核心 prompt 资产，降低获取门槛
- 把外部实践进一步提炼成可直接使用的自有 package，而不是停留在参考资料层
- 在中文语境下完成筛选、重写与结构化整理，让资产更适合长期维护与团队复用

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
- `.nanospec/`、`nanospec/`
  - NanoSpec 任务容器与当前任务指针

## 当前 packages

### 工作流

- `packages/nanospec/`：NanoSpec 任务容器规范与中间文档流程
- `packages/spec-driven/`：spec-driven 工作流能力
- `packages/search-first/`：先搜索、再实现的工作流能力
- `packages/agent-orchestration/`：多 agent 协作与委派编排

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
