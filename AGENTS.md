# 项目上下文

## 目标

这是一个沉淀可复用 AI prompt 资产的工作区。

- 核心资产源码放在 `src/skills/`、`src/agents/` 和 `src/commands/`
- 面向不同 AI 工具的分发适配放在 `targets/`
- 每个可复用资产都应在 `evals/` 中具备明确的评估定义
- 只要能做成确定性校验，就优先放进 `scripts/`

## 语言

- 该仓库默认使用简体中文
- 新增或修改仓库内文档、skill、command、eval 定义时，默认优先使用中文
- 代码、路径、API 名称、协议关键字保持原文

## 工作规则

- 把 prompt 资产视为可版本化的项目产物，而不是一次性聊天输出
- `eval-harness` 只在用户明确提出时才启用，不作为默认流程
- 共享资产默认保持工具无关，只有目标平台明确绑定时才写入平台细节
- 涉及结构性变更后，运行 `python3 scripts/validate_assets.py`
- 外部参考仓库统一放在 `references/repos/`，该目录供 AI 读取，但不纳入当前仓库 git 管理

## Commit 规范

使用简单单行格式：

`<type>: <summary>`

推荐类型：

- `feat`：新增资产或新增能力
- `fix`：修复问题或修复校验
- `docs`：文档或 prompt 文案更新
- `refactor`：重构但不改变预期行为
- `test`：补充或调整 eval、校验脚本
- `chore`：仓库维护

补充约定：

- `summary` 默认使用简洁中文
- 一个 commit 只做一类相对聚焦的改动
- 除非是仓库级变更，否则不要把无关资产混在同一个 commit

## README 要按类别组织各个 skill
