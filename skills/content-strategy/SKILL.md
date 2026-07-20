---
name: content-strategy
description: Content strategy for digital products — microcopy, tone of voice, content hierarchy, onboarding copy, empty states, and error messages. The words are the design. Scored 0–10, minimum 8 to pass.
license: MIT
metadata:
  ai-native-skills.version: 1.0.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/content/content-strategy.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.related_skills: "['ux-psychology', 'readability', 'master-design', 'ux-ui-patterns']"
---

# Content Strategy Skill

## Core contract interface

```yaml
required_inputs:
  - content_inventory
  - audience_profile
allowed_outputs:
  - content_structure
  - tone_guidelines
  - microcopy_variants
  - content_gate_scores
quality_gates:
  - information_sequenced_by_user_mental_model
  - tone_consistent_across_sections
```

Sequence information from the audience's mental model and task progression, not the author's internal organization. The declared tone must remain consistent across sections; contextual variation may change intensity, never identity.

## ⚠️ HARD RULES — Read Before Writing Any Copy

```
RULE 1 — DECLARE TONE CARD FIRST
  Before writing a single word of copy, declare the Tone Card for the product.
  No tone card = no copy. See references/tone-hierarchy.md → Tone Card section.

RULE 2 — SPECIFIC > GENERIC (the 1000-person test)
  Imagine 1000 different people reading this copy. If it applies equally to all of them,
  it is too generic. Rewrite until it is specific enough to fail the test.
  ❌ "We help businesses grow."   (true for 1000 companies)
  ✅ "Sites we build score 90+ on Lighthouse."   (true only for us)

RULE 3 — NO BUZZWORDS
  Banned: seamless, leverage, world-class, cutting-edge, passionate, synergy, innovative.
  If a word appears in every competitor's homepage, delete it.
```

---

## Core Principle

```
Copy is not decoration — it is interface.
A confused user is not stupid. The copy failed.

Three questions before writing any copy:
  1. Who is reading this?
  2. What do they need to know right now?
  3. What should they do next?

If the copy doesn't answer all three — rewrite it.
```

---

## Sections Overview

### 1. Tone of Voice System + Content Hierarchy
→ Load: `references/tone-hierarchy.md`

Contains:
- Tone Dimensions (formal/casual, personal, serious/playful, technical/plain)
- Tone Card template (declare per product before writing)
- F-Pattern and Z-Pattern reading behavior
- Information Hierarchy Rules (most important first, active voice, specificity)
- Review Gates C1, C3, C4 (Tone Consistency, Hierarchy, Specificity)

When to load: Starting a new content project, writing hero copy, auditing tone consistency.

### 2. Microcopy Patterns + Onboarding + SEO
→ Load: `references/microcopy.md`

Contains:
- Button Labels (verb + noun rule, destructive actions, CTA clarity)
- Error Messages (what + why + next step structure)
- Empty States (first use, cleared, no results)
- Loading States (timing thresholds and messaging)
- Confirmation Dialogs (title, body, button copy)
- Onboarding Copy (orient → value → one step → celebrate)
- SEO-Aware Content (page title, meta description, H1/H2, alt text)
- Review Gate C2 (Microcopy Quality)

When to load: Writing UI strings, form errors, empty states, onboarding flows, or SEO metadata.

---

## Content Review Gates Summary (Scored 0–10, Min 8)

| Gate | Topic              | Minimum |
|------|--------------------|---------|
| C1   | Tone Consistency   | 8.0     |
| C2   | Microcopy Quality  | 8.0     |
| C3   | Info Hierarchy     | 8.0     |
| C4   | Specificity        | 8.0     |

**OVERALL MINIMUM: 8.0** — Any gate below 8 blocks ship.

---

## ⚠️ HARD RULES — Reminder at End

```
RULE 1 — Tone Card must be declared before any copy is written.
RULE 2 — Every claim must fail the 1000-person test (specific, not generic).
RULE 3 — No buzzwords: seamless, leverage, world-class, cutting-edge.

If any rule is violated, rewrite before scoring.
```
