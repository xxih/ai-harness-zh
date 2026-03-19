# WARP.md

这个文件为 WARP（warp.dev）在处理本仓库代码时提供指导。

## 项目概览

Claudeception 是一个用于持续学习的 **Claude Code skill**——它让 Claude Code 可以自主提取并保存学到的知识，整理成可复用的 skill。它不是一个应用代码库，而是一个带文档和示例的 skill 定义仓库。

## 关键文件

- `SKILL.md` —— 主 skill 定义（YAML frontmatter + 指令）。这是 Claude Code 实际会加载的内容。
- `resources/skill-template.md` —— 用于创建新 skill 的模板
- `examples/` —— 展示正确格式的示例 skill

## Skill 文件格式

skill 使用 YAML frontmatter，后接 markdown 正文：

```yaml
---
name: kebab-case-name
description: |
  Must be precise for semantic matching. Include:
  (1) exact use cases, (2) trigger conditions like error messages,
  (3) what problem this solves
author: Claude Code
version: 1.0.0
allowed-tools:
  - Read
  - Write
  - Bash
  - Grep
  - Glob
---
```

`description` 字段至关重要——它决定了这个 skill 会在语义匹配时于什么场景被召回。

## 安装路径

- **用户级**：`~/.claude/skills/[skill-name]/`
- **项目级**：`.claude/skills/[skill-name]/`

## Skill 的质量标准

在修改或创建 skill 时，确保它满足：
- **可复用**：能帮助未来任务，而不只是当前这一个实例
- **非平凡**：需要经过发现过程，而不是简单查文档
- **具体**：触发条件清晰（精确报错、症状）
- **已验证**：方案已经真实测试并确认有效

## 研究基础

这个方法建立在关于 skill libraries 的学术研究之上（Voyager、CASCADE、SEAgent、Reflexion）。细节见 `resources/research-references.md`。
