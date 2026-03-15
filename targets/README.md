# 分发适配层

`src/` 下保存工具无关的核心 prompt 资产；`targets/` 下保存面向具体 AI 工具的分发快照与适配层。

约定：

- `targets/<tool>/` 应优先保持与 `src/` 同构，例如 `skills/`、`agents/`、`commands/`
- 在同构资产之外，再叠加该工具需要的配置、包装说明和角色注册
- `targets/` 内容应由 `src/` 同步生成；源资产仍以 `src/` 为准
- 如果未来某个工具需要真正可发布的打包产物，再额外生成到 `dist/`，不要手改生成物

当前已落地：

- `targets/codex/`：Codex CLI 的同构分发目录，包含 `src` 镜像和项目级 `.codex/` 适配基线
