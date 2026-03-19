# learning-evolution 闭环优化

## 背景

当前 `learning-capture` 已收敛为两类落点：

- `rules.md`：项目级 / 团队级 / 分发级长期规则候选
- `notes.md`：其他可复用经验或局部做法

最近几次真实使用里，`rules.md` 往往能沉淀出清晰、稳定、可落点的东西；但 `notes.md` 的边界比较模糊，容易变成“记了一些东西，但不知道下一步要干嘛”的集合。

与此同时，现有 learning 对 skill 的支撑也偏弱。很多重复出现的工作流并不适合直接自动改成 skill，但应该能先留下更接近 skill 的证据、碎片和候选，让后续创建 / 改写 skill 更容易。

## 本次想解决的问题

1. 这个包是否应改名为 `learning-evolution`，以准确表达“闭环演化”而不是“只做捕获”。
2. 规则之外的长期沉淀是否应从 `notes.md` 改成更明确的 `support.md`。
3. 如何借鉴 Claudeception、ECC、Homunculus 与行业方法论，但不把仓库绑死在某个 runtime。
4. 如何把“信号 -> 判断 -> 分流 -> codify”做成闭环：不只记录，还覆盖正式沉淀。

## 约束

1. 仍坚持“默认不自动发布正式资产”，正式 skill / command / 文档更新保持人工决策。
2. 核心能力保持工具无关、文件驱动；若吸收 hooks，只能作为 target 层可选提醒，不作为主流程前提。
3. 新结构必须比当前 `notes.md` 更可理解，且能解释“什么时候记、记什么、记完之后去哪”。
4. 要兼容当前仓库 package-first 组织与 `.learned/` 的默认落点。
