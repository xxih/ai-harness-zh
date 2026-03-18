# 质量领域

这个领域承载编码过程中的质量门禁资产，包括 TDD、验证、评审以及评审反馈处理。

## 范围

- `quality-*` skill 家族
- 独立 reviewer agent
- 命令式质量入口与阶段化质量记录

## 领域规则

- 质量动作要围绕证据、门禁和分级结论展开，而不是流程口号
- 可复用 reviewer prompt 放在 `agents/`
- 轻量入口放在 `commands/`；如果直接调用 skill 更清楚，可以不额外补 command
- 公共落盘目录优先复用 `.quality/`
