# references

这里用于放仓库级外部参考资料入口，尤其是供本地 AI 工具直接读取的外部代码仓库。

## 目录说明

- `references/repos/`：本地外部参考仓库目录
- `references/translations/`：外部参考仓库核心 prompt 的中文翻译资产

## 设计目标

- 外部参考仓库和当前工作区放在同一个根目录下，方便 AI 工具直接读取
- 外部仓库不纳入当前仓库的 git 版本管理，避免污染 `git status`
- 约定一个固定位置，减少每次任务都要重新说明参考路径
- 把不准备分发成 package 的中文翻译资产保留在显眼的参考资料入口

## 约定

- `references/repos/` 只承载外部参考仓库，不承载当前仓库自己的真实资产
- `references/translations/` 承载当前仓库维护的中文翻译资产；这类资料默认不作为分发 package 组织
- 如果需要沉淀可版本化的笔记或提炼结果，请放回当前仓库正式目录，而不是直接改外部参考仓库
- 如果需要沉淀外部 prompt 的中文翻译，请放到 `references/translations/<repo>/`
- 引用时尽量给 AI 工具明确路径，例如 `references/repos/oh-my-opencode/README.md`
