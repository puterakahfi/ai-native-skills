---
name: product-requirements
description: Create, revise, review, and verify Product Requirements Documents (PRDs) for AI-native product development. Use when turning discovery, feature intent, user needs, constraints, and success metrics into a testable PRD, product scope, acceptance criteria, and readiness verdict. Do not use for conceptual PRD explanations, technical architecture specifications, implementation planning alone, or release execution.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/product/product-requirements.contract.yaml
  ai-native-skills.contract-version: "~0.2"
  ai-native-skills.related_skills: '["business-value-alignment", "experiment-design", "product-manager", "user-research", "spec-workflow", "decision-making", "api-contract"]'
---

# Product Requirements / PRD

## Capability identity and artifact aliases

```text
Executable capability ID:
  product-requirements

Canonical user-facing artifact:
  Product Requirements Document (PRD)

Accepted natural-language intents include:
  create / write / draft a PRD
  revise / update an existing PRD
  review / verify PRD readiness
  define product requirements, scope, metrics, or acceptance criteria
  susun kebutuhan produk
  buatkan / revisi / review PRD
```

`PRD` is an artifact alias and user-facing term, not a competing executable skill ID. Route PRD authoring, revision, and readiness-review requests to `product-requirements`. Do not create or prefer a separate `prd` skill merely because the user uses the acronym.

The normal lifecycle composition is:

```text
product-development-workflow
→ product-manager as owner
→ product-requirements as artifact-producing executor
→ PRD plus readiness evidence
```

A conceptual question such as “Apa itu PRD?” or “What is a PRD?” is explanation-only unless the user also asks to author, revise, or review a concrete product artifact.

## When to Use

Use when the user asks to write a PRD, turn discovery notes into product requirements, define goals/metrics/scope/acceptance criteria, revise an existing PRD, or review product readiness before technical specification.

Do not use for:

- conceptual PRD definitions or comparisons without an authoring/revision/review request;
- technical architecture specifications (`spec-workflow`, `api-contract`);
- implementation task breakdown alone (`delivery-work-breakdown` or the governing delivery workflow);
- release or deployment execution;
- automatic approval claims based only on an agent-authored document.

## Allowed outputs

Depending on the request, produce one or more of:

```text
Product Requirements Document (PRD)
requirements summary
scope boundary
acceptance criteria
user and business value
success metrics
risk and dependency list
open questions
launch readiness criteria
PRD readiness verdict
```

The output may be called `PRD`, `Product Requirements Document`, or `dokumen kebutuhan produk` in user-facing text. Preserve `product-requirements` as the executable capability identity in routing, evidence, manifests, and receipts.

## PRD Template

```markdown
# PRD: <Product or Feature Name>

## 1. Problem Statement
<What user or business problem needs solving? Do not start with the solution.>

## 2. Target Users
- Primary user: <who>
- Secondary users: <who, if any>
- Excluded users: <who this does not optimize for>

## 3. User and Business Value
- User value: <who benefits and how>
- Business value: <revenue | activation | retention | credibility | efficiency | risk reduction | learning | strategic option>
- Value confidence: <High | Medium | Low>

## 4. Experiment Evidence or Assumptions
- Experiment evidence: <experiment result, if available>
- Untested assumptions: <assumptions that remain>
- Evidence confidence: <High | Medium | Low>

## 5. Goals
- G1: <measurable outcome>

## 6. Non-Goals
- NG1: <explicitly out of scope>

## 7. Success Metrics
- North-star / primary metric: <metric + target>
- Guardrail metric: <metric + threshold>
- Adoption / activation metric: <metric + target>

## 8. Scope
### In Scope
- <included capability>

### Out of Scope
- <excluded capability or assumption>

## 9. User Stories / Jobs To Be Done
- As a <user>, I want <capability>, so that <outcome>.
- When <situation>, I want to <motivation>, so I can <desired progress>.

## 10. Requirements
### Functional Requirements
- REQ-1: <testable product behavior>

### Non-Functional Requirements
- NFR-1: <performance/security/reliability/accessibility requirement>

## 11. Acceptance Criteria
- AC-1: Given <context>, when <action>, then <observable outcome>. [traces: REQ-1]

## 12. Constraints
- Technical: <constraint>
- Design: <constraint>
- Legal/security/privacy: <constraint>

## 13. Dependencies
- <team/system/decision dependency>

## 14. Risks
- RISK-1: <risk> → mitigation: <mitigation>

## 15. Open Questions
- Q1: <question> → owner: <owner> → due: <date or milestone>

## 16. Launch Criteria
- LC-1: <readiness signal, not just code complete>
```

## Authoring Procedure

1. **Classify the request.** Distinguish authoring, revision, readiness review, and explanation-only intent.
2. **Frame the problem.** Problem statement names a user/business outcome and does not prescribe implementation.
3. **Name the users.** Primary target user is explicit; excluded users are named when relevant.
4. **Carry experiment evidence forward.** Results are referenced, or untested assumptions remain explicit as risks or open questions.
5. **Define goals and non-goals.** Success and boundaries are both documented.
6. **Make metrics measurable.** Each success metric has a target or observable threshold.
7. **Set scope boundaries.** Scope-in and scope-out both exist.
8. **Write requirements.** Every requirement is testable or traces to acceptance criteria.
9. **Write acceptance criteria.** Use Given/When/Then or equivalent observable evidence.
10. **Capture constraints, dependencies, and risks.** Blockers are explicit, not implied.
11. **Define launch criteria.** Readiness includes verification, support, analytics, and operational signals.
12. **Check traceability.** `requirement → acceptance criterion → verification evidence` can be followed.
13. **Preserve identity.** User-facing output may say PRD, while execution evidence names `product-requirements` as the capability applied.

## Revision Procedure

When revising an existing PRD:

1. Identify the effective source version and requested changes.
2. Preserve accepted decisions unless a verified authority supersedes them.
3. Mark added, removed, deferred, or changed requirements and criteria.
4. Re-run scope, metric, risk, traceability, and launch-readiness gates.
5. Do not treat the revised draft as approved without attributable product authority.

## Readiness Review Procedure

When reviewing a PRD rather than authoring one:

1. Inspect the supplied or verified PRD version.
2. Evaluate every quality gate below.
3. Separate missing evidence from failed requirements.
4. Return `READY`, `NEEDS REVISION`, or `BLOCKED` with concrete gaps and next actions.
5. Do not silently rewrite the document unless revision is also requested.

## Quality Gates

- The request is authoring, revision, or readiness review rather than explanation-only intent.
- Problem statement is not a disguised solution.
- Target users are explicit.
- Goals and non-goals both exist.
- High-risk unvalidated assumptions reference `experiment-design` output or remain explicit open questions.
- Success metrics are measurable.
- Scope-in and scope-out both exist.
- Requirements are testable or trace to testable acceptance criteria.
- Acceptance criteria are verifiable.
- Non-functional requirements include reliability, security, performance, accessibility, or privacy when relevant.
- Constraints and dependencies are explicit.
- Open questions have owners or next-step decisions.
- Launch criteria define readiness, not just implementation completion.
- Implementation detail is excluded unless it is a real constraint.
- Routing and receipts identify `product-requirements`; user-facing artifact language may identify the PRD.

## PRD Readiness Verdict

```text
PRD READINESS
Verdict: READY | NEEDS REVISION | BLOCKED
Problem clarity: PASS|FAIL — <note>
Target users: PASS|FAIL — <note>
Goals/non-goals: PASS|FAIL — <note>
Metrics: PASS|FAIL — <note>
Scope boundary: PASS|FAIL — <note>
Requirements: PASS|FAIL — <note>
Acceptance criteria: PASS|FAIL — <note>
Launch criteria: PASS|FAIL — <note>
Blocking gaps:
- <gap>
Next action:
- <action>
```

`READY` means the document passes the readiness checks defined here. It does not prove owner approval, authorize technical implementation, or supersede decision-provenance requirements.

## Common Pitfalls

1. **Artifact/capability confusion.** `PRD` is the produced artifact; `product-requirements` is the executable skill.
2. **False rename.** Creating a second `prd` skill introduces duplicate ownership and routing ambiguity.
3. **Solution-first PRD.** “Build a dashboard” is not a problem statement; name the user outcome first.
4. **No non-goals.** Without explicit non-goals, scope creep is guaranteed.
5. **Vague metrics.** “Improve UX” is not measurable. Use observable behavior or thresholds.
6. **Untestable requirements.** If it cannot be observed or verified, it is not ready for implementation.
7. **Acceptance criteria without traces.** Criteria should point back to requirements.
8. **Launch equals code complete.** Launch readiness also needs verification, support, analytics, and operational confidence.
9. **Hidden open questions.** Unknowns must be named; otherwise they become late-stage blockers.
10. **Readiness equals approval.** An agent-authored or revised PRD does not approve itself.

## Verification Checklist

- [ ] Request intent is authoring, revision, or readiness review.
- [ ] Execution identity remains `product-requirements`; artifact terminology may use PRD.
- [ ] Problem statement is user/business-outcome first.
- [ ] Target users are explicit.
- [ ] Goals and non-goals both exist.
- [ ] Success metrics are measurable.
- [ ] Scope-in and scope-out both exist.
- [ ] Functional requirements are testable.
- [ ] Non-functional requirements cover relevant quality attributes.
- [ ] Acceptance criteria are observable and trace to requirements.
- [ ] Constraints, dependencies, risks, and open questions are explicit.
- [ ] Launch criteria define readiness beyond code completion.
- [ ] PRD can feed MVP planning and technical spec without guessing intent.
- [ ] PRD readiness is not represented as owner approval or implementation authorization.
