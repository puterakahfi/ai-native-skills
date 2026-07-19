# Phases 6–10: Acceptance → Learn

## Phase 6 — Product Acceptance Verification

**Goal:** Prove the complete verified MVP satisfies every in-scope PRD criterion and reconcile accepted-risk authority.

Load:

```text
skill-eval
code-review-workflow
decision-provenance
```

Load domain reviewers only when affected:

```text
design-review
security-review
threat-modeling
web-performance
accessibility
```

Load `acceptance-and-release.md` for the complete contract.

Inputs:

```text
effective verified PRD and MVP scope
decision provenance report and authoritative record IDs
technical specification
all feature evidence packages
code-review verdicts and merge authorization statuses
domain review routes and verdicts
known limitations and proposed accepted risks
```

Produce:

```text
one acceptance-matrix row per in-scope criterion
reviewer and evidence coverage summary
decision provenance summary
hard-gate status
release blockers
verified accepted-risk register
RELEASE_READY or NOT_READY verdict
release approval status
```

Critical rules:

```text
feature merged ≠ complete product accepted
green tests ≠ every criterion verified
screenshot ≠ runtime or hidden-state proof
NOT_VERIFIED blocks readiness unless scope is formally changed by verified authority
LIMITED REVIEW blocks required complete-domain acceptance
code-review-workflow must be technically APPROVED
accepted risk requires attributable authority
RELEASE_READY ≠ automatic release approval
```

**Gate:** every in-scope criterion has direct evidence, explicit status, required reviewer coverage, decision provenance, and no unresolved blocker.

**Done when:** acceptance is `RELEASE_READY` or `NOT_READY`, and the release approval status is reported separately.

---

## Phase 7 — Release Preparation

**Goal:** Prepare traceable release artifacts for a release-ready MVP while preserving the approval boundary.

Entry conditions:

```text
Phase 6 eligibility = RELEASE_READY
release approval = APPROVED or ROUTE_FOR_APPROVAL
```

When `NOT_READY`, return to implementation, verification, review, domain coverage, or a formally approved scope update.

Load:

```text
git-workflow
decision-provenance
deployment-workflow when release preparation needs deployment constraints
```

Produce:

```text
release notes
version or tag plan
changelog
acceptance-matrix reference
decision-record reference
accepted-risk reference
rollback plan
release approval status
```

Rules:

```text
release artifacts preserve the exact accepted scope
new changes invalidate affected evidence and require re-verification
agent-authored release notes are not release approval
ROUTE_FOR_APPROVAL permits preparation but not the release action
```

**Gate:** `RELEASE_READY`, traceable artifacts, rollback plan, and explicit release approval status.

**Done when:** the candidate is prepared and either approved for deployment or waiting at a named approval boundary.

---

## Phase 8 — Deploy

**Goal:** Execute the product-defined delivery path only after the required approval and verify technical health.

Load:

```text
deployment-workflow
observability-design
resilience-engineering
decision-provenance when delivery approval is asserted or changed
incident-response when failures occur
```

Produce:

```text
delivery approval reference
deployment evidence
health checks
observability signals
rollback readiness
incident or blocker report when unhealthy
```

Deployment evidence verifies the actual delivered candidate, not merely local or CI output.

**Gate:** required delivery approval, health, and rollback readiness are verified before launch.

**Done when:** the accepted candidate is healthy in the target environment, or rollback/blocker is reported.

---

## Phase 9 — Launch

**Goal:** Make the product available to intended users with communication, support, measurement, and learning channels.

Load:

```text
product-manager
business-value-alignment
content-strategy
copywriting
cro when persuasion is part of the launch goal
observability-design
decision-provenance when launch approval or audience scope is asserted
```

Produce:

```text
launch approval reference
launch message and channel plan
support and ownership handoff
analytics and success-metric instrumentation
feedback channel
monitoring and response plan
```

Launch is not equivalent to deployment. Users, communication, support, measurement, and feedback must exist.

**Gate:** launch approval is resolved, intended users can access the product, and monitoring/feedback collection is live.

**Done when:** launch operations and product learning signals are active.

---

## Phase 10 — Learn

**Goal:** Convert real product evidence into the next attributable decision.

Load:

```text
product-manager
business-value-alignment
observability-design
user-research
decision-making
decision-provenance when the next direction is approved or superseded
incident-response when incidents affected learning
```

Produce:

```text
success-metric readout
behavioral and qualitative feedback synthesis
incident and defect summary
assumption updates
iterate / pivot / narrow / stop recommendation
next-decision owner and source
next PRD or backlog update
```

Compare evidence with the original value hypothesis and success metrics. Do not interpret activity metrics as value without the declared relationship.

A recommendation becomes the effective next product decision only when the required authority and supersession chain are clear.

**Gate:** post-launch learning produces an owned next decision and updates the next product artifact.

**Done when:** the next action, owner, evidence basis, decision record, and PRD/backlog update are explicit.
