## Coding Tasks（gstack）

### Rules（non-negotiable）

1. **Always spawn, never redirect.** 当用户要求使用任意 gstack skill 时，
   一律通过 `sessions_spawn` 直接拉起 Claude Code session。不要让用户自己
   打开 Claude Code。不要说“这个需要在 Claude Code 里跑”。也不要说
   “你需要自己去打开 Claude Code”。直接做。

2. **Resolve the repo.** 如果用户提到了 repo 或 project，就把 working
   directory 指向对应 repo path。如果路径未知，就追问是哪个 repo，
   不要把动作推回给用户。

3. **Autoplan runs end-to-end.** 对 `/autoplan` 来说：要先 spawn session，
   让它跑完整条 review pipeline（CEO → design → eng），结束后再把 plan
   回报到这里的 chat。把 plan 写入 memory，保证用户之后还能找到。
   用户不应为了这件事离开 Telegram。

### Dispatch Routing

当收到 coding work 时，按下列 tier 选择 dispatch：

**SIMPLE：** “修这个 typo”、“更新那个 config”、单文件改动  
→ `sessions_spawn(runtime: "acp", prompt: "<just the task>")`

**MEDIUM：** 多文件 feature、refactor、skill edits  
→ `sessions_spawn(runtime: "acp", prompt: "<gstack-lite content>\n\n<task>")`

**HEAVY：** 需要特定 gstack methodology  
→ `sessions_spawn(runtime: "acp", prompt: "Load gstack. Run /qa https://...")`  
  Skills：`/cso`、`/review`、`/qa`、`/ship`、`/investigate`、`/design-review`、
  `/benchmark`、`/gstack-upgrade`

**FULL：** 构建完整 feature、多日 scope、需要 planning + review  
→ `sessions_spawn(runtime: "acp", prompt: "<gstack-full content>\n\n<task>")`  
  Claude Code 将执行：`/autoplan` → implement → `/ship` → report back

**PLAN：** 用户想先规划一个 Claude Code project、把 feature/spec 设计清楚，
还不开始写代码  
→ `sessions_spawn(runtime: "acp", prompt: "<gstack-plan content>\n\n<task>")`  
  Claude Code 将执行：`/office-hours` → `/autoplan` → 保存 plan file → 回报  
  同时把 plan link 持久化到 memory/knowledge store。  
  等用户准备开始实现时，再基于该 plan spawn 一个新的 FULL session。

### Decision Heuristic

- 能否在不到 10 行代码内完成？ → **SIMPLE**
- 会改多个文件，但实现路径很明确？ → **MEDIUM**
- 用户是否点名具体 skill（`/cso`、`/review`、`/qa`）？ → **HEAVY**
- “Upgrade gstack” / “update gstack” → **HEAVY**，并执行 `Run /gstack-upgrade`
- 这是一个 feature、project 或 objective（不是单一 task）？ → **FULL**
- 用户是否想先规划而不实现？ → **PLAN**
