# Microcopy Patterns + Onboarding Copy + SEO-Aware Content

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

## Content Review Gate: Microcopy (Scored 0–10, Min 8)

```
Gate C2: Microcopy Quality
  □ All button labels = verb + noun?
  □ Error messages have: what + why + next step?
  □ Empty states are contextual (not generic "No data")?
  Score: __ / 10

OVERALL: __ / 10   MINIMUM: 8.0
```
