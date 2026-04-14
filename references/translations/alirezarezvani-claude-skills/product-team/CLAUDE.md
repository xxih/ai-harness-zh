# Product Team Skills - Claude Code Guidance

本指南覆盖 16 个可用于生产环境的产品管理 skill 及其 Python 自动化工具。

## Product Skills 概览

**可用 skills：**

1. **product-manager-toolkit/**：RICE 优先级、客户访谈分析（2 个工具）
2. **agile-product-owner/**：User story 生成、sprint planning（1 个工具）
3. **product-strategist/**：OKR 级联、战略规划（1 个工具）
4. **ux-researcher-designer/**：Persona 生成、用户研究（1 个工具）
5. **ui-design-system/**：Design token 生成、组件系统（1 个工具）
6. **competitive-teardown/**：竞品矩阵与 gap analysis（1 个工具）
7. **landing-page-generator/**：Landing page 脚手架（1 个工具）
8. **saas-scaffolder/**：SaaS 项目初始化（1 个工具）
9. **product-analytics/**：KPI 设计、retention / cohort / funnel 分析（1 个工具）
10. **experiment-designer/**：实验设计与样本量规划（1 个工具）
11. **product-discovery/**：Discovery 框架与 assumption mapping（1 个工具）
12. **roadmap-communicator/**：路线图沟通与 changelog 生成（1 个工具）
13. **code-to-prd/**：从任意代码库逆向生成 PRD（2 个工具：`codebase_analyzer`、`prd_scaffolder`）
14. **research-summarizer/**：研究归纳与总结（1 个工具）
15. **apple-hig-expert/**：Apple Human Interface Guidelines 合规与设计（1 个工具：`hig_checker`）
16. **spec-to-repo/**：把 spec 文档转换为脚手架仓库

**工具总数：** 17 个 Python 自动化工具

**Agents：** 5 个（`cs-product-manager`、`cs-agile-product-owner`、`cs-product-strategist`、`cs-ux-researcher`、`cs-product-analyst`）

**Slash Commands：** 8 个（`/rice`、`/okr`、`/persona`、`/user-story`、`/competitive-matrix`、`/prd`、`/sprint-plan`、`/code-to-prd`）

## Python 自动化工具

### 1. RICE Prioritizer

`product-manager-toolkit/scripts/rice_prioritizer.py`

**用途：** 用 RICE 框架做功能优先级排序

**公式：** `(Reach × Impact × Confidence) / Effort`

**功能：**

- 组合分析（quick wins vs big bets）
- 季度路线图生成
- 容量规划（story points 或 dev days）
- 面向 Jira / Linear 的 CSV 输入输出
- 面向 dashboard 的 JSON 导出

**用法：**

```bash
# 基础优先级排序
python product-manager-toolkit/scripts/rice_prioritizer.py features.csv

# 带容量规划
python product-manager-toolkit/scripts/rice_prioritizer.py features.csv --capacity 20

# JSON 输出
python product-manager-toolkit/scripts/rice_prioritizer.py features.csv --output json
```

**CSV 格式：**

```csv
feature,reach,impact,confidence,effort
User Dashboard,500,3,0.8,5
API Rate Limiting,1000,2,0.9,3
Dark Mode,300,1,1.0,2
```

### 2. Customer Interview Analyzer

`product-manager-toolkit/scripts/customer_interview_analyzer.py`

**用途：** 基于 NLP 的访谈记录分析

**功能：**

- 痛点抽取与严重度评分
- 功能诉求识别
- 情绪分析
- 主题抽取
- Jobs-to-be-done 模式识别

**用法：**

```bash
python product-manager-toolkit/scripts/customer_interview_analyzer.py interview.txt
python product-manager-toolkit/scripts/customer_interview_analyzer.py interview.txt json
```

### 3. User Story Generator

`agile-product-owner/scripts/user_story_generator.py`

**用途：** 生成符合 INVEST 原则的 user stories

**功能：**

- 带容量分配的 sprint planning
- Epic 拆分成可交付 stories
- Acceptance criteria 生成
- Story point 估算
- 优先级评分

**用法：**

```bash
# 交互模式
python agile-product-owner/scripts/user_story_generator.py

# Sprint planning（30 story points）
python agile-product-owner/scripts/user_story_generator.py sprint 30
```

### 4. OKR Cascade Generator

`product-strategist/scripts/okr_cascade_generator.py`

**用途：** 自动生成 OKR 层级（company → product → team）

**功能：**

- 对齐度评分（纵向与横向）
- 战略模板（growth、retention、revenue、innovation）
- Key result 跟踪
- 进度可视化

**用法：**

```bash
python product-strategist/scripts/okr_cascade_generator.py growth
python product-strategist/scripts/okr_cascade_generator.py retention
```

### 5. Persona Generator

`ux-researcher-designer/scripts/persona_generator.py`

**用途：** 根据用户研究生成 data-driven persona

```bash
python ux-researcher-designer/scripts/persona_generator.py
python ux-researcher-designer/scripts/persona_generator.py --output json
```

### 6. Design Token Generator

`ui-design-system/scripts/design_token_generator.py`

**用途：** 从品牌色自动生成完整 design token 系统

```bash
python ui-design-system/scripts/design_token_generator.py "#0066CC" modern css
python ui-design-system/scripts/design_token_generator.py "#0066CC" modern scss
python ui-design-system/scripts/design_token_generator.py "#0066CC" modern json
```

### 7. Competitive Matrix Builder

`competitive-teardown/scripts/competitive_matrix_builder.py`

**用途：** 生成带权重的竞品评分与 gap analysis

```bash
python competitive-teardown/scripts/competitive_matrix_builder.py competitors.json
```

### 8. Landing Page Scaffolder

`landing-page-generator/scripts/landing_page_scaffolder.py`

**用途：** 生成生产级 landing page，默认输出 Next.js / React TSX + Tailwind CSS，也支持纯 HTML。

**功能：**

- 默认输出 TSX：Next.js 14+ App Router 组件 + Tailwind classes
- 4 种设计风格：`dark-saas`、`clean-minimal`、`bold-startup`、`enterprise`
- 7 类 section 生成器：导航、hero、features、testimonials、pricing、CTA、footer
- 文案框架：PAS、AIDA、BAB

**用法：**

```bash
python landing-page-generator/scripts/landing_page_scaffolder.py config.json --format tsx
python landing-page-generator/scripts/landing_page_scaffolder.py config.json --format html
```

### 9. Project Bootstrapper

`saas-scaffolder/scripts/project_bootstrapper.py`

**用途：** 生成带 auth、billing 与 API 初始化的 SaaS 脚手架

```bash
python saas-scaffolder/scripts/project_bootstrapper.py project_config.json
```

### 10. Metrics Calculator

`product-analytics/scripts/metrics_calculator.py`

**用途：** 产品分析，包括 retention、cohort 与 funnel 分析

**功能：**

- 基于事件数据的 retention curve 分析
- 分阶段的 funnel conversion 跟踪
- Cohort 分组与对比

**用法：**

```bash
python product-analytics/scripts/metrics_calculator.py retention events.csv
python product-analytics/scripts/metrics_calculator.py funnel funnel.csv --stages visit,signup,activate,pay
python product-analytics/scripts/metrics_calculator.py kpi metrics.csv --json
```

### 11. Sample Size Calculator

`experiment-designer/scripts/sample_size_calculator.py`

**用途：** 为 A/B tests 与其他实验做样本量规划

**功能：**

- Minimum detectable effect（MDE）计算
- 支持绝对值与相对值两种 effect size
- 支持自定义 alpha / beta 的 power analysis

**用法：**

```bash
python experiment-designer/scripts/sample_size_calculator.py --baseline-rate 0.12 --mde 0.02 --mde-type absolute
python experiment-designer/scripts/sample_size_calculator.py --baseline-rate 0.12 --mde 0.15 --mde-type relative
python experiment-designer/scripts/sample_size_calculator.py --baseline-rate 0.12 --mde 0.02 --alpha 0.01 --power 0.9
```

### 12. Assumption Mapper

`product-discovery/scripts/assumption_mapper.py`

**用途：** 绘制并排序 discovery 阶段的产品假设

**功能：**

- 按 risk × uncertainty 评分
- 支持结构化 CSV 输入
- 按 desirability / viability / feasibility / usability 分类

**用法：**

```bash
python product-discovery/scripts/assumption_mapper.py assumptions.csv
python product-discovery/scripts/assumption_mapper.py assumptions.csv --json
```

### 13. Changelog Generator

`roadmap-communicator/scripts/changelog_generator.py`

**用途：** 基于 git commit history 生成结构化 changelog

**注意：** 依赖 `git`，必须在 git 仓库内运行。

**用法：**

```bash
python roadmap-communicator/scripts/changelog_generator.py --from v1.0.0 --to HEAD
python roadmap-communicator/scripts/changelog_generator.py --from v1.0.0 --to v2.0.0 --json
```

## Product Workflows

### Workflow 1: 从功能优先级到 Sprint 执行

```bash
python product-manager-toolkit/scripts/rice_prioritizer.py features.csv --capacity 30
python agile-product-owner/scripts/user_story_generator.py sprint 30
```

### Workflow 2: 从战略到团队级 OKRs

```bash
python product-strategist/scripts/okr_cascade_generator.py growth --json > okrs.json
```

### Workflow 3: 从研究到 Persona 产物

```bash
python ux-researcher-designer/scripts/persona_generator.py json > personas.json
```

### Workflow 4: 品牌对齐的 Landing Page

```bash
python ../marketing-skill/content-production/scripts/brand_voice_analyzer.py website_copy.txt --format json > voice.json
python ui-design-system/scripts/design_token_generator.py "#0066CC" modern css
python landing-page-generator/scripts/landing_page_scaffolder.py config.json --format tsx
python competitive-teardown/scripts/competitive_matrix_builder.py competitors.json
```

### Workflow 5: 产品分析与实验

```bash
python product-analytics/scripts/metrics_calculator.py retention events.csv
python product-analytics/scripts/metrics_calculator.py funnel funnel.csv --stages visit,signup,activate,pay
python experiment-designer/scripts/sample_size_calculator.py --baseline-rate 0.12 --mde 0.02 --mde-type absolute
```

### Workflow 6: Discovery 与机会验证

```bash
python product-discovery/scripts/assumption_mapper.py assumptions.csv
```

### Workflow 7: 路线图与发布沟通

```bash
python roadmap-communicator/scripts/changelog_generator.py --from v1.0.0 --to HEAD
```

## 质量标准

**所有 product Python tools 都必须：**

- 采用 CLI-first 设计，便于自动化
- 同时支持交互模式与 batch 模式
- 提供 JSON 输出，便于工具集成
- 优先只依赖标准库
- 给出可执行建议

## Additional Resources

- **Main Documentation:** `../CLAUDE.md`
- **Marketing Brand Voice:** `../marketing-skill/content-production/scripts/brand_voice_analyzer.py`

---

**Last Updated:** March 17, 2026  
**Skills Deployed:** 16/16 product skills production-ready  
**Total Tools:** 16 Python automation tools  
**Agents:** 5 | **Commands:** 8
