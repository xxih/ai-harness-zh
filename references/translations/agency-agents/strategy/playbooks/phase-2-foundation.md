# ⚙️ Phase 2 Playbook — 基础与脚手架

> **Duration**: 3-5 days | **Agents**: 6 | **Gate Keepers**: DevOps Automator + Evidence Collector

---

## 目标

建立后续所有工作都依赖的技术与运营基础。先把骨架搭起来，再往上加肌肉。完成此阶段后，每个 developer 都应该拥有可工作的环境、可部署的 pipeline，以及可直接使用的 design system。

## 前置条件

- [ ] 已通过 Phase 1 Quality Gate（Architecture Package 已批准）
- [ ] 已收到 Phase 1 Handoff Package
- [ ] 所有架构文档已定稿

## Agent 激活顺序

### Workstream A：Infrastructure（Day 1-3，并行）

#### 🚀 DevOps Automator — CI/CD Pipeline + Infrastructure

```text
Activate DevOps Automator for infrastructure setup on [PROJECT].

Input: Backend Architect system architecture + deployment requirements
Deliverables required:
1. CI/CD Pipeline (GitHub Actions / GitLab CI)
   - Security scanning stage
   - Automated testing stage
   - Build and containerization stage
   - Deployment stage (blue-green or canary)
   - Automated rollback capability
2. Infrastructure as Code
   - Environment provisioning (dev, staging, production)
   - Container orchestration setup
   - Network and security configuration
3. Environment Configuration
   - Secrets management
   - Environment variable management
   - Multi-environment parity

Files to create:
- .github/workflows/ci-cd.yml (or equivalent)
- infrastructure/ (Terraform/CDK templates)
- docker-compose.yml
- Dockerfile(s)

Format: Working CI/CD pipeline with IaC templates
Timeline: 3 days
```

#### 🏗️ Infrastructure Maintainer — Cloud Infrastructure + Monitoring

```text
Activate Infrastructure Maintainer for monitoring setup on [PROJECT].

Input: DevOps Automator infrastructure + Backend Architect architecture
Deliverables required:
1. Cloud Resource Provisioning
   - Compute, storage, networking resources
   - Auto-scaling configuration
   - Load balancer setup
2. Monitoring Stack
   - Application metrics (Prometheus/DataDog)
   - Infrastructure metrics
   - Custom dashboards (Grafana)
3. Logging and Alerting
   - Centralized log aggregation
   - Alert rules for critical thresholds
   - On-call notification setup
4. Security Hardening
   - Firewall rules
   - SSL/TLS configuration
   - Access control policies

Format: Infrastructure Readiness Report with dashboard access
Timeline: 3 days
```

#### ⚙️ Studio Operations — Process Setup

```text
Activate Studio Operations for process setup on [PROJECT].

Input: Sprint Prioritizer plan + Project Shepherd coordination needs
Deliverables required:
1. Git Workflow
   - Branch strategy (GitFlow / trunk-based)
   - PR review process
   - Merge policies
2. Communication Channels
   - Team channels setup
   - Notification routing
   - Status update cadence
3. Documentation Templates
   - PR template
   - Issue template
   - Decision log template
4. Collaboration Tools
   - Project board setup
   - Sprint tracking configuration

Format: Operations Playbook
Timeline: 2 days
```

### Workstream B：Application Foundation（Day 1-4，并行）

#### 🎨 Frontend Developer — Project Scaffolding + Component Library

```text
Activate Frontend Developer for project scaffolding on [PROJECT].

Input: UX Architect CSS Design System + Brand Guardian identity
Deliverables required:
1. Project Scaffolding
   - Framework setup (React/Vue/Angular per architecture)
   - TypeScript configuration
   - Build tooling (Vite/Webpack/Next.js)
   - Testing framework (Jest/Vitest + Testing Library)
2. Design System Implementation
   - CSS design tokens from UX Architect
   - Base component library (Button, Input, Card, Layout)
   - Theme system (light/dark/system toggle)
   - Responsive utilities
3. Application Shell
   - Routing setup
   - Layout components (Header, Footer, Sidebar)
   - Error boundary implementation
   - Loading states

Files to create:
- src/ (application source)
- src/components/ (component library)
- src/styles/ (design tokens)
- src/layouts/ (layout components)

Format: Working application skeleton with component library
Timeline: 3 days
```

#### 🏗️ Backend Architect — Database + API Foundation

```text
Activate Backend Architect for API foundation on [PROJECT].

Input: System Architecture Specification + Database Schema Design
Deliverables required:
1. Database Setup
   - Schema deployment (migrations)
   - Index creation
   - Seed data for development
   - Connection pooling configuration
2. API Scaffold
   - Framework setup (Express/FastAPI/etc.)
   - Route structure matching architecture
   - Middleware stack (auth, validation, error handling, CORS)
   - Health check endpoints
3. Authentication System
   - Auth provider integration
   - JWT/session management
   - Role-based access control scaffold
4. Service Communication
   - API versioning setup
   - Request/response serialization
   - Error response standardization

Files to create:
- api/ or server/ (backend source)
- migrations/ (database migrations)
- docs/api-spec.yaml (OpenAPI specification)

Format: Working API scaffold with database and auth
Timeline: 4 days
```

#### 🏛️ UX Architect — CSS System Implementation

```text
Activate UX Architect for CSS system implementation on [PROJECT].

Input: Brand Guardian identity + own Phase 1 CSS Design System spec
Deliverables required:
1. Design Tokens Implementation
   - CSS custom properties (colors, typography, spacing)
   - Brand color palette with semantic naming
   - Typography scale with responsive adjustments
2. Layout System
   - Container system (responsive breakpoints)
   - Grid patterns (2-col, 3-col, sidebar)
   - Flexbox utilities
3. Theme System
   - Light theme variables
   - Dark theme variables
   - System preference detection
   - Theme toggle component
   - Smooth transition between themes

Files to create/update:
- css/design-system.css (or equivalent in framework)
- css/layout.css
- css/components.css
- js/theme-manager.js

Format: Implemented CSS design system with theme toggle
Timeline: 2 days
```

## Verification Checkpoint（Day 4-5）

### Evidence Collector Verification

```text
Activate Evidence Collector for Phase 2 foundation verification.

Verify the following with screenshot evidence:
1. CI/CD pipeline executes successfully (show pipeline logs)
2. Application skeleton loads in browser (desktop screenshot)
3. Application skeleton loads on mobile (mobile screenshot)
4. Theme toggle works (light + dark screenshots)
5. API health check responds (curl output)
6. Database is accessible (migration status)
7. Monitoring dashboards are active (dashboard screenshot)
8. Component library renders (component demo page)

Format: Evidence Package with screenshots
Verdict: PASS / FAIL with specific issues
```

## 质量门禁检查清单

| # | Criterion | Evidence Source | Status |
|---|-----------|----------------|--------|
| 1 | CI/CD pipeline builds, tests, and deploys | Pipeline execution logs | ☐ |
| 2 | Database schema deployed with all tables/indexes | Migration success output | ☐ |
| 3 | API scaffold responding on health check | curl response evidence | ☐ |
| 4 | Frontend skeleton renders in browser | Evidence Collector screenshots | ☐ |
| 5 | Monitoring dashboards showing metrics | Dashboard screenshots | ☐ |
| 6 | Design system tokens implemented | Component library demo | ☐ |
| 7 | Theme toggle functional (light/dark/system) | Before/after screenshots | ☐ |
| 8 | Git workflow and processes documented | Studio Operations playbook | ☐ |

## Gate 决策

**需要双签**：DevOps Automator（基础设施）+ Evidence Collector（视觉验证）

- **PASS**：骨架已工作且具备完整 DevOps pipeline，激活 Phase 3
- **FAIL**：存在明确的基础设施或应用问题，修复后重新验证

## 交接到 Phase 3

```markdown
## Phase 2 → Phase 3 Handoff Package

### For all Developer Agents:
- Working CI/CD pipeline (auto-deploys on merge)
- Design system tokens and component library
- API scaffold with auth and health checks
- Database with schema and seed data
- Git workflow and PR process

### For Evidence Collector (ongoing QA):
- Application URLs (dev, staging)
- Screenshot capture methodology
- Component library reference
- Brand guidelines for visual verification

### For Agents Orchestrator (Dev↔QA loop management):
- Sprint Prioritizer backlog (from Phase 1)
- Task list with acceptance criteria (from Phase 1)
- Agent assignment matrix (from NEXUS strategy)
- Quality thresholds for each task type

### Environment Access:
- Dev environment: [URL]
- Staging environment: [URL]
- Monitoring dashboard: [URL]
- CI/CD pipeline: [URL]
- API documentation: [URL]
```

---

*当 skeleton application 已运行、CI/CD pipeline 已可用，且 Evidence Collector 通过截图验证了所有基础要素后，Phase 2 完成。*
