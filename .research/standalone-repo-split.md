# 可独立能力拆仓记录

## 本次结论

- `learning-capture` + 配套 `_AGENTS` 搭配上下文，已拆到 `references/repos/learning-capture`
- `quality-tdd` / `quality-verify` / `quality-review` / `quality-review-feedback` + `quality-code-reviewer`，已拆到 `references/repos/quality-workflows`
- `quality-router` 已删除，不再保留

## 选择理由

### learning-capture

- 已经是单能力入口
- 自带明确默认落点 `.learned/`
- 配套 `_AGENTS` 上下文本身就围绕这一能力服务
- 更适合作为独立 repo，而不是继续挂在总仓的资产治理域中

### quality-workflows

- 四个 quality skill 本身就是一组完整、可独立使用的质量工作流
- `quality-code-reviewer` 使其具备独立 reviewer 角色
- Codex 运行时配置已经足够形成一个单独 target 包
- `quality-router` 只是入口壳子，没有保留必要

## 当前仓库保留

- workflow 相关共享源资产
- `writing-skills`
- 外部 repo / 翻译 / 研究索引
- 薄 Codex target 包（仅覆盖仍留在当前仓库的共享资产）
