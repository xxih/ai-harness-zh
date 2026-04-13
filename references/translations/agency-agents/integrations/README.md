# Integrations

这个目录保存 The Agency 面向已支持 agentic coding 工具的集成说明和转换产物。

## 已支持的工具

- **[Claude Code](#claude-code)**：`.md` agents，直接使用仓库原生格式
- **[GitHub Copilot](#github-copilot)**：`.md` agents，直接使用仓库原生格式
- **[Antigravity](#antigravity)**：每个 agent 一个 `SKILL.md`，位于 `antigravity/`
- **[Gemini CLI](#gemini-cli)**：extension + `SKILL.md` 文件，位于 `gemini-cli/`
- **[OpenCode](#opencode)**：`.md` agent 文件，位于 `opencode/`
- **[OpenClaw](#openclaw)**：以 `SOUL.md` + `AGENTS.md` + `IDENTITY.md` 组成的 workspace
- **[Cursor](#cursor)**：`.mdc` rule 文件，位于 `cursor/`
- **[Aider](#aider)**：`aider/` 下的 `CONVENTIONS.md`
- **[Windsurf](#windsurf)**：`windsurf/` 下的 `.windsurfrules`

## 快速安装

```bash
# 自动为所有已检测到的工具安装
./scripts/install.sh

# 安装指定的 home 级工具
./scripts/install.sh --tool antigravity
./scripts/install.sh --tool copilot
./scripts/install.sh --tool openclaw
./scripts/install.sh --tool claude-code

# Gemini CLI 在全新 clone 后需要先生成 integration 文件
./scripts/convert.sh --tool gemini-cli
./scripts/install.sh --tool gemini-cli
```

对于 OpenCode、Cursor、Aider、Windsurf 这类项目级工具，请按各自章节里的方式，从目标项目根目录执行安装器。

## 重新生成 integration 文件

如果你新增或修改了 agents，请重新生成所有 integration 文件：

```bash
./scripts/convert.sh
```

---

## Claude Code

The Agency 最初就是为 Claude Code 设计的，不需要转换，agents 可以原生使用。

```bash
cp -r <category>/*.md ~/.claude/agents/
# 或一次性全部安装：
./scripts/install.sh --tool claude-code
```

细节见 [claude-code/README.md](claude-code/README.md)。

---

## GitHub Copilot

The Agency 同样原生支持 GitHub Copilot。agents 可以不经转换，直接复制到 `~/.github/agents/` 和 `~/.copilot/agents/`。

```bash
./scripts/install.sh --tool copilot
```

细节见 [github-copilot/README.md](github-copilot/README.md)。

---

## Antigravity

Skills 会安装到 `~/.gemini/antigravity/skills/`。每个 agent 都会变成一个独立 skill，并加上 `agency-` 前缀，避免命名冲突。

```bash
./scripts/install.sh --tool antigravity
```

细节见 [antigravity/README.md](antigravity/README.md)。

---

## Gemini CLI

Agents 会被打包成一个 Gemini CLI extension，并带有独立的 skill 文件。该 extension 会安装到 `~/.gemini/extensions/agency-agents/`。由于 Gemini manifest 和 skill 目录属于生成产物，从全新 clone 安装前需要先运行 `./scripts/convert.sh --tool gemini-cli`。

```bash
./scripts/convert.sh --tool gemini-cli
./scripts/install.sh --tool gemini-cli
```

细节见 [gemini-cli/README.md](gemini-cli/README.md)。

---

## OpenCode

每个 agent 会变成 `.opencode/agents/` 下的项目级 `.md` 文件。

```bash
cd /your/project && /path/to/agency-agents/scripts/install.sh --tool opencode
```

细节见 [opencode/README.md](opencode/README.md)。

---

## OpenClaw

每个 agent 会变成一个 OpenClaw workspace，包含 `SOUL.md`、`AGENTS.md` 和 `IDENTITY.md`。

安装前，先生成 OpenClaw workspaces：

```bash
./scripts/convert.sh --tool openclaw
```

然后执行安装：

```bash
./scripts/install.sh --tool openclaw
```

细节见 [openclaw/README.md](openclaw/README.md)。

---

## Cursor

每个 agent 会变成一条 `.mdc` rule。规则是项目级作用域，因此需要从项目根目录运行安装器。

```bash
cd /your/project && /path/to/agency-agents/scripts/install.sh --tool cursor
```

细节见 [cursor/README.md](cursor/README.md)。

---

## Aider

所有 agents 会被汇总成一个 `CONVENTIONS.md` 文件。只要该文件位于项目根目录，Aider 就会自动读取。

```bash
cd /your/project && /path/to/agency-agents/scripts/install.sh --tool aider
```

细节见 [aider/README.md](aider/README.md)。

---

## Windsurf

所有 agents 会被汇总成一个 `.windsurfrules` 文件，放在你的项目根目录。

```bash
cd /your/project && /path/to/agency-agents/scripts/install.sh --tool windsurf
```

细节见 [windsurf/README.md](windsurf/README.md)。
