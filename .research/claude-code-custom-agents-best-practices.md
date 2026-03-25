# Claude Code 自定义 Agent 最佳实践调研

检查时间：2026-03-23

## 1. 调研问题

回答两个具体问题：

1. Claude Code 官方对自定义 subagent / agent 的最佳实践怎么说。
2. 像 ECC 那样，在 `agents/*.md` 里写比较详细的流程、检查清单和输出格式，是否算好实践。

本文默认讨论的是 Claude Code 的自定义 subagent，不泛化到其他 agent harness。

## 2. 结论先行

先给结论：

1. Claude Code 官方并不鼓励把 agent 写成一句抽象人设；相反，官方明确鼓励写**聚焦职责、描述清晰、提示详细、工具受限**的 subagent。
2. 因此，像 ECC 那样在 agent 文件里写详细流程，**本身不是坏实践**。
3. 但详细不等于无限膨胀。agent 文件更适合承载：
   - 角色边界
   - 触发时机
   - 核心工作流程
   - 输出格式
   - 权限边界
4. 如果内容已经变成大段参考资料、团队百科、长案例集、模板库或只在部分任务才需要的细节，更适合拆到 `skills/` 的 supporting files，而不是继续塞进 agent body。
5. Claude Code 现在**支持**在 agent frontmatter 里用 `skills:` 显式预加载 skill，而且 subagent **不会继承**父对话里已经激活的 skills；要稳定可用，就应显式列出。

## 3. 官方能力与最佳实践

### 3.1 subagent 是什么

Claude Code 官方将 subagent 定义为：

- 面向特定任务类型的专用助手
- 每个 subagent 都有独立上下文窗口
- 有自己的 system prompt
- 有独立的工具权限和权限模式

这意味着 agent prompt 不是可有可无的标签，而是这个角色真正的运行定义。

官方文档：

- https://code.claude.com/docs/en/sub-agents

### 3.2 官方明确给出的 agent 写法建议

Claude Code 官方在 subagent 示例页给出的最佳实践包括：

- 设计聚焦的 subagent，每个 subagent 只擅长一个具体任务
- 写详细 description，因为 Claude 依靠 description 判断何时委派
- 限制工具访问，只给必要权限
- 把项目级 subagent 纳入版本控制

官方还特别指出，示例里的 `code-reviewer` 是一个“带详细 prompt 的 focused subagent”，并说明这个 prompt 会明确规定：

- 要检查什么
- 按什么顺序工作
- 输出应该如何组织

这说明官方认可的不是“短 prompt”，而是“聚焦但足够具体的 prompt”。

官方参考：

- https://code.claude.com/docs/en/sub-agents

### 3.3 为什么详细 prompt 合理

官方文档同时说明：

- subagent 运行在自己的上下文窗口里
- 依靠自己的 custom system prompt 工作
- Claude 会根据 agent 的 description 决定是否委派

所以如果 agent prompt 太空：

- Claude 不容易判断何时调用它
- 被调用后也缺少稳定执行框架
- 输出格式和质量门槛容易漂移

对于 reviewer、planner、debugger 这类角色，写明确步骤、检查项和输出格式，属于顺着官方能力设计，而不是逆着设计。

## 4. `skills` 与 agent 的关系

### 4.1 Claude Code 是否支持在 agent 中显式声明 skill

支持。

Claude Code 的 subagent frontmatter 支持 `skills` 字段。官方说明：

- `skills` 会在 subagent 启动时把 skill 内容直接注入其上下文
- 这样 subagent 不需要在执行过程中再发现并加载 skill
- 注入的是 skill 的完整内容，不只是“可调用入口”

更关键的一条是：

- subagent **不会继承**父对话中的 skills，必须在 agent 里显式列出

官方参考：

- https://code.claude.com/docs/en/sub-agents

### 4.2 显式列 `skills:` 是否更好

通常是，但有前提。

更适合显式列 `skills:` 的情况：

- 这是该 agent 每次执行都稳定需要的领域约定
- 这些内容是角色默认知识，而不是偶尔才会用到的参考资料
- 不显式列出会导致行为漂移或遗漏关键规范

不适合大量预加载的情况：

- skill 很长
- 只有少数任务才会相关
- 本质上更像参考手册或模板库

原因也很直接：官方明确说明 `skills:` 会把完整 skill 内容注入 subagent 上下文，预加载过多会增加上下文负担。

## 5. skill 为什么仍然重要

Claude Code 官方对 skills 的定位是：

- 扩展 Claude 的 task-specific expertise 和 workflows
- 在相关时自动加载，或由用户显式调用
- 可以带 supporting files，把长参考资料、案例、脚本放在 skill 目录里

官方还建议：

- `SKILL.md` 保持聚焦
- 大段参考资料移到 supporting files
- `SKILL.md` 控制在 500 行以内

这说明官方理想分层不是“所有流程都写进 agent”，而是：

- agent 负责定义角色如何工作
- skill 负责提供任务知识、工作流和可按需加载的支持材料

官方参考：

- https://code.claude.com/docs/en/skills

## 6. 对 ECC 写法的判断

## 6.1 为什么 ECC 风格不违背官方建议

从当前仓库镜像的 ECC 资料看，像下面这些 agent 都偏长：

- [planner.md](/Users/xxih/workspace/my-ai-harness/references/translations/everything-claude-code/docs/zh-CN/agents/planner.md)
- [code-reviewer.md](/Users/xxih/workspace/my-ai-harness/references/translations/everything-claude-code/docs/zh-CN/agents/code-reviewer.md)
- [architect.md](/Users/xxih/workspace/my-ai-harness/references/translations/everything-claude-code/docs/zh-CN/agents/architect.md)

这些文件通常包含：

- 明确角色定义
- 分阶段流程
- 检查清单
- 输出模板
- 风险和门禁标准

这种写法和 Claude Code 官方示例是同方向的，不应仅因为“长”就判定为反模式。

## 6.2 ECC 真正值得借鉴的不是“长”，而是“长得有边界”

ECC 更有价值的地方在于：

- agent 多数仍然按角色聚焦，而不是万能代理
- 长流程通常服务于该角色的固定工作方式
- 任务型细节并没有全部塞进 agent，本体外还有大量 skills 承载工作流和参考材料

在当前镜像里，ECC 的规模也说明了这一点：

- `agents/` 大约 18 个 Markdown 文件
- `skills/` 大约 94 个 `SKILL.md`

也就是说，它不是“只有 agent，没有 skill”；而是 agent 与 skill 分层并存，只是 agent prompt 仍然写得比较重。

## 6.3 什么时候 ECC 风格会变坏

下面这些情况，就不再是好实践：

- 一个 agent 同时承担 planner、reviewer、implementer、release manager 等多种职责
- 每个 agent 都重复抄一遍项目通用规则
- 把长篇 API 文档、案例库、模板库直接塞进 agent body
- agent 文件越来越像一本总操作手册，而不是单一角色定义

问题不在“详细”，而在“职责混装”和“上下文常驻过载”。

## 7. 推荐分层

推荐把 Claude Code 自定义 agent 资产分成三层：

### 7.1 agent 文件负责什么

适合放进 agent body：

- 角色定义
- 适用场景
- 触发时机
- 工作步骤
- 检查清单
- 输出格式
- 工具与权限边界

一句话：回答“这个角色应该怎么工作”。

### 7.2 `skills:` 适合挂什么

适合通过 `skills:` 预加载的内容：

- 该角色默认必需的团队约定
- 稳定的领域规范
- 反复要用到的实现模式

一句话：回答“这个角色默认就该知道什么”。

### 7.3 skill 本体和 supporting files 负责什么

更适合放到 skill 或 supporting files：

- 详细流程手册
- 大段参考文档
- 长案例集
- 模板集合
- 脚本与辅助文件

一句话：回答“遇到这类任务时有哪些可复用知识和材料可以按需读取”。

## 8. 一个实用判断标准

设计自定义 agent 时，可以用下面这组问题快速判断内容应该放哪：

1. 这是这个角色每次都要知道的吗？
   - 是：优先考虑 agent body 或 `skills:`
   - 否：优先放 skill supporting files
2. 这是在定义角色行为，还是在堆参考资料？
   - 定义行为：放 agent
   - 参考资料：放 skill
3. 这是团队/项目的共享规则，还是某个角色的独有流程？
   - 共享规则：优先放 `CLAUDE.md` / 项目规则
   - 独有流程：放 agent
4. 如果把这段删掉，agent 还像这个角色吗？
   - 不像：这段可能属于 agent 核心
   - 仍然像：这段更可能属于 skill 或 supporting files

## 9. 推荐做法

综合官方文档与 ECC 参考，推荐采用下面的写法：

1. 先把 agent 定义成单一职责角色。
2. 在 agent 里写清触发 description、核心流程、检查项和输出格式。
3. 只给必要工具，不做无边界授权。
4. 把每次都要用的少量稳定知识通过 `skills:` 显式挂进去。
5. 把长篇资料、模板、案例和辅助脚本留在 skill supporting files。
6. 项目通用规则继续放在 `CLAUDE.md` 或项目级规则文件，不在每个 agent 里重复。

## 10. 不推荐做法

1. 把 agent 写成一句“你是某某专家”，没有步骤、标准和输出要求。
2. 把所有流程和所有规则都塞进一个万能 agent。
3. 假设 subagent 会自动继承父对话里的 skills。
4. 给 agent 预加载过多 skill，导致常驻上下文臃肿。
5. 用 agent body 承载大量本可拆分的参考资料。

## 11. 结论

对 Claude Code 来说，好的自定义 agent 不是“越短越好”，而是“越聚焦越好，并且足够明确”。

因此：

- ECC 那种在 `agents/*.md` 中写详细流程的做法，可以是好实践。
- 真正需要警惕的不是长度，而是职责混装、常驻上下文过重，以及把本应放进 skill 的参考资料硬塞进 agent。
- 在当前 Claude Code 能力下，更优的写法通常是：
  - agent 定义角色行为
  - `skills:` 显式注入默认知识
  - skill supporting files 承载长资料与按需细节

## 12. 参考资料

- Claude Code Docs, Create custom subagents
  - https://code.claude.com/docs/en/sub-agents
- Claude Code Docs, Extend Claude with skills
  - https://code.claude.com/docs/en/skills
- Claude Code Docs, How Claude remembers your project
  - https://code.claude.com/docs/en/memory
- Anthropic Prompting Best Practices, Be clear and direct
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#be-clear-and-direct
