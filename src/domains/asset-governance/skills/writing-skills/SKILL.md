---
name: writing-skills
description: 当你要创建新 skill、重写已有 skill，或把一段稳定 workflow 升级为长期可复用资产时使用；适用于需要收敛触发词、边界、资源拆分与验证闭环的场景。
---

# Writing Skills

这个 skill 解决的不是“把一次经验写成说明文”，而是把可复用 prompt 工作流做成可发现、可验证、可维护的 skill 资产。默认组合三类经验：用 Anthropic 的规范守住 discoverability 与 progressive disclosure，用 Superpowers 的 fail-first 闭环保证 skill 真能改变 agent 行为，用 Codex `skill-creator` 的目录约束保持资产长期可维护。

## 何时使用

- 你准备创建一个新的仓库内 skill
- 已有 skill 命中率差、正文过长、边界模糊，准备重写
- 你手头有一段稳定 workflow，准备升级成正式 skill 资产
- 你想验证某个 skill 是否真的改变了 agent 行为，而不是只改了文案

不适用：

- 只是项目私有规则，应该优先写进对应领域 `_AGENTS.md`；如果只是结构说明，再写 `README.md` 或任务文档
- 只是一次性经验，还没形成跨任务复用模式
- 可以靠脚本、lint、schema 或 hook 强制的机械规则
- 只是平台运行时安装、打包或 metadata 适配，应优先改 `targets/`

## 产物

每次使用本 skill，默认产出以下最小集合：

1. skill 源资产
   - `src/domains/<domain>/skills/<name>/SKILL.md`
   - 仅在需要时再补 `references/`、`scripts/`、`assets/`
2. 验证记录
   - 若当前任务已有 `nanospec` 容器，优先回写 `outputs/*` 与必要的 `alignment.md`
   - 若没有任务容器，研究结论写入 `.research/`，验证摘要写入 `.quality/`
3. 分发副本
   - 仓库已有 target 快照时，同步对应 `targets/<tool>/skills/<name>/`

## 核心原则

### 1. 先判断它是不是一个 skill

先区分这件事应该沉淀到哪里：

- 跨任务、靠判断执行、需要被模型发现的能力 -> skill
- 仓库长期公共规则 -> `_AGENTS.md`
- 目录结构说明、人工导览 -> `README.md`
- 轻量触发入口或固定命令壳 -> `commands/`
- 平台运行时 wiring、metadata、hooks、安装流 -> `targets/`
- 还没稳定的经验候选 -> `.learned/`

边界判断和检查清单见 `references/authoring-checklist.md`。

### 2. description 只写触发条件

`description` 的作用是帮助模型判断“现在要不要读这个 skill”，不是偷跑 skill 的 workflow。只写触发条件、症状、上下文，不写步骤数量、子技能链路或执行摘要。

### 3. 先看没有 skill 时会怎么失败

写 skill 前先构造一个 pressure scenario，观察没有 skill 时 agent 会怎么误判、漏步或合理化。没有 baseline，就不知道 skill 到底在修什么。验证循环和模板见 `references/validation-loop.md`。

### 4. 主文档保持短，重资料按需下沉

`SKILL.md` 只保留目标、适用边界、主流程和纪律约束。详细 checklist、模板、长示例放 `references/`；可重复执行的确定性操作放 `scripts/`；最终输出要消费的模板或素材才放 `assets/`。

### 5. 资产工程化优先于文档堆砌

skill 目录只保留完成任务必需的文件。不要为了“看起来完整”额外创建 README、安装指南、变更日志或过程笔记。

## 工作流

1. 定义 skill 候选
   - 明确要教会 agent 的单一能力、适用边界和非目标
   - 先判断它该不该升级为 skill，而不是别的资产类型
2. 先做 fail-first baseline
   - 写一个 pressure scenario，描述不给 skill 时最可能出现的错误
   - 记录基线失败：漏步骤、偷懒捷径、description 误导、结构失控、平台细节污染等
   - 环境支持独立 agent 时，优先用独立 agent 验证；不支持时，也要显式写出 baseline 场景与预期失败
3. 设计 discoverability
   - 先写 `name`
   - 再写 `description`，只描述何时使用，不总结 workflow
   - 用真实会被搜索到的触发词、症状、上下文增强可发现性
4. 设计结构
   - `SKILL.md` 保留核心原则、最小流程和纪律约束
   - 重型参考与模板拆到 `references/`
   - 可执行且重复出现的步骤才放 `scripts/`
   - 只有最终输出需要消费的素材才放 `assets/`
5. 写最小 skill
   - 按当前仓库领域结构落到 `src/domains/<domain>/skills/<name>/`
   - 只写能修正 baseline 失败的最小正文
   - 若已有相近 skill，优先 `adapt`，不要平行造轮子
6. 验证并补漏洞
   - 用同一 pressure scenario 复跑，确认行为已改变
   - 再补 1 到 2 个近邻场景，检查是否出现新的合理化路径
   - 一旦发现漏洞，补正文或下沉到 `references/`，再复验
7. 收口与同步
   - 同步必要的目标平台快照
   - 若任务口径变化，先更新 `alignment.md`，再继续执行
   - 没有 fresh validation evidence，就不要宣称 skill ready

## 纪律约束

- 不要把一次性复盘、任务日志或项目私规包装成通用 skill
- 不要把 workflow 摘要塞进 `description`
- 不要把研究、执行、验证、发布四种职责无限堆进一个 skill
- 不要把平台特定术语写进核心资产；平台差异继续放到 `targets/`
- 没有 baseline 或 fresh validation evidence，就不要说“这个 skill 已经可用”

## 渐进加载

只在当前意图需要时再读取参考文件：

- 判断该写 skill 还是别的资产：`references/authoring-checklist.md`
- 需要 frontmatter、结构拆分、目录卫生检查：`references/authoring-checklist.md`
- 需要 baseline / green / loophole plugging 模板：`references/validation-loop.md`
