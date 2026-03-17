# 方案：优化自动学习 skill

## 总体判断

`learning-capture` 的问题不在“分三层”本身，而在：

1. 三层默认都要产出，容易逼出无效记录。
2. `promote-candidates.md` 太像想法箱，不像资产孵化面。
3. 没有把“流程型经验”单独抬高优先级。

所以优化重点不该是再加更多记录字段，而是把“分类之后怎么推进”说清楚。

## 优化方向

### 方向 A：把“三类文件”改成主次分明，而不是平均用力

建议改法：

- `learnings.md`：保留为任务操作经验
- `promote-candidates.md`：升级为共享资产孵化主入口
- `project-rules.md`：继续作为规则候选池

新增要求：

- 每次触发先判断“主价值层”
- 主价值层必须写实
- 非主价值层若无足够证据，可明确记为“本次无新增”，而不是勉强生成弱条目

### 方向 B：重写 `promote-candidates.md` 模板

建议新增字段：

- 建议资产类型：`skill` | `command` | `eval` | `doc-update` | `absorb-existing`
- 触发场景
- 输入材料
- 预期输出
- 步骤骨架
- 与现有资产的关系
- 需要补的验证
- 当前阻塞

这样它才会承接“把这整个流程整理成 skill”这类需求。

### 方向 C：给 `learning-capture` 增加一个轻量判断门

在工作流里加入一个先行判断：

1. 这是单点经验、规则纠正，还是完整流程雏形。
2. 如果是完整流程雏形，优先写 `promote-candidates.md`，并把 `learnings.md` 限制为支持该候选的证据点。
3. 如果只是局部操作技巧，不要硬升 skill 候选。

### 方向 D：为真实案例补一个对照示例

当前样例更像“字体排障 + 目录落位”，天然会让 `project-rules.md` 看起来最强。建议后续补一个更适合 workflow 提炼的示例，比如：

- 把长文改写成小红书图文并完成导出

然后对照展示：

- 哪些内容应进入 `learnings.md`
- 哪些内容应进入 `promote-candidates.md`
- 哪些内容才应进入 `project-rules.md`

## 推荐实施顺序

1. 先改 `SKILL.md` 的定位描述与工作流判断门。
2. 再改 `references/templates.md`，重点强化 `promote-candidates.md`。
3. 补一个“流程型候选”示例到当前任务或 eval 样例中。
4. 最后跑 `python3 scripts/validate_assets.py` 做结构校验。

## 暂不建议的做法

- 不建议现在就把 `learning-capture` 做成自动 hooks 入口。
- 不建议继续要求每次都产出三份同等重量的内容。
- 不建议让 `learnings.md` 承担 workflow 设计职责。
