# 分发适配层

`targets/` 下保存**当前仓库共享源资产**的分发快照与适配层。

约定：

- `src/domains/<domain>/` 是共享源资产真相来源
- `targets/` 内容应与 `src/` 保持同步；当前阶段按需手动维护分发快照
- 若某个主题已经在 `packages/<package>/` 内独立成包，它的 target 包优先放在 `packages/<package>/targets/`，而不是继续混在根级 `targets/`
- 如果未来某个工具需要真正可发布的打包产物，再额外生成到 `dist/`，不要手改生成物
