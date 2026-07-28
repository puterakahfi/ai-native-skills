---
name: skill-authoring-workflow
description: Owns intentional creation, update, restructuring, migration, and deprecation of skills, workflows, and meta-skills. Use when changing a capability package by design, not when auditing health, evaluating behavior, or promoting a verified product lesson.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: workflow
  ai-native-skills.requires: "implementation-context-discovery skill-doctor skill-eval git-workflow decision-provenance"
  ai-native-skills.related_skills: '["workflow-router","skill-doctor","skill-evolution","skill-eval","implementation-context-discovery","git-workflow","decision-provenance"]'
---

# Skill Authoring Workflow

Create and intentionally manage reusable capability packages through one policy-backed lifecycle.

## Boundary

This workflow owns:

- `CREATE`, `UPDATE`, `RESTRUCTURE`, `MIGRATE`, and `DEPRECATE` operations;
- capability type, package shape, metadata, and version decisions;
- centralized behavioral-contract changes;
- applicable executable-test obligations;
- package, behavioral, conformance, documentation, and delivery gates.

It does not own:

- uncertain health audit or repair (`skill-doctor`);
- promotion of verified product learning (`skill-evolution`);
- behavioral application scoring (`skill-eval`);
- universal contract changes without core authority;
- protected-branch writes or merge approval.

## Canonical sources

Before changing a package, load:

```text
contracts/skill-package-policy.yaml
docs/skill-package-standard.md
docs/skill-authoring-template.md
CONTRIBUTING.md
```

Do not duplicate these rules locally. The machine-readable package policy is authoritative for repository validation.

## Inputs

```yaml
skill_operation:
  request: <user or issue request>
  target: <skill name or proposed name>
  operation: CREATE | UPDATE | RESTRUCTURE | MIGRATE | DEPRECATE | NOT_VERIFIED
  issue: <verified issue or NOT_VERIFIED>
  repository: <verified repository>
  branch_base: <verified base>
  acceptance_criteria: []
  write_authority: <verified | not verified>
```

Do not guess missing target, scope, acceptance, repository, branch base, or authority.

## Phase 1 — Discover and classify

1. Verify repository, branch base, issue, scope, and testable acceptance criteria.
2. Inspect the existing capability, related skills, contracts, tests, docs, and conventions.
3. Classify exactly one operation:

```text
CREATE       new reusable capability package
UPDATE       intentional executable behavior change
RESTRUCTURE  package organization change while preserving behavior
MIGRATE      move a legacy package toward current policy
DEPRECATE    retire or replace a capability safely
NOT_VERIFIED insufficient decision evidence
```

4. Classify the capability as `skill`, `workflow`, or `meta-skill`.
5. Hand audit, uncertain repair, verified-learning promotion, and behavioral evaluation to their primary owners.

## Phase 2 — Shape and design

Apply `contracts/skill-package-policy.yaml` and define:

- trigger-focused description;
- ownership and exclusions;
- required inputs and allowed outputs;
- ordered procedure or decision rules;
- evidence, quality gates, and failure verdicts;
- conditional resource-loading rules;
- dependencies and related capabilities;
- side effects and approval boundaries.

Keep `SKILL.md` as the executable entry point. Load [operations-and-reporting.md](references/operations-and-reporting.md) only after the operation is classified and implementation or reporting detail is needed.

## Phase 3 — Implement

Use the operation-specific obligations in [operations-and-reporting.md](references/operations-and-reporting.md). Preserve accepted behavior, change the smallest correct layer, and update centralized regression evidence whenever executable behavior changes.

For `RESTRUCTURE`, behavior preservation must be demonstrated; structure alone is not proof. For `MIGRATE`, file presence alone is not compliance. For `DEPRECATE`, verify replacement, migration, dependency, compatibility, and removal authority.

## Phase 4 — Validate

Run the canonical validation sequence and applicable related gates from [operations-and-reporting.md](references/operations-and-reporting.md).

Report independently:

- package compliance;
- behavioral-evaluation status;
- executable-test status;
- core or adapter conformance;
- documentation and discovery status;
- acceptance and approval status.

Structural validation is not live behavioral proof. Missing live output remains `NOT_RUN`, `INCOMPLETE`, or `NOT_VERIFIED`.

## Phase 5 — Review and deliver

Require:

- self-review;
- independent architecture review;
- QA/eval review;
- documentation review;
- verified branch and PR target;
- green applicable CI;
- explicit merge and approval authority.

Do not merge solely because CI is green when required behavioral or product acceptance is missing.

## Hard gates

Stop or return a non-pass verdict when:

- operation, target, scope, authority, or acceptance is unresolved;
- package policy has blocking errors;
- scripts exist without applicable tests or approved exemption;
- executable behavior changed without centralized regression coverage;
- behavior preservation is claimed without evidence;
- conformance declarations contradict the implemented boundary;
- generated state is committed into the authored package;
- approval or merge authority is missing.