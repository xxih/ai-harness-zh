# Alignment Log

## 2026-03-15

- [歧义] 用户提到“调研三个 repo”，但本轮未显式点名；按当前仓库既有研究上下文，默认解释为 `references/repos/everything-claude-code`、`references/repos/superpowers`、`references/repos/oh-my-opencode`。
- [变更] 本任务不以“全自动学习”为目标，而以“AI 生成候选、人类筛选与改写”为优先方向。
- [变更] 研究重点从“谁更自动”调整为“谁已经具备对应能力，以及哪些能力可脱离 hooks 先行吸收”。
- [变更] 本轮新增研究产物 `assets/auto-learning-landscape.md`，用于承载三仓库证据、hooks 依赖判断与折中方案设计。
- [变更] 用户确认第一阶段只做“纯手工触发”的学习积累，不做半自动候选生成或自动积累实现。
- [变更] 当前优先级从“继续展开方案比较”切换为“先定义规范、目录结构、产出物结构，并落一个最小可用 skill”。
- [变更] 第一阶段交付物调整为新增 `learning-capture` skill，提供会话内 / 任务内手动触发的学习记录与候选升级结构。
- [变更] 用户补充要求：除任务 learnings 外，还需要捕获对话中出现的项目级 / 公共规则纠正，先提取为候选，避免用户手动维护 `AGENTS.md`。
- [变更] `learning-capture` 需要增加 `project-rules.md` 这一层结构，用于排队后续 `AGENTS.md`、README 或共享资产规则更新。
- [变更] 用户否定 `output/xxx` 风格目录，并进一步要求不要统一成单个 `records/`；改为项目根目录下的隐藏目录：`.learning`、`.quality`，以及与研究配套的 `.research`。
- [变更] 路径策略更新为：learning 默认 `.learning/`；quality 有容器优先写容器，无容器回退到 `.quality/`；research 默认 `.research/`。
