# Phases 6–10: Acceptance → Learn

## Phase 6 — Acceptance Verification

**Goal:** Prove the product satisfies the PRD acceptance criteria.

Load conceptually:

```text
skill-eval
code-review-workflow
security-review
design-review
web-performance
accessibility
```

Produce:

```text
- acceptance evidence matrix
- review findings
- release blockers
```

**Gate:** acceptance criteria must have evidence.

**Done when:** release blockers are resolved or explicitly accepted.

---

## Phase 7 — Release

**Goal:** Prepare release artifacts.

Load conceptually:

```text
git-workflow
deployment-workflow
```

Produce:

```text
- release notes
- version/tag plan
- changelog
- rollback note
- release signoff
```

**Gate:** release has notes, version/tag, and rollback plan.

**Done when:** release is approved for deployment.

---

## Phase 8 — Deploy

**Goal:** Deploy safely and verify health.

Load conceptually:

```text
deployment-workflow
observability-design
resilience-engineering
incident-response
```

Produce:

```text
- deployment evidence
- health check output
- rollback readiness
```

**Gate:** deployment health must be verified before launch.

**Done when:** deployment is healthy or rollback/blocker is reported.

---

## Phase 9 — Launch

**Goal:** Release to users with support, analytics, and feedback loop.

Load conceptually:

```text
product-manager
content-strategy
copywriting
cro
observability-design
```

Produce:

```text
- launch message
- support handoff
- analytics checklist
- feedback channel
- monitoring plan
```

**Gate:** launch includes monitoring and feedback loop.

**Done when:** users can access the product and feedback/metrics collection is live.

---

## Phase 10 — Learn

**Goal:** Convert launch data into next decisions.

Load conceptually:

```text
product-manager
observability-design
user-research
decision-making
```

Produce:

```text
- metric readout
- feedback synthesis
- incident/bug summary
- iterate / pivot / stop recommendation
- next PRD or backlog update
```

**Gate:** post-launch learning feeds next PRD or backlog.

**Done when:** next action is explicit.
