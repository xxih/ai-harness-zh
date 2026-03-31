# Orchestration 协议

一种轻量模式，用于在复杂工作中协调 personas、skills 与 task agents。

不需要框架，不需要依赖，只需要结构化 prompt。

---

## 核心概念

大多数真实工作都会跨越多个 domain。一次产品发布需要工程、营销与战略；一次架构评审需要安全、成本分析与团队评估。

Orchestration 的作用是把正确的专业能力接到工作的正确阶段：

- **Personas** 定义“谁在思考”（身份、判断方式、沟通风格）
- **Skills** 定义“如何执行”（步骤、脚本、模板、参考资料）
- **Task agents** 定义“做什么”（有边界、单领域的执行任务）

你要把它们组合起来，模式始终一致。

---

## 模式

### 1. 定义目标

说明你想达成什么，而不是怎么达成。

```text
Objective: Launch a new SaaS product for small accounting firms.
Constraints: 2-person team, $5K budget, 6-week timeline.
Success criteria: 50 paying customers in first 30 days.
```

### 2. 选择合适的 persona

挑选与问题判断方式最匹配的 persona。Persona 会携带其立场、优先级与决策框架。

| 场景 | Persona | 原因 |
|------|---------|------|
| 架构决策、技术栈、招聘计划 | `startup-cto` | 具备务实的工程判断 |
| 发布策略、内容、增长渠道 | `growth-marketer` | 懂渠道，也有预算感 |
| 一个人全都要做 | `solo-founder` | 适合跨领域优先级权衡 |

**激活方式：**

```text
Load agents/personas/startup-cto.md
```

### 3. 加载执行所需的 skills

Persona 知道**做什么**，skills 知道**怎么做得精准**。根据当前阶段加载需要的 skill。

```text
Load skills:
- engineering/aws-solution-architect/SKILL.md
- engineering/mcp-server-builder/SKILL.md
```

persona 负责推动决策，skills 提供结构化步骤、脚本与模板。

### 4. 按阶段工作

把目标拆成多个阶段，每个阶段都可以使用不同的 skill。

```text
Phase 1: Technical Foundation (Week 1-2)
  Persona: startup-cto
  Skills: aws-solution-architect, senior-frontend
  Output: Architecture doc, deployed skeleton

Phase 2: Launch Preparation (Week 3-4)
  Persona: growth-marketer
  Skills: launch-strategy, copywriting, seo-audit
  Output: Landing page, content calendar, launch plan

Phase 3: Go-to-Market (Week 5-6)
  Persona: solo-founder
  Skills: email-sequence, analytics-tracking, pricing-strategy
  Output: Launched product, tracking, first customers
```

### 5. 在阶段之间交接

切换阶段时，把上下文往前传：

```text
Phase 1 complete.
Decisions made: [list key decisions]
Artifacts created: [list files/docs]
Open questions: [what the next phase needs to resolve]

Switching to Phase 2. Load growth-marketer persona and launch-strategy skill.
```

---

## 常见的 Orchestration 模式

### Pattern A: Solo Sprint

一个人、一个目标、多个 domain。你随着阶段切换 persona。

```text
Week 1: startup-cto + engineering skills → Build the thing
Week 2: growth-marketer + marketing skills → Prepare the launch
Week 3: solo-founder + business skills → Ship and iterate
```

适合：side project、MVP、solo founder。

### Pattern B: Domain Deep-Dive

一个 domain，追求最大深度。使用单个 persona，同时叠加多个 skill。

```text
Persona: startup-cto
Skills loaded simultaneously:
  - aws-solution-architect (infrastructure)
  - senior-security (hardening)
  - cto-advisor (tech debt assessment)

Task: Full technical audit of existing system
```

适合：架构评审、合规审计、技术尽调。

### Pattern C: Multi-Agent Handoff

不同 persona 互相审视彼此的工作，适合做质量兜底与覆盖补齐。

```text
Step 1: startup-cto designs the architecture
Step 2: growth-marketer reviews from user/market perspective
Step 3: solo-founder makes the final trade-off decision
```

适合：高风险决策、发布 readiness 评审、投资人准备。

### Pattern D: Skill Chain

不一定需要 persona，把多个 skill 顺序串起来处理流程型工作。

```text
1. content-strategy/SKILL.md → Identify topics and angles
2. copywriting/SKILL.md → Write the content
3. seo-audit/SKILL.md → Optimize for search
4. analytics-tracking/SKILL.md → Set up measurement
```

适合：可重复流程、内容流水线、合规检查清单。

---

## 示例：完整产品发布

下面是一套用于发布 B2B SaaS 产品的完整 orchestration。

### Setup

```text
Objective: Launch invoicing tool for freelancers
Team: 1 developer, 1 marketer
Timeline: 6 weeks
Budget: $3K
```

### Execution

**Week 1-2: Build**

```text
Persona: startup-cto
Skills:
  - aws-solution-architect → Infrastructure
  - senior-frontend → UI implementation

Deliverables:
  - Architecture decision record
  - Deployed MVP (auth, core feature, payments)
  - CI/CD pipeline
```

**Week 3-4: Prepare Launch**

```text
Persona: growth-marketer
Skills:
  - launch-strategy → Launch plan and timeline
  - copywriting → Landing page, emails
  - content-strategy → Blog posts, social content
  - seo-audit → Technical SEO for landing page

Deliverables:
  - Landing page live
  - 5 blog posts scheduled
  - Email sequence configured
  - Launch day checklist
```

**Week 5: Launch**

```text
Persona: solo-founder
Skills:
  - email-sequence → Drip campaign
  - analytics-tracking → Conversion tracking
  - ab-test-setup → Landing page variants

Deliverables:
  - Product Hunt submission
  - Email blast to waitlist
  - Tracking verified end-to-end
```

**Week 6: Iterate**

```text
Persona: solo-founder
Skills:
  - form-cro → Optimize signup flow
  - copy-editing → Refine messaging based on feedback

Deliverables:
  - Conversion improvements shipped
  - Week 1 metrics report
  - Roadmap for month 2
```

---

## 规则

1. **一次只用一个 persona。** 可以切换，但不要在同一个 prompt 里混合两个 persona，始终只选一个 voice。
2. **Skills 可以自由叠加。** 任务需要多少就加载多少，它们不会互相冲突。
3. **Personas 是可选的。** 纯流程型工作只用 skill chain 也足够。
4. **上下文要向前传。** 切阶段时，始终总结决策与产物。
5. **最终由人做决定。** Orchestration 只是建议，人可以覆盖任意阶段、persona 或 skill 选择。

---

## 快速参考

### Persona 激活

```text
Load agents/personas/<name>.md
```

### Skill 加载

```text
Load <domain>/<skill-name>/SKILL.md
```

### 阶段交接

```text
Phase [N] complete.
Decisions: [list]
Artifacts: [list]
Open items: [list]
Switching to: [persona] + [skills]
```

### 可用 Personas

见 [agents/personas/README.md](../agents/personas/README.md)

### 可用 Skills

见 [skill catalog](../README.md)；当前说明里写的是 12 个 domain 下的 177 个 skills。
