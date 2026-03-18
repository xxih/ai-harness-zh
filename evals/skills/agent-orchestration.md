# Asset Eval: agent-orchestration

## Asset Under Test

- Type: skill
- Path: src/domains/workflow/skills/agent-orchestration/SKILL.md
- Goal: provide a tool-neutral orchestration workflow for the main agent in complex coding tasks, covering role layering, staged execution, single-task delegation, parallel independence checks, anti-duplication rules, and result verification.

## Capability Evals

### capability-1

Goal: the skill defines the main agent's orchestration responsibilities instead of generic multi-agent hype.

Success Criteria:

- [ ] `SKILL.md` explicitly defines role layering such as planner, orchestrator, worker, explore, and reviewer
- [ ] `SKILL.md` defines a staged workflow for complex tasks
- [ ] `SKILL.md` makes the main agent responsible for global context and decision-making

Graders:

- Code: `python3 scripts/validate_assets.py`

### capability-2

Goal: the skill defines a clear single-task delegation protocol for subagents.

Success Criteria:

- [ ] `SKILL.md` requires one clear task per delegation
- [ ] `SKILL.md` requires explicit context, non-goals, outputs, and verification for delegated work
- [ ] `SKILL.md` links to a reusable delegation template in `references/`

Graders:

- Code: `python3 scripts/validate_assets.py`

### capability-3

Goal: the skill constrains parallel work with independence checks and anti-duplication rules.

Success Criteria:

- [ ] `SKILL.md` requires an independence check before parallelization
- [ ] `SKILL.md` forbids the main agent from redoing delegated work without a stated reason
- [ ] `SKILL.md` constrains the main agent to non-overlapping work while waiting

Graders:

- Code: `python3 scripts/validate_assets.py`

### capability-4

Goal: the skill enforces result collection and verification gates before adopting delegated output.

Success Criteria:

- [ ] `SKILL.md` states that delegated summaries are not sufficient evidence
- [ ] `SKILL.md` requires reading code, diff, files, or tests before acceptance
- [ ] `SKILL.md` requires fresh verification evidence before completion claims

Graders:

- Code: `python3 scripts/validate_assets.py`

## Regression Evals

### regression-1

Goal: the skill remains tool-neutral and keeps platform bindings out of the core asset.

Success Criteria:

- [ ] `SKILL.md` does not hardcode Claude Code, Codex, or OpenCode subagent APIs as the default workflow
- [ ] `SKILL.md` explicitly pushes platform-specific tool names and APIs to `targets/`

Graders:

- Code: `python3 scripts/validate_assets.py`

### regression-2

Goal: the skill stays concise and moves detailed templates into references.

Success Criteria:

- [ ] detailed prompt and checklist content lives in `references/delegation-template.md`
- [ ] `SKILL.md` links to that reference file instead of embedding a long template inline
- [ ] `SKILL.md` defines a project-local durable output path

Graders:

- Code: `python3 scripts/validate_assets.py`

## Exit Criteria

- Capability evals: all pass in the current repository state
- Regression evals: all pass in the current repository state
- Report: validation command exits with status `0`
