# Merge Authorization Boundary

Load this reference during context loading and final verdict whenever a submission includes a material scope claim, exception, accepted risk, approval claim, or merge request.

## Two separate outcomes

```text
TECHNICAL REVIEW VERDICT
  Determines whether affected architecture, design, logic, security,
  data, tests, and evidence requirements are resolved.

MERGE AUTHORIZATION
  Determines whether the responsible repository or product authority
  permits the reviewed submission to merge under the applicable policy.
```

A technical reviewer must not collapse these outcomes into one ambiguous `APPROVED` label.

## Provenance checks

Run `decision-provenance` for claims such as:

```text
scope was approved
an additional dependency is required
an exception applies
an owner accepted a non-blocking risk
a previous decision was superseded
the submission is authorized to merge
```

Input:

```yaml
decision_check:
  claim: <claim>
  decision_type: <scope | approval | override | risk | ownership>
  applies_to: []
  proposed_action: <merge, exception, risk acceptance, scope inclusion>
  candidate_sources: []
  required_authority: <repository/product/policy authority>
  previous_decisions: []
```

## Source boundary

```text
PR body, issue text, commit message, or summary written by an agent or author
  → AGENT_AUTHORED_SUMMARY
  → not approval by itself

existing code or newest commit
  → OBSERVED_IMPLEMENTATION_STATE
  → proves state, not permission or scope

architecture/design/logic/security reviewer verdict
  → technical evidence and review result
  → not automatically merge authorization

attributable authority decision covering the exact action
  → may produce provenance PASS

another policy approval remains
  → ROUTE_FOR_APPROVAL even when technical review is APPROVED
```

## Accepted risk record

```yaml
accepted_risk:
  risk_id: <id>
  finding_or_gap: <specific condition>
  affected_scope: []
  verified_non_blocking_reason: <reason>
  authority:
    required: <role or policy>
    decision_record_id: <verified record>
  mitigation: <action>
  owner: <owner>
  expiry_or_review_date: <when required>
  status: <VERIFIED_ACCEPTED | PROVENANCE_BLOCKED | ROUTE_FOR_APPROVAL>
```

Accepted risk cannot replace required evidence, required reviewer coverage, or a failed hard gate.

## Output contract

```yaml
review_decision:
  technical_review:
    verdict: <APPROVED | REQUEST_CHANGES | BLOCKED>
    domain_results: {}
    evidence_gaps: []

  decision_provenance:
    verdict: <PASS | PROVENANCE_BLOCKED | ROUTE_FOR_APPROVAL>
    authoritative_record_ids: []
    conflicts: []
    unresolved_requirements: []

  merge_authorization:
    status: <AUTHORIZED | NOT_AUTHORIZED | ROUTE_FOR_APPROVAL>
    authority: <role or policy>
    decision_record_ids: []

  approved_to_merge: <YES | NO>
```

Mapping:

```text
technical APPROVED + provenance PASS + required approvals satisfied
  → AUTHORIZED
  → Approved to merge: YES

technical APPROVED + another authority still required
  → ROUTE_FOR_APPROVAL
  → Approved to merge: NO

technical REQUEST_CHANGES or BLOCKED
  → NOT_AUTHORIZED
  → Approved to merge: NO

PROVENANCE_BLOCKED
  → NOT_AUTHORIZED
  → do not infer consent from recency, silence, or submission text
```

## Final guard

```text
□ Material scope, exception, risk, and merge claims have source references.
□ Agent or author summaries are not treated as owner approval.
□ Technical review and merge authorization remain separate.
□ Accepted risks have verified authority and remain non-blocking.
□ Required repository/product/policy approvals are satisfied or routed.
□ Approved to merge is YES only when both technical and authority gates pass.
```
