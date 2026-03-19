# 验收：仓库重组为 packages 主组织

## 1. package-first 结构

### 场景 1：可分发能力已迁入 `packages/`

- 验证步骤：
  1. 检查根目录是否存在 `packages/agent-orchestration/`、`packages/nanospec/`、`packages/search-first/`、`packages/spec-driven/`、`packages/writing-skills/`、`packages/learning-capture/`、`packages/quality-workflows/`、`packages/codex-base/`
  2. 检查根目录是否已不存在 `src/` 与根级 `targets/`
- 预期结果：
  - package 目录存在
  - `src/` 与根级 `targets/` 不再存在
- 证据：
  - `README.md`
  - `packages/README.md`
  - 当前工作区根目录结构检查结果

## 2. 翻译资产例外

### 场景 2：翻译资产保留在 references

- 验证步骤：
  1. 检查 `references/translations/` 是否存在
  2. 检查 `packages/upstream-translations/` 是否不存在
  3. 检查根 `README.md` 与 `references/README.md` 是否明确翻译资产不属于分发 package
- 预期结果：
  - 翻译资产位于 `references/translations/`
  - 不存在翻译 package
- 证据：
  - `references/translations/README.md`
  - `references/README.md`
  - `README.md`

## 3. Codex target 自动分发

### 场景 3：镜像型 target 可由脚本同步

- 验证步骤：
  1. 运行 `python3 scripts/sync_codex_targets.py`
  2. 检查目标 package 的 `targets/codex/skills/`、`agents/`、`_AGENTS.md` 是否与 source 侧对应
  3. 检查 `packages/codex-base/targets/codex/.codex/` 未被脚本覆盖删除
- 预期结果：
  - 脚本成功完成同步
  - `learning-capture`、`quality-workflows`、`nanospec` 等包的 target 镜像存在
  - `codex-base` 的 `.codex/` 仍保留
- 证据：
  - `scripts/sync_codex_targets.py`
  - `packages/nanospec/targets/codex/skills/nanospec/SKILL.md`
  - `packages/quality-workflows/targets/codex/.codex/config.toml`
  - 最新一次脚本运行输出

## 4. 文档口径一致

### 场景 4：正式文档已切换到新结构

- 验证步骤：
  1. 检查根 `README.md` 是否以 package-first 介绍仓库
  2. 检查 `AGENTS.md` 是否写明 package-first、翻译例外与脚本同步
  3. 检查 `packages/*/README.md` 是否说明各包边界与维护方式
- 预期结果：
  - 文档不再把 `src/` 或根级 `targets/` 当作长期主入口
  - 文档明确翻译资产例外与 Codex target 自动分发
- 证据：
  - `README.md`
  - `AGENTS.md`
  - `packages/nanospec/README.md`
  - `packages/quality-workflows/README.md`
