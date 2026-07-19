---
name: redesign-workflow
description: Delegated, domain-aware redesign workflow for existing visual surfaces — route → compose owners → verify decisions → inspect → direct → specify → produce under a write lease → verify provenance, scope, concurrency, and artifact → facade review → classify → fix → deliver.
license: MIT
metadata:
  ai-native-skills.version: 3.3.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: workflow
  ai-native-skills.implements: ai-native-core/contracts/skills/quality/redesign-workflow.contract.yaml
  ai-native-skills.contract-version: "^2.2.0"
  ai-native-skills.requires: "role-switcher master-design master-engineer decision-provenance design-foundation design-brand design-visual design-layout design-strategy design-interaction design-system design-audit design-review design-refinement business-value-alignment skill-evolution skill-eval git-workflow"
  ai-native-skills.related_skills: '["workflow-router","adaptive-component-design","macrostructures","ui-components","responsiveness","accessibility","dark-light-theming","brand-identity-review"]'
---

# Redesign Workflow

Redesign an existing visual surface through explicit ownership, verified decision provenance, bounded specialist delegation, clean final-diff scope, concurrency-safe writes, domain-appropriate evidence, independent facade review, and a verified correction loop.

The workflow owns lifecycle, state, approvals, preservation, decision handoffs, scope integrity, write coordination, iteration, and delivery reporting. It does not own specialist design knowledge, repository implementation knowledge, or acceptance gates.

## Hard rules

```text
1. Route redesign, refinement, and audit-only before production.
2. Declare exactly one design owner.
3. Patch mode requires an implementation owner and one active repository write owner.
4. Material scope, lock, approval, override, status, and ownership claims require decision provenance.
5. Agent-authored summaries, PR bodies, commits, and inferences are not owner approval.
6. Capture baseline, confirmed scope, preservation locks, and decision records before patch production.
7. Select specialists from changed layers and acceptance criteria; never load everything by default.
8. Product, audience, content, trust, complexity, context, and existing equity drive direction—not taste labels.
9. Port/profile defaults are not universal workflow rules.
10. Structural copy and content decisions precede layout lock.
11. Every repository write uses an expected-head lease.
12. Head drift must be inspected before retry; newest commit is not automatically authoritative.
13. Two reversals of the same decision/path stop automatic writes; never ping-pong or force-push.
14. Every effective changed path must be classified against verified scope.
15. OUT_OF_SCOPE, UNKNOWN, or provenance-blocked changes block passing review and delivery.
16. Verification evidence must match design domain, artifact state, changed layers, and delivery boundary.
17. Build success is not design proof; screenshot evidence is not runtime or interaction proof.
18. Acceptance runs only through design-review and the governing domain reviewer.
19. Preserve PASS, FAIL, PARTIAL, NOT_VERIFIED, and NOT_APPLICABLE exactly.
20. Contextual hard gates come from loaded reviewers, not a global UI checklist.
21. Decision provenance, scope integrity, concurrency integrity, evidence, coverage, and facade verdict all control delivery.
22. Classify root cause and correction ownership before fixing.
23. Maximum design iterations default to 5; after two failed patches in one region, re-read and replan.
24. Verified reusable fixes require skill-evolution and a regression eval.
25. Blocked or bounded attempts are never labeled PASS.
```

## Routing

Use for an existing landing page, dashboard, application surface, static campaign, presentation, identity system, or other visual artifact when direction, structure, visual language, component model, or multiple design layers must change.

```text
audit only, no production requested
  → design-audit

accepted direction + known narrow verified findings
  → design-refinement

broad direction, structure, concept, or multi-layer change
  → redesign-workflow

net-new product, route, or capability
  → product-development-workflow or new-feature-workflow

non-visual regression
  → bugfix-workflow
```

Load `references/redesign-vs-refinement.md` for boundary detail.

## Inputs

```yaml
redesign_input:
  target: <required URL, screenshot, artifact, repository, or named surface>
  goal: <user, communication, business, or delivery outcome>
  design_domain: <digital-interface | visual-communication | presentation | brand-identity | other>
  surface_profile: <concrete domain profile>
  output_mode: <audit-only | spec-only | prototype | patch>
  approval_mode: <autonomous | spec-gated | patch-gated | fully-gated>
  max_iterations: 5

  baseline_ref: <merge base, approved commit, or original artifact>
  repository_branch: <branch or null>
  expected_head: <inspected head or null>

  decision_sources: []
  required_authorities: []
  previous_decision_records: []

  confirmed_scope:
    products: []
    routes_or_surfaces: []
    allowed_paths: []
    allowed_change_types: []
    expected_generated_files: []
    expected_deletions: []
    preserved_paths: []
    preserved_routes: []
    out_of_scope: []

  content_inventory: []
  required_assets: []
  audience: <audience>
  primary_cta: <action or null>
  viewing_context: []
  preservation_locks:
    brand: []
    design_system: []
    content: []
    assets: []
    behavior: []
    routes: []
```

Infer missing context only when evidence is strong and record the assumption. Never infer permission for adjacent products, routes, auth, database, user-data, infrastructure, destructive work, or approval bypass.

## Canonical flow

```text
0  ROUTE
   redesign | design-refinement | design-audit

1  COMPOSE ROLES
   lifecycle owner, design owner, conditional implementation owner,
   repository write owner, selected specialists, reviewer facade, domain reviewer

2  INITIALIZE
   validate target, baseline, branch, decision sources, scope, locks,
   approval mode, expected head, and durable state

3  PREFLIGHT
   inspect complete target, effective diff, existing equity, content, assets,
   system/framework, concurrent automation, constraints, and evidence gaps

4  DIRECTION
   compare alternatives and select product/brand-appropriate direction

5  LAYERED PLAN
   strategy, foundation, structure, components, expression,
   interaction, content, implementation

6  VALUE ALIGNMENT
   user value, business/delivery value, measurable signals

7  SPEC CONFIRMATION
   verify decision provenance; lock scope, paths, routes, exclusions,
   preservation, viewing contexts, acceptance evidence, delegation, and approvals

8  PRODUCTION
   acquire expected-head lease and produce through selected ports/adapters

9  VERIFICATION
   confirm stable actual head; verify decision provenance, effective final diff,
   concurrency, domain evidence, preservation, and implementation boundary

10 REVIEW
   design-review facade + governing domain reviewer

11 DEFECT CLASSIFICATION
   governing reviewer or causal owner, evidence, root cause, correction owner

12 FIX
   smallest correct correction under a fresh write lease
   → verify → focused re-review → learning review

13 DELIVERY
   accepted result, explicit approval route, integrity blocker,
   specialist handoff, or bounded gap report
```

## Role composition

```yaml
role_composition:
  lifecycle_owner: redesign-workflow
  design_owner: master-design
  implementation_owner: null
  repository_write_owner: null
  decision_authority_owners: []
  specialists: []
  reviewer_facade: design-review
  domain_reviewers: []
  coverage_mode: null
```

```text
patch or executable prototype
  → implementation_owner: master-engineer or runtime equivalent
  → exactly one repository_write_owner at a time

digital-interface
  → built-in interactive reviewer

visual-communication
  → built-in static reviewer

presentation
  → built-in presentation reviewer

brand-identity
  → brand-identity-review when available; otherwise LIMITED/handoff

other
  → declared domain reviewer; otherwise LIMITED/ROUTE_ELSEWHERE
```

Load `references/delegation-and-verification.md` for specialist and evidence selection.

## Durable run state

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
  stable_head: <sha or null>
  write_owner: <owner or null>
  head_sequence: []
  contention_cycles: 0

decisions:
  records: []
  authoritative_record_ids: []
  provenance_verdict: null
  conflicts: []
  unresolved_requirements: []

scope:
  products: []
  routes_or_surfaces: []
  allowed_paths: []
  allowed_change_types: []
  expected_generated_files: []
  expected_deletions: []
  preserved_paths: []
  preserved_routes: []
  out_of_scope: []

roles:
  design_owner: <owner>
  implementation_owner: <owner or null>
  repository_write_owner: <owner or null>
  specialists: []
  reviewer_facade: design-review
  domain_reviewers: []

artifacts:
  route_decision: null
  role_composition: null
  decision_provenance_report: null
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
```

Lifecycle states:

```text
initialized → routed → roles_composed → preflight_complete → direction_selected
→ plan_ready → spec_ready → awaiting_approval → producing → verifying
→ provenance_blocked | scope_blocked | concurrent_write_blocked | reviewing
→ classifying_defect → fixing → accepted → delivered
```

## Phase responsibilities

### Route, compose, initialize

Emit one lifecycle route and one explicit role composition. Capture baseline, branch, expected head, initial decision sources, confirmed scope, locks, and approval requirements before production.

### Preflight, direction, and plan

Inspect complete available evidence, not only the visually interesting region. Direction must compare alternatives and explain why rejected options are less fit. Mark each layer `preserve`, `refine`, `replace`, or `not_applicable`. Run `business-value-alignment` before decorative production.

Load `references/phase-genre-macro.md` for direction detail.

### Spec confirmation

Run `decision-provenance` for every material scope, lock, dependency, override, ownership, or approval claim.

```text
provenance PASS
  → update spec only inside the verified decision boundary

PROVENANCE_BLOCKED
  → preserve last verified scope/lock
  → stop dependent mutation

ROUTE_FOR_APPROVAL
  → pause the affected action and route to required authority
```

A new route or feature absent from the approved baseline remains a scope expansion until a verified authoritative decision explicitly includes it.

### Production

Load `references/phase-produce.md`, `references/concurrent-write-integrity.md`, and the selected design/engineering adapters.

Before every repository mutation:

```text
record expected head + intended paths + governing decision records
→ resolve actual head immediately before write
→ write only when actual == expected
→ on drift, inspect code delta and decision provenance before retry
```

Never force-push over uninspected concurrent work. Never replay a stale full-file body merely with a refreshed blob SHA.

### Verification

Load:

```text
references/scope-diff-integrity.md
references/concurrent-write-integrity.md
references/delegation-and-verification.md
references/visual-loop-verification.md when iterating visual output
```

Patch verification must produce:

```text
decision_provenance_report
scope_diff_report
concurrency_report
domain verification evidence
preservation results
implementation checks required by the delivery boundary
```

All reports must reference the actual stable head or final artifact. Missing evidence remains `NOT_VERIFIED`.

### Review

Load `references/phase-review-gates.md`. Invoke the facade only after applicable provenance, scope, and concurrency integrity pass.

Facade output includes domain, loaded reviewers, canonical gates, evidence coverage, primary-domain coverage, contextual hard gates, verdict, findings, limitations, and handoff.

### Defect, fix, and learning

Load `references/phase-fix-loop.md`.

```text
design FAIL/PARTIAL
  → canonical gate + governing reviewer + correction owner

NOT_VERIFIED
  → return to evidence collection or narrow claim

scope contamination
  → restore, remove, preserve-and-split, or obtain verified bounded approval

provenance conflict
  → stop dependent writes and route explicit supersession/approval

concurrent conflict
  → stop writes, declare one owner, or isolate a real lifecycle boundary
```

Apply the smallest valid correction. After a verified reusable fix, run `skill-evolution + skill-eval`.

### Delivery

Load `references/phase-deliver.md`.

Decision precedence:

```text
PROVENANCE_BLOCKED / ROUTE_FOR_APPROVAL
  → no passing delivery for the affected claim

SCOPE_BLOCKED
  → restore, remove, split, or obtain verified dependency approval

CONCURRENT_WRITE_BLOCKED
  → stop writes and coordinate one owner/stable branch

CRITICAL / NEEDS WORK
  → fix while bounded attempts remain

LIMITED REVIEW / ROUTE ELSEWHERE
  → load reviewer, narrow claim, or hand off

PASS
  → only when provenance, scope, concurrency, acceptance, evidence,
    coverage, reviewer-owned hard gates, and preservation pass

CONDITIONAL PASS
  → only explicit non-blocking risks inside verified authority;
    contamination, missing approval, or write contention cannot be accepted as risk

MAX ITERATIONS REACHED
  → deliver best preserved attempt with explicit gaps; never label PASS
```

Average score and mergeability never override provenance, scope, concurrency, verdict, coverage, evidence gaps, hard gates, locks, or acceptance criteria.

## Approval policy

```text
autonomous
  no routine pause, but it never means inferred consent;
  provenance, destructive, irreversible, policy, or conflicting writes still stop

spec-gated
  pause when scope or direction materially differs from verified request/spec

patch-gated
  pause before repository patch or full-file rewrite

fully-gated
  pause before production, every patch, and full-file rewrite
```

Always require explicit verified authority for destructive/irreversible work, production-environment changes, user-content deletion, material scope expansion, lock removal, approval bypass, or unresolved owner conflict.

## Required outputs

Always expose:

```text
route_decision
role_composition
decision_provenance_report
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

## Final guard

```text
□ Correct lifecycle was selected before production.
□ One design owner, implementation owner, and repository write owner are explicit.
□ Material decisions have attributable sources and verified authority.
□ Agent summaries, PR bodies, commits, and recency were not treated as approval.
□ Supersession and authoritative conflicts are explicit.
□ Baseline, confirmed scope, exclusions, and locks were captured.
□ Specialists match changed layers and acceptance criteria.
□ Production followed delegation and verified decision boundaries.
□ Every repository write used the inspected expected head.
□ Head drift was inspected before retry.
□ Two reversals stopped automatic writes.
□ Every effective changed path was classified.
□ OUT_OF_SCOPE, UNKNOWN, and provenance-blocked entries are empty for PASS.
□ Verification matches domain, artifact state, and actual stable head.
□ Review used the facade and governing domain reviewer.
□ PARTIAL, NOT_VERIFIED, and NOT_APPLICABLE were preserved.
□ Provenance, scope, concurrency, and facade verdict all control delivery.
□ Every correction followed root-cause ownership classification.
□ Verified reusable fixes received learning review and regression eval.
□ Blocked or bounded attempts are labeled honestly.
```
