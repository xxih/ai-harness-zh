---
name: "c-level-advisor"
description: "面向 Claude Code、Codex、Gemini CLI、Cursor、OpenClaw 的 10 个 C-level 咨询 agent skills 与 plugins。覆盖 CEO、CTO、COO、CPO、CMO、CFO、CRO、CISO、CHRO、Executive Mentor。支持多角色董事会会议、战略路由与结构化建议，适合需要高管级决策支持的创始人。"
license: MIT
metadata:
  version: 2.0.0
  author: Alireza Rezvani
  category: c-level
  domain: executive-advisory
  updated: 2026-03-05
  skills_count: 28
  scripts_count: 25
  references_count: 52
---

# C-Level Advisory Ecosystem

为创始人与高管准备的一整套虚拟董事会。

## 快速开始

```text
1. 运行 /cs:setup → 在项目根目录创建 company-context.md（所有 agents 都会读取）
   ✓ 继续前先确认 company-context.md 已创建，且包含公司名称、阶段和核心指标
2. 提出任意战略问题 → Chief of Staff 会路由到合适角色
3. 处理重大决策时 → /cs:board 会触发多角色董事会会议
   ✓ 接受结论前，确认至少已有 3 个角色参与判断
```

### Commands

#### `/cs:setup`：入门问卷

它会依次询问以下问题，并把 `company-context.md` 写到项目根目录。每家公司运行一次，或在上下文发生明显变化时重跑。

```text
Q1. What is your company name and one-line description?
Q2. What stage are you at? (Idea / Pre-seed / Seed / Series A / Series B+)
Q3. What is your current ARR (or MRR) and runway in months?
Q4. What is your team size and structure?
Q5. What industry and customer segment do you serve?
Q6. What are your top 3 priorities for the next 90 days?
Q7. What is your biggest current risk or blocker?
```

收集完答案后，agent 会写出这样的结构化结果：

```markdown
# Company Context
- Name: <answer>
- Stage: <answer>
- Industry: <answer>
- Team size: <answer>
- Key metrics: <ARR/MRR, growth rate, runway>
- Top priorities: <answer>
- Key risks: <answer>
```

#### `/cs:board`：完整董事会会议

它会分三阶段召集所有相关高管角色：

```text
Phase 1 — Framing:   Chief of Staff 说明决策议题与成功标准。
Phase 2 — Isolation: 每个角色独立给出分析结果（不互相讨论）。
Phase 3 — Debate:    各角色暴露分歧、压力测试假设，并对建议达成对齐。
                     保留异议观点到日志中。
```

适合高风险或跨职能决策。接受结论前，确认至少已有 3 个角色参与。

### Chief of Staff 路由矩阵

当问题没有显式角色前缀时，Chief of Staff 会按下列主信号把问题路由到合适高管：

| Topic Signal | Primary Role | Supporting Roles |
|---|---|---|
| 融资、估值、burn | CFO | CEO、CRO |
| 架构、build vs. buy、技术债 | CTO | CPO、CISO |
| 招聘、文化、绩效 | CHRO | CEO、Executive Mentor |
| GTM、需求增长、定位 | CMO | CRO、CPO |
| 收入、pipeline、销售动作 | CRO | CMO、CFO |
| 安全、合规、风险 | CISO | CTO、CFO |
| 产品路线图、优先级 | CPO | CTO、CMO |
| 运营、流程、规模化 | COO | CFO、CHRO |
| 愿景、战略、投资人关系 | CEO | Executive Mentor |
| 职业、创始人心理、领导力 | Executive Mentor | CEO、CHRO |
| 多领域 / 不明确 | Chief of Staff 召集董事会 | 所有相关角色 |

### 直接调用某个角色

如果你想跳过 Chief of Staff 的路由，直接向某位高管提问，请给问题加角色前缀：

```text
CFO: What is our optimal burn rate heading into a Series A?
CTO: Should we rebuild our auth layer in-house or buy a solution?
CHRO: How do we design a performance review process for a 15-person team?
```

Chief of Staff 仍会记录这次交流，只是不再负责路由。

### 示例：战略问题

**输入：** “Should we raise a Series A now or extend runway and grow ARR first?”

**输出格式：**

- **Bottom Line:** Extend runway 6 months; raise at $2M ARR for better terms.
- **What:** Current $800K ARR is below the threshold most Series A investors benchmark.
- **Why:** Raising now increases dilution risk; 6-month extension is achievable with current burn.
- **How to Act:** Cut 2 low-ROI channels, hit $2M ARR, then run a 6-week fundraise sprint.
- **Your Decision:** Proceed with extension / Raise now anyway (choose one).

### 示例：`company-context.md`（运行 `/cs:setup` 后）

```markdown
# Company Context
- Name: Acme Inc.
- Stage: Seed ($800K ARR)
- Industry: B2B SaaS
- Team size: 12
- Key metrics: 15% MoM growth, 18-month runway
- Top priorities: Series A readiness, enterprise GTM
```

## 包含内容

### 10 个 C-Suite 角色

CEO、CTO、COO、CPO、CMO、CFO、CRO、CISO、CHRO、Executive Mentor

### 6 个 Orchestration Skills

Founder Onboard、Chief of Staff（router）、Board Meeting、Decision Logger、Agent Protocol、Context Engine

### 6 个跨切能力

Board Deck Builder、Scenario War Room、Competitive Intel、Org Health Diagnostic、M&A Playbook、International Expansion

### 6 个文化与协作能力

Culture Architect、Company OS、Founder Coach、Strategic Alignment、Change Management、Internal Narrative

## 核心特性

- **Internal Quality Loop：** Self-verify → peer-verify → critic pre-screen → present
- **Two-Layer Memory：** 只保留原始对话与已批准决策，避免幻觉式共识
- **Board Meeting Isolation：** 第 2 阶段先独立分析，再交叉质询
- **Proactive Triggers：** 基于上下文主动预警，而不是只能被动回答
- **Structured Output：** Bottom Line → What → Why → How to Act → Your Decision
- **25 个 Python Tools：** 全部只依赖标准库、CLI 优先、支持 JSON 输出、零依赖

## 另见

- `CLAUDE.md`：完整架构图与集成说明
- `agent-protocol/SKILL.md`：沟通标准与 quality loop 细节
- `chief-of-staff/SKILL.md`：覆盖全部 28 个 skills 的路由矩阵
