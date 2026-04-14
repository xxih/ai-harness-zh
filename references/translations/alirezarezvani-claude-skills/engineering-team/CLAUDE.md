# Engineering Team Skills - Claude Code Guidance

本指南覆盖 36 个可用于生产环境的工程 skill 及其 Python 自动化工具。

## Engineering Skills 概览

**Core Engineering（16 个 skills）：**

- `senior-architect`、`senior-frontend`、`senior-backend`、`senior-fullstack`
- `senior-qa`、`senior-devops`、`senior-secops`
- `code-reviewer`、`senior-security`
- `aws-solution-architect`、`ms365-tenant-manager`、`google-workspace-cli`、`tdd-guide`、`tech-stack-evaluator`、`epic-design`
- **`a11y-audit`**：WCAG 2.2 无障碍审计与修复（`a11y_scanner.py`、`contrast_checker.py`）
- **`azure-cloud-architect`**：Azure 基础设施设计、ARM/Bicep 模板与 landing zone
- **`gcp-cloud-architect`**：GCP 基础设施设计、Terraform 模块与云原生模式
- **`security-pen-testing`**：渗透测试方法论、漏洞评估与 exploit 分析
- **`snowflake-development`**：Snowflake 数仓开发、SQL 优化与数据管道模式

**Security（5 个 skills）：**

- `adversarial-reviewer`、`senior-security`、`security-auditor`
- `security-pen-testing`、`a11y-audit`

**AI/ML/Data（5 个 skills）：**

- `senior-data-scientist`、`senior-data-engineer`、`senior-ml-engineer`
- `senior-prompt-engineer`、`senior-computer-vision`

**工具总数：** 34+ Python 自动化工具

## Core Engineering Tools

### 1. Project Scaffolder

`senior-fullstack/scripts/project_scaffolder.py`

**用途：** 为现代技术栈生成生产级项目脚手架

**支持的栈：**

- Next.js + GraphQL + PostgreSQL
- React + REST + MongoDB
- Vue + GraphQL + MySQL
- Express + TypeScript + PostgreSQL

**功能：**

- Docker Compose 配置
- CI/CD pipeline（GitHub Actions）
- 测试基础设施（Jest、Cypress）
- TypeScript + ESLint + Prettier
- 数据库迁移

**用法：**

```bash
# 创建新项目
python senior-fullstack/scripts/project_scaffolder.py my-project --type nextjs-graphql

# 启动服务
cd my-project && docker-compose up -d
```

### 2. Code Quality Analyzer

`senior-fullstack/scripts/code_quality_analyzer.py`

**用途：** 做全面的代码质量分析与指标评估

**功能：**

- 安全漏洞扫描
- 性能问题检测
- 测试覆盖率评估
- 文档质量检查
- 依赖分析
- 可执行的改进建议

**用法：**

```bash
# 分析项目
python senior-fullstack/scripts/code_quality_analyzer.py /path/to/project

# JSON 输出
python senior-fullstack/scripts/code_quality_analyzer.py /path/to/project --json
```

**输出示例：**

```text
Code Quality Report:
- Overall Score: 85/100
- Security: 90/100 (2 medium issues)
- Performance: 80/100 (3 optimization opportunities)
- Test Coverage: 75% (target: 80%)
- Documentation: 88/100

Recommendations:
1. Update lodash to 4.17.21 (CVE-2020-8203)
2. Optimize database queries in UserService
3. Add integration tests for payment flow
```

### 3. Fullstack Scaffolder

`senior-fullstack/scripts/fullstack_scaffolder.py`

**用途：** 快速生成全栈应用

**用法：**

```bash
python senior-fullstack/scripts/fullstack_scaffolder.py my-app --stack nextjs-graphql
```

## AI/ML/Data Tools

### Data Science

**Experiment Designer**  
`senior-data-scientist/scripts/experiment_designer.py`

- A/B test 设计
- 统计 power 分析
- 样本量计算

**Feature Engineering Pipeline**  
`senior-data-scientist/scripts/feature_engineering_pipeline.py`

- 自动化特征生成
- 相关性分析
- 特征选择

**Statistical Analyzer**  
`senior-data-scientist/scripts/statistical_analyzer.py`

- 假设检验
- 因果推断
- 回归分析

### Data Engineering

**Pipeline Orchestrator**  
`senior-data-engineer/scripts/pipeline_orchestrator.py`

- Airflow DAG 生成
- Spark job 模板
- 数据质量检查

**Data Quality Validator**  
`senior-data-engineer/scripts/data_quality_validator.py`

- Schema 校验
- Null check 强制校验
- 异常检测

**ETL Generator**  
`senior-data-engineer/scripts/etl_generator.py`

- ETL 工作流
- CDC 模式
- 增量加载

### ML Engineering

**Model Deployment Pipeline**  
`senior-ml-engineer/scripts/model_deployment_pipeline.py`

- 容器化模型服务
- REST API 生成
- 负载均衡配置

**MLOps Setup Tool**  
`senior-ml-engineer/scripts/mlops_setup_tool.py`

- MLflow 配置
- 模型版本管理
- 漂移监控

**LLM Integration Builder**  
`senior-ml-engineer/scripts/llm_integration_builder.py`

- OpenAI API 集成
- Prompt templates
- 响应解析

### Prompt Engineering

**Prompt Optimizer**  
`senior-prompt-engineer/scripts/prompt_optimizer.py`

- Prompt A/B testing
- Token 优化
- Few-shot 示例生成

**RAG System Builder**  
`senior-prompt-engineer/scripts/rag_system_builder.py`

- 向量数据库搭建
- Embedding 生成
- 检索策略

**Agent Orchestrator**  
`senior-prompt-engineer/scripts/agent_orchestrator.py`

- 多 agent 工作流
- Tool calling 模式
- 状态管理

### Computer Vision

**Vision Model Trainer**  
`senior-computer-vision/scripts/vision_model_trainer.py`

- 目标检测（YOLO、Faster R-CNN）
- 语义分割
- 迁移学习

**Inference Optimizer**  
`senior-computer-vision/scripts/inference_optimizer.py`

- 模型量化
- TensorRT 优化
- ONNX 导出

**Video Processor**  
`senior-computer-vision/scripts/video_processor.py`

- Frame 提取
- 目标跟踪
- Scene detection

## 技术栈模式

### Frontend（React / Next.js）

- TypeScript strict mode
- Component-driven architecture
- Atomic design patterns
- 状态管理（Zustand / Jotai）
- 测试（Jest + React Testing Library）

### Backend（Node.js / Express）

- Clean architecture
- Dependency injection
- Repository pattern
- Domain-driven design
- 测试（Jest + Supertest）

### Fullstack Integration

- GraphQL 作为 API 层
- REST 用于外部服务
- WebSocket 处理实时场景
- Redis 做缓存
- PostgreSQL 做持久化

## 开发工作流

### Workflow 1: New Project Setup

```bash
# 1. 生成脚手架
python senior-fullstack/scripts/project_scaffolder.py my-app --type nextjs-graphql

# 2. 启动服务
cd my-app && docker-compose up -d

# 3. 执行迁移
npm run migrate

# 4. 启动开发环境
npm run dev
```

### Workflow 2: Code Quality Check

```bash
# 1. 分析代码库
python senior-fullstack/scripts/code_quality_analyzer.py ./

# 2. 修复安全问题
npm audit fix

# 3. 运行测试
npm test

# 4. 生产构建
npm run build
```

### Workflow 3: ML Model Deployment

```bash
# 1. 初始化 MLOps 基础设施
python senior-ml-engineer/scripts/mlops_setup_tool.py

# 2. 部署模型
python senior-ml-engineer/scripts/model_deployment_pipeline.py model.pkl

# 3. 监控表现
# Check MLflow dashboard
```

## 质量标准

**所有 engineering tools 都必须：**

- 支持现代技术栈（Next.js、React、Vue、Express）
- 生成生产级代码
- 包含测试基础设施
- 提供 Docker 配置
- 支持 CI/CD 集成

## 集成模式

### GitHub Actions CI/CD

所有 scaffolders 都会生成 GitHub Actions workflows：

```yaml
.github/workflows/
├── test.yml          # PR 上运行测试
├── build.yml         # 构建并 lint
└── deploy.yml        # 发布到生产环境
```

### Docker Compose

多服务开发环境：

```yaml
services:
  - app (Next.js)
  - api (GraphQL)
  - db (PostgreSQL)
  - redis (Cache)
```

## Additional Resources

- **Quick Start:** `START_HERE.md`
- **Team Structure:** `TEAM_STRUCTURE_GUIDE.md`
- **Engineering Roadmap:** `engineering_skills_roadmap.md`（若存在）
- **Main Documentation:** `../CLAUDE.md`

---

**Last Updated:** March 18, 2026  
**Skills Deployed:** 26 engineering skills production-ready  
**Total Tools:** 39+ Python automation tools across core + AI/ML/Data + epic-design + a11y

---

## epic-design

用于构建具有电影感的 2.5D 交互式网站，支持滚动叙事、视差层次与高级动画。包含素材检查流水线、8 个类别的 45+ 技巧，并内建无障碍支持。

**核心特性：**

- 6 层景深系统与自动视差
- 13 种文字动画、9 种滚动模式
- 带背景判断规则的素材检查
- 自动图片分析的 Python 工具
- WCAG 2.1 AA 合规（支持 reduced-motion）

**适用场景：** 产品发布页、作品集网站、SaaS 营销页、活动官网、Apple 风格动画页面

**Live demo:** [epic-design-showcase.vercel.app](https://epic-design-showcase.vercel.app/)
