---
name: skill-eval
description: Skill application verifier — evaluates per-case agent outputs against regression contracts and classifies behavior as APPLIED, PARTIAL, GHOST, or INCOMPLETE. Separates contract validation from real behavioral evaluation.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/quality/skill-eval.contract.yaml
  ai-native-skills.contract-version: "~0.1"
---

# Skill Eval

`skill loaded` does not mean `skill applied`.

```text
APPLIED
  every required behavior appears and no forbidden behavior appears

PARTIAL
  skill-specific behavior is present, but assertions or ordering rules fail

GHOST
  forbidden/generic behavior appears, indicating the skill was ignored or overridden

INCOMPLETE
  the required per-case output was not supplied
```

Use after skill changes, routing changes, model upgrades, prompt changes, AGENTS/context changes, or a verified regression.

## Two Evaluation Layers

### Contract validation

Checks that test files are structurally executable:

```text
skill exists
filename matches skill name
test version matches skill version
case IDs are unique
triggers are non-empty
assertions are well formed
positive and negative rules do not directly contradict
canonical runner accepts the schema
```

Contract validation does not prove an agent applied the skill.

### Behavioral evaluation

For each case:

```text
load the target skill
send the exact trigger without hints
capture the complete agent output
save one output file for that case
run the canonical evaluator
```

Behavioral evaluation requires real outputs. Synthetic CI smoke outputs only prove runner compatibility.

## Contract Format

Store cases at:

```text
contracts/tests/<skill-name>.test.yaml
```

```yaml
skill_test:
  skill: role-switcher
  version: "1.2.0"
  description: Verify bounded role composition.

  cases:
    - id: mobile-tabs-composition
      description: Cross-device acceptance needs owner, specialist, and reviewer.
      trigger: "Tentukan apakah tabs ini cocok untuk mobile dan tablet lalu review implementasinya."
      must_contain:
        - "master-design"
        - "adaptive-component-design"
        - "design-review"
      must_contain_one_of:
        - "BUILT_IN"
        - "built-in interactive"
      must_not_contain:
        - "all skills"
      sequence_required:
        - pattern: "Owner"
          must_come_before: "Specialist|Reviewer"
      quality_gates_tested:
        - one_owner
        - reviewer_facade_present
```

Rules:

- The trigger is natural and contains no instruction to apply the skill.
- Assertions are specific enough to distinguish skill behavior from generic prose.
- Each case represents one coherent behavior or gate cluster.
- `must_not_contain` targets meaningful regressions, not common words.
- Test version matches `metadata["ai-native-skills.version"]` in the governing `SKILL.md`.

## Output Layout

Recommended per-case layout:

```text
eval-outputs/
├── design-review/
│   ├── screenshot-dashboard-runtime-not-verified.txt
│   └── logo-without-domain-reviewer-is-limited.txt
└── workflow-router/
    ├── audit-only-routes-to-design-audit.txt
    └── known-tabs-failure-routes-to-refinement.txt
```

Do not evaluate several different triggers against one shared output. Each case requires its own generated response.

## Running Contract Validation

Validate repository rules and create deterministic compatibility fixtures:

```bash
python scripts/validate-eval-contracts.py

python scripts/validate-eval-contracts.py \
  --write-smoke-outputs .tmp/eval-smoke-outputs
```

Validate contracts through the canonical `ai-native-core` runner:

```bash
AI_NATIVE_CORE_DIR=../ai-native-core \
  bash scripts/run-eval.sh --all --validate-tests
```

The GitHub workflow `.github/workflows/skill-eval.yml` performs these checks automatically.

## Running Behavioral Evals

One skill with per-case outputs:

```bash
AI_NATIVE_CORE_DIR=../ai-native-core \
  bash scripts/run-eval.sh \
    --skill design-review \
    --output-dir eval-outputs \
    --report-json eval-results/design-review.json
```

One specific case:

```bash
AI_NATIVE_CORE_DIR=../ai-native-core \
  bash scripts/run-eval.sh \
    --skill design-review \
    --case screenshot-dashboard-runtime-not-verified \
    --output-file eval-outputs/design-review/screenshot-dashboard-runtime-not-verified.txt
```

All skills:

```bash
AI_NATIVE_CORE_DIR=../ai-native-core \
  bash scripts/run-eval.sh \
    --all \
    --output-dir eval-outputs \
    --report-json eval-results/all.json
```

The wrapper resolves the runner from:

```text
AI_NATIVE_CORE_DIR
.ai-native-skills/.deps/ai-native-core
../ai-native-core
```

## Classification Rules

```text
APPLIED
  all must_contain assertions pass
  at least one must_contain_one_of option passes when declared
  no must_not_contain assertion is found
  all sequence rules pass

PARTIAL
  one or more required assertions or sequence rules fail
  and no forbidden behavior is detected

GHOST
  a forbidden pattern is detected

INCOMPLETE
  a per-case output file is missing
```

A non-APPLIED result exits non-zero.

## Report Requirements

A useful report includes:

```text
skill and case ID
exact trigger provenance
model/runtime/context version
classification
failed assertions
raw output location
report timestamp
```

Do not patch a skill from a failed eval until the failure is classified as:

```text
skill instruction gap
routing/composition gap
context conflict
model behavior drift
test contract defect
local product override
```

## Anti-Patterns

| Anti-pattern | Why it fails |
|---|---|
| Send a hint such as “use role-switcher” | Tests compliance with the hint, not natural activation |
| Reuse one output for unrelated cases | Different triggers require different evidence |
| Treat contract smoke as behavioral proof | Synthetic text never proves model behavior |
| Use vague required words such as “good” | Generic outputs pass accidentally |
| Use broad forbidden words such as “the” | Valid outputs fail accidentally |
| Ignore missing outputs | Evaluation coverage is overstated |
| Patch the skill before classifying the failure | Test, routing, or context defects get copied into skill knowledge |
| Never rerun after model/context changes | Drift remains invisible |

> **Hard rule:** Send each case trigger verbatim without skill names, hints, or extra steering context.