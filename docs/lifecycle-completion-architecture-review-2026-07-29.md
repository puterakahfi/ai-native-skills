# Architecture Review — AI-Native Engineering Lifecycle Completion Decision

Issue: `puterakahfi/ai-native-skills#247`  
Reviewed artifact: `docs/lifecycle-completion-architecture-decision-2026-07-29.md`  
Base: `246-lifecycle-completion@5cd82bb18bd20a286a1ce4a8224c8dc76e4dd7b6`  
Reviewed head after decision commit: `247-lifecycle-semantics-decision@1f7ff8104ee1ec71409496cb50f5b3363bfed6b9`  
Date: 2026-07-29

## Review context

```yaml
review_capability: architecture-review
review_scope: lifecycle_semantics_repository_ownership_and_runtime_boundary
engineering_contracts:
  - ai-native-core/contracts/workflows/product-development.contract.yaml@0.4.0
  - ai-native-core/contracts/skills/meta/workflow-router.contract.yaml@0.2.1
  - ai-native-core/contracts/skills/meta/role-switcher.contract.yaml@0.1.0
repository_contracts:
  - CONTRIBUTING.md
  - docs/skills.md
  - docs/facade-skill-pattern.md
implementation_context:
  changed_files:
    - docs/lifecycle-completion-architecture-decision-2026-07-29.md
  code_or_dependency_change: false
review_independence: LIMITED_SAME_EXECUTION_CONTEXT
```

## Verdict

```text
ARCHITECTURE REVIEW VERDICT
───────────────────────────
Status: PASS WITH FLAGS

Mapping conformance: PASS
ADR required: SATISFIED_BY_DECISION_RECORD
Core RFC required now: NO
New dependencies flagged: none
Parallel lifecycle/router systems flagged: none
Blocking violations: none
Review independence: LIMITED
Owner approval: ROUTE_FOR_APPROVAL
```

## Contract checks

### 1. Single lifecycle ownership

**PASS**

The decision retains `product-development-workflow` as the single product-from-zero lifecycle. It does not introduce `ai-native-engineering-workflow`, a phase-13 product lifecycle, or a competing maintenance workflow.

### 2. Router and role boundaries

**PASS WITH FLAG**

`workflow-router` remains the primary-route selector and `role-switcher` remains the role-composition owner. `maintenance-case` is bounded to signal qualification, shared evidence, case closure, and routing input.

Flag `AR-01`: Any new active-incident or maintenance route vocabulary added by #249 must be declared as an adapter-local extension or use the existing fallback boundary. It must not be represented as canonical Core route semantics without an approved Core RFC.

### 3. Facade applicability

**PASS**

Both proposed capabilities perform coherent domain work beyond routing:

- `documentation-assurance` owns applicability, document mapping, evidence normalization, consistency, and verdict;
- `maintenance-case` owns signal qualification, evidence normalization, bounded case state, outcome, and follow-up.

They therefore fit the facade-skill pattern and do not require new official package types.

### 4. Documentation lifecycle boundary

**PASS WITH FLAG**

Documentation assurance is cross-cutting and does not absorb product-specific content ownership.

Flag `AR-02`: #248 may add stricter adapter-layer completion gates, but must report them as local executable behavior. Promotion to universal Core obligations remains deferred until real transfer evidence is reviewed in #251.

### 5. Operate-and-maintain semantics

**PASS**

A recurring loop correctly preserves both continuous product observation and bounded maintenance-case completion. Existing incident, bugfix, feature, design, deployment, and product-validation owners remain intact.

### 6. Runtime state separation

**PASS WITH REQUIRED FOLLOW-UP**

The decision aligns with the runtime operating-state separation being developed in `ai-native-os#92`: plan, execution, claim, evidence, gate, review, approval, delivery, and product acceptance remain separate.

Required follow-up `AR-03`: #250 must remove or migrate the experimental `EXECUTED → REVIEWED` capability-node transition. Review must be represented as a linked review record or projection, not execution state.

### 7. Cross-repository ownership

**PASS**

- Core retains canonical meaning.
- Skills retains executable procedures and composition.
- Runtime retains state, validation, and persistence.
- Product repositories retain local policy, environment, documentation content, authorization, and product acceptance.

No product-specific policy is moved into reusable Core or Skills artifacts.

### 8. Core RFC verdict

**PASS WITH PROMOTION GATE**

`NO_CORE_CHANGE_FOR_MVP` is proportionate because no canonical product phase is changed and the proposed facades have no independent real-product plus real-maintenance proof yet.

Promotion gate `AR-04`: #251 must run `skill-evolution`; a future RFC requires stable cross-adapter semantics, compatibility impact, required fields/gates, and verified source cases.

### 9. Delivery topology

**PASS WITH AUTHORITY FLAG**

The integration-branch topology is appropriate for dependent epic slices:

```text
child PRs → 246-lifecycle-completion
final integrated PR → main after #251
```

Flag `AR-05`: Creating branches is executed and evidenced. Merge authorization for child and final PRs remains separate and is not granted by this review.

### 10. Validation depth

**NOT_APPLICABLE for executable tests**

This slice adds architecture documentation only. No code, scripts, package manifests, contracts, or capability metadata are changed.

Required validation before merge:

- inspect rendered Markdown and links;
- verify branch base and PR target;
- verify the PR references #247 and #246;
- owner review of material decisions;
- disclose limited reviewer independence.

## Findings

| ID | Severity | Finding | Required action |
|---|---|---|---|
| `AR-01` | Warning | New route vocabulary could silently exceed the Core router contract. | Keep adapter-local/fallback semantics or create an approved Core RFC later. |
| `AR-02` | Warning | Universal documentation-gate claims are not yet real-world validated. | Implement locally in #248 and evaluate promotion in #251. |
| `AR-03` | Required downstream | Experimental orchestration conflates execution and review state. | Correct in #250 without changing Core silently. |
| `AR-04` | Promotion gate | Core promotion lacks independent source cases. | Run product and maintenance validation before RFC. |
| `AR-05` | Authority | Branch creation is not merge authorization. | Obtain owner review and explicit merge authority. |
| `AR-06` | Review limitation | Reviewer and author share one execution context. | Treat this review as `LIMITED`; owner or separate reviewer must confirm before acceptance. |

## Auto-fail checks

| Check | Result |
|---|---|
| Competing lifecycle introduced | PASS — none |
| Competing router introduced | PASS — none |
| Product-specific policy leaked into reusable layer | PASS — none |
| Runtime implementation detail promoted to Core | PASS — none |
| Review/approval/authorization conflated | PASS — none |
| Unapproved dependency or framework introduced | NOT_APPLICABLE |
| Executable behavior changed without tests | NOT_APPLICABLE |

## Recommendation

Proceed to a draft PR targeting `246-lifecycle-completion` and route the decision to owner review.

Do not start #248 or #249 as implementation-complete work until:

1. the decision is reviewed and approved;
2. the child PR target is confirmed;
3. `AR-01` through `AR-06` are preserved as downstream constraints.

## Review receipt

```yaml
architecture_review:
  verdict: PASS_WITH_FLAGS
  blocking_violations: []
  warnings:
    - AR-01
    - AR-02
    - AR-05
  required_downstream_actions:
    - AR-03
    - AR-04
  independence: LIMITED
  owner_approval: ROUTE_FOR_APPROVAL
  merge_authorization: NOT_GRANTED
```
