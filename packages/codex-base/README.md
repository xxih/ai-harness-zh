# codex-base 包

这个包承载仓库维护的 Codex 基线 target 包。

## 组成

- `targets/codex/.codex/`
  - Codex 项目基线配置与角色注册

## 说明

- 这是一个平台绑定包，内容本身就是 target 侧运行时文件
- 不通过 `scripts/sync_codex_targets.py` 生成；按需手工维护
