# Fix Guide — What to Keep, What to Trim, How to Split

## What to Trim (derivable content)

Remove — agent can derive these without being told:
```
❌ Directory listings ("repo structure is: src/, tests/, ...")
❌ Dependency trees that change frequently  
❌ Obvious language facts ("Python uses indentation")
❌ Duplicate sections restating the same rule
❌ Changelog / version history in skill body
❌ Long explanations of why a rule exists (keep the rule, trim the essay)
```

Keep — non-derivable, session-earned knowledge:
```
✓ Pitfalls — would cost time to re-discover
✓ Concrete examples — specific values (not abstract rules)
✓ Decision rules — when to use X vs Y
✓ Copy-pasteable templates
✓ Gate criteria — specific, verifiable
✓ Known violations — "common violation: X causes Y → fix: Z"
```

---

## How to Move Critical Rules to Top + Bottom

```
<!-- Within first 20 lines -->
HARD RULES:
  1. [most important rule — the one most often violated]
  2. [second most important]
  3. [third — max 5 rules here]

[skill body — phases, templates, gates]

<!-- Within last 10 lines -->
REMINDER:
  1. [restate rule 1]
  2. [restate rule 2]
```

Why: LLM attention is U-shaped (Liu et al. 2023). Middle content is least recalled.
Rule: anything that causes critical failure if missed = top + bottom.

---

## How to Split a Monolith

### Decision: split vs trim

```
> 200L AND content separable by phase/topic  → SPLIT
> 200L AND content all about one thing        → TRIM only
≤ 200L but rules buried in middle             → move rules top/bottom only
```

### Split structure

```
skills/<name>/SKILL.md              ← router, ≤ 150L
skills/<name>/references/<topic>.md ← sub-file, ≤ 200L each
```

Router must contain:
- Hard rules (top, first 20L)
- When to use + do NOT use for
- Parameters
- Phase/topic overview with load instructions: `skill_view(file_path='references/<topic>.md')`
- Hard rules reminder (bottom, last 10L)

Each reference sub-file:
- One topic/phase only
- Critical rule reminder at top (2–3 lines)
- Self-contained — readable without router context
- ≤ 200L

### Real example (redesign-workflow)
```
Before: 1271L monolith
After:
  SKILL.md                     168L  router
  references/phase-genre-macro 176L  Phase 0.5+0.6+0.75
  references/phase-produce     155L  Phase 4 templates
  references/phase-review-gates 153L 35+ gates
  references/phase-fix-loop    110L  Phase 6
  references/phase-deliver      68L  Phase 7 + pitfalls
```

---

## How to Resolve Contradictions

```
1. Find conflicting rules (A says X, B says not-X)
2. Determine correct one:
   - Check session history (which rule led to correct output?)
   - Check external evidence (WCAG, Anthropic docs, etc.)
   - Ask user if ambiguous
3. Patch incorrect skill
4. Add pitfall note in correct skill:
   "Note: [skill B] previously said [Y] — this overrides because [reason]"
```

---

## How to Add Missing Delegation

If skill re-implements behavior ux-patterns-for-developers covers:
```
Replace:
  [hand-rolled 50-line behavior spec]

With:
  Load from ux-patterns-for-developers:
  npx skills add https://github.com/thedaviddias/ux-patterns-for-developers --skill <name> --yes --global
  skill_view(name='<pattern-name>') → extract behavior spec

  Internal skill keeps only:
    - CSS tokens / visual template (brand-specific)
    - Overrides where external spec is too generic
```
