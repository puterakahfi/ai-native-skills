# Scope Diff Integrity

Load this reference for repository patch runs before final design review and delivery.

Load `decision-provenance` whenever confirmed scope, preservation locks, required dependencies, exclusions, or scope overrides are created, disputed, or changed.

## Purpose

A redesign branch may contain old commits, rebases, agent summaries, or unrelated history. Acceptance is based on the **effective final diff against the declared baseline and verified decision ledger**, not on commit titles, branch recency, PR narrative, or agent intent.

```text
verified scope decisions
→ capture baseline
→ inspect effective final diff
→ classify every changed path
→ verify dependency and override provenance
→ remove, restore, split, or re-approve contamination
→ review only the clean redesign surface
```

An attractive redesign cannot compensate for unrelated authentication, database, user-data, product-feature, route, or infrastructure changes entering the same delivery.

## Inputs

```yaml
scope_diff_input:
  baseline_ref: <merge base, approved commit, or original artifact>
  target_ref: <current stable branch head or produced artifact>
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
  decision_record_ids: []
  required_dependency_approvals: []
```

Capture `baseline_ref` during initialization. Do not choose a more convenient baseline after contamination is discovered.

Every material scope item must point to a decision record. A scope claim such as “the user explicitly approved this route” is invalid until `decision-provenance` resolves an attributable authoritative source.

## Effective diff

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
  Directly implements a verified scope decision or acceptance criterion.

REQUIRED_DEPENDENCY
  Outside the primary surface but causally required for the redesign to work.
  Must name the reason, owner, acceptance criterion, decision record, and approval.

EXPECTED_GENERATED
  Build/export output explicitly declared by the verified spec.

OUT_OF_SCOPE
  Belongs to another product, feature, route, data model, auth flow,
  infrastructure change, experiment, or user-content concern.

UNKNOWN
  Ownership, causal need, or decision provenance is not established.
```

`REQUIRED_DEPENDENCY` is not a loophole. Formatting, opportunistic cleanup, unrelated refactoring, “it already exists”, “the newest commit added it”, and agent-authored PR text are not sufficient reasons.

## Decision provenance rules

Before changing scope or classification:

```text
verified authoritative decision covers the exact product/path/action
  → scope entry may be added or superseded

agent summary, PR body, commit message, or inference is the only support
  → NON_AUTHORITATIVE
  → scope remains unchanged

implementation exists but no scope decision exists
  → OBSERVED_IMPLEMENTATION_STATE only
  → existence does not prove delivery scope

authoritative sources conflict without explicit supersession
  → PROVENANCE_BLOCKED
  → stop dependent mutation and delivery claim

additional policy/owner approval is required
  → ROUTE_FOR_APPROVAL
  → preserve current safe scope
```

A newer commit or narrative cannot silently supersede an older approved scope. Supersession must be explicit, attributable, and bounded.

## Hard blockers

The following block passing review and delivery until resolved:

```text
□ any OUT_OF_SCOPE entry
□ any UNKNOWN entry
□ scope or override decision is PROVENANCE_BLOCKED
□ material scope item has no decision record
□ agent-authored text is treated as user/owner approval
□ conflicting authoritative scope decisions lack explicit supersession
□ undeclared database migration or schema change
□ undeclared authentication, authorization, entitlement, or user-data change
□ another product or route added only because it shared the branch
□ deletion of a preserved path or route
□ generated or binary artifact without declared provenance
□ submodule or dependency pointer change without a recorded causal requirement
□ final diff cannot be reproduced from the declared baseline and target
```

The visual facade may record observations while blocked, but it cannot authorize merge or passing delivery.

## Resolution

Choose the smallest safe action:

```text
unrelated file added
→ remove it from the effective diff

existing file changed for unrelated work
→ restore it from the baseline

valid work belongs to another lifecycle
→ preserve and split it to another branch, PR, ticket, or workflow

required dependency omitted from the spec
→ verify causal need and decision provenance
→ re-run approval policy

agent claims an owner override without an authoritative source
→ keep the old verified scope
→ record PROVENANCE_BLOCKED

multiple authoritative decisions conflict
→ stop mutation
→ route to the decision owner for explicit supersession

ownership remains unknown
→ keep BLOCKED and hand off
```

Never delete valuable user or product work merely to make a diff look clean. Preserve it in its rightful lifecycle before removing it from the redesign delivery.

## Output contract

```yaml
scope_diff_report:
  baseline_ref: <ref>
  target_ref: <stable ref>
  confirmed_scope: <summary>
  decision_provenance:
    record_ids: []
    verdict: <PASS | PROVENANCE_BLOCKED | ROUTE_FOR_APPROVAL>
    conflicts: []
    unresolved_requirements: []
  changed_entries:
    - path: <path>
      change_type: <added | modified | deleted | renamed | binary | submodule>
      classification: <IN_SCOPE | REQUIRED_DEPENDENCY | EXPECTED_GENERATED | OUT_OF_SCOPE | UNKNOWN>
      owner: <owner>
      rationale: <why>
      acceptance_criterion: <id or null>
      decision_record_id: <id or null>
  contamination:
    out_of_scope: []
    unknown: []
    preserved_path_violations: []
    provenance_blocked: []
  status: PASS | BLOCKED
  required_actions: []
```

`PASS` requires:

```text
all changed entries classified
no contamination blocker
verified provenance for material scope and dependency decisions
no unresolved authoritative conflict
all required approvals satisfied
```

## Workflow placement

```text
INITIALIZE
  capture baseline and initial decision sources

SPEC CONFIRMATION
  verify scope/lock/override provenance
  declare allowed paths, surfaces, change types, and exclusions

PRODUCTION
  modify only verified scope or approved dependencies

VERIFICATION
  generate decision provenance report and scope diff report

REVIEW
  proceed toward passing delivery only when both reports pass

FIX
  restore, remove, split, or obtain explicit bounded approval

DELIVERY
  include scope status, decision ledger IDs, and changed-file manifest
```

## Anti-patterns

```text
❌ “The PR is mergeable, therefore scope is valid.”
❌ “The PR body says the user approved it.”
❌ “The latest commit wins.”
❌ “The route exists, therefore it belongs in this redesign.”
❌ “The unrelated feature existed on the branch, so it can stay.”
❌ Calling database/auth changes design dependencies without causal evidence.
❌ Resetting the baseline to hide unrelated changes.
❌ Inventing a quote, issue comment, owner, or approval source.
❌ Deleting valuable unrelated work instead of preserving it elsewhere.
```

## Final guard

```text
□ Baseline was captured before production or inherited from the approved branch point.
□ Confirmed scope names products, surfaces, paths, change types, and exclusions.
□ Material scope decisions reference verified decision records.
□ Agent-authored summaries are not treated as owner approval.
□ Existing implementation is not confused with delivery authorization.
□ Supersession and conflicts are explicit.
□ Every effective changed entry is classified.
□ Required dependencies have causal evidence and approval.
□ OUT_OF_SCOPE, UNKNOWN, and provenance-blocked lists are empty.
□ Preserved paths and routes remain intact.
□ Scope and provenance reports are attached to verification and delivery.
```
