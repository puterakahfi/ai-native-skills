# Facade Skill Pattern

A facade skill provides one stable entry point to a group of related specialist capabilities while still performing a coherent capability of its own.

It hides subsystem selection and output normalization from callers without absorbing every specialist's knowledge.

## Taxonomy

`facade` is a pattern, not an official `ai-native-skills.type` value.

Use:

```yaml
metadata:
  ai-native-skills.type: skill
  ai-native-skills.pattern: facade
```

A facade remains a `skill` when it performs real domain work such as applicability decisions, evidence normalization, scoring, verdicts, or artifact assembly.

Use `meta-skill` instead when the artifact only selects other skills or workflows and stops after routing.

## Responsibilities

A facade skill normally owns:

```text
one public entry point
input classification
strategy or specialist selection
shared applicability rules
common evidence or data contract
normalized output
conflict and fallback handling
handoff boundaries
```

A facade skill does not own:

```text
every specialist rule
all implementation techniques
complete lifecycle orchestration
product-specific configuration
unrelated domains that merely share a few principles
```

## Facade vs Other Patterns

### Facade skill

```text
caller
→ one capability entry point
→ select relevant specialists
→ perform shared capability work
→ normalize result
```

Example: `design-review` classifies a design target, selects applicable review strategies, normalizes evidence, and produces one score and verdict.

### Meta-skill

```text
caller
→ classify intent
→ select skills/workflow
→ hand off
```

A meta-skill does not perform the selected capability itself.

### Workflow

```text
entry condition
→ ordered lifecycle phases
→ phase gates
→ completed lifecycle outcome
```

A workflow owns an end-to-end process such as redesign, deployment, or bug fixing.

### Adapter skill

```text
external/core contract
→ runtime or product-specific implementation
```

An adapter binds a contract to an execution context. A facade may invoke adapters, but the patterns solve different problems.

## When to Use

Use a facade skill when:

- callers need one stable capability interface;
- several strategies or specialist skills can satisfy different variants of the request;
- applicability must be decided before execution;
- specialist outputs need a shared evidence, result, or report contract;
- callers should not need to understand the internal skill graph;
- the facade can remain small by loading specialists on demand.

Do not use a facade when:

- one focused specialist already handles the capability cleanly;
- the artifact only routes and performs no capability work;
- the process is an ordered multi-phase lifecycle;
- all knowledge would still be copied into the facade;
- the domains are too unrelated to share a meaningful output contract.

## Required Contract

A facade skill should declare:

```yaml
facade:
  capability: <stable public capability>
  owns: []
  does_not_own: []
  built_in_strategies: []
  extension_contract: <contract or documented shape>
  fallback_policy: <limited | route-elsewhere | fail-closed>
  output_contract: <shared result shape>
```

Each plugged-in specialist or strategy should declare:

```yaml
specialist:
  domain: <stable domain id>
  applies_when: []
  required_context: []
  required_evidence: []
  output_contract: <facade-compatible shape>
  unsupported_claims: []
```

## Loading Rule

A facade must load knowledge by phase or decision, not as one permanent bundle.

```text
start with facade only
→ classify
→ load selected strategy/specialist
→ execute shared normalization
→ load reporting rules only when reporting
```

Splitting one monolith into files while always loading every file creates a modular folder but not a modular context.

## Boundary Test

A facade is healthy when:

```text
callers see one simple interface
specialists can evolve independently
the facade remains small
unsupported domains are explicit
output stays consistent across strategies
new domains plug in without rewriting the core
```

A facade is becoming a god skill when:

```text
specialist rules are duplicated in the core
every request loads every reference
new domains require editing many unrelated sections
one scorecard is forced across unrelated disciplines
unsupported work is claimed as fully covered
production and lifecycle ownership leak into the facade
```

## Canonical Example: Design Review

```text
design-review facade
├── owns classification, applicability, evidence, scoring, coverage, verdict
├── built-in interactive review strategy
├── built-in static visual review strategy
├── built-in presentation review strategy
└── external domain reviewers for identity, packaging, motion, and other disciplines
```

The facade can apply universal visual principles to an unsupported design discipline, but it must report a limited review unless a suitable domain reviewer is loaded.

## Anti-patterns

1. **Facade as knowledge dump.** Moving specialist rules into one entry skill recreates a monolith.
2. **Facade as fake meta-skill.** A facade must perform shared capability work, not only route.
3. **Always-load modularity.** Separate files do not help when every file is loaded for every request.
4. **Nearest-domain guessing.** Shared visual principles do not make packaging equivalent to a poster or identity equivalent to marketing artwork.
5. **Output mismatch.** Specialists must map into one shared result contract.
6. **Silent coverage gaps.** Unsupported domains must produce `LIMITED` or route elsewhere, never an invented full pass.
7. **Lifecycle leakage.** Review facades report findings; redesign workflows own production and correction loops.