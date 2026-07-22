# Contract Coverage And Compatibility Registry — Acceptance Review

Status: implementation accepted for owner review under `ai-native-skills#26`

Pull request: `#64`

Canonical policy and generated evidence:

```text
docs/contract-coverage.md
compat/README.md
docs/contract-coverage-discovery.yaml
docs/unowned-contract-candidates.yaml
docs/compatibility-registry-migration.yaml
```

## Objective result

```text
deterministic executable inventory: IMPLEMENTED
contract path and version validation: IMPLEMENTED
structured v2 declaration batch: IMPLEMENTED
reviewed exemptions: IMPLEMENTED
exemption expiry enforcement: IMPLEMENTED
compatibility registry repair: IMPLEMENTED BY RETIREMENT
runtime-binding and reusable-skill collapse: REJECTED
unowned executable artifacts: 0
invalid executable artifacts: 0
explicit v2 conformance errors: 0
```

## Final repository inventory

```text
executable artifacts: 101

contract_backed_v2: 5
legacy_contract_backed: 88
reviewed_exemption: 8
unowned: 0
invalid: 0

active compatibility manifests: 0
compatibility manifests with errors: 0
duplicate compatibility IDs: 0
```

Official executable types:

```text
skill: 85
workflow: 10
meta-skill: 6
```

A legacy contract-backed artifact has a resolvable canonical path and compatible version pin. It remains incomplete under conformance v2 until a reviewed adjacent declaration is added.

## Reviewed v2 declarations

The following adapters have adjacent `adapter.conformance.yaml` declarations and produce `CONFORMANT` structural results:

```text
design-refinement
redesign-workflow
skill-evolution
copywriting
cro
```

Three workflow references were moved from retired skill-contract paths to canonical workflow paths:

```text
design-refinement
→ contracts/workflows/design-refinement.contract.yaml

redesign-workflow
→ contracts/workflows/redesign-workflow.contract.yaml

skill-evolution
→ contracts/workflows/skill-evolution.contract.yaml
```

`redesign-workflow` contained one known stale reviewed-interface snapshot. The migration replaced it only after the complete legacy snapshot matched an explicit precondition. The executable methodology was not bulk-rewritten.

Eval contract versions were aligned with executable patch versions while preserving every case and assertion:

```text
design-refinement: 2.2.1
redesign-workflow: 3.6.1
skill-evolution: 1.0.3
```

## Reviewed exemptions

Eight artifacts have explicit, schema-valid, time-bounded exemption records:

```text
core_gap:
- composition
- visual-hierarchy
- design-audit
- prompt-engineer
- skill-doctor

provider_specific:
- chatgpt-app-development
- github-profile

third_party_delegation:
- ux-patterns-for-developers
```

Every exemption includes artifact identity, owner, rationale, bounded scope, source evidence, revisit triggers, prohibited claims, and review date `2026-10-22`.

An exemption cannot coexist with `adapter.conformance.yaml` or `ai-native-skills.implements`. An overdue review date fails CI.

Core-gap follow-ups:

```text
puterakahfi/ai-native-core#44
→ composition and visual hierarchy semantic conflicts

puterakahfi/ai-native-core#45
→ design audit, image prompt engineering, and skill maintenance contracts
```

An exemption records ownership and migration state. It does not prove core conformance, behavioral correctness, runtime acceptance, product acceptance, review, approval, or authorization.

## Compatibility registry decision

Six stale Hermes records were retired:

```text
diagram-architect
master-design
master-engineer
native-ai-engineer
native-ai-runtime-agent
native-ai-runtime-ops
```

They referenced nonexistent `adapters/hermes/` implementation paths. Most also referenced a retired repository coordinate; `native-ai-runtime-agent` contained a circular implementation-as-runtime-protocol reference.

They were not redirected to `skills/<id>/SKILL.md` because:

```text
reusable skill methodology
≠ concrete runtime adapter
≠ installed runtime binding
```

The executable skills remain active. A future runtime binding requires a real adapter implementation, accepted core port or contract reference, framework/product ownership, structural evidence, and separate runtime/product evidence.

The empty active compatibility registry is therefore an intentional valid state.

## Permanent validation

### Contract Coverage

Validates executable classification, core paths and pins, generated inventory freshness, exemption identity/scope/review dates, collisions, retired records, compatibility duplicates, tracked artifacts, and core v2 migration-mode errors.

### Skill And Gate Contracts

Migrated to core conformance v2 and validates eval contracts, gate registry, canonical paths and pins, v2 `CONFORMANT` results, contradiction-free legacy migration, canonical eval runner, wrapper integration, and per-case behavioral smoke.

### Other required gates

```text
Skill Pack Contracts
Validate capability inventory
```

## Validated implementation evidence

Implementation head containing the complete acceptance artifact:

```text
02c214621d0b8c6cb634062a9e9564b279bfec7c
```

Permanent workflows:

```text
Contract Coverage
run 29911216611 — PASS

Skill And Gate Contracts
run 29911216862 — PASS

Skill Pack Contracts
run 29911216593 — PASS

Validate capability inventory
run 29911216890 — PASS
```

Every substantive step completed successfully. Exact final PR-head checks remain the authoritative merge-time evidence.

## Evidence boundary

```text
contract path and version resolve
≠ structural conformance

structural conformance
≠ behavioral verification

behavioral verification
≠ runtime execution evidence

runtime evidence
≠ product acceptance

product acceptance or review
≠ approval or authorization
```

This change does not claim runtime installation, provider availability, product adoption, or authority-bearing approval.

## Acceptance matrix

| Criterion | Result |
|---|---|
| Every executable has contract ownership or reviewed exemption | PASS |
| Contract paths and pins resolve | PASS |
| No invalid or unowned executable remains | PASS |
| Exemptions have owner, rationale, scope, review date, evidence, and revisit path | PASS |
| Core gaps are tracked upstream | PASS |
| Compatibility registry contains no stale active binding | PASS |
| Circular compatibility references are absent | PASS |
| Duplicate compatibility IDs are absent | PASS |
| V2 declarations are structurally conformant | PASS |
| Legacy migration state does not produce false conformance | PASS |
| Eval and routing behavior remains green | PASS |
| Skill pack and capability inventory remain green | PASS |
| Temporary migration tooling is absent | PASS |
| Runtime and product evidence remain separate | PASS |

## Verdict

```text
contract coverage objective: PASS
compatibility registry objective: PASS
migration safety: PASS
behavioral/eval regression: PASS
repository governance: PASS
ready for owner review: YES
ready for merge: NO — owner approval required
```
