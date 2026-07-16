---
name: content-strategy
description: Content strategy for digital products — microcopy, tone of voice, content hierarchy, onboarding copy, empty states, and error messages. The words are the design. Scored 0–10, minimum 8 to pass.
version: 1.0.0
author: puterakahfi
license: MIT
type: skill
implements: ai-native-core/contracts/skills/experience-design/content-strategy.contract.yaml
related_skills: [ux-psychology, readability, master-design, ux-ui-patterns]
---

# Content Strategy Skill

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

## Tone of Voice System

Define ONCE per product, apply everywhere.

### Tone Dimensions

```
Dimension 1: Formal ←————→ Casual
  Formal:  "Your request has been submitted."
  Casual:  "You're all set!"
  Pick:    Match the user's context — tax software = formal, fitness app = casual

Dimension 2: Distant ←————→ Personal
  Distant: "Users can configure settings."
  Personal: "You can configure your settings."
  Pick:    Always personal for consumer products. Never "users" talking to users.

Dimension 3: Serious ←————→ Playful
  Serious: "Error: payment failed."
  Playful: "Oops — your card didn't go through."
  Pick:    Serious for financial/medical/legal. Playful for lifestyle/social.

Dimension 4: Technical ←————→ Plain
  Technical: "Authentication token expired."
  Plain:     "You've been signed out. Sign in again to continue."
  Pick:      Always translate technical for end users. Technical for developer tools only.
```

### Tone Card (declare per product)

```yaml
product: pkahfi.com
tone:
  formal_casual:    3/10  # lean casual but not slang
  personal:         true  # always "you", never "users"
  serious_playful:  4/10  # grounded, not jokey
  technical_plain:  2/10  # plain English, jargon only in technical context
voice: "Direct, honest, specific. No buzzwords. No filler."
never_use: ["passionate", "leverage", "synergy", "world-class", "seamless"]
```

---

## Content Hierarchy

### F-Pattern and Z-Pattern Reading

```
Users scan — they don't read.

F-Pattern (text-heavy, dense content):
  Line 1: read fully (most important info here)
  Line 2: read partially (supporting info)
  Lines 3+: scan left edge only (structure, keywords)

  → Put most important content in first 2 lines
  → Use bold, headings to create left-edge anchors

Z-Pattern (sparse content, landing pages):
  Top-left → Top-right → Diagonal → Bottom-left → Bottom-right
  
  → Logo top-left
  → Nav top-right
  → Hero copy diagonal center
  → CTA bottom-right
```

### Information Hierarchy Rules

```
1. Most important first — always
   Never: background context → then the point
   Always: the point → then context if needed

2. One idea per sentence
   Never: "We build scalable, maintainable, and high-performance systems."
   Always: "We build systems meant to last."

3. Active voice
   Never: "The form was submitted successfully."
   Always: "We got your form."

4. Concrete over abstract
   Never: "We deliver exceptional experiences."
   Always: "Sites we build score 90+ on Lighthouse."

5. Specificity over generality
   Never: "Fast loading."
   Always: "Loads in under 1 second."
```

---

## Microcopy Patterns

### Button Labels

```
Rule: verb + noun — never just a noun

❌ "Submit"        → ✅ "Send message"
❌ "Continue"      → ✅ "Save and continue"
❌ "OK"            → ✅ "Got it" / "Done" / "Close"
❌ "Delete"        → ✅ "Delete post" (be specific)
❌ "Yes"           → ✅ "Yes, delete" (confirm the action)

Destructive actions: always show what will be destroyed
  "Delete account" not "Delete"
  "Remove photo" not "Remove"

Primary CTA: what happens when they click?
  ✅ "Start free trial" (outcome clear)
  ✅ "Download report" (outcome clear)
  ❌ "Get started" (vague — started what?)
```

### Error Messages

```
Structure: What happened + Why (if helpful) + What to do

❌ "Error 422"
❌ "Invalid input"
❌ "Something went wrong"

✅ "Email already in use. Sign in instead, or use a different email."
✅ "Password must be at least 8 characters."
✅ "We couldn't process your payment. Check your card details and try again."

Rules:
  - Never blame the user ("You entered an invalid email")
  - Never use technical codes for end users
  - Always give a path forward
  - Write in plain language, present tense
```

### Empty States

```
Three types of empty states:

1. FIRST USE (user hasn't done anything yet)
   Don't show: "No data found"
   Show:       What it is + what to do first
   Example:    "Your projects live here. Create your first one to get started."

2. CLEARED (user deleted everything)
   Don't show: blank screen
   Show:       Acknowledge + light encouragement
   Example:    "All caught up. Nothing left to review."

3. NO RESULTS (search/filter returned nothing)
   Don't show: "No results"
   Show:       What was searched + suggestions
   Example:    "No posts match 'architecture'. Try 'system design' or browse all posts."
```

### Loading States

```
< 1 second:    No message needed — just show a spinner
1–3 seconds:   "Loading..." or skeleton UI
3–10 seconds:  Progress indicator + what is happening
               "Analyzing your codebase... (this takes about 30 seconds)"
> 10 seconds:  Step-by-step progress
               "Step 1 of 3: Fetching data..."

Never: show a spinner for > 10 seconds with no explanation
```

### Confirmation Dialogs

```
Title: state what is about to happen (not a question)
  ❌ "Are you sure?"
  ✅ "Delete this project?"

Body: consequence — what is irreversible?
  ❌ "This action cannot be undone."
  ✅ "This will permanently delete 'My Project' and all 47 files inside it."

Buttons:
  Confirm: restate the action  → "Delete project"
  Cancel:  "Cancel" or "Keep project"
  Never:   "Yes" / "No" — too ambiguous
```

---

## Onboarding Copy

```
Principles:
  1. Orient before instruct
     First tell the user WHERE they are, THEN what to do
  2. Value before setup
     Show value first — configuration can wait
  3. One step at a time
     Never show 5 things to complete at once
  4. Celebrate milestones
     Acknowledge completion, don't just advance

First-run checklist copy:
  ❌ "Complete your profile (0/4)"
  ✅ "Set up your workspace" → each step: specific, short, rewarding
```

---

## SEO-Aware Content

```
Page title:   [Primary keyword] — [Brand] | [Value]
  ✅ "Putera Kahfi — Full Stack Engineer, Yogyakarta"

Meta description: 150–160 chars, include primary keyword, end with implicit CTA
  ✅ "Full stack engineer building multi-tenant SaaS from one codebase. 
       Domain architecture, DDD, and long-lived systems."

H1:  One per page. Should match or closely relate to page title keyword.
H2s: Subheadings that answer questions users might search.

Image alt text:
  ❌ "image1.jpg"
  ❌ "Photo"
  ✅ "Screenshot of Blueprint — architectural documentation platform"
```

---

## Content Review Gates (Scored 0–10, Min 8)

```
Gate C1: Tone Consistency
  □ All copy matches declared tone card?
  □ No formal/casual mixing within same context?
  Score: __ / 10

Gate C2: Microcopy Quality
  □ All button labels = verb + noun?
  □ Error messages have: what + why + next step?
  □ Empty states are contextual (not generic "No data")?
  Score: __ / 10

Gate C3: Information Hierarchy
  □ Most important info first in every block?
  □ One idea per sentence?
  □ Active voice throughout?
  Score: __ / 10

Gate C4: Specificity
  □ No generic superlatives ("world-class", "best")?
  □ Claims are concrete or removed?
  □ Never-use list respected?
  Score: __ / 10

OVERALL: __ / 10   MINIMUM: 8.0
```
