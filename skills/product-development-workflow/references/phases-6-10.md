# Phases 6–10: Acceptance → Learn

## Phase 6 — Product Acceptance Verification

**Goal:** Prove the complete approved MVP satisfies every in-scope PRD acceptance criterion.

Load on entry:

```text
skill-eval
code-review-workflow
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
approved PRD and MVP scope
technical specification
all feature evidence packages
code-review verdicts
domain review routes and verdicts
known limitations and proposed accepted risks
```

Produce:

```text
one acceptance-matrix row per in-scope criterion
reviewer and evidence coverage summary
hard-gate status
release blockers
accepted-risk register
RELEASE_READY or NOT_READY verdict
```

Critical rules:

```text
feature merged ≠ complete product accepted
green tests ≠ every criterion verified
screenshot ≠ runtime or hidden-state proof
NOT_VERIFIED blocks release unless scope is formally changed
LIMITED REVIEW blocks required complete-domain acceptance
code-review-workflow must be APPROVED
```

**Gate:** every in-scope criterion has direct evidence, explicit status, required reviewer coverage, and no unresolved release blocker.

**Done when:** product acceptance is `RELEASE_READY`, or `NOT_READY` lists exact rows, evidence, reviewers, and return path.

---

## Phase 7 — Release Preparation

**Goal:** Prepare traceable release artifacts for an accepted MVP.

Entry condition:

```text
Phase 6 verdict = RELEASE_READY
```

When the verdict is `NOT_READY`, return to:

```text
implementation
verification
code review
domain reviewer
or formal PRD/MVP scope change
```

Load on entry:

```text
git-workflow
deployment-workflow when release preparation needs deployment constraints
```

Produce:

```text
release notes
version or tag plan
changelog
acceptance-matrix reference
accepted-risk reference
rollback plan
release signoff
```

Release artifacts must preserve the exact accepted scope. New changes invalidate the prior acceptance evidence and require re-verification.

**Gate:** `RELEASE_READY` acceptance plus notes, version/tag, changelog, rollback, and signoff.

**Done when:** the accepted release candidate is approved for deployment.

---

## Phase 8 — Deploy

**Goal:** Deploy safely and verify technical health before launch.

Load on entry:

```text
deployment-workflow
observability-design
resilience-engineering
incident-response when failures occur
```

Produce:

```text
deployment evidence
health checks
observability signals
rollback readiness
incident or blocker report when unhealthy
```

Deployment evidence verifies the deployed candidate, not merely the local or CI artifact.

**Gate:** deployment health and rollback readiness are verified before launch.

**Done when:** the accepted release is healthy in the target environment, or rollback/blocker is reported.

---

## Phase 9 — Launch

**Goal:** Make the product available to intended users with support and learning channels.

Load on entry:

```text
product-manager
business-value-alignment
content-strategy
copywriting
cro when persuasion is part of the launch goal
observability-design
```

Produce:

```text
launch message and channel plan
support and ownership handoff
analytics and success-metric instrumentation
feedback channel
monitoring and response plan
```

Launch is not equivalent to deployment. Users, communication, support, measurement, and feedback must exist.

**Gate:** intended users can access the product and monitoring/feedback collection is live.

**Done when:** launch operations and product learning signals are active.

---

## Phase 10 — Learn

**Goal:** Convert real product evidence into the next decision.

Load on entry:

```text
product-manager
business-value-alignment
observability-design
user-research
decision-making
incident-response when incidents affected learning
```

Produce:

```text
success-metric readout
behavioral and qualitative feedback synthesis
incident and defect summary
assumption updates
iterate / pivot / narrow / stop recommendation
next PRD or backlog update
```

Compare evidence with the original value hypothesis and success metrics. Do not interpret activity metrics as value without the declared relationship.

**Gate:** post-launch learning changes the next product decision, PRD, experiment, or backlog.

**Done when:** the next action, owner, evidence basis, and product artifact update are explicit.