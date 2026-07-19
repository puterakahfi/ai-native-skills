# Phase 13 — Delivery and Anti-Loop

Deliver only from the current scope-diff status, facade verdict, redesign acceptance criteria, evidence coverage, primary-domain coverage, contextual hard gates, preservation status, and approval boundary.

Average score is supporting information. Mergeability is repository information. Neither is a delivery decision.

## Pre-delivery scope gate

For repository patch runs, load `scope-diff-integrity.md` and require:

```text
scope_diff_report.status = PASS
OUT_OF_SCOPE = []
UNKNOWN = []
preserved-path violations = []
all REQUIRED_DEPENDENCY entries have causal evidence and approval
```

When scope is blocked:

```text
Decision: SCOPE_BLOCKED
Action: restore, remove, split, or explicitly re-approve the dependency
```

A clean design score cannot override a contaminated delivery diff. Scope contamination cannot be converted into a non-blocking accepted risk.

## Delivery decisions

### PASS

Deliver as accepted only when all are true:

```text
scope integrity passes when applicable
facade verdict is PASS
redesign acceptance criteria pass
primary-domain coverage is BUILT_IN or ADAPTER_COVERED
all applicable contextual hard gates pass
required evidence is available
no release-blocking NOT_VERIFIED remains
brand, content, asset, behavior, path, and design-system locks pass
implementation/export checks required by the delivery boundary pass
```

### CONDITIONAL PASS

Deliver conditionally only when:

```text
scope integrity passes when applicable
facade verdict is CONDITIONAL PASS
no verified hard-gate failure exists
remaining gaps are explicitly non-blocking
risks are accepted inside the current approval boundary
risk owner and expiry are recorded when relevant
no missing specialist reviewer is being hidden
```

Do not shorten `CONDITIONAL PASS` to `PASS`. Do not use it to accept unrelated product, auth, database, user-data, or infrastructure changes.

### SCOPE BLOCKED

```text
OUT_OF_SCOPE or UNKNOWN entry exists
preserved path changed or removed
baseline or target is not reproducible
required dependency lacks causal evidence or approval
```

The artifact may receive a visual observation report, but it is not ready to merge or deliver. Resolve contamination and regenerate the report before facade acceptance controls delivery.

### NEEDS WORK or CRITICAL

```text
iterations remain
  → return to defect classification and fix

no iterations remain
  → MAX_ITERATIONS_REACHED with explicit gap report
```

Never deliver these as accepted.

### LIMITED REVIEW

```text
load the required domain reviewer
or narrow the delivery claim to verified universal/partial scope
or hand off to the domain specialist
```

A limited scorecard cannot approve complete identity, packaging, motion, industrial, spatial, fashion, or another specialist-domain outcome.

### ROUTE ELSEWHERE

Stop the unsupported approval claim and state the required route/reviewer.

### MAX ITERATIONS REACHED

Deliver the best preserved attempt with:

```text
current artifact
last known good or rollback path
scope-diff status and contamination list
facade verdict
verified improvements
remaining FAIL/PARTIAL findings
NOT_VERIFIED evidence gaps
scope limitations
specialist or lifecycle handoff
```

Never label it complete, approved, production-ready, or passed.

## Artifact handling

Use canonical project paths and project version-control conventions.

```text
repository patch
  edit the intended canonical files
  compare final effective diff to the captured baseline
  preserve rollback through source control
  split unrelated valuable work before removing it from this delivery
  do not create arbitrary v2/v3/final copies unless required

prototype or exported artifact
  use the declared output path
  compare produced manifest with the approved artifact set
  retain iteration provenance in the delivery manifest
  preserve the last known good artifact when replacement is risky

presentation/static/identity production
  follow domain file, export, master, and naming requirements
  do not impose a single-file HTML convention
```

The workflow does not automatically commit after every creative iteration. Commit behavior follows repository policy and approval mode.

## Delivery manifest

```yaml
delivery_manifest:
  target: <target>
  design_domain: <domain>
  surface_profile: <profile>
  output_mode: <mode>
  baseline_ref: <ref or original artifact>
  target_ref: <ref or produced artifact>
  final_decision: <PASS | CONDITIONAL_PASS | SCOPE_BLOCKED |
                   MAX_ITERATIONS_REACHED | LIMITED_REVIEW | ROUTE_ELSEWHERE>
  scope_diff:
    status: <PASS | BLOCKED | NOT_APPLICABLE>
    confirmed_scope: <summary>
    changed_entries: []
    required_dependencies: []
    out_of_scope: []
    unknown: []
    preserved_path_violations: []
  facade_verdict: <verdict>
  coverage_mode: <mode>
  evidence_coverage: <percentage>
  primary_domain_coverage: <complete | limited | unavailable>
  contextual_hard_gates: <status>
  acceptance_criteria:
    passed: []
    conditional: []
    failed: []
    not_verified: []
  artifact:
    path_or_target: <value>
    changed_files_or_regions: []
    rollback: <path, ref, or method>
  role_composition:
    design_owner: <owner>
    implementation_owner: <owner or null>
    reviewer_facade: design-review
    domain_reviewers: []
  preservation:
    passed: []
    failed: []
    not_verified: []
  verification:
    evidence_available: []
    evidence_gaps: []
    checks_passed: []
    checks_failed: []
    checks_deferred: []
  findings:
    resolved: []
    remaining: []
  accepted_risks: []
  learning_review:
    verdicts: []
    commits: []
  approval_history: []
```

## Human-facing report

```markdown
# Redesign Delivery — [target]

**Decision:** [PASS | CONDITIONAL PASS | SCOPE BLOCKED | MAX ITERATIONS REACHED | LIMITED REVIEW | ROUTE ELSEWHERE]

- Scope integrity: [PASS | BLOCKED | NOT APPLICABLE]
- Design domain: [domain]
- Facade verdict: [verdict]
- Coverage: [mode]
- Evidence coverage: [X%]
- Contextual hard gates: [status]
- Iterations: [N]

## Effective delivery diff
- Baseline: ...
- Target: ...
- In scope: ...
- Required dependencies: ...
- Out of scope / unknown: ...

## Delivered artifact
[path or target]

## Verified improvements
- ...

## Preservation
- Passed: ...
- Failed: ...
- Not verified: ...

## Remaining findings
- `[gate]` [status] — [finding and impact]

## Evidence gaps and limitations
- ...

## Accepted risks
- ...

## Rollback
- ...

## Next route
[none | scope cleanup | verification | defect fix | domain specialist | design-refinement | code review]
```

## Anti-loop protection

Increment iterations only after completed facade review. Scope cleanup before review does not consume a design iteration unless it changes the redesigned artifact.

```text
before each fix
  confirm active defect or contamination entry, governing owner,
  correction owner, preservation set, and required evidence

after two failed patches in one region
  re-read, replan, and consider alternative pattern or justified rewrite

when max_iterations is reached
  stop correction
  preserve current and rollback artifacts
  deliver honest gap report
```

Do not change unrelated regions to improve a score. Do not reset the baseline to hide contamination. Do not replace the approved direction merely because one local fix failed.

## Common delivery failures

| Failure | Correct behavior |
|---|---|
| Homepage redesign also changes auth/database/member features | `SCOPE_BLOCKED`; restore, remove, or split them |
| PR is mergeable but final diff is contaminated | Mergeability is not scope approval |
| `avg >= 8` but hard gate failed | Block PASS |
| Missing runtime/export/specialist evidence | Report NOT_VERIFIED and block the corresponding claim |
| Static artifact forced through touch/motion gates | Use static reviewer and applicable gates |
| Identity system has only one mockup | LIMITED/NOT_VERIFIED until identity evidence exists |
| Repository gets `final-v2-fixed` copies | Follow canonical paths and source-control policy |
| Every iteration auto-committed | Follow approval and repository policy |
| Third blind CSS patch | Re-read and replan after two failed region patches |
| Best attempt called complete | Use MAX_ITERATIONS_REACHED with gaps |
