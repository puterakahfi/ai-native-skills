---
name: skill-authoring-workflow
description: Canonical Skill Development Workflow for intentional creation, update, restructuring, migration, and deprecation of skills, workflows, and meta-skills. Use before changing a capability package by design; do not use it for health audits, behavioral scoring, or verified-learning promotion.
license: MIT
metadata:
  ai-native-skills.version: 1.2.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: workflow
  ai-native-skills.requires: "hermes-task-management-workflow implementation-context-discovery skill-doctor skill-eval git-workflow decision-provenance"
  ai-native-skills.related_skills: '["hermes-task-management-workflow","workflow-router","skill-doctor","skill-evolution","skill-eval","implementation-context-discovery","git-workflow","decision-provenance"]'
---

# Canonical Skill Development Workflow

Also known as `skill-authoring-workflow`, this is the canonical Skill Development Workflow for creating and intentionally managing reusable capability packages through one policy-backed lifecycle.

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

Before changing a package, discover and load:

```text
contracts/skill-package-policy.yaml
docs/skill-package-standard.md
docs/skill-authoring-template.md
CONTRIBUTING.md
scripts/validate-skill-packages.py
scripts/validate-eval-contracts.py
<target package and every conditionally relevant resource>
<related skills, contracts, behavioral tests, executable tests, and docs>
<core policy or contract when universal authority may exist>
<catalog, pack, profile, bundle, or rollout manifests when integration may change>
```

Record exact paths and missing sources in the requirements packet. Do not substitute a remembered convention for repository evidence or duplicate these rules locally. The machine-readable package policy is authoritative for repository validation.

## Required skill development packet

```yaml
skill_development_packet:
  request: <user or issue request>
  goal: <observable capability outcome>
  target_name: <skill name or proposed name>
  operation: CREATE | UPDATE | RESTRUCTURE | MIGRATE | DEPRECATE | NOT_VERIFIED
  capability_type: skill | workflow | meta-skill | NOT_VERIFIED
  issue: <verified issue or NOT_VERIFIED>
  repository: <verified repository>
  write_authority: <verified | not verified>
  scope_in: []
  scope_out: []
  related_skills: []
  references: []
  canonical_source_refs: []
  expected_behaviors: []
  anti_behaviors: []
  acceptance_criteria: []
  rollout_integration_targets: []
  repository_work_gate:
    readiness_ref: <hermes-task-management-workflow receipt>
    base_branch: <explicit verified base>
    working_branch: <explicit non-protected branch>
    pr_target: <explicit verified target>
    workspace_kind: worktree | branch | NOT_VERIFIED
    git_workflow_evidence_refs: []
    mutation_allowed: false
  testing_plan:
    package_validation: []
    centralized_behavioral_contract: []
    eval_cases: []
    executable_tests: []
    related_regressions: []
    conformance: []
    documentation_and_discovery: []
    profile_and_rollout_verification: []
  packet_status: COMPLETE | INCOMPLETE | NOT_VERIFIED
```

Every field must contain attributable evidence, an explicit `NOT_APPLICABLE` with rationale, or a non-pass status. Do not guess missing target, scope, behavior, acceptance, repository topology, tests, rollout, or authority. Writing is forbidden until `packet_status: COMPLETE` and `repository_work_gate.mutation_allowed: true`.

## Phase 0 — Prove readiness before mutation

1. Apply `hermes-task-management-workflow`; assignment, a `ready` column, or a worker claim is not execution permission.
2. Verify its hierarchy, readiness, authority, acceptance, and repository-work gates. Missing gates yield `BLOCKED` or `NOT_VERIFIED` with `mutation_allowed: false`.
3. Apply `git-workflow` and record live base branch, working branch, PR target, worktree or branch path, and protected-branch evidence before editing any skill package.
4. Use a clean isolated worktree or approved non-protected branch. Do not mutate a default checkout, protected branch, dirty shared workspace, or topology inferred from repository defaults.
5. Complete and record the skill development packet and testing plan before the first authored-file write.

Loading these workflows is not evidence that their gates were applied. An application receipt must identify the resolved packet, source-discovery record, readiness decision, git topology evidence, planned checks, and the first mutation occurring after those artifacts.

## Phase 1 — Discover and classify

1. Verify the complete skill development packet, repository-work gate, and testable acceptance criteria.
2. Inspect the canonical sources, existing capability, related skills, contracts, behavioral and executable tests, docs, integration manifests, and conventions.
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

Before implementation, map each expected behavior, anti-behavior, and acceptance criterion to at least one planned evidence source. The testing plan must include package validation, the centralized behavioral contract and cases, applicable executable-resource tests, affected related regressions, conformance, documentation/discovery, and profile or rollout checks for base/fleet capabilities.

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
- profile, bundle, base-skill, and fleet rollout status when applicable;
- acceptance and approval status.

Structural validation is not live behavioral proof. Missing live output remains `NOT_RUN`, `INCOMPLETE`, or `NOT_VERIFIED`.

For bundled scripts or executable resources, absent applicable tests or an approved exemption is a failure. For base, fleet, shared-profile, bundled, or default-loaded capabilities, missing rollout targets or profile-level verification is a failure; repository package validation cannot substitute for runtime distribution evidence.

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

## Workflow application evidence

Before delivery, report:

```yaml
workflow_application_evidence:
  workflow_loaded: true | false
  packet_ref: <artifact or task record>
  canonical_source_refs: []
  readiness_and_repository_gate_ref: <artifact or task record>
  git_topology_evidence_refs: []
  testing_plan_ref: <artifact or task record>
  first_mutation_after_gates_ref: <diff, event, or commit evidence>
  validation_evidence_refs: []
  rollout_evidence_refs: []
  application_status: APPLIED | PARTIAL | GHOST | NOT_VERIFIED
```

`workflow_loaded: true` without phase artifacts is `GHOST` or `NOT_VERIFIED`, never `APPLIED`. Package existence, a clean diff, or green structural validation cannot prove the workflow was followed in sequence.

## Hard gates

Stop or return a non-pass verdict when:

- the complete skill development packet was not recorded before writing;
- `hermes-task-management-workflow` readiness or repository mutation permission is missing;
- `git-workflow` branch/worktree topology evidence is missing or postdates the first edit;
- operation, target, scope, behavior, authority, acceptance, rollout, or testing plan is unresolved;
- package policy has blocking errors;
- scripts or executable resources exist without planned and executed applicable tests or an approved exemption;
- executable behavior changed without centralized regression coverage;
- a base/fleet capability lacks rollout targets or profile-level verification;
- the workflow was loaded but application artifacts are missing;
- behavior preservation is claimed without evidence;
- conformance declarations contradict the implemented boundary;
- generated state is committed into the authored package;
- approval or merge authority is missing.