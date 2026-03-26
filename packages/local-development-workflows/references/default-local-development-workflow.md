# 本地开发默认工作流

这份文档定义当前仓库推荐采用的本地开发默认主线。目标不是覆盖所有特例，而是给日常开发提供一条稳定、低歧义、可复用的默认路径。

## 适用范围

适用于：

- 新功能开发
- bugfix
- 有行为变化的重构
- 需要保留方案、实现、验证和收尾纪律的日常 coding 工作

不适用：

- 一次性纯研究任务
- 极小的纯文案修改
- 只处理远端 PR / comments / merge 的任务

## 默认主线

默认按下面这条主线推进：

`方案 / plan -> search-first -> TDD -> 实现 -> alignment -> 必要时 local review -> verify -> finish`

如果任务进入远端协作，再由 `github-workflows` 接上 PR 生命周期；本地默认主线本身只覆盖“做到可收尾、可发 PR、可本地合回”的阶段。

## 阶段说明

### 1. 方案 / plan

目标：

- 先明确要解决什么
- 明确范围、非目标和验收口径

默认动作：

- 任务复杂时，使用 `nanospec` / `spec-driven` 建立任务容器
- 形成最小可执行 plan，再进入实现

进入下一阶段的条件：

- 当前要实现的行为已经足够明确
- 不再处于“边做边猜需求”的状态

### 2. Search First

目标：

- 先确认仓库里有没有现成模式、相似实现和既有测试

默认动作：

- 先搜本地代码、测试和已有抽象
- 必要时再看 `references/` 或官方资料
- 明确本轮是 `adopt`、`adapt` 还是 `build`

进入下一阶段的条件：

- 已确认本轮实现路径
- 没有明显“其实仓库里早就有现成方案”的风险

### 3. TDD

目标：

- 对行为变化保持测试先行

默认动作：

- 先写失败测试
- 亲眼看到失败
- 再写最小实现让它通过
- 绿灯后再重构

进入下一阶段的条件：

- 当前行为已经被测试锁住
- 至少完成一轮真实的红-绿循环

### 4. 实现

目标：

- 在已有 plan 和测试约束下完成最小实现

默认动作：

- 只实现当前 plan 覆盖的内容
- 不顺手扩 scope
- 发现设计偏差或阻塞时，先记录并校正，再继续

进入下一阶段的条件：

- 当前实现已经达到本轮目标
- 没有明显未处理的核心阻塞

### 5. Alignment

目标：

- 把需求变化、实现偏差和临时决策从对话里收回到正式记录

默认动作：

- 范围变化、方案变化、实现偏差、缺失、歧义出现时，更新 `alignment.md`
- 同步受影响的 spec / plan / tasks

进入下一阶段的条件：

- 当前工作口径重新一致
- 后续执行不再依赖“记忆里刚才说过什么”

### 6. Local Review

目标：

- 在进入最终验证和收尾前，做一次本地独立质量判断

默认动作：

- 不是每次都强制做
- 当改动达到触发条件时，执行 `quality-review`
- reviewer 可以反驳，但必须基于技术事实

具体触发条件见：

- [local-review-trigger-rules.md](local-review-trigger-rules.md)

进入下一阶段的条件：

- 若本轮触发了 local review，则 Critical / Important 已处理完
- 若未触发，则至少完成一次认真自审

### 7. Verify

目标：

- 在收尾、提交、发 PR、宣称完成前拿到 fresh evidence

默认动作：

- 运行能支撑当前结论的完整验证命令
- 至少覆盖 build / tests / diff 检查
- 项目有 types、lint、静态分析时，也一并纳入

进入下一阶段的条件：

- 拿到 fresh verification evidence
- 当前结论是 `ready`，不是“应该没问题”

### 8. Finish

目标：

- 收束当前本地开发分支与 worktree，明确出口

默认动作：

- 使用 `finishing-a-development-branch`
- 先验证，再选出口
- 出口固定收敛到：本地 merge / 推送并发起 PR / 保留现状 / 丢弃当前工作

完成条件：

- 当前分支的出口已经明确
- worktree 是否保留也已经明确

## 默认纪律

- 没有足够清晰的 plan，不进入实现
- 没有 search-first 结论，不轻易新写抽象
- 没有失败测试，不写行为变化相关生产代码
- 发生口径变化时，不只改对话，要回写对齐记录
- 没有 fresh verification evidence，不做完成宣称
- local review 是条件触发，不是所有任务一刀切强制执行
- 进入 finish 前，至少要完成一次真实 verify

## 最小搭配关系

- 方案 / 对齐：`packages/nanospec/`、`packages/spec-driven/`
- 实现前研究：`packages/search-first/`
- 测试先行、评审、验证：`packages/quality-workflows/`
- 分支与 worktree 收尾：`packages/git-workflows/`

## 与远端流程的边界

这份文档只定义本地主线，不定义以下内容：

- Draft / Ready PR 的切换
- review comments 拉取与线程回复
- checks 轮询
- merge / auto-merge / merge queue

这些动作进入远端后，交由 `packages/github-workflows/` 处理。
