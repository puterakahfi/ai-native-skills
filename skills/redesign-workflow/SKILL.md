---
name: redesign-workflow
description: Delegated, domain-aware redesign workflow for existing visual surfaces — route → compose roles → inspect → direct → specify → produce → verify scope and artifact → facade review → classify → fix → deliver.
license: MIT
metadata:
  ai-native-skills.version: 3.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: workflow
  ai-native-skills.implements: ai-native-core/contracts/skills/quality/redesign-workflow.contract.yaml
  ai-native-skills.contract-version: "^2.1.0"
  ai-native-skills.requires: "role-switcher master-design master-engineer design-foundation design-brand design-visual design-layout design-strategy design-interaction design-system design-audit design-review design-refinement business-value-alignment skill-evolution skill-eval git-workflow"
  ai-native-skills.related_skills: '["workflow-router","adaptive-component-design","macrostructures","ui-components","responsiveness","accessibility","dark-light-theming","brand-identity-review"]'
---

# Redesign Workflow

Redesign an existing visual surface through explicit ownership, bounded delegation, a clean delivery boundary, fresh evidence, independent review, and a verified correction loop.

The workflow owns lifecycle, state, approvals, preservation, scope integrity, iteration, and handoffs. `master-design` or a declared domain owner owns design direction. Specialist ports own narrow decisions. `master-engineer` owns repository implementation when required. `design-review` and the loaded domain reviewer own design acceptance.

## Hard Rules

```text
1. Route before production: redesign, refinement, and audit-only are different lifecycles.
2. Exactly one design owner must be explicit.
3. Patch mode requires an implementation owner distinct from the reviewer.
4. Select specialists from changed layers and acceptance criteria; do not load all skills.
5. Record and re-check brand, content, asset, design-system, behavior, and path locks.
6. Capture the baseline and confirmed delivery scope before repository production.
7. Every effective changed path or artifact must be classified before final review.
8. OUT_OF_SCOPE or UNKNOWN changes block passing review and delivery.
9. Product, audience, content, trust, complexity, and existing equity drive direction—not taste.
10. Port or profile defaults are not universal workflow rules.
11. Copy and content that affect structure must be resolved before layout lock.
12. Verify with evidence appropriate to design domain and artifact state.
13. A build is not design verification; a screenshot is not runtime or interaction proof.
14. Review only through the design-review facade and applicable domain reviewer.
15. Preserve PASS, FAIL, PARTIAL, NOT_VERIFIED, and NOT_APPLICABLE exactly.
16. Contextual hard gates come from loaded reviewers, never from a global UI checklist.
17. Facade verdict—not average score alone—controls design delivery or correction.
18. Classify defect ownership before fixing.
19. Maximum iterations default to 5; after two failed patches in one region, re-read and replan.
20. Verified reusable fixes require skill-evolution and a regression eval.
21. A bounded best attempt is never labeled PASS.
```

## When to Use

Use for an existing landing page, dashboard, application surface, static campaign, presentation, identity system, or other visual artifact when direction, structure, visual language, component model, or multiple design layers must change.

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
baseline_ref         merge base, approved commit, or original artifact
confirmed_scope      products, routes, paths, change types, expected outputs, exclusions
products_in_scope    existing product areas allowed to change
content_inventory    live content to preserve, change, or remove
required_assets      supplied logos, products, people, copy, facts, or sources
audience             target users or viewers
primary_cta          primary action when applicable
viewing_context      viewports, devices, channel, final size, room, theme, inputs
preservation_locks   brand, system, behavior, content, asset, and path locks
```

Infer missing values only when evidence is strong and record the assumption. Do not infer permission for unrelated product, auth, database, user-data, or infrastructure changes.

## Canonical Flow

```text
0  ROUTE
   redesign | design-refinement | design-audit

1  COMPOSE ROLES
   design owner, implementation owner when needed, specialists,
   reviewer facade, domain reviewer

2  INITIALIZE
   validate input, approval mode, baseline, run state, safe output boundary

3  PREFLIGHT
   inspect target, equity, brand, content, assets, system,
   implementation, constraints, existing diff, and evidence gaps

4  DIRECTION
   choose and justify product/brand-appropriate direction and macrostructure

5  LAYERED PLAN
   strategy, foundation, structure, components, expression,
   interaction, content, implementation

6  VALUE ALIGNMENT
   user value, business/delivery value, measurable signals

7  SPEC CONFIRMATION
   lock scope, paths, exclusions, preservation, viewing contexts,
   acceptance criteria, delegation plan, and approval boundary

8  PRODUCTION
   produce prototype or patch through delegated ports/adapters

9  VERIFICATION
   collect domain evidence and generate scope_diff_report

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
→ initialize baseline and scope
→ preflight
→ direction
→ layered_plan
→ value_alignment
→ spec_confirmation
→ approval when required
→ production
→ verification + scope diff integrity
   ├─ scope BLOCKED → restore, remove, split, or re-approve dependency
   └─ scope PASS → facade review
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
  baseline_ref: <ref or original artifact>

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

scope:
  products: []
  routes_or_surfaces: []
  allowed_paths: []
  allowed_change_types: []
  expected_generated_files: []
  expected_deletions: []
  preserved_paths: []
  out_of_scope: []

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
  scope_diff_report: null
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
→ scope_blocked | reviewing → classifying_defect → fixing → accepted → delivered
```

Failure or bounded states:

```text
validation_failed | production_failed | verification_blocked | scope_blocked |
limited_review | routed_elsewhere | max_iterations_reached
```

## Phase Responsibilities

### Route and compose

Load `references/redesign-vs-refinement.md`, then `role-switcher` when multiple capabilities or a specialist domain are involved. Emit one route and one role composition before inspecting production details.

### Preflight and direction

Inspect the complete available artifact and current effective diff. Record existing brand/product equity, content, audience/task, trust and conversion needs, density, interaction complexity, system/framework, assets, constraints, preserve/refine/replace candidates, branch contamination already present, and evidence gaps.

Direction must compare alternatives and explain why rejected options are less fit. Load `design-visual`, `design-layout`, and adapters only for declared concerns. Do not select genre from a single label such as “SaaS” or “creative”.

### Layered plan and value alignment

Each layer is `preserve`, `refine`, `replace`, or `not_applicable`:

```text
strategy | foundation | structure | components | expression |
interaction | content | implementation
```

Run `business-value-alignment` before decorative production. A visual change with no user, message, delivery, or business value should be narrowed or stopped.

### Spec confirmation

Lock:

```text
design domain and surface profile
direction and macrostructure rationale
changed and preserved layers
content and asset inventory
viewing contexts and required states
acceptance criteria and required evidence
delegation plan and governing owners
baseline ref and allowed paths/change types
expected generated files and deletions
preserved paths and explicit out-of-scope work
output and approval mode
```

### Production

Load `references/phase-produce.md`. Produce only through selected ports/adapters and within confirmed scope. Do not import fixed scales, breakpoints, CSS motifs, card counts, or component choices as universal workflow policy.

```text
spec-only  → stop after approved spec
prototype  → create a renderable artifact at a safe path
patch      → implementation owner modifies approved paths after approval policy passes
```

A newly required dependency outside the spec must be justified and re-enter approval policy. Preserve the last known good artifact before risky changes.

### Verification

Load `references/delegation-and-verification.md` and `references/visual-loop-verification.md` when iterating. Select evidence by domain, artifact state, changed layers, and delivery boundary. Missing evidence remains `NOT_VERIFIED`.

For patch runs, load `references/scope-diff-integrity.md` and generate `scope_diff_report` from the declared baseline to the current target. Every changed path must be classified. `OUT_OF_SCOPE`, `UNKNOWN`, or preserved-path violations block passing review and delivery until restored, removed, split, or explicitly re-approved as a required dependency.

### Review

Load `references/phase-review-gates.md` only after scope integrity passes for the delivery boundary. The facade returns design domain, loaded reviewers, canonical gate results, coverage, contextual hard-gate status, verdict, findings, limitations, and handoff.

A visual review may be recorded while scope is blocked, but it cannot authorize merge or passing delivery.

### Defect and fix

For each FAIL or PARTIAL design finding, record canonical gate, governing reviewer, evidence, impact, region, defect class, correction owner, and required verification.

For scope contamination, record changed path, classification, causal owner, required preservation action, and whether it must be restored, removed, split, or re-approved. Scope contamination is a workflow blocker, not a design score of zero.

Allowed design-defect classes:

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
  preservation locks, domain coverage, required evidence,
  and scope_diff_report also pass

CONDITIONAL PASS
  deliver only with explicit non-blocking accepted risks inside
  the approval boundary; scope contamination cannot be accepted as risk

NEEDS WORK
  classify and fix while iterations remain

CRITICAL
  block passing delivery; fix or stop

LIMITED REVIEW
  load required reviewer, narrow the claim, or hand off

ROUTE ELSEWHERE
  stop the unsupported approval claim

SCOPE BLOCKED
  restore, remove, split, or explicitly re-approve required dependencies

MAX ITERATIONS REACHED
  deliver the best preserved attempt with explicit gap report;
  never label it PASS
```

Average score may summarize verified applicable design gates, but it never overrides scope integrity, verdict, coverage, hard gates, evidence gaps, locks, or acceptance criteria.

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

Always require explicit approval for destructive, irreversible, production-environment, user-content deletion, or material scope-expansion actions.

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
scope_diff_report
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
□ Baseline, confirmed paths, exclusions, and preservation locks were recorded.
□ Direction is justified by product, brand, audience, content, and context.
□ Production followed the delegation plan and confirmed scope.
□ Every effective changed path or artifact was classified.
□ OUT_OF_SCOPE, UNKNOWN, and preserved-path violations are empty.
□ Verification matches domain and artifact state.
□ Review used the facade and governing domain reviewer.
□ PARTIAL, NOT_VERIFIED, and NOT_APPLICABLE were preserved.
□ Contextual hard gates came from loaded reviewers.
□ Scope integrity and facade verdict both control delivery.
□ Every fix followed defect classification.
□ Verified reusable fixes received learning review and regression eval.
□ Bounded attempts are labeled honestly.
```
