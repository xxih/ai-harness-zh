# agency-agents 具体怎么用

## 目标

回答一个很具体的问题：

`agency-agents` 这个仓库不是“看 README 激活一下就完了”吗？它到底生成了什么 prompt，放在了哪里，为什么某个工具会因此识别到这些 agent？另外，Claude Code、Codex、OpenClaw 分别怎么用？

这份文档只讲“它是怎么生效的”，不讨论它值不值得借鉴。

## 一句话先说清

`agency-agents` 的核心资产其实是仓库根目录各分类下的原始 agent Markdown 文件，例如：

- `engineering/engineering-code-reviewer.md`
- `testing/testing-reality-checker.md`
- `specialized/agents-orchestrator.md`

这些文件才是“源 prompt”。

后面的 `convert.sh` 和 `install.sh` 做的是两件事：

1. `convert.sh`
   - 把“源 prompt”转换成不同工具能吃的格式
   - 输出到 `integrations/<tool>/...`
2. `install.sh`
   - 再把这些转换后的产物复制到对应工具会扫描的位置
   - 这样工具启动时才能发现它们

所以真正的链路是：

`原始 agent .md -> 转换产物 -> 安装到工具目录 -> 工具读取并提供 agent 调用入口`

## 先看原始资产长什么样

以 `engineering/engineering-code-reviewer.md` 为例，它本身就是一份完整 prompt：

- 有 YAML frontmatter：
  - `name`
  - `description`
  - `color`
  - `emoji`
  - `vibe`
- 正文里有角色定义、规则、checklist、输出格式

也就是说，这个文件本身已经足够给某些工具直接用。

例如它的源文件路径是：

- `references/repos/agency-agents/engineering/engineering-code-reviewer.md`

对支持“.md + frontmatter agent 文件”的工具来说，根本不需要再额外“生成 prompt 内容”；直接复制过去就能用。

## 仓库是怎么分类“哪些工具可以直接吃，哪些工具要先转换”的

从 `scripts/install.sh` 和各工具 `integrations/<tool>/README.md` 可以看出，上游大致分成两类：

### 第一类：原始 `.md` 可以直接用

- Claude Code
- GitHub Copilot

特点：

- 不需要 `convert.sh`
- 直接复制原始 agent 文件到工具目录即可

### 第二类：需要先转换成工具特定格式

- OpenCode
- OpenClaw
- Cursor
- Aider
- Windsurf
- Gemini CLI
- Antigravity
- Qwen

特点：

- 先跑 `./scripts/convert.sh --tool <tool>`
- 生成到 `integrations/<tool>/`
- 再跑 `./scripts/install.sh --tool <tool>` 安装

## 例子一：Claude Code 是怎么生效的

这是最简单的一种。

## 生效链路

1. 源 prompt
   - 例如 `engineering/engineering-code-reviewer.md`
2. 安装脚本
   - `install.sh --tool claude-code`
3. 安装位置
   - `~/.claude/agents/`
4. 使用方式
   - 在 Claude Code 会话里直接按名字调用

## 它到底复制了什么

`install.sh` 里的 `install_claude_code()` 逻辑很直接：

- 扫描各分类目录下带 frontmatter 的 `.md`
- 原样复制到 `~/.claude/agents/`

也就是说，对 Claude Code 来说：

- 没有生成新 prompt
- 没有重写正文
- 生效的 prompt 就是原始 `.md` 文件本身

## 具体例子

如果源文件是：

- `references/repos/agency-agents/engineering/engineering-code-reviewer.md`

安装后会变成：

- `~/.claude/agents/engineering-code-reviewer.md`

然后你在 Claude Code 里通过类似下面的话触发：

```text
Use the Code Reviewer agent to review this PR.
```

或者：

```text
Activate Frontend Developer and help me build a React component.
```

## 为什么这样就会生效

因为 Claude Code 会扫描 `~/.claude/agents/` 里的 agent 文件。

只要文件格式符合 Claude Code 的 agent 约定，它就会把这些文件当作可调用 agent。

所以：

- “生效 prompt” = 原始 `.md`
- “使其生效的关键” = 文件被放进了 Claude Code 的 agent 目录

## 例子二：OpenCode 是怎么生效的

OpenCode 不是直接吃原始 agent 文件，而是吃项目内的 `.opencode/agents/*.md`。

## 生效链路

1. 源 prompt
   - `engineering/engineering-code-reviewer.md`
2. 转换
   - `./scripts/convert.sh --tool opencode`
3. 转换产物
   - `integrations/opencode/agents/code-reviewer.md`
4. 安装
   - `./scripts/install.sh --tool opencode`
5. 安装位置
   - 当前项目根目录下的 `.opencode/agents/code-reviewer.md`
6. 使用方式
   - 在 OpenCode 里用 `@code-reviewer`

## 转换时具体做了什么

`convert.sh` 的 `convert_opencode()` 会：

- 读取原始 frontmatter 的 `name`、`description`、`color`
- 把名字转成 slug
- 给 frontmatter 增加：
  - `mode: subagent`
  - 规范化后的 `color: '#RRGGBB'`
- 正文基本保持原样

所以生成物并不是全新 prompt，只是“同一份 prompt 的 OpenCode 包装版”。

## 具体例子

源文件：

- `references/repos/agency-agents/engineering/engineering-code-reviewer.md`

生成后：

- `references/repos/agency-agents/integrations/opencode/agents/code-reviewer.md`

这个生成物的开头是：

```yaml
---
name: Code Reviewer
description: Expert code reviewer who provides constructive, actionable feedback focused on correctness, maintainability, security, and performance — not style preferences.
mode: subagent
color: '#9B59B6'
---
```

然后后面接的正文，仍然是原来的 agent prompt。

## 为什么这样就会生效

因为 OpenCode 会读取项目内的：

- `.opencode/agents/*.md`

而 `mode: subagent` 表示这个 agent 作为按需调用的 subagent 提供，不一定进入默认主 agent 列表。

安装后你会在项目里得到：

- `.opencode/agents/code-reviewer.md`

然后在 OpenCode 中这样调用：

```text
@code-reviewer review this PR.
```

## 这里真正生效的 prompt 是什么

仍然是那份 agent 正文。

只是 OpenCode 需要前面那层 frontmatter 包装，才能把它识别成自己的 subagent。

所以：

- “生效 prompt” = 转换后的 `.opencode/agents/code-reviewer.md`
- “核心内容” = 原始 agent prompt 正文
- “使其生效的关键” = 放到项目根目录 `.opencode/agents/`

## 例子三：OpenClaw 是怎么生效的

OpenClaw 支持，但它吃的不是一整份 `.md agent`，而是 workspace 目录。

## 生效链路

1. 源 prompt
   - `engineering/engineering-code-reviewer.md`
2. 转换
   - `./scripts/convert.sh --tool openclaw`
3. 转换产物
   - `integrations/openclaw/code-reviewer/`
4. 该目录下包含
   - `IDENTITY.md`
   - `SOUL.md`
   - `AGENTS.md`
5. 安装
   - `./scripts/install.sh --tool openclaw`
6. 安装位置
   - `~/.openclaw/agency-agents/code-reviewer/`
7. 注册
   - `openclaw agents add code-reviewer --workspace ~/.openclaw/agency-agents/code-reviewer --non-interactive`
8. 激活
   - 若 gateway 在运行，还需 `openclaw gateway restart`

## 转换时具体做了什么

`convert.sh` 的 `convert_openclaw()` 不再保留“一文件 prompt”，而是把正文按 section 分桶：

- `SOUL.md`
  - 放 persona、communication、critical rules 这类内容
- `AGENTS.md`
  - 放 mission、deliverables、workflow、checklist 这类内容
- `IDENTITY.md`
  - 放标题、emoji、vibe

它的分法是基于标题关键词，而不是人工为每个 agent 单独写三份文件。

## 具体例子

对于 `Code Reviewer`，转换后目录是：

- `references/repos/agency-agents/integrations/openclaw/code-reviewer/`

里面的三个文件分别长这样：

### `IDENTITY.md`

```md
# 👁️ Code Reviewer
Reviews code like a mentor, not a gatekeeper. Every comment teaches something.
```

### `SOUL.md`

这里放：

- `## 🧠 Your Identity & Memory`
- `## 🔧 Critical Rules`
- `## 💬 Communication Style`

也就是“这个 agent 是谁、怎么说话、有哪些边界”。

### `AGENTS.md`

这里放：

- `## 🎯 Your Core Mission`
- `## 📋 Review Checklist`
- `## 📝 Review Comment Format`

也就是“这个 agent 具体做什么、怎么做”。

## 为什么这样就会生效

因为 OpenClaw 的 agent 不是一个单独 `.md` 文件，而是一个 workspace。

它需要：

- identity
- soul
- operational instructions

三部分分开存在。

安装脚本会把这些 workspace 复制到：

- `~/.openclaw/agency-agents/<agent-id>/`

然后再用：

```bash
openclaw agents add <agent-id> --workspace <path> --non-interactive
```

把它注册进 OpenClaw。

如果 gateway 已经启动，还需要：

```bash
openclaw gateway restart
```

这样 OpenClaw 才会重新加载新的 agent。

## 所以 OpenClaw 能不能用

能。

而且这是上游明确支持的目标之一，不是你自己瞎拼出来的。

但要注意，它不是“复制原始 Markdown 就行”，而是：

1. 先转换成 OpenClaw workspace
2. 再安装
3. 再注册
4. 必要时重启 gateway

## Codex 呢

这里要说清楚：`agency-agents` 上游目前没有 Codex 集成。

证据很直接：

- `convert.sh` 支持的工具列表里没有 `codex`
- `install.sh` 支持的工具列表里也没有 `codex`
- `integrations/` 目录也没有 `codex/README.md`

所以你如果问：

> “这个仓库对 Codex 具体生成了什么 prompt，放到了哪里，使得它起作用？”

当前答案是：

- 没有现成答案
- 因为上游根本没做 Codex 适配

## 那 Codex 要怎么用

只能走“手动适配”或者“二次分发”路线。

大概有两种方式：

### 方式 A：手动把某个 agent 当普通 prompt 用

最简单的做法：

- 直接打开某个原始 agent 文件
- 把正文作为系统/角色指令的一部分喂给 Codex

这种方式没有安装目录、没有自动发现机制，纯手工。

### 方式 B：像当前仓库这样做一层 Codex target adapter

当前仓库本身已经有：

- `targets/codex/`

这种结构。

如果要把 `agency-agents` 某些角色接进 Codex，正确方向不是改上游，而是：

1. 选少量高价值 agent
2. 抽到当前仓库的 `src/agents/` 或 `src/skills/`
3. 再通过 `targets/codex/` 的角色注册方式分发给 Codex

也就是说，Codex 可以用，但不是 `agency-agents` 上游开箱即用。

## 三个具体例子汇总

## 例子 A：Claude Code 用 `Code Reviewer`

### 源文件

- `engineering/engineering-code-reviewer.md`

### 安装

```bash
./scripts/install.sh --tool claude-code
```

### 安装后位置

- `~/.claude/agents/engineering-code-reviewer.md`

### 生效 prompt

- 就是这份原始 `.md`

### 触发方式

```text
Use the Code Reviewer agent to review this PR.
```

## 例子 B：OpenCode 用 `Code Reviewer`

### 源文件

- `engineering/engineering-code-reviewer.md`

### 转换

```bash
./scripts/convert.sh --tool opencode
```

### 转换后位置

- `integrations/opencode/agents/code-reviewer.md`

### 安装

```bash
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool opencode
```

### 安装后位置

- `/your/project/.opencode/agents/code-reviewer.md`

### 生效 prompt

- 转换后的 `.opencode/agents/code-reviewer.md`

### 触发方式

```text
@code-reviewer review this PR.
```

## 例子 C：OpenClaw 用 `Code Reviewer`

### 源文件

- `engineering/engineering-code-reviewer.md`

### 转换

```bash
./scripts/convert.sh --tool openclaw
```

### 转换后位置

- `integrations/openclaw/code-reviewer/IDENTITY.md`
- `integrations/openclaw/code-reviewer/SOUL.md`
- `integrations/openclaw/code-reviewer/AGENTS.md`

### 安装

```bash
./scripts/install.sh --tool openclaw
```

### 安装后位置

- `~/.openclaw/agency-agents/code-reviewer/`

### 注册

```bash
openclaw agents add code-reviewer --workspace ~/.openclaw/agency-agents/code-reviewer --non-interactive
openclaw gateway restart
```

### 生效 prompt

- OpenClaw workspace 三件套：
  - `IDENTITY.md`
  - `SOUL.md`
  - `AGENTS.md`

## 最后给一个最简理解框架

如果你以后再看这类仓库，判断“它到底怎么用”，可以只看四件事：

1. 源 prompt 放在哪
2. 有没有转换脚本
3. 转换产物放在哪
4. 工具实际扫描哪个目录

对 `agency-agents` 来说：

- Claude Code
  - 源文件直接安装
- OpenCode
  - 转成 `.opencode/agents/*.md`
- OpenClaw
  - 转成 workspace 三件套
- Codex
  - 上游暂不支持，需要自己做适配

这就是它真正的使用机制。
