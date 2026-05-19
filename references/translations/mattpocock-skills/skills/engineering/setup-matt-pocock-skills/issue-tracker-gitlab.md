# Issue tracker: GitLab

> 原文:[issue-tracker-gitlab.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/setup-matt-pocock-skills/issue-tracker-gitlab.md)

本仓库的 issue 和 PRD 住在 GitLab Issues。所有操作用 [`glab`](https://gitlab.com/gitlab-org/cli) CLI。

## 约定

- **建 issue**:`glab issue create --title "..." --description "..."`。多行 description 用 heredoc。传 `--description -` 打开编辑器。
- **读 issue**:`glab issue view <number> --comments`。用 `-F json` 拿机器可读输出。
- **列 issue**:`glab issue list -F json`,配合 `--label` 过滤。
- **评论**:`glab issue note <number> --message "..."`。GitLab 把评论叫 "notes"。
- **加/去标签**:`glab issue update <number> --label "..."` / `--unlabel "..."`。多个标签可逗号分隔,或重复 flag。
- **关闭**:`glab issue close <number>`。`glab issue close` 不接受关闭评论,所以**先**用 `glab issue note <number> --message "..."` 发解释,再关。
- **Merge request**:GitLab 把 PR 叫 "merge requests"。用 `glab mr create`、`glab mr view`、`glab mr note` 等——形状跟 `gh pr ...` 一样,只是 `mr` 替 `pr`,`note`/`--message` 替 `comment`/`--body`。

仓库从 `git remote -v` 推断 —— `glab` 在 clone 内运行时自动识别。

## skill 说"发到 issue tracker"时

建一条 GitLab issue。

## skill 说"取相关工单"时

跑 `glab issue view <number> --comments`。
