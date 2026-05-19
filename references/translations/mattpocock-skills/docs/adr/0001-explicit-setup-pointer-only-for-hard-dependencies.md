# ADR 0001:setup 指针只在硬依赖上显式标注

> 原文:[docs/adr/0001-explicit-setup-pointer-only-for-hard-dependencies.md](https://github.com/mattpocock/skills/blob/main/docs/adr/0001-explicit-setup-pointer-only-for-hard-dependencies.md)

---

Engineering skill 都依赖"每仓库配置"(issue tracker、triage 标签词表、领域文档布局),这些配置由 `/setup-matt-pocock-skills` 播种。

有些 skill 离了这些配置就根本干不了活——它们必须往一个具体的 issue tracker 发,或者必须打一个具体的标签字符串。

另一些 skill 只是用它来"锐化输出"(术语、ADR 感知),没配置也能用,只是没那么锋利。

我们把这两类拆成 **硬依赖** 和 **软依赖**:

- **硬依赖**(`to-issues`、`to-prd`、`triage`)——明文写一行:
  > "…应该已经提供给你了——没有的话跑 `/setup-matt-pocock-skills`。"
  没有这层映射,输出是**错的**,不是"差点意思"。

- **软依赖**(`diagnose`、`tdd`、`improve-codebase-architecture`、`zoom-out`)——只在散文里含糊提一句"项目的领域术语表"和"你正在动的区域的 ADR"。文档不在也能跑,输出只是没那么锐利。

这种切分让软依赖 skill 保持 token 轻量,也避免在没有"承重"作用的地方傻乎乎地复制粘贴 setup 指针。
