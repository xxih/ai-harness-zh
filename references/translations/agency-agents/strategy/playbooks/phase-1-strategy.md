# 🏗️ Phase 1 Playbook — 策略与架构

> **Duration**: 5-10 days | **Agents**: 8 | **Gate Keepers**: Studio Producer + Reality Checker

---

## 目标

在写下第一行代码之前，先定义清楚我们要构建什么、整体结构是什么、成功标准是什么。每一个架构决策都要留档。每一个 feature 都要被优先级排序。每一笔预算都要有去向。

## 前置条件

- [ ] 已通过 Phase 0 Quality Gate（GO 决策）
- [ ] 已收到 Phase 0 Handoff Package
- [ ] Stakeholders 对项目范围已经达成一致

## Agent 激活顺序

### Step 1：Strategic Framing（Day 1-3，并行）

#### 🎬 Studio Producer — Strategic Portfolio Alignment

```text
Activate Studio Producer for strategic portfolio alignment on [PROJECT].

Input: Phase 0 Executive Summary + Market Analysis Report
Deliverables required:
1. Strategic Portfolio Plan with project positioning
2. Vision, objectives, and ROI targets
3. Resource allocation strategy
4. Risk/reward assessment
5. Success criteria and milestone definitions

Align with: Organizational strategic objectives
Format: Strategic Portfolio Plan Template
Timeline: 3 days
```

#### 🎭 Brand Guardian — Brand Identity System

```text
Activate Brand Guardian for brand identity development on [PROJECT].

Input: Phase 0 UX Research (personas, journey maps)
Deliverables required:
1. Brand Foundation (purpose, vision, mission, values, personality)
2. Visual Identity System (colors, typography, spacing as CSS variables)
3. Brand Voice and Messaging Architecture
4. Logo system specifications (if new brand)
5. Brand usage guidelines

Format: Brand Identity System Document
Timeline: 3 days
```

#### 💰 Finance Tracker — Budget and Resource Planning

```text
Activate Finance Tracker for financial planning on [PROJECT].

Input: Studio Producer strategic plan + Phase 0 Tech Stack Assessment
Deliverables required:
1. Comprehensive project budget with category breakdown
2. Resource cost projections (agents, infrastructure, tools)
3. ROI model with break-even analysis
4. Cash flow timeline
5. Financial risk assessment with contingency reserves

Format: Financial Plan with ROI Projections
Timeline: 2 days
```

### Step 2：Technical Architecture（Day 3-7，并行；需等待 Step 1 输出）

#### 🏛️ UX Architect — Technical Architecture + UX Foundation

```text
Activate UX Architect for technical architecture on [PROJECT].

Input: Brand Guardian visual identity + Phase 0 UX Research
Deliverables required:
1. CSS Design System (variables, tokens, scales)
2. Layout Framework (Grid/Flexbox patterns, responsive breakpoints)
3. Component Architecture (naming conventions, hierarchy)
4. Information Architecture (page flow, content hierarchy)
5. Theme System (light/dark/system toggle)
6. Accessibility Foundation (WCAG 2.1 AA baseline)

Files to create:
- css/design-system.css
- css/layout.css
- css/components.css
- docs/ux-architecture.md

Format: Developer-Ready Foundation Package
Timeline: 4 days
```

#### 🏗️ Backend Architect — System Architecture

```text
Activate Backend Architect for system architecture on [PROJECT].

Input: Phase 0 Tech Stack Assessment + Compliance Requirements
Deliverables required:
1. System Architecture Specification
   - Architecture pattern (microservices/monolith/serverless/hybrid)
   - Communication pattern (REST/GraphQL/gRPC/event-driven)
   - Data pattern (CQRS/Event Sourcing/CRUD)
2. Database Schema Design with indexing strategy
3. API Design Specification with versioning
4. Authentication and Authorization Architecture
5. Security Architecture (defense in depth)
6. Scalability Plan (horizontal scaling strategy)

Format: System Architecture Specification
Timeline: 4 days
```

#### 🤖 AI Engineer — ML Architecture（如适用）

```text
Activate AI Engineer for ML system architecture on [PROJECT].

Input: Backend Architect system architecture + Phase 0 Data Audit
Deliverables required:
1. ML System Design
   - Model selection and training strategy
   - Data pipeline architecture
   - Inference strategy (real-time/batch/edge)
2. AI Ethics and Safety Framework
3. Model monitoring and retraining plan
4. Integration points with main application
5. Cost projections for ML infrastructure

Condition: Only activate if project includes AI/ML features
Format: ML System Design Document
Timeline: 3 days
```

#### 👔 Senior Project Manager — Spec-to-Task Conversion

```text
Activate Senior Project Manager for task list creation on [PROJECT].

Input: ALL Phase 0 documents + Architecture specs (as available)
Deliverables required:
1. Comprehensive Task List
   - Quote EXACT requirements from spec (no luxury features)
   - Each task has clear acceptance criteria
   - Dependencies mapped between tasks
   - Effort estimates (story points or hours)
2. Work Breakdown Structure
3. Critical path identification
4. Risk register for implementation

Rules:
- Do NOT add features not in the specification
- Quote exact text from requirements
- Be realistic about effort estimates

Format: Task List with acceptance criteria
Timeline: 3 days
```

### Step 3：Prioritization（Day 7-10，串行；在 Step 2 之后）

#### 🎯 Sprint Prioritizer — Feature Prioritization

```text
Activate Sprint Prioritizer for backlog prioritization on [PROJECT].

Input:
- Senior Project Manager → Task List
- Backend Architect → System Architecture
- UX Architect → UX Architecture
- Finance Tracker → Budget Framework
- Studio Producer → Strategic Plan

Deliverables required:
1. RICE-scored backlog (Reach, Impact, Confidence, Effort)
2. Sprint assignments with velocity-based estimation
3. Dependency map with critical path
4. MoSCoW classification (Must/Should/Could/Won't)
5. Release plan with milestone mapping

Validation: Studio Producer confirms strategic alignment
Format: Prioritized Sprint Plan
Timeline: 2 days
```

## 质量门禁检查清单

| # | Criterion | Evidence Source | Status |
|---|-----------|----------------|--------|
| 1 | Architecture covers 100% of spec requirements | Senior PM task list cross-referenced with architecture | ☐ |
| 2 | Brand system complete (logo, colors, typography, voice) | Brand Guardian deliverable | ☐ |
| 3 | All technical components have implementation path | Backend Architect + UX Architect specs | ☐ |
| 4 | Budget approved and within constraints | Finance Tracker plan | ☐ |
| 5 | Sprint plan is velocity-based and realistic | Sprint Prioritizer backlog | ☐ |
| 6 | Security architecture defined | Backend Architect security spec | ☐ |
| 7 | Compliance requirements integrated into architecture | Legal requirements mapped to technical decisions | ☐ |

## Gate 决策

**需要双签**：Studio Producer（战略）+ Reality Checker（技术）

- **APPROVED**：携带完整 Architecture Package 进入 Phase 2
- **REVISE**：指定条目需要返工，回到对应 Step
- **RESTRUCTURE**：存在根本性架构问题，重新启动 Phase 1

## 交接到 Phase 2

```markdown
## Phase 1 → Phase 2 Handoff Package

### Architecture Package:
1. Strategic Portfolio Plan (Studio Producer)
2. Brand Identity System (Brand Guardian)
3. Financial Plan (Finance Tracker)
4. CSS Design System + UX Architecture (UX Architect)
5. System Architecture Specification (Backend Architect)
6. ML System Design (AI Engineer — if applicable)
7. Comprehensive Task List (Senior Project Manager)
8. Prioritized Sprint Plan (Sprint Prioritizer)

### For DevOps Automator:
- Deployment architecture from Backend Architect
- Environment requirements from System Architecture
- Monitoring requirements from Infrastructure needs

### For Frontend Developer:
- CSS Design System from UX Architect
- Brand Identity from Brand Guardian
- Component architecture from UX Architect
- API specification from Backend Architect

### For Backend Architect (continuing):
- Database schema ready for deployment
- API scaffold ready for implementation
- Auth system architecture defined
```

---

*当 Studio Producer 与 Reality Checker 都对 Architecture Package 签字通过时，Phase 1 完成。*
