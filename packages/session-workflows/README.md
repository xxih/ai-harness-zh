# session-workflows 包

这个包承载显式触发的 session 收尾、handoff 与换窗口续跑工作流。

## 组成

- `skills/session-handoff/`
  - 在 section 结束、上下文将满或准备换窗口时，先做 learning 出口判断，再生成 handoff 文档
- `targets/codex/`
  - `session-workflows` 的 Codex target 包

## 设计边界

- 这里只处理“当前 session 如何收尾并交接”，不替代分支收尾、PR 生命周期或默认开发主线
- learning 沉淀仍沿用 `packages/learning-evolution/` 的出口判断，不额外发明第二套记录体系
- handoff 文档默认写入仓库根目录 `.session/`，该目录只作为本地上下文接力材料，不纳入 git 管理
- 这是显式触发能力；只有用户主动要求 session 收尾、handoff、保存上下文或换窗口续跑时才使用

## 维护方式

- 先更新 `skills/`
- 再运行 `python3 scripts/sync_codex_targets.py session-workflows`
