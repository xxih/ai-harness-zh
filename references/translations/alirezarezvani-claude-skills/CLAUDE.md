# CLAUDE.md

这个文件为 Claude Code（claude.ai/code）在处理本仓库内容时提供指引。

## 项目目的

这是一个**综合性的 skills 资料库**，面向 Claude AI 与 Claude Code，提供可复用、可用于生产环境的 skill 包，把领域专业知识、最佳实践、分析工具与战略框架封装到一起。团队可以直接下载这些模块化 skill 并纳入自己的工作流。

**当前范围：** 9 个 domain 下的 205 个可用于生产环境的 skill、268 个 Python 自动化工具、384 份参考指南、16 个 agents 与 19 个 slash commands。

**关键区别：** 这**不是**传统应用，而是一个 skill package 库，目标是让用户把它们抽取并部署到自己的 Claude 工作流中。

## 导航图

本仓库采用**模块化文档**。如果需要某个 domain 的具体指导，请看：

| Domain | CLAUDE.md 位置 | 关注点 |
|--------|----------------|--------|
| **Agent Development** | [agents/CLAUDE.md](agents/CLAUDE.md) | `cs-*` agent 创建、YAML frontmatter、相对路径 |
| **Marketing Skills** | [marketing-skill/CLAUDE.md](marketing-skill/CLAUDE.md) | 内容创作、SEO、ASO、需求增长、活动分析 |
| **Product Team** | [product-team/CLAUDE.md](product-team/CLAUDE.md) | RICE、OKR、user stories、UX 研究、SaaS scaffolding |
| **Engineering (Core)** | [engineering-team/CLAUDE.md](engineering-team/CLAUDE.md) | 全栈、AI/ML、DevOps、安全、数据、QA 工具 |
| **Engineering (POWERFUL)** | [engineering/](engineering/) | Agent 设计、RAG、MCP、CI/CD、数据库、可观测性 |
| **C-Level Advisory** | [c-level-advisor/CLAUDE.md](c-level-advisor/CLAUDE.md) | CEO/CTO 级战略决策 |
| **Project Management** | [project-management/CLAUDE.md](project-management/CLAUDE.md) | Atlassian MCP、Jira/Confluence 集成 |
| **RA/QM Compliance** | [ra-qm-team/CLAUDE.md](ra-qm-team/CLAUDE.md) | ISO 13485、MDR、FDA、GDPR、ISO 27001 合规 |
| **Business & Growth** | [business-growth/CLAUDE.md](business-growth/CLAUDE.md) | 客户成功、售前工程、Revenue Operations |
| **Finance** | [finance/CLAUDE.md](finance/CLAUDE.md) | 财务分析、DCF 估值、预算、预测、SaaS 指标 |
| **Standards Library** | [standards/CLAUDE.md](standards/CLAUDE.md) | 沟通、质量、git、安全标准 |
| **Templates** | [templates/CLAUDE.md](templates/CLAUDE.md) | 模板系统用法 |

## 架构总览

### 仓库结构

```text
claude-code-skills/
├── .claude-plugin/            # Plugin registry（marketplace.json）
├── agents/                    # 16 个跨 domain 的 cs-* 前缀 agents
├── commands/                  # 19 个 slash commands（changelog、tdd、saas-health、prd、code-to-prd、plugin-audit、sprint-plan 等）
├── engineering-team/          # 26 个核心工程 skills + Playwright Pro + Self-Improving Agent + A11y Audit
├── engineering/               # 30 个 POWERFUL-tier 高级 skills（含 AgentHub）
├── product-team/              # 13 个产品 skills + Python tools
├── marketing-skill/           # 43 个营销 skills（7 个 pod）+ Python tools
├── c-level-advisor/           # 28 个 C-level 咨询 skills（10 个角色 + orchestration）
├── project-management/        # 6 个 PM skills + Atlassian MCP
├── ra-qm-team/                # 12 个 RA/QM 合规 skills
├── business-growth/           # 4 个 business & growth skills + Python tools
├── finance/                   # 2 个 finance skills + Python tools
├── eval-workspace/            # Skill 评测结果（Tessl）
├── standards/                 # 5 个 standards library 文件
├── templates/                 # 可复用模板
├── docs/                      # MkDocs Material 文档站
├── scripts/                   # 构建脚本（文档生成）
└── documentation/             # 实施计划、sprints、交付资料
```

### Skill Package 模式

每个 skill 都遵循下列结构：

```text
skill-name/
├── SKILL.md              # 主文档
├── scripts/              # Python CLI 工具（无 ML/LLM 调用）
├── references/           # 专家知识库
└── assets/               # 面向用户的模板
```

**设计理念：** skill 是自包含 package。每个 package 都带有可执行工具（Python 脚本）、知识库（markdown references）以及用户模板。团队可以直接把某个 skill 文件夹抽出来使用。

**关键模式：** 知识从 `references/` 流入 `SKILL.md` 工作流，再通过 `scripts/` 执行，最后结合 `assets/` 模板落地。

## Git 工作流

**分支策略：** `feature` → `dev` → `main`（仅通过 PR）

**已启用分支保护：** `main` 分支要求 PR 审批，禁止直接 push。

### 快速开始

```bash
# 1. 始终从 dev 开始
git checkout dev
git pull origin dev

# 2. 创建 feature 分支
git checkout -b feature/agents-{name}

# 3. 开发并提交（conventional commits）
feat(agents): implement cs-{agent-name}
fix(tool): correct calculation logic
docs(workflow): update branch strategy

# 4. push 并创建到 dev 的 PR
git push origin feature/agents-{name}
gh pr create --base dev --head feature/agents-{name}

# 5. 审批后，PR 合并到 dev
# 6. 再定期通过 PR 把 dev 合并到 main
```

**分支保护规则：**

- ✅ Main：必须经 PR 审批，禁止直接 push
- ✅ Dev：未保护，但建议也走 PR
- ✅ All：强制 conventional commits

完整工作流见 [documentation/WORKFLOW.md](documentation/WORKFLOW.md)。  
提交规范见 [standards/git/git-workflow-standards.md](standards/git/git-workflow-standards.md)。

## 开发环境

**不使用 build system 和测试框架**，这是有意为之，目的是保持可移植性。

**Python 脚本约束：**

- 仅使用标准库，尽量减少依赖
- 以 CLI 为先，便于自动化
- 同时支持 JSON 输出和人类可读输出
- 不允许 ML/LLM 调用，保证 skill 可移植且执行快

**如果要增加依赖：**

- 让脚本仍能以最小成本运行（最多 `pip install package` 这一级别）
- 在 `SKILL.md` 里写清全部依赖
- 优先选择标准库实现

## 当前版本

**版本：** `v2.1.2`（最新）

**v2.1.2 亮点：**

- Landing page generator 现在默认输出 **Next.js TSX + Tailwind CSS**（4 种设计风格，7 个 section 生成器）
- **Brand voice integration**：落地页工作流会调用 marketing 的 brand voice analyzer，让文案语气与设计风格匹配
- 修复了跨多个 domain 的 25 个 Python 脚本问题（语法、依赖、`argparse`）
- `237/237` 个脚本已验证 `--help` 可正常运行
- 修复了 competitive teardown 的 `SKILL.md`（6 个失效文件引用）
- 补齐 product 与 marketing skill 之间的跨域工作流文档

**v2.1.1（2026-03-07）：**

- 通过 Tessl 质量评审，把 18 个 skill 从 66-83% 优化到 85-100%
- 为全部 `SKILL.md` 增加 YAML frontmatter（`name` + `description`）
- 新增 6 个 agents、5 个 slash commands、Gemini CLI 支持，以及 MkDocs 文档站

**v2.0.0（2026-02-16）：**

- 新增 25 个 POWERFUL-tier engineering skills（`engineering/`）
- 增加 plugin marketplace 基础设施（`.claude-plugin/marketplace.json`）
- 多平台支持：Claude Code、OpenAI Codex、OpenClaw

历史交付见 [documentation/delivery/](documentation/delivery/) 与 [CHANGELOG.md](CHANGELOG.md)。

## 路线图

**Phase 1-2 已完成：** 9 个 domain 共部署 204 个可用于生产环境的 skills

- Engineering Core（26）、Engineering POWERFUL（30）、Product（14）、Marketing（43）、PM（6）、C-Level（28）、RA/QM（12）、Business & Growth（4）、Finance（2）
- 268 个 Python 自动化工具、384 份参考指南、16 个 agents、19 个 commands
- 从工程、法规合规一路覆盖到销售、客户成功与财务的完整企业场景
- MkDocs Material 文档站，收录 210+ 页面并支持 SEO

更具体的 roadmap 可见各 skill 文件夹下的 `README.md` 或 roadmap 文件。

## 核心原则

1. **Skills are products**：每个 skill 都应可作为独立 package 部署
2. **Documentation-driven**：成败取决于文档是否清晰、可执行
3. **Algorithm over AI**：优先用确定性分析（代码），而不是 LLM 调用
4. **Template-heavy**：尽量提供即拿即用、可定制的模板
5. **Platform-specific**：平台特定的最佳实践优先于泛泛建议

## ClawHub 发布约束

本仓库把 skills 发布到 **ClawHub**（clawhub.com）作为分发注册表。以下规则**不可协商**：

1. **`cs-` 前缀仅用于 slug 冲突。** 只有在 ClawHub 上某个 slug 已被其他发布者占用时，才使用 `cs-` 前缀（例如 `cs-copywriting`、`cs-seo-audit`）。该前缀**只在 ClawHub 注册表内使用**，仓库文件夹名、本地 skill 名称以及 Claude Code、Codex、Gemini CLI 等其他工具中的名称都保持不变。
2. **不要为了匹配 ClawHub slug 而重命名仓库文件夹或本地 skill 名称。** 仓库才是唯一事实来源。
3. **不得依赖付费/商业服务。** 除非由项目本身提供，skill 不得要求付费第三方 API key 或商业服务。可接受免费层 API 与 BYOK（bring-your-own-key）模式。
4. **速率限制：** ClawHub 每小时最多发布 5 个新 skill。批量发布必须遵守这一点，使用 drip timer（`clawhub-drip.timer`）进行分批操作。
5. **`plugin.json` schema：** 只允许这些字段：`name`、`description`、`version`、`author`、`homepage`、`repository`、`license`、`skills: "./"`。不能加额外字段。
6. **版本跟随仓库版本。** ClawHub package 版本必须与仓库 release 版本一致（当前为 `v2.1.2+`）。

## 需要避免的反模式

- 在 skill 之间制造依赖关系，应保持每个 skill 自包含
- 增加复杂的 build system 或测试框架，破坏简洁性
- 给出泛泛建议，而不是具体、可执行的框架
- 在脚本里调用 LLM，破坏可移植性和速度
- 过度描述文件结构，skill 本身应尽量保持简单

## 与本仓库协作时

**创建新 skill：** 按对应 domain 的 roadmap 与 `CLAUDE.md` 指南执行。

**编辑已有 skill：** 保持 markdown 文件之间的一致性，沿用相同的语气、格式与结构模式。

**质量标准：** 每个 skill 都应帮助用户节省 40% 以上时间，并把一致性/质量提升 30% 以上。

## 其他资源

- **`.gitignore`：** 排除了 `.vscode/`、`.DS_Store`、`AGENTS.md`、`PROMPTS.md`、`.env*`
- **Plugin Registry：** [.claude-plugin/marketplace.json](.claude-plugin/marketplace.json) - marketplace 分发注册表
- **Standards Library：** [standards/](standards/) - 沟通、质量、git、文档、安全标准
- **Implementation Plans：** [documentation/implementation/](documentation/implementation/)
- **Sprint Delivery：** [documentation/delivery/](documentation/delivery/)

---

**Last Updated:** March 11, 2026  
**Version:** v2.1.2  
**Status:** 9 个 domain 下已部署 205 个 skills、28 个 marketplace plugins，文档站已上线
