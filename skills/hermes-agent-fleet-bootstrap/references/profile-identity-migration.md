# Hermes profile identity migration

Use this operation when an existing `native-ai-engineering` fleet still uses the v1 profile IDs.

## Standard invocation

```text
# Read-only plan
/hermes-agent-fleet-bootstrap migrate native-ai-engineering

# Apply after reviewing the plan and stopping gateways manually
/hermes-agent-fleet-bootstrap migrate native-ai-engineering --apply

# Explicitly allow the executor to stop any observed running legacy gateway
/hermes-agent-fleet-bootstrap migrate native-ai-engineering --apply --stop-gateways
```

The standard skill invocation dispatches through:

```bash
bash "${HERMES_SKILL_DIR}/scripts/hermes-fleet" \
  migrate native-ai-engineering [--apply] [supported migration flags]
```

## Strategy

The approved migration uses Hermes' native profile rename command:

```text
hermes profile rename <legacy-profile> <agent-profile>
```

This is an in-place identity change. The existing profile directory is renamed rather than cloned, so profile-local config, credentials, SOUL, memory, sessions, skills, cron state, logs, and runtime state remain attached to the same profile data.

The executor does not copy those files, create duplicate live agents, or delete profile data.

## Mapping

```text
engineering-orchestrator -> agent-orchestrator
product-development      -> agent-product
solution-architecture    -> agent-architecture
product-design           -> agent-design
frontend-engineering     -> agent-frontend
backend-platform         -> agent-backend
quality-review            -> agent-review
```

The machine-readable authority is:

```text
assets/profile-identity-maps/native-ai-engineering-v1-to-v2.json
```

## Plan behavior

Without `--apply`, the executor:

1. validates the v1-to-v2 mapping against preset `2.1.1`;
2. inventories only the presence of profile-local state categories without reading secret values;
3. classifies each pair as `PLAN_NATIVE_RENAME`, `SKIP_ALREADY_MIGRATED`, `BLOCKED_BOTH_PRESENT`, or `BLOCKED_BOTH_MISSING`;
4. accepts a resumable mixed state only when every mapping has exactly one side present;
5. writes a secret-free migration receipt.

Plan-only mode never invokes Hermes mutation commands.

## Apply behavior

With `--apply`, the executor:

1. verifies the Hermes binary and version;
2. reads gateway status from `hermes profile show`;
3. blocks when a gateway is not confirmed stopped, unless `--stop-gateways` was explicitly supplied;
4. exports each legacy profile to a timestamped local archive unless `--skip-export` was explicitly supplied;
5. runs native `hermes profile rename`;
6. verifies the target directory exists and the legacy path is absent;
7. updates the target profile description from the approved v2 preset;
8. reconciles approved managed skills while preserving unrelated custom skills;
9. emits an apply receipt and a separate managed-skill reconciliation receipt.

No gateway is started by the migration operation. Start `agent-orchestrator` only after model synchronization and post-migration audit pass.

## Existing state

The following state remains in the renamed profile directory:

```text
config.yaml
.env
auth.json
SOUL.md
profile.yaml
skills/
memory or memories/
sessions/
cron/
state databases
logs and gateway-local state
```

The receipt records only boolean presence by category. It does not record file contents, token values, model values, memory text, session text, or environment variables.

## Managed versus custom skills

After all required renames, the executor runs normal fleet reconcile against preset v2:

```text
managed target skill missing -> install
managed target skill drifted -> update
managed target skill in sync -> preserve
unrelated custom skill        -> preserve
```

The migration does not make a target skill directory equal to the preset by deleting extras.

## Gateway safety

`agent-orchestrator` is the only target gateway-eligible profile.

Native rename preserves the orchestrator profile directory and its local configuration in place. The migration requires the old gateway to be stopped and never starts the new gateway. This prevents concurrent polling with the same Telegram token.

Specialists remain gateway-disabled by contract.

## Failure and recovery

The executor fails closed when:

- a legacy and target profile both exist for the same mapping;
- neither side exists for a required mapping;
- a profile path is symlinked or not a directory;
- preset and identity map order differ;
- the gateway cannot be confirmed stopped;
- export, rename, verification, or managed-skill reconcile fails.

A successfully renamed profile can be moved back with:

```text
hermes profile rename <agent-profile> <legacy-profile>
```

The exported archive is a second local recovery artifact. The executor does not automatically roll back a partially completed migration because automatic rollback could hide the exact state reached. A repeated plan classifies successful pairs as `SKIP_ALREADY_MIGRATED` and remaining legacy pairs as resumable.

## Flags

```text
--apply                    execute mutation; omitted means plan-only
--stop-gateways            explicitly allow stopping observed legacy gateways
--skip-export              skip profile export archives and record a limitation
--skip-reconcile           skip managed-skill reconcile and record a limitation
--hermes-home PATH         override HERMES_HOME
--hermes-bin COMMAND       override the Hermes executable
--preset-file PATH         use an explicit approved preset
--identity-map-file PATH   use an explicit approved identity map
--skills-root PATH         override the repository skill root
--backup-dir PATH          override timestamped export location
--receipt PATH             override migration receipt location
--json                     print the machine-readable receipt
```

## Completion boundary

A `READY` migration receipt proves profile identity transition and managed-skill reconciliation. It does not prove:

- model-provider authentication;
- model-policy synchronization;
- Telegram gateway startup;
- specialist execution;
- independent review behavior;
- product acceptance, merge, release, or deployment authorization.
