# Antigravity 集成

将全部 61 个 Agency agents 安装为 Antigravity skills。每个 agent 都会带上 `agency-` 前缀，避免与现有 skills 冲突。

## 安装

```bash
./scripts/install.sh --tool antigravity
```

这会把 `integrations/antigravity/` 中的文件复制到 `~/.gemini/antigravity/skills/`。

## 激活一个 Skill

在 Antigravity 中，用它的 slug 激活某个 agent：

```text
Use the agency-frontend-developer skill to review this component.
```

可用 slug 遵循 `agency-<agent-name>` 模式，例如：

- `agency-frontend-developer`
- `agency-backend-architect`
- `agency-reality-checker`
- `agency-growth-hacker`

## 重新生成

修改 agents 后，重新生成 skill 文件：

```bash
./scripts/convert.sh --tool antigravity
```

## 文件格式

每个 skill 都是一个带有 Antigravity 兼容 frontmatter 的 `SKILL.md` 文件：

```yaml
---
name: agency-frontend-developer
description: Expert frontend developer specializing in...
risk: low
source: community
date_added: '2026-03-08'
---
```
