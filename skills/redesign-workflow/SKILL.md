---
name: redesign-workflow
description: Delegated, domain-aware redesign workflow for existing visual surfaces — route → compose roles → inspect → direct → specify → produce → verify → facade review → classify → fix → deliver.
license: MIT
metadata:
  ai-native-skills.version: 3.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: workflow
  ai-native-skills.implements: ai-native-core/contracts/skills/quality/redesign-workflow.contract.yaml
  ai-native-skills.contract-version: "^2.0.0"
  ai-native-skills.requires: "role-switcher master-design master-engineer design-foundation design-brand design-visual design-layout design-strategy design-interaction design-system design-audit design-review design-refinement business-value-alignment skill-evolution skill-eval"
  ai-native-skills.related_skills: '["workflow-router","adaptive-component-design","macrostructures","ui-components","responsiveness","accessibility","dark-light-theming","brand-identity-review"]'
---

# Redesign Workflow

Redesign an existing visual surface through explicit ownership, bounded delegation, fresh evidence, independent review, and a verified correction loop.

The workflow owns lifecycle, state, approvals, preservation, iteration, and handoffs. `master-design` or a declared domain owner owns design direction. Specialist ports own narrow decisions. `master-engineer` owns repository implementation when required. `design-review` and the loaded domain reviewer own acceptance.

## Hard Rules

```text
1. Route before production: redesign, refinement, and audit-only are different lifecycles.
2. Exactly one design owner must be explicit.
3. Patch mode requires an implementation owner distinct from the reviewer.
4. Select specialists from changed layers and acceptance criteria; do not load all skills.
5. Record and re-check brand, content, asset, design-system, and behavior locks.
6. Product, audience, content, trust, complexity, and existing equity drive direction—not taste.
7. Port or profile defaults are not universal workflow rules.
8. Copy and content that affect structure must be resolved before layout lock.
9. Verify with evidence appropriate to design domain and artifact state.
10. A build is not design verification; a screenshot is not runtime or interaction proof.
11. Review only through the design-review facade and applicable domain reviewer.
12. Preserve PASS, FAIL, PARTIAL, NOT_VERIFIED, and NOT_APPLICABLE exactly.
13. Contextual hard gates come from loaded reviewers, never from a global UI checklist.
14. Facade verdict—not average score alone—controls delivery or correction.
15. Classify defect ownership before fixing.
16. Maximum iterations default to 5; after two failed patches in one region, re-read and replan.
17. Verified reusable fixes require skill-evolution and a regression eval.
18. A bounded best attempt is never labeled PASS.
```

## When to Use

Use for an existing landing page, dashboard, application surface, static campaign, presentation, or other visual artifact when direction, structure, visual language, component model, or multiple design layers must change.

Route elsewhere:

```text
audit only, no production requested
  → design-audit

known narrow verified failures, accepted direction
  → design-refinement

net-new product definition
  → product-development-workflow

non-visual capability
  → new-feature-workflow

general functional regression unrelated to redesign direction
  → bugfix-workflow
```

`audit-only` remains a compatibility input, but it hands off to `design-audit`; this workflow does not silently continue into production.

## Inputs

```text
target              required — URL, screenshot, artifact, repository, or named surface
goal                 user, communication, business, or delivery outcome
design_domain        digital-interface | visual-communication | presentation |
                     brand-identity | other
surface_profile      concrete profile for the selected domain
output_mode          audit-only | spec-only | prototype | patch; default prototype
approval_mode        autonomous | spec-gated | patch-gated | fully-gated
max_iterations       default 5
products_in_scope    existing product areas allowed to change
content_inventory    live content to preserve, change, or remove
required_assets      supplied logos, products, people, copy, facts, or sources
audience             target users or viewers
primary_cta          primary action when applicable
viewing_context      viewports, devices, channel, final size, room, theme, inputs
preservation_locks   brand, design-system, behavior, content, and asset locks
```

Infer missing values only when evidence is strong and record the assumption.

## Canonical Flow

```text
0  ROUTE
   redesign | design-refinement | design-audit

1  COMPOSE ROLES
   design owner, implementation owner when needed, specialists,
   reviewer facade, domain reviewer

2  INITIALIZE
   validate inputs, approval mode, run state, safe output boundary

3  PREFLIGHT
   inspect target, existing equity, brand, content, assets, system,
   implementation, constraints, and evidence gaps

4  DIRECTION
   choose and justify product/brand-appropriate direction and macrostructure

5  LAYERED PLAN
   strategy, foundation, structure, components, expression,
   interaction, content, implementation

6  VALUE ALIGNMENT
   user value, business/delivery value, measurable signals

7  SPEC CONFIRMATION
   lock scope, preservation, viewing contexts, acceptance criteria,
   delegation plan, and approval boundary

8  PRODUCTION
   produce prototype or patch through delegated ports/adapters

9  VERIFICATION
   collect fresh domain-appropriate evidence

10 REVIEW
   design-review facade + loaded domain reviewer

11 DEFECT CLASSIFICATION
   governing reviewer, root cause, correction owner, required evidence

12 FIX
   smallest correct correction → verify → focused re-review → learning review

13 DELIVERY
   PASS, permitted CONDITIONAL PASS, handoff, or bounded gap report
```

```text
route
→ compose_roles
→ initialize
→ preflight
→ direction
→ layered_plan
→ value_alignment
→ spec_confirmation
→ approval when required
→ production
→ verification
→ facade review
   ├─ PASS / permitted CONDITIONAL PASS → delivery
   ├─ NEEDS WORK / CRITICAL + iterations remain → classify → fix → verify
   ├─ LIMITED REVIEW / ROUTE ELSEWHERE → load reviewer, narrow claim, or handoff
   └─ max iterations → bounded delivery with gap report
```

## Role Composition

Before preflight, record:

```yaml
role_composition:
  lifecycle_owner: redesign-workflow
  design_owner: master-design
  implementation_owner: null
  specialists: []
  reviewer_facade: design-review
  domain_reviewers: []
  coverage_mode: null
```

Rules:

```text
output_mode patch or executable production
  → implementation_owner: master-engineer or runtime equivalent

digital-interface
  → built-in interactive reviewer

visual-communication
  → built-in static reviewer

presentation
  → built-in presentation reviewer

brand-identity
  → brand-identity-review when available; otherwise LIMITED or handoff

other
  → declared domain reviewer; otherwise LIMITED or ROUTE_ELSEWHERE
```

Load `references/delegation-and-verification.md` for role, adapter, and verification selection.

## Durable Run State

```yaml
run:
  id: redesign-<id>
  state: initialized
  route: redesign
  iteration: 0
  max_iterations: 5
  output_mode: prototype
  approval_mode: spec-gated

context:
  target: <resolved>
  design_domain: <domain>
  surface_profile: <profile>
  artifact_state: <source-only | rendered-static | rendered-interactive | mixed>
  goal: <goal>
  viewing_context: []

roles:
  design_owner: <owner>
  implementation_owner: <owner or null>
  specialists: []
  reviewer_facade: design-review
  domain_reviewers: []

locks:
  brand: []
  design_system: []
  content: []
  assets: []
  behavior: []
  preserved_regions: []

artifacts:
  route_decision: null
  role_composition: null
  delegation_plan: null
  preflight_report: null
  design_direction: null
  layered_redesign_plan: null
  value_alignment_report: null
  redesign_spec: null
  redesigned_artifact: null
  production_report: null
  verification_report: null
  design_review_result: null
  defect_report: null
  fix_report: null
  learning_review: null
  delivery_manifest: null

review:
  coverage_mode: null
  loaded_reviewers: []
  verdict: null
  evidence_coverage: null
  primary_domain_coverage: null
  hard_gate_status: null
  findings: []
  not_verified: []
  scope_limitations: []
```

Allowed lifecycle states:

```text
initialized → routed → roles_composed → preflight_complete → direction_selected
→ plan_ready → spec_ready → awaiting_approval → producing → verifying
→ reviewing → classifying_defect → fixing → accepted → delivered
```

Failure or bounded states:

```text
validation_failed | production_failed | verification_blocked |
limited_review | routed_elsewhere | max_iterations_reached
```

## Phase Responsibilities

### Route and compose

Load `references/redesign-vs-refinement.md`, then `role-switcher` when multiple capabilities or a specialist domain are involved. Emit one route and one role composition before inspecting production details.

### Preflight and direction

Inspect complete available evidence before choosing direction. Record:

```text
existing brand and product equity
content and information architecture
actual audience and task
trust and conversion requirements
surface density and interaction complexity
current design system and framework
competitive/category expectations when evidence exists
assets and production constraints
preserve/refine/replace candidates
evidence gaps
```

Direction must include considered alternatives and explain why each rejected option is less fit. Load `design-visual`, `design-layout`, and their adapters only for declared concerns. Do not select genre from a single label such as “SaaS” or “creative”.

### Layered plan and value alignment

Each layer is `preserve`, `refine`, `replace`, or `not_applicable`:

```text
strategy
foundation
structure
components
expression
interaction
content
implementation
```

Run `business-value-alignment` before decorative production. A visual change with no user, message, delivery, or business value should be narrowed or stopped.

### Spec confirmation

The spec must lock:

```text
design domain and surface profile
direction and macrostructure rationale
changed and preserved layers
content and asset inventory
viewing contexts and required states
acceptance criteria and required evidence
delegation plan and governing owners
output and approval mode
out-of-scope work
```

### Production

Load `references/phase-produce.md`. Produce only through selected ports/adapters. Do not import fixed scales, breakpoints, CSS motifs, card counts, or component choices as universal workflow policy.

```text
spec-only
  stop after approved spec

prototype
  create a renderable artifact at a safe path

patch
  implementation owner modifies the editable artifact after approval policy passes
```

Preserve the last known good artifact before risky changes.

### Verification

Load `references/delegation-and-verification.md` and `references/visual-loop-verification.md` when iterating. Select evidence by domain, artifact state, changed layers, and delivery boundary. Missing evidence remains `NOT_VERIFIED`.

### Review

Load `references/phase-review-gates.md`. The facade returns:

```text
design domain and loaded reviewers
canonical gate results
coverage mode
evidence coverage
primary-domain coverage
contextual hard-gate status
verdict and prioritized findings
scope limitations and handoff
```

### Defect and fix

For each FAIL or PARTIAL finding:

```yaml
defect:
  canonical_gate_id: <id>
  governing_reviewer: <reviewer>
  observation: <verified condition>
  evidence: []
  impact: <impact>
  affected_region: <region>
  defect_class: <class>
  correction_owner: <owner>
  verification_required: []
```

Allowed classes:

```text
reusable_skill_defect
reference_knowledge_defect
workflow_orchestration_defect
local_implementation_defect
product_design_lock_defect
domain_specialist_defect
```

Load `references/phase-fix-loop.md`. After a verified reusable fix, run `skill-evolution + skill-eval`; do not promote failed or product-specific attempts.

## Verdict and Delivery

```text
PASS
  deliver only when acceptance criteria, contextual hard gates,
  preservation locks, coverage, and required evidence also pass

CONDITIONAL PASS
  deliver only with explicit non-blocking accepted risks inside
  the current approval boundary

NEEDS WORK
  classify and fix while iterations remain

CRITICAL
  block passing delivery; fix or stop

LIMITED REVIEW
  load required reviewer, narrow the claim, or hand off

ROUTE ELSEWHERE
  stop the unsupported approval claim

MAX ITERATIONS REACHED
  deliver the best preserved attempt with explicit gap report;
  never label it PASS
```

Average score may summarize verified applicable gates, but it never overrides verdict, coverage, hard gates, evidence gaps, or acceptance criteria.

Load `references/phase-deliver.md` for final reporting.

## Approval Policy

```text
autonomous
  no routine pause; irreversible or destructive changes still require approval

spec-gated
  pause when proposed scope or direction materially differs from the request

patch-gated
  pause before repository patch or full-file rewrite

fully-gated
  pause before production, each patch, and full-file rewrite
```

Always require explicit approval for destructive, irreversible, production-environment, or user-content deletion actions.

## Required Outputs

Every routed redesign run exposes:

```text
route_decision
role_composition
delegation_plan
loop_summary
delivery_manifest
```

When the corresponding phase runs:

```text
run_state
preflight_report
design_direction
layered_redesign_plan
value_alignment_report
redesign_spec
redesigned_artifact
production_report
verification_report
design_review_result
defect_report
fix_report
learning_review
gap_report
```

## Final Guard

```text
□ Correct lifecycle was selected before production.
□ One design owner and conditional implementation owner are explicit.
□ Specialists match changed layers; unused adapters were not loaded.
□ Preservation locks were recorded and rechecked.
□ Direction is justified by product, brand, audience, content, and context.
□ Production followed the delegation plan.
□ Verification matches domain and artifact state.
□ Review used the facade and governing domain reviewer.
□ PARTIAL, NOT_VERIFIED, and NOT_APPLICABLE were preserved.
□ Contextual hard gates came from loaded reviewers.
□ Facade verdict controls delivery.
□ Every fix followed defect classification.
□ Verified reusable fixes received learning review and regression eval.
□ Bounded attempts are labeled honestly.
```