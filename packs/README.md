# Skill Pack Manifests

Machine-readable skill installation bundles live under `packs/<pack-id>/pack.yaml`.

A pack manifest is the canonical source for:

```text
- manifest schema and pack version
- entrypoint skills
- ordered dependency inventory
- dependency classification and activation conditions
- local or explicitly pinned external dependency source
- installation profiles
- compatibility projection into workflow metadata
- exact public install command binding
- optional dependencies on other packs
```

Each workflow bound to a pack declares both the manifest path and exact pack version. This prevents a workflow from silently consuming an incompatible manifest revision.

## Dependency classifications

```text
required         universal lifecycle capability required for normal execution
conditional      required only under a declared execution condition
port             stable concern-level routing capability
adapter          narrow specialist attached to a declared port
domain-reviewer  acceptance capability selected by design or task domain
optional         useful outside the direct execution contract
```

Do not classify a capability as `required` merely because the complete installation profile includes it. Repository operations, brand constraints, audit normalization, correction loops, domain review, and reusable learning are conditional unless the workflow contract makes them universal.

## Validation

```bash
python scripts/validate-skill-packs.py
python -m unittest tests/test_validate_skill_packs.py
```

The validator checks schema support, pack and repository identifiers, local skill existence, explicit external repository/ref pins, duplicate and invalid entries, activation conditions, port ownership, domain reviewer declarations, pack dependency cycles, exact workflow manifest/version binding, exact ordered compatibility metadata, profile resolution, and full documentation-command drift.

The upstream `skills` CLI does not currently resolve transitive dependencies from `SKILL.md`. Pack manifests provide a repository-owned distribution contract while preserving Agent Skills-compatible skill folders.
