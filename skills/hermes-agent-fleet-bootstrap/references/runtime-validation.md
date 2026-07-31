# Hermes agent-fleet runtime validation

Use this acceptance gate after identity migration, target-fleet audit, and model-policy synchronization.

## Standard invocation

```text
/hermes-agent-fleet-bootstrap validate-runtime native-ai-engineering \
  --evidence /path/to/sanitized-runtime-evidence.json
```

The installed skill dispatches through:

```bash
bash "${HERMES_SKILL_DIR}/scripts/hermes-fleet" \
  validate-runtime native-ai-engineering \
  --evidence /path/to/sanitized-runtime-evidence.json
```

Direct repository-relative execution is available for CI and debugging:

```bash
bash skills/hermes-agent-fleet-bootstrap/scripts/hermes-fleet-runtime-acceptance \
  native-ai-engineering \
  --evidence skills/hermes-agent-fleet-bootstrap/tests/fixtures/runtime-acceptance-pass-with-limitations.json \
  --json
```

## Required operating order

```text
1. migrate legacy identities
2. audit TARGET_ONLY_COMPLETE
3. configure model/runtime on agent-orchestrator
4. synchronize approved non-secret model policy
5. verify only agent-orchestrator owns a gateway
6. capture bounded planning, backend, and UI scenarios
7. capture Telegram round-trip evidence when a local bot credential is available
8. sanitize evidence
9. run validate-runtime
```

Repository CI must never receive Telegram tokens, provider credentials, OAuth state, memory text, session text, or private task payloads.

## Evidence schema

```json
{
  "schema_version": "1.0.0",
  "fleet_id": "native-ai-engineering",
  "identity_state": "TARGET_ONLY_COMPLETE",
  "profiles": [],
  "migration": {},
  "model_sync": {},
  "scenarios": [],
  "review_independence": {},
  "telegram": {},
  "model_driven_workers": {}
}
```

The evaluator requires the exact ordered target profile set:

```text
agent-orchestrator
agent-product
agent-architecture
agent-design
agent-frontend
agent-backend
agent-review
```

`agent-orchestrator` must be the only `gateway: eligible` profile. Every specialist must declare:

```yaml
gateway: none
worker_mode: headless_on_demand
```

## Routing scenarios

### Planning-only

Required workers:

```text
agent-product
agent-architecture
```

Implementation agents must not be invoked without a documented reason.

### Backend work

Required workers:

```text
agent-backend
agent-review
```

The evidence must contain a unique task ID, observable dependency/handoff data, implementation outputs, and a review verdict.

### UI work

Required workers:

```text
agent-design
agent-frontend
agent-review
```

`agent-backend` must not be selected for a bounded UI-only scenario.

No scenario may count `agent-orchestrator` as the specialist implementer. No bounded scenario may invoke every specialist by default.

## Review independence

Allowed states:

```text
VERIFIED_SEPARATE_RUNTIME
VERIFIED_SEPARATE_PROFILE
LIMITED_SHARED_RUNTIME
LIMITED_SHARED_MODEL_AND_ACCOUNT
```

A `LIMITED_*` state must include concrete limitations. Separate profile identity alone is not represented as complete reviewer independence.

## Telegram evidence

A full Telegram PASS requires sanitized evidence that:

```text
configured_profile: agent-orchestrator
gateway_started: true
message_received: true
response_returned: true
legacy_gateway_running: false
credential_values_redacted: true
evidence_level: LIVE
```

Do not record the bot token. Do not run the legacy and target gateways concurrently with the same token.

When no local bot credential or external Telegram channel is available, record:

```text
evidence_level: NOT_RUN
configured_profile: NOT_CONFIGURED
gateway_started: false
message_received: false
response_returned: false
credential_values_redacted: true
legacy_gateway_running: false
```

This yields `PASS_WITH_LIMITATIONS` when all non-Telegram acceptance gates pass. It must not be called a live gateway PASS.

## Provider-backed worker evidence

Full model-driven worker acceptance requires:

```text
evidence_level: LIVE
specialist_execution_observed: true
```

Repository fixtures may validate routing contracts without provider credentials, but those fixtures yield `PASS_WITH_LIMITATIONS` and preserve `provider_backed_specialist_execution_not_verified`.

## Verdicts

```text
PASS
  all structural, routing, review, Telegram, and provider-backed worker evidence passes

PASS_WITH_LIMITATIONS
  structural and routing evidence passes, but live Telegram or provider-backed workers are not available

NEEDS_WORK
  one or more acceptance checks fail

BLOCKED
  evidence is malformed, unsafe, contains secret material, or cannot be evaluated
```

Both `PASS` and `PASS_WITH_LIMITATIONS` return exit code `0`. `NEEDS_WORK` returns `2`. Unsafe or malformed evidence returns `3`.

## Secret rejection

The evaluator rejects evidence containing raw fields such as:

```text
token
telegram_token
bot_token
api_key
password
client_secret
access_token
refresh_token
authorization
private_key
```

It also rejects strings matching the normal Telegram bot-token shape.

## Local live acceptance checklist

Run this only in the authorized local Hermes environment:

```text
/hermes-agent-fleet-bootstrap migrate native-ai-engineering --apply
/hermes-agent-fleet-bootstrap audit native-ai-engineering
/hermes-agent-fleet-bootstrap sync-models native-ai-engineering --apply

hermes -p agent-orchestrator gateway status
hermes -p agent-orchestrator gateway start
```

Then submit three bounded messages through Telegram:

1. planning-only request;
2. backend request requiring review;
3. UI request requiring design, frontend, and review.

Capture sanitized task IDs, selected profile IDs, dependency state, handoffs, outputs, review verdicts, and return-path evidence. Never copy the token or private conversation content into the repository.

## Completion boundary

A `PASS_WITH_LIMITATIONS` acceptance proves:

- exact target fleet structure;
- one gateway owner by contract;
- headless specialist contracts;
- migration and model-sync evidence shape;
- bounded routing decisions;
- task/dependency/handoff/review evidence requirements;
- secret-free evaluator behavior.

It does not prove a live Telegram round trip or provider-backed specialist reasoning unless those fields are supplied as `LIVE` and pass validation.
