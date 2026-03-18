# 方案：写skill的skill

## 总体策略

本次直接采用“研究结论压缩落地”的策略，而不是从零重新发明一套 skill authoring 方法。

具体做法：

1. 用 Anthropic best practices 约束 discoverability、frontmatter 和 progressive disclosure。
2. 用 Superpowers `writing-skills` 提供 fail-first、pressure scenario、loophole plugging 的迭代闭环。
3. 用 Codex `skill-creator` 提供目录卫生、`references/` 拆分与长期维护约束。
4. 明确把“当前仓库怎么存”和“skill 默认怎么写”分开：仓库存放路径只是实现细节，不进入 skill 默认正文。

这样能避免两个常见问题：

- 只学格式，不学迭代闭环，最后 skill 很整齐但没验证过
- 只学 fail-first，不做目录工程化，最后 skill 越写越散、越来越难维护

## 实施方式

### 阶段 1：先对齐口径，再修正文案

先记录这次偏差：上一版把当前仓库里的 `src/domains/...`、`targets/...`、`nanospec` 等内部结构误写成 skill 的默认前提。对齐后，所有受影响产物都要同步改口径。

### 阶段 2：核对 source skill

读取现有 `src/domains/asset-governance/skills/writing-skills/`，确认它是否满足以下最小要求：

- `description` 只写触发条件，不偷跑 workflow
- 正文保留目标、适用边界、主流程和纪律约束
- 重型内容拆进 `references/`
- 方法论明确吸收三份来源各自的强项
- 默认写成独立 skill 包，不把当前仓库内部路径写成前提

若缺项存在，则直接在 source 资产中补齐；若已满足，则保留 source 为真相来源。

### 阶段 3：同步 target

由于仓库维护 `targets/codex/` 平铺快照，因此需要同步：

- `targets/codex/skills/writing-skills/SKILL.md`
- `targets/codex/skills/writing-skills/references/*`

### 阶段 4：做最小校验

不额外引入新脚本，直接做最小确认：

- 目标文件存在
- source 与 target 内容一致
- skill 正文中不再出现把当前仓库内部结构当默认前提的表述

## 风险与收口

### 风险 1：把当前仓库内部结构误写成 skill 的一部分

收口：

- skill 默认只描述独立可分发内容
- 当前仓库的 source / target / 任务记录只留在实现层和任务层

### 风险 2：把研究文档直接塞进 skill

收口：

- 正式 skill 只保留稳定规则
- 研究证据继续留在研究材料中

### 风险 3：把内部设计理由写进 description

收口：

- description 只写何时使用
- 设计理由留在正文和 references 中

### 风险 4：source 与 target 漂移

收口：

- 本轮以 source 为真相来源
- 手动同步 `targets/codex/`，并用 diff 做最小确认
