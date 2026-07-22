# Runtime Compatibility Registry

The active compatibility registry is intentionally empty.

Six legacy Hermes binding records were retired because they referenced nonexistent implementation paths under:

```text
adapters/hermes/<id>/SKILL.md
```

Most also referenced retired repository coordinates, and one record used its implementation file as a circular replacement for the runtime protocol it claimed to implement.

The retirement decision and evidence are recorded in:

```text
docs/compatibility-registry-migration.yaml
```

Retirement of these records does not retire the reusable executable skills.

```text
SKILL.md presence
≠ runtime adapter implementation
≠ runtime installation
≠ active binding
≠ runtime verification
```

## Ownership boundary

This repository owns:

```text
executable reusable methodology
adjacent static conformance declarations
reviewed contract exemptions
discovery and migration evidence
```

A real runtime binding belongs in:

```text
native-ai-fw
→ orchestration, installed adapter discovery, runtime binding, execution evidence

product registry or product repository
→ product-specific provider, environment, policy, and acceptance configuration
```

Do not recreate a compatibility file merely to associate a skill with a runtime name.

## Requirements for a future active binding

A new compatibility record requires all of the following:

1. a real adapter implementation separate from the reusable `SKILL.md` methodology;
2. an accepted core port or contract referenced by stable ID, canonical path, and compatible version;
3. explicit implementation path and owning repository coordinate;
4. runtime/provider/environment binding owned by the appropriate framework or product registry;
5. no implementation-as-contract or implementation-as-protocol circular reference;
6. structural conformance evidence;
7. separate runtime execution evidence;
8. explicit product acceptance when a product claims the binding is usable.

Use the accepted core schemas where applicable:

```text
adapter_manifest
→ concrete adapter identity and implemented port reference

compatibility_manifest
→ canonical contract path alias migration
```

Neither schema represents product acceptance or runtime success.

## Prohibited shortcuts

```text
skills/<id>/SKILL.md as adapter_path
→ prohibited when no concrete runtime adapter exists

provider permission or installed tool
→ not Native AI Engineering authority

compatible version pin
→ not conformance or runtime evidence

retired legacy record
→ not proof that a future binding exists
```

The empty active registry is therefore a valid, explicit state—not missing data to be filled with placeholders.
