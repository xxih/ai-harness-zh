# Gemini CLI 基础说明

这个仓库是一个面向 Gemini CLI 的**综合性 skills 资料库**，提供可复用、可用于生产环境的 skill packages，把领域专业知识、最佳实践、分析工具与战略框架打包在一起。

## 在 Gemini CLI 中使用 Skills

Gemini CLI 可以通过 `activate_skill` 工具激活本仓库中的任意 skill。

### Skill 位置

skills 按 domain 文件夹组织。每个 skill 都是一个目录，内部包含 `SKILL.md`。

| Domain | Folder |
|--------|--------|
| **Engineering (Core)** | `engineering-team/` |
| **Engineering (Advanced)** | `engineering/` |
| **Product Team** | `product-team/` |
| **Marketing Skills** | `marketing-skill/` |
| **C-Level Advisory** | `c-level-advisor/` |
| **Project Management** | `project-management/` |
| **Regulatory & QM** | `ra-qm-team/` |
| **Business & Growth** | `business-growth/` |
| **Finance** | `finance/` |

### ClawHub 发布约束

当这些 skill 发布到 **ClawHub**（clawhub.com）时：

- **`cs-` 前缀仅在 slug 冲突时使用**：只有在其他发布者已经占用该 slug 时，才在 ClawHub 注册表上加 `cs-` 前缀。仓库文件夹名和本地 skill 名称都不改。
- **不得依赖付费/商业服务**：除非项目自己提供，否则 skill 不得要求付费第三方 API key 或商业服务。
- **`plugin.json`**：只允许字段 `name`、`description`、`version`、`author`、`homepage`、`repository`、`license`、`skills: "./"`。
- **速率限制：** ClawHub 每小时最多发布 5 个新 skill。批量发布需采用 drip publishing。

### 激活 Skill

使用文件夹名即可激活 skill，例如：

```javascript
activate_skill(name="senior-architect")
activate_skill(name="content-creator")
activate_skill(name="cto-advisor")
```

Gemini CLI 会在仓库内查找对应的 `SKILL.md` 并加载其中指令。

## Agents 与 Commands

除了 skills，本仓库还提供专用的 **Agents** 与 **Commands**。

- **Agents**（`agents/`）：面向复杂协作的多 agent personas，例如 `cs-engineering-lead`
- **Commands**（`commands/`）：面向常见任务的预定义工作流，例如 `/tdd`、`/tech-debt`

它们同样按 skill 的方式激活：

```javascript
activate_skill(name="cs-engineering-lead")
activate_skill(name="tdd")
```

## Python 自动化工具

每个 skill 在自己的 `scripts/` 目录下都带有确定性的 Python CLI 工具，全部只使用标准库。

示例：

```bash
python3 marketing-skill/content-production/scripts/seo_checker.py article.txt
```

## Gemini CLI 用户的初始化

运行安装脚本，初始化 Gemini 专用的 skill 索引与符号链接：

```bash
./scripts/gemini-install.sh
```

它会创建 `.gemini/skills/` 目录，便于发现与使用这些 skill。
