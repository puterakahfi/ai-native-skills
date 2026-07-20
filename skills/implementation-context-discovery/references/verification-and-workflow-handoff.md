# Verification and Workflow Handoff

Load this reference after convention locks and implementation mapping exist.

Implementation-context discovery is a pre-code decision gate. It does not replace technical, runtime, visual, accessibility, security, performance, or architecture acceptance.

## Evidence boundaries

```text
repository source and configuration
  can prove declared dependencies, import paths, component source,
  token use, aliases, wrappers, and static convention alignment

build/type/lint/test output
  can prove the executed technical checks represented by those tools

rendered evidence
  can prove visual output in the captured context

runtime interaction evidence
  can prove state, input, focus, loading, error, restoration, and integration behavior

accessibility testing
  can prove only the inspected automated/manual/assistive-technology paths

architecture review
  can issue independent compliance acceptance against the engineering contract
```

Do not upgrade one evidence class into another.

## Pre-implementation gate

Before production, require:

```yaml
preimplementation_gate:
  repository_evidence_inventory: <complete | partial | missing>
  canonicality_decisions: <resolved | partial | blocked>
  convention_locks: <declared | missing>
  reuse_extension_decisions: <declared | unresolved>
  new_dependency_decisions: <approved | rejected | routed | not_applicable>
  implementation_mapping: <ready | blocked>
  evidence_gaps: []
  verdict: <READY_FOR_IMPLEMENTATION | BLOCKED | PARTIAL>
```

`READY_FOR_IMPLEMENTATION` means the implementation path is sufficiently mapped. It does not mean the implementation itself passes.

## Post-implementation source audit

```yaml
implementation_context_verification:
  baseline_ref: <ref>
  implemented_ref: <ref>

  mapping_conformance:
    expected_paths_and_imports: []
    observed_paths_and_imports: []
    status: <PASS | FAIL | PARTIAL | NOT_VERIFIED>

  dependency_audit:
    expected_additions: []
    observed_additions: []
    removed_or_replaced: []
    unauthorized_or_duplicate: []
    status: <PASS | FAIL | PARTIAL | NOT_VERIFIED>

  component_and_utility_audit:
    reused: []
    extended: []
    composed: []
    product_specific: []
    semantic_native: []
    duplicated_or_bypassed: []
    status: <PASS | FAIL | PARTIAL | NOT_VERIFIED>

  system_audit:
    styling_and_tokens: <status>
    iconography: <status>
    state_form_query_and_data: <status>
    build_test_story_tooling: <status>

  runtime_and_rendered_evidence:
    runtime: <status>
    visual: <status>
    interaction: <status>
    accessibility: <status>
    performance: <status>
    security: <status>

  architecture_review:
    status: <PASS | FAIL | PASS_WITH_FLAGS | NOT_RUN>
    evidence_ref: <ref>

  residual_findings: []
  verdict: <PASS | FAIL | PARTIAL | NOT_VERIFIED>
```

## Drift detection beyond package changes

An unchanged dependency manifest does not prove convention preservation.

Inspect for:

- local reimplementation of canonical component behavior;
- new unshared tokens, CSS variables, theme rules, or style helpers;
- local icon SVG sets or copied icons that bypass the canonical family;
- new local state, form, query, cache, or validation infrastructure;
- duplicated wrappers and utilities;
- bypassed aliases or composition roots;
- new framework behavior hidden in route or component files;
- custom controls that lose focus, keyboard, disabled, validation, or accessibility contracts.

## Redesign handoff

```text
redesign-workflow PREFLIGHT
  → inspect repository and changed implementation families
  → run implementation-context-discovery for patch/prototype output
  → add convention locks to the redesign preservation contract

DIRECTION / LAYERED PLAN
  → design decides task, hierarchy, structure, interaction, and expression
  → implementation context maps those decisions to product adapters

SPEC CONFIRMATION
  → lock component/library decisions, expected imports/paths,
    prohibited parallel systems, and dependency authority

PRODUCTION
  → master-engineer implements against the mapping

VERIFICATION
  → implementation-context source audit
  → technical/runtime/rendered evidence
  → architecture-review
  → design-review
```

A redesign may alter the component strategy while still preserving the repository's canonical implementation system. A design decision to use a combobox does not authorize a new combobox library when a fit canonical primitive exists.

## Design-refinement handoff

```text
verified finding + refinement lock + change budget
→ implementation-context-discovery for affected files/components/systems
→ decide reuse, bounded extension, composition, or semantic-native patch
→ add expected imports, paths, and forbidden parallel systems to the change budget
→ apply smallest fix
→ source audit + architecture-review + focused design-review
```

Classification routing:

```text
PATTERN_MISMATCH
  design component family is wrong
  → adaptive-component-design

SYSTEM_CONSTRAINT
  canonical implementation system cannot satisfy the accepted design contract
  → implementation-context-discovery CAPABILITY_GAP decision

CONVENTION_DRIFT
  fit canonical implementation was bypassed
  → smallest repository-consistent correction

IMPLEMENTATION_DEFECT
  mapping is correct, code behavior is broken
  → local implementation owner
```

## New-feature handoff

```text
PLAN / DESIGN DECISION
  → classify affected implementation capability families
  → run implementation-context-discovery before implementation
  → record approved dependencies and prohibited parallel systems

IMPLEMENT
  → master-engineer follows mapping and tests

VERIFY
  → source/import/dependency audit
  → architecture-review
  → design-review when user-facing
```

A dependency listed in a generated feature spec is not automatically approved. Decision provenance and product dependency policy still control authority.

## UI component handoff

`ui-components`, `ux-ui-patterns`, and `adaptive-component-design` decide which component capability and behavior fit the task.

`implementation-context-discovery` decides how that capability maps to the repository:

```text
selected capability: dialog
→ reuse canonical dialog primitive if fit
→ extend bounded variant if necessary
→ compose canonical primitives for product behavior
→ do not rebuild focus trapping and dismissal locally
→ do not add a second dialog library without a proven gap
```

Templates and reference snippets are examples. They do not override a product's canonical component, styling, token, or icon system.

## Architecture-review handoff

Pass:

- engineering contract;
- implementation-context profile;
- convention locks;
- approved exceptions and dependency decisions;
- implementation mapping;
- code or PR diff;
- technical and runtime evidence.

Architecture review independently checks:

```text
stack compliance
layer boundaries
unauthorized dependencies
parallel or duplicate systems
architecture style
folder/module placement
test strategy
ADR requirement
```

Discovery cannot self-certify the implementation it guided.

## Status semantics

```text
PASS
  appropriate evidence confirms the applicable mapping and convention locks

FAIL
  evidence shows drift, unauthorized dependency, or broken required mapping

PARTIAL
  some families pass while others fail or remain incomplete

NOT_VERIFIED
  evidence is missing or cannot prove the claim

NOT_APPLICABLE
  the capability family is outside the declared implementation scope
```

## Completion check

Before claiming the capability complete:

- pre-implementation mapping existed before code;
- changed imports and dependencies were audited;
- local duplication and parallel systems were inspected, not inferred away;
- extension and composition preserved canonical contracts;
- native semantic choices were evaluated without dogma;
- new dependency evidence and authority were complete;
- technical, runtime, rendered, accessibility, performance, and security claims used their governing evidence;
- independent architecture review ran or remains honestly `NOT_RUN`/`NOT_VERIFIED`.
