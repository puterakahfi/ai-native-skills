# Implementation Review — Hermes Agent Fleet Bootstrap Skill

Issue: `puterakahfi/ai-native-skills#262`  
Parent epic: `puterakahfi/ai-native-skills#260`  
Date: 2026-07-29

## Scope

Reviewed the initial declarative package:

- `skills/hermes-agent-fleet-bootstrap/SKILL.md`
- `skills/hermes-agent-fleet-bootstrap/references/topology-and-classification.md`
- `skills/hermes-agent-fleet-bootstrap/references/profile-archetypes.md`
- `skills/hermes-agent-fleet-bootstrap/references/runtime-gateway-and-security.md`
- `skills/hermes-agent-fleet-bootstrap/assets/profile-contract.template.yaml`
- `skills/hermes-agent-fleet-bootstrap/assets/fleet-manifest.template.yaml`
- `skills/hermes-agent-fleet-bootstrap/assets/collaboration-manifest.template.yaml`

No bundled scripts, runtime mutations, dependencies, or profile credentials are added.

## Verdict

```yaml
implementation_review:
  verdict: PASS_WITH_REQUIRED_FOLLOWUP
  package_shape: PASS
  architecture_boundary: PASS
  single_profile_bootstrap_composition: PASS
  specialist_manifest_policy: PASS
  bot_and_gateway_policy: PASS
  security_and_authority_boundary: PASS
  catalog_integration: PENDING_263
  behavioral_contract: PENDING_264
  real_hermes_runtime: PENDING_265
  review_independence: LIMITED_SAME_EXECUTION_CONTEXT
  merge_to_epic_branch: AUTHORIZED_BY_OWNER
  merge_to_main: NOT_AUTHORIZED
```

## Findings

1. The skill remains a `skill` with facade/composer behavior and does not introduce a competing workflow or router.
2. Concrete profile materialization remains delegated to `hermes-profile-bootstrap` through one explicit handoff per profile.
3. The broad `engineering` preset is rejected as the default for every worker; specialist archetypes use responsibility-specific custom manifests.
4. The default runtime topology is one orchestrator bot with specialist profiles operating without dedicated bots.
5. Product-facing profiles may remain separate and use the shared engineering fleet.
6. Runtime, gateway, Kanban, dispatcher, worker, sandbox, and reviewer-independence claims are explicitly limited until direct evidence exists.
7. Machine-readable templates preserve artifact ownership, collaboration, permissions, authority, and readiness distinctions.

## Required follow-up

- #263 must integrate capability discovery, documentation, migration planning, dry-run, and idempotency semantics.
- #264 must add the canonical behavioral contract and deterministic positive/negative fixtures.
- #265 must run the package against an actual Hermes installation and record fail-closed runtime evidence.
- Final Epic acceptance must keep plan, execution, review, owner approval, merge authorization, deployment, and product acceptance separate.

## Completion assessment

This package is suitable for integration into the Epic branch as a dependent, non-releasable slice. It is not independently release-ready and must not be merged to `main` before #263–#265 provide the missing catalog, behavioral, and runtime evidence.
