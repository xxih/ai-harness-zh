---
name: learning-capture
description: 在一个会话或一个任务里手动触发学习积累；把本次问题、决策、证据、可复用模式和项目级规则候选落盘为结构化记录，默认写入项目根目录的 `.learned/`。
---

# Learning Capture

把“这次值得记住什么”做成显式手动动作。当前阶段只做手工触发，不依赖 hooks、observer 或自动入库。目标是在单个会话或任务内先沉淀学习记录、候选模式和项目级规则候选，为后续 `save / absorb / drop`、stocktake 或 `AGENTS.md` 更新做准备。默认落盘位置放在项目根目录 `.learned/`，而不是 `output/` 或 `nanospec` 默认目录。

## 何时使用

- 你刚完成一个非平凡任务，想把这次 learnings 记下来
- 你明确说了“复盘一下”“沉淀一下这次经验”“手动触发学习积累”
- 同一任务里出现了用户纠正、关键取舍、验证教训或可复用 workaround
- 你还不确定是否值得升级为正式 skill，但不想让经验只留在对话里
- 用户在对话里纠正了几个项目级 / 公共规则点，但你不想立刻手改 `AGENTS.md`

不适用：

- 只是一次性 typo、机械改名或纯偶发问题
- 还没有形成任何可复用结论或证据
- 目标是直接产出正式 skill / command / eval，而不是先做记录

## 产物

每次使用本 skill，默认产出以下最小集合：

1. 学习记录
   - 若当前任务已有自己的记录文件，优先回写到该文件
   - 若没有既定记录位置，默认写入 `.learned/learnings.md`
2. 候选升级清单
   - 若当前任务已有自己的记录文件，优先回写到该文件
   - 若没有既定记录位置，默认写入 `.learned/promote-candidates.md`
3. 项目级规则候选
   - 若当前任务已有自己的记录文件，优先回写到该文件
   - 若没有既定记录位置，默认写入 `.learned/project-rules.md`
4. 后续动作状态
   - `keep-local`：先保留在当前任务或项目内
   - `promote-later`：后续进入 `save / absorb / drop` 评审
   - `propose-agents-update`：建议后续更新 `AGENTS.md`、README 或其他仓库级规则文件
   - `drop`：确认不值得继续沉淀

默认要求：

- 一条 learning 或 rule candidate 只描述一个明确模式，不要把多个问题揉成一条
- 每条都要写证据来源，而不是只写抽象结论
- 当前阶段只做记录和分类，不自动升级为正式仓库资产

## 工作流

1. 确认本次学习边界
   - 本次目标是“任务内 / 会话内积累”，不是立即发布正式资产
   - 只抓非平凡、可复用、带证据的模式
2. 收集证据
   - 优先看本次 diff、命令输出、验证结果、用户纠正、失败与修复过程
   - 如果没有证据，只能记录为疑似观察，不能写成确定模式
3. 提炼学习条目
   - 每条至少写清：场景、触发信号、采取动作、证据、适用范围、非适用范围
   - 能落到具体命令、文件、检查动作时，就不要只写口号
4. 分层落盘
   - 当前任务立即可复用的，写入 `learnings.md`
   - 可能升级为共享资产的，写入 `promote-candidates.md`
   - 明显是项目级 / 仓库级口径修正的，写入 `project-rules.md`
5. 标记后续状态
   - 明显只对当前任务有价值：`keep-local`
   - 跨任务复用概率高，但还需要改写：`promote-later`
   - 明显是仓库级规则修正，且后续应更新 `AGENTS.md` 或同类文件：`propose-agents-update`
   - 噪音、一次性修补或重复内容：`drop`
6. 如任务口径因此变化，执行对齐
   - 若 learning 影响当前任务范围、方案或后续动作，更新 `alignment.md`
   - 若存在 `nanospec` 任务容器，同时把后续动作写回 `outputs/3-tasks.md`

## 公共规则捕获

- 如果用户在对话里纠正的是“这个仓库以后都该这样做”的规则，不要只把它记成普通 learning。
- 这类内容应单独写入 `project-rules.md`，至少包含：
  - 原始纠正或归纳后的规则
  - 作用范围：仓库级 / 项目级 / target 级
  - 证据来源：哪段对话、哪个任务、哪次纠正
  - 建议落点：`AGENTS.md`、`README.md`、某个 skill、某个 eval
  - 当前状态：`propose-agents-update` | `keep-local` | `drop`
- 当前阶段默认只“提取并排队”，不自动改写 `AGENTS.md`；是否正式写回由后续任务决定。
- 如果用户明确要求“顺手把 AGENTS.md 也改了”，那是下一步 execute，不属于本 skill 的默认动作。

## 记录约束

- 这个 skill 是手工触发入口，不依赖 hooks 或后台观察器
- 当前阶段不自动生成正式 `src/skills/`、`src/commands/`、`evals/` 资产
- 任务内 learning 和仓库级资产要分层，不要把原始记录直接当成最终 prompt
- 默认根目录使用 `.learned/`，不要把 `nanospec` 当成学习记录的默认载体
- 若一条经验只适用于当前项目、当前目录或当前任务，应优先 `keep-local`
- 若一条纠正已经明显是仓库公共规则，应优先进入 `project-rules.md`，不要混进普通 `learnings.md`
- 若已有相同记录，优先合并，不要制造新的碎片文件

## 模板

需要学习记录模板和候选升级模板时，读取 [references/templates.md](references/templates.md)。
