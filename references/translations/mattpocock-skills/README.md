# Matt Pocock Skills(中文翻译版)

> **来源**:[mattpocock/skills](https://github.com/mattpocock/skills) — Matt Pocock(Total TypeScript 作者)的日常工程 skill 合集。
>
> **原仓库工作副本**:`~/workspace/mattpocock-skills/`(可 `git pull` 跟上游)
>
> **本目录**:对原仓库核心资产的中文翻译。结构镜像原仓库 `skills/<bucket>/<skill>/SKILL.md`。

---

## 这是什么

Matt 自己每天用来做"真实工程"(而不是 vibe coding)的 agent skills。设计原则:

- 小、可适配、可组合
- 模型无关(任何 model 都能用)
- 基于"工程基本功",不是新方法论

Matt 同时反对那些把流程吃掉的方案(GSD、BMAD、Spec-Kit)——他认为它们让 bug 难以排查。

## 解决的四个常见失败模式

| 失败模式 | 解药 |
|---|---|
| **#1 Agent 没做我要的事** | `/grill-me`、`/grill-with-docs`——先把意图聊清楚,再动手 |
| **#2 Agent 啰嗦/绕远** | `CONTEXT.md` 共享语言(术语表),让 agent 说"行话" |
| **#3 代码不工作** | `/tdd` 红绿重构、`/diagnose` 诊断循环 |
| **#4 系统逐渐烂泥球** | `/to-prd`、`/zoom-out`、`/improve-codebase-architecture` 关注模块设计 |

## 仓库结构

```
skills/
├── engineering/     # 日常代码工作(核心)
├── productivity/    # 通用工作流(非代码专属)
├── personal/        # Matt 个人配置(不推广)
├── misc/            # 保留但用得少
├── in-progress/     # 草稿,未发布
└── deprecated/      # 弃用
```

每个 skill 是一个目录,核心是 `SKILL.md`,可能附带其它 `.md` 子文档。

## 安装(原仓库说明)

```bash
npx skills@latest add mattpocock/skills
```

然后跑 `/setup-matt-pocock-skills`,它会问:
- 你用哪个 issue tracker(GitHub / Linear / 本地文件)
- 你 triage 时贴什么标签
- 文档存哪里

## 中文翻译索引

### 顶层文档

- [CLAUDE.md](./CLAUDE.md) — 仓库给 Claude 看的规则
- [CONTEXT.md](./CONTEXT.md) — 共享语言术语表(本仓库自身的)
- [docs/adr/0001-explicit-setup-pointer-only-for-hard-dependencies.md](./docs/adr/0001-explicit-setup-pointer-only-for-hard-dependencies.md) — ADR:setup 指针只在硬依赖上指明

### Engineering(核心)

每天用来做代码工作的 skill。

- **[diagnose](./skills/engineering/diagnose/SKILL.md)** — 难 bug / 性能回退的纪律化诊断循环:复现 → 最小化 → 假设 → 加 log → 修 → 回归测试
- **[grill-with-docs](./skills/engineering/grill-with-docs/SKILL.md)** — Grill 你的计划,同时锻造术语 + 现场更新 `CONTEXT.md` 和 ADR
- **[triage](./skills/engineering/triage/SKILL.md)** — 用 triage 角色状态机走 issue
- **[improve-codebase-architecture](./skills/engineering/improve-codebase-architecture/SKILL.md)** — 借助 `CONTEXT.md` 和 `docs/adr/` 找"加深模块"的机会
- **[setup-matt-pocock-skills](./skills/engineering/setup-matt-pocock-skills/SKILL.md)** — 在每个仓库初始化 issue tracker / triage 标签 / 文档布局
- **[tdd](./skills/engineering/tdd/SKILL.md)** — 红-绿-重构,一次一片垂直切片
- **[to-issues](./skills/engineering/to-issues/SKILL.md)** — 把 plan/spec/PRD 拆成可独立认领的 GitHub issue
- **[to-prd](./skills/engineering/to-prd/SKILL.md)** — 把当前对话上下文凝练成 PRD 并提交为 issue
- **[zoom-out](./skills/engineering/zoom-out/SKILL.md)** — 让 agent 拉远视角讲整体
- **[prototype](./skills/engineering/prototype/SKILL.md)** — 写一次性原型(terminal app 或多套 UI 变体)

### Productivity

不限于代码的通用工作流工具。

- **[caveman](./skills/productivity/caveman/SKILL.md)** — "穴居人"模式:极致压缩沟通,token 砍 ~75%
- **[grill-me](./skills/productivity/grill-me/SKILL.md)** — 让 agent 死磕你的计划,直到决策树每条分支都问透
- **[handoff](./skills/productivity/handoff/SKILL.md)** — 压缩当前对话为交接文档,让另一个 agent 接班
- **[write-a-skill](./skills/productivity/write-a-skill/SKILL.md)** — 写新 skill 时的结构/渐进披露/资源打包

### Misc

留着但不常用。

- **[git-guardrails-claude-code](./skills/misc/git-guardrails-claude-code/SKILL.md)** — Claude Code hook 拦截危险 git 命令
- **[migrate-to-shoehorn](./skills/misc/migrate-to-shoehorn/SKILL.md)** — 把测试里的 `as` 断言迁到 `@total-typescript/shoehorn`
- **[scaffold-exercises](./skills/misc/scaffold-exercises/SKILL.md)** — 生成练习目录结构(sections / problems / solutions / explainers)
- **[setup-pre-commit](./skills/misc/setup-pre-commit/SKILL.md)** — Husky + lint-staged + Prettier + 类型检查 + 测试

### Personal

Matt 自己用的,不推广。

- **[edit-article](./skills/personal/edit-article/SKILL.md)** — 编辑文章
- **[obsidian-vault](./skills/personal/obsidian-vault/SKILL.md)** — Obsidian vault 操作

### In-progress(草稿)

- **[review](./skills/in-progress/review/SKILL.md)** — 双轴 code review
- **[writing-fragments](./skills/in-progress/writing-fragments/SKILL.md)** — 写作:碎片
- **[writing-beats](./skills/in-progress/writing-beats/SKILL.md)** — 写作:节拍
- **[writing-shape](./skills/in-progress/writing-shape/SKILL.md)** — 写作:形状

### Deprecated(未翻译)

`design-an-interface`、`qa`、`request-refactor-plan`、`ubiquitous-language` — 已废弃,跳过翻译。

---

## 翻译说明

- **保留**:代码块、命令、文件路径、变量名、ADR 编号、原文链接(指向原仓库的相对链接保留)
- **意译**:口语化解释、比喻、专有概念配上原词(如"穴居人模式 caveman")
- **跳过**:LICENSE、scripts/(脚本本身,只翻关键注释)、deprecated/

如果原仓库有更新,跑 `~/workspace/mattpocock-skills/` 下 `git pull` 拿最新,然后对照增量翻译这里。
