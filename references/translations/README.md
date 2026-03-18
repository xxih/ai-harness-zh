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

每次准备继续维护某个参考仓库的中文翻译前，先执行：

```bash
python3 scripts/reference_translation_sync.py check <repo> --pull
```

含义：

1. 先把 `references/repos/<repo>/` fast-forward 到远端最新版本
2. 检查 upstream commit 是否变了
3. 检查当前翻译覆盖范围内的源文件内容哈希是否变了
4. 如果任一项变化，提示需要重新审阅并同步中文资产

同步完翻译后，再执行：

```bash
python3 scripts/reference_translation_sync.py snapshot <repo>
```

这会把最新 upstream commit 和当前翻译范围内的源文件哈希写回 `manifest.json`。

## 维护原则

- 先更新源 repo，再判断翻译是否过期
- 只翻译当前明确需要长期复用的核心 prompt 资产
- 若 upstream 变更未影响当前翻译范围，也要先审阅，再更新 `manifest.json`
- 结构性改动后运行 `python3 scripts/validate_assets.py`
