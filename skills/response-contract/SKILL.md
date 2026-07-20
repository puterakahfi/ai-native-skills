---
name: response-contract
description: Persistent output verbosity standard — eliminates filler, enforces answer-first, keeps code exact. Set once in AGENTS.md, applies to every response forever. Works on both sides of the token equation with prompt-optimizer.
license: MIT
metadata:
  ai-native-skills.version: 1.0.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/context/response-contract.contract.yaml
  ai-native-skills.contract-version: "~0.1"
---

# Response Contract

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/context/response-contract.contract.yaml` · compatible line: `~0.1`

```yaml
required_inputs:
- agent_response
allowed_outputs:
- compliant_response
- violation_report
- token_savings_estimate
quality_gates:
- no_filler_openers
- no_conclusion_fluff
- no_unnecessary_hedges
- code_and_commands_always_exact
- response_length_proportional_to_task_complexity
- no_unsolicited_alternatives
- lead_with_answer_not_preamble
- verbosity_level_must_be_declared_in_agents_md
```

Evaluate the supplied agent_response against the declared response rules. Return either a compliant_response or a violation_report, and estimate token savings only from removals that preserve task completeness.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace runtime, repository, architecture, test, or product evidence.


## The Core Rule

```
prompt-optimizer  → input side   — precise prompt in  → no agent confusion
response-contract → output side  — tight response out → no token waste

Token waste comes from both ends.
```

Agent filler is not politeness. It is noise that costs tokens on every single reply, forever.

---

## Set Once in AGENTS.md

This skill is not invoked per prompt. It lives in `AGENTS.md` as a persistent rule:

```markdown
## Response Contract

- Lead with the answer. No preamble.
- No filler openers: "Sure!", "Great question!", "Happy to help!", "Certainly!"
- No conclusion fluff: "I hope this helps!", "Let me know if you need anything!"
- No unnecessary hedges: avoid "likely", "probably", "in most cases" unless uncertainty is the actual answer
- No unsolicited alternatives: do not offer "Option A / Option B" unless asked
- Code blocks: always exact — never paraphrase, summarize, or omit lines with "..."
- Response length: proportional to task complexity
  - Simple question → one sentence or one code block
  - Bug diagnosis → structured phases, no padding between phases
  - Architecture review → structured sections, no filler transitions
- Verbosity level: [concise|normal|verbose] ← product_defined
```

---

## Verbosity Levels

| Level | Description | Use When |
|---|---|---|
| `concise` | Answer only. No explanation unless asked. | Experienced team, high-velocity sprint |
| `normal` | Answer + brief rationale. No filler. | Default for most engineering work |
| `verbose` | Answer + full explanation + context. | Onboarding, unfamiliar domain, junior team |

Switch anytime:
```
"respond concise for this session"
"verbose mode — explain everything"
```

---

## Filler Patterns — Always Remove

### Openers
```
❌ "Sure! I'd be happy to help you with that."
❌ "Great question! Let me take a look."
❌ "Certainly! Here's what I found."
❌ "Of course! I'll help you resolve this."

✅ [answer directly]
```

### Conclusion fluff
```
❌ "I hope this helps! Let me know if you have any questions."
❌ "Feel free to reach out if you need further clarification."
❌ "Let me know if you'd like me to elaborate on any of these points."

✅ [stop after the answer]
```

### Unnecessary hedges
```
❌ "This is likely caused by..."       → ✅ "Caused by..." (if you know)
❌ "You might want to consider..."     → ✅ "Use..." (if it's the right answer)
❌ "In most cases, this usually..."    → ✅ "This..." (direct)
❌ "It's possible that..."             → ✅ state uncertainty explicitly if real
```

### Unsolicited alternatives
```
❌ "Here are three approaches you could take: Option A... Option B... Option C..."
   (when user asked for one solution)

✅ [give the best solution, explain why, stop]
✅ [if tradeoffs genuinely matter, say: "two options worth weighing: X vs Y — use X if [condition]"]
```

---

## Code Block Rules

Code, commands, and error messages are **never compressed**:

```
❌ "Add the following to your config (I've omitted unchanged lines for brevity)..."
❌ "// ... rest of the class unchanged"
❌ "Similar pattern applies to the other 3 methods"

✅ Complete, runnable, copy-pasteable code
✅ If large: show the changed function only, say "function X only — rest of file unchanged"
✅ Never use "..." to skip code the user needs to run
```

---

## Before / After

### Bug diagnosis
```
❌ Normal:
"The reason your React component is re-rendering is likely because you're creating
a new object reference on each render cycle. When you pass an inline object as a
prop, React's shallow comparison sees it as a different object every time, which
triggers a re-render. I'd recommend using useMemo to memoize the object."
→ 56 tokens

✅ Response contract applied:
"New object ref on each render. Inline prop = new ref = re-render. Wrap in useMemo."
→ 18 tokens. Same fix.
```

### Code review
```
❌ Normal:
"Sure! I'd be happy to review this. I noticed a few things that could be improved.
First, on line 42, you might want to consider validating the input before processing
it, as this could potentially lead to issues if unexpected data is passed in..."

✅ Response contract applied:
"[MAJOR] Line 42 — no input validation before processing. Inject malformed data → crash.
Fix: add guard at entry point."
```

---

## AGENTS.md Template

Copy-paste into your project's `AGENTS.md`:

```markdown
## Response Contract

Lead with answer. No filler openers, no conclusion fluff.
Code blocks: always complete and exact — never omit lines.
Length: proportional to complexity.
Verbosity: normal
No unsolicited alternatives unless tradeoffs genuinely matter.
```

---

## Relationship to Other Skills

```
prompt-optimizer    → eliminates input token waste  (precise prompt → no agent guessing)
response-contract   → eliminates output token waste (tight response → no filler)
context-engineering → defines persistent project rules (where response-contract lives)

Use together:
  prompt-optimizer (per prompt) + response-contract (persistent in AGENTS.md)
  = maximum token efficiency on both ends
```
