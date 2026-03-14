# Alignment Log

## 2026-03-15

- [变更] 用户要求从“先做研究结论，再挑一个试点”调整为“先做研究检索与质量保障两类最小 skill，并在本轮直接完成落地”。
- [偏差] 上一轮将“研究检索”和“质量保障”误解成了面向本仓库 prompt 资产治理的 skill，而不是面向 coding 工作流的 skill。
- [变更] 第一波正确落地范围应调整为两个 coding 方向资产：`search-first` 与 `verification-loop`。
- [变更] 撤回误产出的 `reference-search-first` 与 `asset-review-gate`，改为补齐 `search-first`、`verification-loop` 及其 eval、参考文档和校验约束。
- [歧义] 当前“吸收”口径仍然偏向按参考 skill 名称逐个落地，和用户真正想要的“提炼长处、压缩为更精简能力”不一致。
- [变更] 后续策略应调整为“按能力内核吸收”，而不是 `search-first` / `verification-loop` / `tdd-workflow` / `requesting-code-review` 一项项复刻。
- [偏差] `coding-quality-loop` 的默认入口文案混入了内部设计缘由，例如“你不想分别记忆 TDD、验证、评审三个 skill”，会让用户误以为这是使用前提而不是资产打包方式。
- [变更] `coding-quality-loop` 的默认入口应改为面向 coding 场景、质量阶段和交付判断，不再暴露“为何合并成一个 skill”的内部解释。
- [变更] 同步收紧 `evals/skills/coding-quality-loop.md` 与 `scripts/validate_assets.py`，避免把内部纠正直接外显为用户规则的问题再次回归。
