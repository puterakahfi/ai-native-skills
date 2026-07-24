---
name: solid-design
description: Pragmatic SOLID design assessment for responsibilities, extension pressure, behavioral substitutability, client-specific interfaces, and dependency direction — with applicability, alternatives, trade-offs, and explicit rejection of premature abstraction.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.related_skills: '["master-engineer","clean-code","design-patterns","refactoring","test-driven-development","clean-architecture","architecture-review","code-review-workflow"]'
---

# SOLID Design

Use SOLID as a set of design lenses for concrete change pressure, client behavior, and dependency stability. Do not use the acronym as a checklist that forces interfaces, inheritance, indirection, or class proliferation into every implementation.

## Trigger

Load this skill when:

- a class, module, component, service, or local API has unclear responsibilities;
- change pressure suggests an extension point or variation boundary;
- inheritance, interface implementation, mocks, or substitutability is under review;
- consumers depend on broad interfaces they only partly use;
- stable policy depends directly on volatile infrastructure or provider details;
- a proposed pattern or abstraction claims SOLID as its justification;
- code review needs an explicit object/module design verdict.

Do not use this skill as:

- a demand to apply all five principles to every code region;
- architecture ownership — use `master-engineer`;
- pattern implementation guidance — use `design-patterns`;
- behavior-preserving structural execution — use `refactoring`;
- independent architecture acceptance — use `architecture-review`;
- proof that code is correct, secure, performant, or product-accepted.

## Core Boundary

```text
solid-design
  owns:
    per-principle applicability
    responsibility and change-pressure analysis
    behavioral substitutability analysis
    client-interface fitness analysis
    policy/detail dependency-direction analysis
    abstraction-risk and alternative comparison
    smallest justified redesign recommendation

  delegates:
    system and module ownership → master-engineer
    local expression quality → clean-code
    pattern selection and implementation → design-patterns
    structural behavior-preserving change → refactoring
    architecture-style selection → clean-architecture when applicable
    independent compliance verdict → architecture-review
    final merge-readiness lifecycle → code-review-workflow
```

## Hard Rules

```text
1. Applicability before principle.
   A principle may be NOT_APPLICABLE for the reviewed decision. Do not manufacture a violation.

2. Forces before abstraction.
   Name actual change pressure, consumer need, behavior contract, or dependency volatility first.

3. SRP means one cohesive ownership boundary and related reasons to change.
   It does not mean one method, one field, or one stakeholder word per class.

4. OCP protects proven variation pressure.
   It does not require an extension mechanism before a second behavior or credible change force exists.

5. LSP is behavioral substitutability.
   Type compatibility, inheritance, compilation, or shared method names do not prove it.

6. ISP starts from clients.
   Split an interface only when consumers have materially different needs or change pressure.

7. DIP is dependency direction between stable policy and volatile details.
   A dependency-injection container, constructor injection, or interface keyword alone does not prove it.

8. Composition and direct code remain valid options.
   Interfaces and inheritance are not morally superior.

9. Repository conventions and accepted architecture outrank textbook folder or class shapes.

10. Prefer the smallest durable correction.
    Reject speculative factories, adapters, generic repositories, base classes, and indirection without evidence.
```

## Required Inputs

```yaml
solid_context:
  design_subject: <class, module, component, service, API, or diff>
  intended_behavior: <spec, tests, or contract>
  change_pressure: []
  consumers: []
  repository_conventions: <reference | NOT_VERIFIED>
  architecture_and_owner_context: <reference | NOT_VERIFIED>
  existing_variants_or_implementations: []
  affected_tests: []
  preservation_locks: []
```

When consumers, behavior contracts, or actual change forces are missing, mark affected conclusions `NOT_VERIFIED`. Do not infer a universal abstraction requirement.

## Procedure

### 1. Frame the design decision

Name the exact subject, intended behavior, current ownership, consumers, known variants, change pressure, constraints, and non-goals. Separate an observed design problem from a request to “make it SOLID.”

### 2. Establish applicability

For each principle, classify:

```text
APPLICABLE
  evidence shows the principle materially affects the decision

PARTIAL
  only a bounded aspect applies

NOT_APPLICABLE
  the current design has no relevant force or substitution/client/dependency boundary

NOT_VERIFIED
  evidence is insufficient for a responsible conclusion
```

Load [references/principles-and-applicability.md](references/principles-and-applicability.md) for SRP, OCP, applicability, change-pressure mapping, and anti-dogma guidance.

### 3. Assess SRP — responsibility and ownership

Inspect:

- what concept the subject owns;
- which state and invariants belong together;
- which changes occur for the same product or domain reason;
- whether unrelated policies, actors, or volatility are coupled;
- whether decomposition would clarify ownership or merely fragment navigation.

A valid SRP finding names the unrelated change reasons and their consequence. File size or method count alone is not evidence.

### 4. Assess OCP — proven variation pressure

Inspect:

- existing variants and credible near-term variation;
- stable behavior that should remain closed to repeated modification;
- extension seams already accepted by the repository;
- whether a conditional is a clear finite rule or recurring variation pressure;
- whether direct modification remains simpler and safer.

Do not introduce an interface, strategy, plugin, event, or registry merely because future change is imaginable.

### 5. Assess LSP — behavioral substitutability

Inspect the promises clients rely on:

- accepted inputs and strengthened preconditions;
- outputs and weakened postconditions;
- invariants and state transitions;
- errors, side effects, ordering, timing, idempotency, and resource behavior;
- unsupported operations or surprising no-op behavior;
- tests that run the same behavioral contract against substitutes.

Load [references/substitution-interfaces-and-dependencies.md](references/substitution-interfaces-and-dependencies.md) for LSP, ISP, DIP, contract tests, and dependency-direction analysis.

### 6. Assess ISP — client-specific interface fitness

Map each consumer to the operations and guarantees it requires. Report a violation only when broad interfaces create unused dependencies, fake implementations, change coupling, privilege expansion, or confusing contracts.

Do not split interfaces into one-method fragments without cohesive client boundaries.

### 7. Assess DIP — policy and detail direction

Identify:

```text
stable policy
volatile detail
boundary owner
abstraction owner
composition root or wiring location
```

Stable policy should not depend on provider/framework types when that dependency makes policy harder to test, change, or reuse. The abstraction should normally be owned by the policy or consumer boundary, not by the volatile implementation.

Do not add an interface when direct dependency is stable, local, and not creating meaningful coupling risk.

### 8. Compare alternatives

At minimum compare:

```text
keep direct design
clarify ownership without abstraction
bounded extraction
composition
interface or port
polymorphic strategy
repository-accepted pattern
```

For each alternative state the forces it addresses, new indirection, migration cost, testing consequence, and reversal path.

### 9. Select the smallest justified option

The selected option must address a verified risk with less total complexity than it introduces. If no redesign is justified, say so explicitly.

### 10. Define verification and handoff

Specify behavior tests, contract tests, client tests, dependency checks, or architecture review evidence needed after implementation. Delegate structural changes to `refactoring` and architecture acceptance to `architecture-review`.

## Finding Contract

```yaml
principle_finding:
  principle: SRP | OCP | LSP | ISP | DIP
  applicability: APPLICABLE | PARTIAL | NOT_APPLICABLE | NOT_VERIFIED
  location: <file, symbol, module, or boundary>
  evidence: <observable design fact>
  violated_or_at_risk_contract: <behavior, client, ownership, or dependency promise>
  consequence: <change, defect, compatibility, test, or maintenance risk>
  severity: BLOCKING | HIGH | MEDIUM | LOW | NOTE
  confidence: HIGH | MEDIUM | LOW
  smallest_correction: <bounded option>
```

## Output Contract

```yaml
solid_assessment:
  verdict: PASS | PASS_WITH_FLAGS | NEEDS_WORK | NOT_VERIFIED
  subject: <reference>
  intended_behavior: <reference | NOT_VERIFIED>
  repository_conventions: <reference | NOT_VERIFIED>
  change_pressure: []
  consumers: []
  applicability:
    srp: APPLICABLE | PARTIAL | NOT_APPLICABLE | NOT_VERIFIED
    ocp: APPLICABLE | PARTIAL | NOT_APPLICABLE | NOT_VERIFIED
    lsp: APPLICABLE | PARTIAL | NOT_APPLICABLE | NOT_VERIFIED
    isp: APPLICABLE | PARTIAL | NOT_APPLICABLE | NOT_VERIFIED
    dip: APPLICABLE | PARTIAL | NOT_APPLICABLE | NOT_VERIFIED
  principle_findings:
    srp: []
    ocp: []
    lsp: []
    isp: []
    dip: []
  abstraction_risks: []
  alternatives: []
  selected_option: <decision>
  tradeoffs: []
  verification_evidence: []
  evidence_gaps: []
  handoffs: []
```

Verdict rules:

- `PASS` — no material applicable SOLID design risk remains in reviewed scope.
- `PASS_WITH_FLAGS` — only concrete non-blocking design risks remain.
- `NEEDS_WORK` — a verified responsibility, extension, substitution, client-interface, or dependency-direction issue materially impairs safe change or behavior.
- `NOT_VERIFIED` — missing behavior, consumer, change-pressure, repository, or test evidence prevents a responsible verdict.

## Quality Gates

- [ ] Exact subject, behavior, consumers, and change pressure are explicit?
- [ ] Every principle has an applicability classification?
- [ ] Findings cite concrete behavior, ownership, client, or dependency evidence?
- [ ] SRP is based on cohesive change reasons rather than size metrics?
- [ ] OCP is tied to proven variation pressure?
- [ ] LSP checks behavioral contracts rather than compilation or inheritance alone?
- [ ] ISP maps interfaces to actual client needs?
- [ ] DIP distinguishes stable policy from volatile detail?
- [ ] Direct implementation and composition were considered?
- [ ] Premature abstraction and pattern worship were rejected?
- [ ] Alternatives and trade-offs are explicit?
- [ ] Verification and independent review remain separate from design recommendation?

## Failure Signals

```text
SOLID_AS_CHECKLIST
INTERFACE_FOR_EVERY_CLASS
SRP_BY_METHOD_COUNT
OCP_WITHOUT_VARIATION
LSP_BY_TYPE_COMPATIBILITY
ISP_BY_ONE_METHOD_FRAGMENTS
DIP_EQUALS_DI_CONTAINER
PATTERN_WORSHIP
PREMATURE_ABSTRACTION
CLIENTS_NOT_IDENTIFIED
CHANGE_PRESSURE_INVENTED
REPOSITORY_CONTEXT_MISSING
SELF_APPROVED_ARCHITECTURE
```

## Handoff

- To `clean-code`: local naming, flow, readability, error, comment, or duplication findings.
- To `design-patterns`: a verified force set requiring pattern comparison and implementation guidance.
- To `refactoring`: named structural change, behavior locks, green-test evidence, sequence, and stop condition.
- To `clean-architecture`: material architecture-style or policy/mechanism boundary decision.
- To `master-engineer`: ownership, module, API, dependency, or system-level decision.
- To `architecture-review`: implemented design and dependency compliance requiring independent acceptance.
- To `code-review-workflow`: applicability, findings, severity, evidence, unresolved flags, and SOLID verdict.
