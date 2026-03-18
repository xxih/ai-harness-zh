---
name: verification-before-completion
description: 当你准备声称工作已完成、已修复或已经通过时，在 commit 或创建 PR 前使用；它要求先运行验证命令并确认输出，任何成功表述都必须以证据为先
---

# 完成前验证

## 概览

没有验证就声称工作完成，不是高效，而是不诚实。

**核心原则：**先有证据，再有结论。

**违背这条规则的字面要求，就是违背它的精神。**

## 铁律

```
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
```

如果你没有在当前消息对应的上下文里亲自运行验证命令，就不能声称它已经通过。

## 闸门函数

```
在声称任何状态、或表达任何满意之前：

1. IDENTIFY：什么命令可以证明这个结论？
2. RUN：运行完整命令（fresh、完整）
3. READ：完整查看输出、退出码和失败数量
4. VERIFY：输出是否真的支持这个结论？
   - 如果 NO：带着证据陈述真实状态
   - 如果 YES：带着证据陈述结论
5. ONLY THEN：再做结论表达

跳过任一步 = 在撒谎，不是在验证
```

## 常见失败模式

| Claim | Requires | Not Sufficient |
|-------|----------|----------------|
| Tests pass | 测试命令输出 0 failures | 之前跑过、或“should pass” |
| Linter clean | linter 输出 0 errors | 部分检查、外推 |
| Build succeeds | build 命令 exit 0 | linter 通过、日志看着没问题 |
| Bug fixed | 原始症状验证通过 | 改了代码、主观觉得修好了 |
| Regression test works | 验证过红-绿循环 | 测试只通过了一次 |
| Agent completed | VCS diff 显示真实变更 | agent 说“success” |
| Requirements met | 按行逐项核对 checklist | 测试通过 |

## 红旗 - 立刻停下

- 使用 “should”“probably”“seems to” 之类措辞
- 在验证前表达满意（“Great!”、“Perfect!”、“Done!” 等）
- 没验证就要 commit / push / 开 PR
- 直接信任 agent 的成功汇报
- 依赖部分验证
- 想着“就这一次”
- 因为累了想尽快结束
- **任何暗示“已经成功”的说法，而你其实还没做验证**

## 防合理化表

| Excuse | Reality |
|--------|---------|
| "Should work now" | 去跑验证 |
| "I'm confident" | 信心 ≠ 证据 |
| "Just this once" | 没有例外 |
| "Linter passed" | linter ≠ compiler |
| "Agent said success" | 独立验证 |
| "I'm tired" | 疲惫不是借口 |
| "Partial check is enough" | 部分验证证明不了结论 |
| "Different words so rule doesn't apply" | 看精神，不看字面绕法 |

## 关键模式

**Tests：**
```
✅ [Run test command] [See: 34/34 pass] "All tests pass"
❌ "Should pass now" / "Looks correct"
```

**Regression tests（TDD Red-Green）：**
```
✅ Write → Run (pass) → Revert fix → Run (MUST FAIL) → Restore → Run (pass)
❌ "I've written a regression test" (without red-green verification)
```

**Build：**
```
✅ [Run build] [See: exit 0] "Build passes"
❌ "Linter passed" (linter doesn't check compilation)
```

**Requirements：**
```
✅ Re-read plan → Create checklist → Verify each → Report gaps or completion
❌ "Tests pass, phase complete"
```

**Agent delegation：**
```
✅ Agent reports success → Check VCS diff → Verify changes → Report actual state
❌ Trust agent report
```

## 为什么重要

根据 24 条失败记忆整理：
- 人类协作者曾直接说过 “I don't believe you” —— 信任一旦受损，很难恢复
- 未定义函数被错误地当成已完成交付——上线就会崩
- 有遗漏需求却被当成完成——功能实际不完整
- 伪完成会带来返工：错误宣称完成 → 被拉回 → 重做
- 这违反了“Honesty is a core value. If you lie, you'll be replaced.”

## 何时应用

**以下场景一律适用：**
- 任何形式的成功 / 完成宣称
- 任何表达满意的措辞
- 任何关于当前工作状态的正向结论
- commit、创建 PR、标记任务完成之前
- 进入下一个任务之前
- 把工作交给其他 agent 之前或之后做结果确认时

**规则适用于：**
- 原句
- 同义改写
- 含蓄表达成功
- **任何**暗示“已经正确 / 已经完成”的沟通

## 最后结论

**验证没有捷径。**

跑命令。读输出。然后再下结论。

这是不可协商的。
