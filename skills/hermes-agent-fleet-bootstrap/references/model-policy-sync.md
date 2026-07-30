# Hermes fleet model-policy synchronization

Use this executor after the fleet exists and the source profile has an approved model configuration.

## Primary user interface

```text
# Preview only
/hermes-agent-fleet-bootstrap sync-models native-ai-engineering

# Apply to all other profiles in the preset
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

## Behavior

The selected preset is the profile topology authority. The executor:

1. resolves the preset and its orchestrator;
2. uses the orchestrator as the source profile unless `--source-profile` names another profile in the same preset;
3. compares approved model-policy keys against every other profile in the preset;
4. reports `PLAN_UPDATE` or `SKIP_IN_SYNC` without `--apply`;
5. creates a timestamped backup and atomically updates changed target configs with `--apply`;
6. emits a machine-readable receipt without model values or secrets.

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

Secret-looking nested keys inside managed model sections are not copied from the source. Existing target-side secret values are preserved in place.

For Codex app-server runtime, Hermes profiles use the normal shared Codex state under `~/.codex` by default. The model policy still lives in each profile's `config.yaml`, so this executor synchronizes policy while leaving Codex OAuth state outside Hermes profile mutation.

## Flags

```text
--apply                    mutate target profile configs; omitted means plan-only
--hermes-home PATH         override HERMES_HOME (default: ~/.hermes)
--preset-file PATH         use an explicit approved preset file
--source-profile PROFILE   override the preset orchestrator as source; must belong to preset
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

Receipts contain profile IDs, action statuses, policy digests, backup paths, and `credentials_copied: false`. They do not contain model-policy values.

## Exit codes

```text
0  plan valid or apply succeeded
3  preset/config/path preflight failure
4  execution or receipt-write failure
```

## Safety and idempotency

- profile and preset identifiers are restricted to lowercase letters, digits, dot, underscore, and hyphen;
- symlinked Hermes/profile/config paths fail closed;
- missing profiles or an unconfigured source model fail closed;
- existing target configs are backed up before replacement;
- writes are atomic;
- repeated identical apply returns `SKIP_IN_SYNC` and creates no new backup;
- starting a new Hermes session is required before relying on changed model policy.
