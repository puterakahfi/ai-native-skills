# Validation Review — Hermes Agent Fleet Bootstrap

Issue: `puterakahfi/ai-native-skills#264`  
Parent epic: `puterakahfi/ai-native-skills#260`  
PR: `puterakahfi/ai-native-skills#269`  
Date: 2026-07-29

## Scope

Validate the new `hermes-agent-fleet-bootstrap` package, centralized behavioral contract, capability discovery registration, published catalog, contract ownership, safety gates, and deterministic generated evidence before integration into the Epic branch.

## Authored and generated evidence

```yaml
validation_sources:
  skill: skills/hermes-agent-fleet-bootstrap/SKILL.md@0.1.0
  behavioral_contract: contracts/tests/hermes-agent-fleet-bootstrap.test.yaml
  contract_exemption: skills/hermes-agent-fleet-bootstrap/contract.exemption.yaml
  capability_inventory: docs/capability-inventory.json
  capability_classification: catalog/capability-discovery/classifications.json
  capability_topics: catalog/capability-discovery/topics.json
  published_catalog: catalog/published/capability-catalog.json
  contract_coverage: docs/contract-coverage-discovery.yaml
```

The capability is registered as an Hermes/provider-specific facade skill. The reviewed exemption prohibits claims of Core conformance, behavioral verification, runtime acceptance, product acceptance, or approval merely from static package presence.

## Behavioral contract coverage

Fifteen centralized cases cover:

1. complete one-bot engineering fleet;
2. narrow request returning `NOT_JUSTIFIED`;
3. product-facing profiles with a shared engineering fleet;
4. isolated privileged operations;
5. plan-only dry-run;
6. idempotent replay;
7. non-destructive profile migration;
8. framework-per-profile fragmentation rejection;
9. duplicate artifact ownership failure;
10. reviewer–implementer conflict limitation;
11. missing orchestrator failure;
12. circular handoff failure;
13. secret and live-state rejection;
14. missing capability resolution failure;
15. unnecessary specialist bot rejection.

## Verified generation run

```yaml
verified_generation:
  workflow: Generate Epic 260 Validation Artifacts
  run_id: 30468011361
  conclusion: success
  artifact_id: 8730392198
  artifact_name: epic-260-verified-artifacts
  artifact_digest: sha256:18f44fe1c400977be22f641ee32516a59cf5811d8ba62e880e0a5b1a8bb90ee3
  validations:
    capability_inventory: PASS
    capability_discovery: PASS
    published_catalog_build: PASS
    published_catalog_freshness: PASS
    catalog_regression_tests: PASS
    eval_contract_validation: PASS
    contract_coverage_generation: PASS
    contract_coverage_validation: PASS
```

The verified artifacts were committed to the PR head by the validation workflow. Temporary generation workflows were removed and the canonical metadata workflow was restored before this review was authored.

## Findings resolved from CI evidence

| Finding | Resolution |
|---|---|
| Published catalog drift | Capability was registered in canonical classification/topic sources and the published artifact rebuilt with an exact source revision. |
| Unowned executable | A reviewed `provider_specific` contract exemption was added because the MVP is Hermes-specific and no cross-runtime Core contract is justified. |
| Invalid eval entry | YAML boolean `false` was converted to the required string fixture. |
| Unreachable migration reference | `SKILL.md` now directly declares when to load the catalog/migration/idempotency reference. |
| Temporary workflow sources | Both Epic-local workflow files were removed after verified generation. |

## Validation boundary

Static validators and behavioral-contract syntax do not prove that a model follows every case in practice. They also do not prove Hermes profile creation, gateway behavior, Kanban dispatch, worker lifecycle, reviewer independence, filesystem isolation, or real profile migration.

Those direct runtime claims remain owned by issue #265.

## Verdict

```yaml
validation_review:
  package_structure: PASS
  package_metadata: PASS
  capability_inventory: PASS
  capability_discovery: PASS
  published_catalog: PASS
  eval_contract: PASS
  contract_coverage: PASS
  safety_and_negative_cases: PASS_AS_AUTHORED_CONTRACT
  model_behavior_execution: NOT_RUN
  real_hermes_runtime: NOT_RUN
  review_independence: LIMITED_SAME_EXECUTION_CONTEXT
  verdict: PASS_WITH_RUNTIME_FOLLOWUP
  merge_to_epic_branch: AUTHORIZED_BY_OWNER
  merge_to_main: NOT_AUTHORIZED
```

## Completion gate

This slice is eligible for merge into `260-hermes-agent-fleet-bootstrap` when the PR checks on this final clean head pass. Epic product acceptance and final merge remain blocked on #265 real Hermes execution evidence.
