# 规格说明：subagent多agent技能调研与产出

## 本阶段目标

当前阶段只做“研究与收敛”，不直接实现完整多 agent 运行时。交付目标是：

- 盘点三个参考仓库中与 `subagent` / `multi-agent` / orchestration 直接相关的关键资产。
- 识别跨仓库稳定成立的能力内核，而不是按仓库名称逐个复刻。
- 输出当前仓库的候选资产清单，明确首批优先方向、延后项和平台适配边界。

## 输入范围

- `references/repos/everything-claude-code`
- `references/repos/oh-my-opencode`
- `references/repos/superpowers`
- 当前仓库已有 `src/skills/`、`src/agents/` 与 `README.md`

## 本阶段交付

- `brief.md`
- `assets/subagent-multi-agent-landscape.md`
- `outputs/2-plan.md`
- `outputs/3-tasks.md`

## 成功标志

- 三个参考仓库都被逐一研究，并且各自的重点资产、可复用模式、平台绑定前提都被明确记录。
- 研究结论不只是“有哪些文件”，还要能回答“哪些适合沉淀为 `skill / command / agent / eval`，哪些不适合”。
- 给出至少一版面向当前仓库的首批候选方向，并说明为何这样取舍。
- 明确哪些能力应进入核心资产层，哪些只能进入 `targets/` 或继续保留在参考层。

## 非目标

- 不在本阶段落地 tmux、session API、background polling、hook runtime 等运行时实现。
- 不在本阶段直接复制参考仓库中的平台 bootstrap、安装脚本或插件代码。
- 不在本阶段同时新增大量同类 skill；若有与现有资产重叠，优先记录为后续设计决策。

## 设计约束

- 核心资产默认工具无关。
- 平台特定术语、工具映射、配置键和 hook 机制应下沉到 `targets/`。
- 研究结果必须能直接服务下一步 `eval-first` 落地，而不是停留在概念层。
