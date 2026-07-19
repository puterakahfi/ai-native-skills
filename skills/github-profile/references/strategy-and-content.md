# GitHub Profile Strategy and Content

Use this reference before choosing visuals. A strong profile is a decision surface: it helps a specific visitor understand the person, trust the evidence, and take one useful next action.

## Strategy Canvas

```yaml
profile_strategy:
  goal: <primary outcome>
  audience: <primary visitor>
  visitor_question: <what they need to decide>
  positioning: <specific role or value>
  differentiation: <why this person rather than a generic peer>
  proof_theme: <projects | products | open-source | leadership | writing | community>
  desired_action: <one primary action>
  tone: <credible, direct, warm, technical, editorial, etc.>
  exclusions: <what this profile should not become>
```

One profile may support several audiences, but one audience must control the opening hierarchy. Secondary audiences can be served later in the page.

## Narrative Patterns

### Engineering authority

Use when the primary decision is technical credibility.

```text
identity → engineering thesis → selected systems/projects → capabilities
→ current focus → writing/open source → contact
```

Lead with the kind of problems solved, not a list of languages.

### Builder or founder

Use when products and execution matter more than employment history.

```text
identity → product thesis → active products → shipped proof
→ technical/product capabilities → current bets → contact
```

Show what was built, for whom, and what changed.

### Open-source steward

Use when collaboration and community trust are primary.

```text
identity → contribution mission → maintained projects → contribution guidance
→ current roadmap → community links → sponsor/contact
```

Contribution instructions and project health may be more useful than a decorative stack.

### Consultant or freelancer

Use when the desired action is a qualified inquiry.

```text
identity → client problem → service focus → selected outcomes
→ working model → credibility → contact
```

Do not publish unsupported client logos, revenue, conversion, or performance claims.

### Multi-disciplinary personal brand

Use when the person combines engineering, design, writing, research, or entrepreneurship.

```text
identity → unifying thesis → focus areas → selected proof by theme
→ current exploration → writing/products → contact
```

A unifying thesis is mandatory; otherwise the profile becomes unrelated role fragments.

## Evidence Hierarchy

Prefer evidence in this order:

```text
1. Direct repository or shipped-product evidence
2. Specific project context, role, decision, and outcome
3. Maintainer/contributor responsibility and visible activity
4. Public writing, talks, documentation, or community work
5. Verified third-party recognition or client evidence
6. Self-described capability
7. Decorative statistics or counters
```

A self-description may introduce a capability, but important trust claims should be followed by visible proof.

## Project Proof Contract

Each selected project should answer as many of these as evidence permits:

```yaml
project_proof:
  name: <project or product>
  problem: <why it exists>
  role: <what the person owned>
  contribution: <specific work or decision>
  outcome: <verified result or current state>
  technology: <only relevant technology>
  destination: <repository, product, case study, documentation, or demo>
  status: active | maintained | experimental | archived | unknown
```

Never turn missing outcomes into invented metrics. A precise non-metric outcome is better than fake numbers.

## Visitor Question Order

A balanced profile usually answers:

```text
1. Who is this?
2. What do they actually do?
3. Who benefits from it?
4. What evidence proves it?
5. What are they focused on now?
6. How can I inspect more or contact them?
```

Sections that do not answer a visitor question should be removed, compressed, or moved lower.

## Content Roles

### Hero

Contains identity, specific positioning, one supporting sentence, and one or two actions. It may include a brand asset, but essential text must remain semantic text.

### Selected work

Three strong examples usually outperform ten context-free cards. Order by relevance to the target audience, not repository stars alone.

### Capabilities

Group by problem or responsibility when possible:

```text
Architecture and systems
Product engineering
AI-native engineering
Developer experience
Design collaboration
```

Avoid presenting every tool ever used as equal expertise.

### Current focus

Use only supplied or repository-verifiable current work. Include dates or status when “current” may become stale.

### Contact and action

One primary action should be visually dominant. Secondary links remain available without becoming a social-icon wall.

## Copy Rules

```text
specific nouns and verbs over abstract adjectives
proof over self-praise
short opening, richer project context
one terminology system for roles and capabilities
no fake confidence, fake humility, or generic inspirational filler
no “passionate developer” unless the sentence adds specific meaning
no keyword stuffing for recruiters
```

Replace generic claims:

```text
"I build scalable solutions"
→ "I design modular backend systems and AI-native developer tooling."

"Experienced in many technologies"
→ "My core work spans Go/PHP services, Next.js products, DDD, and agent workflows."
```

Only use the replacement when it is true for the subject.

## Redesign Preservation

Before redesigning an existing README, classify:

```text
preserve  verified identity, working links, recognizable brand assets,
          strong project proof, accepted tone, useful community instructions

refine    weak hierarchy, excessive density, inconsistent module styles,
          repetitive stack content, unclear calls to action

remove    stale claims, broken widgets, decorative duplication,
          unsupported metrics, irrelevant counters, generic filler

verify    current focus, employment status, project status, statistics,
          third-party cards, theme variants, external image ownership
```

Do not erase existing equity merely to impose a new visual genre.