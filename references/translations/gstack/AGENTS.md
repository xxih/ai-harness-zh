# gstack — AI Engineering Workflow

gstack 是一组 `SKILL.md` 文件的集合，为 AI agents 提供面向软件开发的结构化角色。每个 skill 都是一个 specialist：CEO reviewer、eng manager、designer、QA lead、release engineer、debugger，等等。

## 可用 skills

skills 放在 `.agents/skills/` 里。按名字直接调用即可，例如 `/office-hours`。

| Skill | 它做什么 |
|-------|---------|
| `/office-hours` | 从这里开始。在你写代码前重构你的产品想法。 |
| `/plan-ceo-review` | CEO 级评审：在需求里找出 10-star product。 |
| `/plan-eng-review` | 锁定架构、数据流、边界情况和测试。 |
| `/plan-design-review` | 给每个设计维度打 0-10 分，并解释 10 分长什么样。 |
| `/design-consultation` | 从零建立完整 design system。 |
| `/review` | 落地前 PR review。找出那些能过 CI、却会在生产出事的 bug。 |
| `/debug` | 系统化 root-cause debugging。先调查，后修复。 |
| `/design-review` | 设计审计 + 修复循环，按 atomic commits 落地。 |
| `/qa` | 打开真实浏览器，找 bug，修 bug，再重新验证。 |
| `/qa-only` | 和 `/qa` 相同，但只出报告，不改代码。 |
| `/ship` | 跑测试、做 review、push、开 PR。一个命令。 |
| `/document-release` | 把所有文档更新到和你刚刚 ship 的内容一致。 |
| `/retro` | 每周 retro，含按人拆分和 shipping streaks。 |
| `/browse` | 无头浏览器，真实 Chromium、真实点击，单命令约 100ms。 |
| `/setup-browser-cookies` | 从你的真实浏览器导入 cookies，用于已登录测试。 |
| `/careful` | 在 destructive commands 前提醒，例如 `rm -rf`、`DROP TABLE`、force-push。 |
| `/freeze` | 把编辑锁定在一个目录内。是硬阻止，不只是提醒。 |
| `/guard` | 一次性同时开启 careful + freeze。 |
| `/unfreeze` | 解除目录编辑限制。 |
| `/gstack-upgrade` | 把 gstack 升到最新版。 |

## 构建命令

```bash
bun install              # 安装依赖
bun test                 # 跑测试（免费，<5s）
bun run build            # 生成文档并编译二进制
bun run gen:skill-docs   # 从模板重新生成 SKILL.md 文件
bun run skill:check      # 查看所有 skills 的健康面板
```

## 关键约定

- `SKILL.md` 文件是从 `.tmpl` 模板**生成**的。编辑模板，不要直接改输出文件。
- 运行 `bun run gen:skill-docs --host codex` 可以重新生成面向 Codex 的输出。
- browse binary 提供无头浏览器访问。skill 里统一用 `$B <command>`。
- safety skills（`careful`、`freeze`、`guard`）使用内联 advisory prose，涉及 destructive operations 时始终先确认。
