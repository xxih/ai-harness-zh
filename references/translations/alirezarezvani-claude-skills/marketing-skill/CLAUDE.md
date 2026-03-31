# Marketing Skills — Agent Instructions

## 面向所有 Agents（Claude Code、Codex CLI、OpenClaw）

这个目录包含 43 个营销 skill，按 specialist pods 组织。

### 使用方式

1. **先走 routing：** 读取 `marketing-ops/SKILL.md`，里面有把用户请求映射到正确 skill 的路由矩阵
2. **检查上下文：** 如果存在 `marketing-context.md`，先读它，其中包含品牌语气、persona 与竞争格局
3. **只加载一个 skill：** 只读取当前需要的 specialist `SKILL.md`，不要批量加载

### Skill Map

- `marketing-context/`：先运行，用来收集品牌上下文
- `marketing-ops/`：router，负责告诉你该去哪里
- `content-production/`：写内容（博客、文章、指南）
- `content-strategy/`：规划要写什么
- `ai-seo/`：为 AI 搜索引擎优化（ChatGPT、Perplexity、Google AI）
- `seo-audit/`：传统 SEO 审计
- `page-cro/`：转化率优化
- `pricing-strategy/`：定价与打包
- `content-humanizer/`：修复 AI 味过重的内容
- `x-twitter-growth/`：X/Twitter 增长、推文撰写、竞品分析

### Python Tools

共 32 个脚本，全部只依赖标准库，直接运行：

```bash
python3 <skill>/scripts/<tool>.py [args]
```

不需要 `pip install`。脚本都带有内嵌样例，可在无参数时跑 demo 模式。

### Anti-Patterns

❌ 不要一次读完全部 43 个 `SKILL.md`  
❌ 如果存在 `marketing-context.md`，不要跳过  
❌ 不要再使用 `content-creator`（已废弃，改用 `content-production`）  
❌ 不要为了这些 Python 工具安装 pip 包
