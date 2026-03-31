# 研究记录

## 任务

检查 `references/repos/agency-agents` 是否已翻译进入 `references/translations/`，若没有则补齐。

## 证据

- `rg -n "agency-agents|Agency Agents|agency agents" references/translations references/README.md README.md packages/README.md` 无命中，说明仓库内没有现成的 `agency-agents` 翻译入口。
- `references/repos/agency-agents` 当前存在，HEAD 为 `6254154899f510eb4a4de10561fecfc1f32ff17f`，分支为 `main`。
- 源仓 `.md` 资产规模较大：
  - 全部 `.md/.sh/.json` 等文件约 822 个
  - 核心业务分组与 `strategy/` 下 `.md` 约 145 个
  - `README.md` 851 行
  - `strategy/nexus-strategy.md` 1110 行

## 候选实现

- 本地既有翻译目录模式：
  - `references/translations/superpowers/`
  - `references/translations/claudeception/`
  - `references/translations/everything-claude-code/`
- 可复用约定：
  - `references/translations/README.md`
  - 各仓库翻译根目录下的 `README.md` 与 `manifest.json`

## 决策

- 结论：`adapt`
- 原因：
  - 该仓库尚未进入 `references/translations/`
  - 直接全量翻译 145 份核心 `.md` 不适合作为当前一次性补录动作
  - 先补一个可维护的首批翻译包更符合现有 `translations` 策略

## 首批范围

- `references/translations/agency-agents/README.md`
- `references/translations/agency-agents/strategy/EXECUTIVE-BRIEF.md`
- `references/translations/agency-agents/strategy/QUICKSTART.md`
- `references/translations/agency-agents/integrations/{aider,claude-code,cursor,github-copilot,mcp-memory,openclaw}/README.md`
- `references/translations/agency-agents/manifest.json`
- `references/translations/README.md` 中补充该仓库说明

## 第二批范围

- `references/translations/agency-agents/strategy/coordination/agent-activation-prompts.md`
- `references/translations/agency-agents/strategy/coordination/handoff-templates.md`
- `references/translations/agency-agents/strategy/runbooks/scenario-startup-mvp.md`
- `references/translations/agency-agents/strategy/runbooks/scenario-enterprise-feature.md`
- `references/translations/agency-agents/strategy/runbooks/scenario-marketing-campaign.md`
- `references/translations/agency-agents/strategy/runbooks/scenario-incident-response.md`
- 同步更新 `references/translations/agency-agents/README.md` 与 `manifest.json`

## 第三批范围

- `references/translations/agency-agents/strategy/playbooks/phase-0-discovery.md`
- `references/translations/agency-agents/strategy/playbooks/phase-1-strategy.md`
- `references/translations/agency-agents/strategy/playbooks/phase-2-foundation.md`
- `references/translations/agency-agents/strategy/playbooks/phase-3-build.md`
- `references/translations/agency-agents/strategy/playbooks/phase-4-hardening.md`
- `references/translations/agency-agents/strategy/playbooks/phase-5-launch.md`
- `references/translations/agency-agents/strategy/playbooks/phase-6-operate.md`
- 同步更新 `references/translations/agency-agents/README.md` 与 `manifest.json`

## 第四批范围

- `references/translations/agency-agents/strategy/nexus-strategy.md`
- 同步更新 `references/translations/agency-agents/README.md` 与 `manifest.json`

## 后续建议

- 若后续确实要长期复用 `agency-agents` 的 agent prompt，再按分组逐批补 `engineering/`、`design/`、`testing/`、`specialized/` 等目录
- 根目录 `README.md` 仍可作为后续导览层补充；真正成本最高的仍是各 division 下的大量 agent prompt
- 对 `integrations/aider/CONVENTIONS.md` 这类 3 万多行的生成产物，不建议优先纳入人工翻译范围
