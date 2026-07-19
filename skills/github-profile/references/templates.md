# GitHub Profile Templates

These are structural starting points, not visual identities to copy verbatim. Replace every placeholder with supplied or verified content, remove irrelevant modules, and select one coherent direction.

## Template A — Concise Technical Authority

Use for engineers, architects, maintainers, or technical leaders who need a durable text-first profile.

```markdown
# Name

**Specific role or positioning**

One concise sentence describing the systems, products, or problems you work on and for whom.

[Selected work](#selected-work) · [Writing](LINK) · [Contact](LINK)

## Selected work

### Project One
Problem, role, meaningful contribution, and verified outcome or current state.

[Repository](LINK) · [Documentation](LINK)

### Project Two
Problem, role, meaningful contribution, and verified outcome or current state.

[Repository](LINK) · [Product](LINK)

## Capabilities

**Architecture:** capability group  
**Product engineering:** capability group  
**AI-native systems:** capability group

## Current focus

- Verified current work or learning focus
- Verified active project or contribution

## Contact

Primary action and bounded secondary links.
```

## Template B — Editorial Personal Brand

Use for multi-disciplinary engineers, designers, builders, researchers, or writers with one unifying thesis.

```markdown
<div align="center">

# Name

**Unifying positioning statement**

Short thesis connecting the person's disciplines and the value created.

[Explore the work](#selected-work) · [Read](LINK) · [Connect](LINK)

</div>

## What I build

A short paragraph defining the recurring problem space, approach, and audience.

## Selected work

- **Project or product** — contribution and verified outcome. [Explore →](LINK)
- **Project or product** — contribution and verified outcome. [Explore →](LINK)
- **Project or product** — contribution and verified outcome. [Explore →](LINK)

## Working principles

- Specific principle visible in the work
- Specific principle visible in the work
- Specific principle visible in the work

## Now

Dated, verified current focus.

## Connect

One primary contact action plus relevant channels.
```

## Template C — Product Builder or Founder

Use when shipped products and product thinking are the strongest proof.

```markdown
# Name

**Builder of specific products for a specific audience**

One sentence connecting product mission, technical capability, and customer/user value.

[Product](LINK) · [Selected builds](#selected-builds) · [Contact](LINK)

## Active products

### Product One
Who it serves, the problem, the person's role, current stage, and verified result.

[Visit product](LINK) · [View repository](LINK)

## Selected builds

- **Build** — what was built, why, and the meaningful contribution. [Explore →](LINK)
- **Build** — what was built, why, and the meaningful contribution. [Explore →](LINK)

## How I work

Short capability groups spanning product, engineering, design collaboration, or AI systems.

## Current bets

- Dated product or research direction
- Dated experiment or open-source initiative

## Work with me

Specific collaboration fit and one primary action.
```

## Template D — Open-Source Maintainer

Use when maintained repositories, contribution quality, and community clarity are primary.

```markdown
# Name

**Maintainer or contributor positioning**

One sentence describing the ecosystem, users, or technical mission supported.

[Projects](#maintained-projects) · [Contributing](LINK) · [Sponsor or contact](LINK)

## Maintained projects

### Project One
Purpose, maintainer responsibility, project status, and useful destination.

[Repository](LINK) · [Docs](LINK) · [Issues](LINK)

## Contribution focus

- Current roadmap or help-wanted area
- Contribution principles or review expectations
- Community support route

## Technical focus

Bounded capability groups relevant to the maintained work.

## Support the work

Sponsor, collaborate, contribute, or contact action as applicable.
```

## Optional Module — Visual Project

Use only when a stable, relevant visual exists.

```markdown
### Project Name

<img src="ASSET" alt="Meaningful description of the project visual" width="100%" />

Short project context, role, contribution, and outcome.

[Explore project →](LINK)
```

The image must not contain the only available project explanation.

## Optional Module — Technology Badges

Use a small, coherent subset after capabilities are already described.

```markdown
### Core tools

BADGES_FOR_ONLY_THE_PRIMARY_TOOLS
```

Do not include a badge for every dependency, platform, editor, or tool ever used.

## Optional Module — Theme-Aware Image

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="DARK_ASSET">
  <source media="(prefers-color-scheme: light)" srcset="LIGHT_ASSET">
  <img alt="Meaningful description" src="FALLBACK_ASSET">
</picture>
```

Verify actual GitHub rendering and preserve nearby semantic text.

## Template Selection Rules

```text
technical authority   → A unless a mature brand or visual portfolio justifies B
multi-disciplinary    → B only with a clear unifying thesis
product founder       → C with product proof before technology lists
open-source maintainer→ D with project health and contribution routes
mixed goal            → select one primary template, borrow at most two modules
```

Never concatenate all four templates. A template is successful when the final README no longer feels like a template.