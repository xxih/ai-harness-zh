---
name: scaffold-exercises
description: 创建过 lint 的练习目录结构(含 sections / problems / solutions / explainers)。当用户想搭练习骨架、建练习 stub,或搭新课程章节时使用。
---

# Scaffold Exercises

> 原文:[skills/misc/scaffold-exercises/SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/misc/scaffold-exercises/SKILL.md)

创建能过 `pnpm ai-hero-cli internal lint` 的练习目录结构,然后 `git commit`。

> 说明:这个 skill 是为 Matt 自己的 [Total TypeScript / AI Hero](https://www.aihero.dev) 课程内容仓库设计的,依赖 `ai-hero-cli` 的 linter。仅供参考结构。

## 目录命名

- **Section**:`exercises/` 下 `XX-section-name/`(如 `01-retrieval-skill-building`)
- **Exercise**:某 section 下 `XX.YY-exercise-name/`(如 `01.03-retrieval-with-bm25`)
- Section 号 = `XX`,exercise 号 = `XX.YY`
- 名字用 dash-case(小写、连字符)

## 练习变体

每个练习至少要有一个子目录:

- `problem/` —— 学生工作区,含 TODO
- `solution/` —— 参考实现
- `explainer/` —— 概念材料,无 TODO

搭 stub 时,**默认 `explainer/`**,除非 plan 指定别的。

## 必须文件

每个子目录(`problem/`、`solution/`、`explainer/`)都要有 `readme.md`,要求:

- **非空**(必须有真实内容,哪怕只有一行标题)
- 没有坏链接

搭 stub 时,建一个含标题 + 描述的最小 readme:

```md
# Exercise Title

Description here
```

如果子目录有代码,**还**要 `main.ts`(>1 行)。但 stub 阶段,只有 readme 的练习也 OK。

## 工作流

1. **解析 plan** —— 抽取 section 名、exercise 名、变体类型
2. **建目录** —— 每个路径 `mkdir -p`
3. **建 stub readme** —— 每个变体目录一个 `readme.md` 含标题
4. **跑 lint** —— `pnpm ai-hero-cli internal lint` 验证
5. **修任何错** —— 迭代到 lint 通过

## Lint 规则摘要

linter(`pnpm ai-hero-cli internal lint`)检查:

- 每个练习有子目录(`problem/`、`solution/`、`explainer/`)
- 至少存在 `problem/`、`explainer/`、或 `explainer.1/` 中的一个
- 主子目录里 `readme.md` 存在且非空
- 没有 `.gitkeep` 文件
- 没有 `speaker-notes.md` 文件
- readme 里没有坏链接
- readme 里没有 `pnpm run exercise` 命令
- 除非只有 readme,否则每个子目录都要 `main.ts`

## 移动 / 重命名练习

重新编号或移动练习时:

1. 用 `git mv`(不是 `mv`)重命名目录 —— 保留 git 历史
2. 更新数字前缀维持顺序
3. 移完后重跑 lint

例子:

```bash
git mv exercises/01-retrieval/01.03-embeddings exercises/01-retrieval/01.04-embeddings
```

## 例:从 plan 搭 stub

给定 plan:

```
Section 05: Memory Skill Building
- 05.01 Introduction to Memory
- 05.02 Short-term Memory (explainer + problem + solution)
- 05.03 Long-term Memory
```

建:

```bash
mkdir -p exercises/05-memory-skill-building/05.01-introduction-to-memory/explainer
mkdir -p exercises/05-memory-skill-building/05.02-short-term-memory/{explainer,problem,solution}
mkdir -p exercises/05-memory-skill-building/05.03-long-term-memory/explainer
```

然后建 readme stub:

```
exercises/05-memory-skill-building/05.01-introduction-to-memory/explainer/readme.md -> "# Introduction to Memory"
exercises/05-memory-skill-building/05.02-short-term-memory/explainer/readme.md     -> "# Short-term Memory"
exercises/05-memory-skill-building/05.02-short-term-memory/problem/readme.md       -> "# Short-term Memory"
exercises/05-memory-skill-building/05.02-short-term-memory/solution/readme.md      -> "# Short-term Memory"
exercises/05-memory-skill-building/05.03-long-term-memory/explainer/readme.md      -> "# Long-term Memory"
```
