# superpowers worktree / clean skill 吸收记录

检查时间：2026-03-24

## 任务目标

- 同步本地 `references/repos/superpowers` 到 upstream 最新 `main`
- 检查 `using-git-worktrees` 与“clean”相关 skill 是否有变更
- 将这两个能力以当前仓库自有 package 的方式吸纳进来

## 检查范围

- 上游参考仓：`references/repos/superpowers`
- 关注 skill：
  - `skills/using-git-worktrees/SKILL.md`
  - `skills/finishing-a-development-branch/SKILL.md`
- 当前仓库已有相邻资产：
  - `packages/agent-orchestration/`
  - `packages/quality-workflows/`

## 同步结果

- 本地 `superpowers` 原 HEAD：`7e516434f2a30114300efc9247db32fb37daa5f9`
- upstream `origin/main`：`8ea39819eed74fe2a0338e71789f06b30e953041`
- 已对本地参考仓执行 fast-forward

新增的 upstream 提交为：

- `8ea3981` Add issue templates and disable blank issues
- `7642153` Add PR template to filter low-quality submissions
- `eccd453` Add Contributor Covenant Code of Conduct
- `fb4adab` Bump cursor plugin version to match release

## 变更结论

- `using-git-worktrees`：无变更
- `finishing-a-development-branch`：无变更
- 因此这次不是“追上新 skill 版本”，而是把当前稳定能力正式吸纳进仓库

## 候选能力拆解

### 1. `using-git-worktrees`

稳定价值：

- worktree 目录选择优先级
- 项目内目录必须先做 ignore 校验
- 建立隔离工作区后先做 baseline 验证
- 与实现流程、子 agent 流程可直接组合

不直接照搬的点：

- 强绑定 `CLAUDE.md`
- 默认自动安装依赖
- 未区分不同 harness 的权限/审批模型

### 2. `finishing-a-development-branch`

稳定价值：

- 完成后先验证，再给出口
- 用结构化选项替代开放式“接下来怎么办”
- 清理 branch / worktree 时要求显式确认

需要修正的点：

- upstream 原文对“选项 2：Push and Create PR”是否自动清理 worktree 存在自相矛盾：
  - 步骤正文写“Then: Cleanup worktree”
  - Quick Reference 又写“Keep Worktree = ✓”
- 当前仓库吸收时改为更保守规则：
  - `push + PR/MR` 后默认保留 worktree
  - 只有用户明确要求时才清理

## 决策

- 结论：`adapt`
- 采用新 package：`packages/git-workflows/`
- 以仓库自有、平台无关的方式沉淀两项 skill：
  - `using-git-worktrees`
  - `finishing-a-development-branch`

## 适配原则

- 保留核心 workflow，不绑定某一平台的 prompt 文件名
- 不默认执行高副作用动作，例如自动 `git pull`、自动装依赖、自动删 worktree
- 对需联网、需审批、可能破坏现场的步骤，统一改成“先检查、再确认、后执行”

