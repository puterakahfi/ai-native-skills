# Workflow Integration Matrix

Use this matrix to attach `production-code-quality-baseline` without creating a second primary lifecycle or duplicating specialist ownership.

## Routing rule

```text
classify requested outcome
→ select exactly one primary lifecycle
→ classify production-code impact
→ attach production-code-quality-baseline when impact is PRODUCTION_CODE_CHANGE
→ preserve the primary lifecycle phase order
→ load quality capabilities only in the phases that need them
```

The overlay owns cross-workflow applicability, evidence, gate, and handoff consistency. The primary workflow still owns delivery sequence and lifecycle-specific behavior.

## Lifecycle matrix

| Primary lifecycle | When baseline attaches | Lifecycle ownership preserved | Required integration | Review/authority boundary |
|---|---|---|---|---|
| `new-feature-workflow` | Approved feature will create or materially change production behavior | Feature scope, topology, design decisions, implementation-context mapping, implementation, verification, submission | Attach at plan; execute TDD and clean-code during implementation; emit applicability, capability-execution, evidence, gate, and blocking records during verification | `architecture-review` and `code-review-workflow`; merge authority remains separate |
| `bugfix-workflow` | Existing production behavior is broken or regressed | Reproduction, causal investigation, smallest root-cause correction, regression verification | Record failing reproduction and RED before correction; apply clean-code and conditional concerns to bounded fix; verify baseline gates | Independent architecture and code review; technical verdict does not self-authorize merge |
| `spec-workflow` | Phase 5 implements production code | Constitution, specification, plan, task/context construction, scope control | Attach only for production implementation tasks; TDD is default; exception requires attributable authority and alternative verification | Baseline output hands off to normal architecture/code review and product policy |
| `product-development-workflow` | Product lifecycle delegates an accepted release unit into production implementation | Discovery, value/acceptance, release-unit decomposition, release/deploy/launch/learn | Do not run a parallel product lifecycle; baseline attaches inside delegated feature/bugfix/spec implementation slice | Product acceptance and release authority remain product-owned |
| `code-review-workflow` | Review consumes a baseline report from a production-code submission | Changed-domain classification, independent technical review, verdict and merge-readiness mapping | Do not re-run the baseline or primary lifecycle; verify report, actual diff, evidence, and missing claims | Technical review remains distinct from approval and merge authorization |
| `deployment-workflow` | Normally does not attach for deployment-only execution; attach only when deployment task also changes production code | Release candidate, authorization, deploy, verify, confirm/rollback | Consume prior technical and quality evidence; do not recreate implementation history | Deployment authority and product acceptance remain separate |
| `redesign-workflow` | Attach when redesign includes repository production-code changes | Design strategy, composition, implementation, rendered acceptance, refinement | Baseline overlays implementation quality; design-review facade still owns rendered/design acceptance | Architecture/code/design verdicts remain separate from merge and product acceptance |
| `spike` | Usually excluded as `DISPOSABLE_EXPERIMENT`; reclassify when output will enter production repository | Reversible experiment and learning decision | A disposable experiment needs explicit bounded classification; production promotion requires a real lifecycle plus baseline | Spike evidence is not implementation approval |
| `task-continuity` | Never replaces or independently attaches the baseline | Resume/source-resolution and exact-next-action recovery | Restore the prior primary lifecycle, baseline state, evidence, gates, blockers, and remaining authorities | Continuity reconstruction cannot upgrade missing evidence or authority |

## Phase composition

### Plan/classify

```text
workflow-router
decision-provenance
implementation-context-discovery
production-code-quality-baseline
primary lifecycle owner
```

Required outputs:

```yaml
production_code_applicability: <status>
primary_lifecycle: <workflow>
quality_overlay: production-code-quality-baseline
applicability_map: {}
required_evidence: []
required_reviewers: []
remaining_authorities: []
```

### Execute

```text
primary lifecycle owner
master-engineer
test-driven-development
clean-code
only justified conditional specialists
```

Required distinctions:

```text
capability resolved
capability executed
output produced
claim made
evidence linked
gate evaluated
```

### Verify/review

```text
baseline evidence and gate evaluation
architecture-review
code-review-workflow
specialist reviewer when material
product/repository authority handoff
```

Do not load `production-code-quality-baseline` as an independent reviewer. It produces and coordinates the report; independent reviewers verify the implemented result.

## Conditional specialist matrix

| Concern | Load when | Valid evidence-backed skip |
|---|---|---|
| `solid-design` | responsibility, extension, substitution, client-interface, or dependency-direction pressure is material | `NOT_APPLICABLE` or `NOT_JUSTIFIED` with force analysis |
| `domain-driven-design` | domain language, invariants, context boundaries, or domain complexity are material | thin pass-through/CRUD with no meaningful domain decision |
| `design-patterns` | recurring design forces and alternatives justify a named pattern | no recurring force or pattern would add needless indirection |
| `clean-architecture` | policy/mechanism, dependency rule, or architecture-style boundary is material | local change with no architecture-style decision |
| `ports-and-adapters` | replaceable external boundary or dependency inversion is material | no external boundary or replacement pressure |
| `security-review` / `threat-modeling` | trust, auth, permission, secret, untrusted input, sensitive data, or attack surface changes | verified absence of security-boundary impact |
| product-defined performance specialist | latency, throughput, memory, scale, or cost objective is materially affected | no material performance objective or path impact |
| `resilience-engineering` / `observability-design` | timeout, retry, degradation, recovery, diagnosis, or operational visibility changes | verified local behavior with no operational boundary impact |
| `data-modeling` | data shape, integrity, compatibility, or migration changes | no data-model or migration impact |
| `design-review` plus domain reviewer | rendered, interactive, content, accessibility, responsive, or exported visual behavior changes | no user-facing/rendered behavior impact |

## Anti-circularity checks

A composition is invalid when:

```text
production-code-quality-baseline becomes the primary lifecycle
code-review-workflow invokes the baseline as its own independent reviewer
baseline marks architecture review PASS before architecture-review executes
new-feature-workflow and spec-workflow both claim primary ownership of the same execution slice
product-development-workflow reimplements feature/bugfix mechanics instead of delegating
review PASS is converted directly into merge or product acceptance
```

## Minimum handoff between workflows

```yaml
quality_handoff:
  source_workflow: <primary lifecycle>
  source_phase: <phase>
  production_code_applicability: <status>
  baseline_report_ref: <ref>
  capabilities_resolved: []
  capabilities_executed: []
  evidence_refs: []
  gate_results: []
  reviewer_results: []
  blocking_gaps: []
  transition_eligibility: {}
  remaining_authorities: []
```

The receiving workflow must preserve unsupported fields as missing or `NOT_VERIFIED`; it must not infer them from a successful prior phase.
