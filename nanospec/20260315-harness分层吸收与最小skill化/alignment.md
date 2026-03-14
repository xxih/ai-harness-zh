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
- [变更] 用户要求对质量方向做更细的补充研究，不只保留抽象分类，还要把 `references/repos/` 中相关 prompt 文件逐个盘点出来，比较差异、重合点和共性。
- [变更] 本轮新增研究产物 `assets/quality-prompt-landscape.md`，作为质量方向吸收判断的证据层，而不是只靠已有 `reference-map.md` 的摘要结论。
- [变更] 用户明确指出应更积极吸收 `superpowers`，并认为 multiagent 已是 Codex、OpenCode、Claude Code 的常见能力，不应再作为主要阻塞条件。
- [变更] 后续文档与 skill 约束需要把 multiagent 从“天然延后项”改为“可选执行路径”，重点只保留对平台绑定 runtime 的收敛。
- [变更] 用户进一步要求质量相关资产以 `superpowers` 为主做中文迁移，并拆成同一前缀的 skill 家族，而不是继续维持单个 `coding-quality-loop`。
- [变更] 当前仓库质量资产命名调整为 `quality-*`，并新增 `quality-router` 作为 `commands/` 的手动触发平替。
