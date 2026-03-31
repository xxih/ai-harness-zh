# GSD Agent 参考

> GSD 的 18 个专用 agent：角色、工具、拉起模式以及相互关系。架构背景请见 [Architecture](../ARCHITECTURE.md)。

---

## 概览

GSD 采用多 agent 架构：由轻量 orchestrator（工作流文件）拉起带全新上下文窗口的专用 agent。每个 agent 都有聚焦角色、受限工具权限，并负责产出特定工件。

### Agent 分类

| 分类 | 数量 | Agents |
|------|------|--------|
| Researchers | 3 | project-researcher、phase-researcher、ui-researcher |
| Analyzers | 2 | assumptions-analyzer、advisor-researcher |
| Synthesizers | 1 | research-synthesizer |
| Planners | 1 | planner |
| Roadmappers | 1 | roadmapper |
| Executors | 1 | executor |
| Checkers | 3 | plan-checker、integration-checker、ui-checker |
| Verifiers | 1 | verifier |
| Auditors | 2 | nyquist-auditor、ui-auditor |
| Mappers | 1 | codebase-mapper |
| Debuggers | 1 | debugger |

---

## Agent 详情

### gsd-project-researcher

**角色：** 在创建 roadmap 之前调研目标领域生态。

| 属性 | 值 |
|------|----|
| **由谁拉起** | `/gsd:new-project`、`/gsd:new-milestone` |
| **并行度** | 4 个实例（stack、features、architecture、pitfalls） |
| **工具** | Read、Write、Bash、Grep、Glob、WebSearch、WebFetch、mcp（context7） |
| **模型（balanced）** | Sonnet |
| **产出** | `.planning/research/STACK.md`、`FEATURES.md`、`ARCHITECTURE.md`、`PITFALLS.md` |

**能力：**
- 通过 Web 搜索获取当前生态信息
- 集成 Context7 MCP 用于库文档查询
- 直接把 research 文档写入磁盘，减少 orchestrator 的上下文负载

---

### gsd-phase-researcher

**角色：** 在规划前调研某个具体阶段的实现方式。

| 属性 | 值 |
|------|----|
| **由谁拉起** | `/gsd:plan-phase` |
| **并行度** | 4 个实例（与 project researcher 相同的关注面） |
| **工具** | Read、Write、Bash、Grep、Glob、WebSearch、WebFetch、mcp（context7） |
| **模型（balanced）** | Sonnet |
| **产出** | `{phase}-RESEARCH.md` |

**能力：**
- 读取 `CONTEXT.md`，让 research 聚焦在用户已经做出的决策上
- 调查该阶段所属领域的实现模式
- 检测测试基础设施，用于 Nyquist 验证映射

---

### gsd-ui-researcher

**角色：** 为前端阶段产出 UI 设计契约。

| 属性 | 值 |
|------|----|
| **由谁拉起** | `/gsd:ui-phase` |
| **并行度** | 单实例 |
| **工具** | Read、Write、Bash、Grep、Glob、WebSearch、WebFetch、mcp（context7） |
| **模型（balanced）** | Sonnet |
| **颜色** | `#E879F9`（fuchsia） |
| **产出** | `{phase}-UI-SPEC.md` |

**能力：**
- 检测设计系统状态（shadcn `components.json`、Tailwind 配置、现有 tokens）
- 为 React / Next.js / Vite 项目提供 shadcn 初始化建议
- 只追问尚未回答的设计契约问题
- 对第三方组件强制执行 registry 安全门禁

---

### gsd-assumptions-analyzer

**角色：** 深入分析某个阶段涉及的代码库，并输出结构化假设，包含证据、置信度和假设错误时的后果。

| 属性 | 值 |
|------|----|
| **由谁拉起** | `discuss-phase-assumptions` 工作流（当 `workflow.discuss_mode = 'assumptions'` 时） |
| **并行度** | 单实例 |
| **工具** | Read、Bash、Grep、Glob |
| **模型（balanced）** | Sonnet |
| **颜色** | Cyan |
| **产出** | 结构化假设，包括决策陈述、证据文件路径、置信等级 |

**关键行为：**
- 读取 `ROADMAP.md` 中的阶段描述和过往 `CONTEXT.md`
- 在代码库中搜索与该阶段相关的文件（组件、模式、相似功能）
- 读取 5 到 15 个最相关源文件，形成基于证据的假设
- 置信度分类：Confident（代码中清楚可见）、Likely（合理推断）、Unclear（可能有多种情况）
- 标记需要外部 research 的议题（库兼容性、生态最佳实践）
- 按 tier 调整输出：`full_maturity`（3 到 5 个区域）、`standard`（3 到 4 个）、`minimal_decisive`（2 到 3 个）

---

### gsd-advisor-researcher

**角色：** 在 `discuss-phase` 的 advisor mode 下，只研究一个灰区决策，并返回结构化对比表。

| 属性 | 值 |
|------|----|
| **由谁拉起** | `discuss-phase` 工作流（当 `ADVISOR_MODE = true` 时） |
| **并行度** | 多实例（每个灰区一个） |
| **工具** | Read、Bash、Grep、Glob、WebSearch、WebFetch、mcp（context7） |
| **模型（balanced）** | Sonnet |
| **颜色** | Cyan |
| **产出** | 5 列对比表（Option / Pros / Cons / Complexity / Recommendation）和一段 rationale |

**关键行为：**
- 使用 Claude 自身知识、Context7 和 Web 搜索，只研究一个被分配的灰区
- 给出真正可行的选项，不用无意义的 filler 选项凑数
- Complexity 一列基于影响面和风险，而不是时间预估
- Recommendation 是条件式建议（“如果 X 选这个”“如果 Y 选那个”），而不是唯一胜者排序
- 按 tier 调整输出：`full_maturity`（3 到 5 个选项并带成熟度信号）、`standard`（2 到 4 个）、`minimal_decisive`（2 个选项并给出明确建议）

---

### gsd-research-synthesizer

**角色：** 将并行 researcher 的输出合成为统一摘要。

| 属性 | 值 |
|------|----|
| **由谁拉起** | `/gsd:new-project`（4 个 researcher 完成后） |
| **并行度** | 单实例（在 researcher 之后顺序执行） |
| **工具** | Read、Write、Bash |
| **模型（balanced）** | Sonnet |
| **颜色** | Purple |
| **产出** | `.planning/research/SUMMARY.md` |

---

### gsd-planner

**角色：** 创建可执行的阶段计划，包含任务拆解、依赖分析和目标反推验证。

| 属性 | 值 |
|------|----|
| **由谁拉起** | `/gsd:plan-phase`、`/gsd:quick` |
| **并行度** | 单实例 |
| **工具** | Read、Write、Bash、Glob、Grep、WebFetch、mcp（context7） |
| **模型（balanced）** | Opus |
| **颜色** | Green |
| **产出** | `{phase}-{N}-PLAN.md` 文件 |

**关键行为：**
- 读取 `PROJECT.md`、`REQUIREMENTS.md`、`CONTEXT.md`、`RESEARCH.md`
- 创建 2 到 3 份适合单个上下文窗口完成的原子任务计划
- 使用带 `<task>` 元素的 XML 结构
- 包含 `read_first` 和 `acceptance_criteria` 段落
- 按依赖关系把计划分进不同 wave

---

### gsd-roadmapper

**角色：** 创建项目 roadmap，包括阶段拆解和需求映射。

| 属性 | 值 |
|------|----|
| **由谁拉起** | `/gsd:new-project` |
| **并行度** | 单实例 |
| **工具** | Read、Write、Bash、Glob、Grep |
| **模型（balanced）** | Sonnet |
| **颜色** | Purple |
| **产出** | `ROADMAP.md` |

**关键行为：**
- 将需求映射到各个阶段（traceability）
- 从需求中推导成功标准
- 尊重阶段数量的 granularity 设置
- 校验覆盖率（每个 v1 需求都必须映射到某个阶段）

---

### gsd-executor

**角色：** 通过原子 commit、偏差处理和 checkpoint 协议来执行 GSD 计划。

| 属性 | 值 |
|------|----|
| **由谁拉起** | `/gsd:execute-phase`、`/gsd:quick` |
| **并行度** | 多实例（wave 内并行，wave 间串行） |
| **工具** | Read、Write、Edit、Bash、Grep、Glob |
| **模型（balanced）** | Sonnet |
| **颜色** | Yellow |
| **产出** | 代码变更、git commit、`{phase}-{N}-SUMMARY.md` |

**关键行为：**
- 每个 plan 使用全新的 200K 上下文窗口
- 严格遵循 XML 任务指令
- 每个完成任务对应一个原子 git commit
- 处理多种 checkpoint 类型：auto、human-verify、decision、human-action
- 在 `SUMMARY.md` 中报告与原计划的偏差
- 验证失败时调用 node repair

---

### gsd-plan-checker

**角色：** 在执行前验证计划是否真的能达成阶段目标。

| 属性 | 值 |
|------|----|
| **由谁拉起** | `/gsd:plan-phase`（验证循环，最多 3 轮） |
| **并行度** | 单实例（迭代式） |
| **工具** | Read、Bash、Glob、Grep |
| **模型（balanced）** | Sonnet |
| **颜色** | Green |
| **产出** | PASS / FAIL 结论及具体反馈 |

**8 个验证维度：**
1. 需求覆盖
2. 任务原子性
3. 依赖顺序
4. 文件范围
5. 验证命令
6. 上下文适配度
7. 缺口检测
8. Nyquist 合规性（启用时）

---

### gsd-integration-checker

**角色：** 验证跨阶段集成和端到端流程。

| 属性 | 值 |
|------|----|
| **由谁拉起** | `/gsd:audit-milestone` |
| **并行度** | 单实例 |
| **工具** | Read、Bash、Grep、Glob |
| **模型（balanced）** | Sonnet |
| **颜色** | Blue |
| **产出** | 集成验证报告 |

---

### gsd-ui-checker

**角色：** 根据质量维度校验 `UI-SPEC.md` 设计契约。

| 属性 | 值 |
|------|----|
| **由谁拉起** | `/gsd:ui-phase`（验证循环，最多 2 轮） |
| **并行度** | 单实例 |
| **工具** | Read、Bash、Glob、Grep |
| **模型（balanced）** | Sonnet |
| **颜色** | `#22D3EE`（cyan） |
| **产出** | BLOCK / FLAG / PASS 结论 |

---

### gsd-verifier

**角色：** 通过目标反推分析验证阶段目标是否达成。

| 属性 | 值 |
|------|----|
| **由谁拉起** | `/gsd:execute-phase`（所有 executor 完成后） |
| **并行度** | 单实例 |
| **工具** | Read、Write、Bash、Grep、Glob |
| **模型（balanced）** | Sonnet |
| **颜色** | Green |
| **产出** | `{phase}-VERIFICATION.md` |

**关键行为：**
- 依据阶段目标校验代码库，而不是只看任务是否完成
- 给出带具体证据的 PASS / FAIL
- 将发现的问题记录下来，交给 `/gsd:verify-work` 处理

---

### gsd-nyquist-auditor

**角色：** 通过生成测试来补齐 Nyquist 验证缺口。

| 属性 | 值 |
|------|----|
| **由谁拉起** | `/gsd:validate-phase` |
| **并行度** | 单实例 |
| **工具** | Read、Write、Edit、Bash、Grep、Glob |
| **模型（balanced）** | Sonnet |
| **产出** | 测试文件、更新后的 `VALIDATION.md` |

**关键行为：**
- 绝不修改实现代码，只改测试文件
- 每个 gap 最多尝试 3 次
- 如果发现实现层面的 bug，会升级为需要用户处理的问题

---

### gsd-ui-auditor

**角色：** 对已实现的前端代码做回溯式 6 支柱视觉审计。

| 属性 | 值 |
|------|----|
| **由谁拉起** | `/gsd:ui-review` |
| **并行度** | 单实例 |
| **工具** | Read、Write、Bash、Grep、Glob |
| **模型（balanced）** | Sonnet |
| **颜色** | `#F472B6`（pink） |
| **产出** | 带评分的 `{phase}-UI-REVIEW.md` |

**6 个审计支柱（1 到 4 分）：**
1. 文案
2. 视觉
3. 色彩
4. 字体
5. 间距
6. 体验设计

---

### gsd-codebase-mapper

**角色：** 浏览代码库并写出结构化分析文档。

| 属性 | 值 |
|------|----|
| **由谁拉起** | `/gsd:map-codebase` |
| **并行度** | 4 个实例（tech、architecture、quality、concerns） |
| **工具** | Read、Bash、Grep、Glob、Write |
| **模型（balanced）** | Haiku |
| **颜色** | Cyan |
| **产出** | `.planning/codebase/*.md`（7 份文档） |

**关键行为：**
- 只读探索 + 结构化输出
- 直接把文档写入磁盘
- 不做复杂推理，只从文件内容中提取模式

---

### gsd-debugger

**角色：** 用科学方法和持久状态调查 bug。

| 属性 | 值 |
|------|----|
| **由谁拉起** | `/gsd:debug`、`/gsd:verify-work`（用于失败情况） |
| **并行度** | 单实例（交互式） |
| **工具** | Read、Write、Edit、Bash、Grep、Glob、WebSearch |
| **模型（balanced）** | Sonnet |
| **颜色** | Orange |
| **产出** | `.planning/debug/*.md`、知识库更新 |

**调试会话生命周期：**
`gathering` → `investigating` → `fixing` → `verifying` → `awaiting_human_verify` → `resolved`

**关键行为：**
- 跟踪假设、证据以及被排除的理论
- 状态可以跨上下文重置持续保存
- 标记为 resolved 前必须经过人工验证
- 问题解决后会追加到持久知识库
- 新会话会先查询知识库

---

### gsd-user-profiler

**角色：** 基于 8 个行为维度分析会话消息，产出带评分的开发者画像。

| 属性 | 值 |
|------|----|
| **由谁拉起** | `/gsd:profile-user` |
| **并行度** | 单实例 |
| **工具** | Read |
| **模型（balanced）** | Sonnet |
| **颜色** | Magenta |
| **产出** | `USER-PROFILE.md`、`/gsd:dev-preferences`、`CLAUDE.md` 中的 profile 区块 |

**行为维度：**
沟通风格、决策模式、调试方式、UX 偏好、厂商选择、挫败触发点、学习方式、解释深度。

**关键行为：**
- 只读 agent：只分析提取出的会话数据，不修改文件
- 产出带评分的维度、置信等级和证据引用
- 当拿不到会话历史时，提供问卷兜底

---

## Agent 工具权限汇总

| Agent | Read | Write | Edit | Bash | Grep | Glob | WebSearch | WebFetch | MCP |
|-------|------|-------|------|------|------|------|-----------|----------|-----|
| project-researcher | ✓ | ✓ | | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| phase-researcher | ✓ | ✓ | | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| ui-researcher | ✓ | ✓ | | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| assumptions-analyzer | ✓ | | | ✓ | ✓ | ✓ | | | |
| advisor-researcher | ✓ | | | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| research-synthesizer | ✓ | ✓ | | ✓ | | | | | |
| planner | ✓ | ✓ | | ✓ | ✓ | ✓ | | ✓ | ✓ |
| roadmapper | ✓ | ✓ | | ✓ | ✓ | ✓ | | | |
| executor | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | | | |
| plan-checker | ✓ | | | ✓ | ✓ | ✓ | | | |
| integration-checker | ✓ | | | ✓ | ✓ | ✓ | | | |
| ui-checker | ✓ | | | ✓ | ✓ | ✓ | | | |
| verifier | ✓ | ✓ | | ✓ | ✓ | ✓ | | | |
| nyquist-auditor | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | | | |
| ui-auditor | ✓ | ✓ | | ✓ | ✓ | ✓ | | | |
| codebase-mapper | ✓ | ✓ | | ✓ | ✓ | ✓ | | | |
| debugger | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | | |
| user-profiler | ✓ | | | | | | | | |

**最小权限原则：**
- Checker 都是只读的（没有 Write / Edit）：它们负责评估，不负责修改
- Researcher 具备 web 访问权限：因为它们需要当前生态信息
- Executor 具备 Edit：因为它们负责改代码，但没有 web 访问
- Mapper 具备 Write：因为它们要写分析文档，但没有 Edit（不改代码）
