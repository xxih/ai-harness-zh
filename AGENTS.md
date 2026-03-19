## 语言

- 该仓库默认使用简体中文
- 新增或修改仓库内文档、skill、command、eval 定义时，默认优先使用中文
- 代码、路径、API 名称、协议关键字保持原文

## 工作规则

- 当前仓库自有资产默认采用 package-first 组织；能单独理解、单独分发、单独运行的能力，优先直接放进 `packages/<package>/`
- 资产分类关系交给 `README.md` 与 `packages/README.md` 组织，不再依赖 `domains` 分层
- 共享资产默认保持工具无关，只有目标平台明确绑定时才写入平台细节
- 涉及结构性变更后，同步更新对应说明文档，避免仓库约定失真
- 外部参考仓库统一放在 `references/repos/`，该目录供 AI 读取，但不纳入当前仓库 git 管理
- 外部 prompt 中文翻译资产保留在 `references/translations/` 或其他根级显眼参考位；这类资料默认不组织成分发 package
- Codex target 镜像默认通过 `scripts/sync_codex_targets.py` 同步，不手工逐个复制 source / target
- 当前仓库自有资产中，仅允许保留根目录 `AGENTS.md` 与 `.nanospec/AGENTS.md`；其他位置禁止新增或保留 `AGENTS.md`
- `packages/*/targets/` 中若需要表达这类分发内容，一律存为 `_AGENTS.md`；实际如何落成运行时 `AGENTS.md` 留待后续工具化分发再处理

## 反馈信号沉淀

<!-- AGENTS: user-feedback-capture -->

- 记录用户明确给出的长期规则、接受 / 拒绝标准和稳定偏好。
- 只记录用户明确表达的内容；不根据语气、情绪或一次性抱怨自行推断。
- 写入位置：
  - 项目级 / 团队级 / 分发级规则 -> `.learned/rules.md`
  - 其他可复用经验或局部做法 -> `.learned/notes.md`
- 写入内容：至少包含内容本身、证据来源、建议落点、下一步动作。
- 默认动作：只记录为候选，不直接修改正式共享文档。
<!-- /AGENTS: user-feedback-capture -->

## Commit 规范

使用简单单行格式：

`<type>: <summary>`

推荐类型：

- `feat`：新增资产或新增能力
- `fix`：修复问题或修复校验
- `docs`：文档或 prompt 文案更新
- `refactor`：重构但不改变预期行为
- `test`：补充或调整验证样例、检查步骤或测试材料
- `chore`：仓库维护

补充约定：

- `summary` 默认使用简洁中文
- 一个 commit 只做一类相对聚焦的改动
- 除非是仓库级变更，否则不要把无关资产混在同一个 commit
