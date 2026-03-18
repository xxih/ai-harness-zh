# agency-agents：直接使用 vs subagent 使用

## 目标

回答两个问题：

1. `agency-agents` 这个库是不是“主要给 subagent 用”的？
2. 直接使用和 subagent 触发，到底有什么区别？

## 结论先行

你的感觉只对了一部分。

更准确的说法是：

- `agency-agents` 的**源资产**不是专门为 subagent 写的，而是**工具无关的 agent prompt 库**
- 这些源资产在不同工具里，会被包装成不同消费方式
- 其中有一部分确实是 subagent / on-demand agent 模式
- 但也有一部分是直接在主会话里按名字激活，根本不是 subagent

所以结论不是：

- “它主要是被 subagent 使用”

而更像：

- “它是一个 agent prompt 资产库，不同工具把它消费成 direct agent、subagent、rule、skill 四类形态”

## 证据从哪里来

这份判断主要来自以下文件：

- `references/repos/agency-agents/README.md`
- `references/repos/agency-agents/scripts/convert.sh`
- `references/repos/agency-agents/scripts/install.sh`
- `references/repos/agency-agents/integrations/*/README.md`

特别关键的信号有两个：

1. README 的默认推荐入口是 Claude Code
   - `Option 1: Use with Claude Code (Recommended)`
2. 只有部分工具的转换格式明确写了 `subagent`
   - 例如 OpenCode 的 `mode: subagent`
   - Qwen 的说明里明确写 `SubAgents`

这说明 subagent 是“部分目标工具下的消费方式”，不是整个仓库唯一的使用模型。

## 先区分：这个仓库的“本体”是什么

`agency-agents` 的本体是各分类目录下的原始 agent Markdown 文件，例如：

- `engineering/engineering-code-reviewer.md`
- `testing/testing-reality-checker.md`
- `specialized/agents-orchestrator.md`

这些文件本身只定义：

- 角色身份
- 工作方式
- checklist
- 输出格式

它们本身并没有强绑定“必须由 subagent 执行”。

也就是说，源资产层面它是：

- agent prompt library

而不是：

- subagent-only library

## 它在不同工具里会变成什么

大致可以分成四类。

## 第一类：直接激活型

代表工具：

- Claude Code
- GitHub Copilot

### 使用方式

在主会话里直接说：

```text
Activate Frontend Developer and help me build a React component.
```

或者：

```text
Use the Reality Checker agent to verify this feature is production-ready.
```

### 机制

- 原始 `.md` agent 文件直接复制到工具的 agent 目录
- 不需要转换成 subagent 特有格式
- 没有额外的 `mode: subagent`

### 这是不是 subagent

通常不算。

因为这里的含义更接近：

- 当前主对话切换到某种 agent persona / role
- 或当前系统从 agent 目录中加载相应角色定义

它不强调“主 agent 委派给另一个独立执行单元”。

## 第二类：subagent / on-demand agent 型

代表工具：

- OpenCode
- Qwen Code
- OpenClaw

其中 OpenCode 和 Qwen 最典型，OpenClaw 也属于“显式 agent 实体”路线。

### OpenCode

`convert.sh` 对 OpenCode 的处理会明确写入：

```yaml
mode: subagent
```

然后安装到：

- `.opencode/agents/<slug>.md`

调用方式是：

```text
@frontend-developer help build this component.
```

这里非常明确是：

- on-demand subagent

### Qwen Code

README 里直接写的是：

- `SubAgents are installed to .qwen/agents/`
- `Or let Qwen auto-delegate based on task context`

这说明它不是简单“按名字扮演一下角色”，而是进入了 Qwen 自己的 subagent 机制。

### OpenClaw

OpenClaw 没写 `mode: subagent`，但它会把每个 agent 转成一个 workspace：

- `SOUL.md`
- `AGENTS.md`
- `IDENTITY.md`

然后通过：

```bash
openclaw agents add <agentId> --workspace <path>
```

注册成 OpenClaw 可调用 agent。

它和 OpenCode 的差别是：

- OpenCode 更像“主会话里按需调用的 subagent prompt”
- OpenClaw 更像“系统里注册了独立 agent 实体”

但两者都比 Claude Code 那种“直接按名字激活”更接近真正的 agent / subagent 体系。

## 第三类：规则注入型

代表工具：

- Cursor
- Aider
- Windsurf

### 这类不是 direct，也不是典型 subagent

它们更像：

- 把 agent prompt 编译成规则文件
- 让主会话在需要时参考这些规则

例如：

- Cursor：每个 agent 变成 `.cursor/rules/<slug>.mdc`
- Aider：所有 agent 汇总进一个 `CONVENTIONS.md`
- Windsurf：所有 agent 汇总进一个 `.windsurfrules`

### 这类的特点

- 不一定真的“切换到一个独立 agent 执行”
- 更像把 agent 作为可引用规则或上下文注入
- 执行主体通常还是当前主助手

所以它既不是纯 direct，也不是典型 subagent，而是：

- rules-based consumption

## 第四类：skill 包装型

代表工具：

- Gemini CLI
- Antigravity

这类把 agent prompt 转成 skill 格式：

- `SKILL.md`
- 或 Gemini extension + skill 目录

调用时通常说：

```text
Use the frontend-developer skill to help me build this UI.
```

这也不是标准意义上的 subagent，更像“能力包 / skill”。

## 所以它“主要”是哪一种

如果按仓库作者的默认入口看，不是 subagent。

因为 README 的第一推荐是：

- Claude Code

而 Claude Code 集成方式是：

- 原始 `.md` 直接复制到 `~/.claude/agents/`
- 在会话里按名字激活

这说明作者并没有把这个仓库只定位成 subagent 库。

但如果按“更 agentic 的目标工具适配”看，subagent / agent registry 路线确实越来越明显：

- OpenCode：明确 `mode: subagent`
- Qwen：明确 `SubAgents`
- OpenClaw：明确注册 agent workspace

所以更准确的判断是：

- 对 Claude/Copilot 这类工具，它更像“直接使用的角色库”
- 对 OpenCode/Qwen/OpenClaw 这类工具，它更像“subagent / agent registry 资产库”

## 直接使用和 subagent 触发，区别到底在哪

这里最关键的差别，不是 prompt 内容本身，而是“执行边界”和“调度方式”。

## 1. 直接使用

### 典型样子

```text
Use the Reality Checker agent to verify this feature.
```

### 本质

- 还是当前主会话在工作
- 只是加载或模仿某个 agent 的角色 prompt
- 上下文、工具权限、会话线程通常仍然属于主助手

### 特点

- 简单
- 切换成本低
- 不一定有显式 delegation
- 不一定有独立状态隔离

## 2. subagent 触发

### 典型样子

```text
@reality-checker review this PR.
```

或者：

- 由系统自动 delegate 给某个 agent
- 或通过 `agentId` 调用注册好的 agent

### 本质

- 主会话不是简单“扮演另一个角色”
- 而是显式调用另一个 agent 实体或 subagent 单元

### 特点

- 角色边界更明确
- 更适合委派、分工、并行或按需调用
- 常常需要工具自己的 agent 注册机制
- 有时会有独立的可见性、配置或生命周期

## 3. 规则注入

### 典型样子

```text
Use the @security-engineer rules to review this code.
```

### 本质

- 主助手仍在执行
- 只是引用某套规则文件
- 更像“给当前助手加一层角色化操作手册”

## 一个更直白的比喻

可以这样理解：

- 直接使用
  - 你让同一个人“戴上另一顶帽子”
- subagent
  - 你真的把任务分派给另一个人
- 规则注入
  - 你给当前这个人塞了一本操作手册

而 `agency-agents` 本身做的，是生产“帽子 / 人员说明书 / 操作手册原稿”，然后由各工具决定用哪种机制消费。

## 为什么这件事容易让人误解

因为这个仓库名字叫 `agents`，而且有很多地方写：

- Activate Agent
- Agents Orchestrator
- SubAgents

很容易让人以为：

- 所有工具里它都一定是“真实 subagent”

但从实现看并不是这样。

实际上它混合了三层语义：

1. prompt 里的“角色扮演”
2. 工具里的“agent / subagent 机制”
3. 规则或 skill 格式的分发包装

这三层在不同工具里并不等价。

## 对你的问题的最短回答

如果只给一句话：

- 不完全正确。`agency-agents` 不是主要给 subagent 用，而是一个可被多种工具消费的 agent prompt 库；只有 OpenCode、Qwen、OpenClaw 这类目标明显偏向 subagent / agent registry 方式，Claude Code、Copilot 更像直接激活，Cursor/Aider/Windsurf 更像规则注入。

## 对当前仓库的启发

这点其实很重要。

因为如果未来我们参考它，不应该问：

- “要不要也做一堆 subagent？”

而应该先问：

- “我们的资产是要被主会话直接调用，还是被独立 subagent 调用，还是作为规则注入？”

这三种消费方式，决定了：

- prompt 怎么写
- frontmatter 要不要扩展
- target adapter 怎么做
- 是否需要 agent registry

## 总结

`agency-agents` 本身更像一个“agent prompt 源资产仓库”，不是单纯的 subagent 仓库。

它在不同工具里分别被消费成：

- 直接激活的 agent
- on-demand subagent
- 注册式 agent workspace
- 规则文件
- skill 文件

所以“direct use”和“subagent trigger”的区别是存在的，而且差别不在 prompt 文案本身，而在工具是否真的给了它独立 agent 执行边界。
