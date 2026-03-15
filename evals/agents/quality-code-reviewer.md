# Asset Eval: quality-code-reviewer

## Asset Under Test

- Type: agent
- Path: agents/quality-code-reviewer.md
- Goal: provide a Chinese subagent specialized in independent code review for the `quality-review` workflow.

## Capability Evals

### capability-1

Goal: the agent performs structured code review with clear severity levels.

Success Criteria:

- [ ] `agents/quality-code-reviewer.md` reviews against requirements or plan
- [ ] `agents/quality-code-reviewer.md` categorizes issues into `Critical` / `Important` / `Minor`
- [ ] `agents/quality-code-reviewer.md` requires an explicit `ready` or `not-ready` assessment

Graders:

- Code: `python3 scripts/validate_assets.py`

### capability-2

Goal: the agent has a stable handoff contract.

Success Criteria:

- [ ] `agents/quality-code-reviewer.md` contains `## 何时使用`
- [ ] `agents/quality-code-reviewer.md` contains `## 输入`
- [ ] `agents/quality-code-reviewer.md` contains `## 输出`
- [ ] `agents/quality-code-reviewer.md` contains `## Prompt`

Graders:

- Code: `python3 scripts/validate_assets.py`

## Regression Evals

### regression-1

Goal: the agent stays Chinese-first and tool-neutral.

Success Criteria:

- [ ] the agent body is primarily in Chinese
- [ ] the agent does not require a specific harness API
- [ ] the agent stays aligned with the `quality-*` naming family

Graders:

- Code: `python3 scripts/validate_assets.py`

## Exit Criteria

- Capability evals: all pass in the current repository state
- Regression evals: all pass in the current repository state
- Report: validation command exits with status `0`
