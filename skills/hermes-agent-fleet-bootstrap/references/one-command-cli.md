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
```

The skill interprets the invocation as:

```text
/hermes-agent-fleet-bootstrap <operation> <preset> [--apply] [supported executor flags]
```

It then executes the bundled runner through the standard skill directory variable:

```bash
bash "${HERMES_SKILL_DIR}/scripts/hermes-fleet" \
  <operation> <preset> [--apply] [supported executor flags]
```

The agent must use the terminal tool, preserve the executor exit code, and return the generated receipt. It must not manually reproduce the runner's profile, skill, Kanban, audit, or receipt operations.

Without `--apply`, `bootstrap` and `reconcile` are plan-only and do not create profiles, install skills, or initialize Kanban. `audit` is always read-only.

## Low-level interface

Direct repository-relative execution remains available for CI, debugging, recovery, and development before the skill has been installed:

```bash
bash skills/hermes-agent-fleet-bootstrap/scripts/hermes-fleet \
  bootstrap native-ai-engineering --apply
```

This is not the primary user-facing invocation because it requires knowledge of the repository checkout path.

## Operations

```text
bootstrap  create missing profiles, synchronize managed skills, initialize Kanban
reconcile  compare and synchronize an approved preset idempotently
audit      inspect conformance without runtime mutation
```

## Deterministic boundary

The executor does not invent a topology through an LLM. It executes an approved preset. The `native-ai-engineering` preset creates or audits:

```text
engineering-orchestrator
product-development
solution-architecture
product-design
frontend-engineering
backend-platform
quality-review
```

Only `engineering-orchestrator` is marked gateway-eligible. The executor does not start a gateway or provision bot tokens.

Custom preset, profile, and skill identifiers are restricted to lowercase letters, digits, dot, underscore, and hyphen. Path traversal, symlinked profile roots, and symlinked managed skill sources fail closed before mutation.

## Side effects

With `--apply`, the executor may:

- run `hermes --version`;
- run `hermes profile create ... --no-skills --no-alias` for missing profiles;
- copy approved skill packages into profile-local `skills/` directories;
- run `hermes kanban init`;
- write a fleet receipt under `$HERMES_HOME/fleet-bootstrap/<preset>/last-receipt.json`.

It does not delete profiles or modify profile memory, sessions, credentials, cron state, provider configuration, or gateway tokens.

Plan-only and audit receipts default to:

```text
.evidence/hermes-fleet/<preset>/last-receipt.json
```

## Exit codes

```text
0  plan valid, apply succeeded, or audit passed
2  audit found drift or missing fleet state
3  preset/preflight failure, missing skill source, missing runner, or missing Hermes
4  execution or receipt-write failure
```

## Useful flags

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

## Idempotency

Repeated apply runs:

- preserve existing profiles;
- skip skill packages whose content digest already matches;
- update only managed skill directories with changed content;
- skip Kanban initialization when an existing database is observed;
- never create duplicate profiles.

Existing profile descriptions and runtime state are preserved rather than silently rewritten.
