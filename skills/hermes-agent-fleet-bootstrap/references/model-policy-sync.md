# Hermes fleet model-policy synchronization

Use this executor only after the `native-ai-engineering` fleet has the complete generation-2 target identities:

```text
agent-orchestrator
agent-product
agent-architecture
agent-design
agent-frontend
agent-backend
agent-review
```

If any legacy profile remains, run profile migration first:

```text
/hermes-agent-fleet-bootstrap migrate native-ai-engineering
/hermes-agent-fleet-bootstrap migrate native-ai-engineering --apply
```

## Primary user interface

```text
# Preview only
/hermes-agent-fleet-bootstrap sync-models native-ai-engineering

# Apply to all remaining agent profiles
/hermes-agent-fleet-bootstrap sync-models native-ai-engineering --apply
```

The standard skill invocation dispatches to:

```bash
bash "${HERMES_SKILL_DIR}/scripts/hermes-fleet-model-sync" \
  native-ai-engineering [--apply]
```

Direct repository-relative execution is available for CI, debugging, recovery, or pre-install development:

```bash
bash skills/hermes-agent-fleet-bootstrap/scripts/hermes-fleet-model-sync \
  native-ai-engineering \
  --hermes-home "$HOME/.hermes" \
  --apply
```

## Identity preflight

The generation-2 guard:

1. requires preset `identity_generation: 2`;
2. derives the source and targets from the selected preset;
3. blocks when any legacy profile directory remains;
4. blocks when any target `agent-*` profile is missing;
5. records `TARGET_ONLY_COMPLETE`, all target profile IDs, and an empty legacy-presence list in successful receipts.

For the default preset, `agent-orchestrator` is the source. The remaining six `agent-*` profiles are targets. A source override must still name a profile declared by the selected preset.

## Model-policy behavior

After identity preflight, the existing synchronization engine:

1. reads the approved source profile configuration;
2. compares approved model-policy keys against every other profile in the preset;
3. reports `PLAN_UPDATE` or `SKIP_IN_SYNC` without `--apply`;
4. creates a timestamped backup and atomically updates changed target configs with `--apply`;
5. emits a machine-readable receipt without model values or secrets.

Managed model-policy keys:

```text
model
auxiliary
fallback_providers
fallback_model
model_aliases
provider_routing
credential_pool_strategies
```

Unmanaged target configuration remains unchanged, including terminal, tools, skills, gateway, memory, and product-local settings.

## Credential boundary

The executor never copies `.env`, `auth.json`, OAuth access or refresh tokens, API keys, passwords, gateway tokens, sessions, memory, or runtime databases.

Secret-looking nested keys inside managed model sections are not copied from the source. Existing target-side secret values are preserved in place, including secret fields inside nested mappings and position-aligned lists.

For Codex app-server runtime, Hermes profiles use the normal shared Codex state under `~/.codex` by default. The model policy still lives in each profile's `config.yaml`, so this executor synchronizes policy while leaving Codex OAuth state outside Hermes profile mutation.

## Flags

```text
--apply                    mutate target profile configs; omitted means plan-only
--hermes-home PATH         override HERMES_HOME (default: ~/.hermes)
--preset-file PATH         use an explicit approved preset file
--source-profile PROFILE   override agent-orchestrator; must belong to preset
--receipt PATH             override receipt location
--json                     print the machine-readable receipt
```

## Receipts

Apply receipts default to:

```text
$HERMES_HOME/fleet-bootstrap/<preset>/last-model-sync-receipt.json
```

Plan receipts default to:

```text
.evidence/hermes-fleet/<preset>/last-model-sync-receipt.json
```

Receipts contain:

```text
preset ID and version
identity generation and state
source and target profile IDs
action statuses
policy digests
backup paths
credentials_copied: false
migration_required: false
```

They do not contain model-policy values, tokens, credentials, memory, sessions, or environment values.

## Exit codes

```text
0  identity preflight and plan valid, or apply succeeded
3  migration required, incomplete targets, or preset/config/path preflight failure
4  execution or receipt-write failure
```

## Safety and idempotency

- profile and preset identifiers are restricted to lowercase letters, digits, dot, underscore, and hyphen;
- legacy and mixed identity fleets are rejected before model config reads or writes;
- symlinked Hermes/profile/config paths fail closed;
- missing profiles or an unconfigured source model fail closed;
- existing target configs are backed up before replacement;
- writes are atomic;
- repeated identical apply returns `SKIP_IN_SYNC` and creates no new backup;
- starting a new Hermes session is required before relying on changed model policy.

## Everyday order

```text
migrate profile identities
-> audit target-only fleet
-> configure model/runtime on agent-orchestrator
-> preview sync-models
-> apply sync-models
-> start new sessions
-> validate gateway and worker runtime
```
