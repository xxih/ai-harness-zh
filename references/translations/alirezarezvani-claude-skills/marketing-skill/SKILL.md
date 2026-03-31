---
name: "marketing-skills"
description: "面向 Claude Code、Codex、Gemini CLI、Cursor、OpenClaw 以及另外 6 个编码代理的 42 个营销 agent skills 与 plugins。包含 7 个 pod：content、SEO、CRO、channels、growth、intelligence、sales。带有 foundation context、orchestration router，以及 27 个只依赖标准库的 Python 工具。"
version: 2.0.0
author: Alireza Rezvani
license: MIT
tags:
  - marketing
  - seo
  - content
  - copywriting
  - cro
  - analytics
  - ai-seo
agents:
  - claude-code
  - codex-cli
  - openclaw
---

# Marketing Skills Division

42 个可用于生产环境的营销 skill，按 7 个专业 pod 组织，并配有一个 context foundation 与 orchestration layer。

## 快速开始

### Claude Code

```text
/read marketing-skill/marketing-ops/SKILL.md
```

router 会把你导向正确的专家 skill。

### Codex CLI

```bash
codex --full-auto "Read marketing-skill/marketing-ops/SKILL.md, then help me write a blog post about [topic]"
```

### OpenClaw

skills 会从仓库中自动发现。直接向 agent 提出营销任务，它会通过 `marketing-ops` 做路由。

## 架构

```text
marketing-skill/
├── marketing-context/     ← Foundation: brand voice、audience、goals
├── marketing-ops/         ← Router: 分发到正确的 skill
│
├── Content Pod (8)        ← Strategy → Production → Editing → Social
├── SEO Pod (5)            ← Traditional + AI SEO + Schema + Architecture
├── CRO Pod (6)            ← Pages, Forms, Signup, Onboarding, Popups, Paywall
├── Channels Pod (5)       ← Email, Ads, Cold Email, Ad Creative, Social Mgmt
├── Growth Pod (4)         ← A/B Testing, Referrals, Free Tools, Churn
├── Intelligence Pod (4)   ← Competitors, Psychology, Analytics, Campaigns
└── Sales & GTM Pod (2)    ← Pricing, Launch Strategy
```

## 首次初始化

先运行 `marketing-context`，生成你的 `marketing-context.md`。其他所有 skill 都会读取这个文件，用于获取品牌语气、受众画像与竞争格局。只需做一次，但收益很高。

## Pod 概览

| Pod | Skills | Python Tools | Key Capabilities |
|-----|--------|-------------|-----------------|
| **Foundation** | 2 | 2 | 品牌上下文采集、skill 路由 |
| **Content** | 8 | 5 | 从 strategy 到 production、editing、humanization |
| **SEO** | 5 | 2 | Technical SEO、AI SEO（AEO/GEO）、schema、architecture |
| **CRO** | 6 | 0 | 页面、表单、注册、onboarding、popup、paywall 优化 |
| **Channels** | 5 | 2 | 邮件序列、付费广告、cold email、ad creative |
| **Growth** | 4 | 2 | A/B testing、referral、free tools、churn prevention |
| **Intelligence** | 4 | 4 | 竞品分析、营销心理学、分析、活动复盘 |
| **Sales & GTM** | 2 | 1 | 定价策略、发布规划 |
| **Standalone** | 4 | 9 | ASO、品牌规范、PMM strategy、prompt engineering |

## Python Tools（27 个脚本）

全部脚本都只依赖标准库，无需 `pip install`，采用 CLI-first 设计，支持 JSON 输出，并内置样例数据方便 demo。

```bash
# 内容评分
python3 marketing-skill/content-production/scripts/content_scorer.py article.md

# AI 写作检测
python3 marketing-skill/content-humanizer/scripts/humanizer_scorer.py draft.md

# 品牌语气分析
python3 marketing-skill/content-production/scripts/brand_voice_analyzer.py copy.txt

# 广告文案校验
python3 marketing-skill/ad-creative/scripts/ad_copy_validator.py ads.json

# 定价情景建模
python3 marketing-skill/pricing-strategy/scripts/pricing_modeler.py

# Tracking plan 生成
python3 marketing-skill/analytics-tracking/scripts/tracking_plan_generator.py
```

## 独特能力

- **AI SEO（AEO/GEO/LLMO）**：不仅优化排名，也优化 AI 引用
- **Content Humanizer**：通过评分检测并修复 AI 写作痕迹
- **Context Foundation**：一个品牌上下文文件可供全部 42 个 skill 共享
- **Orchestration Router**：基于关键词与复杂度评分做智能路由
- **Zero Dependencies**：全部 Python 工具都只使用标准库
