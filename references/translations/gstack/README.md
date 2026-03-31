# gstack 中文翻译

## 当前范围

- 源仓库：`references/repos/gstack`
- 当前先覆盖：
  - `README.md` -> `README.zh-CN.md`
  - `AGENTS.md`
  - `CLAUDE.md`
  - `ARCHITECTURE.md`
  - `BROWSER.md`
  - `ETHOS.md`
  - `CONTRIBUTING.md`
- 暂不覆盖：
  - `SKILL.md`
  - `docs/skills.md`
  - 各子目录下的 skill 文档与实现代码

## 仓库导读

`gstack` 是 Garry Tan 开源的一套 AI engineering workflow。它把 `office-hours`、`plan-ceo-review`、`plan-eng-review`、`review`、`qa`、`ship`、`codex`、`cso` 等角色化 skill 串成完整 sprint 流程，目标是把 Claude Code 这样的 coding agent 用成一个“虚拟工程团队”。

和一些更偏平台能力拆解或 skill-first 流程的参考相比，`gstack` 的特点更明显：

- 强 founder / product 视角，强调先重构问题，再开始实现
- 强 sprint 主线，把 think / plan / build / review / test / ship / reflect 明确串起来
- 强体验导向，把真实浏览器、设计评审、安全审计、第二模型复核都放进同一套操作面
- 明确兼容 Claude Code、Codex、Gemini CLI、Cursor 与 Factory Droid 等多种 host

当前这一版已经覆盖根级主文档，优先把它的定位、安装方式、工作流主线、工程约定、浏览器内核、builder 哲学和贡献方式纳入中文参考。体量最大的 `docs/skills.md` 与各子目录 skill 文档仍待继续扩展。

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
- 当前只覆盖入口资料，不把 generated 或实现细节文档一次性整仓翻完
