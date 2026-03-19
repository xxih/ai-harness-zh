# ai-harness-zh

`ai-harness-zh` 是一个以中文维护的 AI harness 工作区。当前仓库不再追求把所有能力都塞进一个大仓，而是按“索引仓 + 共享源资产 + target 包 + 外部单主题 repo”来组织：**能独立运行、独立安装、独立演进的东西，优先直接拆成单独 repo。**

## 仓库角色

当前仓库主要承担四类职责：

1. **外部参考与中文翻译索引**
   - 跟踪 `references/repos/` 中的 upstream 仓库
   - 维护 `references/translations/` 中的中文翻译与同步元数据
2. **共享源资产工作区**
   - 在 `src/` 中沉淀工具无关、跨 target 可复用的 workflow / quality / asset-governance 资产
3. **薄 target 包与分发快照**
   - 在 `targets/` 中保留面向具体工具的运行时平铺、副本或最小适配层
4. **研究、质量与学习记录**
   - 通过 `.research/`、`.quality/`、`.learned/` 保留任务级证据与过程沉淀

## 分类模型

### 1. 参考 repo 与翻译资产

- `references/repos/`
  - 外部参考仓库入口；适合放 upstream clone、软链接，以及已经独立存在的单主题 repo
- `references/translations/`
  - 外部核心 prompt / skill / command 的中文翻译与同步记录
- 当前已纳入参考的仓库包括 `oh-my-opencode`、`everything-claude-code`、`superpowers`、`agency-agents`、`claudeception`
- 当前已汇总进仓库的现成中文资产包括 `superpowers`、`everything-claude-code`、`oh-my-opencode`

### 2. 共享源资产

- `src/domains/workflow/`
  - 承载研究、spec、编排、任务容器等共享工作流资产
- `src/domains/quality/`
  - 承载 TDD、verify、review、review-feedback 等质量门禁资产
- `src/domains/asset-governance/`
  - 承载 learning-capture、writing-skills 等资产治理能力
- 这一层只保留**跨 target 复用的核心真相**，不直接承载某个平台独有的 hooks、settings、installer、发布脚本

### 3. target 包

- `targets/`
  - 面向具体工具的分发快照与最小适配层
- 当前已落地 target：`targets/codex/`
- target 包可以是工具绑定的，但默认应保持**薄、可映射、可从 `src/` 回溯**
- 如果某个 target 长成一个完整产品，应直接升格为独立 repo，而不是继续在当前仓库无限膨胀

### 4. 记录与任务容器

- `.research/`
  - 研究记录与对比分析
- `.quality/`
  - 质量验证记录
- `.learned/`
  - 规则候选与可复用经验
- `nanospec/`
  - 任务级 spec / alignment 工作目录

## 拆分原则

以下情况，优先**拆成单主题 repo**：

- 已经能被单独安装、单独运行、单独分发
- 强绑定某个工具或平台运行时，例如 Claude hooks、Codex 专属运行包、工具级 installer
- 需要自己的发布节奏、README、验证链路、示例和 issue 边界
- 用户理解它时，更像“一个独立产品 / 包”，而不是“当前仓库的一部分”

以下情况，继续留在当前仓库：

- 仍然是工具无关、跨 target 共享的核心 prompt 资产
- 仍然处于对比、翻译、吸收、抽象阶段
- 只是某个独立 repo / target 包的索引、来源映射或最小分发快照
- 需要和其他共享资产一起统一治理，而不是单独发版

拆分后的当前仓库职责：

- 保留索引说明
- 保留翻译或研究记录
- 保留真正工具无关的核心抽象
- 不再把独立 repo 的完整运行时实现长期塞回本仓

## 当前分类视图

### 外部参考层

- `references/repos/oh-my-opencode`
- `references/repos/everything-claude-code`
- `references/repos/superpowers`
- `references/repos/agency-agents`
- `references/repos/claudeception`

这些仓库本身就是“单主题 repo / 独立 harness repo”的参考样本。

### 当前共享源资产

#### 工作流

- `src/domains/workflow/skills/nanospec/`
- `src/domains/workflow/skills/spec-driven/`
- `src/domains/workflow/skills/search-first/`
- `src/domains/workflow/skills/agent-orchestration/`

#### 质量

- `src/domains/quality/skills/quality-router/`
- `src/domains/quality/skills/quality-tdd/`
- `src/domains/quality/skills/quality-verify/`
- `src/domains/quality/skills/quality-review/`
- `src/domains/quality/skills/quality-review-feedback/`
- `src/domains/quality/agents/quality-code-reviewer.md`

#### 资产治理

- `src/domains/asset-governance/skills/learning-capture/`
- `src/domains/asset-governance/skills/writing-skills/`

### 当前 target 包

#### Codex

- `targets/codex/skills/`
- `targets/codex/agents/`
- `targets/codex/commands/`
- `targets/codex/.codex/config.toml`
- `targets/codex/.codex/agents/*.toml`

当前把它视为 **Codex target 包快照**。如果后续它开始承载安装脚本、独立文档、验证矩阵、target 专属 release 生命周期，应优先拆成独立 repo。

## 工作方式

1. 先在 `references/repos/` 观察外部 harness / target repo 的结构与更新
2. 需要翻译时，把中文版本沉淀到 `references/translations/<repo>/`
3. 确认某类能力是跨 target 共享的，再回收进 `src/domains/<domain>/`
4. 若只是某个工具的薄运行时适配，先放进 `targets/<tool>/`
5. 若某个能力已经能独立运行或独立分发，直接拆成单主题 repo；当前仓库只保留索引、研究、翻译或共享抽象
6. 涉及结构性变化时，同时更新对应 README 与约定文档

## 目录速览

- `README.md`
  - 仓库级定位、分类模型与拆分原则
- `references/README.md`
  - 外部参考 repo 与翻译资产的使用约定
- `src/README.md`
  - 共享源资产层的布局与“毕业”规则
- `targets/README.md`
  - target 包层的定位与升格规则
- `targets/codex/README.md`
  - 当前 Codex target 包的组成与运行时映射

## 当前缺口

- 目前仓库仍以文档和 prompt 资产治理为主，真正的“独立 repo 拆分流”和自动化分发还没有工具化
- `targets/codex/` 仍是手工维护的 target 快照，尚未形成独立发布链路
- 仓库级 e2e 验证还没建立；后续若开始拆 target repo 或加入安装流，再补对应验证场景
