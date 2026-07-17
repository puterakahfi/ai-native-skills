# Phase 6 — FIX + AUTONOMOUS LOOP

## Phase 6: FIX (Skill-First Mandatory)

When any gate scores < 8.0, run IN ORDER. Skipping Step A = not allowed.

```
Step A — Root cause classification (mandatory):
  For each failing gate:
    1. Which skill encodes the rule for this gate?
    2. Is the rule present in that skill? (yes/no)
    3. No → skill is root cause → patch skill FIRST
    4. Yes → was the rule followed in output? (yes/no)
    5. No → output violated existing rule → patch skill (add violation/pitfall note)
    Document: SKILL: [name] | RULE: [quoted] | GAP: [missing]

Step B — Patch the skill:
  - Open relevant skill file
  - Add/strengthen rule, example, or pitfall — be specific:
    NOT: "use proper spacing"
    YES: "section-label padding = var(--sp-6) — never 0 when adjacent to cards"
  - Commit skill patch BEFORE producing new output

Step C — Reproduce from patched skill:
  - Re-run Phase 4 PRODUCE with patched skill loaded
  - Do NOT patch HTML directly — reproduce from skill
  - This verifies the skill fix actually works

Step D — Re-score:
  - Re-run Phase 5 REVIEW on new output
  - Compare gate scores iteration-to-iteration
  - If previously passing gate now fails → skill patch introduced regression → fix
```

**Gate fix quick reference:**

| Gate Failure | Specific Fix |
|---|---|
| G2 Typographic Scale | Replace raw font-size with scale vars; check H1/body ratio |
| G3 Color Semantic | Rename vars; verify each has exactly one role |
| G4 Figure/Ground | Add dot-grid or gradient to body background |
| G5 Whitespace | Differentiate section padding by visual weight |
| G8 First Impression | Rewrite H1 as stance — 50ms test |
| G14 Touch Targets | Add min-height:44px + display:flex + align-items:center |
| G16 Semantic | Add sr-only H2, fix heading hierarchy, add skip link |
| G21 Reduced Motion | Add @media(prefers-reduced-motion:reduce) to ALL animations |
| R1 Type | Add display face (Fraunces/Playfair) vs body face (Inter) |
| C1 Focal Point | Remove min-height:100vh; use padding-top:clamp() |
| C3 Alignment | Remove magic-number px; anchor to grid or sibling edge |

---

## Phase 6: AUTONOMOUS LOOP

```
LOOP STATE:
  iteration:     1
  max:           5 (default, configurable)
  active_layer:  [strategy | UI | UX | voice | interaction | delight | verification]
  skill_patches: []
  score_history: []
  layer_history: []

LOOP BODY:
  0. Declare active layer (one primary, name deferred)
     → Do not skip to delight if lower layer failing

  1. Phase 4: PRODUCE
     → load references/phase-produce.md
     → stamp: macrostructure, genre, iteration N, pre-emit scores

  2. Phase 5: REVIEW
     → load references/phase-review-gates.md
     → score all applicable gates
     → log: score_history.append(avg)

  3. Check exit:
     avg >= 8.0    → EXIT → Phase 7 DELIVER
     iteration >= max → EXIT → Phase 7 DELIVER + gap report

  4. Phase 6: FIX (skill-first mandatory)
     → root cause → patch skill → log skill_patches
     → iteration++
     → goto step 1

LOOP REPORT (emit at exit):
  ════════════════════════════
  Loop complete: N iterations
  Score progression: [8.0 → 8.4 → 9.1]
  Skills patched:
    - [skill]: [rule added]
  Final score: X.X / 10
  Status: ✅ PASS | ⚠️ MAX REACHED

  Residual gaps (if max reached):
    Gate N: [desc] — score — [why not fixed]
  ════════════════════════════

EXTENSION (if max reached, score < 8.0):
  "Loop reached max N. Score: X.X. Residual: [list]. Extend? (Y = 3 more)"
```

**Why skill-first beats output-first:**
```
Output-first (wrong):            Skill-first (correct):
  fix HTML directly                patch skill → reproduce
  same mistake next iter           mistake doesn't recur
  skill never improves             skill accumulates knowledge
  mistakes repeat sessions         mistakes don't repeat sessions
```
