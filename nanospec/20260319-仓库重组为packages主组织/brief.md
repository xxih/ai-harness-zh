# 仓库重组为packages主组织

目标：

- 把当前仓库的主要资产统一收敛到 `packages/` 下。
- 后续以 `packages/<package>/` 作为仓库主组织形式，而不是继续并列维护 `src/`、根级 `targets/`、根级 `references/` 等多套主入口。

当前诉求：

1. 先为这次仓库重组任务产出 NanoSpec `outputs/1-spec.md`。
2. spec 需要明确重组目标状态、交付边界、成功标志与需要同步更新的说明文档。
