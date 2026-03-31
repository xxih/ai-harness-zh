---
name: "business-growth-skills"
description: "面向 Claude Code、Codex、Gemini CLI、Cursor、OpenClaw 的 4 个业务增长 agent skills 与 plugins。覆盖 customer success（健康度评分、流失）、sales engineer（RFP）、revenue operations（pipeline、GTM）、contract & proposal writer。附带只依赖标准库的 Python 工具。"
version: 1.1.0
author: Alireza Rezvani
license: MIT
tags:
  - business
  - customer-success
  - sales
  - revenue-operations
  - growth
agents:
  - claude-code
  - codex-cli
  - openclaw
---

# Business & Growth Skills

面向客户成功、销售与 revenue operations 的 4 个可用于生产环境的 skill。

## 快速开始

### Claude Code

```text
/read business-growth/customer-success-manager/SKILL.md
```

### Codex CLI

```bash
npx agent-skills-cli add alirezarezvani/claude-skills/business-growth
```

## Skills 概览

| Skill | Folder | Focus |
|-------|--------|-------|
| Customer Success Manager | `customer-success-manager/` | 健康度评分、流失预测、扩张机会 |
| Sales Engineer | `sales-engineer/` | RFP 分析、竞争矩阵、PoC 规划 |
| Revenue Operations | `revenue-operations/` | Pipeline 分析、预测准确率、GTM 指标 |
| Contract & Proposal Writer | `contract-and-proposal-writer/` | 提案生成、合同模板 |

## Python Tools

共 9 个脚本，全部只依赖标准库：

```bash
python3 customer-success-manager/scripts/health_score_calculator.py --help
python3 revenue-operations/scripts/pipeline_analyzer.py --help
```

## 规则

- 只加载当前真正需要的那个 `SKILL.md`
- 评分与指标优先用 Python 工具计算，不要手工估算
