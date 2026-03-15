# 学习积累模板

## 1. `learnings.md` 模板

```md
# Learnings

## <YYYY-MM-DD> <主题>

### Learning: <一句话模式名>

- 场景：
- 触发信号：
- 采取动作：
- 证据：
- 适用范围：
- 非适用范围：
- 当前状态：`keep-local` | `promote-later` | `drop`
```

## 2. `promote-candidates.md` 模板

```md
# Promote Candidates

## <YYYY-MM-DD> <主题>

### Candidate: <一句话候选名>

- 来源任务：
- 想沉淀的模式：
- 为什么可能跨任务复用：
- 现有重叠资产：
- 建议动作：`new` | `absorb` | `drop`
- 需要补的内容：
```

## 3. `project-rules.md` 模板

```md
# Project Rules

## <YYYY-MM-DD> <主题>

### Rule Candidate: <一句话规则名>

- 规则内容：
- 作用范围：`repo` | `project` | `target`
- 来源纠正：
- 证据：
- 建议落点：`AGENTS.md` | `README.md` | `<skill-path>` | `<eval-path>`
- 当前状态：`propose-agents-update` | `keep-local` | `drop`
```

## 4. 写法约束

- 一条记录只写一个明确模式。
- `证据` 至少指向一个真实来源：文件、输出、用户纠正、验证结果或差异点。
- `适用范围` 和 `非适用范围` 必须同时出现，避免抽象化。
- `promote-candidates.md` 只放“可能升级”的候选，不放已经决定丢弃的噪音。
- `project-rules.md` 只放项目级 / 公共规则纠正，不要把普通任务技巧混进去。
