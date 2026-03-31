# 开发工作流双线设计调研

检查时间：2026-03-25

## 背景

当前想梳理的不是单个 skill，而是一套更稳定的开发工作流骨架，重点在两个问题：

1. 本地实现阶段，是否要把方案、TDD、验证、review、alignment、学习沉淀固定成一条强闭环。
2. 当多任务并行、PR 往返和 CI 等待变多时，是否应该单独再拉出一条“PR 生命周期线”，甚至固定拆成多个 session。

这份调研结合了：

- 当前仓库已有 package 边界与研究记录
- `superpowers`、`everything-claude-code` 的参考工作流
- GitHub 官方关于 PR / review / auto-merge / merge queue / protected branches 的文档
- Trunk-Based Development 与 Google code review 实践

## 结论先行

不建议长期维护两条彼此独立的主线。

更稳的做法是：

1. 固定一条本地质量主骨架。
2. 把 PR / review / CI / merge 设计成这条主骨架进入远端后的状态机，而不是另一条平行流水线。
3. 在并行任务很多时，增强的是“分支更短、PR 更小、Draft PR 更早、merge 更自动”，而不是强制把流程拆成更多固定 session。

换句话说，推荐的不是：

- 线 1：方案 -> 实现 -> review -> 发布 / CI
- 线 2：方案 -> 实现 -> PR -> review session -> merge session

而是：

- 一条主线：方案 -> 实现闭环 -> pre-PR gate -> PR 生命周期 -> merge / cleanup
- 并行很多时，只把 `PR 生命周期` 从同步动作改成异步推进

## 当前仓库已经隐含的边界

仓库现有资产已经把“本地质量闭环”和“远端 PR 生命周期”分开了：

- `packages/nanospec/`、`packages/spec-driven/`
  - 负责任务容器、spec、plan、alignment
- `packages/quality-workflows/`
  - 负责 `quality-tdd`、`quality-verify`、`quality-review`、`quality-review-feedback`
- `packages/github-workflows/`
  - 负责远端 PR 生命周期动作，不替代质量判断本身

`packages/github-workflows/skills/pr-lifecycle/SKILL.md` 还明确写了：

- 它是远端动作入口
- 不默认自动跑完整闭环
- 不应把“提 PR”自动扩展成“提 PR -> review -> merge”

这说明仓库当前方向本身就更接近“单主线 + 远端状态机”，而不是“两条完全独立工作流”。

## 外部资料给出的稳定信号

### 1. GitHub 原生就把 PR 设计成异步协作容器

GitHub 官方文档对 PR 的定义很清楚：PR 是提议、讨论、review、checks 和 merge 的统一入口，而不是一个只在最后一步才出现的壳。  
来源：

- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews

几个直接影响流程设计的点：

- Draft PR 不能 merge，而且不会自动请求 code owners review。
- Ready for review 后，才进入正式 review 节奏。
- Review 有 `Comment`、`Approve`、`Request changes` 三种状态。
- 评审线程可以 resolve，也可以 re-request review。

这意味着：

- “开 PR”不等于“现在就必须正式 review”
- Draft PR 本身就是把异步协作提前、但不提前触发正式 gate 的机制

### 2. GitHub 已经内建了减少等待的机制

GitHub 官方明确支持：

- protected branches / required reviews / required status checks
- auto-merge
- merge queue
- CODEOWNERS

来源：

- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- https://docs.github.com/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/automatically-merging-a-pull-request
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request-with-a-merge-queue
- https://docs.github.com/github/creating-cloning-and-archiving-repositories/about-code-owners

这些机制的共同点是：尽量把“人盯着等”的同步时间拿掉。

因此在并行任务很多时，更合理的方向通常不是“再开一个 merge session”，而是：

- 达到条件后直接开 auto-merge
- 主分支很忙时用 merge queue
- 用 CODEOWNERS / reviewer request 固定路由

### 3. 好的并行开发依赖小变更、短命分支，而不是更多阶段

Google 的 code review 实践强调：

- 小 CL 更容易被快速 review，也更容易被彻底 review
- review 的响应速度本身很重要
- 大改动应该优先拆小

来源：

- https://google.github.io/eng-practices/review/developer/small-cls.html
- https://google.github.io/eng-practices/review/reviewer/speed.html

Trunk-Based Development 也强调：

- short-lived feature branches
- 分支最好只活几天，最好更短
- 分支开发人数尽量保持在 1 人

来源：

- https://trunkbaseddevelopment.com/short-lived-feature-branches/
- https://trunkbaseddevelopment.com/continuous-integration/

这几条和你的问题直接相关：

- 并行很多时，复杂度的主要来源通常不是“少了一个 review session”
- 真正的复杂度来源通常是“分支太大、活太久、review 太慢、merge 太晚”

## 对你提出的两条线的评估

### 线 1：前期方案 -> 实现闭环 -> review -> 发布 / CI

这是更适合作为默认主线的版本。

优点：

- 本地质量闭环完整，容易形成稳定纪律
- 适合把 `spec-driven`、TDD、verify、alignment、learning capture 串起来
- 适合重要任务、复杂任务、架构变更

问题：

- 如果把 `review` 固定理解成“PR 前必须独立再来一轮正式 review”，可能会拖慢小改动
- 如果把“发布 / CI”理解成最后才接触远端，容易让 PR 反馈来得太晚

因此这条线适合保留，但应稍微改写成：

- 前期方案 -> 实现闭环 -> pre-PR gate -> PR 生命周期

而不是停在“review -> 发布 / CI”。

### 线 2：前期方案 -> 实现闭环 -> PR -> review session -> merge session

它的问题不在于“多了 PR”，而在于把 session 固定按平台动作拆开了。

如果强制规定：

1. 开一个 session 负责提 PR
2. 再开一个 session 负责 review
3. 再开一个 session 负责 merge

那通常会过度复杂，原因是：

- session 切分依据是工具动作，不是状态变化
- 很多 PR 根本不需要独立 merge session
- review 和 comment handling 往往是多轮往返，不天然只属于一个 session
- 如果启用了 auto-merge / merge queue，merge session 的价值会进一步下降

但如果你把它理解成：

- 本地实现 session
- 远端状态同步 / comment handling session
- 只有遇到 blocker 时才开专门 merge / conflict session

那它就不复杂，反而更适合高并行环境。

所以第二条线不该被固化成“三段 session 仪式”，而应该被改造成“异步 PR 生命周期”。

## 推荐工作流

### A. 默认主线

适用于大多数普通开发任务。

1. 前期方案
   - 需求澄清
   - 必要时建 `nanospec` 容器
   - 产出 spec / plan
2. 实现闭环
   - 先搜索现有模式
   - TDD
   - 实现
   - alignment 记录偏差 / 变更 / 缺失
   - 学习信号按需沉淀
3. 本地质量 gate
   - 必要时独立 `quality-review`
   - 必做 `quality-verify`
4. 进入 PR 生命周期
   - 还没准备好正式 review：开 Draft PR
   - 已可评审：开 Ready PR 并 request review
5. 远端反馈闭环
   - 看 comments / reviews / checks
   - 处理反馈
   - 重新 verify
   - 更新 PR
6. 合并
   - 满足条件后 merge / auto-merge / merge queue
7. 收尾
   - cleanup branch / worktree
   - 必要时 summary / learning evolution

可以压缩成一句话：

`方案 -> 实现闭环 -> pre-PR gate -> PR 异步推进 -> 合并收尾`

### B. 并行很多时的增强版

适用于：

- 同时有多个任务并行
- reviewer 响应是异步的
- CI 时间较长
- 主分支更新频繁

增强点应该是：

1. 更小的任务切片
   - 优先把大任务拆成多个可独立 review 的小 PR
2. 更短命的分支
   - 分支寿命尽量控制在 1 到 2 天内
3. 更早的 Draft PR
   - 让上下文、diff、初步 checks 尽早可见
4. 更自动的 merge
   - 满足条件后 auto-merge
   - 主分支繁忙时 merge queue
5. 更明确的状态推进
   - `local-wip`
   - `draft-pr`
   - `ready-for-review`
   - `changes-requested`
   - `approved-waiting-checks`
   - `queued-or-auto-merge`
   - `merged`

重点是：并行场景下增加的是“状态治理”和“等待自动化”，不是固定增加 session 数。

## review 到底放哪

这里最容易混淆，需要拆成两类。

### 1. 本地 review gate

这是 `quality-review` 的位置，目的不是走 GitHub 流程，而是先做一次独立质量判断。

建议在以下场景固定触发：

- 架构变更
- 跨多个模块的耦合改动
- 高风险 bugfix
- 大 diff
- 行为变化明显但测试表达仍不充分
- 合并前的最后一次总审

这类 review 放在 PR 前通常是值得的。

### 2. PR review

这是 GitHub review，目的更偏向：

- 协作确认
- owner 审批
- 远端评论线程
- 分支保护要求

它本来就应该围绕 PR 展开，不必再额外抽象成“PR 之前的另一套 review 流程”。

所以更合理的原则是：

- 重要改动：本地 review gate + PR review
- 小改动：可只做自审 + verify + PR review

不要把所有改动都升级成“双 review 串行”。

## session 该怎么切

如果你喜欢用 session 管理上下文，建议按“状态转换”切，而不是按“平台动作”切。

更合理的切法：

### Session 1：方案与实现

结束条件：

- spec / plan 清楚
- 实现完成
- 已完成本地 verify
- 已决定是否要做本地独立 review

### Session 2：PR 生命周期推进

处理：

- 建 Draft / Ready PR
- request review
- 看 checks
- 拉 comments
- 修反馈
- re-verify

这个 session 可能会被多次 reopen，但它本质上是同一个“远端推进”面。

### Session 3：只在有 blocker 时单开

例如：

- merge conflict
- CI 疑难故障
- 分支需要重切 / 重拆
- merge policy 需要人工判断

默认不要为“merge 本身”固定保留一个 session。

## 与当前仓库资产的映射建议

- 前期方案 / 对齐：
  - `packages/nanospec/`
  - `packages/spec-driven/`
- 实现前研究：
  - `packages/search-first/`
- 实现质量闭环：
  - `packages/quality-workflows/skills/quality-tdd/`
  - `packages/quality-workflows/skills/quality-verify/`
  - `packages/quality-workflows/skills/quality-review/`
- 反馈与学习沉淀：
  - `packages/learning-evolution/`
- 远端 PR 生命周期：
  - `packages/github-workflows/skills/pr-lifecycle/`

如果后续要把这套方法继续产品化，最值得补的不是再发明第三条线，而是把以下状态动作做实：

1. `draft-pr`
2. `ready-for-review`
3. `handle-feedback`
4. `check-status`
5. `auto-merge-or-queue`
6. `cleanup`

## 最终建议

建议把你的想法收敛为下面这版：

### 默认版

`前期方案 -> 实现闭环（TDD / verify / alignment / learning）-> 必要时本地独立 review -> PR（Draft 或 Ready）-> review / comments / checks -> merge / auto-merge -> cleanup`

### 并行增强版

`前期方案 -> 更小任务切片 -> 更早 Draft PR -> Ready 后 request review -> comments / checks 异步推进 -> auto-merge 或 merge queue -> cleanup`

### 一个核心原则

不要把“并行很多”理解成“流程阶段更多”。

更准确的理解应该是：

- 本地质量闭环保持强约束
- 远端 PR 生命周期保持异步状态推进
- 通过小 PR、短命分支、Draft PR、auto-merge、merge queue 降低等待和切换成本

按这个原则看，第二条线原始写法偏复杂；但把它改成“远端异步状态机”后，就是合理的。

## 参考资料

### 仓库内

- `README.md`
- `packages/quality-workflows/README.md`
- `packages/github-workflows/README.md`
- `packages/github-workflows/skills/pr-lifecycle/SKILL.md`
- `.research/pr-review-merge-gap-analysis.md`
- `.research/reference-pr-review-skills-note.md`
- `references/translations/superpowers/skills/requesting-code-review/SKILL.md`
- `references/translations/superpowers/skills/verification-before-completion/SKILL.md`
- `references/translations/superpowers/skills/test-driven-development/SKILL.md`
- `references/translations/superpowers/skills/subagent-driven-development/SKILL.md`

### 外部

- GitHub Docs, About pull requests  
  https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
- GitHub Docs, Creating a pull request  
  https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request
- GitHub Docs, About pull request reviews  
  https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews
- GitHub Docs, About protected branches  
  https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- GitHub Docs, Automatically merging a pull request  
  https://docs.github.com/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/automatically-merging-a-pull-request
- GitHub Docs, Merging a pull request with a merge queue  
  https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request-with-a-merge-queue
- GitHub Docs, About code owners  
  https://docs.github.com/github/creating-cloning-and-archiving-repositories/about-code-owners
- Google Engineering Practices, Small CLs  
  https://google.github.io/eng-practices/review/developer/small-cls.html
- Google Engineering Practices, Speed of Code Reviews  
  https://google.github.io/eng-practices/review/reviewer/speed.html
- Trunk Based Development, Short-Lived Feature Branches  
  https://trunkbaseddevelopment.com/short-lived-feature-branches/
- Trunk Based Development, Continuous Integration  
  https://trunkbaseddevelopment.com/continuous-integration/
