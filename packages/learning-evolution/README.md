# learning-evolution 包

这个包承载“学习信号 -> 判断 -> 分流 -> 沉淀”的闭环能力，以及配套的默认注入上下文。

## 组成

- `_AGENTS.md`
  - 用户反馈与长期候选捕获上下文块
- `skills/learning-evolution/`
  - `learning-evolution` skill
- `targets/codex/`
  - 面向 Codex 的最小 target 包

## 说明

- 这仍然是当前仓库的资产，不是外部参考 repo
- 默认记录分层：长期规则写 `.learned/rules.md`，长期资产支撑卡写 `.learned/support.md`，task-local learnings 优先留在任务容器
- 当证据与目标都足够明确时，本包允许继续 codify 到正式资产，而不是只停在记录层
- 若后续需要别的目标平台，可继续在当前包内增加 `targets/<tool>/`
- Codex target 镜像通过 `python3 scripts/sync_codex_targets.py learning-evolution` 同步
