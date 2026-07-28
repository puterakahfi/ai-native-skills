---
name: workflow-router
description: Detect task intent and route to exactly one governing workflow or standalone capability, including package development, product delivery, feature, bugfix, design, review, deployment, continuity, and verified learning.
license: MIT
metadata:
  ai-native-skills.version: 1.8.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "redesign-workflow design-audit design-refinement design-review brand-identity-review new-feature-workflow package-development-workflow bugfix-workflow code-review-workflow deployment-workflow product-development-workflow delivery-work-breakdown chatgpt-app-development skill-evolution skill-eval git-workflow skill-doctor spec-workflow task-continuity production-code-quality-baseline"
  ai-native-skills.type: meta-skill
  ai-native-skills.implements: ai-native-core/contracts/skills/meta/workflow-router.contract.yaml
  ai-native-skills.contract-version: "~0.2"
  ai-native-skills.related_skills: '["role-switcher","product-development-workflow","delivery-work-breakdown","chatgpt-app-development","package-development-workflow","redesign-workflow","design-audit","design-refinement","design-review","brand-identity-review","skill-evolution","bugfix-workflow","new-feature-workflow","code-review-workflow","deployment-workflow","spec-workflow","task-continuity","production-code-quality-baseline"]'
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

## Core rule

```text
classify requested outcome
→ select exactly one primary lifecycle or standalone capability
→ classify production-code impact
→ attach production-code-quality-baseline when production behavior changes
→ resolve package/platform/domain/design overlays
→ load only material specialists and reviewers
→ execute
```

No execution before routing. Artifact nouns do not determine the lifecycle: a package may be created, extracted, debugged, reviewed, published, or merely inspected.

## Primary routes

| Intent | Primary route | Supporting capabilities |
|---|---|---|
| Build a product from zero | `product-development-workflow` | research, requirements, design, engineering |
| Create/extract/evolve an independently consumable package, library, SDK, adapter, reusable UI, or shared config | `package-development-workflow` | implementation-context discovery, API/architecture/TDD/review skills |
| Audit an existing design without changing it | `design-audit` | `design-review` + applicable domain reviewer |
| Fix known specific design findings while preserving direction | `design-refinement` | prior review, governing reviewer, skill-evolution |
| Change design direction, structure, or multiple layers | `redesign-workflow` | owner, specialists, `design-review` |
| Fix broken implementation behavior | `bugfix-workflow` | production quality, debugging, reviewers |
| Add a product-local capability to an existing product | `new-feature-workflow` | production quality, spec, owners |
| Review code or PR before merge | `code-review-workflow` | architecture/security/design reviewers |
| Deploy or release an existing artifact | `deployment-workflow` | security, architecture, operations |
| Plan or specify | `spec-workflow` | product-manager, plan, relevant owners |
| Preserve or resume work across sessions | `task-continuity` | context-manager, decision-provenance |
| Explore a reversible idea | `spike` | plan, experiment skills |
| Promote a verified lesson | `skill-evolution` | skill-eval, git-workflow |

## Package-development routing

Route to `package-development-workflow` when the requested outcome includes any of:

```text
create or extract a reusable package/library/module
publish or version an SDK/client
separate domain/contracts from provider or framework adapters
build a reusable UI package or shared config
stabilize public exports or SemVer compatibility
prove package installation from a fresh external consumer
migrate a workspace-local package into independent distribution
```

Classification must use intended distribution and ownership, not folder name. A directory under `packages/` may remain a platform-local module.

### Package route takes precedence over generic feature

```text
independently versioned/distributed reusable boundary
  → package-development-workflow

product-local capability with no independent package lifecycle
  → new-feature-workflow
```

Examples:

| Signal | Route |
|---|---|
| “Extract shared auth with Clerk/Auth.js/JWT adapters” | `package-development-workflow` |
| “Create an SDK and manage breaking API compatibility” | `package-development-workflow` |
| “Publish reusable React components with peer dependencies” | `package-development-workflow` |
| “Share ESLint/TypeScript config across independent repos” | `package-development-workflow` |
| “Add login screen and product authorization policy to this app” | `new-feature-workflow` |
| “Fix a regression inside an existing published SDK” | `bugfix-workflow`, preserving package compatibility/publication overlays |
| “Review a package PR before merge” | `code-review-workflow`, using package-development evidence |
| “Publish an already accepted package version” | `deployment-workflow`, preserving immutable package publication gates |

When a candidate is coupled to platform checkout, `workspace:*`, source paths, submodules, Turborepo, framework/provider/database/environment assumptions, or product-specific policy, the package workflow must classify and repair or reject the boundary rather than silently routing back to generic feature work.

## Production-code quality overlay

Production-code quality is an overlay, not a second lifecycle.

```text
new feature, package implementation, bugfix, behavior change, refactor,
migration, or generated code intended for repository submission
  → classify production impact
  → preserve selected primary lifecycle
  → attach production-code-quality-baseline
```

Classification:

```text
PRODUCTION_CODE_CHANGE
NON_PRODUCTION_CHANGE
DISPOSABLE_EXPERIMENT
NOT_VERIFIED
```

`NOT_VERIFIED` blocks complete implementation or merge-readiness claims. Conditional specialists may return `NOT_APPLICABLE` or `NOT_JUSTIFIED`; silence is never PASS.

## Delivery topology overlay

Lifecycle selection does not choose repository topology. Load `delivery-work-breakdown` before Git execution for broad multi-slice capabilities, unresolved base/PR targets, feature-flag exceptions, or dependent release units.

```text
independently releasable slice → verified feature/standalone topology
multiple dependent slices → epic/integration topology
```

Repository default branch, green CI, or mergeability cannot choose the PR target.

## Platform specialist overlays

A platform specialist does not replace the primary lifecycle.

```text
ChatGPT App product from zero → product-development-workflow + chatgpt-app-development
ChatGPT App product-local integration → new-feature-workflow + chatgpt-app-development
Reusable Apps SDK/MCP client or adapter package → package-development-workflow + chatgpt-app-development
Architecture review → architecture-review + relevant platform specialist
Deployment/publication → deployment-workflow + relevant platform specialist
```

## Continuity overlay

`task-continuity` verifies live issue, repository, branch, PR, acceptance, and gate state, then preserves the original governing lifecycle. It never replaces package, feature, bugfix, redesign, review, or deployment ownership.

## Design routing

```text
audit only → design-audit
known targeted finding → design-refinement
broad direction change → redesign-workflow
advisory only → role-switcher + relevant specialist
```

Reusable UI package engineering remains `package-development-workflow`; use design capabilities as specialists/reviewers when its component or visual contract is affected.

## Decision tree

```text
Request
  ↓
Cross-session checkpoint/handoff/resume?
  → task-continuity verifies state; preserve governing lifecycle
  ↓
Verified-case learning required? → skill-evolution
  ↓
Product from zero / no PRD? → product-development-workflow
  ↓
Functional symptom or regression? → bugfix-workflow + production quality
  ↓
Independent reusable package/library/SDK/adapter/UI/config lifecycle?
  → package-development-workflow + production quality when implementing
  ↓
Design-related?
  audit → design-audit
  known fix → design-refinement
  broad change → redesign-workflow
  advisory → role-switcher
  ↓
Product-local new capability? → new-feature-workflow + production quality
  ↓
Code/PR acceptance? → code-review-workflow
  ↓
Deploy/release/publication? → deployment-workflow
  ↓
Plan/spec? → spec-workflow
  ↓
No fit → state fallback and required clarification/evidence
```

## Routing output

```text
Workflow Router
────────────────────────────────────
Request: <normalized request>
Classification: <intent + impact + overlays>
Primary route: <exactly one>
Supporting capabilities: <material only>
Routing rationale: <evidence-based distinction>
Ambiguity resolution: <resolved or blocking unknown>
Execution boundary: <what must happen before work>
Post-fix learning route: <none or skill-evolution subject to authorization>
```

## Anti-patterns

| Anti-pattern | Correct behavior |
|---|---|
| Every reusable module routes to generic feature work | Route independent package lifecycle to `package-development-workflow` |
| Folder named `packages` proves publishability | Classify ownership, portability, distribution, and consumer proof |
| Package build routes directly to deployment success | Preserve compatibility, immutable publication, and fresh-consumer gates |
| A reusable UI package routes only to design | Package lifecycle is primary; design is a specialist/reviewer |
| A package bug routes to package creation lifecycle | Use bugfix workflow and preserve package compatibility evidence |
| One request executes competing primary workflows | Select one lifecycle and explicit handoffs |
| A fresh chat starts from memory | Run task-continuity against current sources first |
| Child work targets default branch automatically | Verify delivery topology and release unit |
| Reviewer selected before lifecycle/domain classification | Resolve route and domain first |
