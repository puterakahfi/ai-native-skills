---
name: redesign-workflow
description: Delegated, domain-aware redesign workflow for existing visual surfaces — route → compose owners → verify decisions → inspect → direct → specify → map repository implementation context → produce under a write lease → verify provenance, scope, conventions, concurrency, and artifact → facade review → classify → fix → deliver.
license: MIT
metadata:
  ai-native-skills.version: 3.6.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: workflow
  ai-native-skills.implements: ai-native-core/contracts/skills/quality/redesign-workflow.contract.yaml
  ai-native-skills.contract-version: ^2.2.0
  ai-native-skills.boundary.covers: '["existing_visual_surface_redesign","redesign_vs_refinement_vs_audit_routing","explicit_design_implementation_and_repository_write_ownership","confirmed_scope_and_baseline_capture","final_effective_diff_integrity","concurrent_branch_write_detection_and_coordination","brand_content_asset_behavior_route_and_path_preservation","direction_macrostructure_and_layered_change_planning","user_and_business_value_alignment","delegated_design_and_implementation_work","prototype_or_repository_patch_production","domain_appropriate_verification","design_review_facade_acceptance","bounded_fix_iterations_and_learning_promotion","passing_delivery_or_honest_blocker_reporting"]'
  ai-native-skills.boundary.delegates: '["net_new_product_definition","audit_only_work_after_route_handoff","known_narrow_refinement_after_route_handoff","non_visual_feature_development","unrelated_product_route_auth_data_or_infrastructure_changes","general_bugfix_workflow","deployment_or_publishing","legal_trademark_clearance","force_overwrite_of_uninspected_concurrent_work","destructive_repository_operations_without_approval"]'
  ai-native-skills.pack: packs/redesign/pack.yaml
  ai-native-skills.pack-version: "1.2.0"
  ai-native-skills.requires: "role-switcher master-design master-engineer implementation-context-discovery business-value-alignment decision-provenance design-foundation design-brand design-visual design-layout design-strategy design-interaction design-system design-audit architecture-review design-review design-refinement skill-evolution skill-eval git-workflow"
  ai-native-skills.related_skills: '["workflow-router","architecture-review","component-family-design","adaptive-component-design","macrostructures","ui-components","responsiveness","accessibility","dark-light-theming","brand-identity-review"]'
---

# Redesign Workflow

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/quality/redesign-workflow.contract.yaml` · compatible line: `^2.2.0`

```yaml
required_inputs:
- current_surface
- confirmed_scope
- baseline_evidence
- artifact_type
- output_mode
- decision_sources
- acceptance_criteria
allowed_outputs:
- redesign_state
- route_decision
- confirmed_scope
- scope_provenance
- decision_log
- integrity_gate
- implementation_context_gate
- concurrency_gate
- final_diff_manifest
- role_composition
- design_owner
- implementation_owner
- repository_write_owner
- redesign_strategy
- option_comparison
- selected_direction
- layered_change_plan
- implementation_context_profile
- convention_locks
- reuse_extension_decisions
- implementation_mapping
- dependency_decisions
- value_alignment
- production_output
- verification_evidence
- review_report
- correction_handoff
- learning_review
- delivery_decision
quality_gates:
- route_before_production
- exactly_one_design_owner
- implementation_owner_required_for_patch_or_executable_prototype
- exactly_one_active_repository_write_owner_for_patch_mode
- material_decisions_require_verified_provenance
- unverified_approval_or_override_claims_block_progress
- current_state_baseline_scope_and_locks_are_captured_before_production
- implementation_context_is_required_before_repository_code_production
- package_presence_does_not_prove_canonicality
- implementation_mapping_precedes_code_production
- new_dependency_requires_proven_capability_gap_consequences_and_authority
- final_effective_diff_is_verified_not_only_patch_commits
- concurrent_writes_are_detected_and_coordinated
- expected_head_lease_guards_every_repository_write
- parent_pointer_moves_only_after_child_stability
- repeated_conflicting_updates_stop_without_force_overwrite
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

The workflow owns lifecycle, state transitions, approvals, preservation, integrity gates, iteration, and handoffs. Specialist skills own narrow design decisions. `component-family-design` owns organism/template family consistency when repeated shared surfaces are affected. `implementation-context-discovery` owns the pre-code repository implementation map. `master-engineer` owns implementation. `architecture-review`, `design-review`, and the governing domain reviewer own acceptance in their domains.

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
11. When a redesign creates or changes a repeated organism, page shell, or equivalent cross-route role, run `component-family-design` before code production.
12. For repository patch or executable prototype output, discover implementation context before code production.
13. Package presence alone does not establish canonical framework, component, styling, icon, state, form, query, or data systems.
14. Reuse, bounded extension, composition, or semantic-native implementation precedes a new dependency proposal.
15. Implementation mapping must name canonical paths/imports and prohibited parallel systems before production.
16. A new dependency requires a proven capability gap, consequences, and verified authority.
17. Every repository write uses an expected-head lease.
18. Inspect head drift before retry; newest commit is not automatically authoritative.
19. Two reversals of the same decision/path stop automatic writes; never ping-pong or force-push.
20. Classify every effective changed path against verified scope.
21. OUT_OF_SCOPE, UNKNOWN, provenance-blocked, or implementation-context-blocked changes block passing review and delivery.
22. Verification evidence must match domain, artifact state, changed layers, and delivery boundary.
23. Build success is not design or architecture proof; screenshot evidence is not runtime or interaction proof.
24. Repository-context discovery cannot self-certify the implementation it guided; run architecture-review after code.
25. Acceptance runs through design-review, governing domain reviewer, and architecture-review when code is delivered.
26. Preserve PASS, FAIL, PARTIAL, NOT_VERIFIED, and NOT_APPLICABLE exactly.
27. Contextual hard gates come from loaded reviewers, not a global UI checklist.
28. Provenance, scope, implementation context, concurrency, evidence, coverage, and facade verdict all control delivery.
29. Classify root cause and correction ownership before fixing.
30. Maximum design iterations default to 5; after two failed patches in one region, re-read and replan.
31. Verified reusable fixes require skill-evolution and a regression eval.
32. Blocked or bounded attempts are never labeled PASS.
33. Never claim a complete redesign environment from the workflow entrypoint alone.
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
redesign_context:
  target:
    repository: <owner/repository or null>
    base_ref: <ref or null>
    branch: <branch or null>
    issue: <issue ref or null>
    pull_request: <pr ref or null>
    artifact_type: <artifact type>
    output_mode: <design artifact | specification | patch | executable prototype>
    expected_head: <commit or null>
    repository_write_owner: <owner or null>

  authority:
    decision_sources: []
    verified_owner_statements: []
    inferred_constraints: []
    unverified_claims: []

  confirmed_scope:
    products: []
    routes: []
    paths: []
    allowed_adjacent_changes: []
    excluded_products: []
    excluded_routes: []
    excluded_paths: []
    destructive_operations_allowed: false

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
   repository write owner, component-family specialist when applicable,
   implementation-context specialist, selected design specialists,
   reviewer facade, domain and architecture reviewers

2  INITIALIZE
   validate target, baseline, branch, decision sources, scope, locks,
   approval mode, expected head, and durable state

3  PREFLIGHT
   inspect complete target, effective diff, equity, content, assets,
   system/framework, shared components, organism and template families,
   route instances, tokens, icons, repository conventions,
   concurrent automation, constraints, and evidence gaps
   → repeated organism/template: run component-family-design
   → patch/prototype: run implementation-context-discovery

4  DIRECTION
   compare alternatives and select product/brand-appropriate direction

5  LAYERED PLAN
   strategy, foundation, structure, component capability,
   component-family and template composition, expression,
   interaction, content, implementation capability requirements

6  VALUE ALIGNMENT
   user value, business/delivery value, measurable signals

7  SPEC CONFIRMATION
   verify decisions; lock scope, paths, routes, exclusions, preservation,
   evidence, delegation, ownership, approvals, convention locks,
   family reuse/variant decisions, route-instance mapping,
   component reuse/extension decisions, implementation mapping,
   and dependency authority

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

## Reusable Fix Promotion

A correction becomes skill knowledge only after verification and reviewer acceptance.

```text
verified reusable correction
→ skill-evolution
→ regression eval
→ clean validation
→ skill publication or merge
```

Do not promote an unverified workaround, project-only exception, or failed patch.

## Integrity gate

Before production and delivery, report:

```yaml
integrity_gate:
  expected_head: <commit>
  actual_head: <commit>
  head_matches_expected: <true | false | unknown>
  active_write_owner: <owner>
  concurrent_writers: []
  reversal_count_by_path_or_decision: {}
  final_diff_scope: []
  scope_classification:
    in_scope: []
    allowed_adjacent: []
    out_of_scope: []
    unknown: []
  provenance_status: <PASS | FAIL | PARTIAL | NOT_VERIFIED>
  implementation_context_status: <PASS | FAIL | PARTIAL | NOT_VERIFIED | NOT_APPLICABLE>
  concurrency_status: <PASS | FAIL | PARTIAL | NOT_VERIFIED | NOT_APPLICABLE>
  delivery_blockers: []
```

## Implementation-context gate

For patch or executable prototype output, report before production:

```yaml
implementation_context_gate:
  repository_ref: <ref>
  implementation_scope: []
  framework_runtime_map: []
  component_system_map: []
  canonical_component_inventory: []
  canonical_component_family_inventory: []
  organism_inventory: []
  template_inventory: []
  route_to_family_instance_map: []
  component_capability_coverage_map: []
  component_variant_inventory: []
  canonical_registry_component_decisions: []
  typography_role_map: []
  semantic_native_eligibility_map: []
  styling_system_map: []
  iconography_implementation_map: []
  state_form_data_tooling_map: []
  workspace_build_test_map: []
  canonicality_decisions: []
  convention_locks: []
  family_reuse_variant_decisions: []
  reuse_extension_decisions: []
  dependency_decisions: []
  implementation_mapping: []
  prohibited_parallel_systems: []
  evidence_gaps: []
  status: <PASS | FAIL | PARTIAL | NOT_VERIFIED>
```

Stop before code when framework, component or family coverage, canonical registry, typography role, semantic-native boundary, style, icon, behavior, or dependency authority remains materially unknown.

## Verification requirements

Match evidence to the changed artifact and domain:

```text
repository patch
  final effective diff
  expected-head and concurrency evidence
  implementation-context conformance
  type/lint/test/build as applicable
  architecture-review
  rendered target surfaces
  domain review through design-review

static visual
  exported artifact at target dimensions
  readability and composition evidence
  governing visual-domain review

responsive interface
  target viewport captures
  adaptation boundary evidence
  touch/pointer/keyboard behavior as applicable
  component-family consistency across relevant routes
  governing interface review

brand or domain-specialized artifact
  registered domain reviewer and canonical gate IDs
  domain-specific evidence
  legal/trademark limitations when applicable
```

## Review and correction

```text
verified output
→ design-review facade
→ governing domain reviewer
→ architecture-review when code is delivered
→ normalized findings
→ root-cause classification
→ correction owner
→ design-refinement or specialist
→ focused re-review
→ learning review
```

`design-review` owns facade routing, evidence normalization, scoring, gate identity, and reporting. It must review equivalent route instances together when component-family consistency is in scope. Domain reviewers own their domain definitions. `architecture-review` independently verifies repository implementation alignment. `implementation-context-discovery` cannot review its own mapping. `component-family-design` cannot self-certify rendered family consistency.

## Delivery rule

Deliver only when:

```text
route is correct
ownership is explicit
material decisions have verified provenance
scope and final effective diff are clean
implementation context and family mapping are resolved when required
expected-head and concurrency gates pass
artifact evidence matches the changed domain
facade and governing reviewer accept within their scope
architecture review accepts delivered code
remaining risks and authority boundaries are explicit
```

Otherwise deliver a blocker, limited review, bounded partial result, or correction handoff without overstating completion.
