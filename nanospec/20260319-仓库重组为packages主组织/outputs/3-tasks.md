## 1. 已完成

验收条件：当前任务容器已建立，并完成首版 spec 与边界记录。

- [x] 1.1 创建 `20260319-仓库重组为packages主组织` 任务骨架，并写入 `.nanospec/.current`。
- [x] 1.2 补充 `brief.md`，明确“以 `packages/` 为主组织形式”的任务目标。
- [x] 1.3 执行 `/align`，记录“去 `domains` 化、单主题 package、Codex target 自动分发”的新范围。
- [x] 1.4 更新 `outputs/1-spec.md`，把目标收敛为 package-first、README 分类组织与脚本自动分发。

## 2. 方案与边界

验收条件：迁移映射、根级例外与脚本自动化方式已经明确。

- [x] 2.1 产出 `outputs/2-plan.md`，明确 package 映射、根级例外和执行顺序。
- [x] 2.2 明确控制目录继续留在根级，不纳入 package 资产层重组。
- [x] 2.3 明确 `references/repos/` 保留为根级外部参考仓库例外，翻译资产保留在 `references/translations/`。
- [x] 2.4 明确 Codex target 自动分发只镜像 source 资产，不覆盖 target 侧 `.codex/*` 等手写 runtime 文件。

## 3. 目录重组

验收条件：自有资产已迁入 package，根级不再保留旧的资产主入口。

- [x] 3.1 将 `nanospec`、`spec-driven`、`search-first`、`agent-orchestration`、`writing-skills` 迁入新的单主题 `packages/*/`。
- [x] 3.2 保留 `references/translations/` 在 references 下，并仅将需要分发的参考资料迁入对应 package。
- [x] 3.3 将根级 `targets/codex/.codex/` 基线迁入 `packages/codex-base/`。
- [x] 3.4 删除已失效的 `src/`、根级 `targets/` 与已迁出的根级内部 references 目录。

## 4. 文档改写

验收条件：正式说明文档已切换到 package-first 口径。

- [x] 4.1 更新根 `README.md`，以 package 清单而不是 domains 分层介绍仓库。
- [x] 4.2 更新 `packages/README.md`，按主题组织 package 分类。
- [x] 4.3 为新增 package 补齐或更新 README，说明包边界与 Codex target 维护方式。
- [x] 4.4 更新 `AGENTS.md` 与 `references/README.md`，同步新的目录规则与例外。

## 5. Codex target 自动分发

验收条件：Codex target 镜像已改为脚本同步，且现有 package target 已完成回写。

- [x] 5.1 新增 `scripts/sync_codex_targets.py`。
- [x] 5.2 运行脚本同步各 package 的 `targets/codex/` 镜像文件。
- [x] 5.3 校对脚本没有覆盖 `README.md`、`.codex/*` 等 target 侧手写文件。

## 6. 验收与沉淀

验收条件：有明确验收清单、验证证据与最终总结。

- [x] 6.1 生成 `outputs/acceptance.md`，覆盖结构、文档与脚本三类验收场景。
- [x] 6.2 运行必要校验，确认目录结构与脚本同步结果符合 spec。
- [x] 6.3 生成 `outputs/summary.md`，沉淀最终结构、关键决策与后续建议。
