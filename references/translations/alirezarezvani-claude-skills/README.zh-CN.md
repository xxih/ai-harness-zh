# Claude Code Skills & Plugins

面向各类编码工具的 agent skills 库。

**为 11 种 AI 编码工具提供的 205 个可用于生产环境的 Claude Code skills、plugins 与 agent skills。**

这是目前最完整的开源 Claude Code skills 与 agent plugins 库之一，同时也可用于 OpenAI Codex、Gemini CLI、Cursor 以及另外 7 种编码代理。它把工程、DevOps、营销、合规、C-level 咨询等领域的可复用专业能力打包成可直接使用的资产。

**支持的平台：** Claude Code · OpenAI Codex · Gemini CLI · OpenClaw · Cursor · Aider · Windsurf · Kilo Code · OpenCode · Augment · Antigravity

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/Skills-205-brightgreen?style=for-the-badge)](#skills-overview)
[![Agents](https://img.shields.io/badge/Agents-16-blue?style=for-the-badge)](#agents)
[![Personas](https://img.shields.io/badge/Personas-3-purple?style=for-the-badge)](#personas)
[![Commands](https://img.shields.io/badge/Commands-19-orange?style=for-the-badge)](#commands)
[![Stars](https://img.shields.io/github/stars/alirezarezvani/claude-skills?style=for-the-badge)](https://github.com/alirezarezvani/claude-skills/stargazers)
[![SkillCheck Validated](https://img.shields.io/badge/SkillCheck-Validated-4c1?style=for-the-badge)](https://getskillcheck.com)

> **5,200+ GitHub stars**，也是目前最完整的开源 Claude Code skills 与 agent plugins 资料库之一。

---

## 什么是 Claude Code Skills 与 Agent Plugins？

Claude Code skills，也常被称为 agent skills 或 coding agent plugins，本质上是模块化的指令包，用来给 AI 编码代理补足其默认不具备的领域专业能力。每个 skill 通常包含：

- **SKILL.md**：结构化指令、工作流与决策框架
- **Python tools**：268 个 CLI 脚本，全部只依赖标准库，无需 `pip install`
- **Reference docs**：模板、检查清单与领域知识资料

**一个仓库，覆盖 11 个平台。** 它可以原生作为 Claude Code plugins、Codex agent skills、Gemini CLI skills 使用，也可以通过 `scripts/convert.sh` 转换到另外 8 种工具。全部 268 个 Python 工具都可以在任何支持 Python 的环境中运行。

### Skills、Agents 与 Personas 的区别

| | Skills | Agents | Personas |
|---|---|---|---|
| **作用** | 怎么做一项任务 | 要做什么任务 | 由谁来思考 |
| **范围** | 单一领域 | 单一领域 | 跨领域 |
| **表达风格** | 中性 | 专业 | 人设驱动 |
| **例子** | “按这些步骤做 SEO” | “执行一次安全审计” | “像创业 CTO 一样思考” |

三者可以协同使用。如何组合，请看 [Orchestration](#orchestration)。

---

## 快速安装

### Gemini CLI（新增）

```bash
# Clone 仓库
git clone https://github.com/alirezarezvani/claude-skills.git
cd claude-skills

# 运行安装脚本
./scripts/gemini-install.sh

# 开始使用 skill
> activate_skill(name="senior-architect")
```

### Claude Code（推荐）

```bash
# 添加 marketplace
/plugin marketplace add alirezarezvani/claude-skills

# 按 domain 安装
/plugin install engineering-skills@claude-code-skills          # 24 个核心工程 skill
/plugin install engineering-advanced-skills@claude-code-skills  # 25 个 POWERFUL-tier skill
/plugin install product-skills@claude-code-skills               # 12 个产品 skill
/plugin install marketing-skills@claude-code-skills             # 43 个营销 skill
/plugin install ra-qm-skills@claude-code-skills                 # 12 个法规/质量 skill
/plugin install pm-skills@claude-code-skills                    # 6 个项目管理 skill
/plugin install c-level-skills@claude-code-skills               # 28 个 C-level 顾问 skill
/plugin install business-growth-skills@claude-code-skills       # 4 个业务与增长 skill
/plugin install finance-skills@claude-code-skills               # 2 个财务 skill

# 也可以安装单独的 skill
/plugin install skill-security-auditor@claude-code-skills       # 安全扫描
/plugin install playwright-pro@claude-code-skills               # Playwright 测试工具包
/plugin install self-improving-agent@claude-code-skills         # 自动记忆整理
/plugin install content-creator@claude-code-skills              # 单个 skill
```

### OpenAI Codex

```bash
npx agent-skills-cli add alirezarezvani/claude-skills --agent codex
# 或：git clone + ./scripts/codex-install.sh
```

### OpenClaw

```bash
bash <(curl -s https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/scripts/openclaw-install.sh)
```

### 手动安装

```bash
git clone https://github.com/alirezarezvani/claude-skills.git
# 把任意 skill 文件夹复制到 ~/.claude/skills/（Claude Code）或 ~/.codex/skills/（Codex）
```

---

## 多工具支持（新增）

**一条脚本把全部 156 个 skills 转成 7 种 AI 编码工具格式：**

| Tool | Format | Install |
|------|--------|---------|
| **Cursor** | `.mdc` rules | `./scripts/install.sh --tool cursor --target .` |
| **Aider** | `CONVENTIONS.md` | `./scripts/install.sh --tool aider --target .` |
| **Kilo Code** | `.kilocode/rules/` | `./scripts/install.sh --tool kilocode --target .` |
| **Windsurf** | `.windsurf/skills/` | `./scripts/install.sh --tool windsurf --target .` |
| **OpenCode** | `.opencode/skills/` | `./scripts/install.sh --tool opencode --target .` |
| **Augment** | `.augment/rules/` | `./scripts/install.sh --tool augment --target .` |
| **Antigravity** | `~/.gemini/antigravity/skills/` | `./scripts/install.sh --tool antigravity` |

**工作方式：**

```bash
# 1. 一次性把全部 skills 转成所有工具格式（约 15 秒）
./scripts/convert.sh --tool all

# 2. 安装到你的项目里（会要求确认）
./scripts/install.sh --tool cursor --target /path/to/project

# 或者用 --force 跳过确认：
./scripts/install.sh --tool aider --target . --force

# 3. 验证
find .cursor/rules -name "*.mdc" | wc -l  # 应显示 156
```

**每种工具都会得到：**

- ✅ 全部 156 个 skills 的原生格式转换结果
- ✅ 针对该工具的 README，包含安装、验证、更新说明
- ✅ 对脚本、参考资料、模板的适配支持
- ✅ 无需手工转换

更多细节见 [integrations/](integrations/)。

---

## Skills Overview

**9 个 domain，205 个 skills：**

| Domain | Skills | Highlights | Details |
|--------|--------|------------|---------|
| **🔧 Engineering — Core** | 26 | 架构、前端、后端、全栈、QA、DevOps、SecOps、AI/ML、数据、Playwright、自进化 agent、Google Workspace CLI、a11y 审计 | [engineering-team/](engineering-team/) |
| **🎭 Playwright Pro** | 9+3 | 测试生成、flaky 修复、Cypress/Selenium 迁移、TestRail、BrowserStack、55 个模板 | [engineering-team/playwright-pro](engineering-team/playwright-pro/) |
| **🧠 Self-Improving Agent** | 5+2 | 自动记忆整理、模式提升、skill 提炼、记忆健康检查 | [engineering-team/self-improving-agent](engineering-team/self-improving-agent/) |
| **⚡ Engineering — POWERFUL** | 30 | Agent designer、RAG architect、database designer、CI/CD builder、security auditor、MCP builder、AgentHub、Helm charts、Terraform | [engineering/](engineering/) |
| **🎯 Product** | 14 | 产品经理、敏捷 PO、战略、UX 研究、UI 设计、落地页、SaaS scaffolder、分析、实验设计、discovery、roadmap communicator、code-to-prd | [product-team/](product-team/) |
| **📣 Marketing** | 43 | 7 个 pod：内容（8）、SEO（5）、CRO（6）、渠道（6）、增长（4）、情报（4）、销售（2），另加 context foundation 与 orchestration router。32 个 Python 工具。 | [marketing-skill/](marketing-skill/) |
| **📋 Project Management** | 6 | Senior PM、scrum master、Jira、Confluence、Atlassian admin、templates | [project-management/](project-management/) |
| **🏥 Regulatory & QM** | 12 | ISO 13485、MDR 2017/745、FDA、ISO 27001、GDPR、CAPA、风险管理 | [ra-qm-team/](ra-qm-team/) |
| **💼 C-Level Advisory** | 28 | 完整 C-suite（10 个角色）+ 编排 + 董事会会议 + 文化与协作 | [c-level-advisor/](c-level-advisor/) |
| **📈 Business & Growth** | 4 | 客户成功、售前工程、Revenue Ops、合同与提案 | [business-growth/](business-growth/) |
| **💰 Finance** | 2 | 财务分析师（DCF、预算、预测），SaaS metrics coach（ARR、MRR、流失、LTV、CAC） | [finance/](finance/) |

---

## Personas

预配置的 agent 身份，附带精选的 skill 组合、工作流以及鲜明的沟通风格。Persona 不只是“使用这些 skills”，而是定义 agent 如何思考、如何排序优先级、如何表达。

| Persona | Domain | Best For |
|---------|--------|----------|
| [**Startup CTO**](agents/personas/startup-cto.md) | Engineering + Strategy | 架构决策、技术栈选择、团队搭建、技术尽调 |
| [**Growth Marketer**](agents/personas/growth-marketer.md) | Marketing + Growth | 内容驱动增长、发布策略、渠道优化、低预算营销 |
| [**Solo Founder**](agents/personas/solo-founder.md) | Cross-domain | 一人创业、side project、MVP 搭建、身兼数职 |

**使用方式：**

```bash
# Claude Code
cp agents/personas/startup-cto.md ~/.claude/agents/

# 任意工具
./scripts/convert.sh --tool cursor  # personas 也会一起转换
```

详情见 [agents/personas/](agents/personas/)。如果要自定义 persona，可参考 [TEMPLATE.md](agents/personas/TEMPLATE.md)。

---

## Orchestration

一种轻量协议，用于在跨 domain 工作中协调 personas、skills 与 agents。不依赖框架。

**四种模式：**

| Pattern | What | When |
|---------|------|------|
| **Solo Sprint** | 在项目不同阶段切换 persona | Side project、MVP、solo founder |
| **Domain Deep-Dive** | 一个 persona 叠加多个 skills | 架构审查、合规审计 |
| **Multi-Agent Handoff** | 不同 persona 互相评审彼此输出 | 高风险决策、发布 readiness |
| **Skill Chain** | 按顺序串联 skills，不一定需要 persona | 内容流水线、可复用检查清单 |

**示例：6 周产品发布**

```text
Week 1-2: startup-cto + aws-solution-architect + senior-frontend → Build
Week 3-4: growth-marketer + launch-strategy + copywriting + seo-audit → Prepare
Week 5-6: solo-founder + email-sequence + analytics-tracking → Ship and iterate
```

完整协议见 [orchestration/ORCHESTRATION.md](orchestration/ORCHESTRATION.md)。

---

## POWERFUL Tier

25 个具备深度生产能力的高级 skill：

| Skill | What It Does |
|-------|-------------|
| **agent-designer** | 多 agent 编排、工具 schema、性能评估 |
| **agent-workflow-designer** | 顺序、并行、router、orchestrator、evaluator 模式 |
| **rag-architect** | RAG pipeline 构建、chunking 优化、检索评估 |
| **database-designer** | schema 分析、ERD 生成、索引优化、迁移生成 |
| **database-schema-designer** | 从需求生成 migrations、types、seed data 与 RLS 策略 |
| **migration-architect** | migration 规划、兼容性检查、rollback 生成 |
| **skill-security-auditor** | 🔒 安全门禁，安装前扫描 skill 中的恶意代码 |
| **ci-cd-pipeline-builder** | 识别技术栈并生成 GitHub Actions / GitLab CI 配置 |
| **mcp-server-builder** | 从 OpenAPI 规格构建 MCP servers |
| **pr-review-expert** | 影响面分析、安全扫描、覆盖率变化 |
| **api-design-reviewer** | REST API lint、破坏性变更检测、设计评分卡 |
| **api-test-suite-builder** | 扫描 API 路由并生成完整测试集 |
| **dependency-auditor** | 多语言依赖扫描、许可证合规、升级规划 |
| **release-manager** | changelog 生成、语义版本 bump、发布 readiness 检查 |
| **observability-designer** | SLO 设计、告警优化、dashboard 生成 |
| **performance-profiler** | Node/Python/Go profiling、bundle 分析、压测 |
| **monorepo-navigator** | Turborepo/Nx/pnpm workspace 管理与影响分析 |
| **changelog-generator** | Conventional Commits 到结构化 changelog |
| **codebase-onboarding** | 从代码库分析自动生成 onboarding 文档 |
| **runbook-generator** | 从代码库生成带命令的运维 runbook |
| **git-worktree-manager** | 带端口隔离与环境同步的并行开发工作流 |
| **env-secrets-manager** | `.env` 管理、泄漏检测、轮换流程 |
| **incident-commander** | 事故响应预案、严重级别分类、PIR 生成 |
| **tech-debt-tracker** | 技术债扫描、优先级排序、趋势看板 |
| **interview-system-designer** | 面试流程设计、题库、校准 |

---

## 🔒 Skill Security Auditor

v2.0.0 新增，可在安装前审计任意 skill 的安全风险：

```bash
python3 engineering/skill-security-auditor/scripts/skill_security_auditor.py /path/to/skill/
```

可扫描：命令注入、代码执行、数据外传、提示注入、依赖供应链风险、权限提升。输出 **PASS / WARN / FAIL**，并附修复建议。

**零依赖。** 只要能运行 Python 就能用。

---

## 最近增强的 Skills

新增了生产级增强的 skill：

- `engineering/git-worktree-manager`：worktree 生命周期与清理自动化脚本
- `engineering/mcp-server-builder`：OpenAPI -> MCP 脚手架与 manifest 校验器
- `engineering/changelog-generator`：发布说明生成器与 conventional commit lint
- `engineering/ci-cd-pipeline-builder`：技术栈检测与 pipeline 生成器
- `marketing-skill/prompt-engineer-toolkit`：prompt A/B tester 与 prompt 版本/差异管理器

这些 skill 现在都自带 `scripts/`、拆分后的 `references/`，以及偏使用导向的 `README.md`。

---

## 使用示例

### 架构评审

```text
Using the senior-architect skill, review our microservices architecture
and identify the top 3 scalability risks.
```

### 内容创作

```text
Using the content-creator skill, write a blog post about AI-augmented
development. Optimize for SEO targeting "Claude Code tutorial".
```

### 合规审计

```text
Using the mdr-745-specialist skill, review our technical documentation
for MDR Annex II compliance gaps.
```

---

## Python 分析工具

skills 中随附 254 个 CLI 工具，全部已验证，只依赖标准库：

```bash
# SaaS 健康检查
python3 finance/saas-metrics-coach/scripts/metrics_calculator.py --mrr 80000 --customers 200 --churned 3 --json

# 品牌语气分析
python3 marketing-skill/content-production/scripts/brand_voice_analyzer.py article.txt

# 技术债评分
python3 c-level-advisor/cto-advisor/scripts/tech_debt_analyzer.py /path/to/codebase

# RICE 优先级排序
python3 product-team/product-manager-toolkit/scripts/rice_prioritizer.py features.csv

# 安全审计
python3 engineering/skill-security-auditor/scripts/skill_security_auditor.py /path/to/skill/

# 落地页生成（TSX + Tailwind）
python3 product-team/landing-page-generator/scripts/landing_page_scaffolder.py config.json --format tsx
```

---

## Related Projects

| Project | Description |
|---------|-------------|
| [**Claude Code Skills & Agents Factory**](https://github.com/alirezarezvani/claude-code-skills-agents-factory) | 大规模构建 skills 的方法论 |
| [**Claude Code Tresor**](https://github.com/alirezarezvani/claude-code-tresor) | 含 60+ prompt 模板的生产力工具箱 |
| [**Product Manager Skills**](https://github.com/Digidai/product-manager-skills) | 资深 PM agent，覆盖 6 个知识域、12 个模板、30+ 框架，包括 discovery、strategy、delivery、SaaS metrics、职业辅导与 AI 产品能力 |

---

## FAQ

**如何安装 Claude Code plugins？**  
先用 `/plugin marketplace add alirezarezvani/claude-skills` 添加 marketplace，再用 `/plugin install <name>@claude-code-skills` 安装任意 skill bundle。

**这些 skills 能用于 OpenAI Codex / Cursor / Windsurf / Aider 吗？**  
可以。它们原生或可转换支持 11 种工具：Claude Code、OpenAI Codex、Gemini CLI、OpenClaw、Cursor、Aider、Windsurf、Kilo Code、OpenCode、Augment、Antigravity。运行 `./scripts/convert.sh --tool all` 后，再用 `./scripts/install.sh --tool <name>` 安装。详情见 [Multi-Tool Integrations](https://alirezarezvani.github.io/claude-skills/integrations/)。

**升级会破坏现有安装吗？**  
不会。该仓库遵循语义化版本，并在 patch release 内保持向后兼容。已有脚本参数、plugin 源路径与 `SKILL.md` 结构不会在 patch 版本中变化。每个版本的变更见 [CHANGELOG](CHANGELOG.md)。

**这些 Python 工具真的是零依赖吗？**  
是。全部 254 个 Python CLI 工具都只用标准库，不需要 `pip install`。每个脚本都验证过可以执行 `--help`。

**我该如何创建自己的 Claude Code skill？**  
每个 skill 都是一个文件夹，包含 `SKILL.md`（frontmatter + 指令），以及可选的 `scripts/`、`references/`、`assets/`。如需逐步指导，可参考 [Skills & Agents Factory](https://github.com/alirezarezvani/claude-code-skills-agents-factory)。

---

## Contributing

欢迎贡献。细则见 [CONTRIBUTING.md](CONTRIBUTING.md)。

**可快速着手的方向：**

- 在空白领域新增 skills
- 改进已有 Python 工具
- 为脚本增加测试覆盖
- 为非英语市场补充翻译

---

## License

MIT，详见 [LICENSE](LICENSE)。

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=alirezarezvani/claude-skills&type=Date)](https://star-history.com/#alirezarezvani/claude-skills&Date)

---

**Built by [Alireza Rezvani](https://alirezarezvani.com)** · [Medium](https://alirezarezvani.medium.com) · [Twitter](https://twitter.com/nginitycloud)
