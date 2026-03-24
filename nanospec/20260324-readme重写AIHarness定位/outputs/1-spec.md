# 规格说明：20260324-readme重写AIHarness定位

## 背景

当前 `README.md` 已经说明仓库会收集翻译与沉淀自有 package，但对 “AI Harness 是什么” 和 “本仓库实际维护 Harness 的哪一层” 解释不足。用户希望用简单、可传播的话把这两个问题讲清楚，并补上推荐参考对象。

在此基础上，用户进一步要求 README 前部先写出成熟 harness 通常已经做了哪些系统能力，而这些能力里有相当一部分对于日常开发者、尤其是裸用 Claude Code 的普通使用者来说，通常还没有被系统化补齐。

## 目标

本任务需要把根 README 调整成一个更清楚的仓库入口，至少回答三件事：

1. AI Harness 是什么。
2. 当前仓库为什么聚焦 Harness 中可定制的那一层。
3. 新读者优先应该参考哪些外部 harness，以及原因是什么。
4. 成熟 harness 已覆盖的系统能力，与当前仓库已有能力相比，差异主要在哪里。

## 交付范围

### 1. AI Harness 定义

README 需要给出一个简单但不失真的定义。

成功标志：

- 明确写出 AI Harness 可以粗略理解为“除了 LLM 外的一切”。
- 同时补足至少一组典型组成，例如 prompt、skills、commands、hooks、rules、工具接入、上下文注入、验证流程、权限约束等。
- 读者能快速理解 Harness 不是单一 prompt 文件，而是一整套运行外壳。

验收证据：

- `README.md`

### 2. 仓库定位说明

README 需要说明本仓库不是在重做 LLM 或完整运行时，而是在研究并沉淀 coding agent 提供的可定制入口。

成功标志：

- 文案明确指出并非整套 harness 都由用户控制。
- 文案明确指出本仓库主要关注 agent 暴露出来的扩展口子，例如 `AGENTS.md`、`SKILL.md`、commands、hooks / plugins、rules、MCP、target 包与相关文档。
- 文案与当前仓库的 `packages/` / `references/` 组织方式一致。

验收证据：

- `README.md`

### 3. 推荐参考的 harness

README 需要新增一节，列出推荐优先参考的 harness 与原因。

成功标志：

- 只列当前仓库已收录、且确实能支持“为什么值得参考”的对象。
- 原因不是泛泛而谈的“很强”“很火”，而是对应其擅长的层次，例如全栈 harness、skill-first workflow、运行时编排与治理。
- 推荐对象与本仓库当前参考区现状一致。

验收证据：

- `README.md`
- `references/repos/`
- `references/translations/`

### 4. 分类能力对照

README 前部需要新增一节，按类别列出成熟 harness 的代表能力、当前仓库已沉淀能力，以及仍未系统化覆盖的部分。

成功标志：

- 至少覆盖需求规划、执行编排、质量门禁、搜索 / 上下文治理、学习沉淀、平台适配几个类别。
- 每个类别至少给出一到两个具体引用点，例如 `superpowers` 的 `brainstorming`、`writing-plans`、`subagent-driven-development`，或 `everything-claude-code` 的 `/quality-gate`、`continuous-learning-v2`，或 `oh-my-opencode` 的 `delegate_task`、`background-agent`。
- 当前仓库一侧必须落到已有 package，而不是抽象地说“我们也有一些能力”。
- 文案明确区分“当前仓库已沉淀的 prompt / workflow 资产”和“普通开发者日常裸用工具时通常还没有做成的运行时、hook、平台或自动化能力”。

验收证据：

- `README.md`
- `packages/`
- `references/repos/`
- `references/translations/`

### 5. NanoSpec 文档落盘

这次任务需要完整落在 `nanospec` 任务容器里。

成功标志：

- `brief.md`、`outputs/1-spec.md`、`outputs/2-plan.md`、`outputs/3-tasks.md` 均已填写。
- `outputs/3-tasks.md` 反映本次交付动作和完成状态，而不是空白模板。

验收证据：

- `nanospec/20260324-readme重写AIHarness定位/brief.md`
- `nanospec/20260324-readme重写AIHarness定位/outputs/1-spec.md`
- `nanospec/20260324-readme重写AIHarness定位/outputs/2-plan.md`
- `nanospec/20260324-readme重写AIHarness定位/outputs/3-tasks.md`

## 非目标

- 不在本次任务里新增 package、skill、command、hook 或 target。
- 不尝试给 AI Harness 下过度学术化或平台无差别的统一定义。
- 不把所有收录过的外部仓库都塞进推荐列表。

## 约束

- 默认使用简体中文；代码、路径、API 名称、协议关键字保持原文。
- README 文案要面向第一次进入仓库的读者，先解释概念，再解释仓库组织。
- README 前部的能力对照要把“外部成熟能力”“当前仓库已有能力”“普通开发者通常尚未系统化补齐的部分”并列写清。
- 推荐理由必须能被当前仓库中的参考材料支撑，避免无依据扩写。
