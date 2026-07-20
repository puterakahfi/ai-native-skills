# Skill Pack Manifests

Machine-readable skill installation bundles live under `packs/<pack-id>/pack.yaml`.

A pack manifest is the canonical source for:

```text
- entrypoint skills
- ordered dependency inventory
- dependency classification and activation conditions
- installation profiles
- compatibility projection into workflow metadata
- public documentation binding
- optional dependencies on other packs
```

## Dependency classifications

```text
required         lifecycle capability required for normal execution
conditional      required only under a declared execution condition
port             stable concern-level routing capability
adapter          narrow specialist attached to a declared port
domain-reviewer  acceptance capability selected by design or task domain
optional         useful outside the direct execution contract
```

## Validation

```bash
python scripts/validate-skill-packs.py
python -m unittest tests/test_validate_skill_packs.py
```

The validator checks local skill existence, duplicate and invalid entries, conditional declarations, port ownership, domain reviewer declarations, pack dependency cycles, workflow metadata compatibility, profile resolution, and documentation drift.

The upstream `skills` CLI does not currently resolve transitive dependencies from `SKILL.md`. Pack manifests provide a repository-owned distribution contract while preserving Agent Skills-compatible skill folders.
