# Out-of-Scope 知识库

> 原文:[OUT-OF-SCOPE.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/triage/OUT-OF-SCOPE.md)

仓库里的 `.out-of-scope/` 目录用来**持久记录被拒的 feature request**。它有两个用途:

1. **机构记忆** —— 一个 feature 当初为啥被拒;别让 issue 关掉后理由也丢了
2. **去重** —— 来了一个和之前被拒的请求匹配的新 issue,skill 能把当时的决策摆出来,而不是重新打嘴仗

## 目录结构

```
.out-of-scope/
├── dark-mode.md
├── plugin-system.md
└── graphql-api.md
```

**一份文件对应一个概念**,不是一份对应一个 issue。多个请求同一件事的 issue 聚到同一份文件。

## 文件格式

写得放松、可读——更像简短的设计文档,而不是数据库条目。用段落、代码样例、举例让理由对第一次接触的人也清楚有用。

```markdown
# Dark Mode

本项目不支持 dark mode 或面向用户的 theming。

## Why this is out of scope

渲染管线假设有一个由 `ThemeConfig` 定义的单一调色板。支持多 theme 会需要:

- 包整棵组件树的 theme context provider
- 每个组件 theme-aware 的样式解析
- 用户 theme 偏好的持久化层

这是一个重大的架构变更,与本项目专注于"内容编写"的方向不符。Theming 是
下游消费者(嵌入或重分发输出的人)的事。

```ts
// 当前的 ThemeConfig 接口并非为运行时切换设计:
interface ThemeConfig {
  colors: ColorPalette; // 单一调色板,构建期解析
  fonts: FontStack;
}
```

## Prior requests

- #42 — "Add dark mode support"
- #87 — "Night theme for accessibility"
- #134 — "Dark theme option"
```

### 文件命名

用简短、描述性的 kebab-case 概念名:`dark-mode.md`、`plugin-system.md`、`graphql-api.md`。浏览目录的人不打开文件也能看出"这是什么被拒了"。

### 写"理由"

理由要有内容——不是"我们不想做",而是为什么。好理由会引用:

- 项目范围或哲学("本项目聚焦 X;theming 是下游的事")
- 技术约束("支持这个要 Y,与我们 Z 架构冲突")
- 战略决策("我们选 A 不是 B,因为...")

理由要**经得起放久**。不要引用临时情况("我们最近太忙了")——那不是真正的拒绝,是延后。

## 何时检查 `.out-of-scope/`

Triage 的第 1 步(采集上下文)时,**读 `.out-of-scope/` 下所有文件**。评估新 issue 时:

- 看请求是否匹配已有 out-of-scope 概念
- 匹配按**概念相似度**,不是关键字——"night theme" 匹配 `dark-mode.md`
- 匹配上就摆给维护者看:"这跟 `.out-of-scope/dark-mode.md` 像——我们以前拒过,理由是 [reason]。你现在还这么想吗?"

维护者可以:

- **确认** —— 新 issue 加到现有文件的 "Prior requests",然后关
- **重新考虑** —— `.out-of-scope` 文件被删或更新,issue 进正常 triage
- **不同意** —— 两个 issue 相关但不同,继续正常 triage

## 何时往 `.out-of-scope/` 写

**只在 enhancement(不是 bug)被以 `wontfix` 拒绝时**。流程:

1. 维护者决定一个 feature request 不在范围内
2. 查是否已有匹配的 `.out-of-scope/` 文件
3. 有:追加到 "Prior requests"
4. 没有:用概念名建新文件,含决策、理由、第一个 prior request
5. 在 issue 上发一条评论解释决策并提到 `.out-of-scope/` 文件
6. 用 `wontfix` 标签关 issue

## 更新或删除 out-of-scope 文件

维护者改主意了:

- 删除 `.out-of-scope/` 文件
- skill 不需要重开旧 issue —— 它们是历史记录
- 触发重新考虑的新 issue 走正常 triage
