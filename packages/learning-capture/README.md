# learning-capture 包

这个包承载“手工触发学习沉淀”能力，以及配套的默认注入上下文。

## 组成

- `_AGENTS.md`
  - 用户反馈捕获上下文块
- `skills/learning-capture/`
  - `learning-capture` skill
- `targets/codex/`
  - 面向 Codex 的最小 target 包

## 说明

- 这仍然是当前仓库的资产，不是外部参考 repo
- skill 正文默认把记录写到仓库根目录 `.learned/`
- 若后续需要别的目标平台，可继续在当前包内增加 `targets/<tool>/`
