---
name: code-review-workflow
description: Evidence-backed code review workflow — classify changed domains, verify architecture, route user-facing changes through the design-review facade, inspect logic and security, then map domain verdicts into an explicit merge decision.
license: MIT
metadata:
  ai-native-skills.version: 2.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "architecture-review design-review master-engineer systematic-debugging security-review threat-modeling"
  ai-native-skills.type: workflow
  ai-native-skills.implements: ai-native-core/contracts/workflows/code-review.contract.yaml
  ai-native-skills.contract-version: "~0.2"
  ai-native-skills.skill_load_order: '[{''phase'': ''architecture-check'', ''load'': [''architecture-review'']}, {''phase'': ''design-check'', ''load'': [''design-review'']}, {''phase'': ''logic-check'', ''load'': [''systematic-debugging'', ''master-engineer'']}, {''phase'': ''security-check'', ''load'': [''security-review'', ''threat-modeling'']}]'
  ai-native-skills.skills: '{''required'': [''architecture-review''], ''optional'': [''design-review'', ''systematic-debugging'', ''master-engineer'', ''security-review'', ''threat-modeling'']}'
---

# Code Review Workflow

Load context → classify changes → architecture → design acceptance → logic → security → verdict.

## Core Rule

```text
Compiled ≠ correct.
Generated ≠ reviewed.
Green CI ≠ architecture approval.
Source diff ≠ rendered design evidence.
Screenshot ≠ runtime, keyboard, or hidden-state evidence.
```

A submission may be approved only when every affected domain has passed or has explicit non-blocking accepted risk under the product approval policy.

## Hard Rules

```text
1. Classify changed domains before selecting reviewers.
2. Always run architecture review for code submissions.
3. Run design review when user-facing or generated visual output can change.
4. Enter design acceptance through the design-review facade.
5. Changed rendered output requires fresh rendered or exported evidence.
6. Source-only design inspection cannot approve visual or interaction acceptance.
7. NOT_VERIFIED is an evidence gap, not PASS or zero.
8. LIMITED REVIEW cannot approve a complete specialist-domain claim.
9. Run security review when trust boundaries or sensitive behavior change.
10. Every blocking verdict cites concrete evidence and affected files/regions.
11. No merge without an explicit final verdict.
```

## Inputs

```yaml
review_context:
  submission: <PR, MR, patch, commit range, or diff>
  specification: <ticket, PRD, acceptance criteria, ADRs>
  engineering_rules: []
  product_design_locks: []
  changed_files: []
  available_evidence:
    tests: []
    ci: []
    previews: []
    runtime: []
    screenshots: []
    exports: []
    accessibility: []
  approval_policy: <product-defined>
```

Missing contracts do not automatically block every review. Record the gap and use repository conventions, specifications, architecture, and declared design locks. Block when the missing contract prevents a required acceptance decision.

## Phase 1 — Load Context

Inspect:

```text
submission diff and description
linked issue/spec/acceptance criteria
repository and product instructions
engineering contracts and ADRs
product design system, locks, and required assets
verification evidence attached to the submission
```

Claims are not evidence. “Responsive tested” requires the tested contexts and observable result.

**Gate:** review context and evidence are declared.

## Phase 2 — Classify Changed Domains

```yaml
change_impact:
  architecture: <none | affected>
  logic: <none | affected>
  security: <none | affected>
  data_or_migration: <none | affected>
  user_facing_design: <none | affected>
  design_domain: <digital-interface | visual-communication | presentation | other | N/A>
  surface_profile: <profile | N/A>
  artifact_state: <rendered-interactive | rendered-static | source-only | mixed | N/A>
  required_reviewers: []
  evidence_gaps: []
```

User-facing design is affected when code can change appearance, interaction, states, content fidelity, accessibility, responsiveness, or generated/exported visual output.

Do not infer “no design change” because only CSS, tokens, props, content data, templates, assets, or generation configuration changed.

**Gate:** affected domains and required reviewers are resolved.

## Phase 3 — Architecture Check

Load `architecture-review`.

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
secrets and obvious security baseline
```

Output:

```text
Architecture: PASS | PASS WITH FLAGS | FAIL | NOT_VERIFIED
```

A failing applicable architecture gate blocks approval.

## Phase 4 — Design Check

Run only when `user_facing_design: affected`.

Load:

```text
references/design-review-adapter.md
```

That adapter owns:

- design-change triggers;
- facade route fields;
- source/rendered/static evidence policy;
- phase-specific design-review loading;
- facade verdict-to-merge mapping;
- design result handoff shape.

Do not maintain a duplicate design scorecard here.

Output:

```text
Design: PASS | CONDITIONAL PASS | NEEDS WORK | CRITICAL |
        LIMITED REVIEW | ROUTE_ELSEWHERE | N/A
```

**Gate:** facade design acceptance is resolved for every affected user-facing surface.

## Phase 5 — Logic Check

Load `master-engineer` for complex logic. Load `systematic-debugging` when the submission claims to fix a bug or regression.

Inspect:

```text
traceability to specification and acceptance criteria
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

## Phase 6 — Security Check

Load `security-review` and `threat-modeling` when the diff affects:

```text
authentication or authorization
trust boundaries or integrations
secrets, tokens, uploads, or untrusted input
personal, financial, or sensitive data
permissions, tenancy, or data isolation
destructive or high-impact actions
```

Output:

```text
Security: PASS | PASS WITH FLAGS | FAIL | NOT_VERIFIED | N/A
```

Applicable unresolved high-risk findings block approval.

## Phase 7 — Final Verdict

```text
APPROVED
  every affected domain passes
  or only explicit accepted non-blocking flags remain

REQUEST CHANGES
  correctable architecture, design, logic, security, test,
  reviewer, or evidence gaps remain

BLOCKED
  critical/hard-gate failure
  missing required specialist reviewer
  unsafe migration/security condition
  or the submission cannot be responsibly evaluated
```

Output:

```markdown
# Code Review Verdict

- Submission: [link or commit range]
- Overall: [APPROVED | REQUEST CHANGES | BLOCKED]
- Approved to merge: [YES | NO]

## Change Classification
- Architecture: [affected/none]
- Logic: [affected/none]
- Security: [affected/none]
- User-facing design: [affected/none]
- Design domain/profile/state: [...]

## Domain Results
- Architecture: [result]
- Design: [facade verdict, score, evidence coverage, primary-domain coverage]
- Logic: [result]
- Security: [result]

## Blocking Findings
1. **[domain] [finding]**
   - Evidence: ...
   - Files/regions: ...
   - Impact: ...
   - Required correction or evidence: ...

## Non-Blocking Flags
- [explicit accepted risk or follow-up]

## Evidence Gaps
- [missing tests, preview, state, runtime, export, or reviewer]

## ADR / Follow-up
- ADR required: [YES | NO]
- Follow-up issues: [...]
```

Do not approve with “looks good”, “CI passed”, or a high partial design score when required evidence or primary-domain coverage is missing.

## Quick Reference

| Phase | Capability | Exit gate |
|---|---|---|
| Context | repository/spec evidence | context declared |
| Classification | changed-domain routing | reviewers selected |
| Architecture | `architecture-review` | architecture gates resolved |
| Design | `design-review` facade adapter | rendered/domain acceptance resolved |
| Logic | engineering/debugging review | behavior and tests resolved |
| Security | security/threat review | applicable risks resolved |
| Verdict | workflow synthesis | explicit merge decision |

## Auto-Fail Anti-Patterns

| Pattern | Why it fails |
|---|---|
| Approve because CI is green | CI does not prove architecture, design, or behavior |
| Approve a visual change from diff only | Source-only evidence cannot prove rendered acceptance |
| Treat screenshot as interaction/runtime proof | Hidden behavior remains unverified |
| Run a hardcoded design checklist | Bypasses facade routing and domain ownership |
| Give specialist-domain approval from universal UI gates | Required reviewer coverage is missing |
| Skip design review because only CSS/content changed | Those changes can alter user-facing output |
| Vague “could be better” finding | No evidence, impact, or correction contract |
| Merge without explicit verdict | Review responsibility is ambiguous |
