---
name: workflow-router
description: Detect task intent and route to the correct workflow or standalone capability — product-from-zero, design audit, design refinement, redesign, bug, feature, review, deploy, spike, or verified-case skill evolution. Route before execution.
license: MIT
metadata:
  ai-native-skills.version: 1.5.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "redesign-workflow design-audit design-refinement design-review brand-identity-review new-feature-workflow bugfix-workflow code-review-workflow deployment-workflow product-development-workflow delivery-work-breakdown chatgpt-app-development skill-evolution skill-eval git-workflow skill-doctor spec-workflow"
  ai-native-skills.type: meta-skill
  ai-native-skills.implements: ai-native-core/contracts/skills/meta/workflow-router.contract.yaml
  ai-native-skills.contract-version: "~0.2"
  ai-native-skills.related_skills: '["role-switcher","product-development-workflow","delivery-work-breakdown","chatgpt-app-development","redesign-workflow","design-audit","design-refinement","design-review","brand-identity-review","skill-evolution","bugfix-workflow","new-feature-workflow","code-review-workflow","deployment-workflow","spec-workflow"]'
---

# Workflow Router

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/meta/workflow-router.contract.yaml` · compatible line: `~0.2`

```yaml
required_inputs:
- user_request
allowed_outputs:
- workflow_selection
- skill_load_order
- routing_rationale
- ambiguity_resolution
- post_fix_learning_route
quality_gates:
- task_type_must_be_classified_before_workflow_selection
- routing_decision_must_be_stated_explicitly
- ambiguous_requests_must_be_clarified_not_assumed
- selected_workflow_must_be_loaded_before_execution
- no_execution_before_routing_confirmed
- fallback_must_be_defined_when_no_workflow_matches
- product_from_zero_requests_must_not_route_directly_to_implementation
- existing_ui_refinement_requests_must_route_to_redesign_workflow_not_new_surface_workflows
- targeted_design_gate_fixes_must_route_to_design_refinement
- explicit_verified_case_learning_requests_must_route_to_skill_evolution
- parent_workflows_with_verified_fixes_must_route_to_skill_evolution_before_final_delivery
- post_fix_learning_route_must_not_bypass_repository_write_or_approval_policy
```

Start from user_request and return workflow_selection, skill_load_order, routing_rationale, ambiguity_resolution, and post_fix_learning_route. Ambiguity is clarified rather than guessed, and any post-fix learning route remains subject to repository write ownership, expected-head, review, and approval policy.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace repository, runtime, workflow, review, approval, or product evidence.


## Core Rule

```text
classify requested outcome
→ select one primary lifecycle or capability
→ resolve platform/domain overlays
→ resolve design domain when design is involved
→ load only required skills/reviewers
→ execute
```

No execution before routing. The artifact noun does not determine the lifecycle: a dashboard, logo, or ChatGPT App may be audited, refined, redesigned, implemented, or reviewed for release.

## Route Classes

| Intent | Primary route | Supporting capabilities |
|---|---|---|
| Build a product from zero | `product-development-workflow` | research, requirements, design, engineering |
| Audit/critique an existing design without changing it | `design-audit` | `design-review` + applicable domain reviewer |
| Fix known specific design findings while preserving direction | `design-refinement` | prior review, governing reviewer, skill-evolution |
| Change design direction, structure, or multiple layers | `redesign-workflow` | owner, specialists, `design-review` |
| Fix broken implementation behavior | `bugfix-workflow` | systematic-debugging, relevant reviewers |
| Add a capability to an existing product | `new-feature-workflow` | spec, product/design/engineering owners |
| Review code or PR before merge | `code-review-workflow` | architecture/security/design reviewers |
| Deploy or release | `deployment-workflow` | security, architecture, operations |
| Plan or specify | `spec-workflow` | product-manager, plan, relevant owners |
| Explore a reversible idea | `spike` | plan, experiment skills |
| Promote a verified lesson | `skill-evolution` | skill-eval, git-workflow |

## Delivery Topology Overlay

Lifecycle selection does not choose repository topology.

```text
one independently releasable slice
  → delivery-work-breakdown may classify feature or standalone change

multiple dependent slices forming one outcome
  → delivery-work-breakdown
  → release_unit: epic
  → child PRs target the epic/integration branch
  → final epic PR targets the release branch after integrated acceptance
```

Load `delivery-work-breakdown` before Git execution for new apps, broad multi-slice capabilities, epic/feature/task decomposition, feature-flag exceptions, or unresolved base/PR targets. Repository defaults, green CI, and mergeability cannot choose the PR target.

## Platform Specialist Overlays

A platform specialist does not replace the primary lifecycle.

```text
ChatGPT App, Apps SDK, MCP app, or ChatGPT widget
  product from zero       → product-development-workflow + chatgpt-app-development
  existing capability     → new-feature-workflow + chatgpt-app-development
  architecture review     → architecture-review + chatgpt-app-development
  deployment/publication  → deployment-workflow + chatgpt-app-development
```

Load `native-ai-engineer` with `chatgpt-app-development` when the request includes contract ownership, MCP/application boundaries, runtime binding, or product-versus-platform placement.

Do not create a separate ChatGPT App lifecycle merely because the target platform is specialized.

## Design Routing

Design requests require:

```text
lifecycle: audit | refinement | redesign | production | advisory
domain: digital-interface | visual-communication | presentation |
        brand-identity | specialized/other
```

### Audit only

```text
audit, critique, score, evaluate, gap report, production-readiness review
→ design-audit
→ design-review facade
→ applicable built-in or external domain reviewer
```

Audit ends with findings unless production was explicitly requested.

### Targeted refinement

```text
known verified findings
accepted direction
sufficient domain coverage
explicit preservation scope
→ design-refinement
```

When findings are unknown, run `design-audit` first.

### Redesign

```text
replace direction, macrostructure, visual language, concept, or multiple layers
→ redesign-workflow
```

A narrow known problem does not become redesign merely because the user says “polish”.

### Advisory

```text
which component fits, which identity principle applies, explain hierarchy
→ role-switcher + relevant owner/specialists
```

Load `design-review` only when an artifact must be accepted or scored.

## Domain Coverage

```text
digital-interface
  design-review + built-in interactive strategy
  coverage: BUILT_IN

visual-communication
  design-review + built-in static strategy
  coverage: BUILT_IN

presentation
  design-review + built-in presentation strategy
  coverage: BUILT_IN

brand-identity
  design-review + brand-identity-review
  namespace: BI
  coverage: ADAPTER_COVERED when adapter is available
  fallback when unavailable: LIMITED REVIEW

packaging, motion/video, industrial, spatial, fashion, service-design,
or another specialized discipline
  load its declared domain reviewer
  without one: LIMITED REVIEW or route elsewhere
```

Never represent universal visual gates as complete specialist-domain coverage.

## Signal Map

| User signals | Route |
|---|---|
| “audit this landing page”, “review dashboard UX”, “what is wrong with this poster?” | `design-audit` + built-in reviewer |
| “review this logo/identity system” | `design-audit` + `design-review` + `brand-identity-review` |
| “fix BI11 variant drift and preserve the concept” | `design-refinement` + `brand-identity-review` |
| “replace the logo concept and identity direction” | `redesign-workflow` + identity owner; review with `brand-identity-review` |
| “fix I4 tabs overflow” | `design-refinement` + built-in interactive reviewer |
| “redesign this landing page” | `redesign-workflow` |
| “fix login bug”, explicit crash/error | `bugfix-workflow` |
| “add upload feature” | `new-feature-workflow` |
| “review PR/code before merge” | `code-review-workflow` |
| “deploy/release” | `deployment-workflow` |
| “build product from zero” | `product-development-workflow` |
| “build a ChatGPT App from zero with Apps SDK/MCP” | `product-development-workflow` + `chatgpt-app-development` |
| “add ChatGPT App integration to this product” | `new-feature-workflow` + `chatgpt-app-development` |
| “plan/write spec” | `spec-workflow` |

Functional symptom words take precedence over visual-polish words when the requested outcome is a functional fix.

## Decision Tree

```text
Request
  ↓
Verified-case learning required? → skill-evolution
  ↓
Product from zero / no PRD? → product-development-workflow
  ↓
Functional symptom or regression? → bugfix-workflow
  ↓
Design-related?
  audit only              → design-audit
  known targeted finding  → design-refinement
  broad direction change  → redesign-workflow
  advisory only           → role-switcher
  then resolve domain reviewer and coverage
  ↓
New capability? → new-feature-workflow
  multi-slice or target unresolved? → delivery-work-breakdown
  ↓
Code/PR acceptance? → code-review-workflow
  ↓
Deploy/release? → deployment-workflow
  ↓
Plan/spec? → spec-workflow
  ↓
Apply platform specialist overlay when target platform requires it
```

## Routing Output

### ChatGPT App product from zero

```text
Workflow Router
────────────────────────────────────
Request: "Build a ChatGPT App from zero using Apps SDK and MCP"
Classification: PRODUCT FROM ZERO + PLATFORM SPECIALIST

Primary route: product-development-workflow
Platform specialist: chatgpt-app-development
Architecture specialist: native-ai-engineer when boundary design is in scope
Execution boundary: discovery and PRD precede implementation
```

### Identity adapter available

```text
Workflow Router
────────────────────────────────────
Request: "Review whether this logo system is production-ready"
Classification: SPECIALIZED DESIGN AUDIT
Design domain: brand-identity

Primary route: design-audit
Reviewer facade: design-review
Domain reviewer: brand-identity-review
Gate namespace: BI
Coverage: ADAPTER_COVERED
Execution boundary: report only; no redesign
```

### Identity adapter unavailable

```text
Primary route: design-audit
Reviewer facade: design-review
Required reviewer: brand-identity-review
Coverage: LIMITED
Verdict ceiling: LIMITED REVIEW
Handoff: install/load adapter or route to identity specialist
```

## Composition with Role Switcher

`workflow-router` chooses lifecycle and platform/domain overlays. `role-switcher` assigns owner, specialists, facade, and domain reviewer.

```text
identity audit
  lifecycle: design-audit
  owner: declared brand/identity owner
  facade: design-review
  domain reviewer: brand-identity-review

ChatGPT App product
  lifecycle: product-development-workflow | new-feature-workflow
  owner: product-manager | master-engineer according to lifecycle
  platform specialist: chatgpt-app-development
  architecture specialist: native-ai-engineer when relevant
```

The final result is one synthesized lifecycle output, not disconnected reports.

## Automatic Post-Fix Learning

After a real failure, verified fix, and regression evidence:

```text
skill-evolution → skill-eval → git-workflow when promotable and writable
```

## Anti-Patterns

| Anti-pattern | Correct behavior |
|---|---|
| “UX review” automatically routes to redesign | Audit-only routes to design-audit |
| Existing design + narrow failure routes to redesign | Use design-refinement |
| Average score chooses lifecycle | Use intent, direction, root cause, coverage, hard gates |
| Logo audit uses UI/static gates only | Load `brand-identity-review` or return LIMITED REVIEW |
| Identity adapter exists but router ignores it | Route to `brand-identity-review` with BI namespace |
| ChatGPT App target creates a competing primary workflow | Preserve lifecycle and add `chatgpt-app-development` as overlay |
| Child work targets the default branch automatically | Run `delivery-work-breakdown` and preserve the governing release unit |
| One request executes competing primary workflows | Select one lifecycle and explicit handoffs |
| Reviewer selected before domain classification | Resolve lifecycle and domain first |
