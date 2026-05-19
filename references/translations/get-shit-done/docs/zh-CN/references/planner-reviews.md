# Reviews Mode - Planner Reference

当 orchestrator 将 Mode 设为 `reviews` 时触发。以 `REVIEWS.md` 的反馈作为附加上下文，从头重新规划。

**思维方式：** 这是一个吸收了评审洞见的全新 planner，不是只做修补的外科医生，而是已经读过同伴批评意见的架构师。

### 第 1 步：加载 `REVIEWS.md`
从 `<files_to_read>` 读取 reviews 文件。解析：
- 每位 reviewer 的反馈（优点、担忧、建议）
- Consensus Summary（已达成共识的担忧，优先级最高）
- Divergent Views（需要调查，并自行做判断）

### 第 2 步：对反馈分类
将 review 反馈分为：
- **Must address**：HIGH 严重级别且有共识的问题
- **Should address**：2 位及以上 reviewer 提到的 MEDIUM 问题
- **Consider**：单个 reviewer 的建议，或 LOW 严重级别问题

### 第 3 步：带着 review 上下文重新规划
按标准规划流程创建新计划，但把 review 反馈作为额外约束：
- 每个 HIGH 严重级别且已达成共识的问题，都**必须**有一个 task 来处理
- MEDIUM 问题应在不过度设计的前提下尽量处理
- 为了便于追踪，在 task 的 action 中注明：`Addresses review concern: {concern}`

### 第 4 步：返回结果
使用标准的 `PLANNING COMPLETE` 返回格式，并额外加入 reviews 区段：

```markdown
### Review Feedback Addressed

| Concern | Severity | How Addressed |
|---------|----------|---------------|
| {concern} | HIGH | Plan {N}, Task {M}: {how} |

### Review Feedback Deferred
| Concern | Reason |
|---------|--------|
| {concern} | {why — out of scope, disagree, etc.} |
```
