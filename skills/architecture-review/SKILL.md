---
name: architecture-review
description: Engineering contract compliance reviewer — checks code, PRs, and system design against the product engineering contract and discovered implementation context. Catches stack violations, layer-boundary breaks, canonical-system bypass, local parallel systems, unauthorized dependencies, and architecture drift before merge.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/quality/architecture-review.contract.yaml
  ai-native-skills.contract-version: ~0.1
  ai-native-skills.related_skills: '["implementation-context-discovery","master-engineer","code-review-workflow","decision-provenance","security-review"]'
---

# Architecture Review

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/quality/architecture-review.contract.yaml` · compatible line: `~0.1`

```yaml
required_inputs:
- code_or_pr_diff
- engineering_contract_ref
allowed_outputs:
- compliance_verdict
- violation_list
- adr_required_flag
- new_dependency_flag
- architecture_smell_list
- recommendation_list
quality_gates:
- must_load_engineering_contract_before_review
- must_check_stack_compliance
- must_check_layer_boundary_violations
- must_check_unauthorized_dependencies
- must_check_architecture_style_compliance
- must_check_test_strategy_compliance
- must_flag_adr_requirement_when_contract_change_detected
- must_not_approve_generated_code_that_violates_contract
- treats_compiled_as_approved_is_forbidden
```

Compilation and test success are evidence, not architecture approval. Review the code or PR diff against the engineering contract and emit a compliance verdict with violations, ADR and dependency flags, smells, and recommendations.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace runtime, repository, architecture, test, or product evidence.

## Core rule

```text
No agent, PR, or generated code passes review
without being checked against the Engineering Contract.
Compiled ≠ Approved.
Implementation-context discovery ≠ self-approval.
```

## When to use

- before merging any PR;
- after an AI agent generates or changes code;
- when a dependency, framework, component system, icon family, styling system, state/form/query/data tool, or integration changes;
- when folder or module structure changes;
- when a canonical shared abstraction may have been bypassed;
- when a local parallel system may have been introduced without a package-manifest change;
- when an exception or migration slice is requested.

## Prerequisites

Required:

```text
engineering_contract_ref
code_or_pr_diff
```

Load when available:

```text
implementation_context_profile
convention_locks
reuse_extension_decisions
approved_new_dependency_decisions
implementation_mapping
architecture_decision_records
technical_and_runtime_evidence
```

When implementation-context evidence is missing for a material stack or convention decision, report `STACK_CONTEXT_MISSING` or `NOT_VERIFIED`; do not assume the package manifest is the complete contract.

## Review procedure

### 1. Load authority and context

Read the engineering contract before judging the diff. Then compare any `implementation-context-discovery` handoff against the actual repository state.

The pre-implementation handoff is decision evidence, not acceptance. Verify it independently.

### 2. Check stack and canonical-system compliance

Verify:

- backend and frontend frameworks match the contract;
- runtime and platform boundaries remain accepted;
- canonical component, styling, token, icon, state, form, query, table, validation, and data systems are preserved;
- a migration target is used only inside an approved migration slice;
- no unauthorized framework or parallel system is introduced;
- product-specific components compose accepted primitives where applicable;
- native semantic elements are not rejected merely for being native;
- native elements do not bypass a fit canonical abstraction with required behavior or policy.

Violation signals:

```text
CONVENTION_DRIFT
  fit canonical abstraction bypassed without evidence

DEPENDENCY_DRIFT
  unapproved duplicate or parallel dependency/system

STACK_CONTEXT_MISSING
  material decision cannot be checked against discovered repository context
```

### 3. Audit dependencies

For every added, removed, replaced, or newly used dependency:

- is its role approved and bounded?
- does it duplicate an accepted capability?
- was a capability gap proven before selection?
- were extension, composition, and semantic-native alternatives reviewed?
- are bundle/runtime, security, accessibility, maintenance, licensing, interoperability, and migration consequences recorded?
- does the decision require an ADR or product authority?

Flag any package added because it was convenient, familiar, popular, or agent-recommended without evidence.

Also inspect dependency use without manifest changes:

- direct imports of already-installed but noncanonical packages;
- copied libraries or vendored source;
- local icon sets;
- local component, styling, state, form, query, cache, or validation infrastructure;
- parallel tokens or theme systems;
- bypassed shared wrappers and aliases.

### 4. Check architecture style and boundaries

- declared architecture style is followed;
- business logic remains in its owning layer;
- domain code has no framework/infrastructure imports;
- ports and adapters preserve dependency inversion;
- aggregates, value objects, events, repositories, and services follow the applicable contract;
- pattern selection is justified by forces;
- product-specific implementation does not leak into reusable core contracts.

### 5. Check folder and module placement

- files live in the correct owner/module/layer;
- no arbitrary top-level folders or duplicate shared areas appear;
- shared primitives do not absorb product-specific policy;
- product-specific components do not masquerade as universal primitives;
- structural changes have the required ADR or approval.

### 6. Check testing and verification strategy

- changed behavior has tests at the correct boundary;
- skipped tests and deferred coverage are reported;
- source, build, runtime, rendered, accessibility, performance, and security evidence are not conflated;
- the verification depth matches the change and risk.

Source/import alignment can pass while runtime, visual, interaction, or accessibility status remains `NOT_VERIFIED`.

### 7. Determine ADR and authority requirements

Flag an ADR or equivalent approved decision when the change adds or switches:

- a framework or runtime;
- a component, styling, icon, state, form, query, table, validation, or data system;
- a database, ORM, queue, event system, provider, or integration boundary;
- architecture style, security baseline, module ownership, or major folder structure;
- a migration strategy or exception to canonical convention locks.

## Verdict format

```text
ARCHITECTURE REVIEW VERDICT
───────────────────────────
Status: PASS | FAIL | PASS WITH FLAGS | NOT_VERIFIED

Implementation context:
  Profile: <reference | missing>
  Convention locks checked: <list>
  Mapping conformance: <PASS | FAIL | PARTIAL | NOT_VERIFIED>

Violations:
  - [BLOCKING] <description>
  - [WARNING]  <description>

Classifications:
  - STACK_CONTEXT_MISSING | CONVENTION_DRIFT | CAPABILITY_GAP |
    DEPENDENCY_DRIFT | IMPLEMENTATION_DEFECT

ADR required: YES | NO | ROUTE_FOR_APPROVAL
New dependencies flagged: []
Parallel/local systems flagged: []

Recommendation:
  <smallest required correction and evidence>
```

## Auto-fail examples

| Anti-pattern | Why it fails |
|---|---|
| Domain imports infrastructure | Layer-boundary violation |
| Fit canonical Dialog is rebuilt with a local overlay | Convention drift and duplicated behavior |
| Another icon package is added while the canonical family fits | Dependency drift |
| Tailwind/token repository gains a parallel local theme grammar without approval | System drift |
| Existing but deprecated package is used because it is installed | Canonicality failure |
| Dependency added because “the AI suggested it” | No capability-gap or authority evidence |
| PR has no required tests | Test-strategy violation |
| Build passes and is treated as architecture approval | Compiled ≠ Approved |
| Discovery handoff is treated as its own acceptance verdict | Reviewer independence lost |

## Quality bar

- engineering contract loaded first;
- implementation context checked when material;
- installed, canonical, migration-target, legacy, deprecated, experimental, and transitive systems remain distinct;
- package changes and package-free local drift are both audited;
- native semantic choices are evaluated against requirements rather than dogma;
- dependencies have bounded capability-gap and authority evidence;
- layer, module, architecture, and test contracts are checked;
- verdict preserves `FAIL`, `PARTIAL`, and `NOT_VERIFIED` rather than upgrading evidence.
