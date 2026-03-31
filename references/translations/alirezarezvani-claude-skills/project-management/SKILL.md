---
name: "pm-skills"
description: "面向 Claude Code、Codex、Gemini CLI、Cursor、OpenClaw 的 6 个项目管理 agent skills 与 plugins。覆盖 Senior PM、scrum master、Jira expert（JQL）、Confluence expert、Atlassian admin 与模板创建。支持通过 MCP 对 Jira/Confluence 做实时自动化。"
version: 1.0.0
author: Alireza Rezvani
license: MIT
tags:
  - project-management
  - jira
  - confluence
  - atlassian
  - scrum
  - agile
agents:
  - claude-code
  - codex-cli
  - openclaw
---

# Project Management Skills

6 个可用于生产环境的项目管理 skill，并集成了 Atlassian MCP。

## 快速开始

### Claude Code

```text
/read project-management/jira-expert/SKILL.md
```

### Codex CLI

```bash
npx agent-skills-cli add alirezarezvani/claude-skills/project-management
```

## Skills 概览

| Skill | Folder | Focus |
|-------|--------|-------|
| Senior PM | `senior-pm/` | 组合管理、风险分析、资源规划 |
| Scrum Master | `scrum-master/` | 速度预测、sprint 健康、retro |
| Jira Expert | `jira-expert/` | JQL 查询、workflow、自动化、dashboard |
| Confluence Expert | `confluence-expert/` | 知识库、页面布局、macros |
| Atlassian Admin | `atlassian-admin/` | 用户管理、权限、集成 |
| Atlassian Templates | `atlassian-templates/` | 蓝图、定制布局、可复用内容 |

## Python Tools

共 6 个脚本，全部只依赖标准库：

```bash
python3 senior-pm/scripts/project_health_dashboard.py --help
python3 scrum-master/scripts/velocity_analyzer.py --help
```

## 规则

- 只加载当前真正需要的那个 `SKILL.md`
- 如果环境里可用，优先用 MCP 工具完成实时 Jira/Confluence 操作
