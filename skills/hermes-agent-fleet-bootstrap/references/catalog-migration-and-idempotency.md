# Catalog Resolution, Migration, and Idempotency

Load this reference when resolving skills for profile contracts, auditing existing profiles, producing a dry-run, or comparing a requested fleet against an existing fleet.

## Capability authority

Use the repository's verified sources in this order:

```text
active issue and accepted scope
→ product/repository constraints
→ capability inventory
→ capability discovery classifications
→ curated job profiles
→ executable skill metadata and dependencies
→ Hermes-specific archetype guidance
```

Hermes archetypes are local profile templates. They do not replace the capability catalog, job profiles, workflow routing, or repository-specific implementation context.

Record capability resolution:

```yaml
capability_resolution:
  requested_responsibility: ""
  candidate_capability_ids: []
  selected_required: []
  selected_optional: []
  rejected: []
  catalog_source: ""
  catalog_version_or_revision: ""
  unresolved: []
  rationale: []
```

A missing capability remains unresolved. Do not invent a skill ID or silently substitute a nearby capability.

## Responsibility-specific composition

Start from the stable responsibility and select the smallest verified capability set.

```text
profile responsibility
→ required outputs and gates
→ applicable workflow or specialist methods
→ required capabilities
→ optional capabilities
→ exclusions
```

Do not start from the broad `engineering` or `full` preset and remove a few items. That approach easily recreates overlapping generalists.

Common foundations are not automatically required everywhere:

- `workflow-router` belongs primarily on profiles receiving ambiguous multi-lifecycle requests.
- `role-switcher` belongs on profiles that compose task-time owners, specialists, or reviewers.
- `git-workflow` belongs only where repository delivery operations are owned and authorized.
- review capabilities belong on reviewers and implementers only when self-review is explicitly limited and independent review remains separate.
- product workflows do not belong on narrow implementation workers by default.

## Per-profile bootstrap composition

Produce exactly one handoff per approved profile:

```yaml
profile_bootstrap_handoff:
  profile_contract_ref: ""
  capability: hermes-profile-bootstrap
  runtime_target: hermes
  profile_name: ""
  preset: custom
  skill_catalog_source: ""
  skills_required: []
  skills_optional: []
  model_policy: {}
  toolset_policy: {}
  verification_policy: {}
  safety_constraints: []
  product_context_reference: ""
  intended_action: CREATE | AUDIT | UPDATE | NO_CHANGE
  execution_status: PLANNED | EXECUTED | BLOCKED | NOT_VERIFIED
  evidence: []
```

The fleet skill coordinates these handoffs. It does not duplicate profile directory generation, skill installation, safe-default writing, or profile doctor behavior.

## Existing-profile audit

Inspect when available:

- profile identifier and description;
- SOUL and stable responsibility;
- installed skills and lock manifest;
- model and tool policies;
- gateway/channel and audience;
- permission and repository scope;
- memory responsibility;
- cron or ongoing operational responsibilities;
- product-specific coupling;
- live-state paths that must not be copied;
- recent workload evidence.

Missing evidence remains `NOT_VERIFIED`.

Audit record:

```yaml
existing_profile_audit:
  profile_id: ""
  observed_sources: []
  responsibility: ""
  installed_skills: []
  gateway: {}
  permissions: {}
  memory_scope: {}
  product_coupling: []
  live_state_present: NOT_INSPECTED | YES | NO
  findings: []
  confidence: HIGH | MEDIUM | LOW | NOT_VERIFIED
```

## Migration classification

Choose one:

```text
KEEP
KEEP_AS_PRODUCT_AGENT
CONVERT_TO_SPECIALIST
MERGE
SPLIT
REGENERATE
DEPRECATE
NOT_VERIFIED
```

Decision rules:

- `KEEP`: responsibility and configuration already match the approved contract.
- `KEEP_AS_PRODUCT_AGENT`: the profile has a valid direct audience, personality, product memory, gateway, or product-facing responsibility; engineering work moves to the shared fleet.
- `CONVERT_TO_SPECIALIST`: durable identity is useful but responsibility and skills should be narrowed.
- `MERGE`: multiple profiles have materially duplicate responsibility and no required isolation.
- `SPLIT`: one profile has conflicting durable responsibilities, permissions, or audiences that require separate profiles.
- `REGENERATE`: reusable skeleton is stale or inconsistent, while live state must be preserved separately.
- `DEPRECATE`: no valid recurring responsibility remains and owner authorizes retirement.
- `NOT_VERIFIED`: evidence or authority is insufficient.

MVP migration produces recommendations only. No profile deletion, state movement, credential copying, or token replacement is automatic.

## Dry-run contract

A dry-run must list every intended action:

```yaml
dry_run:
  fleet_id: ""
  input_revision: ""
  catalog_revision: ""
  existing_state_revision: ""
  profiles:
    create: []
    audit: []
    update: []
    keep: []
    deprecate_recommendations: []
  files:
    create: []
    update: []
    preserve: []
    prohibited: []
  skills:
    install: []
    remove_recommendations: []
    unresolved: []
  gateways:
    create_or_configure: []
    preserve: []
    dedicated_exceptions: []
  permissions:
    changes: []
    manual_approval_required: []
  migration_actions: []
  runtime_commands: []
  blockers: []
  warnings: []
```

A dry-run has no mutation evidence and must report runtime execution as `NOT_RUN`.

## Idempotency comparison

Normalize and compare:

- profile IDs;
- profile contract versions;
- required and optional skill sets;
- source catalog revision;
- model, tool, permission, memory, and gateway policies;
- collaboration edges;
- artifact ownership;
- migration decisions;
- safe distribution file hashes when observable.

Return:

```yaml
idempotency_comparison:
  requested_revision: ""
  observed_revision: ""
  equivalent: true | false | NOT_VERIFIED
  no_change_profiles: []
  create_profiles: []
  update_profiles: []
  removed_or_deprecated_recommendations: []
  policy_drift: []
  skill_drift: []
  gateway_drift: []
  collaboration_drift: []
  prohibited_state_differences: []
  blockers: []
```

Re-running an equivalent request must not create duplicate profiles or rewrite stable files unnecessarily.

## Safe update behavior

- Plan before write.
- Refuse overwrite when an existing profile cannot be audited.
- Preserve live state and local secrets.
- Update reusable skeleton files only through `hermes-profile-bootstrap` behavior.
- Record exact before/after references.
- Separate requested state, observed state, and executed mutation.
- Keep destructive changes as recommendations requiring explicit owner authorization.

## Runtime-unavailable behavior

When Hermes CLI, profile paths, gateway, Kanban, or dispatcher are unavailable:

```text
produce complete plan and handoff
→ report runtime execution NOT_RUN or BLOCKED
→ list exact commands or evidence needed
→ never claim profiles, bots, workers, or boards were created
```
