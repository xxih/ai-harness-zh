# OpenCode 集成

OpenCode agents 是保存在 `.opencode/agents/` 中、带 YAML frontmatter 的 `.md` 文件。转换器会把具名颜色映射成十六进制颜色值，并补上 `mode: subagent`，让这些 agents 通过 `@agent-name` 按需调用，而不是挤进主 agent 选择器。

## 安装

```bash
# 在你的项目根目录执行
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool opencode
```

这会在你的项目目录下创建 `.opencode/agents/<slug>.md` 文件。

## 激活一个 Agent

在 OpenCode 中，用 `@` 前缀调用一个 subagent：

```text
@frontend-developer help build this component.
```

```text
@reality-checker review this PR.
```

也可以直接在 OpenCode UI 的 agent picker 中选择对应 agent。

## Agent 格式

每个生成后的 agent 文件都包含：

```yaml
---
name: Frontend Developer
description: Expert frontend developer specializing in modern web technologies...
mode: subagent
color: "#00FFFF"
---
```

- **mode: subagent**：按需可用，不会出现在主 Tab 轮换列表里
- **color**：十六进制颜色值（源文件中的具名颜色会自动转换）

## 项目级与全局

`.opencode/agents/` 下的 agents 是**项目级**的。若要让它们在所有项目里全局可用，可以把它们复制到 OpenCode 配置目录：

```bash
mkdir -p ~/.config/opencode/agents
cp integrations/opencode/agents/*.md ~/.config/opencode/agents/
```

## 重新生成

```bash
./scripts/convert.sh --tool opencode
```
