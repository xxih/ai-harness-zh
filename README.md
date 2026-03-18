# my-ai-harness

这是一个用于沉淀 AI prompt 资产的工作区。仓库把“核心源资产”和“面向具体 AI 工具的分发适配”分开管理，并为可复用产物保留可验证的评估与脚本化校验能力。

## 仓库约定

- 仓库级上下文位于 `AGENTS.md`
- `src/` 内的源资产按领域组织，领域公共规则优先写在各自的 `AGENTS.md`
- 默认使用简体中文沉淀文档、skill、command 和 eval；代码、路径、协议关键字保留原文
- commit 使用简单格式：`<type>: <summary>`

## 目录约定

- `src/AGENTS.md`
  - 说明 `src/` 源资产层的总布局
- `src/domains/<domain>/AGENTS.md`
  - 定义该领域的公共规则、边界和命名口径
- `src/domains/<domain>/skills/<name>/SKILL.md`
  - 领域内的 skill 源资产
- `src/domains/<domain>/agents/<name>.md`
  - 领域内的独立 agent prompt
- `src/domains/<domain>/commands/`
  - 领域内的轻量任务入口；没有资产时保留空目录即可
- `targets/`
  - 不同 AI 工具的分发目录；可按运行时需要把领域资产做平铺、映射或额外包装
- `evals/`
  - 和资产配套的评估定义与回归用例
- `scripts/`
  - 确定性的校验脚本与同步脚本
- `.learned/`、`.quality/`、`.research/`
  - 默认记录落盘目录
- `references/`
  - 仓库内参考资料入口，包含可追踪说明文档与本地外部仓库目录

## 产出流程

1. 在 `src/domains/<domain>/` 下新增或修改核心资产。
2. 需要回归保护时，再为该资产补齐对应评估，放到 `evals/` 下。
3. 优先补充可执行、可重复的代码评分器；只有必要时才退回规则评分器、模型评分器或人工审查。
4. 若某个 AI 工具需要专属包装，由 `targets/<tool>/` 从领域源资产生成运行时分发目录。
5. 修改 `src/` 后，运行对应同步脚本，例如 `python3 scripts/sync_targets.py codex`。
6. 运行 `python3 scripts/validate_assets.py`，确认结构和最小约束通过。

默认落盘建议：

- 若任务已有自己的记录文件，优先回写到该文件
- 若没有既定位置，coding 研究默认写入 `.research/research-note.md`
- 若没有既定位置，coding 质量结果默认写入 `.quality/quality-check.md`
- 若没有既定位置，learning 相关记录默认写入 `.learned/`

## 当前资产

### 工作流

- `src/domains/workflow/AGENTS.md`
  - 该领域的公共规则，覆盖研究、拆解和执行前准备
- `src/domains/workflow/skills/search-first/`
  - 用于在写新功能、修 bug、加依赖或抽象前，先搜索代码库、测试和外部方案，再决定是 `adopt`、`adapt` 还是 `build`
- `src/domains/workflow/skills/agent-orchestration/`
  - 用于复杂 coding 任务中的主 agent 编排职责，包括角色分层、顺序阶段、单任务委派、并行独立性判定、反重复规则、结果回收与验证

### 质量

- `src/domains/quality/AGENTS.md`
  - 该领域的公共规则，覆盖质量门禁、分级结论和 reviewer 角色
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

- `src/domains/asset-governance/AGENTS.md`
  - 该领域的公共规则，覆盖资产评估、回归保护和经验沉淀
- `src/domains/asset-governance/skills/eval-harness/`
  - 用于先定义评估、再沉淀 prompt 资产
- `src/domains/asset-governance/skills/learning-capture/`
  - 用于在一个会话或一个任务里手动触发学习积累，把 learnings、候选升级项和项目级规则候选落盘为结构化记录

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
- `targets/codex/.codex/AGENTS.md`
  - 说明 Codex 如何把平铺分发目录映射回 `src/domains/` 下的源资产

## 当前缺口

- 目前的质量保证仍以结构校验、规则校验和人工 review 为主，仓库级 e2e 验证链路还没有建立
- 这个缺口已记录，但当前阶段先不补；后续若开始做实际分发脚本或多工具安装流，再补对应的 e2e 场景

## 外部参考仓库

需要参考其他仓库时，统一放到 `references/repos/` 下。

- 这里适合存放外部仓库的 clone 或软链接，例如 `oh-my-opencode`、`everything-claude-code`、`superpowers`
- 该目录位于当前工作区内，本地 AI 工具可以直接读取
- 该目录自带忽略规则，外部仓库内容不会进入当前仓库的 git 追踪
- 具体使用约定见 `references/README.md`
