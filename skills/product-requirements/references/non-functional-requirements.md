# Non-Functional Requirements

Load this reference when a Feature or Full Product PRD needs quality-attribute coverage.

## Applicability rule

For each material quality domain, record one of:

```text
REQUIRED        product behavior or threshold must be specified
CONSTRAINED     an attributable external or technical constraint controls it
NOT_APPLICABLE  the domain does not materially apply, with rationale
NOT_VERIFIED    applicability or target cannot yet be proven
```

Silence is not `NOT_APPLICABLE`. High-risk domains must not be omitted because the user did not mention them.

## Core domains

| Domain | Typical product question | Example requirement shape |
|---|---|---|
| Performance | How quickly must the user-observable outcome occur? | `NFR-PERF-1: 95% of draft-generation requests return a usable result within the product-defined threshold.` |
| Reliability | What failure rate, recovery, or continuity is acceptable? | `NFR-REL-1: A failed generation can be retried without losing supplied input.` |
| Availability | When and where must the capability be usable? | State hours, environments, or product-defined SLO only when attributable. |
| Security | What abuse, access, or trust boundary must be protected? | Define authentication, authorization, data exposure, or review expectations at product level. |
| Privacy | What user data is collected, retained, exposed, or deleted? | Define consent, minimization, retention, or deletion outcomes. |
| Accessibility | Which users and interactions must be supported? | Define keyboard, semantics, contrast, screen-reader, motion, or product-defined standard. |
| Usability | What completion, learnability, or recovery outcome is required? | Define observable task completion or error recovery, not “easy to use.” |
| Compatibility | Which supported clients, surfaces, formats, or integrations matter? | Name attributable browser/device/API/version boundaries. |
| Observability | Which product and operational signals must exist for acceptance? | Name required events, health signals, failure categories, and ownership. |
| Compliance | Which verified legal, regulatory, policy, or contractual obligations apply? | Reference the exact source and scope; do not invent obligations. |
| Maintainability constraint | Which product-approved reversibility or modularity constraint is mandatory? | Keep detailed architecture in solution design; record only attributable product constraints. |
| Cost/usage guardrail | Which product promise depends on cost, quota, latency, or external provider limits? | Define user-visible limits and ownership without guessing provider behavior. |

## Context overlays

### Web application

Review performance, responsive behavior, accessibility, browser compatibility, security, privacy, analytics, error recovery, and operational observability.

### API or service

Review contract compatibility, authentication/authorization, rate/usage behavior, latency, reliability, idempotency/retry semantics, error model, observability, and data handling. Detailed protocol design belongs downstream.

### Internal tool

Review permission scope, auditability, data sensitivity, reliability, supported environment, recovery, and operational ownership. “Internal” does not remove security or privacy obligations.

### AI-generation product

Review output failure/recovery, latency expectations, quality guardrails, harmful or disallowed output handling when relevant, provenance/disclosure requirements, input/output privacy, model/provider limits, cost ownership, and evaluation evidence.

### ChatGPT App or MCP-backed product

Review target ChatGPT surface, authentication/authorization, data scope, tool side effects, user confirmation, native generation versus developer API boundaries, plan/workspace assumptions, capability availability, privacy, accessibility, and production endpoint observability. Verify current platform rules through the platform specialist.

### High-risk or regulated context

Load applicable security, privacy, compliance, safety, and domain reviewers. Missing authoritative obligations remain `NOT_VERIFIED` and may block readiness.

## NFR record

```yaml
non_functional_requirement:
  id: NFR-1
  domain: performance | reliability | security | privacy | accessibility | other
  applicability: REQUIRED | CONSTRAINED | NOT_APPLICABLE | NOT_VERIFIED
  statement: ""
  target_or_threshold: ""
  rationale: ""
  source_refs: []
  acceptance_criteria: []
  verification_method: ""
```

Avoid invented universal thresholds. A numeric target must be attributable to product policy, evidence, constraint, or an explicitly approved experiment.

## Readiness effects

Return `NEEDS_REVISION` when a relevant NFR is acknowledged but vague, untestable, or untraced.

Return `BLOCKED` when:

- a mandatory security, privacy, compliance, safety, or accessibility obligation is unresolved;
- the product promise materially depends on a provider limit, cost owner, or availability claim that is not verified;
- required runtime evidence cannot be obtained before the decision boundary.

A `NOT_APPLICABLE` entry passes only when the rationale is credible for the exact product scope.
