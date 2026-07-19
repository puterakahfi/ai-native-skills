# Phase 13 — Delivery and Anti-Loop

Deliver only from current scope integrity, concurrency integrity, facade verdict, acceptance criteria, evidence coverage, primary-domain coverage, reviewer-owned hard gates, preservation status, and approval boundary.

Average score is supporting information. Mergeability is repository information. A recent commit is chronology. None is a delivery decision.

## Pre-delivery integrity gates

### Scope

For repository patch runs, require:

```text
scope_diff_report.status = PASS
OUT_OF_SCOPE = []
UNKNOWN = []
preserved path/route violations = []
all REQUIRED_DEPENDENCY entries have causal evidence and approval
```

### Concurrency

Load `concurrent-write-integrity.md` and require:

```text
concurrency_report.status = PASS
manifest target head = actual stable branch head
last mutation used a valid expected-head lease
no unresolved DECISION_CONFLICT, SCOPE_EXPANSION, or UNKNOWN drift
no anti-ping-pong threshold reached
parent pointer, when applicable, targets the frozen verified child head
```

When either integrity gate is blocked, design observations may be recorded but merge or passing delivery is forbidden.

## Delivery decisions

### PASS

Deliver as accepted only when all are true:

```text
scope integrity passes
concurrency integrity passes
facade verdict is PASS
redesign acceptance criteria pass
primary-domain coverage is BUILT_IN or ADAPTER_COVERED
all applicable contextual hard gates pass
required evidence is available
no release-blocking NOT_VERIFIED remains
brand, content, asset, behavior, route, path, and design-system locks pass
implementation/export checks required by the delivery boundary pass
```

### CONDITIONAL PASS

Deliver conditionally only when:

```text
scope and concurrency integrity pass
facade verdict is CONDITIONAL PASS
no verified hard-gate failure exists
remaining gaps are explicitly non-blocking
risks are accepted inside the approval boundary
risk owner and expiry are recorded when relevant
no missing specialist reviewer is being hidden
```

Do not use `CONDITIONAL PASS` to accept contamination, a moving branch, unresolved owner conflict, or stale evidence.

### SCOPE BLOCKED

```text
OUT_OF_SCOPE or UNKNOWN entry exists
preserved path/route changed or removed
baseline or target is not reproducible
required dependency lacks causal evidence or approval
```

Action: restore, remove, split, hand off, or explicitly re-approve the true dependency; then regenerate the scope report.

### CONCURRENT WRITE BLOCKED

```text
actual head differs from expected head and drift is conflicting or unknown
same decision/path was automatically reversed twice
multiple agents claim incompatible ownership
parent pointer is chasing a moving child head
delivery manifest or PR body references a stale head
```

Action:

1. stop automated repository writes;
2. report expected and actual heads, changed paths, and decision conflict;
3. declare one repository write owner or split real lifecycles;
4. freeze a head;
5. regenerate scope, verification, concurrency, and review artifacts.

Never resolve this with a force-push over uninspected work or a third automatic reversal.

### NEEDS WORK or CRITICAL

```text
iterations remain
  → return to defect classification and fix under a fresh write lease

no iterations remain
  → MAX_ITERATIONS_REACHED with explicit gap report
```

### LIMITED REVIEW

Load the required domain reviewer, narrow the verified claim, or hand off. Limited coverage cannot approve a complete specialist-domain outcome.

### ROUTE ELSEWHERE

Stop the unsupported approval claim and state the required lifecycle or reviewer.

### MAX ITERATIONS REACHED

Deliver the best preserved attempt with current artifact, rollback, scope/concurrency status, facade verdict, verified improvements, remaining findings, evidence gaps, limitations, and handoff. Never label it complete, approved, production-ready, or passed.

## Artifact handling

```text
repository patch
  edit canonical files only
  compare effective diff to captured baseline
  validate expected head before every mutation
  preserve valuable unrelated work before removing it from this delivery
  do not create arbitrary v2/v3/final copies

prototype or exported artifact
  use declared output path
  compare produced manifest with approved artifact set
  retain iteration and writer provenance
  preserve last known good artifact when replacement is risky

presentation/static/identity production
  follow domain file, export, master, and naming requirements
  do not impose a single-file HTML convention
```

The workflow does not automatically commit after every creative iteration. Commit behavior follows repository policy, approval mode, and valid write ownership.

## Delivery manifest

```yaml
delivery_manifest:
  target: <target>
  design_domain: <domain>
  surface_profile: <profile>
  output_mode: <mode>
  baseline_ref: <ref or original artifact>
  target_ref: <actual stable head or produced artifact>
  final_decision: <PASS | CONDITIONAL_PASS | SCOPE_BLOCKED |
                   CONCURRENT_WRITE_BLOCKED | MAX_ITERATIONS_REACHED |
                   LIMITED_REVIEW | ROUTE_ELSEWHERE>
  scope_diff:
    status: <PASS | BLOCKED | NOT_APPLICABLE>
    confirmed_scope: <summary>
    changed_entries: []
    required_dependencies: []
    out_of_scope: []
    unknown: []
    preserved_path_violations: []
  concurrency:
    status: <PASS | CONCURRENT_WRITE_BLOCKED | NOT_APPLICABLE>
    branch: <branch or null>
    expected_head: <sha or null>
    actual_head: <sha or null>
    drift_classification: <classification or null>
    contention_cycles: <N>
    repository_write_owner: <owner or unresolved>
    head_sequence: []
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
    repository_write_owner: <owner or unresolved>
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

**Decision:** [PASS | CONDITIONAL PASS | SCOPE BLOCKED | CONCURRENT WRITE BLOCKED | MAX ITERATIONS REACHED | LIMITED REVIEW | ROUTE ELSEWHERE]

- Scope integrity: [status]
- Concurrency integrity: [status]
- Stable target head: [sha or not stable]
- Repository write owner: [owner or unresolved]
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

## Concurrency
- Expected head: ...
- Actual head: ...
- Drift: ...
- Contention cycles: ...
- Required owner action: ...

## Delivered or preserved artifact
[path or target]

## Verified improvements
- ...

## Remaining findings and evidence gaps
- ...

## Rollback
- ...

## Next route
[none | owner coordination | scope cleanup | verification | defect fix | domain specialist | new feature | code review]
```

## Anti-loop protection

Design iterations increment only after completed facade review. Scope cleanup and concurrency reconciliation are tracked separately.

```text
before each fix
  confirm active defect/blocker, governing owner, expected head,
  intended paths, preservation set, and required evidence

after two failed design patches in one region
  re-read and replan

after two automated reversals of one decision/path
  stop writes with CONCURRENT_WRITE_BLOCKED

when max design iterations are reached
  preserve artifact and rollback
  deliver honest gap report
```

Do not reset baseline to hide contamination. Do not chase a moving child branch with parent pointers. Do not overwrite PR text repeatedly while the underlying head and decision remain unstable.

## Common delivery failures

| Failure | Correct behavior |
|---|---|
| Homepage redesign also changes auth/database/member features | `SCOPE_BLOCKED`; restore, remove, or split |
| Two agents repeatedly add/remove the same route | `CONCURRENT_WRITE_BLOCKED`; declare owner or split lifecycle |
| Parent pointer follows every moving child head | Freeze child first; do not chase |
| PR is mergeable but diff is contaminated or head unstable | Mergeability is not approval |
| `avg >= 8` but hard gate failed | Block PASS |
| Missing runtime/export/specialist evidence | NOT_VERIFIED and block claim |
| Static artifact forced through interactive gates | Use applicable domain reviewer |
| Best attempt called complete | Use bounded/blocking decision honestly |