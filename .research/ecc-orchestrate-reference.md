# ECC 最新状态与 orchestrate 参考意义

## 任务目标

- 确认当前仓库使用的 ECC 参考是否已经更新到最新 upstream
- 判断 ECC 的 `commands/orchestrate.md` 对当前仓库是否有继续吸收价值

## 候选来源

- 本仓库已有吸收结果：
  - `packages/agent-orchestration/skills/agent-orchestration/SKILL.md`
  - `nanospec/20260315-subagent多agent技能调研与产出/assets/subagent-multi-agent-landscape.md`
- ECC 当前 canonical：
  - `references/repos/everything-claude-code`
- ECC 中文参考镜像：
  - `references/translations/everything-claude-code/README.md`
  - `references/translations/everything-claude-code/docs/zh-CN/commands/orchestrate.md`

## 最新状态结论

- 2026-03-23 已将 `references/repos/everything-claude-code` 快进到 upstream 最新 `main`
- 当前 canonical HEAD 为 `bacc585b877b4426627d1cc478e1f1e5eb0c4f94`
- 之前翻译导入所记录的 canonical commit 为 `fdea3085a76c842edea49a72ea695ccc7ff537ed`
- 从 `fdea3085` 到当前 upstream，ECC 新增/修改了大量当前翻译覆盖范围内的文件，包括：
  - `README.md`
  - `commands/orchestrate.md`
  - 多个 `docs/zh-CN/commands/*`
  - 多个 `docs/zh-CN/skills/*`
- 因此：ECC 的 canonical 参考仓已经是最新；但 `references/translations/everything-claude-code/` 这层中文镜像当前不是最新译稿

## orchestrate 内容拆解

ECC `commands/orchestrate.md` 当前稳定表达了四类东西：

1. 工作流路由
   - `feature / bugfix / refactor / security` 映射到固定 agent 序列
2. 交接契约
   - `Context / Findings / Files Modified / Open Questions / Recommendations`
3. 汇总产物
   - 最终 `ORCHESTRATION REPORT`
4. 平台运行时控制平面
   - `tmux + git worktree + seedPaths + orchestration-status.js`

## 对当前仓库的参考意义

### 可直接继续借鉴

- `workflow-type -> stage sequence`
  - 这类“任务类型到稳定阶段顺序”的路由，适合继续沉淀为仓库自有 workflow 资产
- `handoff/report contract`
  - 交接格式和最终汇总格式适合作为主 agent 回收子任务结果的模板
- `control plane` 视角
  - 把会话、分支、diff、审批、遥测显式化，对以后做 target 侧脚本或 command 有价值

### 当前仓库已经吸收过的部分

- `packages/agent-orchestration/skills/agent-orchestration/SKILL.md` 已经吸收了更通用、平台无关的核心：
  - 角色分层
  - 固定阶段顺序
  - 单任务委派
  - 并行独立性判断
  - 结果回收与验证门禁
- `nanospec/20260315-subagent多agent技能调研与产出/assets/subagent-multi-agent-landscape.md` 也已经明确把 ECC 的稳定价值归纳为：
  - workflow-type -> agent sequence
  - handoff / report contract
  - 外部编排的显式状态文件

### 不应直接照搬的部分

- `orchestrate-worktrees.js`
- `tmux pane` 编排
- `seedPaths`
- `orchestration-status.js`
- 任何强绑定 Claude / ECC 运行时目录和脚本约定的 command 壳

这些都更适合作为未来 `targets/<tool>/` 或脚本层参考，而不是当前仓库核心 prompt/skill 本体。

## 决策

- 结论：`adapt`
- 不建议把 ECC 的 `/orchestrate` 原样搬进当前仓库
- 建议保留两层吸收方式：
  - 核心层：继续维持 `agent-orchestration` 这种平台无关 skill
  - 适配层：若以后确实需要 command，再围绕当前仓库自己的 target 能力补一个薄路由 command，而不是复刻 ECC 的 tmux/worktree 运行时

## 下一步建议

1. 若目标是“让 ECC 中文参考也最新”，先按 canonical HEAD 重新筛一遍 `README` 与 `docs/zh-CN/**` 命中的变更文件，再分批同步中文镜像
2. 若目标是增强本仓库多 agent 入口，可优先考虑新增一个薄命令壳，职责只做：
   - 选择 workflow type
   - 产出 handoff/report 模板
   - 路由到现有 `agent-orchestration` 与 `quality-*` 资产
3. 在没有 target 侧 worktree/tmux 运行时前，不建议把 ECC 的控制平面脚本语义写进核心 skill
