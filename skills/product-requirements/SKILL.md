---
name: product-requirements
description: Author and verify PRDs for AI-native product development. Use when turning discovery, feature intent, user needs, constraints, and success metrics into a Product Requirements Document with testable acceptance criteria and launch readiness gates.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/product-management/product-requirements.contract.yaml
  ai-native-skills.related_skills: '["business-value-alignment", "experiment-design", "product-manager", "user-research", "spec-workflow", "decision-making", "api-contract"]'
---

# Product Requirements

## When to Use

Use when the user asks to write a PRD, turn discovery notes into product requirements, define goals/metrics/scope/acceptance criteria, or review feature readiness before technical spec.

Do not use for: technical architecture specs (`spec-workflow`, `api-contract`); release execution; implementation task breakdown only (`product-manager`).

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

1. **Frame the problem.** Problem statement names a user/business outcome, does not prescribe implementation.
2. **Name the users.** Primary target user explicit; excluded users named when relevant.
3. **Carry experiment evidence forward.** Results referenced, or untested assumptions listed as risks.
4. **Define goals and non-goals.** Success and boundaries both documented.
5. **Make metrics measurable.** Each success metric has a target or observable threshold.
6. **Set scope boundaries.** Scope-in and scope-out both exist.
7. **Write requirements.** Every requirement is testable or traces to acceptance criteria.
8. **Write acceptance criteria.** Use Given/When/Then or equivalent observable evidence.
9. **Capture constraints, dependencies, and risks.** Blockers are explicit, not implied.
10. **Define launch criteria.** Readiness includes verification, support, analytics, and operational signals.
11. **Check traceability.** `requirement → acceptance criterion → verification evidence` can be followed.

## Quality Gates

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
- Implementation detail excluded unless it is a real constraint.

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

## Common Pitfalls

1. **Solution-first PRD.** "Build a dashboard" is not a problem statement; name the user outcome first.
2. **No non-goals.** Without explicit non-goals, scope creep is guaranteed.
3. **Vague metrics.** "Improve UX" is not measurable. Use observable behavior or thresholds.
4. **Untestable requirements.** If it cannot be observed or verified, it is not ready for implementation.
5. **Acceptance criteria without traces.** Criteria should point back to requirements.
6. **Launch equals code complete.** Launch readiness also needs verification, support, analytics, and operational confidence.
7. **Hidden open questions.** Unknowns must be named; otherwise they become late-stage blockers.

## Verification Checklist

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
