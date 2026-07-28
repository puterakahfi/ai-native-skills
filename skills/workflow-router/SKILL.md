---
name: skill-authoring-workflow
description: Owns intentional creation, update, restructuring, migration, and deprecation of skills, workflows, and meta-skills. Use when changing a capability package by design, not when auditing health, evaluating behavior, or promoting a verified product lesson.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
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
- capability classification as `skill`, `workflow`, or `meta-skill`;
- package layout and resource placement;
- metadata and version decisions;
- centralized behavioral-contract creation or update;
- applicable executable-test obligations;
- package, behavioral, conformance, documentation, and delivery gates.

It does not own:

- health audit or repair of an unclear failure (`skill-doctor`);
- promotion of a verified product lesson (`skill-evolution`);
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

Do not copy those rules into a second local policy. The machine-readable policy is authoritative for repository package validation.

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

Missing target, scope, acceptance, repository, or authority must not be guessed.

## Phase 1 — Discover and classify

1. Verify repository, branch base, issue, scope, and acceptance criteria.
2. Inspect existing capability, related skills, contracts, tests, docs, and conventions.
3. Classify exactly one operation:

```text
CREATE       new reusable capability package
UPDATE       intentional executable behavior change
RESTRUCTURE  package organization changes while preserving behavior
MIGRATE      move a legacy package toward current policy
DEPRECATE    retire or replace a capability safely
NOT_VERIFIED insufficient decision evidence
```

4. Classify the capability type:

```text
skill       one reusable capability or expert lens
workflow    ordered phases, gates, ownership, and handoffs
meta-skill  routing or composition of other capabilities
```

If the request is an audit, uncertain repair, verified learning promotion, or behavior evaluation, hand off to its owner rather than forcing authoring.

## Phase 2 — Resolve package shape

Apply `contracts/skill-package-policy.yaml`:

```text
SKILL.md                   required
references/                optional runtime knowledge
scripts/                   optional reusable executable resources
tests/                     conditional when scripts are present
assets/                    optional templates/static resources
adapter.conformance.yaml   optional when implementing a core contract
contracts/tests/<name>.test.yaml
                           centralized behavioral regression contract
```

Rules:

- do not create skill-local `evals/` as a duplicate behavioral source;
- do not use skill-local `docs/` for runtime knowledge;
- place generated outputs outside authored packages;
- create optional directories only when they contain necessary resources;
- use an explicit exemption rather than silently violating policy.

## Phase 3 — Design executable behavior

Define:

- trigger-focused description;
- ownership and exclusions;
- required inputs and allowed outputs;
- ordered procedure or decision rules;
- evidence and quality gates;
- failure behavior and non-pass verdicts;
- resource loading conditions;
- dependencies and related skills;
- repository side effects and approval boundaries.

Keep `SKILL.md` lean. Move deep methodology into linked `references/` only when conditional loading provides value.

## Phase 4 — Implement the operation

### CREATE

Create the smallest complete package and centralized behavioral contract.

### UPDATE

Preserve accepted behavior, change the smallest correct layer, bump executable version, and update regression evidence.

### RESTRUCTURE

Prove behavior preservation. Moving content without behavioral evidence is `NOT_VERIFIED`.

### MIGRATE

Record current compliance, target compliance, exemptions, warnings, and deferred debt. Do not mark a package compliant from file presence alone.

### DEPRECATE

Document replacement, migration path, catalog and dependency impact, compatibility expectations, and removal authority. Do not delete a depended-on capability silently.

## Phase 5 — Validate

Run applicable gates in this order:

```bash
skills-ref validate skills/<skill-name>
python scripts/validate-skill-packages.py --skill <skill-name>
python scripts/validate-eval-contracts.py
AI_NATIVE_CORE_DIR=../ai-native-core bash scripts/run-eval.sh --skill <skill-name> --validate-tests
```

Also run:

- tests for bundled executable resources;
- target behavioral evaluation when real per-case outputs exist;
- related-skill regression contracts affected by changed boundaries;
- adapter/core conformance when applicable;
- documentation, links, taxonomy, catalog, and skill-pack checks;
- original acceptance validation.

Structural validation is not live behavioral proof. Missing live output is `NOT_RUN`, `INCOMPLETE`, or `NOT_VERIFIED`, never `PASS`.

## Phase 6 — Review and deliver

Require:

- self-review;
- independent architecture review;
- QA/eval review;
- documentation review;
- verified branch and PR target;
- green applicable CI;
- explicit remaining merge or approval authority.

Do not merge solely because CI is green when product or behavioral acceptance is still missing.

## Required report

```yaml
skill_operation:
  operation: CREATE | UPDATE | RESTRUCTURE | MIGRATE | DEPRECATE
  target: <skill>
  package_status: COMPLIANT | PARTIAL | EXEMPT | ERROR | NOT_VERIFIED
  behavioral_status: APPLIED | PARTIAL | GHOST | INCOMPLETE | NOT_RUN
  executable_test_status: PASS | FAIL | NOT_APPLICABLE | NOT_VERIFIED
  conformance_status: PASS | FAIL | NOT_APPLICABLE | NOT_VERIFIED
  evidence: []
  known_gaps: []
  next_action: <one exact action>
```

## Hard gates

Stop or return a non-pass verdict when:

- operation, target, scope, authority, or acceptance is unresolved;
- package policy has blocking errors;
- scripts exist without applicable tests or approved exemption;
- executable behavior changed without centralized regression coverage;
- behavior-preservation is claimed without evidence;
- conformance declarations contradict the implemented boundary;
- generated state is committed into the authored package;
- approval or merge authority is missing.
