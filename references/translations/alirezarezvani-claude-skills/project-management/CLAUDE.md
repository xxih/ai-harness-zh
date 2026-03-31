# Project Management Skills - Claude Code Guidance

本指南覆盖 6 个可用于生产环境的项目管理 skill、12 个 Python 自动化工具，以及 Atlassian MCP 集成。

## PM Skills 概览

**可用 skills：**

1. **senior-pm/**：组合健康度、风险分析、资源规划（3 个脚本）
2. **scrum-master/**：Sprint 健康、速度预测、retro（3 个脚本）
3. **jira-expert/**：JQL 构造、workflow 校验（2 个脚本）
4. **confluence-expert/**：空间结构、内容审计（2 个脚本）
5. **atlassian-admin/**：权限审计（1 个脚本）
6. **atlassian-templates/**：模板脚手架（1 个脚本）

**工具总数：** 12 个 Python 自动化工具  
**Agent：** `cs-project-manager`（编排这 6 个 skills）  
**Slash Commands：** 3 个（`/sprint-health`、`/project-health`、`/retro`）  
**核心特性：** 通过 Atlassian MCP Server 直接操作 Jira / Confluence

## Atlassian MCP Integration

**用途：** 通过 Model Context Protocol（MCP）直接集成 Jira 和 Confluence

**能力：**

- 创建、读取、更新 Jira issues
- 管理 Confluence 页面与空间
- 自动化 workflows 与 transitions
- 生成报表与 dashboards
- 对 issues 执行批量操作

**Setup：** 在 Claude Code settings 中配置 Atlassian MCP server

**用法模式：**

```bash
# 通过 MCP 操作 Jira
mcp__atlassian__create_issue project="PROJ" summary="New feature" type="Story"

# 通过 MCP 操作 Confluence
mcp__atlassian__create_page space="TEAM" title="Sprint Retrospective"
```

## 各 Skill 的指引

### Senior PM

`senior-pm/`

**关注点：** 项目规划、干系人管理、风险缓解

**关键 workflows：**

- Project charter 创建
- 干系人分析与沟通计划
- Risk register 维护
- 状态汇报与升级

### Scrum Master

`scrum-master/`

**关注点：** 敏捷仪式、团队辅导、障碍移除

**关键 workflows：**

- Sprint planning facilitation
- Daily standup 协调
- Sprint retrospectives
- Backlog refinement

### Jira Expert

`jira-expert/`

**关注点：** Jira 配置、自定义 workflows、自动化规则

**脚本：**

- `scripts/jql_query_builder.py`：把自然语言模式匹配成 JQL
- `scripts/workflow_validator.py`：校验 workflow 定义中的反模式

**关键 workflows：**

- Workflow customization
- Automation rule creation
- Board configuration
- JQL query optimization

### Confluence Expert

`confluence-expert/`

**关注点：** 文档策略、模板、知识管理

**脚本：**

- `scripts/space_structure_generator.py`：根据团队描述生成空间层级
- `scripts/content_audit_analyzer.py`：分析页面清单中的陈旧 / 孤立内容

**关键 workflows：**

- Space architecture design
- Template library creation
- Documentation standards
- Search optimization

### Atlassian Admin

`atlassian-admin/`

**关注点：** 套件管理、用户管理、系统集成

**脚本：**

- `scripts/permission_audit_tool.py`：分析权限方案中的安全缺口

**关键 workflows：**

- 用户开通与权限管理
- SSO / SAML 配置
- App marketplace 管理
- 性能监控

### Atlassian Templates

`atlassian-templates/`

**关注点：** 常见 PM 场景的即用模板

**脚本：**

- `scripts/template_scaffolder.py`：生成 Confluence storage-format XHTML 模板

**可用模板：**

- Sprint planning template
- Retrospective formats（Start-Stop-Continue、4Ls、Mad-Sad-Glad）
- Project charter
- Risk register
- Decision log

## 集成模式

### Pattern 1: Sprint Planning

```bash
# 1. 在 Jira 中创建 sprint（通过 MCP）
mcp__atlassian__create_sprint board="TEAM-board" name="Sprint 23" start="2025-11-06"

# 2. 生成 user stories（集成 product-team）
python ../product-team/agile-product-owner/scripts/user_story_generator.py sprint 30

# 3. 导入 stories 到 Jira
# （手工导入，或通过 Jira API 集成）
```

### Pattern 2: Documentation Workflow

```bash
# 1. 创建 Confluence 页面模板
mcp__atlassian__create_page space="DOCS" title="Feature Spec" template="feature-spec"

# 2. 关联到 Jira epic
mcp__atlassian__link_issue issue="PROJ-123" confluence_page_id="456789"
```

## Python 自动化工具

### New Scripts（Phase 2）

```bash
# 从自然语言生成 JQL
python jira-expert/scripts/jql_query_builder.py "high priority bugs assigned to me"

# 校验 Jira workflow
python jira-expert/scripts/workflow_validator.py workflow.json

# 生成 Confluence 空间结构
python confluence-expert/scripts/space_structure_generator.py team_info.json

# 审计 Confluence 内容健康度
python confluence-expert/scripts/content_audit_analyzer.py pages.json

# 审计 Atlassian 权限
python atlassian-admin/scripts/permission_audit_tool.py permissions.json

# 生成 Confluence 模板
python atlassian-templates/scripts/template_scaffolder.py meeting-notes
```

## Additional Resources

- **Installation Guide:** `INSTALLATION_GUIDE.txt`
- **Implementation Summary:** `IMPLEMENTATION_SUMMARY.md`
- **Real-World Scenario:** `REAL_WORLD_SCENARIO.md`
- **PM Overview:** `README.md`
- **Main Documentation:** `../CLAUDE.md`

---

**Last Updated:** March 9, 2026  
**Skills Deployed:** 6/6 PM skills production-ready  
**Total Tools:** 12 Python automation tools  
**Agent:** cs-project-manager | **Commands:** 3  
**Integration:** Atlassian MCP Server for Jira/Confluence automation
