# Oh My OpenCode 能力拆解

这份文档不是把 `oh-my-opencode` 当成一个“整套产品”来介绍，而是把它拆成可以单独采纳的能力单元。目标读者是假设你准备构建自己的智能体编程体系，只想吸收其中一部分成熟设计，而不是照搬整个工程。

结论先说：`oh-my-opencode` 的价值不在某一个“神级主提示词”，而在于它把编排、上下文治理、失败恢复、外部生态兼容、代码理解工具链和工作流打包成了一套可组合运行时。真正值得借鉴的，是这些能力如何相互配合，而不是 Sisyphus、Atlas、Prometheus 这些名字本身。

本文基于当前仓库源码梳理，重点参考：

- `src/index.ts`
- `src/config/schema.ts`
- `src/agents/*`
- `src/hooks/*`
- `src/tools/*`
- `src/features/*`
- `src/mcp/*`

如果你现在最关心的是“这个仓库到底有哪些能力资产，分别属于什么领域”，可以直接跳到第 9 节和第 10 节；那两节更像分类索引和 prompt 提炼地图。

## 1. 一张能力地图

如果把 `oh-my-opencode` 还原成“能力积木”，大致可以分成 6 层：

| 层级 | 核心问题 | 代表实现 |
|------|----------|----------|
| 角色层 | 不同任务该由谁做 | `src/agents/` |
| 编排层 | 任务如何拆分、委派、并发、续跑 | `src/tools/delegate-task/`、`src/features/background-agent/`、`src/hooks/atlas/` |
| 工具层 | 智能体如何可靠地理解和修改代码 | `src/tools/lsp/`、`src/tools/ast-grep/`、`src/tools/grep/`、`src/tools/glob/` |
| 治理层 | 如何防止跑偏、停摆、上下文爆炸 | `src/hooks/` 下的一组 hook |
| 资产层 | 如何把技能、命令、MCP、外部插件接进来 | `src/features/builtin-skills/`、`src/features/builtin-commands/`、`src/features/claude-code-*` |
| 配置层 | 如何让用户重组这一切 | `src/config/schema.ts` |

如果你是为了构建自己的体系，最值得看的不是 README 里的“这个项目能做什么”，而是这 6 层之间的边界是否清晰。答案是：整体耦合仍然存在，但边界已经足够清楚，适合按模块采纳。

## 2. 最值得借鉴的 10 个能力单元

下面这 10 个能力单元，基本覆盖了这个项目最有价值的部分。

### 2.1 角色分工，不是单大脑

`oh-my-opencode` 不是让一个主模型干所有事，而是把职责拆成几类：

- 主执行/主编排：`sisyphus`、`atlas`
- 规划：`prometheus`、`metis`、`momus`
- 咨询/研究：`oracle`、`librarian`、`explore`
- 多模态：`multimodal-looker`
- 委派执行器：`sisyphus-junior`

这里最值得借鉴的不是 agent 名单，而是“角色即权限与职责边界”。例如：

- `oracle` 被限制为只读咨询，不能直接写代码或继续委派。
- `explore` 和 `librarian` 负责找信息，不负责落地实现。
- `sisyphus-junior` 是执行工蜂，但被禁止继续 `delegate_task`，避免无限套娃。

这是一种很实用的系统设计：不是靠 prompt 说“请专注”，而是直接把工具权限做成物理边界。对自己的体系来说，这个设计比“写一个更聪明的主 prompt”更有复用价值。

适合采纳的点：

- 按职责定义 agent，而不是按模型厂商定义 agent。
- 用工具白名单/黑名单实现边界，而不是只靠提示词。
- 把“研究”和“执行”彻底拆开，避免主执行模型既找资料又改代码。

移植难度：低。

### 2.2 `delegate_task`：把委派做成一级原语

这个项目的中枢不是某个 planner，而是 `delegate_task`。它不是一个“顺手加的子任务功能”，而是系统级原语。

从 `src/tools/delegate-task/tools.ts` 可以看出，它解决的不是单纯“开一个子会话”，而是同时解决 6 件事：

1. 选择执行者：按 `category` 或 `subagent_type`
2. 挂载技能：`load_skills`
3. 继承上下文：`session_id` 可续接已有子任务
4. 拼装系统提示：技能内容和 category prompt append 合并
5. 支持同步/异步：`run_in_background`
6. 产出可追踪结果：返回任务信息，并与后台管理器联动

这意味着 `delegate_task` 不是“prompt 分发器”，而是“任务执行协议”。

如果你要做自己的体系，建议直接照搬这个思路：

- 委派调用必须有结构化参数，而不是只传一段自然语言。
- 会话续跑是一级能力，不要每次都新建子任务。
- skill 挂载要作为调用参数，而不是藏在模型 prompt 里。
- “同步结果”和“后台执行”必须是同一种协议的两种模式。

适合采纳的点：

- 把任务委派抽象成统一 API。
- 把“代理选择、技能选择、执行模式、上下文续接”四件事放进同一调用面。
- 把自然语言 prompt 放在协议内部，而不是让上层系统自己拼接。

移植难度：中。
原因：你需要自己的 session、task、message 体系。

### 2.3 后台执行管理器：让并行成为常态

`src/features/background-agent/manager.ts` 是这个项目最像“运行时内核”的部分之一。它不是简单做一个异步队列，而是围绕后台 agent 生命周期设计了一套小型调度器：

- `launch` 创建后台任务并立即进入队列
- 根据并发 key 做限流
- 为任务新建独立 session
- 轮询消息稳定性判断完成
- 维护任务状态、开始时间、通知和过期清理
- 支持取消、恢复、结果拉取

有几个设计点值得注意：

- 它以“session”为执行容器，而不是裸 prompt 调用。
- 它把并发限制按 provider/model 分组，而不是全局无脑并发。
- 它把“后台任务状态可查询”当成默认能力，不是假设调用方会记住每个结果。

这类设计特别适合你自己的体系，如果你想做：

- 多 agent 并行探索代码库
- 前台主 agent 一边实施，一边等待研究结果
- UI、文档、测试、调试等任务异步运行

适合采纳的点：

- 后台任务应有独立状态机：`pending -> running -> completed/failed/cancelled`
- 并发限制要按模型或 provider 控制
- 必须提供查询接口，而不是只有 fire-and-forget
- 后台结果要能回到主上下文

移植难度：中。

### 2.4 Category + Skill：把“选模型”和“加能力”分开

这是 `oh-my-opencode` 很值得学的一点。

它没有把“一个 agent = 一个固定模型 + 一套固定 prompt”写死，而是拆成：

- Category：定义任务气质和模型配置
- Skill：定义领域知识、流程说明、可附带 MCP

在 `src/config/schema.ts` 和 `src/features/builtin-skills/skills.ts` 里可以看到：

- 内置 category 更像“执行档位”，例如 `quick`、`ultrabrain`、`visual-engineering`、`writing`
- 内置 skill 更像“可插拔专项能力”，例如 `playwright`、`git-master`、`frontend-ui-ux`

这套拆法非常适合你的目标，因为你明确说了要构建属于自己的体系，并且只采纳部分能力。按这个设计，你可以：

- 保留自己的 agent 角色，但直接复用 category 思维
- 不要整个 Sisyphus，只保留 `git-master` 或 `playwright` 这种 skill 机制
- 给不同业务线定义不同 category，而不是复制整个主 prompt

为什么这套设计好用：

- model/temperature/reasoning 是“执行策略”
- skill prompt/MCP/tooling 是“领域能力”
- 两者组合比“预制一堆角色”更灵活

适合采纳的点：

- 用 category 决定模型、思考预算、文本冗长度、工具权限
- 用 skill 决定知识包、工作规范、MCP 装配
- 委派时显式声明 `load_skills`

移植难度：低到中。

### 2.5 代码理解工具链：不是只有 grep

这个项目一个很成熟的地方，是它默认把“结构化代码工具”放到核心工作流里，而不是让 agent 只靠文本搜索。

当前工具层至少包含：

- LSP：定义跳转、引用查找、符号、诊断、rename
- AST-Grep：结构化搜索、结构化替换
- grep/glob：快速文本级扫描
- session 工具：会话历史检索
- interactive bash：交互式终端
- look_at：多模态查看

其中最值得直接采纳的是两件事：

1. LSP 和 AST 工具必须成为一等公民
2. prompt 要明确告诉 agent 什么时候优先用语义工具，什么时候再退回 grep

很多自建系统失败，不是 agent 不够聪明，而是只有“读文件 + 编辑文件 + grep”。`oh-my-opencode` 的做法更接近真正工程系统：

- 导航靠 LSP
- 批量模式识别靠 AST
- 粗搜索靠 grep/glob
- 验证靠 diagnostics

适合采纳的点：

- 重构动作优先绑定 `lsp_rename`
- 代码模式匹配优先绑定 AST，而不是正则
- 把 diagnostics 作为完成前的最低验证线

移植难度：中。
原因：需要你自己接 LSP 或复用现有编辑器/语言服务器生态。

### 2.6 上下文注入：把“项目知识”前置到运行时

这一块常被忽略，但其实很重要。

`oh-my-opencode` 的上下文不是主要依赖长期记忆库，而是通过一组注入器把“当前最相关的项目上下文”塞进会话：

- `directory-agents-injector`
- `directory-readme-injector`
- `context-injector`
- `compaction-context-injector`

从 `src/features/context-injector/injector.ts` 可以看出，它并不是简单附加一段文本，而是：

- 维护 pending context
- 在 `chat.message` 或消息 transform 阶段注入
- 尽量插到最后一条用户消息附近
- 作为 synthetic part 插入，减少 UI 干扰

这背后的设计哲学是：

- 项目知识应该“按目录、按任务、按时机”注入
- 不是所有知识都进向量库
- 与其做全局记忆，不如做局部高相关知识贴片

这对你构建自己的体系很有参考价值，尤其当你的系统跑在代码仓里时：

- `AGENTS.md`/`README.md`/局部规则文件，可以变成天然上下文源
- 注入时机比“存什么”更关键
- compaction 之后的状态恢复，也应该靠结构化注入，而不是期望模型自己记住

适合采纳的点：

- 做目录级上下文收集，而不是只做全仓库摘要
- 让上下文注入与消息生命周期绑定
- 维护一个“待注入上下文缓冲区”，而不是每轮都重新扫描全仓

移植难度：中。

### 2.7 治理型 Hooks：把防跑偏做成系统机制

`src/hooks/` 是整个项目最密集的价值区。这里不是单纯堆功能，而是把“智能体为什么会失败”拆成一堆可拦截的问题：

- 做到一半停了：`todo-continuation-enforcer`
- 工具输出太长：`tool-output-truncator`
- 注释像 AI 写的：`comment-checker`
- 编辑失败后没恢复：`edit-error-recovery`
- 委派失败后没重试：`delegate-task-retry`
- 上下文窗快爆了：`context-window-monitor`
- Anthropic 上下文上限击穿：`anthropic-context-window-limit-recovery`
- 用户请求里隐含模式切换：`keyword-detector`
- 非交互环境行为异常：`non-interactive-env`

其中最值得你直接借鉴的，不是 hook 数量，而是“把失败模式产品化”。

例如 `todo-continuation-enforcer` 的逻辑非常典型：

- 检查 todo 是否未完成
- 检查是否仍有后台任务运行
- 检查 agent 是否有写权限
- 在满足条件时自动注入 continuation prompt

这说明它不是粗暴的“继续继续继续”，而是一个条件受控的恢复器。

`comment-checker` 也一样，不是让模型自查，而是：

- 在写入前记录调用
- 在写入后读取结果
- 调外部 CLI 检查注释
- 再把警告拼回输出

这种设计非常适合自建系统，因为它本质上是一个“运行时治理框架”：

- 失败恢复不应写死在主 prompt
- 质量检查应尽量由外部程序做
- 自愈逻辑应该和工具执行生命周期挂钩

适合优先采纳的 hook 思路：

- 未完成任务自动续跑
- 工具输出截断
- 编辑失败恢复
- 代码风格/注释质量检查
- 上下文窗预警

移植难度：低到中。

### 2.8 Claude Code 兼容层：把外部生态当资产导入

`oh-my-opencode` 不是只做自己的封闭生态，它做了大量兼容层，把 Claude Code 世界里的资产导进来：

- agent loader
- command loader
- skill loader
- MCP loader
- plugin loader
- session state 兼容

特别是 `src/features/claude-code-plugin-loader/loader.ts`，它做的不是一个轻量 parser，而是完整的插件发现与路径解析机制：

- 读取安装数据库
- 读取 Claude settings
- 判断插件是否启用
- 解析插件 manifest
- 发现 commands/agents/skills/hooks/.mcp.json
- 处理 `${CLAUDE_PLUGIN_ROOT}` 一类变量替换

如果你要做自己的体系，这里有一个很实用的启发：

不要只想着“我的系统要定义自己的格式”，要考虑“如何导入别人已经沉淀好的资产”。

这可以直接变成你的架构原则：

- 内部原生协议是一套
- 外部兼容协议是若干 adapter
- adapter 负责把别人的 agent/command/skill/MCP 描述转换成你的内部结构

适合采纳的点：

- 把生态兼容做成 loader，而不是把外部格式散落在业务代码里
- 对命令、技能、MCP 使用统一前端定义，内部再转换
- 支持环境变量展开和路径重写

移植难度：中到高。
原因：这部分和外部产品格式强耦合。

### 2.9 Slash Commands：把复杂流程做成可复用模板

`oh-my-opencode` 的 command 体系不是简单快捷短语，而是“结构化工作流模板”。例如：

- `/init-deep`
- `/ralph-loop`
- `/ulw-loop`
- `/cancel-ralph`
- `/refactor`
- `/start-work`

这些命令的真正价值不是 slash 本身，而是它们把一套复杂行为压缩成稳定触发器：

- 初始化项目知识库
- 启动持续执行循环
- 按 refactor 模板组织上下文和验证
- 从 plan 切入执行态

如果你自己要搭体系，这个设计可以直接借：

- 把高频复杂流程做成命令模板
- 模板里预埋 task structure、must-do、must-not-do、验证流程
- 命令只是入口，真正的价值是 workflow contract

适合采纳的点：

- 不要把复杂工作流留给用户每次口述
- 把“任务模板”做成一类资产，与 skill 平级
- command 可以绑定 agent，也可以只注入模板

移植难度：低。

### 2.10 MCP 与多模态能力：作为外挂，不要嵌死

当前内置 MCP 不算多，但思路是对的：

- `websearch`
- `context7`
- `grep_app`

再加上 skill 自带 MCP，例如 `playwright`。

这说明它并没有把“外部能力”硬编码进主系统，而是把它们看成一类可声明、可启停、可按 skill 装配的外设。

这比“主 agent 直接集成几十个工具”更容易演进。对你的体系来说尤其适合：

- 核心运行时保持小
- 浏览器、搜索、文档、数据库等能力通过 MCP 或类似协议外挂
- skill 决定是否加载某个外部服务

适合采纳的点：

- 外部工具接入协议化
- MCP 和 skill 形成组合关系
- 外部能力默认按需加载，而不是全量常驻

移植难度：低到中。

## 3. 哪些能力最值得优先采纳

如果你不是想复刻 `oh-my-opencode`，而是建设自己的体系，我建议按下面顺序采纳。

### 第一优先级：强烈建议直接借鉴

这几项的投入产出比最高：

| 能力 | 原因 |
|------|------|
| 结构化委派协议 | 没有它，多 agent 很快退化成 prompt 套娃 |
| 后台任务运行时 | 没有它，并行只是口号 |
| Category + Skill 组合 | 能把“模型策略”和“领域能力”解耦 |
| LSP + AST 工具优先 | 直接决定代码修改的可靠性 |
| TODO 续跑与失败恢复 | 直接提高任务完成率 |
| 上下文注入机制 | 比“大而全记忆库”更实用 |

### 第二优先级：有明显价值，但看你的产品目标

| 能力 | 什么时候要 |
|------|-------------|
| Claude Code 兼容层 | 你想复用现有社区资产时 |
| Slash commands 工作流 | 你有重复性复杂流程时 |
| 注释检查器/质量治理 hook | 你很在意代码产物风格一致性时 |
| 多模态查看和 Playwright skill | 你要覆盖浏览器/UI/文档场景时 |

### 第三优先级：建议先理解思想，不必急着照搬

| 能力 | 建议 |
|------|------|
| 完整 agent 宇宙命名体系 | 借角色设计，不必复制命名和 prompt |
| Ralph loop/ulw-loop 这类强流程命令 | 先验证你的主 runtime 稳定性，再决定要不要做 |
| 各种提醒/通知型 hook | 属于体验增强，不是体系核心 |
| 自动更新/启动 toast 一类能力 | 可明显后置 |

## 4. 哪些东西更像“思路”，哪些东西适合“直接复用”

你可以把本项目的能力再分成两类。

### 可以直接复用的

- `delegate_task` 这类结构化委派协议
- category/skill 的抽象
- LSP/AST/grep 组合式工具层
- hook 化的质量治理
- command 模板体系
- 兼容层 loader 的组织方式

### 更适合借鉴思路、不建议直接照搬的

- Sisyphus/Atlas/Prometheus 的完整 prompt 叙事
- 以 OpenCode session API 为核心的具体实现细节
- 与 Claude Code 兼容层深绑定的目录结构
- 一整套默认 agent 名称、人格和文风

原因很简单：前一类是“体系能力”，后一类更像“这个项目自己的产品表达”。

## 5. 如果你构建自己的体系，可以怎么裁剪

下面给一个更偏工程化的裁剪方案。

### 方案 A：做一个轻量但强执行的体系

保留：

- 委派协议
- 后台任务
- LSP/AST 工具
- TODO 续跑
- 上下文注入

先不要：

- 复杂规划 agent
- Claude 兼容层
- 大量命令模板
- 多模态能力

适用场景：你要的是“更可靠地干活”，不是“生态平台”。

### 方案 B：做一个强扩展的 agent 平台

保留：

- category + skill
- command 体系
- MCP 装载
- 外部生态 loader
- 项目级/用户级配置

先不要：

- 太多质量治理 hook
- 太复杂的 planner/reviewer 三段式

适用场景：你更想搭一个别人能接入资产的底座。

### 方案 C：做一个面向代码仓长期运行的自治系统

保留：

- 后台任务运行时
- 续跑与失败恢复
- 上下文压缩恢复
- 项目知识注入
- 命令模板
- 代码质量治理

适用场景：你希望 agent 在复杂仓库里持续跑，不靠人盯着。

## 6. 一个更适合“自建体系”的重构视角

如果我要基于 `oh-my-opencode` 的思想重建一套自己的系统，我会把它重构成下面 5 个核心子系统：

### 6.1 Task Runtime

负责：

- 创建任务
- 子任务委派
- 同步/异步执行
- 状态机
- 会话续接

对应可参考实现：

- `src/tools/delegate-task/`
- `src/features/background-agent/`

### 6.2 Capability Registry

负责：

- 注册 agent
- 注册 category
- 注册 skill
- 注册 command
- 注册 MCP

对应可参考实现：

- `src/agents/`
- `src/features/builtin-skills/`
- `src/features/builtin-commands/`
- `src/mcp/`

### 6.3 Code Intelligence Layer

负责：

- LSP
- AST
- grep/glob
- diagnostics

对应可参考实现：

- `src/tools/lsp/`
- `src/tools/ast-grep/`
- `src/tools/grep/`
- `src/tools/glob/`

### 6.4 Governance Layer

负责：

- 续跑
- 输出截断
- 编辑恢复
- 注释风格约束
- 上下文窗治理

对应可参考实现：

- `src/hooks/`

### 6.5 Asset Import Layer

负责：

- 导入外部 skills/commands/agents/plugins
- 处理路径、frontmatter、环境变量
- 做兼容协议转换

对应可参考实现：

- `src/features/claude-code-*`

这个拆法比“先设计主 agent，再给它加工具”更稳。因为它从一开始就是运行时视角，而不是 prompt 视角。

## 7. 我对这个项目的核心判断

如果把所有表层包装去掉，`oh-my-opencode` 最值得学的是 4 个判断：

1. 智能体编程系统的核心不是单模型能力，而是任务运行时。
2. prompt 只能定义倾向，真正的边界要靠工具权限、生命周期 hook 和状态机。
3. 上下文管理不是“多做记忆”，而是“按任务、按目录、按时机注入正确上下文”。
4. 真正能复用的资产不只是 prompt，还有 skill、command、MCP、plugin 和外部兼容 adapter。

反过来说，如果你只是采纳这个项目的 prompt 风格，而不采纳它的：

- 委派协议
- 后台任务运行时
- 代码语义工具
- 治理型 hook
- 资产装载机制

那你采纳到的其实只是它最不稳定、最容易过时的部分。

## 8. 建议你的采纳顺序

如果你接下来真的要开始做自己的体系，我建议按这个顺序实现：

1. 先做任务运行时：委派、会话续接、后台任务、结果回收。
2. 再做代码工具层：LSP、AST、grep/glob、diagnostics。
3. 再做治理层：todo 续跑、失败恢复、输出截断。
4. 然后做 category + skill，把模型策略和能力包分离。
5. 最后再做命令模板、MCP 装载、外部生态兼容。

这是因为前 3 步决定“能不能稳定干活”，后 2 步决定“能不能优雅扩展”。

## 9. 按领域分类的完整能力总表

这一节不再按源码目录讲，而是按“你准备提炼哪一类能力”来归类。这样你在提 prompt 时，不会把运行时代码、命令模板、质量治理和生态兼容这些本来不同层级的东西混在一起。

### 9.1 总览表

| 领域 | 回答的问题 | 主要 prompt 资产 | 主要运行时资产 |
|------|------------|------------------|----------------|
| 自治执行与任务编排 | 任务如何拆分、委派、并行、续跑直到完成 | `sisyphus`、`atlas`、`sisyphus-junior`、`/ralph-loop`、`/ulw-loop`、`/start-work` | `delegate_task`、后台任务管理器、`todo-continuation-enforcer`、`session-recovery` |
| 规划、评审与决策 | 执行前如何先想清楚，执行后如何复核 | `prometheus`、`metis`、`momus`、`oracle` | `prometheus-md-only`、Atlas 的委派矩阵 |
| 研究、搜索与情报检索 | 如何找资料、找实现、找上下文 | `librarian`、`explore`、`oracle` | `grep`、`glob`、`session_*`、`websearch`、`context7`、`grep_app` |
| 代码理解与结构化修改 | 如何更可靠地理解和修改代码 | `/refactor`、`/init-deep`、category prompt append | LSP、AST-Grep、`interactive_bash`、`look_at` |
| 质量与风格治理 | 如何避免 AI 味、半途而废、输出污染 | 各类治理型 hook 中的注入提示 | `comment-checker`、`tool-output-truncator`、`thinking-block-validator`、`edit-error-recovery` |
| 上下文、知识与记忆治理 | 如何把正确上下文在正确时机塞回会话 | `AGENTS.md`、skills、commands、局部规则 | `directory-agents-injector`、`directory-readme-injector`、`context-injector`、`compaction-context-injector` |
| 交互入口与工作流模板 | 用户如何稳定触发复杂流程 | builtin commands、slash command、builtin skills | `auto-slash-command`、`keyword-detector`、`think-mode`、`slashcommand` |
| 前端、视觉与多模态 | UI、设计、浏览器、图片/PDF 等任务怎么处理 | `multimodal-looker`、`frontend-ui-ux`、`playwright`、`visual-engineering`、`artistry` | `look_at`、Playwright MCP、`skill_mcp` |
| 生态兼容与资产导入 | 如何吃进 Claude Code / OpenCode 外部资产 | 外部 commands、skills、agents、MCP 定义 | `claude-code-*` loaders、`opencode-skill-loader`、`skill-mcp-manager` |
| 安装、诊断与运维 | 如何安装、检查、通知、定位环境问题 | CLI 文案和 doctor 提示 | `install`、`doctor`、`run`、`get-local-version`、通知类 hooks |
| 配置、共享基础设施与分发 | 如何统一配置、模型解析、跨平台发布 | category 配置、agent override、skill/command frontmatter | `schema.ts`、`shared/*`、`packages/*`、`script/*`、`dist/` |

### 9.2 自治执行与任务编排

- Agents: `sisyphus`、`atlas`、`sisyphus-junior`
- Hooks: `todo-continuation-enforcer`、`session-recovery`、`empty-task-response-detector`、`delegate-task-retry`、`ralph-loop`、`start-work`、`task-resume-info`、`background-notification`
- Tools: `delegate_task`、`call_omo_agent`、`background_output`、`background_cancel`
- Commands: `/ralph-loop`、`/ulw-loop`、`/cancel-ralph`、`/start-work`
- Features: `src/features/background-agent/`、`src/features/boulder-state/`、`src/features/task-toast-manager/`、`src/features/hook-message-injector/`
- 最值得提炼的 prompt 文件: `src/agents/sisyphus.ts`、`src/agents/atlas.ts`、`src/features/builtin-commands/templates/ralph-loop.ts`、`src/features/builtin-commands/templates/start-work.ts`

### 9.3 规划、评审与决策

- Agents: `prometheus`、`metis`、`momus`、`oracle`
- Hooks: `prometheus-md-only`、`atlas`
- Commands: `/start-work` 负责把 plan 切到执行态
- 关键 prompt 文件: `src/agents/prometheus-prompt.ts`、`src/agents/metis.ts`、`src/agents/momus.ts`、`src/agents/oracle.ts`
- 这一类更像“脑力 prompt 资产”，而不是工具链资产；如果你想提炼“如何想”，这一类优先级很高

### 9.4 研究、搜索与情报检索

- Agents: `librarian`、`explore`、`oracle`
- Hooks: `keyword-detector`、`agent-usage-reminder`
- Tools: `grep`、`glob`、`session_list`、`session_read`、`session_search`、`session_info`、`call_omo_agent`
- MCPs: `websearch`、`context7`、`grep_app`
- 关键 prompt 文件: `src/agents/librarian.ts`、`src/agents/explore.ts`
- 这一类的重点不是“单一强 prompt”，而是“研究 agent + 搜索工具 + MCP”的组合协议

### 9.5 代码理解与结构化修改

- Tools: `lsp_goto_definition`、`lsp_find_references`、`lsp_symbols`、`lsp_diagnostics`、`lsp_prepare_rename`、`lsp_rename`、`ast_grep_search`、`ast_grep_replace`、`interactive_bash`、`look_at`
- Hooks: `interactive-bash-session`、`non-interactive-env`、`edit-error-recovery`
- Commands: `/refactor`、`/init-deep`
- Skills: `git-master` 在这个领域里偏“代码变更治理”和“提交策略”
- Features: `src/tools/lsp/`、`src/tools/ast-grep/`
- 最值得提炼的 prompt 文件: `src/features/builtin-commands/templates/refactor.ts`、`src/features/builtin-commands/templates/init-deep.ts`

### 9.6 质量与风格治理

- Hooks: `comment-checker`、`tool-output-truncator`、`context-window-monitor`、`anthropic-context-window-limit-recovery`、`thinking-block-validator`、`question-label-truncator`、`rules-injector`
- Tools: `lsp_diagnostics`
- Skills: `git-master` 会强行拉高提交粒度和历史整理质量；`frontend-ui-ux` 会拉高前端审美和交互质量
- Features: `src/features/context-injector/` 和 `src/features/hook-message-injector/` 也属于质量治理的底层支撑，因为它们减少上下文失真
- 这类 prompt 大多不是主系统 prompt，而是“约束性、警告性、纠偏性提示”

### 9.7 上下文、知识与记忆治理

- Hooks: `directory-agents-injector`、`directory-readme-injector`、`compaction-context-injector`、`claude-code-hooks`
- Tools: `skill`、`slashcommand`、`session_*`
- Features: `src/features/context-injector/`、`src/features/opencode-skill-loader/`、`src/features/claude-code-session-state/`
- Commands: `/init-deep` 用来生产新的 `AGENTS.md`，因此它既是“文档生成命令”，也是“知识基础设施命令”
- 这一类值得提炼的不是文风，而是“注入协议”: 什么上下文以什么粒度、在什么时机进入 prompt

### 9.8 交互入口与工作流模板

- Commands: `/init-deep`、`/ralph-loop`、`/ulw-loop`、`/cancel-ralph`、`/refactor`、`/start-work`
- Tools: `slashcommand`、`skill`
- Hooks: `auto-slash-command`、`think-mode`、`keyword-detector`
- Features: `src/features/builtin-commands/`、`src/features/builtin-skills/`
- 关键 prompt 文件: 所有 builtin command template，以及 `src/features/builtin-skills/skills.ts`
- 如果你的目标是“把复杂流程压缩成一句触发词”，这一类非常值得直接学

### 9.9 前端、视觉与多模态

- Agents: `multimodal-looker`
- Categories: `visual-engineering`、`artistry`
- Skills: `playwright`、`frontend-ui-ux`
- Tools: `look_at`、`skill_mcp`
- MCP: `playwright` skill 会声明自己的 MCP server
- 关键 prompt 文件: `src/agents/multimodal-looker.ts`、`src/features/builtin-skills/skills.ts`、`src/tools/delegate-task/constants.ts`
- 这一类很适合拆成你自己的“视觉执行档位”，因为这里的 prompt 风格和一般代码 agent 完全不同

### 9.10 生态兼容与资产导入

- Features: `src/features/claude-code-agent-loader/`、`src/features/claude-code-command-loader/`、`src/features/claude-code-mcp-loader/`、`src/features/claude-code-plugin-loader/`、`src/features/opencode-skill-loader/`、`src/features/skill-mcp-manager/`
- Hooks: `claude-code-hooks`
- Tools: `skill`、`skill_mcp`、`slashcommand`
- 这一类的核心资产不是 prompt，而是 adapter 和 loader；它决定你能不能吃进已有生态
- 如果你未来也想接别家的命令/技能体系，这一层必须单独设计，不能让业务逻辑直接耦合外部格式

### 9.11 安装、诊断与运维

- CLI Commands: `install`、`doctor`、`run`、`get-local-version`、`version`
- Hooks: `session-notification`、`background-notification`、`auto-update-checker`
- Features: `src/cli/doctor/`、`src/cli/run/`
- 这一类和 prompt 的关系最弱，但和“整套系统是否能长期用”关系很强

### 9.12 配置、共享基础设施与分发

- Config: `src/config/schema.ts`、`src/config/index.ts`
- Shared: `src/shared/` 下的模型解析、frontmatter、JSONC、权限兼容、路径发现、动态截断、版本比较等工具
- Packaging: `packages/*` 平台二进制、`script/build-schema.ts`、`script/build-binaries.ts`、`dist/`
- 这一类几乎不产出“核心 prompt”，但决定了 prompt 是否能稳定挂到系统里运行

### 9.13 跨领域执行档位: Categories

这不是一个独立目录，但它是 prompt 提炼时非常值得单独抽象的一层。它把“模型/温度/思考强度”从具体 agent 里拆了出来。

| Category | 适用领域 | 当前默认定位 |
|----------|----------|--------------|
| `visual-engineering` | 前端、UI、动画、视觉实现 | 视觉导向执行档位 |
| `ultrabrain` | 深逻辑、架构、复杂分析 | 高推理档位 |
| `artistry` | 高创造性、风格化产出 | 创意档位 |
| `quick` | 小修小补、低成本快速任务 | 轻量执行档位 |
| `unspecified-low` | 不属于其他类、但工作量中低 | 通用低档位 |
| `unspecified-high` | 不属于其他类、但工作量较大 | 通用高档位 |
| `writing` | 文档、说明、技术写作 | 文案/写作档位 |

这一层的关键源码在 `src/tools/delegate-task/constants.ts`。如果你要提炼“可复用的 prompt 框架”，category prompt append 的复用价值非常高。

## 10. 如果你的目标是提炼核心 prompt，建议这样分层抽取

这一节把仓库里的资产按“prompt 密度”而不是“功能”来排序。

### 10.1 第一层: 直接就是 prompt 资产

- 主 agent prompts: `src/agents/sisyphus.ts`、`src/agents/atlas.ts`、`src/agents/prometheus-prompt.ts`、`src/agents/metis.ts`、`src/agents/momus.ts`、`src/agents/oracle.ts`、`src/agents/librarian.ts`、`src/agents/explore.ts`、`src/agents/multimodal-looker.ts`
- 命令模板: `src/features/builtin-commands/templates/refactor.ts`、`src/features/builtin-commands/templates/init-deep.ts`、`src/features/builtin-commands/templates/ralph-loop.ts`、`src/features/builtin-commands/templates/start-work.ts`
- Skills: `src/features/builtin-skills/skills.ts`、`src/features/builtin-skills/git-master/SKILL.md`、`src/features/builtin-skills/frontend-ui-ux/SKILL.md`
- Category prompt append: `src/tools/delegate-task/constants.ts`

这些文件是你提炼“可迁移话术”和“工作协议”的第一优先级。

### 10.2 第二层: prompt 很重要，但它们服务于治理和约束

- `src/hooks/todo-continuation-enforcer.ts`
- `src/hooks/prometheus-md-only/index.ts`
- `src/hooks/comment-checker/`
- `src/hooks/ralph-loop/index.ts`
- `src/hooks/start-work/index.ts`
- `src/hooks/rules-injector/`
- `src/hooks/directory-agents-injector/`
- `src/hooks/directory-readme-injector/`

这些文件的价值不在“人格”，而在“什么时候插一句什么话可以把系统拉回正轨”。

### 10.3 第三层: 几乎不该按 prompt 去学，而该按机制去学

- `src/features/background-agent/`
- `src/tools/delegate-task/`
- `src/tools/lsp/`
- `src/tools/ast-grep/`
- `src/features/skill-mcp-manager/`
- `src/features/claude-code-*`
- `src/shared/*`

这些模块决定系统行为边界、并发模型、工具装配方式和生态兼容方式。它们往往比 prompt 更难替代。

### 10.4 推荐的提炼顺序

1. 先抽 agent system prompt 和 command template，建立你的基础语气和任务协议。
2. 再抽 category prompt append 和 skills，建立你的“领域档位”和“能力包”。
3. 然后再抽治理型 hook 中的注入提示，建立你的自愈和纠偏机制。
4. 最后才回头看 runtime 代码，决定哪些地方需要机制复刻，而不是 prompt 复刻。

### 10.5 现成的中文 prompt 索引

仓库里已经有一套中文拆解稿，可直接当二次阅读入口：

- `docs/reference/core-prompts-zh/01-sisyphus-hephaestus.md`
- `docs/reference/core-prompts-zh/02-prometheus.md`
- `docs/reference/core-prompts-zh/03-atlas.md`
- `docs/reference/core-prompts-zh/04-specialist-reviewers.md`
- `docs/reference/core-prompts-zh/05-research-media-agents.md`
- `docs/reference/core-prompts-zh/06-sisyphus-junior.md`
- `docs/reference/core-prompts-zh/07-hook-system-prompts.md`

如果你下一步就是提炼 prompt，本文件负责“分类与地图”，上面那组文件更适合直接看 prompt 内容。

## 11. 按分类阅读源码时，几个值得注意的现状

这不是 bug 报告，而是为了避免你在“按领域提炼”时被源码现状误导。

- 内置 commands 的源码注册表在 `src/features/builtin-commands/commands.ts` 里实际有 6 个: `init-deep`、`ralph-loop`、`ulw-loop`、`cancel-ralph`、`refactor`、`start-work`。
- 但 `src/config/schema.ts` 里的 `BuiltinCommandNameSchema` 目前只枚举了 `init-deep` 和 `start-work`。所以如果你按 schema 看，会低估 command 资产数量。
- `src/config/schema.ts` 里的 `HookNameSchema` 还保留了 `grep-output-truncator` 和 `startup-toast` 这样的兼容项；当前主入口 `src/index.ts` 并没有把它们作为独立 hook 实例化。
- `startup-toast` 在当前实现里更像一个被 `auto-update-checker` 读取的开关，而不是单独的 hook 模块。
- `src/features/AGENTS.md` 里提到过 `remove-deadcode`，但当前 `src/features/builtin-commands/commands.ts` 里并没有这个 command。做分类时应以实际注册表为准，而不是只看说明文档。

---

如果只用一句话总结：

`oh-my-opencode` 最值得你采纳的，不是它作为一个完整产品的形态，而是它把“多智能体编码”拆成了一套可治理、可扩展、可并发、可续跑的运行时能力集合。
