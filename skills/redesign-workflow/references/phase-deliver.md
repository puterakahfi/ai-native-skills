# Phase 13 — Delivery and Anti-Loop

Deliver only from current scope integrity, concurrency integrity, facade verdict, acceptance criteria, evidence coverage, primary-domain coverage, reviewer-owned hard gates, preservation status, approval boundary, and an evidence-backed quality level.

Load `quality-levels.md` before choosing final delivery language. Quality level supplements the integrity and facade decision; it never overrides them.

Average score is supporting information. Mergeability is repository information. A recent commit is chronology. Quality labels are evidence boundaries. None is a delivery decision by itself.

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

When either integrity gate is blocked, design observations and quality evidence may be recorded but merge or passing delivery is forbidden.

## Quality claim gate

```text
Q0 UNRESOLVED
  production forbidden

Q1 FOUNDATION_SAFE
  candidate/handoff only
  never final, release-ready, pixel-polished, or pixel-perfect

Q2 RENDER_VERIFIED
  suitable for current visual review
  remaining optical and regression gaps must be stated

Q3 PIXEL_POLISHED
  default final visual target
  requires Q2 + optical correction + adjacent-regression reinspection
  + facade acceptance + applicable integrity/hard-gate pass

Q4 PIXEL_MATCHED
  Q3 + locked reference/spec + declared comparison method and tolerance
```

Without a locked reference, Q4 is `NOT_APPLICABLE`. Never use `pixel-perfect` from source-only work, build success, a single screenshot, or a high average score.

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
target quality level is reached by current evidence
final visual-delivery claim reaches Q3 by default unless a narrower target was explicitly approved
```

Q3 means release-ready **visual implementation**. It does not independently authorize deployment, merge, publishing, or production-environment changes.

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
quality level and remaining evidence gaps are stated without inflated language
```

Do not use `CONDITIONAL PASS` to accept contamination, a moving branch, unresolved owner conflict, stale evidence, or a falsely elevated quality claim.

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
5. regenerate scope, verification, concurrency, review, and quality artifacts.

Never resolve this with a force-push over uninspected work or a third automatic reversal.

### NEEDS WORK or CRITICAL

```text
iterations remain
  → return to defect classification and fix under a fresh write lease

no iterations remain
  → MAX_ITERATIONS_REACHED with explicit gap report
```

### LIMITED REVIEW

Load the required domain reviewer, narrow the verified claim, or hand off. Limited coverage cannot approve a complete specialist-domain outcome or Q3 final claim.

### ROUTE ELSEWHERE

Stop the unsupported approval claim and state the required lifecycle or reviewer.

### MAX ITERATIONS REACHED

Deliver the best preserved attempt with current artifact, achieved quality level, rollback, scope/concurrency status, facade verdict, verified improvements, remaining findings, evidence gaps, limitations, and handoff. Never label it complete, approved, production-ready, pixel-polished, pixel-perfect, or passed unless the corresponding evidence actually exists.

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
  quality:
    target: <Q1_FOUNDATION_SAFE | Q2_RENDER_VERIFIED | Q3_PIXEL_POLISHED | Q4_PIXEL_MATCHED>
    achieved: <level supported by evidence>
    evidence: []
    blocked_claims: []
    reference_comparison:
      applicable: <true | false>
      method: <value or null>
      tolerance: <value or null>
      approved_deviations: []
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
    viewing_contexts: []
    optical_corrections: []
    adjacent_regressions_checked: []
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

- Quality target: [Q1 | Q2 | Q3 | Q4]
- Quality achieved: [Q1 | Q2 | Q3 | Q4]
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

## Quality evidence
- Rendered/exported contexts: ...
- Optical corrections: ...
- Adjacent regressions: ...
- Reference comparison: ...
- Blocked claims: ...

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

Design iterations increment only after completed facade review. Scope cleanup, concurrency reconciliation, and quality-evidence collection are tracked separately.

```text
before each fix
  confirm active defect/blocker, governing owner, expected head,
  intended paths, preservation set, required evidence, and target quality level

after two failed design patches in one region
  re-read and replan

after two automated reversals of one decision/path
  stop writes with CONCURRENT_WRITE_BLOCKED

when max design iterations are reached
  preserve artifact and rollback
  deliver honest achieved quality and gap report
```

Do not reset baseline to hide contamination. Do not chase a moving child branch with parent pointers. Do not overwrite PR text repeatedly while the underlying head and decision remain unstable. Do not keep patching only to chase the label `pixel-perfect` when no locked reference exists.

## Common delivery failures

| Failure | Correct behavior |
|---|---|
| Homepage redesign also changes auth/database/member features | `SCOPE_BLOCKED`; restore, remove, or split |
| Two agents repeatedly add/remove the same route | `CONCURRENT_WRITE_BLOCKED`; declare owner or split lifecycle |
| Parent pointer follows every moving child head | Freeze child first; do not chase |
| PR is mergeable but diff is contaminated or head unstable | Mergeability is not approval |
| `avg >= 8` but hard gate failed | Block PASS |
| Missing runtime/export/specialist evidence | NOT_VERIFIED and block claim |
| Q1 source candidate called pixel-polished | Report Q1 and continue rendered verification |
| Single screenshot called pixel-perfect | Q4 blocked; require locked reference, method, and tolerance |
| Static artifact forced through interactive gates | Use applicable domain reviewer |
| Best attempt called complete | Use bounded/blocking decision honestly |
