# Phases 1–5: Discovery → Implementation

## Phase 1 — Discovery

**Goal:** Understand the product opportunity before defining a solution.

Load on entry:

```text
model-selection
user-research
business-value-alignment
experiment-design
product-manager
decision-making
```

Produce:

```text
target user segments
jobs-to-be-done and pains
existing alternatives and workarounds
opportunity and business-value brief
success signals and open assumptions
experiment recommendation when evidence is weak
ranked product direction
```

**Gate:** opportunity and business value are explicit before PRD. An `EXPERIMENT_FIRST` verdict must produce an experiment design before PRD/build.

**Done when:** one direction is recommended with user value, business value, metrics, assumptions, and experiment plan when needed.

---

## Phase 2 — Requirements / PRD

**Goal:** Convert the approved opportunity into a testable product contract.

Load on entry:

```text
product-requirements
business-value-alignment
product-manager
```

Produce:

```text
problem statement and target users
goals and non-goals
user and business value
success metrics
scope in/out
functional and non-functional requirements
observable acceptance criteria
constraints, dependencies, risks, and open questions
launch criteria
```

Every acceptance criterion needs a stable ID because implementation and Phase 6 evidence must trace back to it.

```yaml
acceptance_criterion:
  id: AC-01
  outcome: <observable behavior or result>
  context: <user, state, device, data, or system condition>
  evidence_plan: []
  affected_domains: []
```

**Gate:** PRD readiness passes before MVP planning or technical specification.

**Done when:** `PRD READINESS` is `READY`, or explicit blockers prevent progress.

---

## Phase 3 — MVP Slice

**Goal:** Select the smallest valuable release slice or experiment.

Load on entry:

```text
business-value-alignment
experiment-design
product-manager
decision-making
spike when a reversible uncertainty needs proof
```

Produce:

```text
MVP scope in/out
included PRD acceptance-criterion IDs
deferred criteria and scope
success metric mapping
experiment or validation plan
risks and assumptions
```

Removing a criterion from the MVP requires an explicit scope decision; it cannot simply disappear from the later acceptance matrix.

**Gate:** the slice is smaller than the full product and maps to value and success metrics.

**Done when:** one MVP slice is approved.

---

## Phase 4 — Technical Spec

**Goal:** Translate the approved PRD/MVP into agent-executable work and evidence plans.

Load on entry:

```text
spec-workflow
native-ai-engineer
master-engineer
api-contract
data-modeling
diagram-architect when decision-bearing diagrams help
```

Produce:

```text
architecture and design constraints
technical specification
tasks and context packs
criterion-to-task traceability
affected-domain classification
verification and preview/runtime plan
required reviewer plan
```

Minimum traceability:

```yaml
task:
  id: TASK-01
  acceptance_criteria: [AC-01, AC-03]
  affected_domains: [logic, user_facing_design]
  evidence_required: []
```

**Gate:** every implementation task traces to one or more in-scope PRD criteria.

**Done when:** the technical plan can produce direct evidence for each criterion.

---

## Phase 5 — Implementation

**Goal:** Build and verify the approved MVP feature slices without losing product-level traceability.

Load on entry:

```text
new-feature-workflow
test-driven-development
master-engineer
systematic-debugging when failures occur
```

Run each implementation slice through `new-feature-workflow`:

```text
plan against existing PRD/spec
→ pre-implementation design decision when affected
→ implement with tests
→ technical and rendered/static verification
→ submit evidence
→ code-review-workflow verdict
```

Produce one package per feature slice:

```yaml
feature_evidence_package:
  feature: <feature>
  acceptance_criteria: []
  changed_files_or_artifacts: []
  technical_evidence: []
  design_route_and_verdict: <value or NOT_APPLICABLE>
  security_performance_accessibility_evidence: []
  code_review_verdict: <APPROVED | REQUEST CHANGES | BLOCKED>
  known_limitations: []
  accepted_risks: []
```

Rules:

```text
REQUEST CHANGES or BLOCKED returns to implementation/verification
source-only user-facing changes remain NOT_VERIFIED
feature-level PASS does not yet prove cross-feature product acceptance
scope drift requires PRD/MVP/spec update and reapproval
```

**Gate:** every completed feature traces to acceptance criteria, contains direct evidence, and receives the required code-review verdict.

**Done when:** all feature slices needed by the MVP have reviewable evidence packages ready for product-level reconciliation in Phase 6.