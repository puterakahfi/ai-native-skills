# Canonical Design Gate Registry

`gate-registry.yaml` is the machine-readable source of truth for design gate identity. This document explains how to use and extend it.

## Registry ownership

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

Full review questions, evidence interpretation, examples, and correction knowledge remain in the governing owner:

```text
built-in owner filename
  resolves inside skills/design-review/references/

external owner repo-relative path
  resolves to another skill, for example:
  skills/brand-identity-review/references/identity-gates.md
```

This keeps stable IDs in the facade registry without moving specialist knowledge into `design-review`.

## Runtime use

Consult the registry when:

- resolving `focus` or previous gate IDs;
- normalizing built-in or external reviewer findings;
- mapping aliases or deprecated IDs;
- validating reports and handoffs;
- authoring evals that name design gates;
- adding a domain reviewer or gate family.

Do not load the complete registry for every review. Resolve selected IDs on demand.

## Identity rules

```text
1. Every selected or reported design gate ID is registered.
2. Every active gate has exactly one canonical owner.
3. The owner reference contains the full definition.
4. Callers do not redefine a gate or invent local meanings.
5. Similar wording does not create an alias.
6. Deprecated IDs require an explicit migration.
7. A renamed gate keeps its ID only when meaning and owner remain compatible.
8. A materially different gate receives a new ID.
9. External owner paths are repository-relative and cannot escape the repo.
```

## Namespace rules

A namespace is an uppercase prefix followed by a positive integer.

```text
G1
I4
RI1
SV11
PR3
BI2
```

Current external adapter registration:

```yaml
namespaces:
  BI:
    purpose: brand-identity-system-quality

gate_groups:
  brand-identity:
    defaults:
      owner: skills/brand-identity-review/references/identity-gates.md
      design_domain: brand-identity
      status: active
      applicability: brand-identity
```

`BI1–BI16` are owned by `brand-identity-review`; the facade stores their stable identity and routing metadata only.

Do not reserve a namespace merely because it might be useful later. Register it together with a real domain reviewer, owner definitions, and regression coverage.

## Status model

```text
active
  may be selected, scored, and reported

deprecated
  accepted through the migration map; reports use active replacement

reserved
  protected identity; must not be scored
```

## Migration behavior

`gate-migrations.yaml` is authoritative.

```text
active ID
→ use directly

alias
→ normalize to active ID
→ preserve alias only in provenance

deprecated ID
→ load declared replacement(s)
→ state migration in review context

unknown ID
→ reject; never guess
```

Empty alias and deprecated maps are valid. They are safer than invented migrations.

## Eval contract usage

When a trigger or assertion names a design gate, declare it:

```yaml
- id: identity-variant-drift
  trigger: "BI11 failed because inverse geometry changed."
  design_gate_ids: [BI11]
  quality_gates_tested:
    - facade_verdict_controls_workflow_state
```

`design_gate_ids` identifies canonical design gates. `quality_gates_tested` describes behavioral skill/workflow contract gates.

## Adding an external domain reviewer

```text
1. Create the reviewer skill and its owner reference.
2. Define the domain, required evidence, and hard-gate boundary.
3. Check that no active gate already owns the same meaning.
4. Register a unique namespace.
5. Add owner path, domain, applicability, weights, and hard-gate metadata.
6. Add migrations only for real previous IDs.
7. Add eval coverage with design_gate_ids.
8. Update router/role composition and install packs.
9. Run registry and eval validators.
10. Bump registry version for identity/schema changes.
```

A wording clarification in an owner reference does not require a registry bump when identity, applicability, ownership, and hard-gate policy remain unchanged.