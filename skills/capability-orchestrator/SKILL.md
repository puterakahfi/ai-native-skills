---
name: capability-orchestrator
description: Compose a routed request into one complete execution graph with an owner, artifact-producing executors, scoped specialists and overlays, reviewers, validators, gates, order, and evidence requirements. Use after workflow-router and role-switcher when an outcome requires multiple capabilities or a produced artifact.
license: MIT
metadata:
  ai-native-skills.version: 0.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: meta-skill
  ai-native-skills.requires: "workflow-router role-switcher decision-provenance"
  ai-native-skills.related_skills: '["workflow-router","role-switcher","product-development-workflow","product-manager","product-requirements","chatgpt-app-development","skill-eval"]'
---

# Capability Orchestrator

Turn an explicit lifecycle route and role composition into a complete, reviewable execution graph.

## Boundary

```text
workflow-router
→ selects exactly one primary lifecycle or standalone route

role-switcher
→ assigns exactly one owner and scoped specialists/reviewers

capability-orchestrator
→ resolves requested artifacts, executors, dependencies, overlays,
  validators, completion gates, execution order, and evidence requirements
```

This meta-skill does not replace routing, lifecycle ownership, role assignment, runtime scheduling, repository authority, or approval.

## Required inputs

```yaml
orchestration_request:
  user_request: string
  workflow_selection: string
  owner: string
  requested_outcomes: []
  requested_artifacts: []
  context:
    lifecycle: string
    domain: string
    platform: string
  catalog_version: string | NOT_VERIFIED
  available_capabilities: []
```

If workflow, owner, requested outcome/artifact, or catalog evidence is missing, return `BLOCKED`, `AMBIGUOUS`, or `NOT_VERIFIED`; do not invent composition.

## Capability roles

Use these orchestration roles without changing the repository's official package types (`skill`, `workflow`, `meta-skill`):

```text
workflow   ordered lifecycle authority
owner      one capability with synthesis and decision authority
executor   capability that produces a requested artifact or outcome
specialist narrow contribution within owner-defined scope
overlay    platform/domain/quality behavior attached conditionally
reviewer   independent evidence review
validator  deterministic contract or gate check
meta       routing or composition behavior
```

Orchestration roles are facets, not new package types.

## Procedure

### 1. Normalize the outcome

Derive and state:

```yaml
normalized_intent:
  action: string
  lifecycle: string
  domain: string
  platform: string
  requested_artifacts: []
```

The artifact noun alone does not choose the lifecycle.

### 2. Preserve the primary route and owner

Require exactly one primary workflow/standalone route and one owner. Platform specialists cannot replace lifecycle ownership.

### 3. Resolve artifact producers

For every requested artifact, select at least one available capability whose declared outputs include that artifact.

Example:

```text
product_requirements_document
→ product-requirements as executor
→ product-manager remains owner
```

Missing producer returns `ARTIFACT_PRODUCER_NOT_FOUND` and blocks equivalent-completion claims.

### 4. Expand dependencies

Expand required dependencies transitively. Activate conditional dependencies only when their declared context matches.

```text
ChatGPT App product requirements
→ product-development-workflow
→ product-manager
→ product-requirements
→ chatgpt-app-development as platform overlay
```

Do not load optional capabilities without a material contribution.

### 5. Add review and validation

Resolve required reviewers and deterministic validators. When independent review is unavailable, set coverage to `LIMITED` or `NOT_VERIFIED`; never infer PASS.

### 6. Validate graph completeness

A graph is `READY` only when:

- exactly one primary route exists;
- exactly one owner exists;
- every requested artifact has a producer;
- all required dependencies are available and compatible;
- no circular dependency exists;
- reviewer and validator obligations are represented;
- completion gates and expected evidence are explicit.

### 7. Order execution

Produce dependency-safe order. Owner synthesis occurs after executor outputs and before required independent acceptance unless the governing workflow declares another order.

### 8. Track capability state

Use only:

```text
DISCOVERED
SELECTED
LOADED
EXECUTING
EXECUTED
REVIEWED
FAILED
BLOCKED
SKIPPED
```

`SELECTED` is not `LOADED`; `LOADED` is not `EXECUTED`; `EXECUTED` is not `REVIEWED`.

### 9. Require evidence-backed execution claims

A capability may be reported as `EXECUTED` only when all applicable evidence exists:

- capability source/version loaded;
- required procedure steps completed;
- observable output produced;
- completion evidence recorded.

Narrative assertion is not execution evidence.

## Required output

```yaml
execution_graph:
  normalized_intent:
    action: string
    lifecycle: string
    domain: string
    platform: string
  primary_workflow:
    id: string
  owner:
    id: string
    reason: string
  executors:
    - id: string
      produces: []
      depends_on: []
  specialists:
    - id: string
      scope: string
      reason: string
  overlays:
    - id: string
      activation_condition: string
  reviewers:
    - id: string
      reviews: []
      independence: VERIFIED | LIMITED | NOT_VERIFIED
  validators: []
  expected_artifacts:
    - id: string
      producer: string
  completion_gates: []
  execution_order: []
  routing_status: READY | LIMITED | BLOCKED | AMBIGUOUS
  errors: []
```

## Typed errors

```text
ROUTING_AMBIGUOUS
PRIMARY_WORKFLOW_NOT_FOUND
MULTIPLE_PRIMARY_WORKFLOWS
OWNER_NOT_FOUND
MULTIPLE_OWNERS
ARTIFACT_PRODUCER_NOT_FOUND
REQUIRED_CAPABILITY_MISSING
CAPABILITY_VERSION_INCOMPATIBLE
CAPABILITY_ROLE_INVALID
CIRCULAR_DEPENDENCY
REQUIRED_REVIEWER_MISSING
REVIEWER_NOT_INDEPENDENT
SKILL_SOURCE_NOT_LOADED
PROCEDURE_NOT_EXECUTED
EXPECTED_ARTIFACT_MISSING
COMPLETION_GATE_FAILED
EVIDENCE_MISSING
```

## Hard gates

- Do not execute before graph completeness is validated.
- Do not represent a flat capability list as a complete execution graph.
- Do not silently substitute generic reasoning for a missing required executor.
- Do not let platform/domain overlays replace the owner or primary lifecycle.
- Do not claim `EXECUTED` or `REVIEWED` without structured evidence.
- Do not promote universal semantics to `ai-native-core` without core authority and review.
