# Asset Eval: quality-tdd

## Asset Under Test

- Type: skill
- Path: skills/quality-tdd/SKILL.md
- Goal: translate and absorb the core superpowers TDD discipline into a Chinese, reusable quality skill.

## Capability Evals

### capability-1

Goal: the skill enforces test-first discipline rather than treating tests as post-hoc verification.

Success Criteria:

- [ ] `SKILL.md` states that no implementation code should be written before a failing test
- [ ] `SKILL.md` states that seeing the test fail is mandatory
- [ ] `SKILL.md` describes a red-green-refactor style loop

Graders:

- Code: `python3 scripts/validate_assets.py`

### capability-2

Goal: the skill keeps the translated anti-rationalization guidance from superpowers.

Success Criteria:

- [ ] `SKILL.md` warns against “先写实现再补测试”
- [ ] `SKILL.md` treats “这次先跳过” as rationalization rather than pragmatism
- [ ] `SKILL.md` links to `references/testing-anti-patterns.md`

Graders:

- Code: `python3 scripts/validate_assets.py`

## Regression Evals

### regression-1

Goal: the skill stays tool-neutral and reusable inside this repository.

Success Criteria:

- [ ] the skill body is primarily in Chinese
- [ ] `SKILL.md` does not bind itself to a single test framework
- [ ] `SKILL.md` defines a durable output strategy without requiring `nanospec`
- [ ] `SKILL.md` uses a project-local default output path such as `output/quality/quality-check.md`

Graders:

- Code: `python3 scripts/validate_assets.py`

## Exit Criteria

- Capability evals: all pass in the current repository state
- Regression evals: all pass in the current repository state
- Report: validation command exits with status `0`
