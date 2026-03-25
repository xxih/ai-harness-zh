# PR / review / merge / conflict 自动化闭环 gap 分析

检查时间：2026-03-24

## 目标

- 评估当前仓库距离“让 AI 端到端处理提 PR、收 review、处理评论、合并、解冲突”还有哪些缺口
- 明确哪些能力已经有 prompt 级雏形，哪些还缺 runtime / GitHub / CI 执行面

## 期望闭环

目标闭环可拆成 8 个阶段：

1. 创建隔离分支 / worktree
2. 完成实现并做 pre-PR verify
3. 推送分支并创建 PR
4. 请求 review 或触发自动 review
5. 拉取 review comments / review state
6. 逐条处理评论并回帖
7. 处理 CI 失败、merge conflict、需要 rebase 的情况
8. 合并 PR，并清理 branch / worktree

## 当前仓库已具备的能力

### 已有：prompt / workflow 层

- `packages/git-workflows/skills/using-git-worktrees/`
  - 解决阶段 1 的大部分：建立隔离 worktree、ignore 校验、baseline
- `packages/git-workflows/skills/finishing-a-development-branch/`
  - 解决阶段 2、3、8 的一部分：决定 merge / push / keep / discard，描述 PR / MR 收尾
- `packages/quality-workflows/skills/quality-verify/`
  - 解决阶段 2 的验证门禁
- `packages/quality-workflows/skills/quality-review/`
  - 解决“需要独立 reviewer”这件事
- `packages/quality-workflows/skills/quality-review-feedback/`
  - 解决阶段 6 的“收到评论后怎么判断、采纳、反驳”
- `packages/agent-orchestration/`
  - 解决复杂任务中 review / verify / execute 的阶段编排

### 已有：认知层方法论

- 已经调研并吸收 `superpowers` 的：
  - `requesting-code-review`
  - `receiving-code-review`
  - `finishing-a-development-branch`
- 已经识别 ECC 中值得吸收的：
  - `git-workflow`
  - `quality-gate`
  - `PR logger`
  - `autonomous-loops`

## 关键判断

当前仓库**已经有“AI 应该怎么做”的 workflow prompt**，但还没有把“AI 真的能执行到 GitHub / CI / merge 层”的运行时能力补齐。

换句话说：

- 你现在更像“会做这件事的操作手册”
- 还不是“真的能把整条 PR 生命周期跑完的 harness”

## 主要缺口

### Gap 1：缺少明确的 `request-review` 正式资产

现状：

- 你有 `quality-review`
- 但没有一个专门面向“发起 review 请求”的独立 skill / command
- 还没有把 `superpowers/requesting-code-review` 吸纳进仓库

缺什么：

- 何时发 review
- review 的上下文模板
- base/head SHA 的取法
- review findings 的严重级别处理规则
- review 后是否阻塞继续开发

影响：

- 现在能“做 review”，但没有稳定的“发起 review workflow”

### Gap 2：缺少真正的 PR 创建执行面

现状：

- `finishing-a-development-branch` 只写到“若环境已有 CLI 或脚本，则用项目既有方式创建 PR / MR”
- 仓库里没有自有的 `gh pr create` skill / command / wrapper

缺什么：

- PR title / body 生成模板
- `git diff base...HEAD` 摘要生成
- `gh pr create` 的稳定执行封装
- draft / ready / reviewer / label / assignee 的参数策略
- 创建后记录 PR URL、编号、下一步动作

影响：

- 现在是“AI 知道应该发 PR”
- 不是“AI 有仓库自带的发 PR 执行接口”

### Gap 3：缺少 GitHub review comment 拉取与线程回复能力

现状：

- `quality-review-feedback` 只定义“收到反馈后如何判断”
- 没有 GitHub API / `gh api` / MCP 驱动的正式资产

缺什么：

- 拉取 PR review、inline comments、top-level comments
- 将 comment 按线程、文件、严重级别归类
- 回复原 review thread，而不是误发顶层评论
- 标记已处理 / unresolved / need clarification
- 将 comment 与 code diff / commit SHA 关联

影响：

- 现在这个 skill 前提是“评论已经被人喂给你了”
- 还不能自己去 GitHub 抓评论、逐条回帖、更新状态

### Gap 4：缺少 merge conflict / rebase 冲突处理 workflow

现状：

- `agent-orchestration` 只提到“合并冲突成本会影响是否并行”
- 仓库里没有专门处理 merge conflict 的 skill

缺什么：

- 识别冲突来源：rebase、merge、cherry-pick、update branch
- 冲突分类：文本冲突、生成文件冲突、锁文件冲突、重命名冲突
- 解冲突策略：ours / theirs / 手工三方合并 / 重新生成
- 冲突后验证与风险记录
- 回复 review “已 rebase / 已解决冲突”的状态更新

影响：

- 这是你离“AI 能自己把 PR 合进去”最硬的缺口之一

### Gap 5：缺少 CI / checks 轮询与失败修复闭环

现状：

- 有 `quality-verify`
- 没有仓库自有的“PR 发出后看 checks -> 失败则修 -> 再推”的正式资产

缺什么：

- 读取 `gh pr checks` / Actions / CI provider 状态
- 抓失败日志
- 将失败路由到相应修复 skill
- 修复后再 push
- 判断是否 ready to merge

影响：

- 现在验证主要发生在“发 PR 前”
- 但真实 PR 生命周期的大量问题发生在“发 PR 后”

### Gap 6：缺少 merge / auto-merge / cleanup 的 GitHub 执行面

现状：

- `finishing-a-development-branch` 描述了 merge / keep / discard
- 但没有“批准后如何 merge PR”的仓库自有命令或 skill

缺什么：

- squash / merge / rebase merge 策略
- merge 前是否要求 branch up-to-date
- auto-merge 开关
- merge 成功后的 branch 删除
- worktree 清理、session 收尾、记录回写

影响：

- 现在能描述“该合并了”
- 不能稳定执行“怎么合、何时合、合完怎么收尾”

### Gap 7：缺少运行时集成，而不只是 source skill

现状：

- 你有 source skill
- 也有一部分 Codex target 镜像
- 但没有专门面向 GitHub 生命周期的 target runtime

缺什么：

- `gh` 可用性检查
- GitHub auth 检查
- `gh` / MCP 两种执行面择优策略
- 平台命令，例如 `/pr-create`、`/pr-sync`、`/review-feedback`、`/pr-merge`
- hooks，例如 PR 创建后记录 URL、push 前提醒、pre-merge gate

影响：

- 现在仓库更像“知识包”
- 还不是“带执行按钮的工具包”

### Gap 8：缺少状态机和持久化

现状：

- `nanospec` 能记录任务过程
- `.quality/quality-check.md` 能记录阶段结论
- 但没有 PR 生命周期级别的状态文件

缺什么：

- 当前 PR 编号
- 当前 review 状态
- unresolved comments 列表
- CI 状态
- merge blockage 列表
- 最近一次 push / sync / rebase / merge 的时间点

影响：

- AI 可以单轮处理片段
- 但跨多轮、多天持续跟 PR 时，状态容易漂

## 次要缺口

### Gap 9：缺少仓库级 PR 规范资产

当前没有正式沉淀：

- PR title / body 模板
- reviewer 分配策略
- draft vs ready 的切换标准
- comment severity 与处理 SLA
- merge policy（squash / rebase / merge commit）

### Gap 10：缺少面向评论处理的质量门禁

`quality-review-feedback` 已有“先理解再改”，但还缺：

- “一条评论一个 commit / 一轮 comment batch 一个 verify”之类的操作纪律
- “回完评论前先跑哪些验证”的明确门槛
- “哪些评论必须回帖解释，哪些只需修复”的区分

### Gap 11：缺少专门的 GitHub / gh skill 包

从仓库组织上看，还没有一个专门的 `packages/github-workflows/` 或 `packages/pr-workflows/`：

- `git-workflows` 解决的是本地 git 生命周期
- `quality-workflows` 解决的是评审与验证纪律
- 真正的 GitHub PR 生命周期还没有独立 package 承载

## 如果目标是“最终都让 AI 来做”，最缺的不是 prompt，而是这三层

### 1. GitHub 执行层

- `gh` / GitHub MCP 调用
- PR create / view / checks / review / merge / reply

### 2. PR 生命周期状态层

- PR 状态记录
- unresolved review items
- CI / merge blockage

### 3. 冲突与失败恢复层

- merge conflict 处理
- CI 失败修复
- review comment 多轮往返

## 建议的吸纳顺序

### 第一批：先补最短闭环

1. `request-review` skill
2. `pr-create` skill 或 command
3. `review-feedback` GitHub 线程版增强
4. `pr-merge` skill

目标：

- 先让 AI 能完成：
  - 发 PR
  - 读评论
  - 处理评论
  - 合并

### 第二批：补 post-PR 闭环

1. `pr-checks` / `ci-fix` skill
2. `pr-status` 记录文件或状态模板
3. PR logger / PR summary hook

目标：

- 发 PR 后能继续自驱推进，而不是停在“等你来贴日志”

### 第三批：补 hardest path

1. `merge-conflict-resolution` skill
2. `rebase-and-sync` skill
3. auto-merge / branch cleanup 规则

目标：

- 让 AI 能处理最难、最容易翻车的部分

## 总结

当前仓库的真实状态是：

- **本地开发收尾能力：有**
- **评审判断能力：有**
- **评审反馈处理纪律：有**
- **GitHub PR 生命周期执行能力：明显不足**
- **merge conflict / CI / review thread 自动闭环：基本没有**

所以如果你的目标是“最终提 PR、review、合并、解冲突都让 AI 来做”，下一步最合理的不是继续抽象 workflow，而是新增一个专门承载 GitHub / PR 生命周期的 package，把本地 git workflow 和远端 PR workflow 接起来。

