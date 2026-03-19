# Claudeception

每次你使用 AI coding agent 时，它几乎都要从零开始。你花一小时排查一个隐蔽错误，agent 终于找出原因，会话结束。下次再遇到同一个问题？又得再花一小时。

这个 skill 就是为了解决这件事。当 Claude Code 发现某个不那么显然的知识点（比如调试技巧、绕过方案，或某个项目特有模式）时，它会把这些知识保存成一个新的 skill。下次再出现类似问题时，这个 skill 就能被自动加载。

## 安装

### 第一步：克隆 skill

**用户级（推荐）**

```bash
git clone https://github.com/blader/Claudeception.git ~/.claude/skills/claudeception
```

**项目级**

```bash
git clone https://github.com/blader/Claudeception.git .claude/skills/claudeception
```

### 第二步：设置激活 hook（推荐）

这个 skill 可以通过语义匹配自动激活，但配置 hook 可以确保它在每个会话里都评估一次当前任务是否产出了可提炼知识。

#### 用户级设置（推荐）

1. 创建 hooks 目录并复制脚本：

```bash
mkdir -p ~/.claude/hooks
cp ~/.claude/skills/claudeception/scripts/claudeception-activator.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/claudeception-activator.sh
```

2. 在你的全局 Claude 设置（`~/.claude/settings.json`）里加入 hook：

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "~/.claude/hooks/claudeception-activator.sh"
          }
        ]
      }
    ]
  }
}
```

#### 项目级设置

1. 在项目里创建 hooks 目录并复制脚本：

```bash
mkdir -p .claude/hooks
cp .claude/skills/claudeception/scripts/claudeception-activator.sh .claude/hooks/
chmod +x .claude/hooks/claudeception-activator.sh
```

2. 在项目设置中加入 hook（仓库内的 `.claude/settings.json`）：

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/claudeception-activator.sh"
          }
        ]
      }
    ]
  }
}
```

如果你已经有 `settings.json`，把上面的 `hooks` 配置合并进去即可。

这个 hook 会在每次 prompt 提交时注入一条提醒，让 Claude 评估当前任务是否产出了可提炼的知识。相比单纯依赖语义描述匹配，这种方式能获得更高的激活率。

## 用法

### 自动模式

当 Claude Code 遇到以下情况时，会自动激活这个 skill：
- 刚完成一次调试，并找到了不显然的解决方案
- 通过调查或试错找到了某种 workaround
- 解决了一个根因并不直观的错误
- 通过调查学到了项目特有的模式或配置
- 完成了任何一个需要明显“发现过程”的任务

### 显式模式

触发一次学习复盘：

```
/claudeception
```

或者直接要求提炼 skill：

```
Save what we just learned as a skill
```

### 会提炼什么

并不是每个任务都会产出 skill。只有那些确实经历了发现过程（而不是只是查文档）、未来任务会受益、触发条件清晰、且已经验证有效的知识，才会被提炼出来。

## 研究背景

这个想法来自关于 AI agent skill library 的学术研究。

[Voyager](https://arxiv.org/abs/2305.16291)（Wang et al., 2023）展示了游戏 agent 可以逐步构建可复用 skill library，从而避免重复学习已经掌握的内容。[CASCADE](https://arxiv.org/abs/2512.23880)（2024）提出了 “meta-skills”（用于获取 skill 的 skill），这正是 Claudeception 的方向。[SEAgent](https://arxiv.org/abs/2508.04700)（2025）展示了 agent 可以通过试错学习新的软件环境，这启发了复盘模式。[Reflexion](https://arxiv.org/abs/2303.11366)（Shinn et al., 2023）则说明了自我反思会带来帮助。

能够持久化自己学习成果的 agent，会比每次都从头开始的 agent 表现更好。

## 工作原理

Claude Code 原生就有 skills 系统。启动时，它会先加载 skill 的名称和描述（大约每个 100 token）。在工作过程中，它会把当前上下文和这些描述做匹配，再把相关 skill 的正文加载进来。

但这个检索系统不仅可以“读”，也可以“写”。所以当这个 skill 判断某段知识值得提炼时，它会写出一个新的 skill，并把描述优化成便于未来检索命中的样子。

描述字段非常关键。像 “Helps with database problems” 这种描述几乎匹配不到真正有用的场景；而 “Fix for PrismaClientKnownRequestError in serverless” 则会在有人遇到那个错误时更准确地命中。

关于 skills 架构的更多说明可以看[这里](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)。

## Skill 格式

提炼出的 skill 是带 YAML frontmatter 的 markdown 文件：

```yaml
---
name: prisma-connection-pool-exhaustion
description: |
  Fix for PrismaClientKnownRequestError: Too many database connections 
  in serverless environments (Vercel, AWS Lambda). Use when connection 
  count errors appear after ~5 concurrent requests.
author: Claude Code
version: 1.0.0
date: 2024-01-15
---

# Prisma Connection Pool Exhaustion

## Problem
[What this skill solves]

## Context / Trigger Conditions
[Exact error messages, symptoms, scenarios]

## Solution
[Step-by-step fix]

## Verification
[How to confirm it worked]
```

完整模板见 `resources/skill-template.md`。

## 质量门槛

这个 skill 对提炼对象很挑剔。如果某件事只是查了下文档、只对眼前这一次有用，或者还没有真正验证过，那它就不会创建 skill。判断标准是：六个月后有人再撞上同一个问题，这个 skill 真的会帮上忙吗？如果不会，就不该提炼。

## 示例

示例 skill 在 `examples/` 目录里：

- `nextjs-server-side-error-debugging/`：浏览器控制台不显示的服务端错误
- `prisma-connection-pool-exhaustion/`：serverless 环境下的 “too many connections” 问题
- `typescript-circular-dependency/`：检测并修复 import 循环

## Contributing

欢迎贡献。Fork、修改、提 PR 即可。

## License

MIT
