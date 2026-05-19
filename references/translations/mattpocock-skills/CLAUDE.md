# CLAUDE.md(中文翻译)

> 原文:[CLAUDE.md](https://github.com/mattpocock/skills/blob/main/CLAUDE.md)
>
> 给 Claude Code 看的仓库自维护规则。

---

Skills 按"桶"分目录,挂在 `skills/` 下:

- `engineering/` — 日常代码工作
- `productivity/` — 日常非代码工作流工具
- `misc/` — 保留但不常用
- `personal/` — 跟 Matt 自己环境绑定,不对外推广
- `in-progress/` — 草稿,未发布
- `deprecated/` — 已弃用

`engineering/`、`productivity/`、`misc/` 里的每个 skill 都必须在顶层 `README.md` 里有引用,并在 `.claude-plugin/plugin.json` 里有条目。`personal/`、`in-progress/`、`deprecated/` 里的 skill **不得**出现在以上两个文件中。

顶层 `README.md` 里每个 skill 条目必须把 skill 名链接到它的 `SKILL.md`。

每个 bucket 目录都有自己的 `README.md`,列出该桶下所有 skill,带一行简介,skill 名链接到 `SKILL.md`。
