---
name: new-feature-workflow
description: Guided new feature workflow — plan, design, implement, verify, submit, review. Spec must exist before implementation. Branch strategy, issue tracker, and approval policy are product-defined.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "master-engineer master-design spec-workflow test-driven-development"
  ai-native-skills.type: workflow
  ai-native-skills.implements: ai-native-core/contracts/workflows/new-feature.contract.yaml
  ai-native-skills.skill_load_order: '[{''phase'': ''plan'', ''load'': [''master-engineer'']}, {''phase'': ''design'', ''load'': [''master-engineer'', ''diagram-architect'', ''master-design'', ''design-review'']}, {''phase'': ''implement'', ''load'': [''master-engineer'']}, {''phase'': ''review'', ''load'': [''architecture-review'', ''design-review'']}]'
  ai-native-skills.skills: '{''required'': [''master-engineer'', ''architecture-review''], ''optional'': [''diagram-architect'', ''master-design'', ''design-review'']}'
---

# New Feature Workflow

## Overview

A structured new feature workflow that enforces the right sequence and gates. The core rule: **spec must exist before implementation**. What varies per team (branch strategy, spec format, issue tracker, approval) is declared by the product adapter.

## Required Skills

Load these skills before executing the workflow:

| Phase | Load Skill |
|---|---|
| Phase 1: Plan | `master-engineer` |
| Phase 2: Design | `master-engineer` + `diagram-architect` (if system design) + `master-design` (if UI) + `design-review` (if UI review) |
| Phase 3: Implement | `master-engineer` |
| Phase 6: Review | `architecture-review` + `design-review` (if UI involved) |

> Agent instruction: when entering each phase, load the listed skills and follow their process before proceeding.

## Required Skill

Load `master-engineer` before executing Phase 3.

## Optional Skills

- `diagram-architect` — for Phase 2 when system design is needed
- `master-design` — for Phase 2 when UI/UX design is needed

## Phases

---

### Phase 1: Plan
**Gate:** Spec must exist before implementation.

Define before touching any code:

1. **What** — feature description, user problem being solved
2. **Scope** — what's in, what's explicitly out
3. **Acceptance criteria** — how do we know it's done?
4. **Technical approach** — high-level approach, affected components
5. **Issue tracker item** — linked ticket/issue

Spec format is product-defined. Minimum required:

```yaml
feature_spec:
  title: ""
  problem: ""
  scope_in: []
  scope_out: []
  acceptance_criteria: []
  technical_approach: ""
  issue_ref: ""
```

**Done when:** Spec written, acceptance criteria explicit, issue tracker item exists.

---

### Phase 2: Design *(product-defined: required or optional)*
**Gate:** Design reviewed before implementation.

Required when the feature involves:
- New system boundaries or contracts
- UI/UX changes
- Data model changes
- New integrations

Use `diagram-architect` for system/contract diagrams.
Use `master-design` for UI/UX wireframes and interaction contracts.

**Done when:** Design artifacts exist and reviewed by relevant stakeholder.

---

### Phase 3: Implement
**Gate:** Implementation must trace to spec. No scope creep.

Load and follow `master-engineer` skill.

1. Implement following the agreed spec and design
2. Write tests as you go — unit, integration, as appropriate
3. Each commit traces to a spec item
4. Raise a flag immediately if spec needs to change — don't silently expand scope

**Done when:** All acceptance criteria implemented, tests written, no unrelated changes bundled.

---

### Phase 4: Verify
**Gate:** Verification evidence required before submission.

Run the full test suite — method is product-defined (local, CI, or both).

```bash
# Example: local
pytest tests/ -q

# Example: trigger CI
git push origin <branch>
```

Capture evidence: test output, CI link, or screenshot.

**Done when:** Full suite green, evidence captured.

---

### Phase 5: Submit
**Gate:** Submission must reference spec and issue tracker item.

Submit code for review — mechanism is product-defined (PR, MR, patch).

Checklist:
- [ ] References issue tracker item
- [ ] References spec (link or summary)
- [ ] Description includes: what, why, how
- [ ] Acceptance criteria checklist in submission
- [ ] Verification evidence attached
- [ ] No unrelated changes bundled

**Done when:** Submission open, spec and issue referenced.

---

### Phase 6: Review
**Gate:** Approval required before merge.

- [ ] Peer review completed
- [ ] Feedback addressed
- [ ] Acceptance criteria verified by reviewer
- [ ] Approved by required reviewers
- [ ] Merged

---

## Quick Reference

| Phase | Gate | Done When |
|---|---|---|
| **1. Plan** | Spec exists | Acceptance criteria explicit |
| **2. Design** | Design reviewed | Artifacts exist and reviewed |
| **3. Implement** | Traces to spec | Acceptance criteria implemented |
| **4. Verify** | Full suite green | Evidence captured |
| **5. Submit** | Spec + issue referenced | Submission open |
| **6. Review** | Approved | Merged |

## Common Pitfalls

1. **Skipping Phase 1** — implementing without spec leads to scope creep and rework
2. **Vague acceptance criteria** — "works correctly" is not a criterion
3. **Silent scope creep** — adding more than specced without updating spec
4. **Bundling unrelated changes** — makes review hard, breaks bisect
5. **Skipping design for UI/system changes** — implementation without design contract leads to misalignment
