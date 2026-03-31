# Templates - Claude Code Guidance

本指南说明 agents、commands 与标准化 workflows 所使用的模板系统。

## 模板目的

**位置：** `templates/`

**用途：** 为所有 domain 提供可复用模板，用于保持 agent 开发、slash command 创建以及 workflow 自动化的一致性。

## 可用模板

### Agent Templates

**位置：** `templates/agent-template.md`（创建后）

**用途：** 作为新建 `cs-*` agents 的起点

**包含内容：**

- YAML frontmatter 结构
- 必需的 markdown 章节
- workflow 文档格式
- 集成示例模式

**适用场景：** 在 `agents/` 目录下创建任意新 agent

### Command Templates

**位置：** `templates/command-template.md`（创建后）

**用途：** 创建新的 slash commands

**包含内容：**

- command 结构
- 参数解析模式
- help 文档格式

**适用场景：** 在 `commands/` 目录下创建 slash commands

### Workflow Templates

**位置：** `templates/workflow-template.md`（创建后）

**用途：** 统一记录各 skill 中的标准 workflows

**包含内容：**

- 分步骤格式
- 预期输出
- 错误处理模式

## 模板使用模式

```bash
# 1. 复制模板
cp templates/agent-template.md agents/domain/cs-new-agent.md

# 2. 按你的 agent 进行定制
vim agents/domain/cs-new-agent.md

# 3. 严格遵循模板结构

# 4. 测试相对路径和集成点

# 5. 用 conventional commit 提交
git commit -m "feat(agents): implement cs-new-agent from template"
```

## 相关文档

- **Agent Development：** `../agents/CLAUDE.md`
- **Standards：** `../standards/CLAUDE.md`
- **Main Documentation：** `../CLAUDE.md`

---

**Last Updated:** November 5, 2025  
**Purpose:** Consistent templates for rapid agent and workflow development
