---
name: newproject
description: "用于新建项目或升级既有仓库的项目引导与仓库基线初始化 skill。当用户要补齐基础文件、代码质量、发布自动化、CI、GitHub 配置、依赖管理与安全扫描时使用；所需模板、workflow 与脚本都内置在 `assets/` 下。"
---

# newproject

为新项目或已有项目提供端到端初始化。
它把所需模板、workflow 和脚本都放在自己的 `assets/` 目录中。

如果本次初始化需要结构化用户输入，先检测当前宿主环境里有哪些提问工具可用：

- 如果 `AskUserQuestion` 可用，就使用 `AskUserQuestion`
- 否则，如果 `request_user_input` 可用，就使用 `request_user_input`
- 如果两者都不可用，就直接用普通文本向用户提问

必须在第一次提问前完成这一步检测，并在整次执行里持续使用同一种提问工具。

## 这个 Skill 会初始化什么

```text
Tier 1 — Foundation
  project scaffold      README, LICENSE, .gitignore, .editorconfig, CONTRIBUTING.md
  AGENTS.md baseline    shared AI instructions + CLAUDE.md symlink
  release workflow      conventional commits, changelog-driven releases, release.yml
  ci pipeline           GitHub Actions CI for the detected project type

Tier 2 — Quality and Governance
  code quality          ESLint/Prettier or Ruff/golangci-lint/rustfmt + markdownlint
  GitHub repo setup     PR template, issue forms, labels, 可选 CODEOWNERS, branch protection
  dependencies          Dependabot + auto-merge workflow

Tier 3 — Security
  security scanning     CodeQL when supported, dependency review, secret scanning guidance
```

## 资产布局

本包所需文件全部都在 package 内：

- `assets/foundation/`：README、LICENSE、CONTRIBUTING、.gitignore、.editorconfig
- `assets/quality/`：ESLint、Prettier、Ruff、markdownlint、pre-commit hook
- `assets/ci/`：GitHub Actions CI 模板
- `assets/release/`：commitlint 配置、release workflow、提取脚本与参考说明
- `assets/github/`：PR 模板、issue forms、labels、CODEOWNERS 模板、branch protection 脚本
- `assets/dependencies/`：Dependabot 模板与 auto-merge workflow
- `assets/security/`：CodeQL 与 dependency review workflows

---

## Step 1: 检测项目与当前状态

在提问前先检查仓库：

```bash
# Project type indicators
ls package.json pyproject.toml setup.py requirements.txt go.mod Cargo.toml 2>/dev/null

# Web framework indicators
ls next.config.* nuxt.config.* vite.config.* angular.json svelte.config.* astro.config.* remix.config.* 2>/dev/null

# Existing foundation files
ls README.md LICENSE .gitignore .editorconfig CONTRIBUTING.md CHANGELOG.md AGENTS.md CLAUDE.md 2>/dev/null
file AGENTS.md CLAUDE.md 2>/dev/null

# Existing GitHub configuration
ls .github/ 2>/dev/null
ls .github/workflows/ 2>/dev/null
ls .github/pull_request_template.md .github/ISSUE_TEMPLATE/ .github/CODEOWNERS .github/dependabot.yml 2>/dev/null

# Existing tooling
ls eslint.config.* .eslintrc* prettier.config.* .prettierrc* ruff.toml .pre-commit-config.yaml .golangci.yml rustfmt.toml .markdownlint.json 2>/dev/null
ls .husky/ 2>/dev/null

# Existing release / CI / security workflows
ls .github/workflows/ci* .github/workflows/release* .github/workflows/commitlint* .github/workflows/codeql* .github/workflows/dependency-review* 2>/dev/null

# Package manager and scripts for Node projects
ls package-lock.json yarn.lock pnpm-lock.yaml bun.lockb 2>/dev/null
node -e "const p=require('./package.json'); console.log(JSON.stringify(p.scripts||{}, null, 2))" 2>/dev/null || true

# Git state
git status --short 2>/dev/null || echo "git not initialized"
git remote -v 2>/dev/null || echo "no remote"
git branch --show-current 2>/dev/null || true
```

判定以下信息：

- **Project type**
  - 如果存在 `package.json`，且同时存在某个 web framework 配置，则为 `web`
  - 如果存在 `package.json`，但没有 web framework 配置，则为 `node`
  - 如果存在 `pyproject.toml`、`setup.py` 或 `requirements.txt`，则为 `python`
  - 如果存在 `go.mod`，则为 `go`
  - 如果存在 `Cargo.toml`，则为 `rust`
  - 否则为 `other`
- **Project state**
  - 如果没有包清单、没有 README、没有 `.github/`，且没有 git remote，则视为全新目录
  - 否则视为已有项目
- **Package manager**（Node 项目）
  - 有 `package-lock.json` 则为 `npm`
  - 有 `yarn.lock` 则为 `yarn`
  - 有 `pnpm-lock.yaml` 则为 `pnpm`
  - 有 `bun.lockb` 则为 `bun`
  - 都没有则默认 `npm`
- **Available scripts**（Node 项目）
  - 记录是否存在 `lint`、`test`、`build`
- **Version source of truth**
  - Node / web 使用 `package.json`
  - Python 使用 `pyproject.toml` 或 `setup.py`
  - Rust 使用 `Cargo.toml`
  - Go 或其他项目如果没有版本文件，则默认按 tag-only 流程处理

---

## Step 2: 选择本次执行范围

### Path A — 全新项目

对于全新目录，在推荐技术栈之前先收集基础项目上下文。

显式使用 `AskUserQuestion` / `request_user_input`：

- 如果目录名不足以明确项目名：
  - “What is the project name?”
- 总是要问：
  - “Please provide a short description (1-2 sentences).”

然后用项目名和描述推荐一个默认技术栈，例如：

> “Based on your description, I suggest a Node.js + TypeScript setup with Vitest,
> ESLint, and Prettier. That gives you a fast default for libraries and apps.
> Confirm this stack or tell me what you prefer.”

显式用 `AskUserQuestion` / `request_user_input` 让用户确认或覆盖这个推荐技术栈。

之后展示清单：

```text
New [type] project: [name]

Tier 1 — Foundation
  [x] scaffold and repo baseline
  [x] release workflow
  [x] CI pipeline

Tier 2 — Quality and Governance
  [x] code quality
  [x] GitHub repository setup
  [x] dependency management

Tier 3 — Security
  [x] security scanning
```

显式使用 `AskUserQuestion` / `request_user_input`：

- “Press Enter to run everything, or tell me what to skip: for example `skip security`, `tier1 only`, or `code quality only`.”

### Path B — 已有项目

对于已有仓库，不要再问项目名或描述。
先读取仓库，自行推断上下文。

在展示清单前，先读取最相关的项目说明文件：

- `README.md`
- `AGENTS.md`
- 如果存在 `CLAUDE.md` 且不是指向 `AGENTS.md` 的 symlink，也要读
- 包元数据，例如 `package.json`、`pyproject.toml`、`go.mod`、`Cargo.toml`
- `CHANGELOG.md`
- `.github/workflows/` 下已有 workflow

然后在询问范围之前，先给用户一段简短理解总结。总结至少应包含：

- 推断出的项目名
- 项目大致是做什么的
- 检测出的技术栈
- 当前已经存在哪些初始化项
- `newproject` 能补上的最高价值缺口

之后再按当前状态标记清单，默认优先未完成的 Tier 1 项：

```text
Project: [detected type] — [project name]

Tier 1 — Foundation
  [done or empty] scaffold and repo baseline
  [done or empty] release workflow
  [done or empty] CI pipeline

Tier 2 — Quality and Governance
  [done or empty] code quality
  [done or empty] GitHub repository setup
  [done or empty] dependency management

Tier 3 — Security
  [done or empty] security scanning
```

显式使用 `AskUserQuestion` / `request_user_input`：

- “Which parts should I run? Press Enter to run unchecked Tier 1 items, or say `all`, `tier2`, or specific parts.”

后续所有步骤都以用户选定的 scope 为准。

---

## Step 3: Foundation 与仓库基线

当用户选择 scaffold and repo baseline 时执行本节。

### 3.1 如有需要先初始化 Git

如果当前目录还不是 git 仓库：

```bash
git init
git checkout -b main
```

如果已经是 git 仓库，则跳过。

### 3.2 创建或更新基础文件

只能使用本 package 自带的 vendored assets：

- `assets/foundation/templates/README.md.template`
- `assets/foundation/templates/LICENSE-MIT.template`
- `assets/foundation/templates/CONTRIBUTING.md.template`
- `assets/foundation/gitignore/`
- `assets/foundation/editorconfig/.editorconfig`

应用以下规则：

- `README.md`
  - 缺失时，用模板创建
  - 替换 `{{PROJECT_NAME}}`、`{{DESCRIPTION}}`、`{{PROJECT_TYPE}}`
  - 如果已存在，只补缺失的标准章节，例如 installation、usage、contributing
- `LICENSE`
  - 缺失时默认使用 MIT
  - 把 `{{YEAR}}` 替换为当前年份
  - 把 `{{AUTHOR}}` 替换为用户名
  - 如果用户名未知，要显式使用 `AskUserQuestion` / `request_user_input`
- `.gitignore`
  - 缺失时，复制对应语言模板
  - 如果已存在，只追加明确缺失的语言相关片段
- `.editorconfig`
  - 缺失时复制 vendored 模板
- `CONTRIBUTING.md`
  - 缺失时由模板创建
  - 如果已存在，保留原内容，后续在 release workflow 步骤再补缺失章节

### 3.3 创建标准目录

只创建当前缺失的目录：

- Node 或 web：`src/`、`tests/`、`docs/`、`scripts/`
- Python：`src/<package_name>/`、`tests/`、`docs/`、`scripts/`
- Go：`cmd/<project_name>/`、`internal/`、`pkg/`、`docs/`、`scripts/`
- Rust：`docs/`、`scripts/`
- Other：`src/`、`tests/`、`docs/`、`scripts/`

对于 Python，如果 `src/<package_name>/` 是新建的，也要同时创建 `src/<package_name>/__init__.py`。

### 3.4 让 `AGENTS.md` 成为统一真相源

统一 `AGENTS.md` 与 `CLAUDE.md`，让不同 AI 工具读取同一份约束。

先检测当前状态：

```bash
[ -L CLAUDE.md ] && echo "CLAUDE.md is a symlink" || echo "CLAUDE.md is not a symlink"
[ -f AGENTS.md ] && echo "AGENTS.md exists" || echo "AGENTS.md missing"
[ -f CLAUDE.md ] && echo "CLAUDE.md exists" || echo "CLAUDE.md missing"
```

按以下状态处理：

- **Already unified**：`CLAUDE.md` 已经是指向 `AGENTS.md` 的 symlink
  - 保持不变
- **两个文件都不存在**
  - 创建最小版 `AGENTS.md`：

    ```markdown
    # AGENTS.md

    This file provides guidance to AI coding assistants (Claude Code, OpenAI Codex,
    and others) when working with code in this repository.

    ## Contributor Conventions

    Follow [CONTRIBUTING.md](CONTRIBUTING.md) for all contribution conventions.
    ```

  - 然后执行 `ln -s AGENTS.md CLAUDE.md`
- **只有 `CLAUDE.md` 存在且它是普通文件**
  - 把它移动到 `AGENTS.md`
  - 如果标题是 `# CLAUDE.md`，改成 `# AGENTS.md`
  - 然后创建 symlink：`ln -s AGENTS.md CLAUDE.md`
- **只有 `AGENTS.md` 存在**
  - 创建 symlink：`ln -s AGENTS.md CLAUDE.md`
- **两个文件都存在且都是普通文件**
  - 在合并前，显式使用 `AskUserQuestion` / `request_user_input`
  - 以 `AGENTS.md` 为基准
  - 只把 `CLAUDE.md` 中尚未出现的章节追加进去
  - 标题统一为 `# AGENTS.md`
  - 再把 `CLAUDE.md` 替换为 symlink

当文件状态修正完成后，确保 `AGENTS.md` 含有一个指向 `CONTRIBUTING.md` 的 `## Contributor Conventions` 章节。

---

## Step 4: 代码质量与发布工作流

当用户选择 code quality、release workflow，或两者都选时执行本节。
如果是 Node 项目并且两者都要做，先做 code quality，再做 release workflow，这样可以顺带共享 husky。

### 4.1 Code Quality

只能使用本 package 自带的 vendored assets：

- `assets/quality/config/eslint.config.js`
- `assets/quality/config/prettier.config.js`
- `assets/quality/config/ruff.toml`
- `assets/quality/config/.markdownlint.json`
- `assets/quality/hooks/pre-commit`

#### Node 或 Web

安装基础工具：

```bash
npm install --save-dev \
  eslint \
  @eslint/js \
  prettier \
  eslint-config-prettier \
  lint-staged \
  husky
```

如果是 TypeScript 项目，再安装：

```bash
npm install --save-dev \
  typescript-eslint \
  @typescript-eslint/eslint-plugin \
  @typescript-eslint/parser
```

然后：

- 如果不存在 flat config，就把 `assets/quality/config/eslint.config.js` 复制到 `eslint.config.js`
- 如果缺少 `prettier.config.js`，就复制 `assets/quality/config/prettier.config.js`
- 给 `package.json` 增加 `lint-staged` 配置：

  ```json
  {
    "lint-staged": {
      "*.{js,jsx,ts,tsx}": ["eslint --fix", "prettier --write"],
      "*.{json,css,md,yml,yaml}": ["prettier --write"],
      "*.md": ["markdownlint-cli2 --fix"]
    }
  }
  ```

- 只有在 `.husky/` 不存在时才初始化 husky：

  ```bash
  ls .husky/ 2>/dev/null || npx husky init
  ```

- 确保 `.husky/pre-commit` 会运行 `npx lint-staged`

#### Python

安装并配置 Ruff：

```bash
pip install ruff pre-commit
```

然后：

- 如果缺失，则复制 `assets/quality/config/ruff.toml` 到 `ruff.toml`
- 如果缺失，则复制 `assets/quality/hooks/pre-commit` 到 `.pre-commit-config.yaml`
- 执行 `pre-commit install`

#### Go

安装 `golangci-lint`，并在缺失时创建 `.golangci.yml`：

```bash
brew install golangci-lint
```

使用以下基线配置：

```yaml
run:
  timeout: 5m

linters:
  enable:
    - gofmt
    - goimports
    - govet
    - errcheck
    - staticcheck
    - unused
    - gosimple

issues:
  exclude-rules:
    - path: _test\.go
      linters: [errcheck]
```

#### Rust

确保标准工具已安装：

```bash
rustup component add rustfmt clippy
```

如果缺失，则创建 `rustfmt.toml`：

```toml
edition = "2021"
max_width = 100
tab_spaces = 4
```

#### 所有项目类型

配置 markdown lint：

```bash
npm install --save-dev markdownlint-cli2
```

如果 `.markdownlint.json` 缺失，则复制 `assets/quality/config/.markdownlint.json`。

如果 `AGENTS.md` 中还没有下面这句话，就补进去：

> `Code quality: run the configured formatter and linter before committing.`

### 4.2 Release Workflow

只能使用本 package 自带的 vendored assets：

- `assets/release/config/commitlint.config.js`
- `assets/release/workflows/commitlint-check.yml`
- `assets/release/workflows/release.yml`
- `assets/release/scripts/extract-release-notes.sh`
- `assets/release/references/changelog-style-guide.md`

#### Conventional Commits

对于 Node 或 web 项目，本地安装 commitlint：

```bash
npm install --save-dev \
  @commitlint/cli \
  @commitlint/config-conventional \
  husky
```

把 `assets/release/config/commitlint.config.js` 复制到 `commitlint.config.js`。

确保 `.husky/commit-msg` 存在，并运行：

```bash
npx --no -- commitlint --edit $1
```

对于非 Node 项目，则把
`assets/release/workflows/commitlint-check.yml` 复制到
`.github/workflows/commitlint-check.yml`。

#### Release Workflow Files

复制这些文件：

- `assets/release/workflows/release.yml` → `.github/workflows/release.yml`
- `assets/release/scripts/extract-release-notes.sh` → `scripts/extract-release-notes.sh`
- `assets/release/references/changelog-style-guide.md` → `docs/changelog-style-guide.md`

然后：

- 给 `scripts/extract-release-notes.sh` 增加可执行权限
- 配置 `release.yml` 里的 tag glob
  - 无前缀时使用 `'*.*.*'`
  - 如果仓库已有 tag 前缀，则用 `'myapp-*.*.*'`
- 配置 `release.yml` 里的版本校验来源
  - Node / web：`package.json`
  - Python：`pyproject.toml` 或已有版本文件
  - Rust：`Cargo.toml`
  - Go 或 generic 仓库若是 tag-only，则跳过版本文件校验

#### CHANGELOG.md

如果缺少 `CHANGELOG.md`，按带链接标题的格式创建：

```markdown
# Changelog

All notable changes to this project will be documented in this file.
Versions follow [Semantic Versioning](https://semver.org).

## [Unreleased](https://github.com/OWNER/REPO/compare/v0.0.0...HEAD)
```

真实发布时，使用这种格式：

```markdown
## [1.2.0](https://github.com/OWNER/REPO/compare/v1.1.0...v1.2.0) (2026-03-18)
```

规则：

- `Unreleased` 必须始终是带链接的标题
- 每次 commit 或 merge 到 `main`，都必须在 `Unreleased` 下手工加入一条面向用户的简短 changelog
- 每个 release 标题都必须比较上一个 tag 和新 tag
- 某个 release section 里的第一条加粗行会成为 GitHub Release 标题

#### CONTRIBUTING.md 与 AGENTS.md

确保 `CONTRIBUTING.md` 记录了这条 release 流程：

1. 所有 merge 到 `main` 的变更都必须更新 `CHANGELOG.md`
2. 新条目要在 merge commit 之前或随 merge commit 一起写到 `Unreleased`
3. 日常开发中要始终保持 `Unreleased` 最新
4. 发布当天，把累积的 `Unreleased` 条目整理成新的版本 section
5. 如果项目有版本文件，则同步 bump 版本
6. 提交这些 release 变更
7. 给该精确 commit 打 tag
8. 推送 commit 与 tag

如果 `AGENTS.md` 里还没有下面这句话，就补进去：

> `Release: every change merged to main must update CHANGELOG.md under the Unreleased section. When the user says "release" or "ship", follow the Release Workflow section in CONTRIBUTING.md and use docs/changelog-style-guide.md for changelog editing.`

#### Verification

如果仓库的 `CHANGELOG.md` 已有某个版本 section，则 dry-run 一次提取脚本：

```bash
CHANGELOG_FILE=CHANGELOG.md ./scripts/extract-release-notes.sh v1.2.0
```

如果脚本失败，在宣称 release setup 完成之前，先修好 changelog 格式。

同时也要检查 `Unreleased` 是否已经承载了持续开发的记录，而不是在正常 feature / fix 合并进 `main` 后被留空。

---

## Step 5: CI Pipeline 与 GitHub 仓库配置

当用户选择 CI pipeline、GitHub repository setup，或两者都选时执行本节。

### 5.1 CI Pipeline

只能使用本 package 自带的 vendored assets：

- `assets/ci/workflows/ci-node.yml`
- `assets/ci/workflows/ci-python.yml`
- `assets/ci/workflows/ci-go.yml`
- `assets/ci/workflows/ci-rust.yml`
- `assets/ci/workflows/ci-generic.yml`

如果需要，先创建 `.github/workflows/`。

#### Node 或 Web

如果存在 `package.json` 但没有 lockfile，则在写 CI 前先生成一个：

```bash
npm install
```

把 `assets/ci/workflows/ci-node.yml` 复制到 `.github/workflows/ci.yml`。

然后按项目实际情况定制：

- 配置 Node matrix
  - libraries 与 CLIs：`[18, 20, 22]`
  - web apps：通常单个当前 LTS 版本即可
- 设置对应包管理器的安装命令：
  - `npm ci`
  - `yarn install --frozen-lockfile`
  - `pnpm install --frozen-lockfile`
  - `bun install --frozen-lockfile`
- 如果没有 `lint` script，就删除或注释 lint step
- 如果没有 `test` script，就删除或注释 test step
- 如果没有 `build` script，就删除或注释 build step
- 如果无法从 `package.json` 推断 test 命令，要显式使用 `AskUserQuestion` / `request_user_input`

#### Python

把 `assets/ci/workflows/ci-python.yml` 复制到 `.github/workflows/ci.yml`。

然后定制：

- Python matrix 默认用 `["3.11", "3.12", "3.13"]`
- install 命令通常是 `pip install -e ".[dev]"` 或 `pip install -r requirements-dev.txt`
- test 命令通常是 `pytest`
- 当 Ruff 已配置时，lint 命令使用 `ruff check .`

#### Go

把 `assets/ci/workflows/ci-go.yml` 复制到 `.github/workflows/ci.yml`。

然后：

- 根据 `go.mod` 设置 Go 版本
- 保留 `go test ./...`
- 保留 `go build ./...`
- 如果存在 `.golangci.yml`，加入官方 `golangci-lint` action

#### Rust

把 `assets/ci/workflows/ci-rust.yml` 复制到 `.github/workflows/ci.yml`。

然后：

- 默认使用 stable toolchain，除非项目明确需要 nightly
- 保留 `cargo fmt --check`、`cargo clippy`、`cargo test`、`cargo build`
- 如果同时选择了 security scanning，并且用户明确希望在 CI 里做 Rust 依赖审计，再加 `cargo audit`

#### Other

把 `assets/ci/workflows/ci-generic.yml` 复制到 `.github/workflows/ci.yml`。

然后用真实命令替换占位的 install、test、lint、build。
如果仓库本身无法暴露这些命令，要显式使用 `AskUserQuestion` / `request_user_input`。

如果 `AGENTS.md` 中还没有下面这句话，就补进去：

> `CI: keep .github/workflows/ci.yml aligned with the repository's real install, lint, test, and build commands.`

### 5.2 GitHub Repository Setup

只能使用本 package 自带的 vendored assets：

- `assets/github/templates/pull-request-template.md`
- `assets/github/templates/bug-report.yml`
- `assets/github/templates/feature-request.yml`
- `assets/github/templates/CODEOWNERS.template`
- `assets/github/scripts/configure-branch-protection.sh`

在进行 GitHub API 修改之前，先确认：

```bash
gh auth status
git remote -v
gh repo view --json nameWithOwner --jq .nameWithOwner
```

如果 `gh` 不存在或未登录，要引导用户先安装并认证。

然后：

- 如果缺失，则把 PR 模板复制到 `.github/pull_request_template.md`
- 把 issue templates 复制到 `.github/ISSUE_TEMPLATE/`
- 如果 issue label prefix 不明显，要显式使用 `AskUserQuestion` / `request_user_input`，并同步更新两个 YAML 里的 `labels:`
- 创建 `.github/CODEOWNERS`
  - 单人仓库用 `* @username`
  - 只有在仓库目录结构足够明确时，才做目录级或文件类型级 ownership
  - 如果 ownership 有歧义，要显式使用 `AskUserQuestion` / `request_user_input`
- 对主分支应用 branch protection
  - 需要 1 个 approval
  - dismiss stale reviews
  - 禁用 force pushes 和删除分支
  - required status checks 先留空，等 CI 至少跑过一轮后再补

可以在定制后运行 vendored script，也可以直接调用 `gh api`：

```bash
REPO=$(gh repo view --json nameWithOwner --jq .nameWithOwner)

gh api \
  --method PUT \
  "repos/${REPO}/branches/main/protection" \
  --field required_status_checks='{"strict":true,"contexts":[]}' \
  --field enforce_admins=false \
  --field required_pull_request_reviews='{"required_approving_review_count":1,"dismiss_stale_reviews":true}' \
  --field restrictions=null \
  --field allow_force_pushes=false \
  --field allow_deletions=false
```

如果 `AGENTS.md` 里还没有下面这句话，就补进去：

> `PRs: all pull requests must use the PR template (.github/pull_request_template.md). Branch protection requires at least 1 approving review before merge.`

---

## Step 6: 依赖管理与安全扫描

当用户选择 dependency management、security scanning，或两者都选时执行本节。

### 6.1 Dependency Management

只能使用本 package 自带的 vendored assets：

- `assets/dependencies/config/dependabot-node.yml`
- `assets/dependencies/config/dependabot-python.yml`
- `assets/dependencies/config/dependabot-go.yml`
- `assets/dependencies/config/dependabot-rust.yml`
- `assets/dependencies/config/dependabot-generic.yml`
- `assets/dependencies/workflows/dependabot-auto-merge.yml`

识别仓库里存在的所有 ecosystem：

- `package.json` 对应 `npm`
- `pyproject.toml`、`setup.py` 或 `requirements.txt` 对应 `pip`
- `go.mod` 对应 `gomod`
- `Cargo.toml` 对应 `cargo`
- `github-actions` 永远都要有

按项目实际情况生成 `.github/dependabot.yml`，并确保 `github-actions` ecosystem 也被包含进去。
如果是 polyglot 仓库，要把多个 section 合并到同一个文件中。

默认策略：

- 每周一次 grouped updates
- 只对 patch 和 minor updates 启用 auto-merge

把 `assets/dependencies/workflows/dependabot-auto-merge.yml` 复制到
`.github/workflows/dependabot-auto-merge.yml`。

workflow 推上去之后，如果仓库支持 auto-merge，则启用它：

```bash
REPO=$(gh repo view --json nameWithOwner --jq .nameWithOwner)
gh api --method PATCH "repos/${REPO}" --field allow_auto_merge=true
```

如果 `AGENTS.md` 里还没有下面这句话，就补进去：

> `Dependencies: Dependabot opens PRs for updates automatically. Patch and minor updates are auto-merged; major updates require manual review.`

### 6.2 Security Scanning

只能使用本 package 自带的 vendored assets：

- `assets/security/workflows/codeql.yml`
- `assets/security/workflows/dependency-review.yml`

识别 CodeQL 语言：

- Node 或 web → `javascript-typescript`
- Python → `python`
- Go → `go`
- Rust 或其他不支持的语言 → 跳过 CodeQL

如果当前语言支持 CodeQL：

- 把 `assets/security/workflows/codeql.yml` 复制到 `.github/workflows/codeql.yml`
- 把 matrix 语言改成检测结果

无论如何都要复制 `assets/security/workflows/dependency-review.yml` 到
`.github/workflows/dependency-review.yml`。

对于 Rust 项目，要明确解释 CodeQL 不支持，并推荐：

```bash
cargo install cargo-audit
cargo audit
```

Secret scanning 是仓库设置，不是 workflow 文件。需要引导用户：

1. GitHub 仓库 → Settings → Security & analysis
2. 打开 Secret scanning
3. 如果可用，再打开 Push protection

如果仓库是 public 的，可以尝试通过 `gh api` 开启：

```bash
REPO=$(gh repo view --json nameWithOwner --jq .nameWithOwner)
gh api --method PATCH "repos/${REPO}" \
  --field "security_and_analysis[secret_scanning][status]=enabled" \
  --field "security_and_analysis[secret_scanning_push_protection][status]=enabled"
```

如果 `AGENTS.md` 里还没有下面这句话，就补进去：

> `Security: CodeQL runs on supported languages, dependency review blocks high and critical CVEs in PRs, and the Security tab must stay clean.`

---

## Step 7: GitHub 权限、提交策略与验证

### 7.1 自动化 GitHub 仓库设置

在选中的文件都提交并推送后，再自动化与之对应的 GitHub 设置。

如果配置了 release workflow，确保 GitHub Actions 可以写 release：

```bash
REPO=$(gh repo view --json nameWithOwner --jq .nameWithOwner)

gh api --method PUT "repos/${REPO}/actions/permissions/workflow" \
  --field default_workflow_permissions=write \
  --field can_approve_pull_request_reviews=true
```

如果配置了 dependency management，确保仓库启用 auto-merge：

```bash
gh api --method PATCH "repos/${REPO}" --field allow_auto_merge=true
```

如果配置了 security scanning，则按上面的方式尝试启用 secret scanning；
如果因为 GitHub 方案限制而失败，要明确说明失败原因。

### 7.2 提交这些改动

默认按每个选中 section 拆成聚焦的 conventional commit，除非用户明确要求一次 squashed setup commit。

建议的 commit message：

- scaffold and repo baseline → `chore: initialize project scaffold`
- code quality → `chore: add code quality tooling`
- release workflow → `ci: add release workflow automation`
- CI pipeline → `ci: add project CI pipeline`
- GitHub repository setup → `chore: add GitHub repository configuration`
- dependency management → `chore: add Dependabot dependency management`
- security scanning → `ci: add security scanning workflows`

### 7.3 在宣称成功前先验证

只检查本次实际选中的 section：

- Foundation
  - `README.md`、`LICENSE`、`.gitignore`、`.editorconfig`、`CONTRIBUTING.md` 存在
  - `AGENTS.md` 存在，且 `CLAUDE.md` 是 symlink
- Code quality
  - 配置文件存在
  - 在预期场景下已经安装 husky 或 pre-commit
- Release workflow
  - `release.yml` 存在
  - `scripts/extract-release-notes.sh` 有可执行权限
  - `CHANGELOG.md` 使用带链接的标题
- CI
  - `.github/workflows/ci.yml` 与仓库真实 install / lint / test / build 命令一致
- GitHub repo setup
  - PR template、issue forms、`CODEOWNERS` 存在
  - branch protection 已应用，或者失败原因已经被明确说明
- Dependency management
  - `.github/dependabot.yml` 存在
  - `dependabot-auto-merge.yml` 存在
- Security
  - 语言支持时存在 `codeql.yml`
  - 存在 `dependency-review.yml`
  - 如果无法自动启用 secret scanning，要把后续动作说清楚

### 7.4 最终总结

结尾时用具体 summary，只列出真正执行过的 section，例如：

```text
Setup complete for [project name] ([type] project)

Configured
  [x] scaffold and repo baseline
  [x] release workflow
  [x] CI pipeline
  [x] code quality
  [x] GitHub repository setup
  [x] dependency management
  [x] security scanning

Manual follow-up
  [ ] add required status checks to branch protection after the first CI run
  [ ] enable secret scanning manually if GitHub plan limits blocked automation
```

只列相关的 section、失败项和 follow-up，不要泛化展开。
