---
name: chatgpt-app-development
description: Design and deliver ChatGPT Apps with the OpenAI Apps SDK and MCP — product boundary, cost ownership, tool contracts, widget UX, native ChatGPT capability handoff, auth, state, security, testing, deployment, and publication readiness.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.requires: "native-ai-engineer ai-system-design api-contract master-design adaptive-component-design accessibility threat-modeling security-review observability-design"
  ai-native-skills.related_skills: '["product-development-workflow","new-feature-workflow","native-ai-engineer","ai-system-design","api-contract","master-design","adaptive-component-design","security-review","threat-modeling","observability-design"]'
---

# ChatGPT App Development

Build ChatGPT Apps as conversational products with MCP-backed tools and optional in-chat UI. Keep product economics, platform boundaries, tool contracts, user experience, and security explicit before implementation.

## Trigger

Load this skill when the target surface is a ChatGPT App, OpenAI Apps SDK integration, MCP app, ChatGPT widget, or an existing product capability exposed inside ChatGPT.

Do not use this skill for:

- ordinary OpenAI API integrations with no ChatGPT App surface;
- generic MCP servers that are not intended for ChatGPT;
- Custom GPT instruction/knowledge authoring without an app integration;
- product-specific business rules that belong in the product repository.

## Hard Rules

```text
1. MCP does not determine who pays for model or image generation.
   The invoked execution surface determines cost ownership.

2. Native ChatGPT generation with no developer API call
   → uses the end user's available ChatGPT capability and plan/workspace limits.

3. Developer-owned OpenAI API call
   → uses the developer's API organization, key, quota, and billing.

4. Never hide a developer-paid model/image call behind a tool described as
   "generate with ChatGPT" or "use the user's quota".

5. If user-account generation is a product requirement, the MCP server prepares
   structured context and hands execution back to the ChatGPT conversation.
   It must not proxy the same generation through a developer API key.

6. One tool owns one clear job. Separate read, write, render, and destructive actions.

7. Business rules stay in the product/application core. MCP handlers and widgets are adapters.

8. User-specific or sensitive data requires explicit auth, least privilege, and privacy review.

9. ChatGPT UI is conversational augmentation, not a web dashboard compressed into an iframe.

10. Apps SDK behavior, publication terminology, and plan availability are volatile.
    Verify current official OpenAI documentation before final architecture or release claims.
```

## Required Classification

Before designing tools or UI, classify the requested product:

```yaml
chatgpt_app:
  lifecycle: product-from-zero | existing-product-feature | migration | review
  primary_value: conversation | connected-data | external-action | structured-workflow
  generation_surface: chatgpt-native | developer-api | external-provider | none
  cost_owner: end-user-chatgpt | developer-api-org | customer-provider-account | mixed
  data_scope: public | anonymous-session | authenticated-user | workspace-sensitive
  ui_mode: text-only | inline | carousel | fullscreen | mixed
  persistence: none | widget-local | product-backend | mixed
  distribution: private-development | workspace | public
```

If `generation_surface` or `cost_owner` is unclear, the architecture is not ready.

## Procedure

### 1. Verify the platform facts

Use current official OpenAI Apps SDK and ChatGPT documentation. Confirm:

- supported MCP transport and server requirements;
- tool/resource metadata and annotations;
- widget bridge and UI resource behavior;
- authentication and protected-resource requirements;
- current testing, deployment, and publication process;
- relevant ChatGPT plan/workspace availability and limits;
- separation between ChatGPT billing and API Platform billing.

Record the retrieval date for release-sensitive decisions.

### 2. Define the product and economic boundary

Produce a capability ownership matrix:

```text
Capability                 Execution surface          Cost/limit owner
MCP tool execution         Product server             App operator
Product database/storage   Product backend            App operator
Native ChatGPT generation  ChatGPT conversation       End user/workspace
OpenAI API generation      Developer API organization Developer
External provider call     Declared provider account  Contract-defined
```

For mixed systems, identify every paid hop. Do not summarize mixed ownership as "user quota".

Load `references/product-and-billing-boundary.md` when generation, subscriptions, credits, or cost ownership matter.

### 3. Design the application boundary

Map responsibilities before code:

```text
ChatGPT conversation
  intent, natural-language control, native capabilities

MCP adapter
  tool discovery, validation, auth context, structured I/O, resource binding

Widget
  focused interaction, presentation state, staged input, follow-up messages

Product application core
  use cases, policy, identity/asset/workflow rules, immutable DTOs

Infrastructure
  persistence, storage, external services, observability
```

No business policy in tool handlers, route handlers, React components, or prompt strings.

### 4. Specify MCP contracts

For each tool define:

- trigger-focused name and description;
- one job and owning module;
- explicit input schema;
- structured output schema;
- read/write/destructive/open-world annotations;
- auth requirement;
- idempotency and retry behavior;
- typed expected failures;
- UI resource binding when rendered;
- audit/observability fields where appropriate.

Prefer data tools and render tools with clear boundaries. Do not create a single `do_everything` tool.

Load `references/mcp-contracts.md` for the contract checklist and patterns.

### 5. Design the conversational UI

Choose the smallest useful UI mode:

```text
text-only   tool result is understandable without interaction
inline      one focused task, summary, or confirmation
carousel    a small set of comparable choices
fullscreen  deeper focused work that still uses the ChatGPT composer
```

Keep the response usable without the widget. Avoid deep navigation, nested scrolling, duplicated composer controls, and dashboard chrome.

Load `references/widget-ux-and-state.md` for UI, state, and native-capability handoff guidance.

### 6. Secure identity, data, and actions

Determine:

- anonymous versus authenticated tools;
- OAuth scopes and least privilege;
- read/write confirmation policy;
- protected-resource metadata;
- CSP and allowed origins;
- prompt-injection and untrusted-content boundaries;
- data retention, deletion, and privacy disclosures;
- secret handling and log redaction.

Load `references/auth-security-and-privacy.md` whenever tools access user data, write external state, upload assets, or use OAuth.

### 7. Map implementation without platform leakage

The product repository owns product-specific adapters and composition. This reusable skill only defines execution behavior and gates.

For a Next.js product, a valid mapping may be:

```text
app/ or route composition       framework entry points
src/modules/<owner>/            product domain/application capability
apps/chatgpt/server/             MCP inbound adapter
apps/chatgpt/widget/             bundled ChatGPT UI
composition roots               concrete wiring
```

The exact folders remain product decisions. Do not force this example over accepted repository architecture.

### 8. Verify and prepare release

Evidence must cover:

- tool discovery and routing;
- schemas, annotations, auth, expected errors, and write confirmation;
- widget rendering and interaction in ChatGPT;
- native generation handoff versus developer API invocation;
- security, privacy, and prompt-injection cases;
- responsive/accessibility behavior;
- observability and failure degradation;
- deployment endpoint and current publication requirements.

Load `references/testing-release-and-submission.md` before claiming integration or release readiness.

## Required Output

```markdown
## ChatGPT App Boundary
- Lifecycle:
- Primary value:
- Generation surface:
- Cost owner:
- Data scope:
- Distribution:

## Capability and Cost Matrix

## MCP Tool Inventory

## UI and State Model

## Auth, Security, and Privacy

## Implementation Mapping

## Verification Plan

## Known Limitations and Volatile Assumptions
```

## Quality Gates

- [ ] Generation surface and cost owner are explicit.
- [ ] No developer API key is used for a capability promised as native user-account generation.
- [ ] ChatGPT and API Platform billing are not conflated.
- [ ] Tool inventory has one job per tool with read/write separation.
- [ ] Tool schemas, annotations, errors, auth, and UI binding are explicit.
- [ ] MCP/widget code is an adapter; business rules remain in the product core.
- [ ] UI mode matches task depth and does not reproduce a dashboard blindly.
- [ ] Critical information remains understandable outside the widget.
- [ ] User-specific data and write actions have least-privilege auth and confirmation policy.
- [ ] Prompt injection, untrusted content, CSP, secrets, logs, and retention are reviewed.
- [ ] Native capability handoff and developer API invocation are tested separately.
- [ ] Current official OpenAI docs were checked before release-sensitive claims.
- [ ] Deployment, observability, failure handling, and publication evidence are recorded.

## Failure Signals

Return `NOT_READY` or route back when:

- cost ownership is inferred rather than verified;
- a tool silently calls a paid model/image API using the developer's credentials;
- native ChatGPT availability is promised for every plan without current evidence;
- one MCP tool mixes reads, writes, rendering, and generation;
- the widget is the only place where critical meaning exists;
- authenticated data is exposed through anonymous tools;
- external content is trusted as instructions;
- publication readiness is claimed from local code or screenshots alone;
- current Apps SDK documentation was not checked for a release-sensitive decision.

## Handoff

```text
product from zero
  → product-development-workflow + chatgpt-app-development

existing product capability
  → new-feature-workflow + chatgpt-app-development

architecture boundary
  → native-ai-engineer + chatgpt-app-development

security-sensitive app
  → threat-modeling + security-review

implemented UI acceptance
  → design-review + accessibility

release/deployment
  → deployment-workflow + observability-design
```
