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

The workflow owns lifecycle, state transitions, approvals, preservation, integrity gates, iteration, and handoffs. Specialist skills own narrow design decisions. `master-engineer` owns repository implementation when required. `design-review` and the governing domain reviewer own acceptance.

## Hard rules

```text
1. Route redesign, refinement, and audit-only before production.
2. Declare exactly one design owner.
3. Patch mode requires an implementation owner and one active repository write owner.
4. Material scope, lock, approval, override, status, and ownership claims require decision provenance.
5. Agent summaries, PR bodies, commits, recency, and inference are not owner approval.
6. Capture baseline, confirmed scope, preservation locks, and decision records before patch production.
7. Select specialists from changed layers and acceptance criteria; never load everything by default.
8. Product, audience, content, trust, complexity, context, and existing equity drive direction—not taste labels.
9. Port/profile defaults are not universal workflow rules.
10. Structural copy and content decisions precede layout lock.
11. Every repository write uses an expected-head lease.
12. Inspect head drift before retry; newest commit is not automatically authoritative.
13. Two reversals of the same decision/path stop automatic writes; never ping-pong or force-push.
14. Classify every effective changed path against verified scope.
15. OUT_OF_SCOPE, UNKNOWN, or provenance-blocked changes block passing review and delivery.
16. Verification evidence must match domain, artifact state, changed layers, and delivery boundary.
17. Build success is not design proof; screenshot evidence is not runtime or interaction proof.
18. Acceptance runs only through design-review and the governing domain reviewer.
19. Preserve PASS, FAIL, PARTIAL, NOT_VERIFIED, and NOT_APPLICABLE exactly.
20. Contextual hard gates come from loaded reviewers, not a global UI checklist.
21. Provenance, scope, concurrency, evidence, coverage, and facade verdict all control delivery.
22. Classify root cause and correction ownership before fixing.
23. Maximum design iterations default to 5; after two failed patches in one region, re-read and replan.
24. Verified reusable fixes require skill-evolution and a regression eval.
25. Blocked or bounded attempts are never labeled PASS.
```

## Route

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

Use this workflow for an existing landing page, dashboard, application surface, static campaign, presentation, identity system, or another visual artifact when multiple design layers or the overall direction must change.

Load `references/redesign-vs-refinement.md` before production.

## Required context

```yaml
redesign_input:
  target: <required>
  goal: <outcome>
  design_domain: <digital-interface | visual-communication | presentation | brand-identity | other>
  surface_profile: <profile>
  output_mode: <audit-only | spec-only | prototype | patch>
  approval_mode: <autonomous | spec-gated | patch-gated | fully-gated>
  max_iterations: 5

  baseline_ref: <approved baseline>
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
  preservation_locks: <brand, system, content, asset, behavior, route locks>
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
   inspect complete target, effective diff, equity, content, assets,
   system/framework, concurrent automation, constraints, and evidence gaps

4  DIRECTION
   compare alternatives and select product/brand-appropriate direction

5  LAYERED PLAN
   strategy, foundation, structure, components, expression,
   interaction, content, implementation

6  VALUE ALIGNMENT
   user value, business/delivery value, measurable signals

7  SPEC CONFIRMATION
   verify decisions; lock scope, paths, routes, exclusions, preservation,
   evidence, delegation, ownership, and approvals

8  PRODUCTION
   acquire expected-head lease and produce through selected ports/adapters

9  VERIFICATION
   confirm stable actual head; verify decision provenance, final diff,
   concurrency, domain evidence, preservation, and implementation boundary

10 REVIEW
   design-review facade + governing domain reviewer

11 DEFECT CLASSIFICATION
   governing reviewer or causal owner, evidence, root cause, correction owner

12 FIX
   smallest correct correction under a fresh write lease
   → verify → focused re-review → learning review

13 DELIVERY
   accepted result, approval route, integrity blocker,
   specialist handoff, or bounded gap report
```

## Composition rules

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

Specialists are selected by changed concern:

```text
strategy/content/IA/copy/conversion
  → design-strategy and narrow adapters

visual direction/color/type/depth/iconography/composition/motion
  → design-visual and narrow adapters

macrostructure/responsiveness/component substitution/spacing
  → design-layout and narrow adapters

behavior/pattern/states/accessibility semantics
  → design-interaction and narrow adapters

tokens/theme/system governance
  → design-system and applicable adapters
```

Load `references/delegation-and-verification.md` for the complete matrix.

## Reference map

Load only when applicable:

| Concern | Reference / skill |
|---|---|
| Lifecycle boundary | `references/redesign-vs-refinement.md` |
| State, phase handoffs, approval, outputs | `references/orchestration-state-and-decisions.md` |
| Decision authority and supersession | `decision-provenance` |
| Direction and macrostructure | `references/phase-genre-macro.md` |
| Delegation and domain evidence | `references/delegation-and-verification.md` |
| Production policy | `references/phase-produce.md` |
| Final effective diff | `references/scope-diff-integrity.md` |
| Branch write lease and contention | `references/concurrent-write-integrity.md` |
| Fast visual iteration evidence | `references/visual-loop-verification.md` |
| Facade review | `references/phase-review-gates.md` |
| Defect, fix, and learning | `references/phase-fix-loop.md` |
| Delivery and anti-loop | `references/phase-deliver.md` |

## Integrity before acceptance

Patch or repository-backed delivery must produce:

```text
decision_provenance_report
scope_diff_report
concurrency_report
domain verification evidence
preservation results
implementation checks required by the delivery boundary
```

```text
PROVENANCE_BLOCKED / ROUTE_FOR_APPROVAL
  → preserve last verified decision boundary
  → stop the affected mutation or approval claim

SCOPE_BLOCKED
  → restore, remove, preserve-and-split, or obtain verified bounded approval

CONCURRENT_WRITE_BLOCKED
  → stop writes; coordinate one owner and stable child head

integrity PASS
  → facade acceptance may proceed
```

Visual observations may be recorded while integrity is blocked, but cannot authorize passing delivery.

## Correction loop

```text
design FAIL/PARTIAL
  → canonical gate + governing reviewer + correction owner

NOT_VERIFIED
  → collect evidence or narrow the claim; do not invent a design fix

scope/provenance/concurrency blocker
  → resolve through the owning integrity contract, not a design score

verified reusable correction
  → skill-evolution + skill-eval
```

Apply the smallest valid correction and preserve accepted direction, passing regions, locks, and rollback path.

## Delivery

```text
PASS
  requires provenance, scope, concurrency, acceptance, evidence,
  coverage, reviewer-owned hard gates, and preservation to pass

CONDITIONAL PASS
  allows only explicit non-blocking risk inside verified authority;
  missing approval, contamination, or write contention cannot be accepted as risk

NEEDS WORK / CRITICAL
  fix while bounded attempts remain

LIMITED REVIEW / ROUTE ELSEWHERE
  load reviewer, narrow claim, or hand off

MAX ITERATIONS REACHED
  deliver best preserved attempt with explicit gaps; never label PASS
```

Average score and mergeability never override provenance, scope, concurrency, verdict, coverage, evidence gaps, hard gates, locks, or acceptance criteria.

## Approval boundary

```text
autonomous
  no routine pause, but never inferred consent

spec-gated
  pause when scope or direction materially differs from verified request/spec

patch-gated
  pause before repository patch or full-file rewrite

fully-gated
  pause before production, every patch, and full-file rewrite
```

Always require explicit verified authority for destructive/irreversible work, production-environment changes, user-content deletion, material scope expansion, lock removal, approval bypass, or unresolved owner conflict.

## Final guard

```text
□ Correct lifecycle was selected before production.
□ Design, implementation, repository-write, and review ownership are explicit.
□ Material decisions have attributable sources and verified authority.
□ Agent summaries, PR bodies, commits, and recency were not treated as approval.
□ Baseline, confirmed scope, exclusions, and preservation locks are captured.
□ Specialists match changed layers and acceptance criteria.
□ Production followed delegation and verified decision boundaries.
□ Every write used the inspected expected head; drift was inspected before retry.
□ Two reversals stopped automatic writes.
□ Every effective changed path was classified.
□ OUT_OF_SCOPE, UNKNOWN, and provenance-blocked entries are empty for PASS.
□ Verification matches domain, artifact state, and actual stable head.
□ Review used the facade and governing domain reviewer.
□ PARTIAL, NOT_VERIFIED, and NOT_APPLICABLE were preserved.
□ Integrity reports and facade verdict all control delivery.
□ Every correction followed root-cause ownership classification.
□ Verified reusable fixes received learning review and regression eval.
□ Blocked or bounded attempts are labeled honestly.
```
