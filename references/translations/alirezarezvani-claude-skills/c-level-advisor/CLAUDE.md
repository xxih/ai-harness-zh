# C-Level Advisory Skills — Claude Code Guidance

一套完整的虚拟董事会：28 个 skills，覆盖 10 个高管角色、编排层、跨切能力以及文化与协作框架。

## 架构

```text
/cs:setup (Founder Interview) → company-context.md
                │
        Chief of Staff (Router)
                │
    ┌───────────┼───────────┐
    10 Roles    6 Cross-Cut  6 Culture
    │           │            │
    └───────────┼────────────┘
                │
        Executive Mentor (Critic)
                │
        Decision Logger (Two-Layer Memory)
```

## Skills 概览

### C-Suite Roles（10）

| Role | Folder | Reasoning Technique | Scripts |
|------|--------|-------------------|---------|
| **CEO** | `ceo-advisor/` | Tree of Thought | `strategy_analyzer`、`financial_scenario_analyzer` |
| **CTO** | `cto-advisor/` | ReAct | `tech_debt_analyzer`、`team_scaling_calculator` |
| **COO** | `coo-advisor/` | Step by Step | `ops_efficiency_analyzer`、`okr_tracker` |
| **CPO** | `cpo-advisor/` | First Principles | `pmf_scorer`、`portfolio_analyzer` |
| **CMO** | `cmo-advisor/` | Recursion of Thought | `marketing_budget_modeler`、`growth_model_simulator` |
| **CFO** | `cfo-advisor/` | Chain of Thought | `burn_rate_calculator`、`unit_economics_analyzer`、`fundraising_model` |
| **CRO** | `cro-advisor/` | Chain of Thought | `revenue_forecast_model`、`churn_analyzer` |
| **CISO** | `ciso-advisor/` | Risk-Based | `risk_quantifier`、`compliance_tracker` |
| **CHRO** | `chro-advisor/` | Empathy + Data | `hiring_plan_modeler`、`comp_benchmarker` |
| **Executive Mentor** | `executive-mentor/` | Adversarial | `decision_matrix_scorer`、`stakeholder_mapper` |

### Orchestration（6）

| Skill | Folder | Purpose |
|-------|--------|---------|
| **C-Suite Onboard** | `cs-onboard/` | Founder interview → `company-context.md` |
| **Chief of Staff** | `chief-of-staff/` | 路由问题、触发 board meetings |
| **Board Meeting** | `board-meeting/` | 6 阶段多 agent 讨论 |
| **Decision Logger** | `decision-logger/` | 双层记忆（raw + approved） |
| **Agent Protocol** | `agent-protocol/` | agent 间调用、循环预防、quality loop |
| **Context Engine** | `context-engine/` | 公司上下文加载与匿名化 |

### Cross-Cutting Capabilities（6）

| Skill | Folder | Purpose |
|-------|--------|---------|
| **Board Deck Builder** | `board-deck-builder/` | 生成董事会 / 投资人更新 |
| **Scenario War Room** | `scenario-war-room/` | 多变量 what-if 建模 |
| **Competitive Intel** | `competitive-intel/` | 系统化竞品跟踪 |
| **Org Health Diagnostic** | `org-health-diagnostic/` | 跨职能健康评分 |
| **M&A Playbook** | `ma-playbook/` | 收购或被收购 |
| **International Expansion** | `intl-expansion/` | 市场进入策略 |

### Culture & Collaboration（6）

| Skill | Folder | Purpose |
|-------|--------|---------|
| **Culture Architect** | `culture-architect/` | 设计并落地公司文化 |
| **Company OS** | `company-os/` | EOS / Scaling Up 操作系统 |
| **Founder Coach** | `founder-coach/` | 创始人成长与辅导 |
| **Strategic Alignment** | `strategic-alignment/` | 战略级联与 silo 检测 |
| **Change Management** | `change-management/` | 基于 ADKAR 的变革推进 |
| **Internal Narrative** | `internal-narrative/` | 面向所有受众统一叙事 |

## Executive Mentor Slash Commands

只有这个 skill 带有 `plugin.json`（namespace: `em`），因为它提供了 slash commands。其他 skills 由 Chief of Staff router 或用户直接按名称调用。这是刻意设计的，只有真正需要命名空间命令时才加 `plugin.json`。

| Command | Purpose |
|---------|---------|
| `/em:challenge` | 对任意方案做 pre-mortem |
| `/em:board-prep` | 董事会会议准备 |
| `/em:hard-call` | 处理困难决策的框架 |
| `/em:stress-test` | 压测任意假设 |
| `/em:postmortem` | 诚实复盘 |

## 关键设计决策

- **Two-layer memory：** 仅保留原始记录与已批准决策，避免幻觉式共识
- **Phase 2 isolation：** 董事会会议期间，各 agent 先独立思考，再交叉质询
- **Internal Quality Loop：** Self-verify → peer-verify → critic pre-screen → present。未经验证的输出不应到达创始人
- **Proactive triggers：** 每个角色都带有上下文驱动的预警
- **User Communication Standard：** Bottom Line → What → Why → How to Act → Your Decision。只给结果，不叙述过程

## Python Tools（共 25 个）

全部脚本只依赖标准库，CLI-first，支持 JSON 输出，并带内置样例数据。

```bash
# 示例
python cfo-advisor/scripts/burn_rate_calculator.py
python cro-advisor/scripts/churn_analyzer.py
python cpo-advisor/scripts/pmf_scorer.py
python org-health-diagnostic/scripts/health_scorer.py
python strategic-alignment/scripts/alignment_checker.py
python decision-logger/scripts/decision_tracker.py
```

## 与其他 Domain 的集成

| C-Level Role | Layers Above |
|-------------|-------------|
| CMO | `marketing-skill/`（内容、需求生成、ASO 执行） |
| CFO | `finance/financial-analyst`（表格、DCF） |
| CRO | `business-growth/`（revenue ops、sales engineering） |
| CISO | `ra-qm-team/`（ISO 27001 检查清单、ISMS 审计） |
| CPO | `product-team/`（PM toolkit、user stories、sprint planning） |

---

**Last Updated:** 2026-03-05  
**Skills Deployed:** 28 skills（10 roles + 5 mentor commands + 6 orchestration + 6 cross-cutting + 6 culture）  
**Python Tools:** 25（stdlib-only）  
**Reference Docs:** 52
