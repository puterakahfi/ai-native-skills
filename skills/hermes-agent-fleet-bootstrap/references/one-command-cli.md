# One-command Hermes fleet execution

Use this deterministic executor after the fleet topology and agent responsibility contracts are approved.

## Primary user interface

The installed Hermes skill slash command is the normal entrypoint. Users should not need to know where the skill package is stored.

```text
# Preview a fresh target fleet without mutation
/hermes-agent-fleet-bootstrap bootstrap native-ai-engineering

# Create missing target profiles, synchronize managed skills, and initialize Kanban
/hermes-agent-fleet-bootstrap bootstrap native-ai-engineering --apply

# Read-only conformance and identity-state audit
/hermes-agent-fleet-bootstrap audit native-ai-engineering

# Preview reconciliation of an existing target fleet
/hermes-agent-fleet-bootstrap reconcile native-ai-engineering

# Apply target-fleet reconciliation
/hermes-agent-fleet-bootstrap reconcile native-ai-engineering --apply

# Preview model-policy synchronization from the preset orchestrator
/hermes-agent-fleet-bootstrap sync-models native-ai-engineering

# Apply non-secret model-policy synchronization
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

The agent must use the terminal tool, preserve the executor exit code, and return the generated receipt. It must not manually reproduce profile, skill, Kanban, model-policy, audit, or receipt operations.

Without `--apply`, `bootstrap`, `reconcile`, and `sync-models` are plan-only. `audit` is always read-only.

## Target preset v2

The `native-ai-engineering` preset is a breaking identity generation with version `2.0.0`:

```text
agent-orchestrator
agent-product
agent-architecture
agent-design
agent-frontend
agent-backend
agent-review
```

Only `agent-orchestrator` is gateway-eligible and user-facing by default. Every other default profile has:

```yaml
gateway: none
worker_mode: headless_on_demand
```

The fleet remains product-neutral. Product and repository identity are task context, not reusable profile IDs.

## Identity-state preflight

Before planning profile or skill actions, the executor classifies the observed profile directories:

```text
EMPTY
TARGET_ONLY_COMPLETE
TARGET_ONLY_PARTIAL
LEGACY_ONLY_COMPLETE
LEGACY_ONLY_PARTIAL
MIXED
UNVERSIONED
```

Behavior:

```text
EMPTY
→ fresh bootstrap or reconcile may proceed

TARGET_ONLY_COMPLETE
→ audit or idempotent reconcile may proceed

TARGET_ONLY_PARTIAL
→ audit reports NEEDS_WORK; reconcile may create missing target profiles

LEGACY_ONLY_COMPLETE / LEGACY_ONLY_PARTIAL
→ audit reports migration required
→ bootstrap and reconcile fail closed

MIXED
→ audit reports an ambiguous migration state
→ bootstrap and reconcile fail closed
```

Legacy or mixed fleets must use the approved non-destructive migration operation delivered separately. Ordinary bootstrap and reconcile never reinterpret legacy profiles as target profiles, rename directories, copy live state, or retire old identities.

## Low-level interface

Direct repository-relative execution remains available for CI, debugging, recovery, and development before the skill is installed:

```bash
bash skills/hermes-agent-fleet-bootstrap/scripts/hermes-fleet \
  bootstrap native-ai-engineering --apply

bash skills/hermes-agent-fleet-bootstrap/scripts/hermes-fleet-model-sync \
  native-ai-engineering --apply
```

This is not the primary user-facing invocation because it requires knowledge of the repository checkout path.

## Operations

```text
bootstrap    create missing target profiles, synchronize managed skills, initialize Kanban
reconcile    compare and synchronize an approved target preset idempotently
audit        classify identity state and inspect conformance without runtime mutation
sync-models  synchronize non-secret model policy from the preset orchestrator to target profiles
```

## Catalog-backed symlink model

Managed fleet skills are projected as symlinks to a fixed catalog clone:

```text
~/.hermes/ai-native-skills/skills/<skill-id>
→ ~/.hermes/profiles/<profile-id>/skills/<skill-id>
```

This makes the update mechanism explicit and machine-independent:

```bash
cd ~/.hermes/ai-native-skills && git pull
```

All managed profile skills then observe the new catalog content immediately. Profile-local skills that are not listed in the fleet preset remain real directories and are preserved.

## Deterministic and safety boundary

The executors apply approved presets; they do not invent topology through an LLM. Custom preset, profile, and skill identifiers are restricted to lowercase letters, digits, dot, underscore, and hyphen. Unsafe identifiers, overlapping target and legacy IDs, duplicate skills, malformed semantic versions, invalid gateway ownership, invalid worker modes, path traversal, invalid skill sources, and profile-root symlinks fail closed. Managed skill entries are the one intentional symlink boundary: each must resolve to the approved catalog skill source.

The executor does not:

- start or stop a messaging gateway;
- provision or copy bot/provider credentials;
- copy `.env`, `auth.json`, API keys, OAuth tokens, passwords, sessions, memory, cron, Kanban databases, or runtime databases;
- rename or delete legacy profiles;
- claim Telegram or worker runtime readiness.

## Side effects

With `--apply`, fleet bootstrap or reconcile may:

- run `hermes --version`;
- run `hermes profile create ... --no-skills --no-alias` for missing target profiles;
- create or update approved skill symlinks in profile-local `skills/` directories;
- run `hermes kanban init`;
- write a secret-free receipt under `$HERMES_HOME/fleet-bootstrap/<preset>/last-receipt.json`.

With `--apply`, model-policy synchronization may:

- read the selected preset and source profile `config.yaml`;
- create timestamped backups of changed target `config.yaml` files;
- atomically synchronize approved model-policy keys;
- write a secret-free receipt under `$HERMES_HOME/fleet-bootstrap/<preset>/last-model-sync-receipt.json`.

Plan-only and audit receipts default to:

```text
.evidence/hermes-fleet/<preset>/last-receipt.json
.evidence/hermes-fleet/<preset>/last-model-sync-receipt.json
```

Fleet receipts expose preset version, identity generation, target profile IDs, orchestrator profile, observed identity state, non-secret actions, findings, and readiness. They record:

```yaml
credentials_copied: false
live_state_copied: false
```

## Exit codes

```text
0  plan valid, apply succeeded, or audit passed
2  audit found missing, drifted, legacy, partial, or mixed fleet state
3  preset/preflight failure, unsafe identity state, missing skill, missing profile/config, or missing Hermes
4  execution or receipt-write failure
```

## Useful flags

Fleet executor:

```text
--apply                 execute mutations; omitted means plan-only
--hermes-home PATH      override HERMES_HOME
--hermes-bin COMMAND    override Hermes binary
--skills-root PATH      override local skill catalog root
--preset-file PATH      use an explicit approved preset
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

Load `model-policy-sync.md` for exact managed keys, credential boundaries, backups, receipts, and idempotency behavior.

## Idempotency

Repeated fleet apply runs:

- preserve existing target profiles;
- skip skill packages whose content digest already matches;
- update only changed managed skill directories;
- skip Kanban initialization when an existing database is observed;
- never create duplicate profiles;
- preserve unmanaged profile configuration and runtime-owned state.

Repeated model-policy apply runs:

- preserve target-specific configuration outside managed model-policy keys;
- preserve target-side secret values without copying source secrets;
- skip profiles whose sanitized model-policy digest already matches;
- create no new backup when every target is already in sync.
