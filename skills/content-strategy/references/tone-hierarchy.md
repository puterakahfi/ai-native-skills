# Tone of Voice System + Content Hierarchy

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

## Content Review Gates (Scored 0–10, Min 8)

```
Gate C1: Tone Consistency
  □ All copy matches declared tone card?
  □ No formal/casual mixing within same context?
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
```
