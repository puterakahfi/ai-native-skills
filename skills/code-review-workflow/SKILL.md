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

A submission may be approved only when every affected review domain has either passed or has explicit non-blocking accepted risk under the product approval policy.

## Hard Rules

```text
1. Classify changed domains before selecting reviewers.
2. Always run architecture review for a code submission.
3. Run design review when user-facing appearance, interaction, state, content fidelity,
   accessibility, responsiveness, or generated/exported visuals can change.
4. Design review must enter through the design-review facade.
5. Changed rendered behavior requires fresh rendered or exported evidence.
6. Source-only design inspection cannot approve visual or interaction acceptance.
7. NOT_VERIFIED is an evidence gap, not a PASS or zero score.
8. LIMITED REVIEW cannot approve a complete specialist-domain claim.
9. Run security review when trust boundaries or sensitive behavior change.
10. Every blocking verdict must cite concrete evidence and affected files/regions.
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

Missing product contracts do not automatically block every review. Record the gap and review against repository conventions, specifications, existing architecture, and declared design locks. Block only when the missing contract prevents a required acceptance decision.

## Phase 1 — Load Context

Inspect:

```text
submission diff and description
linked issue/spec/acceptance criteria
repository and product instructions
engineering contracts and ADRs
product design system, visual locks, and required assets
verification evidence attached to the submission
```

Record evidence separately from claims. A PR description saying “responsive tested” is not evidence unless the tested viewports and result are available.

**Gate:** review context and available evidence are explicit.

## Phase 2 — Classify Changed Domains

Classify each affected domain before reviewing:

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

User-facing design is affected when the diff can change:

- rendered appearance, typography, spacing, hierarchy, color, assets, or content;
- interaction, navigation, focus, overflow, responsive/adaptive behavior, or state feedback;
- loading, empty, error, permission, success, or destructive states;
- generated/exported poster, slide, thumbnail, PDF, or other visual output;
- accessibility semantics or operability;
- logo, product, person, price, claim, or other required fidelity.

Do not infer “no design change” merely because only CSS, tokens, component props, content data, or generated templates changed.

**Gate:** all changed domains and required reviewers are resolved.

## Phase 3 — Architecture Check

Load `architecture-review`.

Review only against evidence and applicable contracts:

```text
stack and dependency policy
layer and module boundaries
data ownership and migrations
API/event contracts and compatibility
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

### 4.1 Resolve facade route

Start with `design-review/SKILL.md` and declare:

```yaml
design_review_route:
  design_domain: <domain>
  surface_profile: <profile>
  artifact_state: <state>
  review_depth: <focused | release>
  coverage_mode: <BUILT_IN | ADAPTER_COVERED | LIMITED | ROUTE_ELSEWHERE>
  domain_reviewers: []
  selected_components: []
  changed_regions: []
  required_viewing_contexts: []
  evidence_available: []
  evidence_gaps: []
```

Use `focused` for an ordinary PR affecting bounded regions. Use `release` only when this review is the final design acceptance boundary and all required evidence is available.

### 4.2 Apply artifact-state evidence policy

```text
source-only
  inspect implementation, tokens, semantics, content, and declared state coverage
  mark rendered visual, interaction, runtime, and export claims NOT_VERIFIED
  do not approve changed rendered output

rendered-interactive or mixed
  inspect changed regions at required viewports/themes
  exercise changed interactions, states, and expected inputs
  capture runtime evidence when executable behavior changed
  inspect accessibility semantics/focus when affected

rendered-static or mixed static output
  inspect final size and actual destination context
  verify crop, safe area, fidelity, mandatory content, and export integrity
```

A screenshot may verify visible composition but cannot prove keyboard operation, overflow behavior after interaction, reduced motion, console/runtime health, or hidden states.

### 4.3 Run selected facade phases

```text
CLASSIFY / ROUTE
→ UNIVERSAL REVIEW
→ applicable domain/surface reviewer
→ selected component review
→ EVIDENCE + SCORE
→ REPORT
```

Do not copy a local mini-scorecard into this workflow. The facade and loaded domain reviewers own gates, scoring, coverage, and verdict.

Design result:

```text
PASS
CONDITIONAL PASS
NEEDS WORK
CRITICAL
LIMITED REVIEW
ROUTE_ELSEWHERE
N/A
```

### 4.4 Map design verdict to review decision

```text
PASS
  eligible for approval

CONDITIONAL PASS
  eligible only when every remaining risk is explicit, non-blocking,
  and accepted by the configured authority

NEEDS WORK
  request changes

CRITICAL
  block

LIMITED REVIEW
  block complete-domain approval; obtain the required domain reviewer
  or narrow the claim and merge scope

ROUTE_ELSEWHERE
  block until the required specialist reviewer is available

NOT_VERIFIED evidence required for changed acceptance
  request evidence or changes; do not silently approve
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
trust boundaries or external integrations
secrets, tokens, uploads, or untrusted input
personal, financial, or other sensitive data
permissions, tenancy, or data isolation
destructive or high-impact actions
```

Output:

```text
Security: PASS | PASS WITH FLAGS | FAIL | NOT_VERIFIED | N/A
```

Applicable unresolved high-risk security findings block approval.

## Phase 7 — Final Verdict

Map all domain results into one merge decision:

```text
APPROVED
  every affected domain passes
  or only explicit non-blocking accepted flags remain

REQUEST CHANGES
  correctable architecture, design, logic, security, test, or evidence gaps remain

BLOCKED
  critical/hard-gate failure
  missing required specialist reviewer
  unsafe migration/security condition
  submission cannot be responsibly evaluated
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
- [missing tests, preview, viewport, state, runtime, export, or reviewer]

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
| Architecture | `architecture-review` | applicable architecture gates resolved |
| Design | `design-review` facade | rendered/domain acceptance resolved |
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
| Give logo/identity approval from universal UI gates | Specialist-domain coverage is missing |
| Skip design review because only CSS/content changed | Those changes can alter user-facing output |
| Vague “could be better” finding | No evidence, impact, or correction contract |
| Merge without explicit verdict | Review responsibility is ambiguous |
