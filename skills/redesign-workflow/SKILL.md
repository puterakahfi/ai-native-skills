---
name: redesign-workflow
description: Delegated, domain-aware redesign workflow for existing visual surfaces — route → compose roles → inspect → direct → specify → produce under a write lease → verify scope and artifact → facade review → classify → fix → deliver.
license: MIT
metadata:
  ai-native-skills.version: 3.2.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: workflow
  ai-native-skills.implements: ai-native-core/contracts/skills/quality/redesign-workflow.contract.yaml
  ai-native-skills.contract-version: "^2.2.0"
  ai-native-skills.requires: "role-switcher master-design master-engineer design-foundation design-brand design-visual design-layout design-strategy design-interaction design-system design-audit design-review design-refinement business-value-alignment skill-evolution skill-eval git-workflow"
  ai-native-skills.related_skills: '["workflow-router","adaptive-component-design","macrostructures","ui-components","responsiveness","accessibility","dark-light-theming","brand-identity-review"]'
---

# Redesign Workflow

Redesign an existing visual surface through explicit ownership, bounded delegation, a clean delivery boundary, concurrency-safe writes, fresh evidence, independent review, and a verified correction loop.

The workflow owns lifecycle, state, approvals, preservation, scope integrity, write coordination, iteration, and handoffs. `master-design` or a declared domain owner owns design direction. Specialist ports own narrow decisions. `master-engineer` owns repository implementation when required. `design-review` and the loaded domain reviewer own design acceptance.

## Hard Rules

```text
1. Route before production: redesign, refinement, and audit-only are different lifecycles.
2. Exactly one design owner must be explicit.
3. Patch mode requires an implementation owner distinct from the reviewer.
4. Select specialists from changed layers and acceptance criteria; do not load all skills.
5. Record and re-check brand, content, asset, design-system, behavior, and path locks.
6. Capture baseline and confirmed delivery scope before repository production.
7. Every effective changed path or artifact must be classified before final review.
8. OUT_OF_SCOPE or UNKNOWN changes block passing review and delivery.
9. Capture an expected branch head before every repository mutation.
10. Re-resolve the current head immediately before writing; stale-head writes are forbidden.
11. On head drift, inspect and classify the concurrent delta before any retry.
12. Two reversals of the same decision/path stop automatic writes; never ping-pong or force-push.
13. Product, audience, content, trust, complexity, and existing equity drive direction—not taste.
14. Port or profile defaults are not universal workflow rules.
15. Copy and content that affect structure must be resolved before layout lock.
16. Verify with evidence appropriate to design domain and artifact state.
17. A build is not design verification; a screenshot is not runtime or interaction proof.
18. Review only through the design-review facade and applicable domain reviewer.
19. Preserve PASS, FAIL, PARTIAL, NOT_VERIFIED, and NOT_APPLICABLE exactly.
20. Contextual hard gates come from loaded reviewers, never from a global UI checklist.
21. Scope integrity, concurrency integrity, and facade verdict all control delivery.
22. Classify defect ownership before fixing.
23. Maximum design iterations default to 5; after two failed patches in one region, re-read and replan.
24. Verified reusable fixes require skill-evolution and a regression eval.
25. A bounded or concurrency-blocked attempt is never labeled PASS.
```

## When to Use

Use for an existing landing page, dashboard, application surface, static campaign, presentation, identity system, or other visual artifact when direction, structure, visual language, component model, or multiple design layers must change.

Route elsewhere:

```text
audit only, no production requested
  → design-audit

known narrow verified failures, accepted direction
  → design-refinement

net-new product or route
  → product-development-workflow or new-feature-workflow

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
repository_branch    branch that receives patch-mode writes
expected_head        inspected branch head used as the next write lease
products_in_scope    existing product areas allowed to change
content_inventory    live content to preserve, change, or remove
required_assets      supplied logos, products, people, copy, facts, or sources
audience             target users or viewers
primary_cta          primary action when applicable
viewing_context      viewports, devices, channel, final size, room, theme, inputs
preservation_locks   brand, system, behavior, content, asset, route, and path locks
```

Infer missing values only when evidence is strong and record the assumption. Do not infer permission for unrelated product, route, auth, database, user-data, or infrastructure changes.

## Canonical Flow

```text
0  ROUTE
   redesign | design-refinement | design-audit

1  COMPOSE ROLES
   design owner, implementation owner when needed, specialists,
   reviewer facade, domain reviewer

2  INITIALIZE
   validate input, baseline, confirmed scope, branch, expected head, and run state

3  PREFLIGHT
   inspect target, equity, brand, content, assets, system,
   implementation, current diff, concurrent writers, constraints, evidence gaps

4  DIRECTION
   choose and justify product/brand-appropriate direction and macrostructure

5  LAYERED PLAN
   strategy, foundation, structure, components, expression,
   interaction, content, implementation

6  VALUE ALIGNMENT
   user value, business/delivery value, measurable signals

7  SPEC CONFIRMATION
   lock scope, paths, routes, exclusions, preservation, viewing contexts,
   acceptance criteria, delegation plan, ownership, approval boundary

8  PRODUCTION
   acquire expected-head lease
   verify current head
   produce prototype or patch through delegated ports/adapters

9  VERIFICATION
   confirm final head stability
   collect domain evidence
   generate scope_diff_report and concurrency_report

10 REVIEW
   design-review facade + loaded domain reviewer

11 DEFECT CLASSIFICATION
   governing reviewer or causal owner, root cause, correction owner, evidence

12 FIX
   smallest correct correction under a fresh write lease
   → verify → focused re-review → learning review

13 DELIVERY
   PASS, permitted CONDITIONAL PASS, handoff,
   CONCURRENT_WRITE_BLOCKED, or bounded gap report
```

```text
route
→ compose_roles
→ initialize baseline + scope + expected head
→ preflight
→ direction
→ plan + value + spec
→ production under validated write lease
   ├─ head drift COMPATIBLE → inspect, absorb, renew lease
   ├─ overlapping implementation → reconcile under governing owner
   └─ decision conflict / scope expansion / unknown → stop writes
→ verification + scope diff + concurrency report
   ├─ scope BLOCKED → restore, remove, split, or re-approve dependency
   ├─ concurrency BLOCKED → owner coordination or isolated lifecycle branch
   └─ integrity PASS → facade review
      ├─ PASS / permitted CONDITIONAL PASS → delivery
      ├─ NEEDS WORK / CRITICAL → classify → fix under fresh lease
      ├─ LIMITED REVIEW / ROUTE ELSEWHERE → reviewer or handoff
      └─ max iterations → bounded delivery with gap report
```

## Role Composition

```yaml
role_composition:
  lifecycle_owner: redesign-workflow
  design_owner: master-design
  implementation_owner: null
  specialists: []
  reviewer_facade: design-review
  domain_reviewers: []
  coverage_mode: null
  repository_write_owner: <single writer or coordination owner>
```

```text
output_mode patch or executable production
  → implementation_owner: master-engineer or runtime equivalent
  → exactly one repository_write_owner at a time

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

Load `references/delegation-and-verification.md` for specialist selection, `references/scope-diff-integrity.md` for delivery-boundary validation, and `references/concurrent-write-integrity.md` for branch-write coordination.

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
  baseline_ref: <ref>

repository:
  branch: <branch or null>
  inspected_head: <sha or null>
  expected_head: <sha or null>
  write_owner: <owner or null>
  head_sequence: []
  contention_cycles: 0

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
  routes: []
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
  concurrency_report: null
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
→ scope_blocked | concurrent_write_blocked | reviewing
→ classifying_defect → fixing → accepted → delivered
```

## Phase Responsibilities

### Route and compose

Load `references/redesign-vs-refinement.md`, then `role-switcher` when multiple capabilities or a specialist domain are involved. Emit one route, one role composition, and one repository write owner before production.

### Preflight and direction

Inspect complete available evidence, current effective diff, branch head, and active automation signals. Record brand/product equity, content, audience/task, trust needs, density, interaction complexity, system/framework, assets, constraints, branch contamination, concurrent writers, and evidence gaps.

Direction must compare alternatives and explain rejected options. Load only declared ports/adapters. Do not select genre from one label such as “SaaS” or “creative”.

### Layered plan and value alignment

Each layer is `preserve`, `refine`, `replace`, or `not_applicable`:

```text
strategy | foundation | structure | components | expression |
interaction | content | implementation
```

Run `business-value-alignment` before decorative production. Changes without user, message, delivery, or business value should be narrowed or stopped.

### Spec confirmation

Lock domain, direction, changed/preserved layers, content/assets, viewing contexts, acceptance evidence, delegation owners, baseline, allowed paths/routes/change types, expected outputs/deletions, preserved paths/routes, out-of-scope work, branch write owner, and approval mode.

A new route or feature absent from the approved baseline is a scope expansion unless the spec explicitly approves it.

### Production

Load `references/phase-produce.md`. Produce only through selected ports/adapters and confirmed scope.

Before every repository write:

1. load `concurrent-write-integrity.md`;
2. record `expected_head` and intended paths;
3. resolve current branch head immediately before mutation;
4. write only if heads match;
5. if they differ, inspect the delta and classify it before retry.

Never force-push over an uninspected concurrent commit. Never replay a stale full-file body merely with a refreshed blob SHA.

### Verification

Select evidence by domain, artifact state, changed layers, and delivery boundary. Missing evidence remains `NOT_VERIFIED`.

For patch runs:

- generate `scope_diff_report` from declared baseline to actual current head;
- generate `concurrency_report` proving the artifact and manifest refer to the stable actual head;
- block on out-of-scope/unknown paths, stale manifests, decision conflict, or repeated contention.

### Review

Invoke `design-review` only after delivery-boundary scope and concurrency integrity pass. Visual observations may be recorded earlier, but they cannot authorize merge or passing delivery.

### Defect and fix

Design FAIL/PARTIAL findings use canonical gate, governing reviewer, evidence, defect class, correction owner, and fresh verification.

Scope contamination uses path classification and preservation action. Concurrent conflict uses expected/actual head, delta classification, contention cycles, and coordination action. Neither is scored as a design gate.

Allowed design-defect classes:

```text
reusable_skill_defect
reference_knowledge_defect
workflow_orchestration_defect
local_implementation_defect
product_design_lock_defect
domain_specialist_defect
```

After a verified reusable fix, run `skill-evolution + skill-eval`.

## Concurrency Decisions

```text
COMPATIBLE
  absorb delta, re-run scope/preservation, renew expected-head lease

OVERLAPPING_IMPLEMENTATION
  reconcile one implementation under governing owner, then verify

DECISION_CONFLICT
  stop automatic writes; declare owner or split lifecycle

SCOPE_EXPANSION
  stop automatic writes; route new feature/product work separately

UNKNOWN
  stop and hand off

same decision/path reversed twice
  CONCURRENT_WRITE_BLOCKED
  no third automatic reversal
```

Do not chase a moving child branch with repeated parent submodule-pointer commits. Freeze the child head first.

## Verdict and Delivery

```text
PASS
  requires acceptance, reviewer-owned hard gates, coverage, evidence,
  preservation, scope PASS, and concurrency PASS

CONDITIONAL PASS
  requires scope/concurrency PASS and only explicit non-blocking risks;
  contamination or write contention cannot be accepted as risk

NEEDS WORK / CRITICAL
  classify and fix while bounded attempts remain

LIMITED REVIEW / ROUTE ELSEWHERE
  load reviewer, narrow claim, or hand off

SCOPE BLOCKED
  restore, remove, split, or re-approve dependency

CONCURRENT WRITE BLOCKED
  stop writes, report head drift and conflict, coordinate one owner

MAX ITERATIONS REACHED
  deliver best preserved attempt with gaps; never label PASS
```

Average score and mergeability never override scope, concurrency, verdict, coverage, hard gates, evidence gaps, locks, or acceptance criteria.

Load `references/phase-deliver.md` for reporting.

## Approval Policy

```text
autonomous
  no routine pause; destructive, irreversible, or conflicting writes still stop

spec-gated
  pause when scope or direction materially differs from request

patch-gated
  pause before repository patch or full-file rewrite

fully-gated
  pause before production, every patch, and full-file rewrite
```

Always require explicit approval for destructive, irreversible, production-environment, user-content deletion, material scope-expansion, or unresolved owner-conflict actions.

## Required Outputs

Every routed redesign run exposes:

```text
route_decision
role_composition
delegation_plan
loop_summary
delivery_manifest
```

When applicable:

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
concurrency_report
design_review_result
defect_report
fix_report
learning_review
gap_report
```

## Final Guard

```text
□ Correct lifecycle was selected before production.
□ One design owner, implementation owner, and repository write owner are explicit.
□ Specialists match changed layers.
□ Baseline, allowed paths/routes, exclusions, and locks were recorded.
□ Production followed delegation and confirmed scope.
□ Every effective changed path was classified.
□ OUT_OF_SCOPE, UNKNOWN, and preserved-path violations are empty.
□ Every repository write used the inspected expected head.
□ Head drift was inspected before retry.
□ Two reversals stopped automatic writes.
□ Parent pointers do not chase an unstable child head.
□ Verification matches domain and actual stable head.
□ Review used facade and governing domain reviewer.
□ PARTIAL, NOT_VERIFIED, and NOT_APPLICABLE were preserved.
□ Scope, concurrency, and facade verdict all control delivery.
□ Verified reusable fixes received learning review and regression eval.
□ Blocked or bounded attempts are labeled honestly.
```
