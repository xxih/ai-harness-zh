# my-ai-harness

这是一个用于沉淀 AI prompt 资产的工作区。仓库把“核心源资产”和“面向具体 AI 工具的分发适配”分开管理，并为可复用产物保留可验证的评估与脚本化校验能力。

## 仓库约定

- 仓库级上下文位于 `AGENTS.md`
- 默认使用简体中文沉淀文档、skill、command 和 eval；代码、路径、协议关键字保留原文
- commit 使用简单格式：`<type>: <summary>`

## 目录约定

- `src/skills/`：核心 skill 源资产，每个 skill 放在 `src/skills/<name>/SKILL.md`
- `src/agents/`：核心 agent 源资产，保存可复用的独立 agent prompt
- `src/commands/`：核心 command 源资产，保存更轻量的任务型 prompt
- `targets/`：不同 AI 工具的分发目录，保留和 `src/` 对齐的资产镜像，并叠加工具专属配置
- `evals/`：和资产配套的评估定义与回归用例
- `scripts/`：确定性的校验脚本与辅助工具
- `.learned/`：项目根目录下的学习积累记录目录
- `.quality/`：项目根目录下的质量记录目录
- `.research/`：项目根目录下的研究与编排记录目录
- `references/`：仓库内参考资料入口，包含可追踪说明文档与本地外部仓库目录
- `references/repos/`：本地参考仓库存放处，供 AI 工具读取，默认不纳入当前 git 版本管理

## 产出流程

1. 在 `src/skills/`、`src/agents/` 或 `src/commands/` 中新增或修改核心资产。
2. 需要回归保护时，再为该资产补齐对应评估，放到 `evals/` 下。
3. 优先补充可执行、可重复的代码评分器；只有必要时才退回规则评分器、模型评分器或人工审查。
4. 若某个 AI 工具需要专属包装，先保持 `targets/<tool>/` 与 `src/` 的资产分类一致。
5. 修改 `src/` 后，运行对应同步脚本，例如 `python3 scripts/sync_targets.py codex`。
6. 运行 `python3 scripts/validate_assets.py`，确认结构和最小约束通过。

默认落盘建议：

- 若任务已有自己的记录文件，优先回写到该文件
- 若没有既定位置，coding 研究默认写入 `.research/research-note.md`
- 若没有既定位置，coding 质量结果默认写入 `.quality/quality-check.md`
- 若没有既定位置，learning 相关记录默认写入 `.learned/`

## 当前资产

### 工程研发

- `src/skills/eval-harness/`
  - 用于先定义评估、再沉淀 prompt 资产
- `src/skills/agent-orchestration/`
  - 用于复杂 coding 任务中的主 agent 编排职责，包括角色分层、顺序阶段、单任务委派、并行独立性判定、反重复规则、结果回收与验证
- `src/skills/search-first/`
  - 用于在写新功能、修 bug、加依赖或抽象前，先搜索代码库、测试和外部方案，再决定是 `adopt`、`adapt` 还是 `build`
- `src/skills/learning-capture/`
  - 用于在一个会话或一个任务里手动触发学习积累，把 learnings、候选升级项和项目级规则候选落盘为结构化记录

### 工程研发 / 质量

- `src/skills/quality-router/`
  - 作为 `src/commands/` 的平替，支持手动触发 `/tdd`、`/verify`、`/review`、`/review-feedback`
- `src/skills/quality-tdd/`
  - 用于在功能开发、bugfix、重构前执行测试先行
- `src/skills/quality-verify/`
  - 用于在完成宣称前执行验证门禁，要求 fresh verification evidence
- `src/skills/quality-review/`
  - 用于在关键节点和合并前请求独立代码评审
- `src/skills/quality-review-feedback/`
  - 用于在收到评审意见后先核实、再实现或反驳

### 工程研发 / 质量 Agents

- `src/agents/quality-code-reviewer.md`
  - 用于以独立 subagent 方式做质量评审；这是当前仓库唯一保留的质量 agent，风格对齐 `superpowers`

### 内容生产

- `src/skills/xiaohongshu-carousel/`
  - 用于把已有内容快速转换成可直接发布的小红书图文多图
  - 主输入为 `slides.md`，通过 `scripts/build_xiaohongshu_carousel.py` 生成 HTML、manifest 和图片

## 分发适配

### Codex

- `targets/codex/skills/`
  - `src/skills/` 的 Codex 分发镜像
- `targets/codex/agents/`
  - `src/agents/` 的 Codex 分发镜像
- `targets/codex/commands/`
  - `src/commands/` 的 Codex 分发镜像
- `targets/codex/.codex/config.toml`
  - 定义 Codex 运行基线与 multi-agent 角色注册
- `targets/codex/.codex/agents/*.toml`
  - 定义 Codex reviewer / explorer / docs-researcher 等角色的工具专属行为
- `targets/codex/.codex/AGENTS.md`
  - 说明 Codex 如何消费 `src/` 下的核心资产，以及 `config.toml` 与角色配置的关系

## 当前缺口

- 目前的质量保证仍以结构校验、规则校验和人工 review 为主，仓库级 e2e 验证链路还没有建立
- 这个缺口已记录，但当前阶段先不补；后续若开始做实际分发脚本或多工具安装流，再补对应的 e2e 场景

## 外部参考仓库

需要参考其他仓库时，统一放到 `references/repos/` 下。

- 这里适合存放外部仓库的 clone 或软链接，例如 `oh-my-opencode`、`everything-claude-code`、`superpowers`
- 该目录位于当前工作区内，本地 AI 工具可以直接读取
- 该目录自带忽略规则，外部仓库内容不会进入当前仓库的 git 追踪
- 具体使用约定见 `references/README.md`
