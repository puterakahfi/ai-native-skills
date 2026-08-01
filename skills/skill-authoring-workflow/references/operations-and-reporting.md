# Skill Authoring Operations and Reporting

Load this reference after `skill-authoring-workflow` has verified the repository context and classified the request as `CREATE`, `UPDATE`, `RESTRUCTURE`, `MIGRATE`, or `DEPRECATE`.

## Pre-write gate receipt

Implementation may start only after the main workflow records all of these:

```yaml
pre_write_gate_receipt:
  skill_development_packet_ref: <complete artifact or task record>
  canonical_source_discovery_ref: <paths, findings, and missing-source verdicts>
  hermes_readiness_ref: <hierarchy, readiness, authority, and mutation decision>
  git_topology_ref: <base, working branch, PR target, workspace, live evidence>
  testing_plan_ref: <criterion-to-check mapping>
  first_mutation_authorized: true
```

The receipt must predate the first authored-file write. A skill-load log, assignment, `ready` status, or later reconstruction is not an equivalent receipt.

## Package shape

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
- create optional directories only when necessary;
- use a reviewed exemption rather than silently violating policy.

## Operation guidance

### CREATE

Create the smallest complete package and centralized behavioral contract.

### UPDATE

Preserve accepted behavior, change the smallest correct layer, bump executable version, and update regression evidence.

### RESTRUCTURE

Prove behavior preservation. Moving content without behavioral evidence is `NOT_VERIFIED`.

### MIGRATE

Record current compliance, target compliance, exemptions, warnings, and deferred debt. File presence alone does not prove compliance.

### DEPRECATE

Document replacement, migration path, catalog and dependency impact, compatibility expectations, and removal authority. Do not silently delete a depended-on capability.

## Validation sequence

```bash
skills-ref validate skills/<skill-name>
python scripts/validate-skill-packages.py
python scripts/validate-eval-contracts.py
AI_NATIVE_CORE_DIR=../ai-native-core bash scripts/run-eval.sh --skill <skill-name> --validate-tests
```

Also run, when applicable:

- tests for bundled executable resources;
- target behavioral evaluation when real per-case outputs exist;
- related-skill regression contracts affected by changed boundaries;
- adapter/core conformance;
- documentation, links, taxonomy, catalog, and skill-pack checks;
- original acceptance validation.
- profile, bundle, default-skill, and fleet distribution checks for base/shared capabilities.

Before writing, the testing plan must name the exact command, evidence surface, or explicit `NOT_APPLICABLE` rationale for every category above. Discovery of scripts/resources after writing reopens the gate until executable tests or a reviewed exemption are added. Discovery of base/fleet rollout scope reopens the gate until integration targets and profile-level checks are explicit.

Structural validation is not live behavioral proof. Missing live output is `NOT_RUN`, `INCOMPLETE`, or `NOT_VERIFIED`, never `PASS`.

## Required report

```yaml
skill_operation:
  operation: CREATE | UPDATE | RESTRUCTURE | MIGRATE | DEPRECATE
  target: <skill>
  skill_development_packet_ref: <artifact or task record>
  pre_write_gate_receipt_ref: <artifact or task record>
  package_status: COMPLIANT | PARTIAL | EXEMPT | ERROR | NOT_VERIFIED
  behavioral_status: APPLIED | PARTIAL | GHOST | INCOMPLETE | NOT_RUN
  executable_test_status: PASS | FAIL | NOT_APPLICABLE | NOT_VERIFIED
  conformance_status: PASS | FAIL | NOT_APPLICABLE | NOT_VERIFIED
  profile_rollout_status: PASS | FAIL | NOT_APPLICABLE | NOT_VERIFIED
  workflow_application_status: APPLIED | PARTIAL | GHOST | NOT_VERIFIED
  evidence: []
  known_gaps: []
  next_action: <one exact action>
```

Report package, behavioral, executable-test, conformance, profile/rollout, and workflow-application evidence independently. A loaded workflow with no pre-write artifacts is `GHOST` or `NOT_VERIFIED` even when the final package validates.