---
name: skill-doctor
description: Skill health workflow — audit, triage, fix, and verify skill files. Detects monoliths (> 200L), Lost-in-Middle violations, stale content, duplicate rules, and missing structure. Run periodically or before publishing skills.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: workflow
  ai-native-skills.related_skills: '["skill-eval","redesign-workflow","context-engineering"]'
---

# Skill Doctor

Audit → Triage → Fix → Verify. Produces healthy, agent-compliant skill files.

<!-- CRITICAL RULES — top placement -->
```
HARD RULES:
  1. Read skill fully before modifying
  2. Preserve ALL functional content — trim derivable/redundant only
  3. Critical rules → top (first 20L) AND bottom (last 10L) of every skill
  4. Split only when > 200L AND content separable by phase/topic
  5. Verify line count + structure after every fix
```

## When to Use

- Before publishing to skills.sh / ai-native-skills repo
- When `skill-eval` returns PARTIAL or GHOST — root cause may be skill structure
- After a skill has been patched 3+ times (check for drift/contradiction)
- Periodic maintenance (monthly across all skills)

`skill-doctor` = checks the skill file.  `skill-eval` = checks agent behavior. Both needed.

---

## Parameters

| Param | Required | Description |
|---|---|---|
| `target` | NO | Skill name — omit to audit all skills |
| `mode` | NO | `audit-only` / `triage` / `full` — default: `full` |
| `auto_fix` | NO | `true` = apply fixes; `false` = report only (default) |

---

## Phase 1: AUDIT

```bash
# Line count all skills, flag over-limit
wc -l skills/*/SKILL.md | sort -rn
wc -l skills/*/SKILL.md | awk '$1 > 200 {print "OVER:", $1, $2}'
```

Per-skill checks:
```
□ Line count ≤ 200L
□ Critical rules in first 20L
□ Critical rules repeated in last 10L
□ One topic per file (not multiple unrelated domains)
□ No derivable content (dir listings, dep trees, obvious facts)
□ No internal contradictions
□ No stale examples (paths/files that no longer exist)
```

Cross-skill checks:
```
□ Duplicate rules across skills
□ Contradictions (skill A says X, skill B says not-X)
□ Missing delegation (skill re-implements what ux-patterns covers)
□ Orphan references (skill references non-existent skill)
```

For full fix criteria → `skill_view(name='skill-doctor', file_path='references/fix-guide.md')`

---

## Phase 2: TRIAGE

```
HEALTHY  — ≤ 200L, rules at top+bottom, one topic, no stale content
TRIM     — > 200L but all content necessary; remove derivable only
SPLIT    — > 200L AND content separable by phase/topic
REWRITE  — contradictions or fundamentally wrong structure
DEFER    — over-limit but rarely loaded; flag, don't fix now
```

Triage report:
```
TRIAGE REPORT
══════════════
Healthy:  N — [names]
Trim:     N — [names]
Split:    N — [names]
Rewrite:  N — [names]
Defer:    N — [names]
Over-limit (> 200L): N skills
```

---

## Phase 3: FIX

Priority order:
1. **REWRITE** — contradictions first (most agent confusion)
2. **SPLIT** — monoliths (Lost in Middle)
3. **TRIM** — remove derivable content
4. **Top/Bottom** — move critical rules to correct positions

Split pattern:
```
Before: skills/big-skill/SKILL.md  (800L)
After:
  skills/big-skill/SKILL.md              (~150L router)
  skills/big-skill/references/part-a.md  (~180L, on-demand)
  skills/big-skill/references/part-b.md  (~180L, on-demand)

Router must have: hard rules top + phase overview + load instructions + hard rules bottom
Each ref file must have: critical rule reminder at top, ≤ 200L
```

---

## Phase 4: VERIFY

```bash
wc -l skills/<name>/SKILL.md        # ≤ 200L
head -20 skills/<name>/SKILL.md     # critical rules present?
tail -10 skills/<name>/SKILL.md     # reminder present?
ls skills/<name>/references/         # sub-files exist if referenced
```

---

## Health Scorecard

| Dimension | Pass condition | Score |
|---|---|---|
| Length | ≤ 200L | /10 |
| Top placement | Critical rules in first 20L | /10 |
| Bottom repeat | Critical rules in last 10L | /10 |
| One topic | Single coherent domain | /10 |
| No derivable | No obvious/stale content | /10 |
| Has templates | Copy-pasteable blocks present | /10 |
| Has gates | Specific, verifiable criteria | /10 |
| No contradiction | No conflicting rules internally | /10 |

**Health score: __ / 80.  Pass: ≥ 64 (80%)**

---

## Delivery Report

```
SKILL DOCTOR REPORT
════════════════════
Skills audited: N  |  Fixed: N  |  Healthy: N

Fixed:
  [skill]: [N]L → [N]L router + N refs — [action]

Deferred:
  [skill]: [reason]
════════════════════
```

<!-- CRITICAL RULES — bottom repeat (Lost in Middle fix) -->
```
REMINDER:
  1. Read fully before modifying
  2. Trim derivable only — preserve functional content
  3. Critical rules at top AND bottom
  4. Verify line count after every fix
```
