---
name: skill-doctor
description: Audit, triage, repair, and verify existing skill packages. Use for unclear health problems, contradictions, stale content, package-policy violations, broken references, bloat, or missing maintenance evidence.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "skill-eval"
  ai-native-skills.type: workflow
  ai-native-skills.related_skills: '["skill-eval","skill-authoring-workflow","skill-evolution","context-engineering"]'
---

# Skill Doctor

Audit → Triage → Repair → Verify.

## Boundary

`skill-doctor` owns health diagnosis and repair of existing capability packages when the failure or required fix is not already an accepted intentional change.

It does not own:

- creating a new capability or accepted structural redesign (`skill-authoring-workflow`);
- promoting verified product learning (`skill-evolution`);
- scoring whether an agent applied a skill (`skill-eval`);
- protected-branch writes, review approval, or merge authority.

## Canonical sources

Load before assigning package compliance:

```text
contracts/skill-package-policy.yaml
docs/skill-package-standard.md
scripts/validate-skill-packages.py
```

Do not duplicate package rules inside this workflow.

## Health dimensions

Keep two verdict classes separate.

### Package compliance — blocking when policy says error

```text
required and prohibited paths
conditional tests for bundled scripts
central behavioral contract requirements
frontmatter and metadata validity
generated-artifact leakage
explicit exemptions
```

### Content health — advisory unless another contract makes it blocking

```text
clarity and cohesion
contradictions
stale examples or links
unreferenced resources
unnecessary duplication
progressive disclosure
readability and context cost
```

A line-count target such as `≤ 200` is advisory. It may identify review pressure, but it is not package invalidity by itself. Split only when content is separable and behavior can be preserved.

## Inputs

```yaml
skill_health_request:
  target: <skill or all>
  mode: audit-only | triage | repair
  issue: <verified issue or NOT_VERIFIED>
  accepted_behavior: <evidence or NOT_VERIFIED>
  write_authority: <verified | not verified>
```

## Phase 1 — Inspect

1. Read the complete target skill and every referenced resource needed to understand behavior.
2. Inspect related skills, central behavioral contracts, conformance declarations, docs, and recent changes.
3. Run package validation:

```bash
python scripts/validate-skill-packages.py --skill <skill-name>
```

4. Inspect content health without treating advisory style preferences as canonical validity rules.
5. When behavioral correctness is questioned, delegate scoring to `skill-eval` using real per-case outputs.

## Phase 2 — Classify findings

Use:

```text
PACKAGE_ERROR       blocking policy violation
PACKAGE_WARNING     migration or discouraged-path finding
CONTENT_ERROR       contradiction or broken executable guidance
CONTENT_WARNING     bloat, readability, duplication, stale example risk
BEHAVIOR_NOT_VERIFIED no real behavioral evidence
HEALTHY             no blocking finding and required evidence exists
```

Package status:

```text
COMPLIANT | PARTIAL | EXEMPT | ERROR | NOT_VERIFIED
```

Do not report `HEALTHY` when package status is `ERROR`, accepted behavior is unknown after a behavior-affecting repair, or required validation was not run.

## Phase 3 — Triage

Choose one primary action:

```text
NO_CHANGE    no actionable defect
TRIM         remove redundant or derivable content
SPLIT        move conditional depth into references
REPAIR       fix contradiction, stale path, broken resource, or policy violation
MIGRATE      hand intentional broad package migration to skill-authoring-workflow
DEFER        evidence, authority, or safe repair scope is missing
```

If the target change is already intentional and accepted rather than diagnostic, hand off to `skill-authoring-workflow`.

## Phase 4 — Repair

Rules:

- preserve accepted functional behavior;
- patch the smallest correct layer;
- never remove content merely to satisfy an advisory line target;
- link references from `SKILL.md` with explicit load conditions;
- remove or relocate generated state;
- add tests when bundled scripts require them;
- update centralized behavioral contracts when executable behavior changes;
- bump version for executable behavior changes;
- avoid unrelated cleanup;
- respect repository write and approval policy.

## Phase 5 — Verify

Run applicable checks:

```bash
skills-ref validate skills/<skill-name>
python scripts/validate-skill-packages.py --skill <skill-name>
python scripts/validate-eval-contracts.py
AI_NATIVE_CORE_DIR=../ai-native-core bash scripts/run-eval.sh --skill <skill-name> --validate-tests
```

Also verify:

- bundled executable tests;
- target and affected related-skill behavioral contracts;
- adapter/core conformance when applicable;
- links and referenced files;
- original accepted behavior after behavior-affecting repairs.

Structural checks do not prove behavioral application. Missing live outputs remain `NOT_VERIFIED` or `INCOMPLETE`.

## Required report

```yaml
skill_doctor_report:
  target: <skill>
  action: NO_CHANGE | TRIM | SPLIT | REPAIR | MIGRATE | DEFER
  package_status: COMPLIANT | PARTIAL | EXEMPT | ERROR | NOT_VERIFIED
  content_status: HEALTHY | WARNING | ERROR | NOT_VERIFIED
  behavioral_status: APPLIED | PARTIAL | GHOST | INCOMPLETE | NOT_RUN
  blocking_findings: []
  advisory_findings: []
  changes: []
  evidence: []
  known_gaps: []
  next_action: <one exact action>
```

## Hard gates

- Never claim `HEALTHY` while package validation has blocking errors.
- Never promote advisory style preferences into repository policy.
- Never repair unknown behavior without preservation evidence.
- Never treat package validation as behavioral proof.
- Never treat behavioral output scoring as package-compliance proof.
- Never modify files in audit-only mode.
- Never bypass repository write, review, or merge authority.
