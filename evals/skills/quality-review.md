# Asset Eval: quality-review

## Asset Under Test

- Type: skill
- Path: skills/quality-review/SKILL.md
- Goal: translate and absorb the superpowers request-review workflow into a Chinese, reusable quality skill.

## Capability Evals

### capability-1

Goal: the skill requests independent review at the right cadence.

Success Criteria:

- [ ] `SKILL.md` states that review should happen at major completion points or before merge
- [ ] `SKILL.md` prefers an independent reviewer or multiagent path when available
- [ ] `SKILL.md` describes how to act on Critical / Important / Minor style findings

Graders:

- Code: `python3 scripts/validate_assets.py`

### capability-2

Goal: the skill keeps the reusable reviewer prompt outside the main skill body.

Success Criteria:

- [ ] `SKILL.md` links to `references/reviewer-template.md`
- [ ] the reviewer template includes strengths, issues, and assessment style output
- [ ] `SKILL.md` defines a durable output strategy without requiring `nanospec`
- [ ] `SKILL.md` uses a project-local default output path such as `output/quality/quality-check.md`

Graders:

- Code: `python3 scripts/validate_assets.py`

## Regression Evals

### regression-1

Goal: the skill stays tool-neutral while allowing optional multiagent review.

Success Criteria:

- [ ] the skill body is primarily in Chinese
- [ ] `SKILL.md` does not require one specific harness API
- [ ] `SKILL.md` treats reviewer or multiagent execution as optional, not mandatory
- [ ] `SKILL.md` does not require `nanospec/<task>/...` as its output path

Graders:

- Code: `python3 scripts/validate_assets.py`

## Exit Criteria

- Capability evals: all pass in the current repository state
- Regression evals: all pass in the current repository state
- Report: validation command exits with status `0`
