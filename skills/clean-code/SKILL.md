---
name: clean-code
description: Evidence-backed internal code-quality assessment and implementation guidance — naming, readability, control flow, errors, comments, duplication, functions, classes, modules, and tests without arbitrary metric dogma or behavior-changing cleanup.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.related_skills: '["master-engineer","implementation-context-discovery","refactoring","test-driven-development","solid-design","architecture-review","code-review-workflow"]'
---

# Clean Code

Evaluate and improve how implementation intent is expressed inside functions, classes, modules, tests, and local APIs. Preserve behavior, repository conventions, and accepted architecture while making the code easier to understand, change, verify, and operate.

## Trigger

Load this skill when:

- implementation or a diff needs an internal code-quality review;
- code works but is difficult to understand or modify safely;
- naming, control flow, error handling, duplication, comments, or local structure is under question;
- a feature implementation needs code-quality guidance before independent review;
- a named code smell needs diagnosis before `refactoring` is applied.

Do not use this skill as:

- a formatter or linter replacement;
- architecture acceptance — use `architecture-review`;
- a behavior-preserving transformation procedure — use `refactoring`;
- a substitute for tests, runtime evidence, security review, or product acceptance;
- permission to rewrite unrelated code while implementing a feature.

## Core Boundary

```text
clean-code
  owns:
    internal readability and maintainability diagnosis
    local implementation guidance
    named code-quality findings
    smallest safe correction recommendation

  delegates:
    repository convention discovery → implementation-context-discovery
    architecture and owner decisions → master-engineer
    structural behavior-preserving change → refactoring
    behavior proof → test-driven-development and applicable tests
    independent architecture acceptance → architecture-review
    final merge-readiness lifecycle → code-review-workflow
```

## Hard Rules

```text
1. Evidence before preference.
   Cite the code region, behavior, repository rule, or concrete maintenance risk.

2. Repository conventions outrank personal style.
   Do not normalize code into a preferred style that conflicts with accepted local practice.

3. Behavior is a preservation lock.
   Cleanup must not silently add a feature, fix an unrelated bug, alter an API, or change observable semantics.

4. Metrics are signals, not verdicts.
   Line count, parameter count, complexity, nesting, and class size can trigger inspection but cannot auto-fail code without context.

5. Duplication means duplicated knowledge or change responsibility.
   Similar syntax alone is not enough to justify abstraction.

6. Comments explain why, constraints, trade-offs, hazards, or non-obvious contracts.
   Comments that merely translate the code are a smell, not a success condition.

7. Error handling must preserve meaning.
   Do not swallow, flatten, log-and-ignore, or replace actionable errors with vague messages.

8. Tests are production code for behavior evidence.
   Test naming, setup, fixtures, assertions, and failure messages must communicate the protected behavior.

9. Smallest durable correction.
   Do not turn a local readability issue into a speculative framework, hierarchy, generic abstraction, or repository-wide rewrite.

10. Formatter, linter, compiler, or green tests are evidence — not clean-code approval by themselves.
```

## Required Inputs

```yaml
clean_code_context:
  code_or_diff: <required>
  intended_behavior: <spec, tests, or stated contract>
  repository_conventions: <reference | NOT_VERIFIED>
  architecture_and_owner_context: <reference | NOT_VERIFIED>
  affected_tests: []
  change_scope: []
  preservation_locks: []
```

When intended behavior or material repository conventions are missing, report `NOT_VERIFIED` for conclusions that depend on them. Do not invent the preferred local style.

## Procedure

### 1. Establish behavior and scope

Identify the code under review, intended behavior, accepted scope, preservation locks, and relevant repository conventions. Separate the requested change from opportunistic cleanup.

### 2. Read for intent before style

Explain what the code appears to do, where decisions are made, what changes together, and which parts require external context. If the implementation cannot be understood confidently, record the evidence gap before recommending a rewrite.

### 3. Inspect local expression quality

Review the materially affected areas:

```text
names and vocabulary
function focus and control flow
class/module cohesion and ownership
state mutation and side effects
parameter and return contracts
error semantics and recovery
comments and documentation
knowledge duplication
API and boundary readability
test readability and failure diagnosis
```

Load [references/readability-and-structure.md](references/readability-and-structure.md) for naming, flow, functions, modules, and tests.

Load [references/errors-comments-and-duplication.md](references/errors-comments-and-duplication.md) for error meaning, comments, duplication, side effects, and evidence rules.

### 4. Name findings by risk, not taste

Each finding must include:

```yaml
finding:
  location: <file, symbol, or region>
  category: <naming | flow | cohesion | errors | comments | duplication | side-effects | api | tests>
  evidence: <observable code fact>
  consequence: <comprehension, change, defect, test, or operation risk>
  severity: BLOCKING | HIGH | MEDIUM | LOW | NOTE
  confidence: HIGH | MEDIUM | LOW
```

Do not report “unclean”, “bad naming”, or “too long” without the concrete ambiguity, mixed responsibility, hidden state, duplicated knowledge, or change risk.

### 5. Choose the smallest correction route

```text
clarify name or contract
→ simplify expression or guard flow
→ isolate side effect
→ improve error semantics
→ remove misleading comment or add decision rationale
→ remove proven duplicated knowledge
→ extract cohesive function/module
→ delegate a named structural change to refactoring
→ route an owner/boundary issue to master-engineer or architecture-review
```

Do not extract an abstraction until the shared concept and change reason are proven.

### 6. Verify preservation and quality delta

Check applicable tests, types, lint, build, focused runtime behavior, and changed failure paths. Report what each evidence item proves and what remains unverified.

A cleaner diff is not complete when behavior changed accidentally, coverage regressed, errors lost meaning, or the new abstraction increases indirection without reducing a verified risk.

## Output Contract

```yaml
code_quality_review:
  verdict: PASS | PASS_WITH_FLAGS | NEEDS_WORK | NOT_VERIFIED
  scope_reviewed: []
  repository_conventions: <reference | NOT_VERIFIED>
  intended_behavior: <reference | NOT_VERIFIED>
  readability_findings: []
  maintainability_risks: []
  named_smells: []
  recommended_refactorings: []
  behavior_change_risk: []
  verification_evidence: []
  evidence_gaps: []
  handoffs: []
```

Verdict rules:

- `PASS` — no material internal code-quality finding remains in reviewed scope.
- `PASS_WITH_FLAGS` — only concrete non-blocking risks remain.
- `NEEDS_WORK` — a correctable code-quality issue materially impairs safe comprehension, change, testing, failure diagnosis, or maintenance.
- `NOT_VERIFIED` — missing behavior, repository, code, or test evidence prevents a responsible verdict.

## Quality Gates

- [ ] Intended behavior and reviewed scope are explicit?
- [ ] Repository conventions were inspected or marked `NOT_VERIFIED`?
- [ ] Every material finding cites a code region and consequence?
- [ ] Metrics were used as investigation signals rather than automatic verdicts?
- [ ] Duplication was evaluated as duplicated knowledge/change responsibility?
- [ ] Error meaning and side effects remain visible?
- [ ] Recommended changes preserve behavior and stay inside scope?
- [ ] Structural changes are delegated to `refactoring` with tests green first?
- [ ] Architecture concerns are handed to the architecture owner/reviewer?
- [ ] Verification evidence and remaining gaps are separated?

## Failure Signals

```text
STYLE_PREFERENCE_AS_RULE
ARBITRARY_METRIC_GATE
LINT_EQUALS_CLEAN
BEHAVIOR_CHANGING_CLEANUP
UNRELATED_REWRITE
PREMATURE_ABSTRACTION
DUPLICATION_BY_SYNTAX_ONLY
ERROR_MEANING_LOST
COMMENT_TRANSLATES_CODE
REPOSITORY_CONTEXT_MISSING
EVIDENCE_FREE_FINDING
```

## Handoff

- To `refactoring`: named smell, preservation locks, green-test evidence, smallest structural transformation, and stop condition.
- To `master-engineer`: ownership, API, module, dependency, or architecture decision that exceeds local expression quality.
- To `architecture-review`: implemented boundary or contract compliance requiring independent acceptance.
- To `code-review-workflow`: scoped findings, severity, evidence, unresolved flags, and clean-code verdict.
