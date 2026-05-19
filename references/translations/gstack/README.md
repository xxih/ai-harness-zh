# gstack 中文翻译

## 当前范围

- 源仓库：`references/repos/gstack`
- 当前先覆盖：
  - `README.md` -> `README.zh-CN.md`
  - `AGENTS.md`
  - `CLAUDE.md`
  - `ARCHITECTURE.md`
  - `BROWSER.md`
  - `DESIGN.md`
  - `ETHOS.md`
  - `CONTRIBUTING.md`
  - `docs/skills.md`
  - `docs/ADDING_A_HOST.md`
  - `docs/OPENCLAW.md`
  - `docs/REMOTE_BROWSER_ACCESS.md`
  - `SKILL.md`
  - `*/SKILL.md`
  - `SKILL.md.tmpl`
  - `*/SKILL.md.tmpl`
  - `openclaw/agents-gstack-section.md`
  - `openclaw/gstack-full-CLAUDE.md`
  - `openclaw/gstack-lite-CLAUDE.md`
  - `openclaw/gstack-plan-CLAUDE.md`
  - `review/*.md`
  - `review/specialists/*.md`
  - `qa/references/*.md`
  - `qa/templates/*.md`
  - `cso/ACKNOWLEDGEMENTS.md`
- 暂不覆盖：
  - `CHANGELOG.md`
  - `TODOS.md`
  - 各目录下的实现代码、设计长文、测试与其余非核心说明文件

## 仓库导读

`gstack` 是 Garry Tan 开源的一套 AI engineering workflow。它把 `office-hours`、`plan-ceo-review`、`plan-eng-review`、`review`、`qa`、`ship`、`codex`、`cso` 等角色化 skill 串成完整 sprint 流程，目标是把 Claude Code 这样的 coding agent 用成一个“虚拟工程团队”。

和一些更偏平台能力拆解或 skill-first 流程的参考相比，`gstack` 的特点更明显：

- 强 founder / product 视角，强调先重构问题，再开始实现
- 强 sprint 主线，把 think / plan / build / review / test / ship / reflect 明确串起来
- 强体验导向，把真实浏览器、设计评审、安全审计、第二模型复核都放进同一套操作面
- 明确兼容 Claude Code、Codex、Gemini CLI、Cursor 与 Factory Droid 等多种 host

当前这一版已经覆盖根级主文档、`docs/skills.md`、host onboarding / OpenClaw / remote browser 三份补充文档、根级 `SKILL.md` / `SKILL.md.tmpl`、全部子目录 `*/SKILL.md` / `*/SKILL.md.tmpl`、`openclaw/` 目录下 4 份 orchestrator prompt 资产，以及 `review/*.md`、`review/specialists/*.md`、`qa/references/*.md`、`qa/templates/*.md`、`cso/ACKNOWLEDGEMENTS.md` 这批 skill 支撑资产。其中：

- 根级 `SKILL.md` 重点翻译 gstack 的共享 preamble、全局约束与默认浏览器入口
- 子目录 `*/SKILL.md` 采用“结构化中文译要”方式，保留命令名、路径和协议关键字，重点翻译 skill 的职责、阶段、gate 与交付要求
- `*.tmpl` 模板文件采用“中文模板译要 + 保留 resolver / 占位符”的方式，重点保留生成链路、关键 gate 与模板职责
- `review/specialists/*.md` 与 `qa/*` 支撑文档按原结构翻成中文，便于对照 `/review`、`/qa`、`/ship` 的真实 prompt 依赖
- 重复的 generated shell preamble、内嵌脚本和实现性细节不逐字镜像，统一交给根级 `SKILL.md` 与源仓库源码对照

这样既能把 gstack 的完整 workflow 面翻成中文，又能避免把大量重复生成脚本机械复制进参考资产。

## 同步规则

维护 `gstack` 中文翻译前：

1. 先更新 `references/repos/gstack/` 到准备对照的 upstream 版本
2. 记录最新 upstream commit
3. 检查当前翻译覆盖范围内的源文件是否漂移
4. 如有变化，手动同步本目录下对应中文文件
5. 同步完成后，更新 `references/translations/gstack/manifest.json`

## 翻译原则

- 中文尽量保留原文的产品语气、约束强度和流程顺序
- skill 名称、路径、命令、代码块、工具名与协议关键字保持原文
- 对安装命令、路径约定和 host 相关差异，优先保留原始技术表述，避免误导
- 对 generated 的 `SKILL.md`，优先保留能帮助中文读者理解 workflow 的信息密度；重复 preamble 与实现性脚本按需摘要，而不是机械逐字复制
