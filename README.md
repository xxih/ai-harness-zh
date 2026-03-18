# ai-harness-zh

`ai-harness-zh` 是一个以中文维护的 AI harness 工作区。仓库先汇总、翻译并持续同步外部主流 AI harness 的核心 prompt 资产，再把稳定可复用的方法沉淀为适合个人长期使用的 AI harness 源资产与分发适配。

## 仓库定位

- 优先维护 `references/translations/` 中的外部 AI harness 中文翻译与同步元数据
- 持续跟踪 `references/repos/` 中的 upstream 仓库，并定期检查是否需要更新翻译
- 在 `src/` 中提炼真正值得长期复用的个人工作流、质量门禁与资产治理能力
- 通过 `targets/` 为具体工具生成分发快照，避免直接把平台细节写死在源资产里

## 当前重点

### 1. 汇总各大 AI harness 的中文翻译

- `references/repos/` 用于放外部参考仓库，本地 AI 工具可直接读取
- `references/translations/` 用于放已版本化的中文翻译资产与同步记录
- 当前已纳入参考的仓库包括 `oh-my-opencode`、`everything-claude-code`、`superpowers`、`agency-agents`
- 当前已汇总进仓库的现成中文资产包括 `superpowers`、`everything-claude-code`、`oh-my-opencode`
- 翻译资产优先覆盖“最核心、最常被直接读取、最适合长期复用”的 prompt/skill

### 2. 定期同步 upstream 更新

- 每次同步前先更新 `references/repos/<repo>/` 到准备对照的 upstream 版本
- 同步后手动更新 `references/translations/<repo>/manifest.json`
- `manifest.json` 会记录 upstream commit 与当前翻译覆盖范围内的源文件哈希
- 当前阶段以人工审阅和最小必要记录为主，不再额外维护仓库级校验脚本

### 3. 基于翻译沉淀个人 AI harness

- `src/` 保存工具无关的核心源资产
- `targets/` 保存面向具体工具的分发快照与适配层
- `.research/`、`.quality/`、`.learned/` 分别承接研究、质量与学习记录
- 先保持根目录整洁，后续再决定 skills 的迭代机制

## 目录约定

- `src/README.md`
  - 说明 `src/` 源资产层的总布局
- `src/domains/<domain>/_AGENTS.md`
  - 领域根目录下的载体文件；存放某些 `skills/`、`commands/` 需要默认注入的搭配上下文
- `src/domains/<domain>/skills/<name>/SKILL.md`
  - 领域内的 skill 源资产
- `src/domains/<domain>/agents/<name>.md`
  - 领域内的独立 agent prompt
- `src/domains/<domain>/commands/`
  - 领域内的轻量任务入口；没有资产时保留空目录即可
- `targets/`
  - 不同 AI 工具的分发目录；可按运行时需要把领域资产做平铺、映射或额外包装
- `.learned/`、`.quality/`、`.research/`
  - 默认记录落盘目录
- `references/`
  - 仓库内参考资料入口，包含说明文档、本地外部仓库与中文翻译目录

## 产出流程

1. 先在 `references/repos/` 观察外部 AI harness 的结构与更新。
2. 需要翻译时，把中文版本沉淀到 `references/translations/<repo>/`。
3. 确认某类能力值得长期复用后，再回收进 `src/domains/<domain>/`。
4. 若某个 AI 工具需要专属包装，由 `targets/<tool>/` 维护对应运行时分发目录。
5. 修改 `src/` 后，按需手动同步对应 `targets/` 分发副本；若某个目标工具需要承载 `AGENTS.md` 类内容，当前阶段在 `targets/` 中保存为 `_AGENTS.md`。
6. 涉及结构性变化时，同时更新相关说明文档。

默认落盘建议：

- 若任务已有自己的记录文件，优先回写到该文件
- 若没有既定位置，coding 研究默认写入 `.research/research-note.md`
- 若没有既定位置，coding 质量结果默认写入 `.quality/quality-check.md`
- 若没有既定位置，learning 相关记录默认写入 `.learned/`

## 当前资产

### 工作流

- `src/domains/workflow/skills/nanospec/`
  - 用于统一任务中间文档目录规范，并以 `alignment.md` 作为跨阶段纠偏入口
- `src/domains/workflow/skills/spec-driven/`
  - 用于给任务建立统一的 spec-driven 工作目录：保留共享工作面和 `alignment.md` 纠偏机制，不内置阶段路由
- `src/domains/workflow/skills/search-first/`
  - 用于在写新功能、修 bug、加依赖或抽象前，先搜索代码库、测试和外部方案，再决定是 `adopt`、`adapt` 还是 `build`
- `src/domains/workflow/skills/agent-orchestration/`
  - 用于复杂 coding 任务中的主 agent 编排职责，包括角色分层、顺序阶段、单任务委派、并行独立性判定、反重复规则、结果回收与验证

### 质量

- `src/domains/quality/skills/quality-router/`
  - 作为同领域 `commands/` 的平替，支持手动触发 `/tdd`、`/verify`、`/review`、`/review-feedback`
- `src/domains/quality/skills/quality-tdd/`
  - 用于在功能开发、bugfix、重构前执行测试先行
- `src/domains/quality/skills/quality-verify/`
  - 用于在完成宣称前执行验证门禁，要求 fresh verification evidence
- `src/domains/quality/skills/quality-review/`
  - 用于在关键节点和合并前请求独立代码评审
- `src/domains/quality/skills/quality-review-feedback/`
  - 用于在收到评审意见后先核实、再实现或反驳
- `src/domains/quality/agents/quality-code-reviewer.md`
  - 用于以独立 subagent 方式做质量评审；这是当前仓库唯一保留的质量 agent

### 资产治理

- `src/domains/asset-governance/skills/learning-capture/`
  - 用于在一个会话或一个任务里手动触发学习积累，把 learnings、候选升级项和项目级规则候选落盘为结构化记录
- `src/domains/asset-governance/skills/writing-skills/`
  - 用于创建、重写或更新仓库内 skill 资产，先做调研，再收敛触发词、frontmatter、结构、资源拆分与验证方式

## 分发适配

### Codex

- `targets/codex/skills/`
  - 从 `src/domains/*/skills/` 收集并平铺出的 Codex 运行时 skills
- `targets/codex/agents/`
  - 从 `src/domains/*/agents/` 收集并平铺出的 Codex 运行时 agents
- `targets/codex/commands/`
  - 从 `src/domains/*/commands/` 收集并平铺出的 Codex 运行时 commands
- `targets/codex/.codex/config.toml`
  - 定义 Codex 运行基线与 multi-agent 角色注册
- `targets/codex/.codex/agents/*.toml`
  - 定义 Codex reviewer / explorer / docs-researcher 等角色的工具专属行为

## 当前缺口

- 目前的质量保证仍以结构校验、规则校验和人工 review 为主，仓库级 e2e 验证链路还没有建立
- 这个缺口已记录，但当前阶段先不补；后续若开始做实际分发脚本或多工具安装流，再补对应的 e2e 场景

## 外部参考仓库

需要参考其他仓库时，统一放到 `references/repos/` 下。

- 这里适合存放外部仓库的 clone 或软链接，例如 `oh-my-opencode`、`everything-claude-code`、`superpowers`
- 该目录位于当前工作区内，本地 AI 工具可以直接读取
- 该目录自带忽略规则，外部仓库内容不会进入当前仓库的 git 追踪
- 外部核心 prompt 的中文翻译与同步元数据放到 `references/translations/`
- 具体使用约定见 `references/README.md` 和 `references/translations/README.md`
