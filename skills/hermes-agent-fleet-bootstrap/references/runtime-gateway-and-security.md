# Runtime, Gateway, and Security Reference

Load this reference when defining bots, messaging gateways, Kanban workers, permissions, sandboxing, credentials, or runtime verification.

## Runtime identities

```text
Hermes profile
  durable identity, configuration, SOUL, skills, memory, sessions, and local runtime state

bot or messaging gateway
  optional user-facing communication surface for one profile

worker process
  bounded execution of a selected profile for assigned work

Kanban or durable work item
  shared coordination state, dependencies, status, comments, retries, and handoffs
```

Do not collapse these concepts. A persistent profile does not require a dedicated bot, and a bot does not prove a multi-agent runtime exists behind it.

## Default gateway policy

The `native-ai-engineering` v2 target is:

```yaml
gateway_policy:
  default_front_door:
    profile: agent-orchestrator
    mode: messaging_front_door
  specialist_default:
    profiles:
      - agent-product
      - agent-architecture
      - agent-design
      - agent-frontend
      - agent-backend
      - agent-review
    mode: none
    worker_mode: headless_on_demand
    execution: kanban_or_verified_on_demand_worker
```

Only `agent-orchestrator` is gateway-eligible by default. A specialist bot is justified only when the profile has an independent audience, product-facing identity, direct operational responsibility, separate tenant, or explicit security boundary.

A Telegram display name may differ from the internal profile ID. Runtime routing, receipts, and worker evidence must still identify `agent-orchestrator` and the actual selected specialist profile IDs.

Record:

```yaml
gateway_record:
  profile_id: ""
  mode: none | messaging_front_door | dedicated
  channel: telegram | discord | cli | desktop | other | NOT_VERIFIED
  audience: []
  token_reference: ""
  token_in_distribution: false
  routing_rule: ""
  runtime_evidence: []
```

Never include tokens or credentials in reusable profile distributions or receipts.

## Legacy gateway transition

The legacy gateway profile is `engineering-orchestrator`; the target is `agent-orchestrator`.

Ordinary bootstrap, reconcile, audit, and model-policy synchronization do not move gateway ownership. Migration must return:

```yaml
gateway_transition:
  legacy_profile: engineering-orchestrator
  target_profile: agent-orchestrator
  action: MANUAL_REBIND
  token_copied: false
  gateway_started: false
```

Do not run legacy and target gateways concurrently with the same Telegram token. Stop and verify the legacy gateway before manually configuring or starting the target gateway. Never claim the gateway moved or started without direct runtime evidence.

## Durable work model

```text
agent-orchestrator receives outcome
→ selects exactly one primary workflow
→ creates or routes durable work items
→ assigns the smallest relevant agent-* specialist set
→ specialists consume bounded tasks and artifacts
→ specialists record outputs, evidence, risks, and handoffs
→ agent-review evaluates independently when required
→ agent-orchestrator synthesizes actual state
→ response returns through the originating gateway
```

The fleet skill defines this contract. It does not implement or claim Kanban, dispatcher, worker spawning, retry, or persistence behavior unless the actual Hermes runtime is observed.

## Runtime verification checklist

Verify against the selected Hermes installation:

- installed Hermes version or revision;
- profile create/show/list commands;
- profile directory location;
- gateway start/stop/status behavior;
- channel-specific routing and token rules;
- Kanban availability and board location;
- dispatcher or worker-lane availability;
- profile addressing and task assignment;
- worker process lifecycle;
- retry, failure, cancellation, and resume behavior;
- shared artifact or workspace behavior;
- concurrent write and repository collision controls;
- logs, receipts, and evidence locations.

If any required behavior cannot be observed, report it as `NOT_VERIFIED` or `BLOCKED`. Preset installation or documentation is not runtime proof.

## Profile isolation is not sandbox proof

Separate Hermes profile directories may isolate application state, but do not automatically prove:

- separate operating-system users;
- filesystem restrictions;
- process isolation;
- network restrictions;
- secret-store separation;
- repository write boundaries;
- cloud-account or environment separation;
- production blast-radius controls.

Every profile contract should record:

```yaml
permission_policy:
  filesystem:
    allowed_paths: []
    denied_paths: []
    evidence: []
  repositories:
    read: []
    write: []
    evidence: []
  network:
    allowed_destinations: []
    evidence: []
  credentials:
    references: []
    storage: ""
    evidence: []
  environments:
    allowed: []
    production_access: false
    evidence: []
  sandbox:
    type: none | os_user | container | vm | runtime_backend | other | NOT_VERIFIED
    evidence: []
```

Missing isolation evidence must not be inferred from profile naming.

## Privileged operations profiles

An `agent-operations` or equivalent profile requires:

- separate credentials or scoped identity;
- explicit allowed environments;
- least-privilege tools;
- command and mutation logging;
- rollback procedure;
- health-verification procedure;
- human approval for production and irreversible actions;
- incident ownership and escalation path;
- blast-radius and sandbox evidence.

Runtime completion does not grant release, deployment, or risk acceptance authority.

## Reviewer independence

Record actual shared resources:

```yaml
review_independence:
  reviewer_profile: agent-review
  implementer_profiles: []
  same_model: true | false | NOT_VERIFIED
  shared_context: true | false | NOT_VERIFIED
  shared_tools: true | false | NOT_VERIFIED
  shared_permissions: true | false | NOT_VERIFIED
  prior_implementation_participation: true | false | NOT_VERIFIED
  status: VERIFIED | LIMITED_SHARED_MODEL | LIMITED_SHARED_CONTEXT | LIMITED_SHARED_TOOLS | NOT_VERIFIED
  limitations: []
```

Separate profile names alone do not establish independence. A limited review may still produce useful findings, but must not be represented as fully independent acceptance.

## Product-facing bot exceptions

A durable product or domain profile may keep a dedicated bot when it serves direct users, an independent audience, or a recurring product workflow. A product profile is optional and should be created only when persistent product context, stakeholder relationship, or acceptance responsibility is justified. Product profiles remain outside the reusable `native-ai-engineering` agent-* fleet.

Generic example:

```text
@product_bot
→ product-facing agent and product-context custodian
→ prepares a bounded engineering request
→ agent-orchestrator coordinates the shared engineering fleet
→ product authority accepts or rejects the result
```

The example is product-neutral. A named product such as `visualmate`, an office portal, an internal finance system, or a client product is illustrative only and does not become part of reusable specialist identity.

Product-facing profiles should not automatically receive repository write, production access, or the full engineering skill suite. Load `product-context-and-environments.md` before sharing a fleet across products or mixing personal, office, client, or tenant contexts.

## Prohibited distribution content

Never include:

```text
.env
.env.*
auth.json
state.db
state.db-wal
state.db-shm
sessions/
memories/
cron/
logs/
cache/
secrets/
tokens/
credentials/
```

A live Hermes profile may contain runtime-managed state locally. That state is not part of the reusable profile distribution and must not be copied during bootstrap, model synchronization, or migration.

## Fail-closed conditions

- Bot or gateway tokens are requested for committed output.
- Two profiles are configured to share a token without verified runtime support and policy.
- Legacy and target gateways would run concurrently with the same token.
- A specialist receives a default gateway without a dedicated-audience exception.
- Production access is granted without explicit authorization.
- Filesystem or repository scope is implied but not evidenced.
- Runtime worker behavior is claimed without execution evidence.
- Reviewer independence is inferred from profile names.
- Existing live profile state would be overwritten or copied destructively.
