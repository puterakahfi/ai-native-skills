# Executable Contract Coverage

Every executable artifact under `skills/*/SKILL.md` must have one explicit static ownership state.

```text
contract-backed v2
→ reviewed adjacent adapter.conformance.yaml

legacy contract-backed
→ resolvable canonical contract path and compatible version pin
→ migration remains incomplete until a reviewed v2 declaration exists

reviewed exemption
→ no applicable accepted contract or intentionally provider/external boundary
→ owner, scope, rationale, evidence, review date, and revisit trigger are mandatory
```

The generated inventory is:

```text
docs/contract-coverage-discovery.yaml
```

Regenerate it with:

```bash
python3 scripts/inventory-contract-coverage.py \
  --root . \
  --core-root ../ai-native-core \
  --output docs/contract-coverage-discovery.yaml
```

Validate the repository with:

```bash
python3 scripts/validate-contract-coverage.py \
  --root . \
  --core-root ../ai-native-core
```

## Contract-backed artifacts

A path and version pin prove only that the artifact identifies a compatible core agreement. They do not prove complete structural conformance or executable behavior.

A v2 declaration lives next to the executable method:

```text
skills/<id>/SKILL.md
skills/<id>/adapter.conformance.yaml
```

The declaration is reviewed against the actual executable responsibility. It must not be generated from matching IDs or copied contract lists without semantic review.

```text
contract ID match
≠ semantic compatibility
≠ adapter conformance
```

## Reviewed exemptions

A reviewed exemption lives at:

```text
skills/<id>/contract.exemption.yaml
```

It is a temporary ownership record, not a waiver from quality or evidence requirements.

Allowed classifications:

```text
core_gap
→ a reusable capability is blocked by a missing or semantically incompatible core contract

provider_specific
→ the executable intentionally owns a provider or platform-specific surface

third_party_delegation
→ the executable delegates to an externally owned catalog or implementation surface
```

Every exemption must contain:

```text
artifact identity and type
owner
specific rationale
bounded scope
review date
source evidence
revisit triggers
blocking core issue for core_gap
prohibited claims
```

An overdue review date fails CI. An exemption cannot coexist with `adapter.conformance.yaml` or `ai-native-skills.implements`.

The exemption explicitly prohibits claiming:

```text
core contract conformance
behavioral verification
runtime acceptance
product acceptance
approval or authorization
```

Current core-gap tracking:

```text
puterakahfi/ai-native-core#44
→ composition and visual hierarchy semantic conflicts

puterakahfi/ai-native-core#45
→ design audit, image prompt engineering, and skill maintenance contracts
```

## Evidence layers

```text
static contract reference or exemption
≠ structural conformance
≠ behavioral verification
≠ runtime execution evidence
≠ product acceptance
≠ approval or authorization
```

Behavioral evaluation remains owned by executable tests and evaluation tooling. Runtime evidence belongs to `native-ai-fw` or an owning runtime adapter. Product evidence and acceptance belong to product repositories.

## Compatibility registry

Runtime compatibility records are not substitutes for executable contract ownership. See [`../compat/README.md`](../compat/README.md).

## Change rules

When adding or changing an executable artifact:

1. inspect the current core manifest;
2. identify an accepted contract only when semantics and boundaries match;
3. otherwise record a reviewed exemption and create a core issue for reusable gaps;
4. update the generated inventory;
5. run Contract Coverage and relevant behavioral tests;
6. never infer stronger evidence from a green static check.
