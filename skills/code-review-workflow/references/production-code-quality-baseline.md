# Production-Code Quality Baseline Review Adapter

Use this adapter when a code submission creates or materially changes production behavior.

The code-review workflow does not re-run the primary delivery lifecycle or replace the baseline. It consumes the submitted baseline report, verifies its evidence against the actual diff and repository state, and issues an independent technical verdict.

## Required input

```yaml
engineering_quality_baseline:
  production_code_applicability: <status>
  primary_lifecycle: <workflow>
  overlay: production-code-quality-baseline
  applicability_map: {}
  capabilities_resolved: []
  capabilities_executed: []
  capability_outputs: []
  tdd_evidence: []
  claims: []
  evidence_refs: []
  gate_results: []
  reviewer_results: []
  blocking_gaps: []
  final_quality_state: <status>
  transition_eligibility: {}
  remaining_authorities: []
```

For a production-code submission, a missing report is an evidence gap. It is not proof that no quality concern applies.

A legacy or externally produced submission may still be reviewed, but the reviewer must:

1. record the baseline as missing or partial;
2. classify which mandatory evidence can be reconstructed safely;
3. preserve unavailable TDD ordering as `NOT_VERIFIED` rather than inventing RED-before-GREEN history;
4. run applicable technical review domains;
5. issue `REQUEST CHANGES` or `BLOCKED` when a mandatory claim cannot be supported;
6. keep any accepted exception attributable to product/repository authority.

## Review classification

Add these fields to change classification:

```yaml
quality_baseline_review:
  production_code_applicability: <status>
  baseline_report: <present | partial | missing | not_applicable>
  primary_lifecycle_consistency: <pass | needs_work | not_verified>
  capability_execution_evidence: <pass | needs_work | not_verified>
  tdd_ordering_evidence: <pass | authorized_exception | needs_work | not_verified | not_applicable>
  conditional_applicability_map: <pass | needs_work | not_verified>
  mandatory_gate_state: <pass | pass_with_flags | needs_work | blocked | not_verified>
  remaining_authorities: []
```

## Non-collapse checks

Verify each distinction explicitly:

```text
selected or resolved capability ≠ executed capability
executed capability ≠ successful evidence
successful command ≠ clean-code or architecture approval
baseline self-review ≠ independent architecture review
architecture review ≠ code-review verdict
technical verdict ≠ merge authorization
merge authorization ≠ delivery or product acceptance
```

## Evidence review

### TDD

Accept RED-before-GREEN only when ordering evidence supports:

```text
failing behavior or regression reproduction
→ RED result
→ minimal implementation
→ GREEN result
→ refactor while green
```

Do not infer TDD from:

```text
test-file presence
file timestamps alone
final green suite
PR text claiming test-first
post-hoc regression coverage
```

An `AUTHORIZED_EXCEPTION` requires an external authority reference, bounded scope, reason, alternative verification, and residual risk.

### Clean code and module boundaries

The baseline report may provide findings and claims, but code review must inspect the actual changed implementation.

Verify:

```text
named readability or maintainability findings
repository vocabulary and conventions
behavior-preservation locks
module and ownership decisions
error and failure paths
smallest safe correction
no unrelated cleanup or abstraction ceremony
```

Lint, formatting, compilation, and tests are supporting evidence, not approval for this domain.

### Conditional design-quality concerns

For every concern, verify that the applicability result is evidence-backed:

```text
SOLID
DDD
design patterns
Clean Architecture
ports and adapters
security and threat modeling
performance
resilience and observability
data or migration safety
design and accessibility
```

`NOT_APPLICABLE` and `NOT_JUSTIFIED` are valid when supported. Do not request interfaces, patterns, entities, layers, or ports merely because a capability exists.

`NOT_VERIFIED` on a material concern remains an evidence gap.

## Verdict mapping

```text
APPROVED
  baseline report present or legitimately not applicable
  mandatory claims have appropriate evidence
  applicable specialists and independent reviews are resolved
  no blocking gap remains

REQUEST CHANGES
  missing or incorrect baseline evidence can be corrected
  TDD ordering, regression, clean-code, module, failure-path,
  conditional applicability, or reviewer evidence remains insufficient

BLOCKED
  a hard safety/authority boundary fails
  required evidence cannot be obtained responsibly
  a mandatory reviewer is unavailable
  the submission depends on a false or self-authorized exception
```

An approved technical verdict still reports merge authorization separately.

## Required report section

```markdown
## Production-Code Quality Baseline
- Production-code applicability: [...]
- Primary lifecycle and overlay consistency: [...]
- Baseline report: [present | partial | missing | N/A]
- Capabilities resolved/executed/evidenced: [...]
- TDD ordering or authorized exception: [...]
- Clean-code and module/failure-path result: [...]
- Conditional applicability map: [...]
- Mandatory gate result: [...]
- Blocking gaps: [...]
- Remaining authorities: [...]
```

Refer to:

```text
skills/production-code-quality-baseline/references/evidence-status-authority-matrix.md
```

for canonical adapter-level status and authority distinctions while the core RFC remains provisional.
