---
name: production-code-quality-baseline
description: Attach the default evidence-backed engineering quality overlay to substantive production-code work. Classify production impact, preserve one primary lifecycle, enforce TDD or an attributable exception, assess clean code and module boundaries, route conditional specialists only when justified, collect claim-appropriate evidence, and block unsupported completion or merge-readiness claims.
license: MIT
metadata:
  ai-native-skills.version: 0.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: workflow
  ai-native-skills.requires: "decision-provenance implementation-context-discovery master-engineer test-driven-development clean-code solid-design domain-driven-design design-patterns clean-architecture ports-and-adapters security-review threat-modeling resilience-engineering observability-design data-modeling design-review architecture-review code-review-workflow"
  ai-native-skills.skill_load_order: '[{"phase":"classify","load":["decision-provenance","implementation-context-discovery"]},{"phase":"plan","load":["master-engineer","test-driven-development"]},{"phase":"execute","load":["master-engineer","test-driven-development","clean-code"]},{"phase":"verify","load":["clean-code"]},{"phase":"review","load":["architecture-review","code-review-workflow"]},{"phase":"handoff","load":["decision-provenance"]}]'
  ai-native-skills.skills: '{"required":["decision-provenance","implementation-context-discovery","master-engineer","test-driven-development","clean-code","architecture-review","code-review-workflow"],"optional":["solid-design","domain-driven-design","design-patterns","clean-architecture","ports-and-adapters","security-review","threat-modeling","resilience-engineering","observability-design","data-modeling","design-review"]}'
  ai-native-skills.related_skills: '["workflow-router","role-switcher","new-feature-workflow","bugfix-workflow","spec-workflow","code-review-workflow","product-development-workflow"]'
---

# Production-Code Quality Baseline

## Status and ownership

This is a provisional executable adapter for the quality-lifecycle boundary tracked by:

```text
ai-native-core#56
ai-native-core#59
ai-native-skills#137
```

Until the core RFC is accepted and this adapter declares reviewed conformance, use the adjacent `contract.exemption.yaml` as the static ownership record.

Do not claim:

```text
core contract conformance
behavioral verification
runtime acceptance
product acceptance
approval or authorization
```

The overlay coordinates existing capabilities. It does not absorb their methods or replace their ownership.

## Core operating rule

```text
route one primary lifecycle
→ classify production-code applicability
→ attach this quality baseline as an overlay when applicable
→ classify always-required and conditional concerns
→ load phase-specific capabilities
→ execute and record observable outputs
→ collect claim-appropriate evidence
→ run independent architecture and code review
→ preserve remaining approval and merge authority
```

`production-code-quality-baseline` is never a competing primary lifecycle.

Examples:

```text
new feature
  primary_lifecycle: new-feature-workflow
  overlay: production-code-quality-baseline

bug or regression
  primary_lifecycle: bugfix-workflow
  overlay: production-code-quality-baseline

spec-driven implementation
  primary_lifecycle: spec-workflow and/or new-feature-workflow according to the accepted delivery topology
  overlay during production implementation: production-code-quality-baseline

code review only
  primary_lifecycle: code-review-workflow
  overlay: NOT_APPLICABLE unless the review is evaluating a prior baseline report
```

## Hard rules

1. Classify production impact before implementation.
2. Preserve exactly one primary lifecycle.
3. Attach the overlay automatically for substantive production-code work even when the user does not enumerate TDD, clean code, SOLID, DDD, patterns, architecture, or review.
4. Never treat available, listed, installed, or resolved capabilities as execution evidence.
5. Production behavior changes require RED → minimal GREEN → refactor while green, or an attributable authorized exception.
6. A test file, timestamp, or final green suite does not prove RED-before-GREEN ordering.
7. The agent cannot approve its own TDD or evidence exception.
8. Apply `clean-code` during implementation and verification for materially changed code.
9. Assess module ownership and error/failure paths without manufacturing abstractions.
10. Classify every conditional concern before final quality state.
11. Load a conditional specialist only when verified forces make it `APPLICABLE` or materially `PARTIAL`.
12. `NOT_APPLICABLE` and `NOT_JUSTIFIED` require inspectable rationale.
13. Silence or omission is `NOT_VERIFIED`, never PASS.
14. Green tests, lint, typecheck, or build do not prove clean-code, SOLID, DDD, pattern, or architecture quality.
15. PASS-like claims require claim-appropriate evidence.
16. Architecture review remains independent of implementation ownership.
17. Code review is required before merge authorization, but review does not create authorization.
18. Technical PASS does not self-authorize merge, delivery, release, production mutation, or product acceptance.
19. Product repositories own commands, thresholds, stack policy, exception authority, reviewer policy, and merge authority.
20. Generic performance specialist selection remains product-defined until a universal capability is published.

## Phase 1 — Classify

**Gate:** `production_code_applicability_must_be_classified_before_execution`

Classify from the requested outcome and repository impact:

```text
PRODUCTION_CODE_CHANGE
  creates or materially changes production behavior

NON_PRODUCTION_CHANGE
  no material production behavior impact

DISPOSABLE_EXPERIMENT
  explicitly bounded throwaway work with no production submission

NOT_VERIFIED
  impact or intended outcome is insufficiently established
```

Common `PRODUCTION_CODE_CHANGE` cases:

```text
new feature
bug fix
behavior change
behavior-preserving refactor
structural or data migration
production code generated for repository submission
```

Common non-production candidates:

```text
pure documentation
analysis without implementation
static configuration with no production behavior
explicit disposable experiment
```

A filename or artifact noun is not sufficient evidence. A “small config change” may still affect production behavior; a large analysis document may not.

Produce:

```yaml
production_code_applicability:
  status: PRODUCTION_CODE_CHANGE | NON_PRODUCTION_CHANGE | DISPOSABLE_EXPERIMENT | NOT_VERIFIED
  requested_outcome: <summary>
  repository_impact: <summary>
  evidence_refs: []
  exclusions: []
  blocking_gaps: []
```

When status is `NOT_VERIFIED`, stop any complete production-quality claim.

## Phase 2 — Plan the overlay

**Gate:** `baseline_plan_and_applicability_map_must_exist_before_implementation`

Record:

```yaml
engineering_quality_plan:
  primary_lifecycle: <workflow>
  overlay: production-code-quality-baseline
  issue_or_task_ref: <ref>
  effective_verified_scope:
    scope_in: []
    scope_out: []
    acceptance_criteria_refs: []
  repository_context_ref: <implementation-context-discovery output>
  always_required: []
  applicability_map: {}
  capabilities_resolved: []
  required_evidence: []
  required_reviewers: []
  product_policy_refs: []
```

### Always required

Evaluate for every `PRODUCTION_CODE_CHANGE`:

```text
scope and acceptance traceability
repository implementation context
behavior-test strategy
TDD or authorized exception
affected regression coverage
clean-code quality
module and ownership boundaries
error and failure-path behavior
product-defined technical checks
independent architecture review
code review before merge authorization
```

### Conditional applicability map

Classify every concern:

| Concern | Specialist when applicable | Material trigger |
|---|---|---|
| SOLID | `solid-design` | responsibility, extension, substitution, client-interface, or dependency pressure |
| Domain modeling | `domain-driven-design` | domain complexity, bounded contexts, invariants, ubiquitous language |
| Design pattern | `design-patterns` | recurring forces with evidence-backed trade-offs |
| Clean Architecture | `clean-architecture` | policy/mechanism or dependency-boundary pressure |
| Ports and adapters | `ports-and-adapters` | replaceable external boundary or dependency inversion need |
| Security | `security-review` | auth, data, trust boundary, secret, abuse, or permission risk |
| Threat modeling | `threat-modeling` | material attack surface or security-boundary change |
| Performance | product-defined specialist | latency, throughput, memory, cost, or scale risk |
| Resilience | `resilience-engineering` | timeout, retry, recovery, degradation, or failure-mode risk |
| Observability | `observability-design` | operational visibility, diagnosis, or runtime evidence need |
| Data/migration | `data-modeling` | shape, integrity, compatibility, or migration risk |
| Design/accessibility | `design-review` plus domain reviewer | changed user-facing or rendered behavior |

Valid statuses:

```text
APPLICABLE
PARTIAL
NOT_APPLICABLE
NOT_JUSTIFIED
NOT_VERIFIED
BLOCKED
```

Example:

```yaml
applicability_map:
  solid_design:
    status: NOT_JUSTIFIED
    rationale: cohesive bounded function with no responsibility, extension, substitution, client-interface, or dependency pressure
    evidence_refs: [<ref>]
  domain_driven_design:
    status: NOT_APPLICABLE
    rationale: thin data pass-through with no material domain invariant or bounded-context decision
    evidence_refs: [<ref>]
  performance:
    status: PARTIAL
    specialist: <product-defined>
    rationale: query path affects an existing latency objective
    evidence_refs: [<ref>]
```

No verified force means do not manufacture interfaces, factories, patterns, entities, repositories, layers, ports, or use cases.

## Phase 3 — Execute

**Gate:** `implementation_must_follow_test_and_quality_plan`

Load:

```text
master-engineer
test-driven-development
clean-code
conditional specialists with APPLICABLE or material PARTIAL status
```

### TDD evidence sequence

For production behavior changes:

```text
failing behavior or regression reproduction
→ RED evidence
→ minimal passing implementation
→ GREEN evidence
→ refactor while tests remain green
```

Record observable evidence:

```yaml
tdd_evidence:
  failing_behavior_ref: <ref>
  red_result_ref: <ref>
  implementation_ref: <ref>
  green_result_ref: <ref>
  refactor_result_ref: <ref | null>
  ordering_evidence: []
  status: PASS | AUTHORIZED_EXCEPTION | NEEDS_WORK | NOT_VERIFIED | NOT_APPLICABLE
```

An authorized exception requires:

```yaml
authorized_exception:
  authority_ref: <external product/repository authority>
  bounded_scope: <scope>
  reason: <why TDD cannot validly apply>
  alternative_verification: []
  residual_risk: []
```

`AUTHORIZED_EXCEPTION` is not automatically PASS.

### Clean-code and boundary execution

Apply `clean-code` to the changed implementation. Preserve behavior, repository conventions, and scope. Do not use arbitrary line limits or unrelated cleanup.

Assess:

```text
readability and maintainability findings
named smells with evidence
behavior-change risk
module/service ownership
failure and error paths
smallest safe corrections
verification evidence and gaps
```

## Phase 4 — Verify claims and evidence

**Gate:** `mandatory_claims_must_have_claim_appropriate_evidence`

Distinguish:

```text
capabilities_resolved
capabilities_executed
outputs_produced
claims_made
evidence_refs
gate_results
reviewer_results
```

These are not interchangeable.

Examples:

```text
test command output
  may support test/build behavior
  does not prove clean-code or architecture quality

source mapping
  may support repository-convention alignment
  does not prove runtime, visual, or accessibility acceptance

specialist report
  may support its named concern
  does not create approval or merge authorization
```

Use claim-specific records:

```yaml
quality_claims:
- id: <claim-id>
  claim: <bounded statement>
  concern: <tdd | regression | clean_code | module_boundary | solid | ddd | pattern | architecture | command | runtime | design>
  evidence_refs: []
  reviewer_ref: <ref | null>
  status: PASS | PASS_WITH_FLAGS | NEEDS_WORK | BLOCKED | NOT_APPLICABLE | NOT_JUSTIFIED | NOT_VERIFIED | AUTHORIZED_EXCEPTION
```

Missing evidence remains visible as `NOT_VERIFIED` and a blocking gap when mandatory.

## Phase 5 — Independent review

**Gate:** `independent_architecture_and_code_review_required_before_merge_readiness`

Run:

```text
architecture-review
→ code-review-workflow
```

Architecture review evaluates the implemented design and evidence. Pre-code planning, green CI, or implementation-owner self-review cannot replace it.

Code review maps technical evidence and findings to merge readiness. It does not grant merge authority unless a separate product policy explicitly gives that actor the authority.

Record:

```yaml
reviewer_results:
  architecture_review:
    reviewer_ref: <ref>
    verdict: <verdict>
    evidence_refs: []
    findings: []
  code_review:
    reviewer_ref: <ref>
    verdict: <verdict>
    evidence_refs: []
    findings: []
remaining_authorities:
  approval_refs: []
  merge_authorization_ref: <ref | null>
  product_acceptance_ref: <ref | null>
```

## Phase 6 — Handoff

**Gate:** `final_quality_state_must_preserve_blocking_gaps_and_authority_boundaries`

Produce:

```yaml
engineering_quality_baseline:
  production_code_applicability: <status>
  primary_lifecycle: <workflow>
  overlay: production-code-quality-baseline
  core_candidate_ref: puterakahfi/ai-native-core#59
  assessments: []
  capabilities_resolved: []
  capabilities_executed: []
  tdd_evidence: []
  claims: []
  evidence_refs: []
  gate_results: []
  reviewer_results: []
  blocking_gaps: []
  final_quality_state: PASS | PASS_WITH_FLAGS | NEEDS_WORK | BLOCKED | NOT_VERIFIED
  transition_eligibility: <eligible | blocked | product_policy_required>
  remaining_authorities: []
```

### Blocking rules

```text
mandatory NEEDS_WORK, BLOCKED, or NOT_VERIFIED
  → block complete or merge-ready claim

TDD exception without attributable authority
  → BLOCKED

required capability only resolved, not executed
  → NOT_VERIFIED

architecture review missing
  → complete architecture acceptance blocked

code review missing
  → merge readiness blocked

technical PASS with no merge authority
  → product_policy_required
```

## Failure modes

Stop or downgrade the result when:

- production impact is unknown;
- the primary lifecycle is missing or replaced by the overlay;
- implementation starts before the baseline plan;
- RED-before-GREEN evidence is missing;
- an exception is self-authorized;
- a conditional concern is silently skipped;
- an unregistered capability ID is invented;
- commands are used as proof for unrelated design-quality claims;
- required reviewer evidence is missing;
- blocking gaps are hidden;
- technical review is presented as approval, merge authorization, delivery, or product acceptance.

## Handoffs

```text
workflow-router
  owns lifecycle selection and overlay attachment

primary workflow
  owns delivery sequence

role-switcher
  owns owner/specialist/reviewer composition

individual engineering skills
  own their specialist methods

architecture-review and code-review-workflow
  own independent technical review

Native AI OS
  owns runtime resolution, execution records, evidence persistence, gate evaluation, transition enforcement, and observability

product repository
  owns commands, thresholds, exception authority, merge authority, release, and product acceptance
```
