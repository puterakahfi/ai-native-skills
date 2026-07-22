# Contract Coverage And Compatibility Registry — Acceptance Review

Status: candidate acceptance evidence for `ai-native-skills#26`

Pull request: `#64`

Canonical policies:

```text
docs/contract-coverage.md
compat/README.md
```

Generated evidence:

```text
docs/contract-coverage-discovery.yaml
docs/unowned-contract-candidates.yaml
docs/compatibility-registry-migration.yaml
```

## Objective review

Issue `#26` requires every executable artifact to have an authoritative contract reference or an explicit reviewed exemption, while compatibility metadata must describe real implementations rather than stale or circular claims.

Candidate result:

```text
deterministic executable inventory: IMPLEMENTED
contract path and version validation: IMPLEMENTED
structured v2 declarations: IMPLEMENTED REPRESENTATIVE BATCH
reviewed exemptions: IMPLEMENTED
exemption expiry enforcement: IMPLEMENTED
compatibility registry repair: IMPLEMENTED BY RETIREMENT
runtime-binding and reusable-skill collapse: REJECTED
unowned executable artifacts: 0
invalid executable artifacts: 0
explicit v2 conformance errors: 0
```

## Repository inventory

Current deterministic coverage:

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

## Reviewed v2 declaration batch

The following adapters have reviewed `adapter.conformance.yaml` declarations and produce `CONFORMANT` structural results:

```text
design-refinement
redesign-workflow
skill-evolution
copywriting
cro
```

### Workflow path repair

Three stale workflow references were migrated from legacy skill paths to canonical workflow paths:

```text
design-refinement
→ contracts/workflows/design-refinement.contract.yaml

redesign-workflow
→ contracts/workflows/redesign-workflow.contract.yaml

skill-evolution
→ contracts/workflows/skill-evolution.contract.yaml
```

`redesign-workflow` contained one known stale reviewed interface snapshot. The executable method already followed the current lifecycle model; only the reviewed interface block was replaced after an exact legacy-snapshot precondition matched.

Eval contract versions were aligned with the executable patch versions while preserving all cases and assertions:

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

Every exemption contains:

```text
artifact identity and type
owner
specific rationale
bounded scope
review date: 2026-10-22
evidence references
revisit triggers
blocking issue for core_gap
prohibited evidence and authority claims
```

An exemption cannot coexist with `adapter.conformance.yaml` or `ai-native-skills.implements`. An overdue review date fails CI.

Core-gap follow-ups:

```text
puterakahfi/ai-native-core#44
→ composition and visual hierarchy semantic conflicts

puterakahfi/ai-native-core#45
→ design audit, image prompt engineering, and skill maintenance contracts
```

An exemption means ownership and migration state are explicit. It does not prove core conformance, behavioral correctness, runtime acceptance, product acceptance, review, approval, or authorization.

## Compatibility registry decision

Six Hermes compatibility records were retired:

```text
diagram-architect
master-design
master-engineer
native-ai-engineer
native-ai-runtime-agent
native-ai-runtime-ops
```

The records claimed nonexistent paths under `adapters/hermes/`, most referenced a retired repository coordinate, and `native-ai-runtime-agent` contained a circular implementation-as-runtime-protocol reference.

They were not rewritten to point at `skills/<id>/SKILL.md` because:

```text
reusable skill methodology
≠ concrete runtime adapter
≠ installed runtime binding
```

The executable skills remain active. A future binding requires a real adapter implementation, an accepted core port or contract reference, framework/product ownership, structural evidence, and separate runtime/product evidence.

The empty active compatibility registry is therefore an intentional valid state.

## Permanent validation

### Contract Coverage

The permanent workflow validates:

```text
all executable classifications
core contract paths and version pins
inventory freshness
exemption schema and artifact identity
classification, scope, blocking issue, and review date
no declaration/exemption collision
retired compatibility records remain absent
no invalid or duplicate compatibility records
no temporary source tooling or tracked bytecode
core v2 migration-mode reports have zero explicit errors
```

### Skill And Gate Contracts

The existing workflow was migrated to core conformance v2 and validates:

```text
repository eval contracts
canonical design gate registry
current core path and version resolution
all v2 declarations are CONFORMANT
strict legacy adapters are contradiction-free
legacy NOT_CHECKABLE is allowed only for a missing declaration
migration diagnostics remain INFO-only
canonical core eval runner
wrapper integration
per-case behavioral smoke
```

### Other repository gates

```text
Skill Pack Contracts
Validate capability inventory
```

Both remain required and passed on the synchronized candidate implementation head.

## Candidate validation evidence

Synchronized implementation head:

```text
236763310a3756ea85363a8c467edbc435b8d0d6
```

Permanent workflow results:

```text
Contract Coverage
run 29911023450 — PASS

Skill And Gate Contracts
run 29911023447 — PASS

Skill Pack Contracts
run 29911023477 — PASS

Validate capability inventory
run 29911023565 — PASS
```

Exact final review-head evidence is recorded in PR `#64` after this acceptance artifact is included and all four permanent workflows pass again.

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
| Compatibility paths point only to real active implementations | PASS — stale records retired; no active placeholders |
| Circular compatibility references are absent | PASS |
| Duplicate compatibility IDs are absent | PASS |
| V2 declarations are structurally conformant | PASS |
| Legacy migration state does not produce false conformance | PASS |
| Eval and routing behavior remains green | PASS |
| Skill pack and capability inventory remain green | PASS |
| Temporary migration tooling is absent | PASS |
| Runtime and product evidence remain separate | PASS |

## Candidate verdict

```text
contract coverage objective: PASS
compatibility registry objective: PASS
migration safety: PASS
behavioral/eval regression: PASS
repository governance: PASS
ready for owner review: PENDING FINAL-HEAD CI
ready for merge: NO — owner approval required
```
