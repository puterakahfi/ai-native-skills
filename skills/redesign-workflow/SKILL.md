---
name: redesign-workflow
description: Delegated, domain-aware redesign workflow for existing visual surfaces — route → compose owners → verify decisions → inspect → direct → specify → map repository implementation context → produce under a write lease → verify provenance, scope, conventions, concurrency, and artifact → facade review → classify → fix → deliver.
license: MIT
metadata:
  ai-native-skills.version: 3.5.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: workflow
  ai-native-skills.implements: ai-native-core/contracts/skills/quality/redesign-workflow.contract.yaml
  ai-native-skills.contract-version: ^2.2.0
  ai-native-skills.boundary.covers: '["existing_visual_surface_redesign","redesign_vs_refinement_vs_audit_routing","explicit_design_implementation_and_repository_write_ownership","confirmed_scope_and_baseline_capture","final_effective_diff_integrity","concurrent_branch_write_detection_and_coordination","brand_content_asset_behavior_route_and_path_preservation","direction_macrostructure_and_layered_change_planning","user_and_business_value_alignment","delegated_design_and_implementation_work","prototype_or_repository_patch_production","domain_appropriate_verification","design_review_facade_acceptance","bounded_fix_iterations_and_learning_promotion","passing_delivery_or_honest_blocker_reporting"]'
  ai-native-skills.boundary.delegates: '["net_new_product_definition","audit_only_work_after_route_handoff","known_narrow_refinement_after_route_handoff","non_visual_feature_development","unrelated_product_route_auth_data_or_infrastructure_changes","general_bugfix_workflow","deployment_or_publishing","legal_trademark_clearance","force_overwrite_of_uninspected_concurrent_work","destructive_repository_operations_without_approval"]'
  ai-native-skills.pack: packs/redesign/pack.yaml
  ai-native-skills.pack-version: "1.1.0"
  ai-native-skills.requires: "role-switcher master-design master-engineer implementation-context-discovery business-value-alignment decision-provenance design-foundation design-brand design-visual design-layout design-strategy design-interaction design-system design-audit design-review design-refinement skill-evolution skill-eval git-workflow"
  ai-native-skills.related_skills: '["workflow-router","architecture-review","adaptive-component-design","macrostructures","ui-components","responsiveness","accessibility","dark-light-theming","brand-identity-review"]'
---

# Redesign Workflow

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/quality/redesign-workflow.contract.yaml` · compatible line: `^2.2.0`

```yaml
required_inputs:
- target
allowed_outputs: []
quality_gates:
- lifecycle_route_resolved_before_production
- exactly_one_design_owner_is_explicit
- implementation_owner_is_explicit_when_patching
- exactly_one_repository_write_owner_is_active
- specialists_are_selected_from_declared_changed_layers
- baseline_and_confirmed_scope_are_recorded_before_patch_production
- preservation_locks_are_recorded_and_rechecked
- production_follows_declared_delegation_plan
- production_remains_inside_confirmed_scope
- every_repository_write_uses_expected_head_lease
- head_drift_is_inspected_before_retry
- repeated_decision_reversal_stops_automatic_writes
- parent_pointer_does_not_chase_unstable_child_head
- verification_strategy_matches_primary_design_domain_and_artifact_state
- final_effective_diff_must_match_confirmed_scope
- every_changed_path_must_be_classified
- scope_contamination_blocks_review_and_delivery
- concurrency_block_is_not_reported_as_pass
- review_uses_design_review_facade_and_loaded_domain_reviewer
- gate_statuses_preserve_partial_not_verified_and_not_applicable
- contextual_hard_gates_are_reviewer_owned
- facade_scope_and_concurrency_control_delivery
- defect_classification_precedes_fix
- verified_reusable_fixes_run_learning_review_and_regression_eval
- max_iteration_delivery_is_not_labeled_as_passed
```

A parent repository pointer may move only after the child repository has a stable reviewed commit. Do not make the parent chase an uncommitted worktree, transient child head, failed validation state, or head that may still be rewritten; preserve expected-head leases and re-inspect drift before retry.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace repository, runtime, workflow, review, approval, or product evidence.

Redesign an existing visual surface through explicit ownership, verified decision provenance, bounded specialist delegation, repository-consistent implementation mapping, clean final-diff scope, concurrency-safe writes, domain-appropriate evidence, independent facade and architecture review, and a verified correction loop.

The workflow owns lifecycle, state transitions, approvals, preservation, integrity gates, iteration, and handoffs. Specialist skills own narrow design decisions. `implementation-context-discovery` owns the pre-code repository implementation map. `master-engineer` owns implementation. `architecture-review`, `design-review`, and the governing domain reviewer own acceptance in their domains.

It routes net-new product definition, audit-only work, known narrow refinements, non-visual feature development, and general bug fixes to their owning workflows. It does not own unrelated product/route/auth/data/infrastructure changes, deployment or publishing, legal or trademark clearance, force-overwriting uninspected concurrent work, or destructive repository operations without approval.

## Dependency and installation model

Runtime composition and package installation are separate concerns.

```text
ai-native-skills.requires
  → backward-compatible runtime capability hint
  → does not prove dependencies are installed

ai-native-skills.pack + ai-native-skills.pack-version
  → bind this workflow version to one canonical manifest contract

packs/redesign/pack.yaml
  → canonical ordered dependency inventory
  → classifies required, conditional, port, adapter, domain-reviewer, and optional skills
  → defines minimum and complete installation profiles
  → governs the documented Redesign Pack command
```

Installing `redesign-workflow` alone installs only the entrypoint because the upstream skills CLI does not currently resolve transitive dependencies from `SKILL.md`. Before execution, verify required capability availability, resolve conditional capabilities from the run context, and select adapters only from changed concerns and acceptance criteria.

Load `references/dependencies-and-installation.md` for the complete dependency contract, installation profiles, runtime preflight, and validation commands.

## Hard rules

```text
1. Route redesign, refinement, and audit-only before production.
2. Declare exactly one design owner.
3. Patch mode requires an implementation owner and one active repository write owner.
4. Material scope, lock, approval, override, status, ownership, and dependency claims require decision provenance.
5. Agent summaries, PR bodies, commits, recency, and inference are not owner approval.
6. Capture baseline, confirmed scope, preservation locks, and decision records before patch production.
7. Select specialists from changed layers and acceptance criteria; never load everything by default.
8. Product, audience, content, trust, complexity, context, and existing equity drive direction—not taste labels.
9. Port/profile defaults are not universal workflow rules.
10. Structural copy and content decisions precede layout lock.
11. For repository patch or executable prototype output, discover implementation context before code production.
12. Package presence alone does not establish canonical framework, component, styling, icon, state, form, query, or data systems.
13. Reuse, bounded extension, composition, or semantic-native implementation precedes a new dependency proposal.
14. Implementation mapping must name canonical paths/imports and prohibited parallel systems before production.
15. A new dependency requires a proven capability gap, consequences, and verified authority.
16. Every repository write uses an expected-head lease.
17. Inspect head drift before retry; newest commit is not automatically authoritative.
18. Two reversals of the same decision/path stop automatic writes; never ping-pong or force-push.
19. Classify every effective changed path against verified scope.
20. OUT_OF_SCOPE, UNKNOWN, provenance-blocked, or implementation-context-blocked changes block passing review and delivery.
21. Verification evidence must match domain, artifact state, changed layers, and delivery boundary.
22. Build success is not design or architecture proof; screenshot evidence is not runtime or interaction proof.
23. Repository-context discovery cannot self-certify the implementation it guided; run architecture-review after code.
24. Acceptance runs through design-review, governing domain reviewer, and architecture-review when code is delivered.
25. Preserve PASS, FAIL, PARTIAL, NOT_VERIFIED, and NOT_APPLICABLE exactly.
26. Contextual hard gates come from loaded reviewers, not a global UI checklist.
27. Provenance, scope, implementation context, concurrency, evidence, coverage, and facade verdict all control delivery.
28. Classify root cause and correction ownership before fixing.
29. Maximum design iterations default to 5; after two failed patches in one region, re-read and replan.
30. Verified reusable fixes require skill-evolution and a regression eval.
31. Blocked or bounded attempts are never labeled PASS.
32. Never claim a complete redesign environment from the workflow entrypoint alone.
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

  implementation_context:
    required: <true when patch or executable prototype>
    profile_ref: <implementation_context_profile or null>
    canonicality_decisions: []
    convention_locks: []
    reuse_extension_decisions: []
    dependency_decisions: []
    implementation_mapping: []
    prohibited_parallel_systems: []
    evidence_gaps: []
```

Infer missing context only when evidence is strong and record the assumption. Never infer permission for adjacent products, routes, auth, database, user data, infrastructure, dependency installation, destructive work, or approval bypass.

## Canonical flow

```text
0  ROUTE
   redesign | design-refinement | design-audit

1  COMPOSE ROLES
   lifecycle owner, design owner, conditional implementation owner,
   repository write owner, implementation-context specialist,
   selected design specialists, reviewer facade, domain and architecture reviewers

2  INITIALIZE
   validate target, baseline, branch, decision sources, scope, locks,
   approval mode, expected head, and durable state

3  PREFLIGHT
   inspect complete target, effective diff, equity, content, assets,
   system/framework, shared components, tokens, icons, repository conventions,
   concurrent automation, constraints, and evidence gaps
   → patch/prototype: run implementation-context-discovery

4  DIRECTION
   compare alternatives and select product/brand-appropriate direction

5  LAYERED PLAN
   strategy, foundation, structure, components, expression,
   interaction, content, implementation capability requirements

6  VALUE ALIGNMENT
   user value, business/delivery value, measurable signals

7  SPEC CONFIRMATION
   verify decisions; lock scope, paths, routes, exclusions, preservation,
   evidence, delegation, ownership, approvals, convention locks,
   reuse/extension decisions, implementation mapping, and dependency authority

8  PRODUCTION
   acquire expected-head lease and produce through selected ports/adapters
   using the approved repository implementation mapping

9  VERIFICATION
   confirm stable actual head; verify decision provenance, final diff,
   concurrency, implementation-context conformance, domain evidence,
   preservation, technical checks, and delivery boundary

10 ARCHITECTURE + DESIGN REVIEW
   architecture-review for repository implementation
   design-review facade + governing domain reviewer for design acceptance

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
  → implementation_context_owner: implementation-context-discovery
  → implementation_owner: master-engineer or runtime equivalent
  → post_implementation_reviewer: architecture-review
  → exactly one repository_write_owner at a time

spec-only or non-code visual artifact
  → implementation-context-discovery: NOT_APPLICABLE unless mapping to an existing repository is requested

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

repository framework/component/styling/icon/state/form/query/data/build conventions
  → implementation-context-discovery before implementation
```

Load `references/delegation-and-verification.md` for the complete design matrix and `implementation-context-discovery/references/verification-and-workflow-handoff.md` for repository implementation handoff.

## Reference map

Load only when applicable:

| Concern | Reference / skill |
|---|---|
| Dependency model and installation | `references/dependencies-and-installation.md` |
| Lifecycle boundary | `references/redesign-vs-refinement.md` |
| State, phase handoffs, approval, outputs | `references/orchestration-state-and-decisions.md` |
| Decision authority and supersession | `decision-provenance` |
| Direction and macrostructure | `references/phase-genre-macro.md` |
| Delegation and domain evidence | `references/delegation-and-verification.md` |
| Repository implementation context | `implementation-context-discovery` |
| Production policy | `references/phase-produce.md` |
| Final effective diff | `references/scope-diff-integrity.md` |
| Branch write lease and contention | `references/concurrent-write-integrity.md` |
| Fast visual iteration evidence | `references/visual-loop-verification.md` |
| Architecture acceptance | `architecture-review` |
| Facade design review | `references/phase-review-gates.md` |
| Defect, fix, and learning | `references/phase-fix-loop.md` |
| Delivery and anti-loop | `references/phase-deliver.md` |

## Integrity before acceptance

Patch or repository-backed delivery must produce:

```text
decision_provenance_report
scope_diff_report
implementation_context_profile
convention_lock_and_mapping_report
implementation_context_verification
concurrency_report
architecture_review_result
domain verification evidence
preservation results
implementation checks required by the delivery boundary
```

```text
PROVENANCE_BLOCKED / ROUTE_FOR_APPROVAL
  → preserve last verified decision boundary
  → stop the affected mutation or approval claim

IMPLEMENTATION_CONTEXT_BLOCKED
  → stop code production for the affected capability
  → resolve evidence, canonicality, mapping, or dependency authority

SCOPE_BLOCKED
  → restore, remove, preserve-and-split, or obtain verified bounded approval

CONCURRENT_WRITE_BLOCKED
  → stop writes; coordinate one owner and stable child head

integrity PASS
  → architecture and facade acceptance may proceed
```

Visual observations may be recorded while integrity is blocked, but cannot authorize passing delivery.
