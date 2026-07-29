# Integration Review — Hermes Agent Fleet Bootstrap

Issue: `puterakahfi/ai-native-skills#263`  
Parent epic: `puterakahfi/ai-native-skills#260`  
Date: 2026-07-29

## Integrated behavior

- Capability selection is explicitly sourced from the capability inventory, discovery classifications, job profiles, executable skill metadata, and active product/repository constraints.
- Hermes archetypes remain local profile templates and do not become a hidden second catalog.
- Every approved profile receives one `hermes-profile-bootstrap` handoff.
- Existing profiles are audited before migration recommendations.
- Migration is recommendation-only and preserves live sessions, memories, cron state, runtime databases, credentials, tokens, and gateway state.
- Dry-run lists intended profiles, files, skills, policies, gateways, permissions, runtime commands, and migration actions without writes.
- Idempotency compares normalized requested and observed state and rejects duplicate profile creation or unnecessary rewrites.
- Missing runtime commands produce a concrete handoff and `NOT_RUN`/`BLOCKED`, never a false execution claim.

## Added artifacts

- `references/catalog-migration-and-idempotency.md`
- `assets/capability-resolution.template.yaml`
- `assets/migration-plan.template.yaml`
- `assets/dry-run-plan.template.yaml`

## Review verdict

```yaml
integration_review:
  verdict: PASS_WITH_REQUIRED_FOLLOWUP
  capability_authority: PASS
  per_profile_bootstrap_composition: PASS
  dry_run_contract: PASS
  idempotency_contract: PASS
  non_destructive_migration: PASS
  secret_and_live_state_exclusion: PASS
  runtime_unavailable_handoff: PASS
  generated_inventory_and_discovery_sync: PENDING_264
  real_profile_audit: PENDING_265
  real_runtime_execution: PENDING_265
  review_independence: LIMITED_SAME_EXECUTION_CONTEXT
  merge_to_epic_branch: AUTHORIZED_BY_OWNER
  merge_to_main: NOT_AUTHORIZED
```

## Required follow-up

1. #264 must add canonical behavioral fixtures and synchronize generated capability inventory/discovery artifacts for the new executable skill.
2. #264 must validate that every referenced capability ID resolves and that broad presets are rejected for specialist workers.
3. #265 must inspect real existing Hermes profiles before assigning migration decisions.
4. #265 must prove dry-run and repeated-run behavior against the actual Hermes installation.

## Acceptance boundary

This slice is suitable for integration into the Epic branch. It does not prove that any profile was created, changed, or migrated and does not authorize destructive changes, final merge, release, deployment, or product acceptance.
