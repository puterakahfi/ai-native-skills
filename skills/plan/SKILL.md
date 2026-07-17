---
name: plan
description: 'Plan mode: write an actionable markdown plan with exact file paths and bite-sized steps before any execution starts.'
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/software-engineering/plan.contract.yaml
---

# Plan Mode

Use this skill when the user wants a plan instead of execution.

---

## ⛔ HARD RULES

- **Save plan to `.hermes/plans/<name>.md` — never output only to chat**
- **Each task must be independently verifiable**
- **Task granularity: 1 task = 1 atomic change, not a feature**

---

## Core behavior

For this turn, you are planning only.

- Do not implement code.
- Do not edit project files except the plan markdown file.
- Do not run mutating terminal commands, commit, push, or perform external actions.
- You may inspect the repo or other context with read-only commands/tools when needed.
- Your deliverable is a markdown plan saved inside the active workspace under `.hermes/plans/`.

## Output requirements

Write a markdown plan that is concrete and actionable.

Include, when relevant:
- Goal
- Current context / assumptions
- Proposed approach
- Step-by-step plan
- Files likely to change
- Tests / validation
- Risks, tradeoffs, and open questions

If the task is code-related, include exact file paths, likely test targets, and verification steps.

## Save location

Save the plan with `write_file` under:
- `.hermes/plans/YYYY-MM-DD_HHMMSS-<slug>.md`

Treat that as relative to the active working directory / backend workspace. Hermes file tools are backend-aware, so using this relative path keeps the plan with the workspace on local, docker, ssh, modal, and daytona backends.

If the runtime provides a specific target path, use that exact path.
If not, create a sensible timestamped filename yourself under `.hermes/plans/`.

## Interaction style

- If the request is clear enough, write the plan directly.
- If no explicit instruction accompanies `/plan`, infer the task from the current conversation context.
- If it is genuinely underspecified, ask a brief clarifying question instead of guessing.
- After saving the plan, reply briefly with what you planned and the saved path.

---

## Reference material

For detailed guidance on plan content, see:

- [`references/granularity-structure.md`](references/granularity-structure.md) — Overview, when full plans help, task granularity, plan document structure, and task format
- [`references/writing-process.md`](references/writing-process.md) — Step-by-step writing process, principles (DRY/YAGNI/TDD), common mistakes, and execution handoff

---

## Execution Handoff

After saving the plan, offer the execution approach:

**"Plan complete and saved. Ready to execute using subagent-driven-development — I'll dispatch a fresh subagent per task with two-stage review (spec compliance then code quality). Shall I proceed?"**

When executing, use the `subagent-driven-development` skill:
- Fresh `delegate_task` per task with full context
- Spec compliance review after each task
- Code quality review after spec passes
- Proceed only when both reviews approve

---

## ⛔ HARD RULES (reminder)

- **Save plan to `.hermes/plans/<name>.md` — never output only to chat**
- **Each task must be independently verifiable**
- **Task granularity: 1 task = 1 atomic change, not a feature**
