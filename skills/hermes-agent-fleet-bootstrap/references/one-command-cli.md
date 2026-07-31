# One-command Hermes fleet execution

Use this deterministic executor after the fleet topology and specialist contracts are approved.

## Primary user interface

The installed Hermes skill slash command is the normal entrypoint. Users should not need to know where the skill package is stored.

```text
# Preview without mutation
/hermes-agent-fleet-bootstrap bootstrap native-ai-engineering

# Create missing profiles, synchronize managed skills, and initialize Kanban
/hermes-agent-fleet-bootstrap bootstrap native-ai-engineering --apply

# Read-only conformance audit
/hermes-agent-fleet-bootstrap audit native-ai-engineering

# Preview reconciliation after skill catalog changes
/hermes-agent-fleet-bootstrap reconcile native-ai-engineering

# Apply reconciliation
/hermes-agent-fleet-bootstrap reconcile native-ai-engineering --apply

# Preview model-policy synchronization from the orchestrator
/hermes-agent-fleet-bootstrap sync-models native-ai-engineering

# Apply model-policy synchronization to the remaining preset profiles
/hermes-agent-fleet-bootstrap sync-models native-ai-engineering --apply
```

The skill interprets the invocation as:

```text
/hermes-agent-fleet-bootstrap <operation> <preset> [--apply] [supported executor flags]
```

Fleet bootstrap, reconcile, and audit execute through:

```bash
bash "${HERMES_SKILL_DIR}/scripts/hermes-fleet" \
  <operation> <preset> [--apply] [supported executor flags]
```

`sync-models` is dispatched by the same wrapper to:

```bash
bash "${HERMES_SKILL_DIR}/scripts/hermes-fleet-model-sync" \
  <preset> [--apply] [supported model-sync flags]
```

The agent must use the terminal tool, preserve the executor exit code, and return the generated receipt. It must not manually reproduce the runner's profile, skill, Kanban, model-policy, audit, or receipt operations.

Without `--apply`, `bootstrap`, `reconcile`, and `sync-models` are plan-only. `audit` is always read-only.

## Low-level interface

Direct repository-relative execution remains available for CI, debugging, recovery, and development before the skill has been installed:

```bash
bash skills/hermes-agent-fleet-bootstrap/scripts/hermes-fleet \
  bootstrap native-ai-engineering --apply

bash skills/hermes-agent-fleet-bootstrap/scripts/hermes-fleet-model-sync \
  native-ai-engineering --apply
```

This is not the primary user-facing invocation because it requires knowledge of the repository checkout path.

## Operations

```text
bootstrap    create missing profiles, synchronize managed skills, initialize Kanban
reconcile    compare and synchronize an approved preset idempotently
audit        inspect conformance without runtime mutation
sync-models  synchronize non-secret model policy from one preset profile to the others
```

## Deterministic boundary

The executors do not invent a topology through an LLM. They execute an approved preset. The `native-ai-engineering` preset creates or audits:

```text
engineering-orchestrator
product-development
solution-architecture
product-design
frontend-engineering
backend-platform
quality-review
```

Only `engineering-orchestrator` is marked gateway-eligible. The executors do not start a gateway or provision bot tokens.

Custom preset, profile, and skill identifiers are restricted to lowercase letters, digits, dot, underscore, and hyphen. Path traversal, symlinked profile roots, and symlinked managed skill or model-config paths fail closed before mutation.

## Side effects

With `--apply`, fleet bootstrap or reconcile may:

- run `hermes --version`;
- run `hermes profile create ... --no-skills --no-alias` for missing profiles;
- copy approved skill packages into profile-local `skills/` directories;
- run `hermes kanban init`;
- write a fleet receipt under `$HERMES_HOME/fleet-bootstrap/<preset>/last-receipt.json`.

With `--apply`, model-policy synchronization may:

- read the selected preset and source profile `config.yaml`;
- create timestamped backups of changed target `config.yaml` files;
- atomically synchronize approved model-policy keys;
- write a receipt under `$HERMES_HOME/fleet-bootstrap/<preset>/last-model-sync-receipt.json`.

Neither executor deletes profiles or modifies profile memory, sessions, credentials, cron state, gateway tokens, or product truth. Model-policy synchronization never copies `.env`, `auth.json`, API keys, OAuth tokens, passwords, or secret-looking nested values.

Plan-only and audit receipts default to:

```text
.evidence/hermes-fleet/<preset>/last-receipt.json
.evidence/hermes-fleet/<preset>/last-model-sync-receipt.json
```

## Exit codes

```text
0  plan valid, apply succeeded, or audit passed
2  audit found drift or missing fleet state
3  preset/preflight failure, missing skill source, missing runner, missing profile/config, or missing Hermes
4  execution or receipt-write failure
```

## Useful flags

Fleet executor:

```text
--apply                 execute mutations; omitted means plan-only
--hermes-home PATH      override HERMES_HOME
--hermes-bin COMMAND    override Hermes binary
--skills-root PATH      override local skill catalog root
--preset-file PATH      use an explicit preset for testing or controlled extension
--receipt PATH          override receipt location
--skip-kanban           do not initialize Kanban
--json                  print the machine-readable receipt
```

Model-policy sync:

```text
--apply                    execute mutations; omitted means plan-only
--hermes-home PATH         override HERMES_HOME
--preset-file PATH         use an explicit approved preset
--source-profile PROFILE   override the preset orchestrator; must belong to preset
--receipt PATH             override receipt location
--json                     print the machine-readable receipt
```

Load `model-policy-sync.md` for the exact managed keys, credential boundary, receipts, and idempotency behavior.

## Idempotency

Repeated fleet apply runs:

- preserve existing profiles;
- skip skill packages whose content digest already matches;
- update only managed skill directories with changed content;
- skip Kanban initialization when an existing database is observed;
- never create duplicate profiles.

Repeated model-policy apply runs:

- preserve target-specific configuration outside managed model-policy keys;
- preserve target-side secret values without copying source secrets;
- skip profiles whose sanitized model-policy digest already matches;
- create no new backup when every target is already in sync.

Existing profile descriptions and runtime state are preserved rather than silently rewritten.
