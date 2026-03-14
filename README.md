# my-ai-harness

这是一个用于沉淀 AI prompt 资产的工作区，重点资产类型是 `skills/` 和 `commands/`，并且所有可复用产物都应经过可验证的评估流程。

## 仓库约定

- 仓库级上下文位于 `AGENTS.md`
- 默认使用简体中文沉淀文档、skill、command 和 eval；代码、路径、协议关键字保留原文
- commit 使用简单格式：`<type>: <summary>`

## 目录约定

- `skills/`：可复用的长流程资产，每个 skill 放在 `skills/<name>/SKILL.md`
- `commands/`：更轻量的任务型 prompt 资产
- `evals/`：和资产配套的评估定义与回归用例
- `scripts/`：确定性的校验脚本与辅助工具

## 产出流程

1. 在 `skills/` 或 `commands/` 中新增或修改资产。
2. 为该资产补齐对应的评估定义，放到 `evals/` 下。
3. 优先补充可执行、可重复的代码评分器；只有必要时才退回规则评分器、模型评分器或人工审查。
4. 运行 `python3 scripts/validate_assets.py`，确认结构和最小约束通过。

## 当前首个资产

- `skills/eval-harness/`
  - 一个工具无关的评估驱动开发 skill，用来规范后续 skill 和 command 的产出方式。
