# superpowers 核心 prompt 翻译方案研究

## 要解决的问题

- 在当前仓库里增加一个可版本化目录，用于沉淀外部参考仓库的中文 prompt 翻译。
- 首批先覆盖 `references/repos/superpowers`。
- 后续每次继续维护翻译前，都要先确认参考仓库是否已经更新；若更新，需要同步审阅并更新中文资产。

## 本地与外部候选

- 本地现状
  - `references/repos/` 已作为外部参考仓库固定入口，但没有已版本化的中文翻译目录。
  - `scripts/validate_assets.py` 已负责结构校验，适合补充最小目录约束。
- 外部来源
  - `references/repos/superpowers/skills/*/SKILL.md`
  - `references/repos/superpowers/README.md`

## 候选方案

### 方案 A：把翻译直接写回 `references/repos/<repo>/`

- 优点
  - 路径最短，源文和译文挨在一起。
- 缺点
  - `references/repos/` 默认不纳入当前仓库版本管理。
  - 容易污染外部参考仓库，不符合“不要直接改外部仓库”的约定。

### 方案 B：在 `src/` 下建一个专门领域存放翻译

- 优点
  - 完全纳入正式资产层。
- 缺点
  - 这些内容本质上是“外部仓库参考翻译”，不是当前仓库核心 tool-neutral 资产。
  - 会混淆 `src/` 的职责边界。

### 方案 C：在 `references/` 下新增已版本化翻译目录，并为每个 repo 记录同步元数据

- 优点
  - 语义清晰：源 repo 仍在 `references/repos/`，中文翻译则在 `references/translations/`。
  - 可以保留 mirror 风格路径，方便对照。
  - 可以通过脚本记录 upstream commit 与源文件哈希，做确定性同步检查。
- 缺点
  - 需要维护一份 manifest。

## 决策

- 结论：`adapt` 方案 C。
- 目录定为 `references/translations/<repo>/`。
- 通过 `manifest.json` 记录：
  - 源 repo 路径、远端、分支
  - 最近一次审阅对应的 upstream commit
  - 当前翻译覆盖范围与源文件哈希
- 通过 `scripts/reference_translation_sync.py` 提供：
  - `check <repo> --pull`：先拉最新，再检查是否过期
  - `snapshot <repo>`：翻译同步完成后回写元数据

## 首批范围

- `superpowers` 先覆盖 `skills/*/SKILL.md`
- 暂不覆盖 supporting references、helper prompt、agents、commands

## 后续建议

- 后续新增 repo 时，沿用同一目录与 manifest 结构。
- 如果某个 repo 的“核心 prompt”不止 `skills/*/SKILL.md`，再按 repo 级 README 单独扩大范围。
