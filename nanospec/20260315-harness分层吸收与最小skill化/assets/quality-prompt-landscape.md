# 质量方向 Prompt 版图研究

## 1. 研究目标

这份文档专门补齐“质量方向”的证据层研究。目标不是继续抽象地说“有 TDD、验证、评审”，而是把 `references/repos/` 里真正承载这些约束的 prompt 文件找出来，回答四个问题：

1. 每个仓库把质量能力写在哪些文件里。
2. 这些文件分别扮演什么角色：`skill`、`command`、`agent`，还是运行时里的提醒模板。
3. 它们之间哪些地方高度重合，哪些地方明显不同。
4. 这些差异对当前仓库继续打磨 `coding-quality-loop` 有什么具体启发。

## 2. 研究范围与方法

### 2.1 范围

本次只看三个参考仓库：

- `references/repos/everything-claude-code`
- `references/repos/superpowers`
- `references/repos/oh-my-opencode`

质量方向的判定关键词主要是：

- TDD / test-first
- verify / verification / quality gate
- code review / reviewer
- build fix / type check / lint / coverage
- security review
- completion gate / verification reminder

### 2.2 方法

- 先用关键词筛出候选文件。
- 再只读真正承载质量约束的源文件，不把多语言镜像文档重复计入。
- 对每个文件标记三类信息：`阶段`、`载体类型`、`运行时依赖`。

说明：

- `docs/zh-CN`、`docs/ja-JP`、`docs/ko-KR`、`docs/zh-TW` 这类翻译镜像本轮不重复统计。
- `oh-my-opencode` 有一部分“prompt”并不是 Markdown，而是源码里的提醒模板与 hook 注入文本；这些仍计入，因为它们实际承担了质量约束。

## 3. 总览结论

先给结论，再展开：

1. `everything-claude-code` 的质量资产最“模块化”。同一能力常常同时存在 `skill`、`command`、`agent` 三种载体，适合拆单个能力吸收，但也最容易重复。
2. `superpowers` 的质量资产最“纪律化”。它不是强调更多检查项，而是强调在压力下不要自我放过，核心是反合理化、反偷懒、反口头完成。
3. `oh-my-opencode` 的质量能力最“系统化”。它较少给用户一个独立的 TDD 或 verify skill，而是把验证提醒、完成门禁、计划审查写进 orchestration 和 hooks 里。
4. 三者共同的骨架其实一致：实现前约束、改动后验证、独立视角审查、完成前门禁。
5. 当前仓库后来已不再维持单个 `coding-quality-loop`，而是改成 `quality-*` 家族；这份研究仍可作为拆分依据。
   - `superpowers` 的“证据先于宣称”和“反合理化”表达强度
   - `oh-my-opencode` 的“系统自动提醒/强制完成门禁”思路
6. 若只把 `superpowers` 看成“依赖 subagent 的特殊工作流”，结论会偏保守。以 2026 年的主流 harness 现状看，multiagent 已经更接近常见执行能力，真正需要裁掉的是 worktree 前置、仓库绑定脚本和平台专属 runtime。

## 4. 分仓库盘点

## 4.1 everything-claude-code

### 4.1.1 核心文件

| 文件                                | 类型    | 质量阶段 | 作用                                                             | 备注                               |
| ----------------------------------- | ------- | -------- | ---------------------------------------------------------------- | ---------------------------------- |
| `skills/tdd-workflow/SKILL.md`      | skill   | 实现前   | 测试先行、80%+ 覆盖率、单元/集成/E2E 全覆盖                      | 更像“完整测试流程说明书”           |
| `skills/verification-loop/SKILL.md` | skill   | 改动后   | build / types / lint / tests / security / diff review 六阶段验证 | 机械检查最完整                     |
| `commands/tdd.md`                   | command | 实现前   | `/tdd` 命令入口，调用 `tdd-guide` agent                          | 是 skill 的轻量命令壳              |
| `commands/verify.md`                | command | 改动后   | `/verify` 命令入口，按固定顺序执行验证                           | 输出格式非常短                     |
| `commands/code-review.md`           | command | 交付前   | 对未提交 diff 做安全与质量审查                                   | 直接阻止 commit                    |
| `commands/quality-gate.md`          | command | 改动后   | formatter/lint/type 的轻量质量管线                               | 比 `/verify` 更轻、更偏 path scope |
| `commands/test-coverage.md`         | command | 改动后   | 分析覆盖率缺口并补测试                                           | 把覆盖率单独拆出                   |
| `commands/build-fix.md`             | command | 改动后   | 按错误逐个修复 build/type 问题                                   | 是 build 救火专用                  |
| `agents/tdd-guide.md`               | agent   | 实现前   | TDD 专家，强调 RED/GREEN/REFACTOR 和覆盖率                       | 还补了 eval-driven TDD             |
| `agents/code-reviewer.md`           | agent   | 交付前   | 高置信度代码评审，带严重级别和审查过滤                           | 强调少噪声、高置信度               |
| `agents/build-error-resolver.md`    | agent   | 改动后   | 只为把 build/type 拉绿，要求最小 diff                            | 非常聚焦                           |
| `agents/security-reviewer.md`       | agent   | 交付前   | OWASP 方向的安全审查                                             | 与通用 review 分离                 |

### 4.1.2 邻近与变体文件

这些文件不一定都需要吸收，但它们说明 ECC 的质量能力是“横向分叉”的：

- `commands/python-review.md`
- `commands/go-review.md`
- `commands/kotlin-review.md`
- `commands/go-test.md`
- `commands/kotlin-test.md`
- `agents/python-reviewer.md`
- `agents/go-reviewer.md`
- `agents/kotlin-reviewer.md`
- `agents/go-build-resolver.md`
- `agents/kotlin-build-resolver.md`
- `skills/security-review/SKILL.md`

这组文件显示出 ECC 的一个明显特征：先做通用能力，再做语言/栈专用分支。

### 4.1.3 这个仓库的质量思路

- 质量能力被拆得很细，便于按需调用。
- `skill` 负责方法论，`command` 负责可触发入口，`agent` 负责具体人格化执行。
- “验证”主要被理解为一组可枚举、可执行的机械检查。
- “评审”主要被理解为按严重级别输出问题。
- “安全”被视为质量的平行分支，而不是默认包含在所有 review 里。

### 4.1.4 强项与弱项

强项：

- 模块化清楚，几乎每个质量子能力都能独立复用。
- 对 build/type/lint/tests/security/diff 这类机械验证最完整。
- 语言专用 review/build/test 分支很适合大型 prompt 仓库扩展。

弱项：

- 资产之间明显重复，例如 `tdd-workflow`、`tdd` 命令、`tdd-guide` agent 三层都在讲同一个能力。
- 对“人在压力下会跳过验证”这件事约束不够强，更多是 checklist，而不是行为约束。
- 很依赖调用方自己知道何时该用哪一个。

## 4.2 superpowers

### 4.2.1 核心文件

| 文件                                                                 | 类型           | 质量阶段        | 作用                                                        | 备注                           |
| -------------------------------------------------------------------- | -------------- | --------------- | ----------------------------------------------------------- | ------------------------------ |
| `skills/test-driven-development/SKILL.md`                            | skill          | 实现前          | 强硬 TDD 纪律，强调“没看到 fail 就不算测试”                 | 语气最强，反合理化最明显       |
| `skills/test-driven-development/testing-anti-patterns.md`            | reference      | 实现前/测试设计 | 反 mock 行为测试、反 test-only methods、反不完整 mock       | 是 TDD 的配套炮火              |
| `skills/verification-before-completion/SKILL.md`                     | skill          | 改动后/完成前   | 所有完成宣称前必须跑新鲜验证                                | 核心是“evidence before claims” |
| `skills/requesting-code-review/SKILL.md`                             | skill          | 交付前          | 请求独立代码评审，强调 review cadence                       | 默认走独立 reviewer，现已较易迁移 |
| `skills/requesting-code-review/code-reviewer.md`                     | prompt 模板    | 交付前          | review prompt 模板，按 Strengths / Issues / Assessment 输出 | 非常适合复用                   |
| `skills/receiving-code-review/SKILL.md`                              | skill          | 评审反馈处理    | 处理外部 review 意见时先核实，不做表演性认同                | 这个维度 ECC 基本没有          |
| `agents/code-reviewer.md`                                            | agent          | 交付前          | 高级 reviewer，按计划与标准审查实现                         | 更偏“对照计划”而不是扫描 diff  |
| `skills/subagent-driven-development/SKILL.md`                        | workflow skill | 执行期          | 每个任务后做 spec review，再做 code quality review          | 把 review 嵌进任务节奏         |
| `skills/subagent-driven-development/code-quality-reviewer-prompt.md` | prompt 模板    | 执行期/交付前   | 二阶段 review 中的 code quality reviewer 模板               | 强调文件职责和可测试性         |
| `skills/finishing-a-development-branch/SKILL.md`                     | skill          | 收尾            | 合并前先验测试，再给选项                                    | 是 branch 层完成门禁           |
| `docs/testing.md`                                                    | docs           | 元层            | 测试 superpowers 自身 skill 的真实会话验证办法              | 把“技能测试”也做成验证体系     |

### 4.2.2 这个仓库的质量思路

- 核心不是“检查项多”，而是“不能自我欺骗”。
- 强调压力下的行为约束，例如：
  - 忘了先写测试就删代码重来
  - 没有 fresh verification evidence 就不能说完成
  - 收到 review 反馈也不能先表态、后核实
- 质量链路不是简单的 `test → verify → review`，而是把“请求 review”和“接收 review”拆成两端。
- 在 subagent 工作流里，review 不是终点，而是每个任务后都发生。

### 4.2.3 强项与弱项

强项：

- 对 AI/agent 在压力下偷懒、跳步、合理化的约束极强。
- `verification-before-completion` 抓住了一个很关键但常被漏掉的阶段：完成宣称之前。
- `receiving-code-review` 很罕见，它处理的是“收到反馈后怎么不盲从”。
- 二阶段 review 机制比单次 review 更稳：先看 spec，再看质量。

弱项：

- 若直接照搬整套 workflow，容易把它的任务节奏、语气和角色拆分一起带进来。
- 表达风格很强，直接照搬容易把仓库文风带得过硬。
- 对 build/type/lint/tests/security 的具体机械命令覆盖，没有 ECC 那么系统。

## 4.3 oh-my-opencode

### 4.3.1 核心文件

| 文件                                           | 类型           | 质量阶段      | 作用                                                                         | 备注                       |
| ---------------------------------------------- | -------------- | ------------- | ---------------------------------------------------------------------------- | -------------------------- |
| `AGENTS.md`                                    | 仓库级提示     | 全流程        | 定义测试模式、禁用反模式、CI/test/build/typecheck 约束                       | 质量先是仓库规约           |
| `docs/guide/orchestration.md`                  | guide          | 计划到执行    | 把验证嵌进 Prometheus/Atlas/Sisyphus 体系                                    | 明确存在 Verify 阶段       |
| `docs/guide/overview.md`                       | guide          | 全流程        | 强调 Atlas 独立验证完成情况                                                  | 面向用户解释               |
| `docs/reference/features.md`                   | reference      | 执行期        | `/refactor` 明确要求 TDD verification after changes                          | 是命令能力说明             |
| `src/agents/AGENTS.md`                         | agent registry | 计划/执行     | `Momus` 为计划 reviewer，`Atlas` 为 orchestrator                             | review 先从计划开始        |
| `src/hooks/atlas/AGENTS.md`                    | hook 文档      | 执行后/完成前 | Atlas 在工具执行后注入 verification reminder                                 | 质量被系统强制追加         |
| `src/hooks/atlas/system-reminder-templates.ts` | 提醒模板源码   | 执行后/完成前 | 规定 Read code → lsp_diagnostics → tests/build → hands-on QA → gate decision | 最像“验证 prompt 正文”     |
| `src/hooks/atlas/verification-reminders.ts`    | 提醒模板源码   | 完成前        | completion gate、QA tasks、plan checkbox 更新                                | 进度与验证绑定             |
| `src/hooks/atlas/tool-execute-after.ts`        | hook 实现      | 执行后        | 在 `task` 后自动拼接 verification reminder                                   | 把 prompt 变成强制系统行为 |

### 4.3.2 这个仓库的质量思路

- 它没有像 ECC 或 superpowers 那样给用户一组清晰的独立质量 skill。
- 质量主要体现在三件事：
  - 计划阶段有人审 plan：`Momus`
  - 执行后系统自动提醒验证：Atlas hooks
  - 完成前必须更新 plan/todo/QA 状态：completion gate
- 它把“不要相信 subagent 自报完成”写成系统提醒，而不是单个可选 skill。

### 4.3.3 强项与弱项

强项：

- 最擅长把质量约束系统化、自动化。
- 强制把验证和进度跟踪绑在一起，减少“做了但没记”“说完成但没核实”。
- hands-on QA 要求很强，明确前端要真打开、CLI 要真运行、API 要真 curl。

弱项：

- 可直接挪用的 prompt 资产不多，很多价值埋在源码和 hooks 里。
- 运行时依赖最重，不适合作为当前仓库第一波直接吸收对象。
- 它更像“质量执行系统”而不是“质量知识资产”。

## 5. 重合点与共性

三仓库虽然风格差异很大，但共性非常稳定。

### 5.1 共同骨架

| 共同母题                 | ECC                             | superpowers                                | Oh My OpenCode                                   |
| ------------------------ | ------------------------------- | ------------------------------------------ | ------------------------------------------------ |
| 实现前先设质量约束       | `tdd-workflow` / `tdd-guide`    | `test-driven-development`                  | `/refactor` 的 TDD verification、计划期澄清      |
| 改动后必须机械验证       | `verification-loop` / `verify`  | `verification-before-completion`           | Atlas verification reminder                      |
| 需要独立审查视角         | `code-reviewer` / `code-review` | `requesting-code-review` / reviewer prompt | `Momus` 计划审查、Atlas 后验校验                 |
| 不信“已经完成”的口头报告 | diff review + report            | evidence before claims                     | “subagent work is extremely suspicious” 提醒文本 |
| 测试不能只看 happy path  | 80%+ 覆盖率、edge cases         | anti-patterns、real behavior               | 读取代码并要求 tests/build/hands-on QA           |

### 5.2 重合区域

这些能力在三个仓库里高度重合，只是载体不同：

1. TDD
   - ECC：skill + command + agent 三层并存
   - superpowers：一个高强度 skill + 反模式参考
   - OMO：没有独立 skill，但 `/refactor` 和系统提醒里有 TDD 验证要求

2. 改动后验证
   - ECC：build/types/lint/tests/security/diff 的 checklist
   - superpowers：fresh evidence gate
   - OMO：hook 自动注入“先读代码，再跑 diagnostics/tests/build，再做 hands-on QA”

3. 独立评审
   - ECC：通用 reviewer + 语言专用 reviewer
   - superpowers：请求评审、接收评审、二阶段评审
   - OMO：plan reviewer + orchestrator 后验验证

4. 完成门禁
   - ECC：更多依赖操作者主动调用 `/verify` 或 `/code-review`
   - superpowers：完成宣称前必须自证
   - OMO：系统注入 completion gate，甚至要求更新 plan/todo 才算完成

## 6. 关键差异

## 6.1 粒度差异

- ECC：最细，按单一子能力切很多文件。
- superpowers：中等粒度，一个 skill 常带强行为规范和大量判断规则。
- OMO：最粗，很多质量能力不以单独 prompt 文件存在，而以系统行为出现。

## 6.2 约束方式差异

- ECC：靠 checklist 和专门角色。
- superpowers：靠“铁律”与反合理化语言。
- OMO：靠 hook 与 orchestrator 自动注入。

## 6.3 用户触达方式差异

- ECC：用户需要知道 `/tdd`、`/verify`、`/code-review` 等命令。
- superpowers：用户通常进入某个 skill 或 subagent 工作流，由流程带着走。
- OMO：很多质量动作不是用户主动点单，而是系统在后台替你加上。

## 6.4 可移植性差异

- ECC：最高，最适合当前仓库吸收。
- superpowers：中高，multiagent 本身已不是主要障碍，但语气、worktree 约束和整套 workflow 节奏仍需裁剪。
- OMO：最低，更适合作为设计启发，不适合直接照搬。

## 6.5 “评审”定义差异

- ECC 的评审更像“对当前 diff 做问题扫描”。
- superpowers 的评审更像“对当前任务结果做节奏化的独立把关”。
- OMO 的评审先发生在计划层，再发生在执行验证层，强调系统不信自报完成。

## 7. 对当前仓库的直接启发

## 7.1 `coding-quality-loop` 已经吸收的部分

当前仓库已经吸收到的骨架主要来自：

- ECC 的 `tdd-workflow` / `verification-loop` / `code-review`
- superpowers 的 `test-driven-development` / `requesting-code-review`

也就是：

- 实现前考虑测试先行
- 改动后做验证闭环
- 关键节点做独立评审

## 7.2 当前还没吸收、但值得下一轮考虑的部分

### A. `verification-before-completion` 的“完成宣称门禁”

当前 `coding-quality-loop` 说了 `ready / not-ready`，但没有像 superpowers 那样把“没有 fresh evidence 就不能说完成”写成独立而强硬的门槛。

可吸收方式：

- 直接把这条原则吸收到 `coding-quality-loop/references/verify.md` 和主 `SKILL.md`
- `ready` 必须和 fresh evidence 绑定，而不是只给一个结果标签

### B. `receiving-code-review` 的“反馈处理”维度

当前仓库有“做 review”，还没有“收到 review 后如何处理反馈”的共享资产。

可吸收方式：

- 短期先吸收到 `coding-quality-loop/references/review.md`
- 如果后续 PR review / code review 变多，再拆成独立后置处理资产

### C. `requesting-code-review` 的独立 reviewer 节奏

当前仓库强调“要 review”，但还没把“谁来 review”写成明确执行建议。

可吸收方式：

- 在高风险改动、关键节点、完成宣称前，优先请求独立 reviewer
- 当环境支持 multiagent 时，把 reviewer 作为优先路径；不支持时再退回当前会话自审

### D. OMO 的“自动完成门禁/提醒”思路

当前仓库是纯 prompt 资产仓，短期不适合做 hooks 系统，但它给了两个很清楚的启发：

1. 验证提醒要明确到“用什么工具、按什么顺序验证”
2. 完成记录要和验证动作绑定，不能只说“应该验证”

可吸收方式：

- 在 `nanospec` 的执行/验收阶段加入更明确的 verification checklist
- 或在 `coding-quality-loop` 里补一份更强的“交付前检查模板”

### E. ECC 的语言专用分支策略

如果当前仓库未来继续扩展 coding 类 skill，一个自然方向不是再堆一个大而全 `coding-quality-loop`，而是：

- 保持一个通用入口 skill
- 再按栈补充可选 references 或专用评审附录

例如：

- Python 评审附录
- Go 构建/测试附录
- 前端交互验证附录

## 8. 对“是否继续拆 skill”的判断

基于这轮研究，当前最合理的判断是：

1. 维持 `coding-quality-loop` 作为通用入口是对的。
2. 但不应再把所有质量能力都继续往一个入口里硬塞。
3. 下一轮若继续扩展，更适合补“附录型 reference”或“后置处理型 skill”，而不是回到三四个并列入口。

优先级建议：

1. 先用 `superpowers` 补强 `coding-quality-loop` 的“completion gate / fresh evidence / reviewer cadence”。
2. 再评估是否需要一个轻量的 `receiving-review-feedback` 类资产。
3. 暂不吸收 OMO 的运行时 hook 体系，只吸收它的提醒结构和 gate 设计。

## 9. 最终结论

如果只看“功能名”，三个仓库都在讲 TDD、验证、评审。

但如果看“真正写进 prompt 的行为约束”，它们的分工很不一样：

- `everything-claude-code` 负责把质量能力拆成可点用的模块。
- `superpowers` 负责把质量纪律写到 agent 很难耍滑头。
- `oh-my-opencode` 负责把质量要求变成系统默认行为。

对当前仓库最有价值的吸收路径不是继续复制文件名，而是：

1. 用 ECC 的模块边界组织能力。
2. 用 superpowers 的完成门禁、反合理化语言和独立 reviewer 节奏补强关键环节。
3. 用 OMO 的系统提醒思路指导 future references / nanospec 验收模板设计。
