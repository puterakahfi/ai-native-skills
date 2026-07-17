# Skill Packs Reference

## Presets

Choose the smallest preset that satisfies the intended runtime.

| Preset | Use when | Includes |
|---|---|---|
| `minimal` | Profile should only route work and understand Native AI boundaries | meta-skills, core workflows, Native AI runtime skills, context/rule skills |
| `engineering` | Default for coding/product engineering | `minimal` + engineering quality + architecture foundation |
| `product` | Profile will design/build product UX and landing/app surfaces | `engineering` + design/product/CRO pack |
| `runtime-ops` | Profile will operate a canonical remote Hermes runtime | `minimal` + runtime ops, deployment, observability, incident skills |
| `full` | Profile should be a complete AI-native engineering workstation | all packs below |

Default to `engineering` unless the user names a narrower or broader preset.

---

## Required Skill Packs

### Meta-skills

Install in every preset:

```text
workflow-router
role-switcher
```

Purpose: classify the request before execution and compose the right workflow/role lenses.

### Core workflows

Install in every preset:

```text
spec-workflow
product-development-workflow
new-feature-workflow
bugfix-workflow
code-review-workflow
deployment-workflow
```

Add for product/design presets:

```text
redesign-workflow
```

### Native AI runtime foundation

Install in every preset:

```text
native-ai-engineer
native-ai-runtime-agent
native-ai-runtime-ops
context-engineering
context-manager
rule-manager
response-contract
model-selection
business-value-alignment
experiment-design
```

Purpose: keep core/app/runtime/product/profile boundaries explicit, make profile behavior repeatable, require model choice to be intentional, and align work to measurable value before execution, and turn uncertain value into minimum viable experiments.

### Engineering quality foundation

Install for `engineering`, `product`, `runtime-ops`, and `full`:

```text
systematic-debugging
test-driven-development
refactoring
architecture-review
security-review
threat-modeling
git-workflow
plan
spike
skill-eval
```

### Architecture foundation

Install for `engineering`, `product`, and `full`:

```text
domain-driven-design
ports-and-adapters
api-contract
event-driven-design
service-design
systems-thinking
adr
```

### Runtime operations pack

Install for `runtime-ops` and `full`:

```text
observability-design
resilience-engineering
incident-response
deployment-workflow
native-ai-runtime-ops
```

### Product/design pack

Install for `product` and `full`:

```text
product-manager
product-requirements
master-design
design-review
design-system
design-genre
information-architecture
accessibility
responsiveness
ui-components
ux-patterns-for-developers
ux-ui-patterns
ux-psychology
visual-hierarchy
composition
macrostructures
motion-design
readability
dark-light-theming
copywriting
content-strategy
cro
web-performance
```
