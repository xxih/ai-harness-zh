# Issue tracker: GitHub

> 原文:[issue-tracker-github.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/setup-matt-pocock-skills/issue-tracker-github.md)

本仓库的 issue 和 PRD 住在 GitHub Issues。所有操作用 `gh` CLI。

## 约定

- **建 issue**:`gh issue create --title "..." --body "..."`。多行 body 用 heredoc。
- **读 issue**:`gh issue view <number> --comments`,评论用 `jq` 过滤,同时取标签。
- **列 issue**:`gh issue list --state open --json number,title,body,labels,comments --jq '[.[] | {number, title, body, labels: [.labels[].name], comments: [.comments[].body]}]'`,配合 `--label`、`--state` 过滤。
- **评论**:`gh issue comment <number> --body "..."`
- **加/去标签**:`gh issue edit <number> --add-label "..."` / `--remove-label "..."`
- **关闭**:`gh issue close <number> --comment "..."`

仓库从 `git remote -v` 推断 —— `gh` 在 clone 内运行时自动识别。

## skill 说"发到 issue tracker"时

建一条 GitHub issue。

## skill 说"取相关工单"时

跑 `gh issue view <number> --comments`。
