# 方案：自动学习调研与折中方案

## 总体判断

这条线值得做，但不应该直接按 ECC 的完整实现逆向复刻。

对当前仓库更合理的策略是分层处理：

1. 先把“学习候选的评估与入库”设计清楚。
2. 再把“任务内 learnings 的记录与传播”变成稳定动作。
3. 最后才考虑是否在 `targets/` 层补提醒型 hooks。

换句话说，当前更该解决的是“什么值得沉淀、如何减少碎片化、如何让人类改写 prompt 更省力”，而不是先解决“如何自动采集更多 observation”。

基于用户最新确认，本轮第一阶段只落“纯手工触发”能力，先把规范、目录结构和产出物结构定下来。

## 三仓库吸收策略

### everything-claude-code

吸收方式：`adapt`

吸收重点：

- `/learn`、`/learn-eval` 背后的保存前判断逻辑
- `skill-stocktake` 的治理视角
- 项目作用域 / 全局作用域的区分思路

明确裁剪：

- 不直接吸收 hooks 观察链路
- 不直接吸收 instinct 存储结构、observer agent、命令体系

### superpowers

吸收方式：`adopt + adapt`

吸收重点：

- 人工确认优先
- 经验要被改写成高执行力 prompt，而不是原样存档
- 先判断“是否值得沉淀”，再决定是否入库

明确裁剪：

- 不引入平台 bootstrap
- 不把 session-start hook 当成当前仓库前置条件

### oh-my-opencode

吸收方式：`adapt`

吸收重点：

- 任务内 `learnings / issues / problems` 的记录方式
- 让 learnings 先服务当前任务的后续步骤
- 自动提醒和长期资产化分离

明确裁剪：

- 不引入 46 hooks 的编排系统
- 不引入 orchestrator runtime、background task、状态管理体系

## 建议方案

### 方案 A：学习候选卡

形态：

- 每次重要任务结束后，由 AI 生成一张学习候选卡
- 人工决定 `save / absorb / drop`

适合当前仓库作为最低成本起步方案。

### 方案 B：半自动候选池

形态：

- 定期扫描 `nanospec/` 任务产物、review 结论、失败记录
- 自动聚合候选经验
- 人工审核后再升级成正式资产

这是当前最平衡的主方案。

### 方案 C：任务内 learnings 传播

形态：

- 在任务容器内维护 `learnings.md`、`issues.md`、`promote-candidates.md`
- 在同一任务的后续步骤中优先消费这些文件

这适合作为方案 A / B 的增强层。

### 方案 D：target 层提醒型 hooks

形态：

- 仅在支持的平台适配层增加提醒
- hooks 只负责提示生成候选、触发评审
- hooks 不直接写正式资产

这是第二阶段之后再考虑的增强方案。

## 推荐实施顺序

第一阶段：

- 新增 `learning-capture` skill
- 定义 `learnings.md`、`promote-candidates.md` 与 `project-rules.md` 的结构
- 定义项目根目录隐藏记录目录：`.learning`、`.quality`、`.research`
- 定义 learning 与 quality 的不同回写策略：
  - learning 默认写 `.learning/`
  - quality 有容器优先写容器，无容器回退到 `.quality/`
  - research / orchestration 默认写 `.research/`
- 先支持手工触发，不做 hooks 或扫描自动化

第二阶段：

- 形成 `save / absorb / drop` 评审准则
- 形成周期性 stocktake 节奏
- 把任务内 learnings 记录并入 `nanospec` 任务容器
- 明确哪些 learnings 可升级为 skill / command / eval

第三阶段：

- 若某个 target 平台确实受益明显，再为该 target 增加提醒型 hooks

## 风险与收口

### 风险 1：把“自动学习”误做成“自动发布资产”

收口：

- 正式资产入库必须保留人工确认
- AI 默认只能生成候选和归档建议

### 风险 2：沉淀大量低质量碎片

收口：

- 引入 `save / absorb / drop`
- stocktake 时优先合并，而不是不断新增

### 风险 3：过早引入重运行时

收口：

- hooks 仅进入 `targets/`
- 核心仓库先保持工具无关、文件驱动
