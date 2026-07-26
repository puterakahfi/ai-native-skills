---
name: workflow-router
description: Detect task intent and route to the correct workflow or standalone capability — product-from-zero, commercial creative production, product-image preparation, design audit, design refinement, redesign, bug, feature, review, deploy, spike, verified-case skill evolution, or cross-session task continuity. Route before execution.
license: MIT
metadata:
  ai-native-skills.version: 1.7.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "commercial-creative-production product-image-production redesign-workflow design-audit design-refinement design-review brand-identity-review new-feature-workflow bugfix-workflow code-review-workflow deployment-workflow product-development-workflow delivery-work-breakdown chatgpt-app-development skill-evolution skill-eval git-workflow skill-doctor spec-workflow task-continuity"
  ai-native-skills.type: meta-skill
  ai-native-skills.implements: ai-native-core/contracts/skills/meta/workflow-router.contract.yaml
  ai-native-skills.contract-version: "~0.2"
  ai-native-skills.related_skills: '["role-switcher","commercial-creative-production","product-image-production","product-development-workflow","delivery-work-breakdown","chatgpt-app-development","redesign-workflow","design-audit","design-refinement","design-review","brand-identity-review","skill-evolution","bugfix-workflow","new-feature-workflow","code-review-workflow","deployment-workflow","spec-workflow","task-continuity"]'
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

Start from `user_request` and return `workflow_selection`, `skill_load_order`, `routing_rationale`, `ambiguity_resolution`, and `post_fix_learning_route`. Ambiguity is clarified rather than guessed, and post-fix learning remains subject to repository write ownership, expected-head, review, and approval policy.

Keep this interface synchronized with the pinned core contract. Executable routing may add evidence-backed route classes without claiming a newer canonical interface.

## Core rule

```text
classify requested outcome
→ choose exactly one primary lifecycle or standalone capability
→ resolve continuity, platform, delivery-topology, and domain overlays
→ compose one owner, narrow specialists, and applicable reviewers
→ load only required capabilities
→ execute
```

No execution before routing. The artifact noun does not determine the lifecycle: a dashboard, logo, product photo, banner, or ChatGPT App may be audited, prepared, refined, redesigned, produced, implemented, or reviewed.

## Route classes

| Intent | Primary route | Supporting capabilities |
|---|---|---|
| Build a product from zero | `product-development-workflow` | research, requirements, design, engineering |
| Create a new commercial catalog, marketplace image, flyer, poster, banner, social ad, or campaign creative | `commercial-creative-production` | `product-image-production` when needed, `master-design`, `design-visual`, provider adapter, `design-review` |
| Prepare one product image, cutout, retouch, restore, normalize, or create a reusable Product Asset Master | standalone `product-image-production` | provider adapter when executing; `design-review` when acceptance is requested |
| Audit/critique an existing design without changing it | `design-audit` | `design-review` + applicable domain reviewer |
| Fix known specific design findings while preserving direction | `design-refinement` | causal specialist, prior review, governing reviewer, skill-evolution |
| Change design direction, structure, concept, or multiple layers of an existing artifact | `redesign-workflow` | owner, narrow specialists, `design-review` |
| Fix broken implementation behavior | `bugfix-workflow` | systematic-debugging, relevant reviewers |
| Add a capability to an existing product | `new-feature-workflow` | spec, product/design/engineering owners |
| Review code or PR before merge | `code-review-workflow` | architecture/security/design reviewers |
| Deploy or release | `deployment-workflow` | security, architecture, operations |
| Plan or specify | `spec-workflow` | product-manager, plan, relevant owners |
| Preserve or resume work across sessions or runtimes | `task-continuity` overlay | `context-manager`, `decision-provenance`, preserved lifecycle |
| Explore a reversible idea | `spike` | plan, experiment skills |
| Promote a verified lesson | `skill-evolution` | skill-eval, git-workflow |

## Commercial creative routing boundary

```text
one product source → reusable asset only
→ product-image-production

new commercial artifact from raw or prepared assets
→ commercial-creative-production

provider-specific image prompt/edit translation only
→ prompt-engineer

existing commercial artifact, broad direction replacement
→ redesign-workflow

existing artifact, known narrow defect and preservation scope
→ design-refinement + causal specialist

existing artifact, findings only
→ design-audit + design-review

final export acceptance only
→ design-review + built-in static-visual strategy
```

Hard routing rule:

```text
raw or unverified product source + preparation required
→ product-image-production before final commercial composition
```

Do not route raw product imagery directly to `master-design`, `design-visual`, or a provider prompt.

A verified destination-compatible Product Asset Master may bypass reprocessing and hand off directly to the commercial workflow.

## Delivery topology overlay

Lifecycle selection does not choose repository topology.

```text
one independently releasable slice
→ delivery-work-breakdown may classify feature or standalone change

multiple dependent slices forming one outcome
→ delivery-work-breakdown
→ release_unit: epic
→ parent epic and child work items
→ child PRs target the epic/integration branch
→ final epic PR targets the release branch after integrated acceptance
```

Load `delivery-work-breakdown` before repository execution for new apps, broad multi-slice capabilities, unresolved base/PR targets, feature-flag exceptions, or dependent work. Repository defaults, green CI, and mergeability cannot choose the PR target.

## Platform specialist overlays

A platform specialist does not replace the primary lifecycle.

```text
ChatGPT App, Apps SDK, MCP app, or ChatGPT widget
  product from zero       → product-development-workflow + chatgpt-app-development
  existing capability     → new-feature-workflow + chatgpt-app-development
  architecture review     → architecture-review + chatgpt-app-development
  deployment/publication  → deployment-workflow + chatgpt-app-development
```

Load `native-ai-engineer` when contract ownership, MCP/application boundaries, runtime binding, or product-versus-platform placement is in scope.

Do not create `chatgpt-app-workflow` merely because the target platform is specialized.

## Continuity overlay

Cross-session continuity verifies state; it does not replace the governing lifecycle.

```text
checkpoint or handoff only
→ task-continuity

resume feature implementation
→ task-continuity validates authoritative sources
→ new-feature-workflow remains primary

resume bugfix, redesign, commercial production, review, or deployment
→ task-continuity performs continuity validation
→ preserve the governing lifecycle
```

No execution before resume verdict. Do not continue from memory when current issue, branch, PR, acceptance, or gate state can be verified.

## Design routing

Design requests require:

```text
lifecycle: audit | refinement | redesign | production | advisory | acceptance

domain: digital-interface | visual-communication | presentation |
        brand-identity | specialized/other
```

### Audit only

```text
audit, critique, score, evaluate, gap report, production-readiness review
→ DESIGN AUDIT
→ design-audit
→ design-review facade
→ applicable built-in or external domain reviewer
→ report only
```

Audit ends with findings unless production was explicitly requested.

### Targeted refinement

```text
known verified finding
+ accepted direction
+ explicit preservation scope
+ sufficient causal ownership
→ design-refinement
→ targeted correction
→ preserve unaffected layers
```

When findings are unknown, run `design-audit` first.

A known product-mask, halo, clipping, color, or source-fidelity defect may load `product-image-production` as the causal specialist without changing the refinement lifecycle.

### Redesign

```text
existing artifact
+ replace direction, macrostructure, visual language, concept, or multiple layers
→ redesign-workflow
```

A narrow known problem does not become redesign merely because the user says “polish”.

### Production

```text
new commercial static artifact
+ brief/raw or prepared assets
+ exported deliverable expected
→ commercial-creative-production
```

Within production:

- standalone asset preparation remains `product-image-production`;
- raw product sources load Product Image Production before composition;
- verified Product Asset Masters are reused within approved destinations;
- prompt translation remains a supporting capability;
- acceptance remains with `design-review`.

### Advisory

```text
which component fits, which identity principle applies, explain hierarchy,
explain whether a source is suitable without producing or accepting an artifact
→ role-switcher + relevant owner/specialist
```

Load `design-review` only when an artifact must be accepted or scored.

### Acceptance only

```text
export already exists + user asks whether it passes
→ design-review + applicable domain strategy
```

Acceptance-only work does not reopen production unless a finding is accepted for correction.

## Domain coverage

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
  coverage: ADAPTER_COVERED when available
  fallback: LIMITED REVIEW

packaging, motion/video, industrial, spatial, fashion, service-design,
or another specialized discipline
  load its declared domain reviewer
  without one: LIMITED REVIEW or route elsewhere
```

Universal visual gates do not prove complete specialist-domain coverage.

## Signal map

| User signals | Route |
|---|---|
| “create a new Instagram ad/flyer/banner/catalog from these raw product photos” | `commercial-creative-production` + `product-image-production` before design |
| “use this approved Product Asset Master in a new marketplace banner” | `commercial-creative-production`; reuse approved master |
| “remove the background and give me a transparent product PNG” | standalone `product-image-production` |
| “translate this approved edit plan into an image-model prompt” | `prompt-engineer` |
| “audit this landing page”, “review dashboard UX”, “what is wrong with this poster?” | `design-audit` + built-in reviewer |
| “review this logo/identity system” | `design-audit` + `design-review` + `brand-identity-review` |
| “fix BI11 variant drift and preserve the concept” | `design-refinement` + `brand-identity-review` |
| “replace the logo concept and identity direction” | `redesign-workflow` + identity owner |
| “fix I4 tabs overflow” | `design-refinement` + built-in interactive reviewer |
| “fix only the dark-background halo on this approved transparent asset” | `design-refinement` + `product-image-production` |
| “redesign this existing landing page/poster/campaign” | `redesign-workflow` |
| “fix login bug”, explicit crash/error | `bugfix-workflow` |
| “add upload feature” | `new-feature-workflow` |
| “review PR/code before merge” | `code-review-workflow` |
| “deploy/release” | `deployment-workflow` |
| “build product from zero” | `product-development-workflow` |
| “build a ChatGPT App from zero with Apps SDK/MCP” | `product-development-workflow` + platform specialist `chatgpt-app-development` |
| “add ChatGPT App integration to this product” | `new-feature-workflow` + platform specialist `chatgpt-app-development` |
| “plan/write spec” | `spec-workflow` |
| “continue this in a new chat”, “prepare a handoff”, “resume the previous task” | `task-continuity` before the preserved governing lifecycle |

Functional symptom words take precedence over visual-polish words when the requested outcome is a functional fix.

## Decision tree

```text
Request
  ↓
Cross-session checkpoint, handoff, or resume?
  → task-continuity verifies authoritative sources
  → preserve original governing lifecycle
  → no execution before resume verdict
  ↓
Verified-case learning required? → skill-evolution
  ↓
Product from zero / no PRD? → product-development-workflow
  ↓
Functional symptom or regression? → bugfix-workflow
  ↓
Design or commercial visual work?
  audit only                       → design-audit
  acceptance only                  → design-review
  known targeted existing defect   → design-refinement
  existing broad direction change  → redesign-workflow
  one product asset only           → product-image-production
  new commercial static artifact   → commercial-creative-production
  advisory only                    → role-switcher
  then resolve domain reviewer and coverage
  ↓
New product capability? → new-feature-workflow
  multi-slice or target unresolved? → delivery-work-breakdown
  ↓
Code/PR acceptance? → code-review-workflow
  ↓
Deploy/release? → deployment-workflow
  ↓
Plan/spec? → spec-workflow
  ↓
Apply platform specialist overlay when required
```

## Routing output contract

```yaml
workflow_selection:
  classification:
  primary_route:
  overlays: []
  design_lifecycle: <audit | refinement | redesign | production | advisory | acceptance | not_applicable>
  design_domain: <domain or not_applicable>
  standalone_capability: <capability or null>
  reviewer_facade: <reviewer or null>
  domain_reviewer: <reviewer or null>

skill_load_order: []
routing_rationale: []
ambiguity_resolution:
  unresolved: []
  clarification_or_safe_fallback:
post_fix_learning_route:
  required: <true | false | not_verified>
  route: <skill-evolution | local_only | null>
  repository_and_approval_policy_preserved: true
```

## Examples

### New commercial ad from raw product photo

```text
Workflow Router
────────────────────────────────────
Classification: NET-NEW COMMERCIAL STATIC PRODUCTION
Primary route: commercial-creative-production
Asset specialist: product-image-production
Design owner: master-design
Reviewer: design-review + built-in static strategy
Execution boundary: raw source must reach an approved Product Asset Master before final composition
```

### Standalone transparent product asset

```text
Classification: STANDALONE PRODUCT IMAGE PRODUCTION
Primary capability: product-image-production
Commercial workflow: not loaded
Reviewer: design-review only when acceptance is requested
```

### Cross-session feature resume

```text
Continuity overlay: task-continuity
Evidence: authoritative sources and continuity validation
Primary lifecycle after VALID resume: new-feature-workflow
Rule: preserve the governing lifecycle; no execution before resume verdict
```

### ChatGPT App product from zero

```text
Classification: PRODUCT FROM ZERO + PLATFORM SPECIALIST
Primary route: product-development-workflow
Platform specialist: chatgpt-app-development
Architecture specialist: native-ai-engineer when boundaries are in scope
Execution boundary: discovery and PRD precede implementation
```

### Identity adapter available

```text
Classification: SPECIALIZED DESIGN AUDIT
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
Required reviewer: brand-identity-review
Coverage: LIMITED
Verdict ceiling: LIMITED REVIEW
Do not fall back to built-in interactive gates.
```

## Executable quality gates

```text
route_before_execution
exactly_one_primary_lifecycle_or_capability
artifact_noun_does_not_override_lifecycle
commercial_production_is_distinguished_from_asset_preparation_prompt_audit_refinement_and_redesign
raw_product_source_cannot_bypass_required_product_image_production
verified_Product_Asset_Master_can_be_reused_without_unnecessary_reprocessing
platform_specialist_does_not_replace_lifecycle
continuity_overlay_preserves_governing_lifecycle
release_unit_is_classified_before_repository_execution
reviewer_and_domain_coverage_are_explicit
ambiguous_requests_must_be_clarified_not_assumed
post_fix_learning_route_must_not_bypass_repository_write_or_approval_policy
```

## Anti-patterns

```text
❌ Route every product-photo request to final design.
❌ Route every banner request to commercial production without checking whether it is audit, refinement, or redesign.
❌ Let prompt-engineer become product-fidelity owner.
❌ Reprocess a verified Product Asset Master without a destination change or discovered defect.
❌ Replace a governing lifecycle with task-continuity or a platform specialist.
❌ Choose PR topology from the default branch or CI state.
❌ Treat missing specialist reviewer coverage as PASS.
❌ Start implementation before routing, scope, and ambiguity are resolved.
```

## Final guard

```text
□ Task type is classified before workflow selection.
□ Exactly one primary lifecycle or standalone capability is explicit.
□ Commercial production boundaries are resolved before design execution.
□ Raw product sources cannot bypass required preparation.
□ Platform, continuity, topology, and domain overlays do not replace the lifecycle.
□ Owner, specialists, reviewer facade, and domain coverage are explicit when applicable.
□ Skill load order matches the selected route.
□ Ambiguity and fallback are recorded.
□ Repository write and approval policies remain intact.
□ No execution occurred before routing was confirmed.
```
