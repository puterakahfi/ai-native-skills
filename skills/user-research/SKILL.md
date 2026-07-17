---
name: user-research
description: User research methodology — interview techniques, usability testing, jobs-to-be-done framework, affinity mapping, and tracing insights to design decisions. For validating assumptions before building.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/product/user-research.contract.yaml
  ai-native-skills.related_skills: '["product-manager", "ux-psychology", "information-architecture", "content-strategy"]'
---

# User Research

## Hard Rule

```
All design decisions are assumptions until validated by real users.
The minimum viable research question: "What is the one thing we most need to learn before building this?"
Answer that. Nothing else first.
```

## Research Methods by Phase

```
DISCOVERY (what problem to solve):  User interviews (generative), diary studies, contextual inquiry
DEFINITION (what to build):         JTBD analysis, affinity mapping, card sorting
VALIDATION (does the design work):  Usability testing, first-click testing, 5-second test, A/B testing
MEASUREMENT (is it working):        Analytics review, NPS/CSAT, retention analysis
```

---

## User Interviews

**When:** Use for WHY questions (why abandon checkout, why choose competitor). NOT for what% or how-many → use analytics/surveys.

```
Before the interview:
  □ Define ONE research question per session
  □ Recruit participants matching target persona
  □ 45–60 min sessions (users open up after 20 min)

Discussion guide structure:
  1. Intro (5 min): rapport, consent, recording
  2. Context (10 min): tell me about your role / how you do X today
  3. Core questions (25 min): open-ended, follow the user's thread
  4. Concept probe (10 min): show concept if testing one
  5. Wrap (5 min): anything else? who else should we talk to?

Interview rules:
  ✅ "Tell me about a time when..." (past behavior = truth)
  ✅ Follow silence — count to 5 before filling the gap
  ✅ "Why?" 3 times minimum on every interesting answer
  ✅ Ask about behavior, not opinion ("what do you do" not "what would you do")
  ❌ Never ask leading questions: "Do you find X frustrating?"
  ❌ Never ask hypothetical: "Would you use a feature that..."
  ❌ Never show your product before exploring the problem space
```

### Affinity Mapping (after 5+ interviews)

```
1. Write every insight on a sticky note (one insight = one note)
2. Group notes that are about the same theme
3. Name each group (the theme, not the notes)
4. Identify patterns: what appears in 3+ interviews?
5. Rank themes by frequency × severity

Output: Top 3–5 themes with evidence, surprising insights, confirmed/invalidated assumptions
```

---

## Jobs-to-be-Done (JTBD)

```
Users don't buy products — they hire them to do a job.

FUNCTIONAL: "I need to track my expenses"
EMOTIONAL:  "I want to feel in control of my finances"
SOCIAL:     "I want to be seen as financially responsible"

Full job statement: "When [situation], I want to [motivation], so I can [outcome]."

Example: "When reviewing expenses at month end, I want to see where money went without
          manual categorization, so I can decide without spending hours on spreadsheets."
```

**JTBD Interview Questions:**
```
"Walk me through the last time you [job]."
"What triggered that? What happened just before?"
"What were you using before? Why did you switch?"
"What would make you stop using this entirely?"
"If this didn't exist, what would you do instead?"  ← reveals real alternatives
```

---

## Usability Testing

**Nielsen's rule:** 5 users reveal 85% of usability problems. Sessions 6–10: comparative. Sessions 11+: diminishing returns. Run 5 per segment minimum when testing across different user segments.

```
Think-aloud instruction: "Say out loud everything you're thinking. There are no wrong
answers — we're testing the design, not you."

Facilitator rules:
  ✅ "What are you thinking right now?"
  ✅ "What did you expect to happen?"
  ✅ Note where they hesitate, hover, backtrack
  ❌ Never say "that's right" or "good job"
  ❌ Never help (unless completely stuck and frustrated)
  ❌ Never explain what the UI does

Good tasks:
  - Realistic scenario: "Imagine you just got paid. Pay your rent."
  - Outcome-focused: "Find out how much you spent on food last month."
  - Not UI-directed: never say "click the button" or "go to Settings"

Measure per task: success rate (%), time on task (sec), error count, satisfaction (post-task 1–7)
```

---

## Tracing Insights to Decisions

```
Decision traceability format:
  Decision: [what was decided]
  Based on: [research insight — which interview/test, what was observed]
  Alternatives considered: [what else was tried/considered]
  Expected outcome: [what we expect to happen]
  Validation: [how we'll know if it worked]

Example:
  Decision: Remove "Login" from hero
  Based on: 4/5 usability test participants tried "Login" expecting to see work portfolio
  Alternatives: Keep login but move to nav, add explainer text
  Expected outcome: Reduced bounce from hero, clearer path to work section
  Validation: Heatmaps show fewer clicks, time-to-work-section decreases
```

---

## Research Gates (Scored 0–10, Min 8)

```
Gate R1: Research Question
  □ Research question defined before any design started?
  □ Question is about WHY/HOW (not WHAT/HOW MANY)?
  Score: __ / 10

Gate R2: Evidence Quality
  □ Design decisions trace to observed behavior (not stated preference)?
  □ Insights come from ≥ 3 participants?
  Score: __ / 10

Gate R3: Assumption Tracking
  □ All major assumptions documented?
  □ Assumptions ranked by risk × uncertainty?
  □ Plan to validate highest-risk assumptions?
  Score: __ / 10

Gate R4: Decision Traceability
  □ Each major design decision cites a research insight?
  □ Decisions that couldn't be validated are flagged as assumptions?
  Score: __ / 10

OVERALL: __ / 10   MINIMUM: 8.0
```
