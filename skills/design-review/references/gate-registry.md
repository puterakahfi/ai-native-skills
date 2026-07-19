# Canonical Design Gate Registry

`gate-registry.yaml` is the machine-readable source of truth for design gate identity. This document explains how to use and extend it.

## What the registry owns

The registry owns only stable identity and routing metadata:

```text
gate id
canonical name and title
namespace
one governing owner reference
design domain
status
applicability group
default weight
contextual hard-gate policy
migration relationship
```

The registry does **not** own the full review question, evidence interpretation, examples, or correction knowledge. Those stay in the governing owner:

```text
universal-gates.md
interactive-surface-gates.md
static-visual-gates.md
or a declared external domain reviewer
```

This prevents `design-review` from becoming a god skill while keeping gate IDs stable across audit, refinement, workflows, reports, and evals.

## Runtime use

Consult the registry when:

- resolving `focus` or previous gate IDs;
- normalizing findings from built-in or external reviewers;
- mapping aliases or deprecated IDs;
- validating a report or handoff;
- authoring an eval that names a design gate;
- adding a domain reviewer or new gate family.

Do not load the full registry merely to review an unrelated artifact. The facade may resolve selected IDs on demand.

## Identity rules

```text
1. Every selected or reported design gate ID must be registered.
2. Every active gate has exactly one canonical owner.
3. The owner reference contains the full gate definition.
4. Callers must not redefine a gate or invent a local meaning for its ID.
5. Similar wording does not create an alias.
6. Deprecated IDs require an explicit migration entry.
7. A renamed gate keeps its ID only when its meaning and owner remain materially compatible.
8. A materially different gate receives a new ID.
```

## Namespace rules

A namespace is an uppercase prefix followed by a positive integer.

```text
G1
I4
RI1
SV11
PR3
```

Current namespaces are declared in `gate-registry.yaml`. External domain reviewers must register a unique namespace before adding gates.

Example future adapter:

```yaml
namespaces:
  BI:
    purpose: brand-identity

gate_groups:
  brand-identity:
    defaults:
      owner: skills/brand-identity-review/references/identity-gates.md
      design_domain: brand-identity
      status: active
      applicability: brand-identity
    gates:
      BI1:
        canonical_name: concept-symbol-fit
        title: Concept/Symbol Fit
```

Do not reserve `BI` or any other prefix merely because it might be useful later. Add the namespace together with the real domain reviewer and gates.

## Status model

```text
active
  may be selected, scored, and reported

deprecated
  accepted only through the migration map; reports use the active replacement

reserved
  namespace or identity is protected but must not be scored
```

## Migration behavior

`gate-migrations.yaml` is authoritative for aliases and deprecations.

```text
incoming active ID
→ use directly

incoming alias
→ normalize to canonical active ID
→ retain alias in provenance only

incoming deprecated ID
→ load declared replacement(s)
→ state the migration in the review context

unknown ID
→ reject; do not guess
```

The registry baseline intentionally preserves existing active IDs. Empty alias and deprecated maps are valid and safer than invented mappings.

## Eval contract usage

When an eval trigger or assertion names a design gate, declare it explicitly:

```yaml
- id: tabs-overflow
  trigger: "Finding I4 failed on tablet."
  design_gate_ids: [I4]
  quality_gates_tested:
    - facade_verdict_controls_workflow_state
```

`quality_gates_tested` describes behavioral contract gates. `design_gate_ids` identifies canonical design-review gates. They are different namespaces and must not be mixed.

## Change procedure

```text
1. Identify the governing domain reviewer and owner reference.
2. Check that no active gate already owns the same meaning.
3. Register or reuse a namespace.
4. Add the full gate definition to the owner reference.
5. Add the identity metadata to gate-registry.yaml.
6. Add alias/deprecation migration only when replacing a real prior ID.
7. Add or update eval coverage with design_gate_ids.
8. Run the registry and eval validators.
9. Bump registry version for identity/schema changes.
```

A wording clarification in an owner reference does not require a registry-version bump when identity, applicability, ownership, and hard-gate policy remain unchanged.
