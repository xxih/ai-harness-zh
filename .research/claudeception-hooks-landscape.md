# claudeception 与 Claude hooks 调研

## 1. 任务目标

- 把 `claudeception` 作为本地参考仓库纳入 `references/repos/`。
- 分析它和当前仓库的交叉、差异与可借鉴点。
- 顺带调研 Claude Code 官方 hooks 机制，判断后续怎么利用。

## 2. 本地落点

- 已 clone 到：`references/repos/claudeception`
- 本地最新提交：`62dbb91d1183a866b5cf40079265c825b2695843`（2026-02-20, `chore: sync local skill updates`）
- 结构非常小：核心只有 `SKILL.md`、`README.md`、`scripts/claudeception-activator.sh`、`resources/skill-template.md`、`examples/*/SKILL.md` 等少量文件。

## 3. claudeception 是什么

### 3.1 仓库定位

`claudeception` 本质上不是一个通用 harness 框架，而是一个 **Claude Code 自我学习 skill repo**：

- 它把“每次任务做完都要判断有没有可提炼知识”写成一个高优先级 meta-skill。
- 一旦发现某次调试、排障、试错、项目约定具有复用价值，就把它写成新的 Claude skill。
- 目标不是记 session note，而是直接产出 **可被未来语义召回的 skill**。

### 3.2 它的核心机制

1. `SKILL.md` 定义一个名为 `claudeception` 的 skill。
2. skill 内部要求 agent：
   - 先搜已有 skill，避免重复创建；
   - 判断本次知识是否可复用、非平凡、具体、已验证；
   - 必要时做 web research；
   - 把结果写成标准 skill 模板。
3. `scripts/claudeception-activator.sh` 通过 `UserPromptSubmit` hook 每次注入提醒：
   - 先完成用户任务；
   - 然后强制评估本次是否值得抽取 skill；
   - 若值得，再调用 `Skill(claudeception)`。

### 3.3 它更像什么

更像：

- “continuous-learning / retrospective-to-skill”的单能力仓库
- 一个可安装、可复制、可直接挂到 Claude Code 的 repo 级 skill 包

而不是：

- 多领域、多资产、多分发目标的源资产工作区
- 工具无关的中台式 prompt 仓库

## 4. 和当前仓库的交叉重合

### 4.1 目标层面的重合

当前仓库与 `claudeception` 在这几件事上明显重合：

1. **都关心知识沉淀，而不是只做一次性对话。**
2. **都强调可复用经验要落盘。**
3. **都重视 skill 作为长期资产，而不是只写零散 note。**
4. **都接受“先研究、再抽象、再沉淀”的工作方式。**

### 4.2 与现有资产的具体对应

- `src/domains/asset-governance/skills/learning-capture/SKILL.md`
  - 和 `claudeception` 最接近，都在回答“这次任务里什么值得记住”。
- `src/domains/asset-governance/skills/writing-skills/`
  - 对应 `claudeception` 里的“把经验整理成正式 skill”的后半段能力。
- `src/domains/workflow/skills/search-first/`
  - 对应 `claudeception` 中“生成 skill 前先检索已有技能、必要时补 web research”的方法。
- `.learned/` / `.research/`
  - 对应它的 session retrospective 与知识整理落点，只是当前仓库默认先记记录，不直接升格为 skill。

## 5. 和当前仓库的不一样

### 5.1 抽象层级不同

当前仓库：

- 是 **工具无关源资产 + 多目标分发** 的工作区；
- 默认先把经验放进 `src/`、`targets/`、`.learned/`、`.research/` 这些分层；
- 明确避免一开始就把平台细节写死。

`claudeception`：

- 是 **明确绑定 Claude Code** 的 repo；
- 默认目标就是往 `.claude/skills/` 里继续生成新 skill；
- 自带 hook 安装说明，直接依赖 Claude 的运行时行为。

### 5.2 沉淀对象不同

当前仓库 `learning-capture`：

- 默认沉淀的是 `rules.md` / `notes.md` 候选；
- 默认动作是“先记为候选，不自动修改正式共享资产”；
- 刻意不依赖 hooks、observer、自动入库。

`claudeception`：

- 默认沉淀对象就是正式 skill；
- 目标是让未来会话通过语义匹配自动加载；
- 倾向于把本次发现直接升级为执行资产。

### 5.3 自动化程度不同

当前仓库：

- 偏手工触发、强分层、低自动化；
- 重点是治理失真风险。

`claudeception`：

- 偏自动提醒、自动回顾、自动提炼；
- 重点是减少“学到了但忘了写下来”的损耗。

### 5.4 repo 形态不同

当前仓库：

- 参考仓库、翻译仓库、源资产、分发适配都在一个 workspace 里。

`claudeception`：

- 整个 repo 只服务一个能力：continuous learning skill。

## 6. 可借鉴的点

### 6.1 最值得借的不是内容，而是产品化边界

`claudeception` 做得最清楚的一点：

- 一个 repo 只讲一个高杠杆能力；
- 安装方式、触发方式、产物格式都非常直接；
- 没有把 skill、hooks、研究背景、示例拆成过度复杂的体系。

这对当前仓库的启发是：

- 某些能力完全可以先做成 **单主题 repo / 单主题 target 包**，而不是一开始就塞回总仓。

### 6.2 提炼门槛写得很清楚

它对“什么值得升格为 skill”定义得比很多仓库都具体：

- 必须非显然
- 必须可复用
- 必须有明确触发条件
- 必须验证过
- 必须先检查是否已有近似 skill

这些判断门槛很适合补到当前仓库后续的：

- `learning-capture` -> `promote-later` 判定标准
- `writing-skills` 的输入筛选标准
- 后续若做“note 升 skill”的路由规则

### 6.3 skill 描述面向召回，而不是面向美观

它反复强调 `description` 要写：

- 具体错误信息
- 具体症状
- 具体框架 / 文件 / 场景
- 具体该在什么情况下触发

这点和 Anthropic 官方 skill discoverability 原则一致，值得直接 adopt 到本仓库所有 skill authoring 规范里。

### 6.4 示例驱动很有效

它的 `examples/*/SKILL.md` 很小，但很有用，因为它们把“抽出来的 skill 到底长什么样”讲清楚了。

当前仓库后续如果要做：

- `learning-capture` -> `skill` 升级流
- `target` 级安装包
- `Claude` 专属 continuous-learning 能力

都很适合保留类似的最小示例集。

## 7. Claude Code hooks 官方机制

以下以 Claude Code 官方 hooks 文档为准。

### 7.1 hooks 能拦什么

官方当前支持的事件包括：

- `PreToolUse`：工具调用前
- `PostToolUse`：工具调用后
- `Notification`：Claude 通知时
- `UserPromptSubmit`：用户 prompt 提交时
- `Stop` / `SubagentStop`：主 agent 或子 agent 停止时
- `PreCompact`：上下文压缩前
- `SessionStart` / `SessionEnd`：会话生命周期
- `PreToolUse` 还能细分成 `canBlock` 型守门点

### 7.2 hook 类型

官方当前支持四类 hook：

- `command`：本地命令
- `prompt`：直接返回一段 prompt 注入
- `agent`：交给一个 agent 做处理
- `http`：调用 HTTP 端点

这意味着 hooks 已经不只是“跑 shell 脚本”，而是一个比较完整的运行时拦截层。

### 7.3 hook 能做什么输出

官方文档里几个关键输出能力：

- 通过 stderr 给提醒
- 在可阻断事件里返回退出码 `2` 来 block
- 通过 JSON 返回 `decision: block` 或 `decision: approve`
- 通过 `hookSpecificOutput.additionalContext` 给 Claude 注入上下文
- 对 `UserPromptSubmit` 可返回 `additionalContext`、`hookSpecificOutput.additionalContext`，以及 `hookSpecificOutput.additionalPrompt`、`updatedInput`

也就是说，hooks 不只是做日志，还能做：

- 守门
- 轻量策略注入
- prompt 改写
- 生命周期记忆拼装

### 7.4 配置层级

官方文档明确说了 hooks 配置可来自：

- 企业策略
- 命令行参数
- 本地项目配置
- 用户全局配置

因此后续如果要做 `targets/claude/`，应该把：

- **共享默认 hooks**
- **项目覆盖**
- **用户级私有 hooks**

分开设计，而不是只给一份硬编码 `settings.json` 片段。

### 7.5 异步能力

官方支持 `async: true`。

这非常适合：

- 背景记录 observation
- 落 session 摘要
- 统计成本
- 做 pattern extraction 候选分析

而不适合：

- 需要同步阻断的质量门禁
- 需要立即反馈修改建议的前置检查

## 8. hooks 机制怎么用更合适

### 8.1 可以按三层利用

#### 第一层：提醒 / 注入

适合 `UserPromptSubmit`、`SessionStart`：

- 注入本仓当前任务规则
- 注入“任务完成后做 learning evaluation”提醒
- 注入当前工作区的默认 workflow 入口说明

这是 `claudeception` 当前已经在做的层。

#### 第二层：观察 / 落盘

适合 `PostToolUse`、`Stop`、`PreCompact`：

- 收集本次工具调用的关键线索
- 在 session 结束或 compact 前整理 observation
- 只写候选记录，不直接升格正式资产

这层最适合当前仓库，因为它和你现在“先记录、后晋升”的治理原则一致。

#### 第三层：守门 / 阻断

适合 `PreToolUse`：

- 禁止高风险命令
- 提醒 / 阻断非预期分发写入
- 阻断违反仓库目录约定的新增文件
- 做最小质量门禁

这层适合后续把仓库规则真正产品化，但要谨慎，避免过度打断。

## 9. 对当前仓库的具体建议

### 9.1 总结判断

对 `claudeception`，当前最合适的决策不是 `adopt`，而是 **adapt**。

原因：

- 它的核心思想很有价值；
- 但它强依赖 Claude Code skill / hook 运行时；
- 当前仓库的核心定位仍是工具无关源资产，不适合直接把整套实现并入 `src/`。

### 9.2 建议吸收路线

1. **先保留为参考仓库**
   - 已完成：`references/repos/claudeception`
2. **吸收“提炼门槛”和“skill 描述写法”**
   - 适合补进 `learning-capture` / `writing-skills` 的规则与模板
3. **若要做 Claude 专属能力，放到 future `targets/claude/`**
   - 不要直接污染工具无关 `src/`
4. **把 hooks 先用于“候选记录”，不要一上来自动生成正式 skill**
   - 先让 hooks 把 observation 写到 `.learned/notes.md` 或任务容器
   - 再由手工或显式 skill 决定是否升级
5. **如果后续真做 continuous-learning 能力，建议拆两层**
   - 核心层：工具无关的 retrospective / promotion criteria
   - 适配层：Claude hooks / settings / shell wrappers

### 9.3 一个更稳的落地形态

如果你后面要“好好利用 hooks”，更建议走这个结构：

- `src/domains/asset-governance/skills/session-retrospective/`
  - 只定义什么该提炼、怎么分类、何时 promote
- `targets/claude/...`
  - 放 `settings.json` 片段、hook 脚本、Claude 专属 skill 安装说明
- `targets/codex/...`
  - 保持手工触发或用工具能力等价替代，不强求 hooks 对齐

这样能同时保住：

- 工具无关核心
- Claude 专属自动化
- 后续跨平台迁移空间

## 10. 本次结论

- `claudeception` 已适合作为 `references/repos/` 里的独立参考仓库保留。
- 它和当前仓库的最大交叉点，是“把任务经验沉淀成长期可复用资产”。
- 最大差异是：你当前仓库偏治理分层、手工晋升；它偏 Claude 运行时绑定、自动晋升。
- 最值得参考的不是“自动生成 skill”本身，而是：
  - 提炼门槛
  - 面向召回的 description 写法
  - 用 hooks 做轻量强制回顾
- 若后续要利用 Claude hooks，建议优先做：
  - `UserPromptSubmit` 提醒注入
  - `Stop` / `PreCompact` 的 observation 落盘
  - `PreToolUse` 的少量高价值守门
- 当前阶段最合适路线：**保留参考 + 抽象规则 + 未来放入 `targets/claude/` 适配，而不是直接并入核心 `src/`。**

## 11. 证据来源

### 本地仓库

- `references/repos/claudeception/README.md`
- `references/repos/claudeception/SKILL.md`
- `references/repos/claudeception/scripts/claudeception-activator.sh`
- `references/repos/claudeception/resources/skill-template.md`
- `src/domains/asset-governance/skills/learning-capture/SKILL.md`
- `src/domains/workflow/skills/search-first/SKILL.md`
- `README.md`

### 官方 / 外部资料

- Claude Code hooks 官方文档：https://docs.claude.com/en/docs/claude-code/hooks
- Anthropic 工程文章：Agent Skills
  - https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
