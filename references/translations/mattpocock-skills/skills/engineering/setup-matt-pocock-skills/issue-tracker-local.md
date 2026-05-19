# Issue tracker: 本地 Markdown

> 原文:[issue-tracker-local.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/setup-matt-pocock-skills/issue-tracker-local.md)

本仓库的 issue 和 PRD 是 `.scratch/` 下的 markdown 文件。

## 约定

- **一个 feature 一个目录**:`.scratch/<feature-slug>/`
- **PRD** 在 `.scratch/<feature-slug>/PRD.md`
- **实现 issue** 在 `.scratch/<feature-slug>/issues/<NN>-<slug>.md`,从 `01` 开始编号
- **Triage 状态** 记在每个 issue 文件靠顶的 `Status:` 行(角色字符串见 `triage-labels.md`)
- **评论和讨论历史** 追加到文件底部 `## Comments` 标题下

## skill 说"发到 issue tracker"时

在 `.scratch/<feature-slug>/` 下建新文件(目录不存在就建)。

## skill 说"取相关工单"时

读引用路径处的文件。用户通常会直接传路径或 issue 编号。
