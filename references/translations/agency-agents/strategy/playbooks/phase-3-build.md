# 🔨 Phase 3 Playbook — 构建与迭代

> **Duration**: 2-12 weeks (varies by scope) | **Agents**: 15-30+ | **Gate Keeper**: Agents Orchestrator

---

## 目标

通过持续的 Dev↔QA loops 实现全部功能。每个任务都必须先被验证，才能进入下一个任务。这是绝大多数工作真正发生的阶段，也是 NEXUS 编排价值最明显的地方。

## 前置条件

- [ ] 已通过 Phase 2 Quality Gate（foundation 已验证）
- [ ] 已有带 RICE 分数的 Sprint Prioritizer backlog
- [ ] CI/CD pipeline 已运行
- [ ] design system 与 component library 已可用
- [ ] 含认证系统的 API scaffold 已就绪

## Dev↔QA Loop：核心机制

Agents Orchestrator 通过以下循环管理每个任务：

```text
FOR EACH task IN sprint_backlog (ordered by RICE score):

  1. ASSIGN task to appropriate Developer Agent (see assignment matrix)
  2. Developer IMPLEMENTS task
  3. Evidence Collector TESTS task
     - Visual screenshots (desktop, tablet, mobile)
     - Functional verification against acceptance criteria
     - Brand consistency check
  4. IF verdict == PASS:
       Mark task complete
       Move to next task
     ELIF verdict == FAIL AND attempts < 3:
       Send QA feedback to Developer
       Developer FIXES specific issues
       Return to step 3
     ELIF attempts >= 3:
       ESCALATE to Agents Orchestrator
       Orchestrator decides: reassign, decompose, defer, or accept
  5. UPDATE pipeline status report
```

## Agent 分配矩阵

### Primary Developer Assignment

| Task Category | Primary Agent | Backup Agent | QA Agent |
|--------------|--------------|-------------|----------|
| **React/Vue/Angular UI** | Frontend Developer | Rapid Prototyper | Evidence Collector |
| **REST/GraphQL API** | Backend Architect | Senior Developer | API Tester |
| **Database operations** | Backend Architect | — | API Tester |
| **Mobile (iOS/Android)** | Mobile App Builder | — | Evidence Collector |
| **ML model/pipeline** | AI Engineer | — | Test Results Analyzer |
| **CI/CD/Infrastructure** | DevOps Automator | Infrastructure Maintainer | Performance Benchmarker |
| **Premium/complex feature** | Senior Developer | Backend Architect | Evidence Collector |
| **Quick prototype/POC** | Rapid Prototyper | Frontend Developer | Evidence Collector |
| **WebXR/immersive** | XR Immersive Developer | — | Evidence Collector |
| **visionOS** | visionOS Spatial Engineer | macOS Spatial/Metal Engineer | Evidence Collector |
| **Cockpit controls** | XR Cockpit Interaction Specialist | XR Interface Architect | Evidence Collector |
| **CLI/terminal tools** | Terminal Integration Specialist | — | API Tester |
| **Code intelligence** | LSP/Index Engineer | — | Test Results Analyzer |
| **Performance optimization** | Performance Benchmarker | Infrastructure Maintainer | Performance Benchmarker |

### Specialist Support（按需激活）

| Specialist | When to Activate | Trigger |
|-----------|-----------------|---------|
| UI Designer | Component needs visual refinement | Developer requests design guidance |
| Whimsy Injector | Feature needs delight/personality | UX review identifies opportunity |
| Visual Storyteller | Visual narrative content needed | Content requires visual assets |
| Brand Guardian | Brand consistency concern | QA finds brand deviation |
| XR Interface Architect | Spatial interaction design needed | XR feature requires UX guidance |
| Analytics Reporter | Deep data analysis needed | Feature requires analytics integration |

## 并行构建轨道

对于 NEXUS-Full 部署，默认同时运行四条轨道：

### Track A：Core Product Development

```text
Managed by: Agents Orchestrator (Dev↔QA loop)
Agents: Frontend Developer, Backend Architect, AI Engineer,
        Mobile App Builder, Senior Developer
QA: Evidence Collector, API Tester, Test Results Analyzer

Sprint cadence: 2-week sprints
Daily: Task implementation + QA validation
End of sprint: Sprint review + retrospective
```

### Track B：Growth & Marketing Preparation

```text
Managed by: Project Shepherd
Agents: Growth Hacker, Content Creator, Social Media Strategist,
        App Store Optimizer

Sprint cadence: Aligned with Track A milestones
Activities:
- Growth Hacker → Design viral loops and referral mechanics
- Content Creator → Build launch content pipeline
- Social Media Strategist → Plan cross-platform campaign
- App Store Optimizer → Prepare store listing (if mobile)
```

### Track C：Quality & Operations

```text
Managed by: Agents Orchestrator
Agents: Evidence Collector, API Tester, Performance Benchmarker,
        Workflow Optimizer, Experiment Tracker

Continuous activities:
- Evidence Collector → Screenshot QA for every task
- API Tester → Endpoint validation for every API task
- Performance Benchmarker → Periodic load testing
- Workflow Optimizer → Process improvement identification
- Experiment Tracker → A/B test setup for validated features
```

### Track D：Brand & Experience Polish

```text
Managed by: Brand Guardian
Agents: UI Designer, Brand Guardian, Visual Storyteller,
        Whimsy Injector

Triggered activities:
- UI Designer → Component refinement when QA identifies visual issues
- Brand Guardian → Periodic brand consistency audit
- Visual Storyteller → Visual narrative assets as features complete
- Whimsy Injector → Micro-interactions and delight moments
```

## Sprint 执行模板

### Sprint Planning（Day 1）

```text
Sprint Prioritizer activates:
1. Review backlog with updated RICE scores
2. Select tasks for sprint based on team velocity
3. Assign tasks to developer agents
4. Identify dependencies and ordering
5. Set sprint goal and success criteria

Output: Sprint Plan with task assignments
```

### Daily Execution（Day 2 到 Day N-1）

```text
Agents Orchestrator manages:
1. Current task status check
2. Dev↔QA loop execution
3. Blocker identification and resolution
4. Progress tracking and reporting

Status report format:
- Tasks completed today: [list]
- Tasks in QA: [list]
- Tasks in development: [list]
- Blocked tasks: [list with reason]
- QA pass rate: [X/Y]
```

### Sprint Review（Day N）

```text
Project Shepherd facilitates:
1. Demo completed features
2. Review QA evidence for each task
3. Collect stakeholder feedback
4. Update backlog based on learnings

Participants: All active agents + stakeholders
Output: Sprint Review Summary
```

### Sprint Retrospective

```text
Workflow Optimizer facilitates:
1. What went well?
2. What could improve?
3. What will we change next sprint?
4. Process efficiency metrics

Output: Retrospective Action Items
```

## Orchestrator 决策逻辑

### Task Failure Handling

```text
WHEN task fails QA:
  IF attempt == 1:
    → Send specific QA feedback to developer
    → Developer fixes ONLY the identified issues
    → Re-submit for QA
    
  IF attempt == 2:
    → Send accumulated QA feedback
    → Consider: Is the developer agent the right fit?
    → Developer fixes with additional context
    → Re-submit for QA
    
  IF attempt == 3:
    → ESCALATE
    → Options:
      a) Reassign to different developer agent
      b) Decompose task into smaller sub-tasks
      c) Revise approach/architecture
      d) Accept with known limitations (document)
      e) Defer to future sprint
    → Document decision and rationale
```

### Parallel Task Management

```text
WHEN multiple tasks have no dependencies:
  → Assign to different developer agents simultaneously
  → Each runs independent Dev↔QA loop
  → Orchestrator tracks all loops concurrently
  → Merge completed tasks in dependency order

WHEN task has dependencies:
  → Wait for dependency to pass QA
  → Then assign dependent task
  → Include dependency context in handoff
```

## 质量门禁检查清单

| # | Criterion | Evidence Source | Status |
|---|-----------|----------------|--------|
| 1 | All sprint tasks pass QA (100% completion) | Evidence Collector screenshots per task | ☐ |
| 2 | All API endpoints validated | API Tester regression report | ☐ |
| 3 | Performance baselines met (P95 < 200ms) | Performance Benchmarker report | ☐ |
| 4 | Brand consistency verified (95%+ adherence) | Brand Guardian audit | ☐ |
| 5 | No critical bugs (zero P0/P1 open) | Test Results Analyzer summary | ☐ |
| 6 | All acceptance criteria met | Task-by-task verification | ☐ |
| 7 | Code review completed for all PRs | Git history evidence | ☐ |

## Gate 决策

**Gate Keeper**：Agents Orchestrator

- **PASS**：应用功能完整，激活 Phase 4
- **CONTINUE**：还需要更多 sprints，继续留在 Phase 3
- **ESCALATE**：存在系统性问题，需要 Studio Producer 介入

## 交接到 Phase 4

```markdown
## Phase 3 → Phase 4 Handoff Package

### For Reality Checker:
- Complete application (all features implemented)
- All QA evidence from Dev↔QA loops
- API Tester regression results
- Performance Benchmarker baseline data
- Brand Guardian consistency audit
- Known issues list (if any accepted limitations)

### For Legal Compliance Checker:
- Data handling implementation details
- Privacy policy implementation
- Consent management implementation
- Security measures implemented

### For Performance Benchmarker:
- Application URLs for load testing
- Expected traffic patterns
- Performance budgets from architecture

### For Infrastructure Maintainer:
- Production environment requirements
- Scaling configuration needs
- Monitoring alert thresholds
```

---

*当所有 sprint tasks 都通过 QA、所有 API endpoints 均已验证、性能基线达标且没有未关闭的关键 bug 时，Phase 3 完成。*
