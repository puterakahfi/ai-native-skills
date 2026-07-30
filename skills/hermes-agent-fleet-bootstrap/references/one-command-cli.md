# One-command Hermes fleet CLI

Use this deterministic executor after the fleet topology and specialist contracts are approved.

## Primary command

From the `ai-native-skills` repository root:

```bash
bash skills/hermes-agent-fleet-bootstrap/scripts/hermes-fleet \
  bootstrap native-ai-engineering --apply
```

Without `--apply`, the command is plan-only and does not create profiles, install skills, or initialize Kanban:

```bash
bash skills/hermes-agent-fleet-bootstrap/scripts/hermes-fleet \
  bootstrap native-ai-engineering
```

## Operations

```bash
# Preview a bootstrap
bash skills/hermes-agent-fleet-bootstrap/scripts/hermes-fleet \
  bootstrap native-ai-engineering

# Create missing profiles, synchronize managed skills, and initialize Kanban
bash skills/hermes-agent-fleet-bootstrap/scripts/hermes-fleet \
  bootstrap native-ai-engineering --apply

# Read-only conformance audit
bash skills/hermes-agent-fleet-bootstrap/scripts/hermes-fleet \
  audit native-ai-engineering

# Preview reconciliation after skill catalog changes
bash skills/hermes-agent-fleet-bootstrap/scripts/hermes-fleet \
  reconcile native-ai-engineering

# Apply reconciliation
bash skills/hermes-agent-fleet-bootstrap/scripts/hermes-fleet \
  reconcile native-ai-engineering --apply
```

## Deterministic boundary

The CLI does not invent a topology through an LLM. It executes an approved preset. The `native-ai-engineering` preset creates or audits:

```text
engineering-orchestrator
product-development
solution-architecture
product-design
frontend-engineering
backend-platform
quality-review
```

Only `engineering-orchestrator` is marked gateway-eligible. The CLI does not start a gateway or provision bot tokens.

## Side effects

With `--apply`, the CLI may:

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
3  preset/preflight failure, missing skill source, or missing Hermes
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
