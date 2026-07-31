# Product Context and Environment Topology

Load this reference when deciding whether a product needs its own Hermes profile, when one engineering fleet serves multiple products, or when personal, office, client, or tenant environments must remain separated.

## Product-neutral fleet

The `native-ai-engineering` preset is a reusable engineering organization. It is not tied to VisualMate, pkahfi, a specific employer, repository, product name, industry, or tenant.

```text
trusted environment
→ engineering-orchestrator
→ shared specialist fleet
→ bounded product or repository context per task
```

Examples of trusted environments:

```text
personal laptop / personal Hermes home
office laptop / office Hermes home
client A isolated Hermes home
client B isolated Hermes home
```

A product name used in an example is illustrative only. Never infer that `visualmate`, `pkahfi`, or another named product is required, privileged, or automatically present.

## Product profile is optional

A repository or product does not automatically require a persistent Hermes product profile.

Use no dedicated product profile when work is occasional, context is small, or repository-local evidence is sufficient:

```text
user
→ engineering-orchestrator
→ bounded task context
→ specialist fleet
```

The task should identify at least:

```yaml
product_context:
  product_or_service: ""
  repository_or_workspace: ""
  objective: ""
  accepted_decisions: []
  constraints: []
  acceptance_criteria: []
  authority: PLAN_ONLY | CREATE_OR_UPDATE | REVIEW_ONLY
```

Do not create a product profile merely because a repository exists.

## When a durable product profile is justified

A persistent product profile may be justified when several of these are recurring and durable:

- product intent, positioning, or user model;
- domain language and business rules;
- accepted product decisions;
- stakeholder and approval flow;
- roadmap, release, or acceptance responsibility;
- direct user-facing bot or product interaction;
- repeated work across multiple repositories;
- product-specific memory that should not become specialist identity.

A justified product profile owns product context and acceptance boundaries. It does not automatically own architecture, frontend, backend, testing, security review, deployment, or the full engineering skill catalog.

```text
product profile
→ product-context custodian and product-facing authority
→ bounded handoff to engineering-orchestrator
→ shared specialist fleet
→ reviewed result
→ originating product profile or human accepts product outcome
```

## Domain profile for multiple related products

When several products share durable terminology, stakeholders, policy, and acceptance flow, one domain profile may be simpler than one profile per repository.

```text
finance-systems
├ billing-service
├ reporting-dashboard
└ reconciliation-worker

finance-systems product/domain profile
→ engineering-orchestrator
→ shared specialist fleet
```

The smallest sufficient persistent context boundary must win.

## Office and personal environments

Personal and office products should not silently share runtime state, credentials, memory, sessions, Kanban state, or product context.

Preferred isolation:

```text
personal machine
~/.hermes

office machine
~/.hermes
```

When the same host must serve multiple trust environments, use separate Hermes homes:

```bash
# Personal environment
export HERMES_HOME="$HOME/.hermes-personal"

# Office environment
export HERMES_HOME="$HOME/.hermes-office"
```

Bootstrap a separate office fleet:

```bash
bash skills/hermes-agent-fleet-bootstrap/scripts/hermes-fleet \
  bootstrap native-ai-engineering \
  --hermes-home "$HOME/.hermes-office" \
  --apply
```

Open the office orchestrator with the same environment selected:

```bash
HERMES_HOME="$HOME/.hermes-office" \
  hermes -p engineering-orchestrator
```

Separate `HERMES_HOME` roots isolate Hermes-managed application state. They do not by themselves prove operating-system, filesystem, process, network, cloud-account, or secret-store isolation.

## Shared-fleet boundary

One fleet may serve multiple products only when they are allowed to share the same engineering trust environment.

Before sharing a fleet, verify:

```yaml
shared_fleet_boundary:
  organization_or_owner: ""
  products_or_repositories: []
  shared_credentials_allowed: true | false | NOT_VERIFIED
  shared_memory_allowed: true | false | NOT_VERIFIED
  shared_kanban_allowed: true | false | NOT_VERIFIED
  shared_filesystem_allowed: true | false | NOT_VERIFIED
  tenant_boundary: single | multiple | NOT_VERIFIED
  security_boundary: shared | isolated | NOT_VERIFIED
  evidence: []
```

Use separate fleets or runtime homes when products belong to different employers, clients, tenants, confidentiality zones, credential scopes, or production blast-radius boundaries.

## Product repository versus product profile

```text
product repository
  versioned source code, requirements, architecture records,
  policies, tests, acceptance evidence, and product truth

product profile
  optional durable agent context for recurring product-facing work
```

A repository can exist without a product profile. A product profile can coordinate several repositories. Repository evidence remains authoritative over remembered profile context when they conflict.

## Product-facing bots

A product profile may retain a dedicated bot when it serves an independent audience or product workflow.

Generic example:

```text
@product_bot
→ product-facing agent
→ prepares bounded product context
→ submits an engineering request
→ shared engineering orchestrator coordinates specialists
→ product authority accepts or rejects the result
```

This exception does not grant the product profile repository write access, production credentials, or the full engineering skill suite.

## Fail-closed conditions

- A personal product or memory is inferred inside an office fleet.
- An office or client repository is routed through a personal product profile without explicit authorization.
- Separate employers, clients, or tenants share one fleet without verified permission and security boundaries.
- A product profile is created only because a repository or framework exists.
- Product facts are embedded permanently in reusable specialist identity.
- Profile memory silently overrides repository evidence or accepted product records.
- Separate `HERMES_HOME` roots are represented as complete OS or credential sandboxing.
