# learning-capture补充AGENTS联动

目标：

把原先想写进 `learning-capture` 正文的 AGENTS 协同说明，上收为领域级 `_AGENTS.md` 规则：在 `src/domains/<domain>/` 子一级提供一个载体文件，用来存放某些 skill / command 搭配时需要默认注入的上下文。

要求：

1. 用 NanoSpec 方式补齐本次任务的 spec / plan / tasks。
2. 尽量不改现有 skill 正文，只补全局规则与首个领域示例。
3. 明确 `_AGENTS.md` 的分隔机制，采用 XML 注释标签包裹，并能直接标明“这块是给哪个 skill / command 搭配使用的”。
4. 当前仓库自有资产中，仅保留根目录 `AGENTS.md` 与 `.nanospec/AGENTS.md`；`targets/` 若需要承载这类内容，统一存为 `_AGENTS.md`。
