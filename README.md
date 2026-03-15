# my-ai-harness

这是一个用于沉淀 AI prompt 资产的工作区，重点资产类型是 `skills/` 和 `commands/`，并且所有可复用产物都应经过可验证的评估流程。

## 仓库约定

- 仓库级上下文位于 `AGENTS.md`
- 默认使用简体中文沉淀文档、skill、command 和 eval；代码、路径、协议关键字保留原文
- commit 使用简单格式：`<type>: <summary>`

## 目录约定

- `skills/`：可复用的长流程资产，每个 skill 放在 `skills/<name>/SKILL.md`
- `agents/`：可复用的独立 agent prompt，适合配合 subagent / multiagent 工作流
- `commands/`：更轻量的任务型 prompt 资产
- `evals/`：和资产配套的评估定义与回归用例
- `scripts/`：确定性的校验脚本与辅助工具
- `references/`：仓库内参考资料入口，包含可追踪说明文档与本地外部仓库目录
- `references/repos/`：本地参考仓库存放处，供 AI 工具读取，默认不纳入当前 git 版本管理

## 产出流程

1. 在 `skills/` 或 `commands/` 中新增或修改资产。
2. 为该资产补齐对应的评估定义，放到 `evals/` 下。
3. 优先补充可执行、可重复的代码评分器；只有必要时才退回规则评分器、模型评分器或人工审查。
4. 运行 `python3 scripts/validate_assets.py`，确认结构和最小约束通过。

默认落盘建议：

- 若任务已有自己的记录文件，优先回写到该文件
- 若没有既定位置，coding 研究默认写入 `output/research/research-note.md`
- 若没有既定位置，coding 质量结果默认写入 `output/quality/quality-check.md`

## 当前资产

### 工程研发

- `skills/eval-harness/`
  - 用于先定义评估、再沉淀 prompt 资产
- `skills/search-first/`
  - 用于在写新功能、修 bug、加依赖或抽象前，先搜索代码库、测试和外部方案，再决定是 `adopt`、`adapt` 还是 `build`

### 工程研发 / 质量

- `skills/quality-router/`
  - 作为 `commands/` 的平替，支持手动触发 `/tdd`、`/verify`、`/review`、`/review-feedback`
- `skills/quality-tdd/`
  - 用于在功能开发、bugfix、重构前执行测试先行
- `skills/quality-verify/`
  - 用于在完成宣称前执行验证门禁，要求 fresh verification evidence
- `skills/quality-review/`
  - 用于在关键节点和合并前请求独立代码评审
- `skills/quality-review-feedback/`
  - 用于在收到评审意见后先核实、再实现或反驳

### 工程研发 / 质量 Agents

- `agents/quality-code-reviewer.md`
  - 用于以独立 subagent 方式做质量评审；这是当前仓库唯一保留的质量 agent，风格对齐 `superpowers`

### 内容生产

- `skills/xiaohongshu-carousel/`
  - 用于把已有内容快速转换成可直接发布的小红书图文多图
  - 主输入为 `slides.md`，通过 `scripts/build_xiaohongshu_carousel.py` 生成 HTML、manifest 和图片

## 外部参考仓库

需要参考其他仓库时，统一放到 `references/repos/` 下。

- 这里适合存放外部仓库的 clone 或软链接，例如 `oh-my-opencode`、`everything-claude-code`、`superpowers`
- 该目录位于当前工作区内，本地 AI 工具可以直接读取
- 该目录自带忽略规则，外部仓库内容不会进入当前仓库的 git 追踪
- 具体使用约定见 `references/README.md`
