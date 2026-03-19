# references

这里用于放仓库级参考资料，尤其是供本地 AI 工具直接读取的外部代码仓库与本地拆出的独立 repo。

## 目录说明

- `references/repos/`：本地外部参考仓库与本地拆出 repo 的目录
- `references/translations/`：外部参考仓库核心 prompt 的中文翻译资产

## 设计目标

- 把外部参考 repo、已拆独立 repo 和当前工作区放在同一个根目录下，方便 AI 工具直接读取
- 外部仓库和拆出 repo 不纳入当前仓库的 git 版本管理，避免污染 `git status`
- 为总仓之外的单主题能力提供固定索引位置
- 把需要长期复用的中文翻译沉淀为当前仓库自己的版本化资产

## 约定

- `references/repos/` 下的内容默认不提交到当前仓库
- 如果某个能力已经拆成独立 repo，优先把完整实现放在这里，而不是再塞回当前总仓
- 如果需要沉淀可版本化的笔记、翻译或高层说明，再回写当前仓库的正式目录
- 引用时尽量给 AI 工具明确路径，例如 `references/repos/quality-workflows/README.md`
