# Alignment Log

## 2026-03-19

- [变更] 用户发起“仓库重组为 `packages/` 主组织”任务，并要求本轮先写 spec，不直接进入 plan / execute。
- [变更] 本轮口径明确为：package-first 只作用于仓库自有可交付资产层；`.nanospec/`、`nanospec/`、`.learned/`、`.quality/`、`.research/`、`scripts/` 等控制 / 记录目录继续保留在根级。
- [变更] `references/repos/` 继续保留为根级外部参考仓库例外，不纳入 package 资产层重组；其中翻译资产后续按用户澄清保留在 `references/translations/`，不进入 package。
- [变更] 用户将本轮任务升级为 `/run`：不仅要继续写 plan，还要完整推进到执行、验收与总结。
- [变更] 用户明确给出新的重组原则：能单独运行、能单独分发的能力，优先成为单主题 package，而不是继续挂在 `domains` 目录下；分类关系交给 README 组织，而不是靠 `src/domains/*` 表达。
- [变更] 用户要求把 Codex target 分发改成脚本自动化，避免后续每次手工同步 source / target 时反复消耗 token。
- [变更] 本轮 scope 因此从“把现有顶层内容归入 `packages/`”进一步收敛为“去 `domains` 化、package-first、README 组织分类、Codex target 自动分发”。
- [偏差] 上一版 spec 仍保留“`src/domains/*` 中的资产获得 package 归属”的过渡表述，已不足以表达新的 package-first 目标；需要同步重写 spec / plan / tasks，避免把 `src/domains` 继续写成长期结构。
- [缺失] 当前仓库尚无统一的 Codex target 自动同步脚本，也没有约定哪些文件属于 package source、哪些文件属于 target-side runtime config；plan 阶段需要补上这一点。
- [变更] 用户进一步澄清：翻译资产不属于要分发出去的东西，不需要组织成 package；应保留在 `references/` 或根目录显眼位置，优先接受 `references/`。
- [偏差] 刚完成的实现把翻译资产迁到了 `packages/upstream-translations/`，这与用户刚给出的边界不一致；需要立即回退为 `references/translations/`，并同步修正 README、AGENTS、spec、plan、tasks 与学习记录。
