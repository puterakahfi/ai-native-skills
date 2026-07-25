# Evidence, Status, and Authority Matrix

Use this reference when producing or reviewing a `production-code-quality-baseline` handoff.

The matrix prevents four common collapses:

```text
applicability ≠ execution
execution ≠ evidence-backed gate result
technical review ≠ approval
approval ≠ merge or product authority unless policy says so
```

## 1. Applicability status

Applicability answers whether a concern materially belongs in the verified scope. It does not answer whether work passed.

| Status | Meaning | Minimum evidence | Effect |
|---|---|---|---|
| `APPLICABLE` | Material verified forces require the concern | affected boundary and trigger evidence | Load the owning specialist and require its output |
| `PARTIAL` | Only a bounded part of the concern applies | exact included and excluded scope | Load the specialist for the bounded slice |
| `NOT_APPLICABLE` | The concern is outside the verified behavior or boundary | inspectable absence-of-impact rationale | Do not load the specialist; retain the rationale |
| `NOT_JUSTIFIED` | The concern exists conceptually but current forces do not justify an abstraction or pattern | alternatives and force/trade-off assessment | Do not manufacture architecture |
| `NOT_VERIFIED` | Evidence is insufficient to decide | named evidence gap | Block a complete quality claim when material |
| `BLOCKED` | A prerequisite, authority, source, or safe execution path is unavailable | blocker and owner | Stop the affected slice |

### Applicability examples

```yaml
solid_design:
  status: NOT_JUSTIFIED
  evidence:
    - one cohesive implementation
    - no extension, substitution, client-interface, or dependency-direction pressure
  prohibited_action:
    - introduce an interface only to satisfy a checklist

domain_driven_design:
  status: APPLICABLE
  evidence:
    - conflicting business language across two bounded contexts
    - invariant cannot remain in transport or persistence code
  required_skill: domain-driven-design
```

## 2. Capability state

Capability state must be recorded as separate facts.

| State | Proves | Does not prove |
|---|---|---|
| Available | Capability exists in a catalog | Installed, selected, executed, or successful |
| Installed | Named runtime/profile can load it | Selected for this task or executed |
| Resolved | Router selected it for this scope | Started, completed, or produced evidence |
| Executed | An execution record and outputs exist | Outputs are correct or gates pass |
| Evidenced | Claims link to appropriate evidence | Independent review or authority exists |
| Reviewed | A reviewer issued a bounded verdict | Approval, merge authorization, delivery, or product acceptance |

Required handoff shape:

```yaml
capabilities_resolved: []
capabilities_executed: []
capability_outputs: []
claim_evidence_links: []
reviewer_results: []
```

Never replace these arrays with one undifferentiated `skills_used` list.

## 3. Gate status

Gate status answers whether one named quality obligation is satisfied.

| Status | Meaning | Blocking default |
|---|---|---|
| `PASS` | Claim-appropriate evidence fully satisfies the gate | No |
| `PASS_WITH_FLAGS` | Gate passes with explicit non-blocking risks | No, unless product policy says otherwise |
| `NEEDS_WORK` | Correctable material finding remains | Yes |
| `BLOCKED` | Safe completion is impossible under current prerequisites or authority | Yes |
| `NOT_APPLICABLE` | Gate is outside verified scope with evidence | No for that gate |
| `NOT_JUSTIFIED` | Requested abstraction/pattern is unsupported by forces | No; implementing it anyway is a defect |
| `NOT_VERIFIED` | Evidence is missing or insufficient | Yes when the gate is mandatory |
| `AUTHORIZED_EXCEPTION` | External authority accepted a bounded exception plus alternative verification | Policy-defined; never automatically PASS |

### Mandatory evidence examples

| Claim | Appropriate evidence | Insufficient evidence |
|---|---|---|
| TDD RED | failing test/reproduction before implementation plus ordering trace | test file exists; final suite is green |
| TDD GREEN | same focused test passes after minimal implementation | unrelated full-suite pass |
| Regression covered | focused regression and relevant suite pass | manual statement that bug is fixed |
| Clean code assessed | named findings, repository conventions, preservation locks, correction evidence | formatter/linter pass |
| SOLID assessed | force-by-force responsibility/substitution/interface/dependency analysis | interface count or DI container presence |
| DDD assessed | domain complexity, language, invariant, boundary evidence | entities/repositories exist |
| Pattern justified | problem forces, alternatives, trade-offs, smallest implementation | pattern name appears in code |
| Architecture accepted | independent architecture-review verdict against implemented diff | design plan, compilation, or owner self-review |
| User-facing behavior accepted | rendered/runtime/interaction/accessibility evidence as applicable | source and import inspection only |

## 4. TDD exception authority

A TDD exception is valid only when all fields exist:

```yaml
authorized_exception:
  authority_ref: <external product/repository authority>
  bounded_scope: <exact affected slice>
  reason: <why RED-GREEN cannot validly apply>
  alternative_verification: []
  residual_risk: []
  expiry_or_revisit: <condition>
```

Invalid exceptions:

```text
agent self-approval
inconvenience or time pressure alone
post-hoc tests labeled as test-first
missing alternative verification
repository-wide waiver for a bounded limitation
exception silently converted to PASS
```

## 5. Review and authority state

Record review and authority separately.

| Record | Owner | Answers |
|---|---|---|
| Implementation output | `master-engineer` / implementation owner | What changed and why? |
| Specialist assessment | Owning specialist | Is one concern applicable and satisfied? |
| Architecture review | Independent `architecture-review` | Is the implemented architecture acceptable? |
| Code review | `code-review-workflow` reviewer | What is the technical merge-readiness verdict? |
| Approval | Product/repository policy authority | Is the result approved within that authority scope? |
| Merge authorization | Repository-defined authority | May the PR be merged now? |
| Delivery record | Delivery owner | What was delivered, where, and with what evidence? |
| Product acceptance | Product acceptance owner | Did the delivered outcome satisfy product acceptance? |

Canonical non-collapse rules:

```text
architecture-review PASS ≠ code-review PASS
code-review PASS ≠ approval
approval ≠ merge authorization unless the policy explicitly grants it
merge ≠ deployment
technical delivery ≠ product acceptance
```

## 6. Final state calculation

Use the strongest truthful result:

```text
mandatory BLOCKED
  → final_quality_state: BLOCKED

mandatory NEEDS_WORK
  → final_quality_state: NEEDS_WORK

mandatory NOT_VERIFIED
  → final_quality_state: NOT_VERIFIED

all mandatory gates PASS, only accepted non-blocking flags remain
  → final_quality_state: PASS_WITH_FLAGS

all mandatory gates PASS with no material flags
  → final_quality_state: PASS
```

Transition eligibility remains separate:

```yaml
transition_eligibility:
  technical_completion: eligible | blocked
  review_ready: eligible | blocked
  merge_ready: eligible | blocked | product_policy_required
  delivery_ready: product_policy_required
  product_acceptance: product_policy_required
```

A technical `PASS` may still produce `merge_ready: product_policy_required`.

## 7. Minimum baseline report

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
  accepted_non_blocking_risks: []
  final_quality_state: <status>
  transition_eligibility: {}
  remaining_authorities: []
```

If any required field cannot be supported, preserve the gap explicitly. Do not infer PASS from a missing record.
