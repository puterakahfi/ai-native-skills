# Release Unit Classification

Use this reference before issue creation, branch creation, or PR targeting.

## Decision factors

Classify from delivery behavior, not artifact size.

| Factor | Standalone / feature pressure | Epic / product-release pressure |
|---|---|---|
| Dependencies | no dependent slices | several ordered or coupled slices |
| Releasability | safe and useful alone | incomplete or unusable alone |
| Activation | no partial activation risk | partial merge may expose incomplete behavior |
| Acceptance | slice-level acceptance is sufficient | end-to-end combined acceptance required |
| Authorization | one bounded feature decision | one release decision governs many children |
| Rollback | independent rollback | coordinated rollback or integration state |

## Classification

### `standalone_change`

Use when the work is operationally independent, does not represent a user-facing capability by itself, and can be reviewed/released without a parent release decision.

Examples:

- inert documentation;
- a backward-compatible internal helper with no runtime activation;
- isolated CI correction.

### `feature`

Use when the work creates one independently releasable behavior with its own acceptance criteria and no required sibling slices.

### `epic`

Use when several children form one governed outcome and at least one child is not independently releasable.

Typical signals:

- new app surface;
- platform integration;
- multi-module workflow;
- migration requiring old/new coordination;
- product flow whose value appears only after frontend, backend, auth, and runtime pieces integrate.

### `product_release`

Use when multiple epics or major capabilities are governed by one launch/release decision, shared acceptance matrix, and coordinated deployment or support plan.

## Feature-flag exception

A flag may replace a long-lived epic branch only when all are evidenced:

```yaml
feature_flag_exception:
  policy_ref: <approved record>
  default_state: disabled
  incomplete_paths_covered: true
  bypass_paths: []
  disabled_state_verified: true
  rollback_or_kill_switch: <defined>
  owner: <attributable>
```

A config key or conditional statement is not proof of safe incremental release.

## Anti-patterns

- “Only three files, so it is a feature.”
- “CI is green, so direct-to-main is safe.”
- “The default branch is main, therefore PR target is main.”
- “We can call it a task and skip a parent epic.”
- “A feature flag exists somewhere.”
