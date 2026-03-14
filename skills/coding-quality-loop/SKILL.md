---
name: coding-quality-loop
description: 面向 coding 任务的统一质量闭环。默认按实现前、改动后、交付前给出测试先行、验证、评审建议；若用户明确触发 `/tdd`、`/verify`、`/review`，则路由到对应阶段。
---

# Coding Quality Loop

这是一个面向 coding 任务的统一质量闭环入口。默认提供覆盖实现前、改动后、交付前的整体质量建议；只有当用户明确要求某一阶段时，才展开对应说明。

## 何时使用

- 你正在实现功能、修 bug、重构代码，希望有完整的质量约束
- 你已经完成一轮改动，需要系统检查测试、验证和评审是否齐备
- 你要在高风险改动、关键节点或交付前判断当前结果是否 `ready`
- 你明确说了 `/tdd`、`/verify`、`/review`，想直接进入某个阶段

不适用：

- 还没有进入 coding 阶段
- 目标只是做 prompt 资产治理或文案审校
- 只是机械格式修复，且没有行为变化或质量风险

## 产物

每次使用本 skill，默认产出以下最小集合：

1. 质量结论
   - 若存在当前任务目录，写入 `nanospec/<task>/outputs/quality-check.md`
   - 若不存在任务目录，至少在回复中给出结构化质量结论
2. 阶段结果
   - TDD 阶段：测试策略或失败测试记录
   - Verify 阶段：build / types / lint / tests / diff review 结果
   - Review 阶段：主要风险、阻塞项、是否可继续
3. 最终判断
   - `ready`
   - `not-ready`

## 工作流

1. 默认入口
   - 如果用户只是说“做这个功能”或“修这个 bug”，默认按一条完整质量链路理解：
   - 实现前：判断是否需要测试先行，或先补保护性测试
   - 改动后：执行 build / types / lint / tests / diff review 等验证闭环
   - 交付前：在高风险节点、关键任务完成后或请求评审时做独立审查
2. 路由规则
   - 明确出现 `/tdd`、`先写测试`、`test first`：路由到 TDD 阶段
   - 明确出现 `/verify`、`验证一下`、`跑质量检查`：路由到验证阶段
   - 明确出现 `/review`、`帮我 review`、`做代码评审`：路由到评审阶段
3. 默认建议
   - 有行为变化时，不要跳过测试先行
   - 一轮实现完成后，不要跳过验证闭环
   - 高风险改动、关键任务完成前或交付前，不要跳过独立评审
4. 阶段回写
   - 各阶段结果统一回写到 `quality-check.md` 或当前任务记录中
   - 如果存在阻塞问题，结论必须是 `not-ready`

## 阶段说明

- TDD 阶段：读取 [references/tdd.md](references/tdd.md)
- Verify 阶段：读取 [references/verify.md](references/verify.md)
- Review 阶段：读取 [references/review.md](references/review.md)

## 路由约束

- 默认先给整体质量建议，不要求用户一开始指定阶段
- 只有明确触发阶段动作时，才展开对应细节
- 阶段路由只改变当前响应重点，不改变最终质量闭环
- 这个 skill 解决的是 coding 质量闭环，不绑定特定 harness 或 `.claude/` 目录
