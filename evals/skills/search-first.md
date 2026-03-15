# Asset Eval: search-first

## Asset Under Test

- Type: skill
- Path: src/skills/search-first/SKILL.md
- Goal: provide a research-before-coding workflow that searches the codebase, tests, and external references before writing net-new implementation.

## Capability Evals

### capability-1

Goal: the skill requires searching existing code and tests before writing implementation.

Success Criteria:

- [ ] `SKILL.md` explicitly checks the local codebase first
- [ ] `SKILL.md` explicitly checks tests or existing usage patterns
- [ ] `SKILL.md` positions search before implementation

Graders:

- Code: `python3 scripts/validate_assets.py`

### capability-2

Goal: the skill requires searching external references when the problem likely already has known solutions.

Success Criteria:

- [ ] `SKILL.md` explicitly checks package ecosystems, docs, or `references/repos/`
- [ ] `SKILL.md` requires comparing candidate options instead of blindly coding
- [ ] `SKILL.md` includes a clear decision model such as `adopt` / `adapt` / `build`

Graders:

- Code: `python3 scripts/validate_assets.py`

### capability-3

Goal: the skill produces a durable research output that can guide implementation.

Success Criteria:

- [ ] `SKILL.md` defines a reusable output such as `research-note.md`
- [ ] `SKILL.md` requires recording evidence paths or source names
- [ ] `SKILL.md` requires a next-step recommendation for implementation
- [ ] `SKILL.md` uses a project-local default output path such as `output/research/research-note.md`

Graders:

- Code: `python3 scripts/validate_assets.py`

## Regression Evals

### regression-1

Goal: the skill remains focused on coding tasks rather than repository governance.

Success Criteria:

- [ ] the skill body is primarily in Chinese
- [ ] `SKILL.md` is clearly about coding features, bugs, integrations, or abstractions
- [ ] `SKILL.md` does not frame itself as a skill for maintaining this repository's prompt assets

Graders:

- Code: `python3 scripts/validate_assets.py`

### regression-2

Goal: the skill stays concise and moves detailed templates into references.

Success Criteria:

- [ ] detailed search checklist lives in `references/`
- [ ] `SKILL.md` links to that reference file instead of embedding a long template

Graders:

- Code: `python3 scripts/validate_assets.py`

## Exit Criteria

- Capability evals: all pass in the current repository state
- Regression evals: all pass in the current repository state
- Report: validation command exits with status `0`
