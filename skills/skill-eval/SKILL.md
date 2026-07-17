---
name: skill-eval
description: Skill application verifier — tests whether a skill was actually applied (behavior + gate compliance) or just loaded and ignored. Produces PASS/FAIL per quality gate.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/quality-control/skill-eval.contract.yaml
---

## HARD RULES
- Never test with leading hints ("using the role-switcher skill...") — defeats the test
- must_contain strings must be unique to skill behavior, not generic LLM output
- Re-run after every model upgrade or AGENTS.md change

# Skill Eval

## States

```
Skill loaded ≠ Skill applied

1. Load skill → read → ignore → answer from general knowledge  [GHOST]
2. Load skill → partially follow → gates violated              [PARTIAL]
3. Load skill → fully apply → output matches contract          [APPLIED]
```

## When to Use
- After adding a new skill — verify it actually changes agent behavior
- Regression testing — verify existing skills still work after model/prompt changes
- Debugging agent drift — agent was following a skill, now seems to ignore it
- Quality audit — prove to stakeholders that skills are enforced, not decorative

---
## 3 Levels of Verification

### Level 1: Structural Check
```
skill: role-switcher
expected structure:
  - "Roles active: ..." line at top
  - ## <Lens> sections
  - ## Synthesis section with P1/P2/P3

verdict: PASS if structure present, FAIL if flat generic output
```

### Level 2: Gate Compliance Check
```
skill: systematic-debugging
gate: understand_before_fixing
test: send a bug report
expected: "root cause" appears BEFORE "fix" in output
violation: agent proposes fix in first paragraph → FAIL
```

### Level 3: Generic Response Detection
```
Generic response signals (FAIL):
- "Sure! Here are some suggestions..."
- "Great question! Generally speaking..."
- "I'll help you with that..."
- "There are several approaches..."

Skill-applied signals (PASS):
- Structured output matching skill's output format
- References skill-specific frameworks/checklists
- States active roles / active phase
```

---
## How to Run an Eval

### Step 1: Load test case

```yaml
# from contracts/tests/<skill>.test.yaml
skill: role-switcher
case: design-audit
trigger: "Audit design ini — apa yang kurang?"
must_contain: ["Roles active:", "master-design", "Synthesis"]
must_not_contain: ["Here are some suggestions", "Generally speaking"]
```

### Step 2: Send trigger to agent with skill loaded

```
[Load skill: role-switcher]
[Send trigger verbatim — do not add context or hints]
```

### Step 3: Evaluate output

```
SKILL EVAL RESULT — role-switcher / design-audit
─────────────────────────────────────────────────
Trigger: "Audit design ini — apa yang kurang?"

must_contain:
  [✓] "Roles active:"
  [✓] "master-design"
  [✓] "Synthesis"
  [✗] "ux-psychology"    ← MISSING

must_not_contain:
  [✓] "Here are some suggestions" — not found
  [✓] "Generally speaking" — not found

Gate compliance:
  [✓] intent_must_be_detected_before_role_selection
  [✗] multi_role_output_must_be_structured_by_lens — ux-psychology lens absent

Verdict: PARTIAL — skill loaded but ux-psychology role not activated
```

### Step 4: Classify

| Classification | Signal |
|---|---|
| **APPLIED** | All must_contain met, no must_not_contain violated, gates honored |
| **PARTIAL** | Some must_contain missing OR some gates violated |
| **GHOST** | must_not_contain violated (generic response) OR no skill structure in output |

---
## Writing New Test Cases

```yaml
# contracts/tests/<skill-name>.test.yaml
skill_test:
  skill: <skill-name>
  version: "0.1.0"
  description: <what this tests>

  cases:
    - id: <case-id>
      description: <what this case verifies>
      trigger: "<exact prompt to send — no hints>"
      must_contain:
        - "<string that must appear in output>"
      must_not_contain:
        - "<generic response string that signals skill not applied>"
      must_contain_one_of:        # optional — verdict patterns
        - "APPROVED"
        - "REQUEST CHANGES"
      sequence_required:          # optional — ordering check
        - pattern: "root cause"
          must_come_before: "fix|solution"
      quality_gates_tested:
        - <gate_id from contract>
```

**Rules for good test cases:**
- Trigger must be a **canonical** use case — most natural way to invoke this skill
- `must_contain` strings must be **unique to skill behavior** — not things any LLM would say
- `must_not_contain` must catch **generic LLM responses** — the "skill not applied" signal
- One test case per quality gate where possible

---
## Automated Runner

```bash
./scripts/run-eval.sh role-switcher          # single skill
./scripts/run-eval.sh --all                  # all skills
./scripts/run-eval.sh --all --report eval-results/$(date +%Y%m%d).json
```

---
## Regression Schedule

Run skill evals:
- After any skill update
- After model upgrade/change
- Weekly as a cron health check
- After any AGENTS.md change

If a skill regresses (was APPLIED, now PARTIAL/GHOST) → patch the skill before merging.

---
## Anti-Patterns

| Anti-Pattern | Why It Fails |
|---|---|
| Test with leading context ("using the role-switcher skill...") | Hints the agent, not a real test |
| must_contain: "good" | Too generic — any LLM output contains "good" |
| must_not_contain: "the" | Too broad — will always fail |
| Only test structural output, skip gate compliance | Catches GHOST but misses PARTIAL |
| Never re-run after model change | Model updates can silently break skill behavior |

---
> **HARD RULES reminder:** canonical trigger, no hints → unique must_contain strings → classify APPLIED/PARTIAL/GHOST → re-run after every model/skill change.
