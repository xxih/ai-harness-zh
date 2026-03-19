# references

这里用于放仓库级参考资料，尤其是供本地 AI 工具直接读取的外部代码仓库。

## 目录说明

- `references/repos/`：本地外部参考仓库目录
- `references/translations/`：外部参考仓库核心 prompt 的中文翻译资产

## 设计目标

- 把外部参考 repo 和当前工作区放在同一个根目录下，方便 AI 工具直接读取
- 外部仓库不纳入当前仓库的 git 版本管理，避免污染 `git status`
- 为“已经独立存在的单主题 repo / target 包”提供固定索引位置
- 把需要长期复用的中文翻译沉淀为当前仓库自己的版本化资产

## 使用方式

推荐两种放法：

1. clone 外部仓库到 `references/repos/<repo-name>/`
2. 把你本机已有仓库软链接到 `references/repos/<repo-name>`

示例：

```bash
git clone <repo-url> references/repos/oh-my-opencode
ln -s /absolute/path/to/everything-claude-code references/repos/everything-claude-code
```

## 约定

- `references/repos/` 下的内容默认不提交到当前仓库
- 如果某个能力已经拆成独立 repo，优先把它放在这里作为参考或对照，而不是把完整实现重新塞回当前仓库
- 如果需要沉淀可版本化的笔记或提炼结果，请放回当前仓库的正式目录，而不是直接改外部参考仓库
- 如果需要沉淀外部 prompt 的中文翻译，请放到 `references/translations/<repo>/`
- 引用时尽量给 AI 工具明确路径，例如 `references/repos/oh-my-opencode/README.md`
- 如果要在该目录内批量搜索，优先使用显式路径或 `rg -uu references/repos`，因为默认 git-aware 搜索可能会跳过被忽略目录
