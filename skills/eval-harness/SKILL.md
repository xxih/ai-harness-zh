---
name: eval-harness
description: Use when creating or revising reusable AI prompt assets that need explicit success criteria, regression coverage, and repeatable validation across skills or commands.
---

# Eval Harness

将评估当作 AI prompt 资产的单元测试。先定义通过标准，再改资产，再执行评分器，最后报告结果。

## 何时使用

- 新建或重构可复用的 `skill`
- 新建或重构可复用的 `command`
- 为 prompt 资产建立回归保护
- 比较不同版本资产的稳定性或通过率

如果只是一次性的临时 prompt，不需要沉淀为仓库资产时，不必启用这个 skill。

## 产物

每次使用本 skill 时，默认产出以下内容中的最小必要集合：

1. 目标资产本身
   - `skills/<name>/SKILL.md`
   - 或 `commands/<name>.md`
2. 配套评估定义
   - `evals/skills/<name>.md`
   - 或 `evals/commands/<name>.md`
3. 必要的确定性校验脚本
   - `scripts/...`
4. 一份简短的验证结论
   - 说明通过项、失败项、残余风险

## 工作流

1. 先界定资产边界
   - 明确资产服务的场景、输入、输出和不负责的部分
   - 尽量避免把共享资产绑定到单一 AI 工具或单一目录约定
2. 先写评估，再写资产
   - 定义 capability evals：新资产应具备什么能力
   - 定义 regression evals：不能破坏哪些既有约束
   - 优先选用代码评分器，其次规则评分器，再考虑模型评分器或人工审查
3. 最小化实现
   - 只写通过当前评估所需的最小改动
   - 把模板、示例和长文档放进 `references/`，不要把 `SKILL.md` 写成说明书
4. 执行验证
   - 运行确定性检查并记录结果
   - 需要多次尝试时再记录 `pass@k`
   - 发布关键路径或高风险资产优先使用 `pass^k`
5. 汇总结论
   - 输出通过率、阻塞项和是否可继续复用

## 评分器选择顺序

1. 代码评分器
   - 文件存在、frontmatter 完整、关键片段命中、脚本返回码正确
2. 规则评分器
   - 正则、schema、目录结构、命名约束
3. 模型评分器
   - 结构质量、表达清晰度、边界覆盖
4. 人工评分器
   - 安全、合规、业务高风险判断

默认原则：能用确定性评分器，就不要用模型评分器。

## 指标

- `pass@1`：首次尝试即通过
- `pass@k`：最多 k 次尝试内至少一次通过
- `pass^k`：连续 k 次全部通过

建议阈值：

- capability evals：`pass@3 >= 0.90`
- regression evals：关键路径 `pass^3 = 1.00`

## 约束

- 共享 skill 优先写成工具无关版本；只有目标平台强绑定时，才引入平台细节
- 评估必须能在仓库内落盘，不要只存在于对话里
- 评估应尽量快速，否则团队不会持续执行
- 安全、权限、外部系统写操作等高风险事项，保留人工审查

## 模板

需要示例时，读取 [references/templates.md](references/templates.md)。
