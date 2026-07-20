---
name: delivery-work-breakdown
description: Classify a delivery release unit, decompose verified scope into product/epic/feature/task/spike/bug hierarchy, trace child work to parent acceptance criteria, and define branch bases, PR targets, integration topology, and final epic acceptance before repository work begins.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "product-manager decision-provenance git-workflow"
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/product/delivery-work-breakdown.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.boundary.covers: '["release_unit_classification","product_epic_feature_task_spike_and_bug_hierarchy","parent_child_acceptance_traceability","delivery_dependency_graph","issue_plan_structure","integration_and_release_branch_topology","work_item_base_branch_and_pr_target_decisions","epic_acceptance_and_final_release_gate_planning","direct_to_release_branch_exception_reasoning"]'
  ai-native-skills.boundary.delegates: '["product_value_or_prd_authoring","acceptance_criterion_definition","issue_tracker_api_execution","repository_branch_commit_or_pr_execution","feature_flag_implementation","code_implementation","technical_code_review","product_release_authorization","deployment_execution"]'
  ai-native-skills.related_skills: '["product-manager","product-development-workflow","new-feature-workflow","decision-provenance","git-workflow","code-review-workflow","deployment-workflow"]'
---

# Delivery Work Breakdown

Classify the release unit before creating branches, issues, or pull requests.

```text
verified delivery scope
→ release-unit classification
→ work hierarchy and dependencies
→ branch topology and PR targets
→ integration acceptance
→ final release gate
```

This skill owns delivery decomposition and topology decisions. It does not author the PRD, execute Git operations, implement code, approve release, or deploy.

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/product/delivery-work-breakdown.contract.yaml` · compatible line: `^1.0.0`

```yaml
required_inputs:
- delivery_intent_or_scope
- acceptance_criteria
- repository_and_release_context
allowed_outputs:
- release_unit_classification
- release_unit_rationale
- work_hierarchy
- parent_child_traceability
- dependency_graph
- issue_plan
- branch_topology
- pr_target_matrix
- integration_plan
- epic_acceptance_plan
- final_release_gate
- topology_gap_report
quality_gates:
- release_unit_must_be_classified_before_branch_creation
- epic_required_for_dependent_non_independently_releasable_slices
- every_child_work_item_must_trace_to_parent_acceptance_criteria
- no_orphan_feature_task_spike_or_bug_items
- dependency_graph_must_be_explicit_and_cycle_checked
- base_branch_and_pr_target_must_be_explicit_per_work_item
- epic_child_prs_must_target_the_epic_or_integration_branch
- direct_to_release_branch_requires_independent_releasability_or_approved_safe_feature_flag
- feature_flag_exception_requires_disabled_or_equivalent_safe_default_and_no_unflagged_path
- green_ci_or_mergeability_does_not_override_release_topology
- final_epic_pr_requires_integrated_end_to_end_acceptance
- release_ready_state_does_not_self_authorize_merge_or_release
- product_defined_repository_and_approval_policy_must_be_preserved
```

Exact declarations make ownership reviewable. They do not replace product approval, repository evidence, runtime evidence, code review, or release authorization.

## Hard rules

```text
1. Classify the release unit before branch creation.
2. File count, commit count, or CI status does not determine the release unit.
3. Dependent slices that form one outcome default to an epic.
4. Every child item has one parent and acceptance-criterion references.
5. Every work item declares base branch and PR target.
6. Epic child PRs target the epic/integration branch.
7. Direct-to-release requires independent releasability or an approved safe flag.
8. A flag name alone is not evidence: default state and all runtime paths must be verified.
9. Child CI success is not epic acceptance.
10. Release-ready quality does not self-authorize merge or release.
```

## When to load

Load for:

- product development that will create more than one implementation slice;
- a broad capability added to an existing product;
- new app, platform integration, migration, or multi-module delivery;
- unclear epic/feature/task decomposition;
- branch-base or PR-target decisions;
- trunk-based versus epic-branch decisions;
- release planning where partial integration risk matters.

Do not load merely for a single already-classified atomic task whose approved parent, base branch, and PR target are all explicit.

## Required context

Resolve before classification:

```yaml
delivery_context:
  intent_or_scope: <verified request, PRD, or feature spec>
  acceptance_criteria: []
  repository:
    release_branch: <known | unknown>
    branch_policy_ref: <record | unknown>
    merge_policy_ref: <record | unknown>
  release_constraints:
    dependent_slices: []
    partial_activation_risk: <yes | no | unknown>
    end_to_end_acceptance_required: <yes | no | unknown>
    independently_releasable_evidence: []
    feature_flag_policy_ref: <record | none | unknown>
  decision_provenance_refs: []
```

Unknown repository or release policy is a topology gap, not permission to assume `main`.

## Phase 1 — Classify the release unit

Allowed classifications:

```text
standalone_change
feature
epic
product_release
```

Use the decision factors in `references/release-unit-classification.md`.

### Epic is required when any applies

- multiple dependent slices form one user/runtime outcome;
- individual slices are not independently releasable;
- end-to-end acceptance needs the combined slices;
- partial merge can expose or activate incomplete behavior;
- one release decision governs multiple features/tasks.

### Epic may be avoided only with evidence

- each slice is independently releasable and backward-compatible; or
- an approved feature flag is disabled by default and no incomplete path bypasses it; or
- product policy defines trunk-based integration with equivalent activation and acceptance controls.

Return the classification and rationale before continuing.

## Phase 2 — Build the work hierarchy

Allowed work item types:

```text
product → epic → feature → task
                    ↘ spike
                    ↘ bug
```

Every non-root work item records:

```yaml
work_item:
  id: <tracker ref or provisional id>
  type: <epic | feature | task | spike | bug>
  parent_ref: <required>
  acceptance_criteria_refs: []
  dependencies: []
  independently_releasable: <true | false | unknown>
  verification_scope: []
```

Block orphan items and dependency cycles. Spikes produce evidence or decisions; they do not silently become production code.

Use `references/work-hierarchy-and-traceability.md`.

## Phase 3 — Define branch topology and PR targets

For every work item, declare:

```yaml
repository_topology:
  release_branch: <product-defined>
  integration_branch: <required for epic unless equivalent policy exists>
  branch_naming_policy_ref: <product-defined>
  merge_policy_ref: <product-defined>

work_item_topology:
  branch: <name or naming rule>
  base_branch: <explicit>
  pr_target: <explicit>
  direct_to_release_allowed: <true | false>
  reason: <evidence-backed>
```

Default mappings:

```text
epic child             → epic/integration branch
autonomous feature     → product-defined release/integration branch
safely flagged slice   → product-defined branch after flag proof
final epic             → release branch after epic acceptance
```

Never use the repository default branch as an implicit answer.

Use `references/branch-topology-and-pr-targets.md`.

## Phase 4 — Define epic acceptance

An epic acceptance plan includes:

- parent acceptance matrix;
- child completion and evidence map;
- integration verification;
- end-to-end product/runtime evidence when applicable;
- unresolved gaps;
- release-eligibility state;
- release-authorization route.

```text
all child PRs merged to epic branch
≠ epic accepted

integrated acceptance evidence + no blocking gap
→ epic release-eligible
→ route for release authorization
```

## Output contract

```yaml
release_unit_classification:
  type: epic
  rationale: []
  evidence: []
  unknowns: []

work_hierarchy:
  root_ref: <product or epic>
  items: []
  dependency_graph: []
  orphan_items: []
  cycles: []

branch_topology:
  release_branch: <explicit>
  integration_branch: <explicit or justified not applicable>
  policy_refs: []

pr_target_matrix:
  - work_item_ref: <ref>
    base_branch: <branch>
    pr_target: <branch>
    direct_to_release_allowed: false
    rationale: <reason>

epic_acceptance_plan:
  criteria: []
  required_evidence: []
  final_pr_target: <release branch>
  release_authority: <product-defined>

verdict: PASS | NEEDS_WORK | BLOCKED
```

## Blocking conditions

Return `BLOCKED` when:

- release unit is unresolved;
- required parent or acceptance traceability is missing;
- dependency cycles remain;
- release branch or repository policy is unknown and execution is requested;
- an epic child is aimed at the release branch without an approved exception;
- feature-flag safety is claimed without attributable policy and runtime coverage;
- final epic PR is requested before integrated acceptance.

## Workflow composition

```text
product-development-workflow | new-feature-workflow
→ product-manager defines verified scope and acceptance criteria
→ delivery-work-breakdown classifies release unit and topology
→ implementation-context-discovery maps repository conventions
→ implementation slices execute
→ git-workflow performs approved branch/PR operations
→ code-review-workflow verifies each slice
→ epic acceptance verifies the integrated release unit
```

`git-workflow` executes the topology; it does not invent it.

## Evidence boundary

This skill may prove that a topology is explicit and internally consistent. It cannot prove:

- branches or PRs were actually created;
- a feature flag protects every runtime path;
- code is correct;
- the integrated epic works;
- product or release authority approved merge.

Those require repository, runtime, review, and decision-provenance evidence.
