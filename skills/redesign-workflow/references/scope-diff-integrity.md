# Scope Diff Integrity

Load this reference for repository patch runs before final design review and delivery.

## Purpose

A redesign branch may contain old commits, rebases, or unrelated history. Acceptance is based on the **effective final diff against the declared baseline**, not on commit titles or agent intent.

```text
confirmed redesign scope
→ capture baseline
→ inspect effective final diff
→ classify every changed path
→ remove, restore, or split contamination
→ review only the clean redesign surface
```

An attractive redesign cannot compensate for unrelated authentication, database, user-data, product-feature, or infrastructure changes entering the same delivery.

## Inputs

```yaml
scope_diff_input:
  baseline_ref: <merge base, approved commit, or original artifact>
  target_ref: <current branch head or produced artifact>
  confirmed_scope:
    products: []
    routes_or_surfaces: []
    allowed_paths: []
    allowed_change_types: []
    expected_generated_files: []
    expected_deletions: []
    preserved_paths: []
    out_of_scope: []
```

Capture `baseline_ref` during initialization. Do not choose a more convenient baseline after contamination is discovered.

## Effective Diff

For Git-backed work, inspect the merge-base diff or equivalent:

```bash
git diff --name-status <baseline>...<target>
git diff --stat <baseline>...<target>
git diff --check <baseline>...<target>
```

Also inspect renamed, deleted, binary, generated, and submodule entries. A clean working tree alone does not prove a clean delivery diff.

For non-Git artifacts, compare the produced artifact manifest with the approved source and declared output set.

## Classification

Every changed entry receives exactly one classification:

```text
IN_SCOPE
  Directly implements a confirmed redesign layer or acceptance criterion.

REQUIRED_DEPENDENCY
  Outside the primary surface but causally required for the redesign to work.
  Must name the dependency, reason, owner, and acceptance criterion.

EXPECTED_GENERATED
  Build/export output explicitly declared by the spec.

OUT_OF_SCOPE
  Belongs to another product, feature, route, data model, auth flow,
  infrastructure change, experiment, or user-content concern.

UNKNOWN
  Ownership or causal need is not established.
```

`REQUIRED_DEPENDENCY` is not a loophole. Formatting, opportunistic cleanup, unrelated refactoring, and “it was already on the branch” are not sufficient reasons.

## Hard Blockers

The following block passing review and delivery until resolved:

```text
□ any OUT_OF_SCOPE entry
□ any UNKNOWN entry
□ undeclared database migration or schema change
□ undeclared authentication, authorization, entitlement, or user-data change
□ another product or route added only because it shared the branch
□ deletion of a preserved path
□ generated or binary artifact without declared provenance
□ submodule or dependency pointer change without a recorded causal requirement
□ final diff cannot be reproduced from the declared baseline and target
```

The visual facade may still record design observations, but the workflow decision remains blocked. Do not spend review cycles polishing an artifact whose delivery boundary is contaminated.

## Resolution

Choose the smallest safe action:

```text
unrelated file added
→ remove it from the effective diff

existing file changed for unrelated work
→ restore it from the baseline

valid work belongs to another lifecycle
→ split it to another branch, PR, or workflow

required dependency was omitted from the spec
→ document the causal requirement and re-run approval policy

ownership remains unknown
→ keep BLOCKED and hand off to the repository owner
```

Never delete user or product work merely to make a diff look clean. Preserve it in its rightful branch or artifact before removing it from the redesign delivery.

## Output Contract

```yaml
scope_diff_report:
  baseline_ref: <ref>
  target_ref: <ref>
  confirmed_scope: <summary>
  changed_entries:
    - path: <path>
      change_type: <added | modified | deleted | renamed | binary | submodule>
      classification: <IN_SCOPE | REQUIRED_DEPENDENCY | EXPECTED_GENERATED | OUT_OF_SCOPE | UNKNOWN>
      owner: <owner>
      rationale: <why>
      acceptance_criterion: <id or null>
  contamination:
    out_of_scope: []
    unknown: []
    preserved_path_violations: []
  status: PASS | BLOCKED
  required_actions: []
```

`PASS` requires every changed entry to be classified and no contamination blocker to remain.

## Workflow Placement

```text
SPEC CONFIRMATION
  declare allowed paths/surfaces/change types and baseline

PRODUCTION
  modify only the declared scope or explicitly approved dependencies

VERIFICATION
  generate scope_diff_report before facade acceptance

REVIEW
  proceed with passing-delivery evaluation only when scope status is PASS

FIX
  restore, remove, or split contamination; then regenerate the report

DELIVERY
  include scope status and changed-file manifest
```

## Anti-Patterns

```text
❌ “The PR is mergeable, therefore scope is valid.”
❌ “The unrelated feature existed on the branch, so it can stay.”
❌ “Only the homepage was reviewed, so other changed files do not matter.”
❌ Calling database/auth changes design dependencies without causal evidence.
❌ Resetting the baseline to hide unrelated changes.
❌ Deleting valuable unrelated work instead of preserving it elsewhere.
```

## Final Guard

```text
□ Baseline was captured before production or inherited from the approved branch point.
□ Confirmed scope names products, surfaces, paths, and allowed change types.
□ Every effective changed entry is classified.
□ Required dependencies have causal evidence and approval.
□ OUT_OF_SCOPE and UNKNOWN lists are empty.
□ Preserved paths remain intact.
□ Scope report is attached to verification and delivery.
```
