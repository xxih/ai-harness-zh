# 内部资产包

`packages/` 用来放**仍属于当前仓库、但已经具备独立主题边界**的资产包。

和 `src/` 的区别：

- `src/` 放跨主题、跨 target 共享的核心源资产
- `packages/` 放已经能独立理解、独立分发、独立维护的主题包
- 这些包仍然属于当前仓库，不属于 `references/repos/`

## 当前包

- `packages/learning-capture/`
  - `learning-capture` skill 与其配套 `_AGENTS.md` 搭配上下文
- `packages/quality-workflows/`
  - `quality-tdd`、`quality-verify`、`quality-review`、`quality-review-feedback` 与 `quality-code-reviewer`
