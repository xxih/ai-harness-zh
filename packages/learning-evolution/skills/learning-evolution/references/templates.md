# 学习演化模板

## 1. 先选出口

每条信号先收口到以下之一，再决定怎么写：

- `drop`
- `keep-task-local`
- `queue-support`
- `codify-now`

## 2. `.learned/support.md` 模板

```md
# Support

## <YYYY-MM-DD> <主题>

### Support: <一句话标题>

- 类型：`skill` | `command` | `eval` | `doc` | `workflow`
- 作用域：`project` | `cross-project`
- 触发：
- 重复信号：
- 证据：
- 原料：
- 建议落点：`<skill-path>` | `<command-path>` | `<eval-path>` | `README.md` | `AGENTS.md`
- 建议动作：`update-existing` | `new-skill` | `new-command` | `new-eval` | `doc-update` | `queue-support` | `drop`
```

写之前先自问：这条内容是否明确在支持某个正式资产？如果回答不出来，就不要写进 `support.md`。

## 3. `.learned/rules.md` 模板

```md
# Rules

## <YYYY-MM-DD> <主题>

### Rule: <一句话规则名>

- 规则：
- 证据：
- 落点：`project-instructions` | `README.md` | `<skill-path>` | `<eval-path>`
- 下一步：`propose-rules-doc-update` | `codify-now` | `keep-local` | `drop`
```

## 4. task-local learnings 写法

若内容只服务当前工作，不进入 `.learned/`，应直接回写当前上下文已有记录位置；至少写清：

- 当前 learnings 是什么
- 它影响当前工作的哪个后续动作
- 下一步如何消费它

## 5. 写法约束

- 一条记录只写一个明确模式。
- `support.md` 只承接长期候选的支撑卡，不承接普通杂记。
- `证据` 至少指向一个真实来源：文件、输出、用户纠正、验证结果或差异点。
- `原料` 要尽量写成后续可直接 codify 的素材，例如步骤骨架、输入输出样例、验证线索、边界。
- 若记录来自运行过程中的显式反馈信号，优先把原始反馈写进 `证据`，不要自行改写成模糊共识。
- 若证据已足够支撑正式资产更新，就应优先 `codify-now`，不要无限堆积在 `support.md`。
