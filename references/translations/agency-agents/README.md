# agency-agents 中文翻译

## 当前范围

- 源仓库：`references/repos/agency-agents`
- 当前先覆盖：
  - `strategy/EXECUTIVE-BRIEF.md`
  - `strategy/QUICKSTART.md`
  - `strategy/nexus-strategy.md`
  - `strategy/coordination/agent-activation-prompts.md`
  - `strategy/coordination/handoff-templates.md`
  - `strategy/playbooks/*.md`
  - `strategy/runbooks/scenario-startup-mvp.md`
  - `strategy/runbooks/scenario-enterprise-feature.md`
  - `strategy/runbooks/scenario-marketing-campaign.md`
  - `strategy/runbooks/scenario-incident-response.md`
  - `integrations/aider/README.md`
  - `integrations/README.md`
  - `integrations/antigravity/README.md`
  - `integrations/claude-code/README.md`
  - `integrations/cursor/README.md`
  - `integrations/gemini-cli/README.md`
  - `integrations/github-copilot/README.md`
  - `integrations/mcp-memory/README.md`
  - `integrations/opencode/README.md`
  - `integrations/openclaw/README.md`
  - `integrations/windsurf/README.md`
- 当前不覆盖：
  - 根目录 `README.md` 的整份逐段翻译
  - 各 division 下的大批 agent prompt
  - `integrations/aider/CONVENTIONS.md` 这类生成型聚合文件

## 仓库导读

`agency-agents` 是一个多角色 agent prompt 仓库。源仓把 prompt 资产按 division 组织，覆盖工程、设计、营销、产品、项目管理、测试、支持、空间计算与 specialized 等方向，并提供一套名为 `NEXUS` 的多 agent 协作方法。

当前这份中文翻译先覆盖“怎么用这套体系”的入口资料，而不是一次性全量翻译所有 agent prompt。这样做的目的有两个：

- 先把最容易复用的战略导读和工具接入说明纳入本仓库
- 把翻译范围、同步口径和 upstream commit 固化下来，便于后续按需继续扩展

## 目录说明

- `strategy/EXECUTIVE-BRIEF.md`
  - NEXUS 的高层概览、收益、交付物和部署模式
- `strategy/QUICKSTART.md`
  - 5 分钟上手指南，适合快速理解三种运行模式和常用激活 prompt
- `strategy/nexus-strategy.md`
  - NEXUS 的完整操作纲领，覆盖 operating model、质量门禁、handoff、风险与激活模板
- `strategy/coordination/*.md`
  - agent 激活 prompt 与标准 handoff 模板
- `strategy/playbooks/*.md`
  - 覆盖从 discovery 到 operate 的 7 阶段执行手册
- `strategy/runbooks/*.md`
  - 针对 Startup MVP、Enterprise Feature、Marketing Campaign、Incident Response 的场景化流程
- `integrations/README.md` 与 `integrations/*/README.md`
  - integrations 总览页与全部工具接入说明

## 同步规则

维护 `agency-agents` 中文翻译前：

1. 先更新 `references/repos/agency-agents/` 到准备对照的 upstream 版本
2. 记录最新 upstream commit
3. 检查当前翻译覆盖范围内的源文件是否发生变化
4. 如有变化，手动同步本目录下对应中文文件
5. 同步完成后，更新 `references/translations/agency-agents/manifest.json`

## 翻译原则

- 中文尽量保持原文的约束、流程顺序和指令强度
- agent 名称、路径、命令、代码块、frontmatter 字段与协议关键字保持原文
- 对明显是 generated 或聚合产物的大文件，优先记录范围，不强行一次性全量翻译
