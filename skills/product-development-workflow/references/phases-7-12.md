# Phases 7–12: Implementation → Product Validation and Learning

## Phase 7 — Implementation

**Goal:** Build approved slices without losing product-level traceability.

Run each slice through `new-feature-workflow` with default engineering-quality composition, tests, implementation-context mapping, runtime/rendered evidence where applicable, code review, and merge authorization.

**Gate:** every completed slice traces to PRD/MVP, experience, solution, and delivery decisions and contains the required evidence package.

---

## Phase 8 — Product Acceptance

**Goal:** Prove the complete verified MVP satisfies every in-scope criterion and reconcile reviewer coverage, risks, and authority.

Load `acceptance-and-release.md` for the full matrix and release contract.

Critical distinctions:

```text
feature merged ≠ complete product accepted
green tests ≠ every criterion verified
Product Acceptance ≠ real-user Product Validation
RELEASE_READY ≠ release permission
```

**Gate:** every in-scope criterion has direct evidence, explicit status, required reviewer coverage, decision provenance, and no unresolved blocker.

---

## Phase 9 — Release

Prepare release notes, version/tag plan, changelog, acceptance references, risks, rollback, and approval status only for a `RELEASE_READY` candidate. Release preparation does not self-authorize release.

---

## Phase 10 — Deploy

Execute only the approved delivery path and verify the actual candidate, health, observability, resilience, and rollback readiness in the target environment.

---

## Phase 11 — Launch

Make the product available to intended users with approval, communication, support ownership, analytics, monitoring, and feedback channels. Deployment alone is not launch.

---

## Phase 12 — Product Validation and Learning

**Goal:** Determine whether the launched product creates observable value for real users and turn the evidence into the next attributable decision.

Keep evidence states distinct:

```text
Engineering verification: does the software work correctly?
Product Acceptance: does it satisfy the approved PRD/MVP?
Product Validation: does it create observable value for real users?
```

Produce:

```text
validation hypothesis and target users
real workflow and expected signals
quantitative and qualitative evidence
observed behavior and limitations
incident/defect summary
assumption updates
continue / improve / pivot / narrow / stop recommendation
decision owner and provenance
next PRD or backlog action
skill-evolution review for reusable findings
```

Missing or weak usage evidence is `NOT_VERIFIED` or `LIMITED`, not automatic success or failure.

**Gate:** reviewed real-user evidence produces an owned next decision and updates the next product artifact.

**Done when:** the next action, owner, evidence basis, decision record, and PRD/backlog update are explicit.
