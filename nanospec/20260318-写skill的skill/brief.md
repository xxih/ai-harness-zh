# 写skill的skill

## 背景

用户希望参考 `.research/skill-authoring-landscape.md` 的调研结论，用 `nanospec` 工作流产出一个“创建 skill 的 skill”。

当前仓库里已经存在一个 `writing-skills` 初稿，但上一版把很多当前仓库内部结构误写进了 skill 正文。需要按本次任务把它纠正为默认可独立分发、可被其他人直接导入 AI 工具使用的 skill。

## 目标

1. 用 NanoSpec 为本次任务建立完整的 brief / spec / plan / tasks 工作面。
2. 产出或确认一个可复用的“创建 skill”资产，正文默认保持独立，不依赖当前仓库内部目录结构。
3. 让该 skill 明确体现调研结论：
   - adopt Anthropic 的底层规范与 progressive disclosure
   - adapt Superpowers 的 fail-first / pressure scenario 迭代闭环
   - adapt Codex `skill-creator` 的目录工程化与资源分层
4. 若当前仓库维护某个工具的分发副本，只把它当成打包副本，而不是 skill 正文的默认前提。

## 约束

1. 仓库内文档默认使用简体中文。
2. 核心资产默认工具无关、仓库无关。
3. 没有明确说明时，各个 skill 保持独立。
4. 不为了“完整”新增多余 README、安装说明或过程文档。
