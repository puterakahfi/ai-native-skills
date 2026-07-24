---
name: code-review-workflow
description: Evidence-backed code review workflow — classify changed domains, verify architecture, route user-facing changes through design review, assess internal code and object/module design quality, inspect logic and security, then separate technical approval from provenance-backed merge authorization.
license: MIT
metadata:
  ai-native-skills.version: 2.2.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "architecture-review clean-architecture clean-code solid-design design-review decision-provenance master-engineer systematic-debugging security-review threat-modeling"
  ai-native-skills.type: workflow
  ai-native-skills.implements: ai-native-core/contracts/workflows/code-review.contract.yaml
  ai-native-skills.contract-version: "~0.3"
  ai-native-skills.skill_load_order: '[{"phase":"load-context","load":["decision-provenance"]},{"phase":"architecture-check","load":["architecture-review","clean-architecture"]},{"phase":"design-check","load":["design-review"]},{"phase":"code-design-quality","load":["clean-code","solid-design"]},{"phase":"logic-check","load":["systematic-debugging","master-engineer"]},{"phase":"security-check","load":["security-review","threat-modeling"]},{"phase":"verdict","load":["decision-provenance"]}]'
  ai-native-skills.skills: '{"required":["architecture-review","decision-provenance","clean-code"],"optional":["clean-architecture","solid-design","design-review","systematic-debugging","master-engineer","security-review","threat-modeling"]}'
---

# Code Review Workflow

Load context → classify changes and decision claims → architecture → design acceptance → internal code/object quality → logic → security → technical verdict → merge authorization.

## Core boundary

```text
Compiled ≠ correct.
Generated ≠ reviewed.
Green CI ≠ architecture approval.
Source diff ≠ rendered design evidence.
Screenshot ≠ runtime, keyboard, or hidden-state evidence.
Technical APPROVED ≠ automatically authorized to merge.
```

A submission can report `Approved to merge: YES` only when:

```text
all affected technical domains pass
+ applicable accepted risks are verified and non-blocking
+ decision-provenance PASS
+ required repository/product/policy approvals are satisfied
```

## Hard rules

```text
1. Classify changed domains before selecting reviewers.
2. Classify material scope, exception, risk, and merge claims before accepting them.
3. Always run architecture review for code submissions.
4. Run design review when user-facing or generated visual output can change.
5. Enter design acceptance through the design-review facade.
6. Changed rendered output requires fresh rendered or exported evidence.
7. Source-only design inspection cannot approve visual or interaction acceptance.
8. NOT_VERIFIED is an evidence gap, not PASS or zero.
9. LIMITED REVIEW cannot approve a complete specialist-domain claim.
10. Run security review when trust boundaries or sensitive behavior change.
11. Every blocking verdict cites concrete evidence and affected files/regions.
12. Agent/author PR text is not owner approval.
13. Existing code or newest commit proves state, not scope or authority.
14. Accepted risk requires verified authority and cannot hide a blocker.
15. Technical review verdict and merge authorization must be reported separately.
16. No merge without explicit technical approval and merge authorization.
17. Run `clean-code` for materially changed implementation; lint, formatting, compilation, and green tests are not clean-code approval.
18. Run `solid-design` only when responsibility, variation, substitution, client-interface, or dependency relationships are materially affected.
19. Use `clean-architecture` as an architecture-style or policy/mechanism specialist only when that decision is material; `architecture-review` remains the acceptance gate.
20. Do not force SOLID or Clean Architecture ceremony into changes where applicability is `NOT_APPLICABLE` or `NOT_JUSTIFIED`.
```

## Inputs

```yaml
review_context:
  submission: <PR, MR, patch, commit range, or diff>
  specification: <ticket, PRD, acceptance criteria, ADRs>
  engineering_rules: []
  product_design_locks: []
  changed_files: []

  decision_sources: []
  required_authorities: []
  previous_decision_records: []
  claimed_scope_or_exceptions: []
  claimed_accepted_risks: []

  available_evidence:
    tests: []
    ci: []
    previews: []
    runtime: []
    screenshots: []
    exports: []
    accessibility: []

  approval_policy: <product-defined>
  merge_authority: <role or policy>
```

Missing contracts do not automatically block every review. Record the gap and use repository conventions, specifications, architecture, and declared locks. Block when the gap prevents a required domain verdict or authority decision.

## Phase 1 — Load context

Inspect:

```text
submission diff and description
linked issue/spec/acceptance criteria
repository and product instructions
engineering contracts and ADRs
product design system, locks, and required assets
verification evidence attached to the submission
claimed scope, exception, accepted-risk, and merge decisions
source references and required authorities for those decisions
```

Claims are not evidence. Submission text such as “responsive tested”, “owner approved”, or “risk accepted” requires the relevant evidence or decision source.

Load `decision-provenance` when a material claim affects scope, exception, accepted risk, approval, or merge permission.

**Gate:** context, evidence, decision sources, and approval policy are declared.

## Phase 2 — Classify changed domains and claims

```yaml
change_impact:
  architecture: <none | affected>
  architecture_style_or_boundary_design: <none | affected>
  internal_code_quality: <none | affected>
  object_module_design: <none | affected>
  logic: <none | affected>
  security: <none | affected>
  data_or_migration: <none | affected>
  user_facing_design: <none | affected>
  design_domain: <digital-interface | visual-communication | presentation | brand-identity | other | N/A>
  surface_profile: <profile | N/A>
  artifact_state: <rendered-interactive | rendered-static | source-only | mixed | N/A>
  required_reviewers: []
  evidence_gaps: []

material_decision_claims:
  scope: []
  dependency_or_exception: []
  accepted_risk: []
  approval_or_merge: []
  required_authorities: []
```

User-facing design is affected when code can change appearance, interaction, states, content fidelity, accessibility, responsiveness, or generated/exported visual output.

Do not infer “no design change” because only CSS, tokens, props, content data, templates, assets, or generation configuration changed.

Do not infer a claim is authoritative because it appears in the latest commit or PR body.

**Gate:** affected domains, reviewers, material claims, and required authorities are resolved.

## Phase 3 — Architecture check

Load `architecture-review`. Load `clean-architecture` only when the submission materially changes or claims an architecture style, policy/mechanism boundary, dependency rule, use-case boundary, or broad architecture migration. `clean-architecture` supplies applicability and boundary reasoning; it does not replace the independent architecture verdict.

Review applicable concerns:

```text
stack and dependency policy
layer/module boundaries
data ownership and migrations
API/event compatibility
folder/package placement
failure handling and observability implications
test strategy and regression coverage
ADR requirement
secrets and baseline security concerns
```

Output:

```text
Architecture: PASS | PASS WITH FLAGS | FAIL | NOT_VERIFIED
```

A failing applicable architecture gate blocks technical approval.

## Phase 4 — Design check

Run only when `user_facing_design: affected`.

Load:

```text
references/design-review-adapter.md
```

The adapter owns design-change triggers, facade route fields, evidence policy, reviewer coverage, verdict mapping, and design handoff. Do not maintain a duplicate design scorecard here.

Output:

```text
Design: PASS | CONDITIONAL PASS | NEEDS WORK | CRITICAL |
        LIMITED REVIEW | ROUTE_ELSEWHERE | N/A
```

A `CONDITIONAL PASS` is technically usable only when the remaining risk is verified as non-blocking and accepted by the required authority.

**Gate:** facade design acceptance is resolved for every affected user-facing surface.

## Phase 5 — Internal code and object/module design quality

Run `clean-code` when materially changed hand-written or generated implementation affects readability, maintainability, control flow, errors, duplication, local contracts, or test readability.

Run `solid-design` only when the change materially affects:

```text
class/module/service responsibility and ownership
proven variation or extension seams
inheritance, substitution, or implementation contracts
client-specific interface shape
stable-policy versus volatile-detail dependency direction
an explicit SOLID or abstraction claim
```

Inspect:

```text
repository vocabulary and conventions
readability and working-memory load
control flow, errors, comments, and duplicated knowledge
cohesive ownership and reasons to change
behavioral substitutability rather than type compatibility alone
actual client needs rather than interface-size dogma
abstraction benefit versus new indirection
behavior-change risk and required tests
```

Do not fail a submission from arbitrary line, method, parameter, or class-size limits. Do not approve internal quality merely because formatters, linters, compilation, or tests pass.

Output:

```text
Code quality: PASS | PASS WITH FLAGS | NEEDS WORK | NOT_VERIFIED | N/A
Object/module design: PASS | PASS WITH FLAGS | NEEDS WORK | NOT_VERIFIED | N/A
```

A verified blocking code-quality or object-design issue prevents technical approval. `NOT_APPLICABLE` or `NOT_JUSTIFIED` specialist conclusions must not be converted into invented work.

**Gate:** local implementation quality and materially applicable object/module design are resolved without duplicating architecture acceptance or refactoring ownership.

## Phase 6 — Logic check

Load `master-engineer` for complex logic. Load `systematic-debugging` when the submission claims to fix a bug or regression.

Inspect:

```text
traceability to verified specification and acceptance criteria
business rules and state transitions
edge cases and boundary inputs
error, retry, idempotency, and partial failure behavior
concurrency or ordering risks when relevant
regression tests for verified bug fixes
silent failure and data-loss paths
```

Output:

```text
Logic: PASS | PASS WITH FLAGS | FAIL | NOT_VERIFIED | N/A
```

## Phase 7 — Security check

Load `security-review` and `threat-modeling` when trust boundaries, authentication/authorization, secrets/tokens, untrusted input, sensitive data, permissions, tenancy, isolation, or high-impact behavior are affected.

Output:

```text
Security: PASS | PASS WITH FLAGS | FAIL | NOT_VERIFIED | N/A
```

Applicable unresolved high-risk findings block technical approval. A risk-acceptance claim must still pass decision provenance and applicable policy.

## Phase 8 — Technical verdict and merge authorization

Load:

```text
references/merge-authorization.md
decision-provenance
```

### Technical review verdict

```text
APPROVED
  every affected technical domain passes
  or only verified non-blocking flags remain

REQUEST CHANGES
  correctable architecture, design, code-quality, object-design, logic, security, test,
  reviewer, or evidence gaps remain

BLOCKED
  critical/hard-gate failure
  missing required specialist reviewer
  unsafe condition
  or the submission cannot be responsibly evaluated
```

### Merge authorization

```text
AUTHORIZED
  technical verdict APPROVED
  + provenance PASS
  + all required policy approvals satisfied

NOT_AUTHORIZED
  technical verdict REQUEST CHANGES/BLOCKED
  or provenance blocked
  or a required authority rejected the action

ROUTE_FOR_APPROVAL
  technical verdict APPROVED
  but another required authority has not decided
```

A reviewer may conclude the implementation is technically approved while still reporting:

```text
Approved to merge: NO
Merge authorization: ROUTE_FOR_APPROVAL
```

That is not a contradiction; it preserves the authority boundary.

## Required report

```markdown
# Code Review Verdict

- Submission: [link or commit range]
- Technical review: [APPROVED | REQUEST CHANGES | BLOCKED]
- Decision provenance: [PASS | PROVENANCE_BLOCKED | ROUTE_FOR_APPROVAL]
- Merge authorization: [AUTHORIZED | NOT_AUTHORIZED | ROUTE_FOR_APPROVAL]
- Approved to merge: [YES | NO]

## Change Classification
- Architecture: [affected/none]
- Architecture style/boundary design: [affected/none]
- Internal code quality: [affected/none]
- Object/module design: [affected/none]
- Logic: [affected/none]
- Security: [affected/none]
- User-facing design: [affected/none]
- Design domain/profile/state: [...]

## Domain Results
- Architecture: [result]
- Clean Architecture specialist: [applicability/boundary decision or N/A]
- Design: [facade verdict, evidence coverage, primary-domain coverage]
- Code quality: [clean-code verdict/findings/gaps]
- Object/module design: [solid-design verdict/findings/gaps or N/A]
- Logic: [result]
- Security: [result]

## Decision Provenance
- Effective scope/exception decisions: [...]
- Authoritative record IDs: [...]
- Conflicts/unresolved approvals: [...]

## Blocking Findings
1. **[domain] [finding]**
   - Evidence: ...
   - Files/regions: ...
   - Impact: ...
   - Required correction or evidence: ...

## Accepted Risks / Non-Blocking Flags
- [risk, authority record, owner, mitigation, expiry]

## Evidence Gaps
- [missing tests, preview, state, runtime, export, reviewer, or decision source]

## ADR / Follow-up
- ADR required: [YES | NO]
- Follow-up issues: [...]
```

Do not approve with “looks good”, “CI passed”, a high partial design score, author self-approval, or missing authority evidence.

## Auto-fail anti-patterns

| Pattern | Why it fails |
|---|---|
| Approve because CI is green | CI does not prove architecture, design, behavior, or authority |
| Approve a visual change from diff only | Source-only evidence cannot prove rendered acceptance |
| Treat screenshot as interaction/runtime proof | Hidden behavior remains unverified |
| Run a hardcoded design checklist | Bypasses facade routing and domain ownership |
| Give specialist-domain approval from universal gates | Required reviewer coverage is missing |
| Treat PR body as product-owner approval | Agent/author summary is not authority |
| Treat newest commit as approved scope | Recency proves state, not intent |
| Let author accept their own risk without policy authority | Risk acceptance provenance is missing |
| Report technical APPROVED as automatic merge permission | Review and authorization are separate |
| Merge without explicit final statuses | Responsibility and authority are ambiguous |

| Treat lint, formatting, or green tests as clean-code approval | Tools prove selected checks, not readability or maintainability |
| Run SOLID on every local edit | Specialist applicability and concrete change pressure are missing |
| Require fixed Clean Architecture layers during review | Architecture-style dogma bypasses repository context and applicability |
