# 自动学习 / 积累能力调研

## 1. 研究问题

本次不是问“哪个仓库最自动”，而是问：

1. 三个参考 repo 里，谁真正有“自动学习 / 自动积累”能力。
2. 这些能力是靠 prompt、command、skill、hooks，还是靠更重的运行时。
3. 如果当前仓库不想先上 hooks-heavy 方案，什么能力仍然值得先吸收。

## 2. 结论先行

### 2.1 总判断

- `everything-claude-code` 是三者里唯一把“持续学习”做成显式能力产品面的仓库。
- `superpowers` 更像“把过去失败经验写进 prompt 纪律”，不是自动学习系统。
- `oh-my-opencode` 更像“把执行提醒、状态延续、验证门禁做成系统行为”，不是面向知识沉淀的学习闭环。

### 2.2 对当前仓库的启发

如果当前仓库马上照着 ECC 做，很容易把注意力放到 hooks、observer、项目作用域存储这些重机制上。

但对当前阶段更有价值的，其实是拆开看三种能力：

1. 候选经验从哪里来。
2. 候选经验如何被人快速筛选、改写、升级成可复用资产。
3. 哪些提醒需要自动化，哪些入库动作必须保留人工确认。

## 3. 分仓库证据

### 3.1 everything-claude-code

#### 3.1.1 已有能力

ECC 在 README 中把“Memory Persistence”与“Continuous Learning”直接列成主能力，明确写到：

- `README.md:68` 提到通过 hooks 自动跨 session 保存 / 加载上下文。
- `README.md:69` 提到从 session 自动提取模式，沉淀为可复用 skill。
- `README.md:485-496` 把 `Continuous Learning v2` 定义成 instinct-based learning system，并配套 `/instinct-status`、`/instinct-import`、`/instinct-export`、`/evolve`。

#### 3.1.2 机制形态

ECC v1 的 `skills/continuous-learning/SKILL.md` 写得很直接：

- `SKILL.md:21-25` 明确它通过 `Stop hook` 在 session 结束时评估并抽取模式。
- `SKILL.md:62-78` 给出需要写入用户 settings 的 hook 配置。
- `SKILL.md:108-117` 又进一步说明 v2 的核心提升就是“hooks 做观察，instinct 做原子学习单元”。

ECC v2 则更进一步：

- `continuous-learning-v2/SKILL.md:40-45` 把观察机制升级为 `PreToolUse/PostToolUse`。
- `continuous-learning-v2/SKILL.md:85-123` 说明 hooks 先采集 observation，再由 observer agent 产出 instinct，最后再通过 `/evolve` 聚类成 skills / commands / agents。
- `continuous-learning-v2/SKILL.md:139-187` 明确安装步骤就是先开观察 hooks。

#### 3.1.3 对本题的意义

ECC 证明了“自动学习”这件事确实能做，而且不只是概念。

但它当前的强点和强依赖是绑在一起的：

- 强点：自动观察、项目作用域、置信度、导入导出、进化为高阶资产。
- 强依赖：hooks、observer、用户目录存储、命令体系。

也就是说，ECC 更适合作为“上限参考”，不适合作为当前仓库的第一步原样吸收对象。

### 3.2 superpowers

#### 3.2.1 已有能力

`superpowers` 的核心不在自动学习，而在强工作流纪律：

- `README.md:7-15` 强调 agent 不应直接写代码，而是先澄清、规划、再执行。
- `README.md:101-117` 列出整套基础工作流，重点在 brainstorming、plan、TDD、review、finish。
- `README.md:117` 甚至强调这些 workflow 是 mandatory，不只是建议。

它也依赖 hook 做 bootstrap：

- `hooks/session-start:17-19` 会读取 `using-superpowers` 内容。
- `hooks/session-start:35-59` 会把这段内容注入 session 上下文。
- `docs/README.opencode.md:240-246` 也说明在 OpenCode 里通过 `experimental.chat.system.transform` 自动注入 context。

#### 3.2.2 与“学习 / 积累”有关的部分

superpowers 不是完全没有积累意识，只是它的积累更像“经验被人工固化进 prompt”：

- `skills/verification-before-completion/SKILL.md:110-115` 直接写着这套门禁来自 “24 failure memories”。
- 这说明它有经验回流，但回流方式是把失败教训变成更硬的 skill 文案，而不是自动抽取、自动入库。

另一个弱相关点是：

- `skills/using-superpowers/references/gemini-tools.md:30` 提到 Gemini CLI 有 `save_memory` 工具。

但这只是平台工具映射，不是 superpowers 自己的持续学习机制。

#### 3.2.3 对本题的意义

superpowers 最值得借的不是“自动学习技术栈”，而是：

1. 人工确认前置。
2. 经验必须被改写成高约束、高执行力的 prompt。
3. 不把“自动写入知识库”当成默认正确，而是把“是否值得沉淀”当成一道判断题。

### 3.3 oh-my-opencode

#### 3.3.1 已有能力

`oh-my-opencode` 的重心在系统编排，而不是知识沉淀。

- `src/AGENTS.md:7-18` 表明整个系统是 `createManagers -> createTools -> createHooks -> createPluginInterface` 的插件架构。
- `src/AGENTS.md:31-40` 显示它有 46 个 hooks，覆盖 session、tool guard、continuation、skill reminder 等多个层面。

其中 Atlas 相关 hooks 体现的是“自动提醒”和“状态延续”：

- `src/hooks/atlas/tool-execute-after.ts:57-141` 在 orchestrator 调用 subagent 之后，自动拼接 completion gate、verification reminder、下一步提示。
- `src/hooks/atlas/system-reminder-templates.ts:42-104` 把“subagent 不可信，必须验证”的提醒写成强系统文案。
- `src/hooks/atlas/verification-reminders.ts:75-89` 要求主控回读 notepads 中的 `learnings.md`、`issues.md`、`problems.md`，把 learnings 传给后续任务。

#### 3.3.2 它有无“学习能力”

严格说，它有“局部学习”能力，但没有“资产化学习”闭环：

- 有：在计划执行过程中记录 learnings，并将其传播给后续子任务。
- 没有：把这些 learnings 自动评估、去重、升级成长期 skill / command / eval 资产。

所以它更像“执行期上下文记忆系统”，不是“跨任务的知识沉淀系统”。

#### 3.3.3 对本题的意义

oh-my-opencode 最值得借的是：

1. 把学习记录挂在任务流里，而不是等到最后想起来再总结。
2. 让提醒自动发生，但不让知识自动入库。
3. 让“当前任务 learnings”先服务下一步执行，再决定是否升级为长期资产。

## 4. 能力矩阵

| 能力点 | ECC | superpowers | oh-my-opencode |
| --- | --- | --- | --- |
| 显式连续学习定位 | 强 | 弱 | 弱 |
| 自动观察 session | 强，且依赖 hooks | 弱，主要做 bootstrap | 强，但目标是执行编排 |
| 将经验写成长期资产 | 强 | 中，偏人工写回 skill | 弱，更多停留在 task-level notes |
| 人工审核再入库 | 中 | 强 | 中 |
| hooks 依赖度 | 很高 | 中 | 很高 |
| 适合当前仓库直接吸收 | 中，需大幅裁剪 | 高，方法论层面 | 中，适合借任务内 learnings 机制 |

## 5. “ECC 强依赖 hooks”到底卡在哪里

不是 hooks 本身有问题，而是当前仓库如果直接照搬，会一下子引入四层复杂度：

1. 观察层：何时捕获 session / tool / diff / prompt。
2. 存储层：写到哪里，如何区分全局 / 项目。
3. 评估层：哪些模式值得留下，哪些只是噪音。
4. 演化层：怎么把 observation 升级成 skill / command / eval。

ECC 把这四层做得很完整，所以效果强；但也因此不适合当前仓库直接上。

当前仓库更现实的切法应该是：

- 先做“评估层 + 入库层”。
- 再做“轻观察层”。
- 最后才考虑“hooks 自动观察层”。

## 6. 可选方案

### 方案 A：人工触发的学习卡片

#### 核心思路

每次完成一个非平凡任务后，不自动入库，只由 AI 生成一张“候选学习卡片”，人来决定：

- 丢弃
- 合并进已有资产
- 升级为新 skill / command / eval 线索

#### 输入来源

- 本次 nanospec 任务目录
- `outputs/summary.md`、`acceptance.md`、review 结论
- 相关 diff、失败点、用户纠正

#### 优点

- 最轻，不依赖 hooks。
- 最符合“prompt 优化本来就需要人”的前提。
- 能快速开始积累，不会因为自动化工程量过大而迟迟不上线。

#### 缺点

- 触发频率依赖人。
- 容易遗漏一些本来值得保留的经验。

#### 适用判断

这是当前仓库最稳妥的第一步。

### 方案 B：半自动候选生成 + 人工入库

#### 核心思路

用脚本定期扫描近一段时间的任务产物，自动生成“候选经验列表”，但绝不自动落到正式资产。

AI 负责：

- 聚合候选模式
- 去重
- 生成建议归档位置
- 给出“新建 / 合并 / 放弃”建议

人负责：

- 判断是否真的可复用
- 重写 prompt 文案
- 决定是否补 eval

#### 可借鉴来源

- ECC 的 `/learn-eval`：先检查重叠，再决定 save / absorb / drop。
- ECC 的 `skill-stocktake`：用库存盘点视角治理资产。
- superpowers：强调经验必须被改写成真正能执行的 prompt。

#### 优点

- 自动化程度比方案 A 高很多。
- 不需要 hooks 也能形成稳定节奏。
- 能较早建立“自动学习不是自动发布”的仓库习惯。

#### 缺点

- 需要定义候选来源和扫描节奏。
- 仍需要人工做最后一跳。

#### 适用判断

这是最像“当前阶段最佳平衡点”的方案。

### 方案 C：任务内 learnings 自动传播，长期入库仍人工确认

#### 核心思路

借 oh-my-opencode 的思路，在每个任务容器内维护：

- `learnings.md`
- `issues.md`
- `promote-candidates.md`

执行期间自动提醒回看这些文件，优先把 learnings 用在当前任务的后续步骤。
任务结束后，再统一做人审，决定是否提升为仓库级资产。

#### 优点

- 能让学习发生在任务过程中，而不是事后回忆。
- 能直接改善同一任务里的后续执行质量。
- 长期资产入库仍可保持克制。

#### 缺点

- 对任务容器纪律要求更高。
- 需要在 nanospec 或相关 skill 中补约定。

#### 适用判断

适合作为方案 A / B 的增强层，而不是单独存在。

### 方案 D：仅在 target 层启用“提醒型 hooks”

#### 核心思路

核心仓库保持工具无关；只有在 `targets/` 里，才为支持 hooks 的平台增加“提醒型 hooks”：

- 提醒生成学习卡片
- 提醒回看候选模式
- 提醒在完成前运行学习评估

但 hooks 不直接写正式 skill / command / eval。

#### 优点

- 保留平台增强能力。
- 不污染核心资产层。
- 比 ECC 的全自动观察轻得多。

#### 缺点

- 仍要维护 target-specific 适配。
- 不同平台行为一致性有限。

#### 适用判断

适合第二阶段以后做，不适合现在先上。

## 7. 推荐路径

### 推荐结论

最推荐的路径不是“直接做 ECC 式全自动学习”，而是：

1. 先上方案 B，建立“半自动候选生成 + 人工入库”的主流程。
2. 同时吸收方案 C，把任务内 learnings 记录做起来。
3. 等候选质量和人工筛选标准稳定后，再考虑方案 D 的提醒型 hooks。

### 为什么不是先做全自动

因为当前真正稀缺的不是“采集更多 observation”，而是：

- 哪些经验值得沉淀。
- 如何把经验改写成高质量 prompt 资产。
- 何时应合并进现有资产，而不是继续碎片化。

这些判断恰恰最适合由 AI 辅助、人类拍板。

## 8. 面向当前仓库的最小落地建议

如果要尽快开始，可先只做三件事：

1. 定义一个固定的“学习候选卡”模板。
2. 定义一个“save / absorb / drop”评审流程。
3. 定义一个周期性 stocktake，把候选卡升级为 skill / command / eval，或直接丢弃。

这三件事都不需要 hooks，却已经能让“自动学习 / 积累”开始形成闭环。
