---
name: "product-skills"
description: "面向 Claude Code、Codex、Gemini CLI、Cursor、OpenClaw 的 10 个产品 agent skills 与 plugins。覆盖 PM toolkit（RICE）、agile PO、product strategist（OKR）、UX researcher、UI design system、competitive teardown、landing page generator、SaaS scaffolder、research summarizer。附带只依赖标准库的 Python 工具。"
version: 1.1.0
author: Alireza Rezvani
license: MIT
tags:
  - product
  - product-management
  - ux
  - ui
  - saas
  - agile
agents:
  - claude-code
  - codex-cli
  - openclaw
---

# Product Team Skills

8 个可用于生产环境的产品 skill，覆盖产品管理、UX/UI 设计与 SaaS 开发。

## 快速开始

### Claude Code

```text
/read product-team/product-manager-toolkit/SKILL.md
```

### Codex CLI

```bash
npx agent-skills-cli add alirezarezvani/claude-skills/product-team
```

## Skills 概览

| Skill | Folder | Focus |
|-------|--------|-------|
| Product Manager Toolkit | `product-manager-toolkit/` | RICE 优先级、客户发现、PRD |
| Agile Product Owner | `agile-product-owner/` | User stories、sprint planning、backlog |
| Product Strategist | `product-strategist/` | OKR 级联、市场分析、愿景设计 |
| UX Researcher Designer | `ux-researcher-designer/` | Personas、journey maps、可用性测试 |
| UI Design System | `ui-design-system/` | Design tokens、组件文档、响应式 |
| Competitive Teardown | `competitive-teardown/` | 系统化竞品分析 |
| Landing Page Generator | `landing-page-generator/` | 转化优化落地页 |
| SaaS Scaffolder | `saas-scaffolder/` | 生产级 SaaS 脚手架 |

## Python Tools

共 9 个脚本，全部只依赖标准库：

```bash
python3 product-manager-toolkit/scripts/rice_prioritizer.py --help
python3 product-strategist/scripts/okr_cascade_generator.py --help
```

## 规则

- 只加载当前真正需要的那个 `SKILL.md`
- 评分和分析优先用 Python 工具完成，不要靠手工判断
