# subagent多agent技能调研与产出

背景：

- 当前仓库已经沉淀了 `search-first`、`quality-*`、`quality-code-reviewer` 等 coding 资产，但还没有围绕 `subagent` / `multi-agent` / delegation / orchestration 形成成体系的核心资产。
- `references/repos/` 中的 `everything-claude-code`、`oh-my-opencode`、`superpowers` 都已经把多 agent 工作流做到了比较成熟的程度，但三者都带有明显的平台运行时假设，不能直接整仓照搬。
- 这轮任务的目标不是先写运行时，而是先把“哪些 prompt 资产值得吸收、哪些只应留在 target 适配层”研究清楚，再决定第一波要落哪些 `skill / command / agent / eval`。

目标：

- 仔细调研三个参考仓库里与 `subagent` / `multi-agent` / orchestration 直接相关的资产、工作流和平台约束。
- 提炼跨仓库都稳定成立的能力内核，区分适合进入核心资产层的内容和只适合留在 `targets/` 的平台适配内容。
- 为下一步实现提供清晰候选清单，明确首批优先方向、非目标与延后项。

约束：

- 核心资产默认保持工具无关，不把 Claude Code、Codex、OpenCode 的特定 API、hooks、session runtime、tmux pane 管理直接写进 `src/` 核心资产。
- 第一阶段只做研究与方案收敛，不急着实现一整套运行时编排系统。
- 若某个模式本质上只是已有能力的补强，要优先考虑并入现有资产，而不是机械新增同质 skill。
- 产物默认使用中文，保留路径、工具名、配置项等原文。
