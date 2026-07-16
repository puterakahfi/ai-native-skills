---
name: user-research
description: User research methodology — interview techniques, usability testing, jobs-to-be-done framework, affinity mapping, and tracing insights to design decisions. For validating assumptions before building.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/product/user-research.contract.yaml
  ai-native-skills.related_skills: '[''product-manager'', ''ux-psychology'', ''information-architecture'', ''content-strategy'']'
---

# User Research Skill

## Core Principle

```
All design decisions are assumptions until validated by real users.

The cost of assumption vs research:
  Assumption cost:  0 hours now, potentially months wasted building wrong thing
  Research cost:    2–5 hours now, confidence that you're building right thing

The minimum viable research question:
  "What is the one thing we most need to learn before building this?"
  Answer that. Nothing else first.
```

---

## Research Methods by Phase

```
DISCOVERY (what problem to solve):
  → User interviews (generative)
  → Diary studies
  → Contextual inquiry (watch users in their environment)

DEFINITION (what to build):
  → Jobs-to-be-done analysis
  → Affinity mapping
  → Card sorting (IA)

VALIDATION (does the design work):
  → Usability testing
  → First-click testing
  → 5-second test (first impression)
  → A/B testing (quantitative)

MEASUREMENT (is it working):
  → Analytics review
  → NPS / CSAT
  → Retention analysis
```

---

## User Interviews

### When to Use

```
Use interviews for: WHY questions
  Why do users abandon checkout?
  Why do they choose competitor X?
  What does success look like for them?

Do NOT use interviews for: WHAT or HOW MANY questions
  What % of users abandon? → analytics
  How many users have this problem? → survey + analytics
```

### Interview Protocol

```
Before the interview:
  □ Define research question (ONE question per interview session)
  □ Recruit participants who match target persona
  □ Prepare discussion guide (not a script — a guide)
  □ 45–60 minute sessions (not shorter, users open up after 20 min)

Discussion guide structure:
  1. Intro (5 min): rapport, consent, explain recording
  2. Context (10 min): tell me about your role / how you do X today
  3. Core questions (25 min): open-ended, follow the user's thread
  4. Concept probe (10 min): if testing a concept, show it now
  5. Wrap (5 min): anything else? who else should we talk to?

Interview rules:
  ✅ Ask "tell me about a time when..." (past behavior = truth)
  ✅ Follow silence — count to 5 before filling the gap
  ✅ "Why?" 3 times minimum on every interesting answer
  ✅ Ask about behavior, not opinion ("what do you do" not "what would you do")
  ❌ Never ask leading questions: "Do you find X frustrating?"
  ❌ Never ask hypothetical: "Would you use a feature that..."
  ❌ Never show your product before exploring the problem space
```

### Analysis: Affinity Mapping

```
After 5+ interviews:
  1. Write every insight on a sticky note (one insight = one note)
  2. Group notes that are about the same theme
  3. Name each group (the theme, not the notes)
  4. Identify patterns: what appears in 3+ interviews?
  5. Rank themes by frequency × severity

Output:
  - Top 3–5 themes with supporting evidence
  - Insights that surprised you (most valuable)
  - Assumptions that were confirmed or invalidated
```

---

## Jobs-to-be-Done (JTBD)

### The Framework

```
Users don't buy products — they hire them to do a job.
The "job" has three dimensions:

FUNCTIONAL: the practical task
  "I need to track my expenses"

EMOTIONAL: how they want to feel
  "I want to feel in control of my finances"

SOCIAL: how they want to be perceived
  "I want to be seen as someone who is financially responsible"

The full job statement:
  "When [situation], I want to [motivation], so I can [outcome]."

Example:
  "When I'm reviewing expenses at month end,
   I want to see where money went without manual categorization,
   so I can make decisions without spending hours on spreadsheets."
```

### JTBD Interview Questions

```
  "Walk me through the last time you [job]."
  "What triggered that? What happened just before?"
  "What were you using before? Why did you switch?"
  "What would make you stop using this entirely?"
  "If this didn't exist, what would you do instead?"

The last question is the most powerful —
it reveals the real alternatives, not just stated competitors.
```

---

## Usability Testing

### When 5 Users Is Enough

```
Nielsen's rule: 5 users reveal 85% of usability problems.
  
Session 1–5:  generative — discover what problems exist
Session 6–10: comparative — test which solution works better
Session 11+:  diminishing returns (save budget for iteration)

Exception: if testing across very different user segments,
run 5 per segment minimum.
```

### Think-Aloud Protocol

```
Instruction to participant:
  "As you use this, please say out loud everything you're thinking.
   There are no wrong answers — we're testing the design, not you.
   If something is confusing, that means we need to fix the design."

Facilitator rules:
  ✅ "What are you thinking right now?"
  ✅ "What did you expect to happen?"
  ✅ Note where they hesitate, hover, backtrack
  ❌ Never say "that's right" or "good job"
  ❌ Never help (unless they're completely stuck and frustrated)
  ❌ Never explain what the UI does ("just try to use it naturally")
```

### Usability Test Tasks

```
Good tasks:
  - Realistic scenario: "Imagine you just got paid. Pay your rent."
  - Outcome-focused: "Find out how much you spent on food last month."
  - Not UI-directed: never say "click the button" or "go to Settings"

Measure per task:
  - Success rate (% who completed)
  - Time on task (seconds)
  - Error count
  - Satisfaction (post-task: "How easy was that? 1–7")
```

---

## Tracing Insights to Decisions

```
Every design decision should trace to a research insight.

Decision traceability format:
  Decision: [what was decided]
  Based on: [research insight — which interview/test, what was observed]
  Alternatives considered: [what else was tried/considered]
  Expected outcome: [what we expect to happen]
  Validation: [how we'll know if it worked]

Example:
  Decision: Remove "Login" from hero
  Based on: 4/5 usability test participants tried "Login" expecting to see work portfolio,
            not an auth form. Confusion in all 4 cases.
  Alternatives: Keep login but move to nav, add explainer text
  Expected outcome: Reduced bounce from hero, clearer path to work section
  Validation: Heatmaps show fewer clicks on removed area, time-to-work-section decreases
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
