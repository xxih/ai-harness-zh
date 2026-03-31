# Agent Development Guide

本指南说明如何创建带 **`cs-*` 前缀的 agents**，让它们与本仓库中的 42 个生产级 skill 无缝集成。

## Agent 架构

### 什么是 `cs-*` Agents？

**`cs-*` agents** 是专门的 Claude Code agents，用来编排仓库里现有的 177 个 skills。每个 agent：

- 通过相对路径引用 skills，例如 `../../marketing-skill/`
- 直接执行 skill package 中的 Python 自动化工具
- 遵循既有工作流与模板
- 保持 skill 的可移植性与独立性

**核心原则：** agent 是用来**编排** skills 的，不是替代 skills。skills 仍然要保持自包含和可移植。

### ClawHub 发布约束

当 skills 发布到 **ClawHub**（clawhub.com）时：

- **`cs-` 前缀仅用于 slug 冲突**，只在 ClawHub 注册表上生效；仓库文件夹名和本地 skill 名称都不改
- **不得依赖付费/商业服务**
- **`plugin.json`** 只能包含：`name`、`description`、`version`、`author`、`homepage`、`repository`、`license`、`skills: "./"`
- **速率限制：** 每小时最多发布 5 个新 skill；批量发布使用 drip publishing

### 当前可用的生产级 Agents

**当前共有 16 个 agents：**

| Agent | Domain | Description |
|-------|--------|-------------|
| [cs-content-creator](marketing/cs-content-creator.md) | Marketing | AI 驱动内容创作，兼顾品牌语气与 SEO |
| [cs-demand-gen-specialist](marketing/cs-demand-gen-specialist.md) | Marketing | 需求生成与客户获取 |
| [cs-ceo-advisor](c-level/cs-ceo-advisor.md) | C-Level | CEO 战略顾问 |
| [cs-cto-advisor](c-level/cs-cto-advisor.md) | C-Level | CTO 技术领导顾问 |
| [cs-product-manager](product/cs-product-manager.md) | Product | RICE 优先级与客户发现 |
| [cs-product-strategist](product/cs-product-strategist.md) | Product | 产品战略、OKR 级联、市场定位 |
| [cs-agile-product-owner](product/cs-agile-product-owner.md) | Product | 敏捷产品 ownership 与 backlog 管理 |
| [cs-ux-researcher](product/cs-ux-researcher.md) | Product | UX research、可用性测试、设计洞察 |
| [cs-product-analyst](product/cs-product-analyst.md) | Product | 产品分析、KPI 设计、实验设计 |
| [cs-engineering-lead](engineering-team/cs-engineering-lead.md) | Engineering | 工程团队协作与事故管理 |
| [cs-workspace-admin](engineering-team/cs-workspace-admin.md) | Engineering | 通过 gws CLI 管理 Google Workspace |
| [cs-senior-engineer](engineering/cs-senior-engineer.md) | Engineering | 架构决策、代码评审、CI/CD |
| [cs-growth-strategist](business-growth/cs-growth-strategist.md) | Business | 增长策略与收入优化 |
| [cs-financial-analyst](finance/cs-financial-analyst.md) | Finance | 财务分析、DCF、SaaS 指标 |
| [cs-project-manager](project-management/cs-project-manager.md) | PM | 带 Atlassian 集成的项目管理 |
| [cs-quality-regulatory](ra-qm-team/cs-quality-regulatory.md) | RA/QM | 法规事务与质量管理 |

**可用模板：** [templates/agent-template.md](../templates/agent-template.md)。创建新 agent 时从这里开始。

### Agent 与 Skill 的区别

| Aspect | Agent (`cs-*`) | Skill |
|--------|---------------|-------|
| **目的** | 编排并执行工作流 | 提供工具、知识与模板 |
| **位置** | `agents/domain/` | `domain-skill/skill-name/` |
| **结构** | 单个带 YAML frontmatter 的 `.md` 文件 | `SKILL.md` + `scripts/` + `references/` + `assets/` |
| **集成方式** | 通过 `../../` 引用 skills | 自包含、无依赖 |
| **命名** | `cs-content-creator`、`cs-ceo-advisor` | `content-creator`、`ceo-advisor` |

## Agent 文件结构

### 必需的 YAML Frontmatter

每个 agent 文件都必须以合法的 YAML frontmatter 开头：

```yaml
---
name: cs-agent-name
description: One-line description of what this agent does
skills: skill-folder-name
domain: domain-name
model: sonnet
tools: [Read, Write, Bash, Grep, Glob]
---
```

**字段定义：**

- **name**：带 `cs-` 前缀的 agent 标识，例如 `cs-content-creator`
- **description**：一句话描述 agent 的用途
- **skills**：该 agent 对应的 skill 文件夹，例如 `marketing-skill/content-creator`
- **domain**：domain 分类，例如 `marketing`、`product`、`engineering`、`c-level`、`pm`、`ra-qm`
- **model**：Claude 模型，如 `sonnet`、`opus`、`haiku`
- **tools**：该 agent 可使用的 Claude Code 工具数组

### 必需的 Markdown 章节

在 YAML frontmatter 之后，至少包含这些章节：

1. **Purpose**（2-3 段）
2. **Skill Integration**
   - Skill Location
   - Python Tools
   - Knowledge Bases
   - Templates
3. **Workflows**（至少 3 个 workflow）
4. **Integration Examples**（具体代码/命令示例）
5. **Success Metrics**（如何衡量效果）
6. **Related Agents**（交叉引用）
7. **References**（文档链接）

## 相对路径解析

### 路径模式

所有 skill 引用都使用 `../../` 模式：

```markdown
**Skill Location:** `../../marketing-skill/content-creator/`

### Python Tools

1. **Brand Voice Analyzer**
   - **Path:** `../../marketing-skill/content-creator/scripts/brand_voice_analyzer.py`
   - **Usage:** `python ../../marketing-skill/content-creator/scripts/brand_voice_analyzer.py content.txt`

2. **SEO Optimizer**
   - **Path:** `../../marketing-skill/content-creator/scripts/seo_optimizer.py`
   - **Usage:** `python ../../marketing-skill/content-creator/scripts/seo_optimizer.py article.md "keyword"`
```

### 为什么用 `../../`？

从 agent 所在位置：`agents/marketing/cs-content-creator.md`  
到 skill 所在位置：`marketing-skill/content-creator/`

导航路径是：`agents/marketing/` → `../../`（回到仓库根）→ `marketing-skill/content-creator/`

**务必验证路径能正确解析。**

## Python 工具集成

### 执行模式

agents 直接执行 skill package 中的 Python 工具：

```bash
# 在 agent 上下文中
python ../../marketing-skill/content-creator/scripts/brand_voice_analyzer.py input.txt

# JSON 输出
python ../../marketing-skill/content-creator/scripts/brand_voice_analyzer.py input.txt json

# 带参数
python ../../product-team/product-manager-toolkit/scripts/rice_prioritizer.py features.csv --capacity 20
```

### 工具要求

所有 Python 工具都必须：

- 只依赖标准库，或把最小依赖写清到 `SKILL.md`
- 同时支持 JSON 输出和人类可读输出
- 提供 `--help`
- 正确返回退出码（`0` 成功，`1` 错误）
- 对缺失参数做友好处理

### 错误处理

当 Python 工具执行失败时：

1. 检查文件路径解析
2. 确认输入文件存在
3. 检查 Python 版本兼容性（3.8+）
4. 查看工具的 `--help`
5. 阅读 stderr 中的错误信息

## Workflow 文档写法

### Workflow 结构

每个 workflow 至少包含：

```markdown
### Workflow 1: [Clear Descriptive Name]

**Goal:** One-sentence description

**Steps:**
1. **[Action]** - Description with specific commands/tools
2. **[Action]** - Description with specific commands/tools
3. **[Action]** - Description with specific commands/tools

**Expected Output:** What success looks like

**Time Estimate:** How long this workflow takes

**Example:**
\`\`\`bash
# Concrete example command
python ../../marketing-skill/content-creator/scripts/seo_optimizer.py article.md "primary keyword"
\`\`\`
```

### 最低要求

每个 agent 至少要写 **3 个 workflows**，分别覆盖：

1. 主要使用场景
2. 高级使用场景
3. 集成使用场景

## Agent 模板

创建新 agent 时可以直接套用：

```markdown
---
name: cs-agent-name
description: One-line description
skills: skill-folder-name
domain: domain-name
model: sonnet
tools: [Read, Write, Bash, Grep, Glob]
---

# Agent Name

## Purpose

[2-3 paragraphs describing what this agent does, why it exists, and who it serves]

## Skill Integration
```
