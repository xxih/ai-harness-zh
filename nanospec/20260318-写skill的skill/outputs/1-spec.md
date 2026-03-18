# 规格说明：写skill的skill

## 1. 背景

`.research/skill-authoring-landscape.md` 已经给出明确判断：

- Anthropic 官方 best practices 适合作为 skill 底层规范
- Superpowers `writing-skills` 适合作为 skill 迭代闭环
- Codex `skill-creator` 适合作为目录工程化与资源分层蓝图

本次任务不是重新做一轮调研，而是基于这个结论，真正落一个可复用的“创建 skill”资产。

## 2. 任务目标

本次任务需要产出并确认一个可独立分发的 skill，指导后续“创建新 skill、重写已有 skill、把稳定 workflow 升级为 skill 资产”这类工作。

## 3. 交付范围

### 3.1 独立 skill 正文

需要存在一个稳定的 `writing-skills`，指导如何判断“该不该写成 skill”、如何写 description、如何做 references 拆分，以及如何通过 fail-first 闭环验证 skill 质量。

成功标志：

- skill 正文不再把作者当前仓库的领域分层、任务容器、记录目录或 target 目录写成默认前提
- 正文明确覆盖适用场景、不适用场景、产物、核心原则、工作流与纪律约束
- skill 明确体现“三源合成”思路：Anthropic 规范、Superpowers 闭环、Codex 工程化
- 详细检查项与验证循环拆到 `references/`，而不是把正文写成大而全说明文

验收证据：

- `src/domains/asset-governance/skills/writing-skills/SKILL.md`
- `src/domains/asset-governance/skills/writing-skills/references/authoring-checklist.md`
- `src/domains/asset-governance/skills/writing-skills/references/validation-loop.md`

### 3.2 当前仓库中的实现与分发副本

当前仓库可以保留 source 存放位置和 target 分发副本，但它们只是当前仓库的实现与打包方式，不应反向污染 skill 正文。

成功标志：

- source 版本与分发副本内容一致
- skill 被放在什么目录，不改变它“默认独立”的正文口径

验收证据：

- `src/domains/asset-governance/skills/writing-skills/SKILL.md`
- `src/domains/asset-governance/skills/writing-skills/references/authoring-checklist.md`
- `src/domains/asset-governance/skills/writing-skills/references/validation-loop.md`
- `targets/codex/skills/writing-skills/SKILL.md`
- `targets/codex/skills/writing-skills/references/authoring-checklist.md`
- `targets/codex/skills/writing-skills/references/validation-loop.md`

### 3.3 NanoSpec 任务记录

本次任务使用 NanoSpec 只是为了当前会话的工作记录与对齐，不属于最终 skill 对外分发内容。

成功标志：

- 当前任务中的对齐决策已记录，且不再与 skill 正文冲突

验收证据：

- `nanospec/20260318-写skill的skill/alignment.md`
- `nanospec/20260318-写skill的skill/outputs/1-spec.md`
- `nanospec/20260318-写skill的skill/outputs/2-plan.md`
- `nanospec/20260318-写skill的skill/outputs/3-tasks.md`

## 4. 非目标

- 不在本次任务中额外设计新的 skill 安装器、metadata 生成器或仓库级自动校验脚本
- 不把 `.research/skill-authoring-landscape.md` 原样复制进正式 skill
- 不把当前仓库内部结构写进通用 skill 正文
- 不把平台特定运行时术语写进通用 skill 正文

## 5. 约束

- 默认使用简体中文
- 正式 skill 目录保持精简，只保留完成任务必需的文件
- 若发现 scope 变化或交付口径变化，需要先执行 align 再继续
