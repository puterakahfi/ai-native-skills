---
name: new-feature-workflow
description: Evidence-backed new-feature workflow — verify scope and decision authority, approve architecture/design decisions, discover repository implementation context, implement with tests, verify technical, convention, and rendered outcomes, submit a decision ledger, and merge only through code-review-workflow approval plus merge authorization.
license: MIT
metadata:
  ai-native-skills.version: 2.4.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "master-engineer master-design delivery-work-breakdown implementation-context-discovery decision-provenance spec-workflow clean-architecture solid-design clean-code test-driven-development architecture-review code-review-workflow design-review"
  ai-native-skills.type: workflow
  ai-native-skills.implements: ai-native-core/contracts/workflows/new-feature.contract.yaml
  ai-native-skills.contract-version: ~0.4
  ai-native-skills.skill_load_order: '[{"phase":"plan","load":["master-engineer","decision-provenance"]},{"phase":"delivery-topology","load":["delivery-work-breakdown","decision-provenance"]},{"phase":"design-decision","load":["master-engineer","clean-architecture","solid-design","diagram-architect","master-design","decision-provenance"]},{"phase":"implementation-context","load":["implementation-context-discovery","decision-provenance"]},{"phase":"implement","load":["master-engineer","clean-code","solid-design","test-driven-development"]},{"phase":"verify","load":["clean-code","solid-design","architecture-review","design-review","decision-provenance"]},{"phase":"submit","load":["decision-provenance"]},{"phase":"review","load":["code-review-workflow"]}]'
  ai-native-skills.skills: '{"required":["master-engineer","delivery-work-breakdown","implementation-context-discovery","decision-provenance","clean-code","test-driven-development","architecture-review","code-review-workflow"],"optional":["clean-architecture","solid-design","diagram-architect","master-design","design-review"]}'
---

# New Feature Workflow

```text
verified scope
→ approved delivery topology
→ approved architecture/design decisions
→ repository implementation-context mapping
→ implementation with tests
→ technical, convention, runtime, and rendered verification
→ decision/evidence handoff
→ independent review and merge authorization
```

## Core boundary

```text
Spec before implementation.
Decision authority before material scope, dependency, exception, or lock changes.
Design decision before implementation when affected.
Implementation-context mapping before code in an existing repository.
Rendered acceptance after implementation when user-facing output changes.
Architecture and code-review approval before merge.
```

A wireframe or specification decides what to build. `implementation-context-discovery` decides how the accepted capability maps to the repository. Neither proves the implemented result. Technical review and merge authority remain independent.

## Hard rules

```text
1. Define problem, verified scope, criteria, and affected domains before coding.
2. Material scope, lock, dependency, migration, exception, and approval claims require decision provenance.
3. Agent-authored issue/spec/PR text is not owner approval by itself.
4. Separate pre-implementation design and implementation-context decisions from post-implementation acceptance.
5. Never claim implemented PASS from a wireframe, mapping, diagram, or source-only artifact.
6. Implementation must trace to verified scope, design decisions, convention locks, and implementation mapping.
7. Existing repositories require implementation-context discovery before code when framework/component/styling/icon/state/form/query/data/build conventions are affected.
8. Package presence alone does not establish canonical status.
9. Reuse, bounded extension, composition, or semantic-native implementation precedes a dependency proposal.
10. A new dependency requires a proven capability gap, consequences, and verified authority.
11. A new route, data boundary, permission behavior, product dependency, framework/system change, or material lock change requires explicit bounded approval.
12. Write tests as part of implementation.
13. User-facing or generated visual changes require fresh rendered/exported evidence.
14. Source-only evidence cannot approve changed visual, interaction, runtime, or accessibility behavior.
15. Run architecture-review after implementation; pre-code discovery cannot self-certify.
16. LIMITED REVIEW cannot authorize complete specialist-domain acceptance.
17. Conditional acceptance requires verified non-blocking risk authority.
18. Submit spec, issue, decision ledger, implementation-context handoff, technical evidence, and applicable design evidence together.
19. Final technical review and merge authorization belong to code-review-workflow.
20. Do not bundle unrelated, unapproved, or opportunistic migration work.
21. Use `clean-architecture` only when architecture-style or policy/mechanism boundaries are materially affected and justified by forces.
22. Use `solid-design` only when responsibility, extension, substitution, client-interface, or dependency design is material.
23. Apply `clean-code` during implementation and verification without arbitrary size metrics or behavior-changing cleanup.
24. Pre-implementation engineering design guidance never self-approves the implemented architecture or code quality.
```

## When to use

Use when adding a capability to an existing product or codebase.

```text
product from zero        → product-development-workflow
bug or regression        → bugfix-workflow
broad design replacement → redesign-workflow
known narrow design fix  → design-refinement
review-only request      → code-review-workflow or design-audit
```

## Workflow context

Record before implementation:

```yaml
feature:
  title: <title>
  problem: <problem>
  issue_ref: <issue or task>

  delivery_topology:
    release_unit: <standalone_change | feature | epic | product_release>
    parent_ref: <epic/product ref or null>
    acceptance_criteria_refs: []
    dependency_refs: []
    independently_releasable: <true | false | unknown>
    feature_flag_policy_ref: <record | null | unknown>
    release_branch: <product-defined>
    integration_branch: <branch | not_applicable | unknown>
    base_branch: <explicit>
    pr_target: <explicit>
    topology_record_ref: <delivery-work-breakdown output>

  decision_sources: []
  required_authorities: []
  previous_decision_records: []

  effective_verified_scope:
    scope_in: []
    scope_out: []
    approved_dependencies: []
    preserved_routes_or_boundaries: []
    prohibited_parallel_systems: []

  acceptance_criteria: []
  affected_domains:
    architecture: <true | false>
    architecture_style_or_boundary_design: <true | false>
    internal_code_quality: <true | false>
    object_module_design: <true | false>
    logic: <true | false>
    data: <true | false>
    security: <true | false>
    user_facing_design: <true | false>
    generated_or_exported_visual: <true | false>

  implementation_context:
    repository_ref: <ref>
    affected_capability_families: []
    profile_ref: <implementation_context_profile or null>
    canonicality_decisions: []
    convention_locks: []
    reuse_extension_decisions: []
    dependency_decisions: []
    implementation_mapping: []
    evidence_gaps: []

  technical_approach: <summary>
  verification_plan: []
  approval_policy: <product-defined>
  merge_authority: <role or policy>
```

## Phase 1 — Plan

**Gate:** spec, affected domains, scope provenance, and verification plan exist before implementation.

Define:

```text
problem and intended outcome
scope in and scope out
observable acceptance criteria
technical approach
architecture, logic, data, security, design, and implementation-system impact
issue tracker reference
verification and evidence plan
decision sources and required authorities
```

Run `decision-provenance` for initial scope and claimed approval. An agent-authored issue or generated spec is not automatically an approved system of record.

Replace “works correctly” with observable behavior, context, and expected result.

**Done when:** scope, criteria, issue, authorities, affected capability families, and evidence plan are explicit.

## Phase 1B — Delivery topology

**Gate:** release unit, parent, acceptance traceability, dependency graph, base branch, and PR target are explicit before branch creation or PR submission.

Load `delivery-work-breakdown`. A dependent child of an epic branches from and targets the approved epic/integration branch. Direct-to-release requires independent releasability or an approved default-safe feature flag with no unflagged incomplete path.

Block orphan tasks, dependency cycles, unknown targets, and any target justified only by the repository default branch.

**Done when:** the topology verdict is PASS and recorded in workflow context.

## Phase 2 — Architecture and design decision

**Gate:** applicable decisions have verified authority before implementation mapping.

Required when the feature changes:

```text
system boundaries, contracts, integration, data model, or permissions
user flow, IA, component model, interaction, responsive behavior, or visual direction
required states, content, assets, or fidelity locks
specialized generated/exported behavior
framework or shared implementation-system responsibilities
```

Load only relevant owners:

```text
master-engineer       architecture, contracts, data, integration
clean-architecture    architecture-style applicability and policy/mechanism boundaries when material
solid-design          responsibility, extension, substitution, client-interface, dependency design when material
master-design         task flow, component model, responsive behavior, visual direction
diagram-architect     decision-bearing diagrams when useful
decision-provenance   authority, scope, supersession, unresolved approval
specialized owner     domains outside built-in coverage
```

Load `references/design-decision-and-acceptance.md` for decision schema and handoff.

**Done when:** approval boundary, required states/contexts, locks, assumptions, and implementation-ready criteria are explicit.

## Phase 3 — Implementation-context discovery

**Gate:** repository convention locks and implementation mapping exist before code production.

Load `implementation-context-discovery` for the affected capability families.

Inspect applicable evidence:

```text
engineering contracts and ADRs
package manifests and lockfiles
workspace/framework configuration and aliases
shared components, registry, primitives, variants, tokens, imports
icon wrappers and repeated icon usage
state, form, query, validation, animation, table, and data tooling
build, lint, test, Storybook, examples, migrations, and deprecations
```

Produce:

```text
implementation_context_profile
canonicality_decisions
convention_locks
reuse_extension_decisions
new_dependency_decisions
implementation_mapping
prohibited_parallel_systems
evidence gaps and verification plan
```

Decision order:

```text
reuse
→ existing variant
→ bounded extension
→ compose canonical primitives
→ product-specific component
→ semantic native element
→ dependency only after a proven capability gap
```

`package.json` presence is insufficient. A source-copied component system may be canonical through registry/source/import evidence. A legacy or transitive package is not automatically valid for new work.

When a dependency candidate remains `ROUTE_FOR_APPROVAL` or material canonicality is `unknown`, stop the affected implementation slice.

**Done when:** the selected implementation path, expected paths/imports, protected systems, dependency authority, and evidence gaps are explicit.

## Phase 4 — Implement

**Gate:** code traces to verified scope, decisions, convention locks, and implementation mapping.

Load `master-engineer`, `clean-code`, and `test-driven-development`. Load `solid-design` only when the approved implementation materially changes class/module/service ownership, extension seams, substitution contracts, client interfaces, or policy/detail dependency relationships.

`clean-code` guides local implementation quality; it does not authorize unrelated cleanup or replace behavior tests. `solid-design` may conclude `NOT_APPLICABLE`; do not manufacture abstractions.

```text
implement one approved slice at a time
reuse/extend/compose mapped canonical systems
write tests at the relevant boundary
trace changed paths, imports, dependencies, and behavior to criteria
preserve design, content, route, asset, and repository-convention locks
keep unrelated cleanup and migration outside the submission
```

When implementation needs a material scope, dependency, mapping, or decision change:

```text
stop the affected slice
→ decision-provenance and/or implementation-context-discovery
→ reapprove or route for approval
→ update spec, locks, mapping, evidence plan, and traceability
→ continue only after the relevant gate passes
```

Existing implementation does not retroactively approve expansion.

**Done when:** criteria are implemented with tests and no unapproved change or parallel system is bundled.

## Phase 5 — Verify

**Gate:** technical evidence, implementation-context conformance, applicable rendered acceptance, architecture review, and accepted-risk provenance exist before submission.

Technical and convention evidence may include:

```text
tests and regression tests
type, lint, and build output
contract, migration, runtime, or integration evidence
changed import/path/dependency audit
canonical component/token/icon/state/form/query/data mapping check
local parallel-system inspection
clean-code review and behavior-change risk
solid-design assessment when materially applicable
clean-architecture decision trace when architecture-style or boundary design was material
architecture-review
security evidence when affected
```

For user-facing or generated/exported visual changes, load `design-review` and the applicable domain reviewers.

Evidence boundary:

```text
source/import mapping → static convention alignment only
build/tests           → executed technical checks only
rendered interactive  → affected contexts/states/inputs/runtime/accessibility
rendered static       → final size/crop/fidelity/content/export
specialized domain    → governing reviewer or complete acceptance blocked
backend-only          → design acceptance NOT_APPLICABLE
```

For `CONDITIONAL PASS` or another non-blocking exception, run `decision-provenance` against accepted-risk authority.

**Done when:** technical, convention, architecture, design, and risk evidence is resolved for verified scope.

## Phase 6 — Submit

**Gate:** submission references spec, issue, decision ledger, implementation context, scope, and evidence.

Include:

```text
what changed and why
spec and issue reference
effective scope and exclusions
authoritative decision-record IDs
acceptance-criteria checklist
design/architecture decisions and locks
delivery topology record, release unit, parent, base branch, and PR target
implementation_context_profile and convention locks
reuse/extension/composition/native/dependency decisions
implementation mapping and prohibited parallel systems
implementation diff and technical evidence
clean-code verdict/findings/gaps
solid-design applicability/verdict/findings when applicable
clean-architecture applicability and boundary decision when applicable
architecture-review result
design-review route/verdict/findings/gaps when applicable
accepted risks with authority, owner, mitigation, expiry
confirmation that unrelated/unapproved changes are absent
```

Do not submit as design-complete while rendered evidence is `NOT_VERIFIED`. Do not claim owner approval without an attributable source. Do not claim stack conformance merely because no dependency file changed.

**Done when:** submission is traceable, authority-backed, and evidence-backed.

## Phase 7 — Review

**Gate:** explicit `code-review-workflow` approval and merge authorization before merge.

Pass the complete handoff to code review.

```text
Technical review:
  APPROVED | REQUEST CHANGES | BLOCKED

Merge authorization:
  AUTHORIZED | NOT_AUTHORIZED | ROUTE_FOR_APPROVAL
```

```text
APPROVED + AUTHORIZED
  → eligible to merge under product policy

APPROVED + ROUTE_FOR_APPROVAL
  → technically ready, but do not merge

REQUEST CHANGES / BLOCKED / NOT_AUTHORIZED
  → return to implementation, verification, context discovery, or authority resolution
```

Feature-level `NEEDS WORK`, `CRITICAL`, `LIMITED REVIEW`, `ROUTE ELSEWHERE`, `NOT_VERIFIED`, provenance blocker, delivery-topology mismatch, implementation-context blocker, or architecture failure cannot be downgraded to a non-blocking merge flag.

## Quick reference

| Phase | Primary gate | Done when |
|---|---|---|
| Plan | Spec + scope provenance | Scope, criteria, issue, authorities, affected domains explicit |
| Delivery topology | Release unit + hierarchy + PR target | Parent, dependencies, base branch, target, and exception evidence explicit |
| Architecture/design | Decision authority | Boundaries, contexts, states, locks, criteria explicit |
| Implementation context | Repository evidence + mapping | Canonicality, locks, selected adapters, dependency authority explicit |
| Implement | Traceability | Criteria implemented with tests and no silent drift |
| Verify | Evidence + independent reviews | Technical, convention, architecture, design, risk evidence resolved |
| Submit | Complete handoff | Submission is traceable and reviewable |
| Review | Technical + merge authority | Explicit authorization issued |

## Common pitfalls

| Anti-pattern | Correct behavior |
|---|---|
| Agent-generated issue means scope approved | Verify attributable authority |
| Default branch becomes the PR target | Consume the approved delivery topology |
| Green child CI means the epic is complete | Run integrated epic acceptance |
| Design says Select, so any Select library is allowed | Map the capability through implementation context |
| Installed package means canonical | Inspect usage, ownership, conventions, and decisions |
| Fit shared component rebuilt locally | Report convention drift and reuse/extend/compose |
| New icon/component library added for convenience | Require capability gap and authority |
| Native HTML is always forbidden | Evaluate semantic sufficiency and repository precedent |
| Wireframe or mapping reviewed, therefore UI passed | Verify implementation later |
| CI green, therefore feature complete | Collect code quality, object-design when applicable, architecture, runtime, design, and risk evidence |
| Apply SOLID or Clean Architecture to every change | Classify applicability and select the smallest justified design |
| Lint and formatting pass, therefore code quality PASS | Run clean-code evidence review without arbitrary metrics |
| No package change means no stack drift | Inspect local parallel systems and imports |
| Technical approval means merge now | Wait for merge authorization |
| Scope or dependency grows during implementation | Stop, re-map, verify provenance, and reapprove |
