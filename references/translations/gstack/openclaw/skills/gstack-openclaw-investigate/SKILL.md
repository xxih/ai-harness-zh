---
name: gstack-openclaw-investigate
description: 以 root cause investigation 为核心的系统化调试。四个阶段：investigate、analyze、hypothesize、implement。铁律是：不先找到根因，就不允许修。用户说要 debug、fix bug、排查 error 或做 root cause analysis 时使用；当用户报告异常、stack trace、unexpected behavior 或“刚刚还好好的现在坏了”时也应主动进入。
version: 1.0.0
metadata: { "openclaw": { "emoji": "🔍" } }
---
<!-- 中文参考译文。 -->

# Systematic Debugging

核心铁律只有一句：**没有根因调查，就不要修。**

## 四个阶段

1. `Investigate`
   - 收集症状、重现步骤、错误信息和上下文
   - 逐步追代码路径，不先拍脑袋下结论
2. `Analyze`
   - 整理证据，缩小怀疑范围
3. `Hypothesize`
   - 明确候选根因，并说清什么证据会推翻它
4. `Implement`
   - 只有在根因成立后才进入修复

## 关键规则

- 一次只问一个问题。
- 不修 symptom，不做 whack-a-mole 式补丁。
- 最终输出必须说明根因、证据和对应修复点。
