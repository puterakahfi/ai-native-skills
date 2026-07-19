# Phases 1–5: Discovery → Implementation

## Phase 1 — Discovery

**Goal:** Understand the opportunity, evidence quality, and likely decision owners before defining a solution.

Load:

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
target users and jobs-to-be-done
pains, alternatives, and workarounds
opportunity and business-value brief
success signals and open assumptions
experiment recommendation when evidence is weak
ranked product direction
decision domains and likely responsible owners
```

**Gate:** opportunity, value, evidence gaps, and decision owners are explicit before PRD.

An `EXPERIMENT_FIRST` verdict produces an experiment design before PRD/build.

---

## Phase 2 — Requirements / PRD

**Goal:** Convert the recommended opportunity into a testable product contract with verified scope authority.

Load:

```text
product-requirements
business-value-alignment
product-manager
decision-provenance
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
decision sources and required authorities
```

Every acceptance criterion needs a stable ID:

```yaml
acceptance_criterion:
  id: AC-01
  outcome: <observable behavior or result>
  context: <user, state, device, data, or system condition>
  evidence_plan: []
  affected_domains: []
  scope_decision_record_ids: []
```

Run `decision-provenance` before calling a PRD approved or ready for downstream execution.

```text
agent-generated PRD draft
  → useful artifact
  → not owner approval by itself

verified authority covers the exact PRD version and scope
  → PRD may be treated as effective

conflict or missing authority
  → PROVENANCE_BLOCKED or ROUTE_FOR_APPROVAL
```

**Gate:** PRD readiness and scope provenance pass before MVP planning or technical specification.

---

## Phase 3 — MVP Slice

**Goal:** Select the smallest valuable release slice or experiment and verify who approved it.

Load:

```text
business-value-alignment
experiment-design
product-manager
decision-making
decision-provenance
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
MVP decision record IDs
```

Removing or deferring a criterion requires an explicit bounded scope decision; it cannot silently disappear from the later acceptance matrix.

```text
verified MVP decision
  → record effective scope and deferred criteria

agent summary or newest document only
  → NON_AUTHORITATIVE
  → keep previous verified scope

additional authority required
  → ROUTE_FOR_APPROVAL
```

**Gate:** the slice is smaller than the full product, value-aligned, and approved by the required authority.

---

## Phase 4 — Technical Spec

**Goal:** Translate the verified PRD/MVP into agent-executable work and evidence plans.

Load:

```text
spec-workflow
native-ai-engineer
master-engineer
api-contract
data-modeling
diagram-architect when useful
decision-provenance when a new dependency or boundary is introduced
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
approved dependency and exception records
```

Minimum traceability:

```yaml
task:
  id: TASK-01
  acceptance_criteria: [AC-01, AC-03]
  affected_domains: [logic, user_facing_design]
  evidence_required: []
  decision_record_ids: []
```

A dependency, route, data boundary, or exception absent from the verified PRD/MVP must be approved or routed before implementation.

**Gate:** every task traces to one or more in-scope criteria and every material expansion has decision provenance.

---

## Phase 5 — Implementation

**Goal:** Build and verify approved MVP slices without losing product-level traceability.

Load:

```text
new-feature-workflow
test-driven-development
master-engineer
systematic-debugging when failures occur
```

Run each slice through `new-feature-workflow`:

```text
plan against verified PRD/MVP/spec
→ verify feature scope and design-decision authority
→ implement with tests
→ technical and rendered/static verification
→ submit decision/evidence handoff
→ code-review technical verdict + merge authorization
```

Produce one package per slice:

```yaml
feature_evidence_package:
  feature: <feature>
  acceptance_criteria: []
  effective_verified_scope: []
  decision_provenance_report: <reference>
  changed_files_or_artifacts: []
  technical_evidence: []
  design_route_and_verdict: <value or NOT_APPLICABLE>
  other_domain_evidence: []
  code_review_verdict: <APPROVED | REQUEST CHANGES | BLOCKED>
  merge_authorization: <AUTHORIZED | NOT_AUTHORIZED | ROUTE_FOR_APPROVAL>
  known_limitations: []
  accepted_risks: []
```

Rules:

```text
REQUEST CHANGES or BLOCKED returns to implementation/verification
NOT_AUTHORIZED or ROUTE_FOR_APPROVAL blocks merge action
source-only user-facing changes remain NOT_VERIFIED
feature-level PASS does not prove cross-feature product acceptance
scope drift requires provenance-backed PRD/MVP/spec update
```

**Gate:** every completed slice traces to criteria, contains direct evidence, preserves verified scope, and has required review/authorization statuses.

**Done when:** all slices needed by the MVP have evidence packages ready for Phase 6 reconciliation.
