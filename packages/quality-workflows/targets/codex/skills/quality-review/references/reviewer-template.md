# Reviewer Template

用于独立 reviewer 或 multiagent reviewer 的统一评审模板。

## 输入

- `WHAT_WAS_IMPLEMENTED`
- `PLAN_OR_REQUIREMENTS`
- `BASE_SHA`
- `HEAD_SHA`
- `DESCRIPTION`

## 审查重点

### Code Quality

- 职责是否清晰
- 错误处理是否完整
- 类型或接口约束是否可靠
- 是否引入不必要复杂度

### Architecture

- 设计是否符合当前问题规模
- 是否有明显的性能或安全风险
- 是否引入意外副作用

### Testing

- 测试是否真的覆盖真实逻辑，而不是只测 mock
- 是否覆盖关键边界和回归风险
- 当前测试结果是否可信

### Requirements

- 是否符合计划、spec 或验收条件
- 是否有 scope creep
- 是否遗漏关键需求

## 输出格式

### Strengths

- 写清楚做得好的具体点

### Issues

#### Critical

- 必修问题：功能错误、安全问题、数据风险、明显不满足需求

#### Important

- 应修问题：关键边界缺失、错误处理不足、测试缺口、设计偏差

#### Minor

- 可后续处理的问题：命名、提示信息、轻量优化、文档补充

每个问题至少写清：

- 文件或位置
- 问题是什么
- 为什么重要
- 如何修复

### Assessment

- 是否 `ready`
- 一到两句技术判断
