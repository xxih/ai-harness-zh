---
name: quality-router
description: 质量相关 skill 的手动触发入口；当用户明确说 `/tdd`、`/verify`、`/review` 或 `/review-feedback` 时，路由到对应的 `quality-*` skill。
---

# Quality Router

把质量动作做成显式入口，而不是要求用户记住额外的命名约定。这个 skill 只负责手动路由，不重复各阶段的完整方法论。

## 何时使用

- 你想手动触发某个质量动作，而不是走默认工作流
- 你明确说了 `/tdd`
- 你明确说了 `/verify`
- 你明确说了 `/review`
- 你明确说了 `/review-feedback`

不适用：

- 你需要完整理解某个质量技能本身
- 你还没进入 coding 阶段

## 产物

每次使用本 skill，默认产出以下最小集合：

1. 路由结论
   - 当前请求应进入哪个 `quality-*` skill
2. 质量记录
   - 若当前任务已有自己的记录文件，统一回写到该文件
   - 若没有既定记录位置，默认写入 `.quality/quality-check.md`

## 工作流

1. 识别用户显式触发词
   - `/tdd` -> `quality-tdd`
   - `/verify` -> `quality-verify`
   - `/review` -> `quality-review`
   - `/review-feedback` -> `quality-review-feedback`
2. 只做轻路由
   - 不在这里重复 TDD、验证、评审、评审反馈处理的长规则
   - 进入目标 skill 后，再读取对应 references 或模板
3. 回写统一记录
   - 各阶段结果优先并入当前任务已有记录
   - 若没有共享记录载体，则写入 `.quality/quality-check.md`

## 路由约束

- 这个 skill 是手动入口，不是第二套质量方法论
- 所有质量相关 skill 使用统一前缀 `quality-`
- 若用户未显式触发命令式入口，应直接使用目标 skill，而不是先经过 router
- 若有任务容器或现成记录文件，可以回写，但不依赖任何特定框架
- 默认把结果落到 `.quality/quality-check.md` 或当前工作面，而不是只停留在回复中
