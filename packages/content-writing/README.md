# content-writing 包

这个包承载平台无关的内容写作内核。

## 组成

- `skills/content-writing/`
  - `content-writing` skill source
- `targets/codex/`
  - `content-writing` 的 Codex target 包

## 包边界

- 只覆盖写作内核：voice capture、结构组织、事实纪律、文风约束与交付前质量检查
- 不负责内容策略、SEO 研究、多平台改写、中文平台排版或发布自动化
- 若后续需要扩展平台层或研究层，优先新增配套 skill，而不是把所有内容生产职责塞进一个 skill

## 维护方式

- 先更新 `skills/content-writing/`
- 再运行 `python3 scripts/sync_codex_targets.py content-writing`
