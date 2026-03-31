# ⚡ NEXUS 快速上手指南

> **5 分钟内，从零进入可编排的多 agent pipeline。**

---

## 什么是 NEXUS？

**NEXUS**（Network of EXperts, Unified in Strategy）把 The Agency 的 AI specialists 组织成一条协同 pipeline。它不是一个一个地激活 agents，再赌它们能配合好，而是明确规定：谁做什么、什么时候做、每一步如何校验质量。

## 选择你的模式

| 我想要…… | 使用 | Agents | 时间 |
|-------------|-----|--------|------|
| 从零构建一个完整产品 | **NEXUS-Full** | All | 12-24 weeks |
| 构建一个 feature 或 MVP | **NEXUS-Sprint** | 15-25 | 2-6 weeks |
| 做一个具体任务（bug fix、campaign、audit） | **NEXUS-Micro** | 5-10 | 1-5 days |

---

## 🚀 NEXUS-Full：启动完整项目

**复制下面这段 prompt 来激活完整 pipeline：**

```text
Activate Agents Orchestrator in NEXUS-Full mode.

Project: [YOUR PROJECT NAME]
Specification: [DESCRIBE YOUR PROJECT OR LINK TO SPEC]

Execute the complete NEXUS pipeline:
- Phase 0: Discovery (Trend Researcher, Feedback Synthesizer, UX Researcher, Analytics Reporter, Legal Compliance Checker, Tool Evaluator)
- Phase 1: Strategy (Studio Producer, Senior Project Manager, Sprint Prioritizer, UX Architect, Brand Guardian, Backend Architect, Finance Tracker)
- Phase 2: Foundation (DevOps Automator, Frontend Developer, Backend Architect, UX Architect, Infrastructure Maintainer)
- Phase 3: Build (Dev↔QA loops — all engineering + Evidence Collector)
- Phase 4: Harden (Reality Checker, Performance Benchmarker, API Tester, Legal Compliance Checker)
- Phase 5: Launch (Growth Hacker, Content Creator, all marketing agents, DevOps Automator)
- Phase 6: Operate (Analytics Reporter, Infrastructure Maintainer, Support Responder, ongoing)

Quality gates between every phase. Evidence required for all assessments.
Maximum 3 retries per task before escalation.
```

---

## 🏃 NEXUS-Sprint：构建一个 Feature 或 MVP

**复制下面这段 prompt：**

```text
Activate Agents Orchestrator in NEXUS-Sprint mode.

Feature/MVP: [DESCRIBE WHAT YOU'RE BUILDING]
Timeline: [TARGET WEEKS]
Skip Phase 0 (market already validated).

Sprint team:
- PM: Senior Project Manager, Sprint Prioritizer
- Design: UX Architect, Brand Guardian
- Engineering: Frontend Developer, Backend Architect, DevOps Automator
- QA: Evidence Collector, Reality Checker, API Tester
- Support: Analytics Reporter

Begin at Phase 1 with architecture and sprint planning.
Run Dev↔QA loops for all implementation tasks.
Reality Checker approval required before launch.
```

---

## 🎯 NEXUS-Micro：执行一个具体任务

**根据场景选择并复制 prompt：**

### 修复一个 Bug

```text
Activate Backend Architect to investigate and fix [BUG DESCRIPTION].
After fix, activate API Tester to verify the fix.
Then activate Evidence Collector to confirm no visual regressions.
```

### 执行一轮营销活动

```text
Activate Social Media Strategist as campaign lead for [CAMPAIGN DESCRIPTION].
Team: Content Creator, Twitter Engager, Instagram Curator, Reddit Community Builder.
Brand Guardian reviews all content before publishing.
Analytics Reporter tracks performance daily.
Growth Hacker optimizes channels weekly.
```

### 进行合规审计

```text
Activate Legal Compliance Checker for comprehensive compliance audit.
Scope: [GDPR / CCPA / HIPAA / ALL]
After audit, activate Executive Summary Generator to create stakeholder report.
```

### 排查性能问题

```text
Activate Performance Benchmarker to diagnose performance issues.
Scope: [API response times / Page load / Database queries / All]
After diagnosis, activate Infrastructure Maintainer for optimization.
DevOps Automator deploys any infrastructure changes.
```

### 市场研究

```text
Activate Trend Researcher for market intelligence on [DOMAIN].
Deliverables: Competitive landscape, market sizing, trend forecast.
After research, activate Executive Summary Generator for executive brief.
```

### UX 改进

```text
Activate UX Researcher to identify usability issues in [FEATURE/PRODUCT].
After research, activate UX Architect to design improvements.
Frontend Developer implements changes.
Evidence Collector verifies improvements.
```

---

## 📁 策略文档

| Document | Purpose | Location |
|----------|---------|----------|
| **Master Strategy** | 完整 NEXUS doctrine | `strategy/nexus-strategy.md` |
| **Phase 0 Playbook** | Discovery 与 intelligence | `strategy/playbooks/phase-0-discovery.md` |
| **Phase 1 Playbook** | Strategy 与 architecture | `strategy/playbooks/phase-1-strategy.md` |
| **Phase 2 Playbook** | Foundation 与 scaffolding | `strategy/playbooks/phase-2-foundation.md` |
| **Phase 3 Playbook** | Build 与 iterate | `strategy/playbooks/phase-3-build.md` |
| **Phase 4 Playbook** | Quality 与 hardening | `strategy/playbooks/phase-4-hardening.md` |
| **Phase 5 Playbook** | Launch 与 growth | `strategy/playbooks/phase-5-launch.md` |
| **Phase 6 Playbook** | Operate 与 evolve | `strategy/playbooks/phase-6-operate.md` |
| **Activation Prompts** | 即用型 agent prompts | `strategy/coordination/agent-activation-prompts.md` |
| **Handoff Templates** | 标准 handoff 格式 | `strategy/coordination/handoff-templates.md` |
| **Startup MVP Runbook** | 4-6 周 MVP 构建 | `strategy/runbooks/scenario-startup-mvp.md` |
| **Enterprise Feature Runbook** | 企业功能开发 | `strategy/runbooks/scenario-enterprise-feature.md` |
| **Marketing Campaign Runbook** | 多渠道营销活动 | `strategy/runbooks/scenario-marketing-campaign.md` |
| **Incident Response Runbook** | 生产事故处理 | `strategy/runbooks/scenario-incident-response.md` |

---

## 🔑 30 秒理解关键概念

1. **Quality Gates**：没有基于证据的批准，就不能进入下一阶段
2. **Dev↔QA Loop**：每个任务都必须先 build 再 test；`PASS` 才继续，`FAIL` 就重试，最多 3 次
3. **Handoffs**：agents 之间必须结构化传递上下文，不能冷启动接手
4. **Reality Checker**：最终质量裁决者，默认立场是 `NEEDS WORK`
5. **Agents Orchestrator**：负责管理整个 pipeline 的控制器
6. **Evidence Over Claims**：看截图、测试结果和数据，不看口头断言

---

## 🎭 一眼看懂 Agents 分组

```text
ENGINEERING         │ DESIGN              │ MARKETING
Frontend Developer  │ UI Designer         │ Growth Hacker
Backend Architect   │ UX Researcher       │ Content Creator
Mobile App Builder  │ UX Architect        │ Twitter Engager
AI Engineer         │ Brand Guardian      │ TikTok Strategist
DevOps Automator    │ Visual Storyteller  │ Instagram Curator
Rapid Prototyper    │ Whimsy Injector     │ Reddit Community Builder
Senior Developer    │ Image Prompt Eng.   │ App Store Optimizer
                    │                     │ Social Media Strategist
────────────────────┼─────────────────────┼──────────────────────
PRODUCT             │ PROJECT MGMT        │ TESTING
Sprint Prioritizer  │ Studio Producer     │ Evidence Collector
Trend Researcher    │ Project Shepherd    │ Reality Checker
Feedback Synthesizer│ Studio Operations   │ Test Results Analyzer
                    │ Experiment Tracker  │ Performance Benchmarker
                    │ Senior Project Mgr  │ API Tester
                    │                     │ Tool Evaluator
                    │                     │ Workflow Optimizer
────────────────────┼─────────────────────┼──────────────────────
SUPPORT             │ SPATIAL             │ SPECIALIZED
Support Responder   │ XR Interface Arch.  │ Agents Orchestrator
Analytics Reporter  │ macOS Spatial/Metal │ Data Analytics Reporter
Finance Tracker     │ XR Immersive Dev    │ LSP/Index Engineer
Infra Maintainer    │ XR Cockpit Spec.    │ Sales Data Extraction
Legal Compliance    │ visionOS Spatial    │ Data Consolidation
Exec Summary Gen.   │ Terminal Integration│ Report Distribution
```

---

<div align="center">

**先选模式，再走 playbook，然后把执行交给 pipeline。**

`strategy/nexus-strategy.md` — 完整 doctrine

</div>
