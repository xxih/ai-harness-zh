## 1. 已完成

验收条件：当前任务目录已建立，并形成第一轮可指导后续实现的研究结论。

- [x] 1.1 创建 `nanospec/20260315-subagent多agent技能调研与产出/` 任务骨架，并写入 `.nanospec/.current`。
- [x] 1.2 盘点当前仓库已有 `search-first`、`quality-*`、`quality-code-reviewer` 等相关资产，识别当前缺口。
- [x] 1.3 调研 `references/repos/everything-claude-code` 中与 subagent / orchestration 相关的关键资产与平台前提。
- [x] 1.4 调研 `references/repos/superpowers` 中与 subagent-driven development / parallel delegation / review gate 相关的关键资产与平台前提。
- [x] 1.5 调研 `references/repos/oh-my-opencode` 中与 planner / orchestrator / background agents / parallel explore 相关的关键资产与平台前提。
- [x] 1.6 产出 `assets/subagent-multi-agent-landscape.md`，汇总三仓库研究结论、跨仓库稳定模式与候选资产方向。
- [x] 1.7 回写 `brief.md`、`outputs/1-spec.md`、`outputs/2-plan.md` 与本任务清单。

## 2. 下一步候选

验收条件：确定第一波真正进入核心资产层的条目，并收敛命名与边界。

- [x] 2.1 执行 `/align`，根据用户新要求把第一波从多个分立资产收敛为一个聚合型 `agent-orchestration` skill。
- [ ] 2.2 明确 `iterative-retrieval` 应独立成 skill，还是并入现有 `search-first`。
- [ ] 2.3 明确 `verification-gate` 是否需要新增资产，还是复用现有 `quality-verify`。
- [x] 2.4 为 `agent-orchestration` 先写 `evals/`，约束角色分层、单任务委派、并行判定、反重复规则和验证门禁。

## 3. 后续实现

验收条件：首批核心资产落地，并完成最小分发与校验。

- [x] 3.1 落地 `src/skills/agent-orchestration/`，用一个 skill 覆盖主 agent 编排职责。
- [x] 3.2 更新对应 `evals/skills/agent-orchestration.md`。
- [x] 3.3 更新 `README.md`，按类别纳入新资产。
- [x] 3.4 更新 `scripts/validate_assets.py`，覆盖新 skill 的最小确定性约束。
- [x] 3.5 运行 `python3 scripts/sync_targets.py codex`，同步 `targets/codex`。
- [x] 3.6 运行 `python3 scripts/validate_assets.py`，确认结构校验通过。

## 4. 明确延后项

验收条件：这些内容被清晰记录，但不进入第一波实现范围。

- [ ] 4.1 暂不把 tmux、background polling、session lineage、pane 管理等运行时实现纳入核心资产层。
- [ ] 4.2 暂不直接移植 OpenCode hooks、Claude Code bootstrap、平台插件装配代码。
- [ ] 4.3 暂不实现大而全的一体化 harness 或完整 multi-agent runtime。
