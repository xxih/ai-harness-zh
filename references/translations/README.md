# references/translations

这里用于保存外部参考仓库中“核心 prompt 资产”的中文翻译版本。

## 目录约定

- `references/translations/<repo>/`
  - 某个参考仓库的中文翻译根目录
- `references/translations/<repo>/manifest.json`
  - 记录源仓库路径、分支、最近一次审阅时的 upstream commit，以及当前翻译覆盖的源文件哈希
- `references/translations/<repo>/README.md`
  - 记录该仓库当前翻译范围、同步口径和注意事项
- 其余文件尽量镜像源仓库的相对路径，例如：
  - `skills/brainstorming/SKILL.md`
  - `skills/test-driven-development/SKILL.md`

## 当前策略

- 翻译资产默认放在当前仓库内，纳入版本管理
- 源仓库继续放在 `references/repos/<repo>/`，不直接提交外部仓库内容
- 首批先覆盖各仓库最核心、最常被 AI 直接读取的 prompt 资产
- `superpowers` 当前按 `skills/*/SKILL.md` 作为首批范围

## 同步流程

每次准备继续维护某个参考仓库的中文翻译前：

1. 先把 `references/repos/<repo>/` 更新到准备对照的 upstream 版本
2. 记录或确认最新 upstream commit
3. 检查当前翻译覆盖范围内，哪些源文件发生了变化
4. 如有变化，手动同步中文资产
5. 同步完成后，把最新 upstream commit 和当前翻译范围写回 `manifest.json`

## 维护原则

- 先更新源 repo，再判断翻译是否过期
- 只翻译当前明确需要长期复用的核心 prompt 资产
- 若 upstream 变更未影响当前翻译范围，也要先审阅，再更新 `manifest.json`
- 结构性改动后同步更新相关 README、manifest 与说明文档
