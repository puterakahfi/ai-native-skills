# Phase 10 — Design Review Facade Adapter

Use this reference after fresh verification of the current redesign artifact.

`redesign-workflow` supplies context and evidence. `design-review` owns classification, canonical gate resolution, applicability, scoring, coverage, verdict, and reporting. Built-in or external domain reviewers own specialist gates, evidence interpretation, hard-gate triggers, and correction knowledge.

Do not maintain a duplicate scorecard here.

## Entry condition

```text
□ current artifact exists in the declared artifact state
□ design domain and surface profile are resolved
□ role composition and reviewer coverage are explicit
□ required viewing contexts were captured
□ affected states/interactions were exercised when applicable
□ runtime, export, or specialist evidence was captured when required
□ preservation locks were checked
□ verification report belongs to the current iteration
□ evidence gaps are recorded honestly
```

A build alone is not visual verification. A screenshot alone is not interaction, runtime, responsive, export, or specialist-domain proof.

## Reviewer route

```text
digital-interface
  design-review facade
  + built-in interactive reviewer
  coverage: BUILT_IN

visual-communication
  design-review facade
  + built-in static reviewer
  coverage: BUILT_IN

presentation
  design-review facade
  + built-in presentation reviewer
  coverage: BUILT_IN

brand-identity
  design-review facade
  + brand-identity-review when available
  coverage: ADAPTER_COVERED
  fallback: LIMITED or ROUTE_ELSEWHERE

other
  design-review facade
  + declared external domain reviewer
  fallback: LIMITED or ROUTE_ELSEWHERE
```

Universal visual gates never replace a required specialist reviewer.

## Phase-specific loading

```text
CLASSIFY / ROUTE
  design-review/SKILL.md
  design-review/references/review-routing.md
  design-review/references/facade-boundary.md when coverage is unclear
  design-review/references/gate-registry.yaml for selected or prior gate IDs
  design-review/references/gate-migrations.yaml only for real aliases/deprecations
  design-review/references/review-profiles.md only for built-in profiles

UNIVERSAL REVIEW
  design-review/references/universal-gates.md

DOMAIN / SURFACE REVIEW
  design-review/references/interactive-surface-gates.md OR
  design-review/references/static-visual-gates.md OR
  loaded external domain reviewer

COMPONENT REVIEW
  design-review/references/component-review.md only for affected components

EVIDENCE + SCORE
  design-review/references/evidence-and-scoring.md

REPORT
  design-review/references/review-report.md
```

During a focused iteration, also use `iteration-review-mode.md`. Do not load the full gate inventory defensively.

## Route from redesign state

```yaml
review_route:
  design_domain: <domain>
  surface_profile: <profile>
  artifact_state: <rendered-interactive | rendered-static | source-only | mixed>
  review_depth: <focused | full | release>
  coverage_mode: <BUILT_IN | ADAPTER_COVERED | LIMITED | ROUTE_ELSEWHERE>
  domain_reviewers: []
  viewing_context: []
  selected_gate_ids: []
  selected_components: []
  changed_layers: []
  acceptance_criteria: []
  evidence_available: []
  evidence_gaps: []
  preservation_locks: []
```

Every selected or reported design gate must be active and canonical in the registry.

## Review mode

```text
focused
  target findings or changed layers
  adjacent regression gates
  preserved gates and locks
  affected contextual hard gates

full
  all applicable universal and loaded domain gates
  major present components
  full only with BUILT_IN or ADAPTER_COVERED primary-domain coverage

release
  full review
  required runtime/export/specialist production evidence
  all applicable contextual hard gates verified
  no complete approval with insufficient coverage
```

## Gate status preservation

Every selected gate receives exactly one:

```text
PASS
FAIL
PARTIAL
NOT_VERIFIED
NOT_APPLICABLE
```

Rules:

```text
missing evidence → NOT_VERIFIED, not FAIL and not zero
irrelevant gate → NOT_APPLICABLE
mixed verified scope → PARTIAL with missing scope named
FAIL/PARTIAL → eligible for defect handoff
NOT_VERIFIED → evidence gap or verification handoff, not design-fix evidence
```

## Verdict mapping

```text
PASS
  → delivery only when redesign acceptance criteria, preservation locks,
    required evidence, and contextual hard gates also pass

CONDITIONAL PASS
  → delivery only when remaining gaps are explicitly non-blocking,
    accepted, and inside the approval boundary

NEEDS WORK
  → Phase 11 defect classification when iterations remain

CRITICAL
  → block passing delivery and classify immediately

LIMITED REVIEW
  → load the required domain reviewer, narrow the approval claim,
    or hand off to the specialist

ROUTE ELSEWHERE
  → stop unsupported approval; do not continue scoring as if covered
```

An average at or above 8 never overrides a contextual hard-gate failure, missing primary-domain coverage, or required `NOT_VERIFIED` evidence.

## Defect handoff

For each failed or partial gate:

```yaml
defect_candidate:
  canonical_gate_id: <id>
  governing_reviewer: <built-in or external reviewer>
  status: <FAIL | PARTIAL>
  observation: <verified condition>
  evidence: []
  impact: <user, business, accessibility, fidelity, runtime, or delivery impact>
  affected_region: <region>
  recommendation: <correction direction>
  suspected_layer: <strategy | foundation | structure | component |
                    expression | interaction | content | implementation |
                    product-lock | domain-specialist>
```

Do not infer correction ownership from the visible symptom. Phase 11 owns classification.

For `NOT_VERIFIED`:

```yaml
evidence_gap:
  canonical_gate_id: <id>
  governing_reviewer: <reviewer>
  missing_evidence: []
  claim_blocked: <claim>
  next_verification: <required action>
```

## Review output

```markdown
## [target] · Redesign Review · Iteration [N]

**X.XX / 10** — [VERDICT] · Evidence coverage [X%]

- Design domain: [domain]
- Primary-domain coverage: [BUILT_IN | ADAPTER_COVERED | LIMITED | ROUTE_ELSEWHERE]
- Loaded reviewers: [reviewers]
- Contextual hard gates: [status]
- Acceptance criteria: [status]

### Findings
- `[gate]` [FAIL/PARTIAL] — [observation] → [correction direction]

### Not verified
- `[gate]` — [missing evidence and blocked claim]

### Preservation
- Passed: ...
- Failed: ...
- Not verified: ...

### Scope limitations
- ...

### Handoff
[delivery | defect classification | verification | domain reviewer | route elsewhere]
```

The full score/report semantics remain owned by `design-review/references/evidence-and-scoring.md` and `review-report.md`.