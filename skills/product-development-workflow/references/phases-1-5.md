# Phases 1–5: Discovery → Implementation

## Phase 1 — Discovery

**Goal:** Understand the product opportunity.

Load conceptually:

```text
model-selection
user-research
business-value-alignment
experiment-design
product-manager
decision-making
```

Produce:

```text
- target user segments
- jobs-to-be-done
- pain points
- existing alternatives/workarounds
- opportunity list
- business value alignment brief
- experiment recommendation when assumptions are unverified
- ranked recommendation
```

**Gate:** Opportunity and business value must be explicit before PRD; EXPERIMENT_FIRST must produce an experiment design before PRD/build.

**Done when:** one MVP direction is recommended with user value, business value, metrics, rationale, open assumptions, and experiment plan when evidence is weak.

---

## Phase 2 — Requirements / PRD

**Goal:** Convert opportunity into a PRD.

Load conceptually:

```text
product-requirements
business-value-alignment
experiment-design
product-manager
```

Produce:

```text
- problem statement
- target users
- goals and non-goals
- user value and business value
- success metrics
- scope in/out
- user stories or JTBD
- functional requirements
- non-functional requirements
- acceptance criteria
- constraints, dependencies, risks, open questions
- launch criteria
```

**Gate:** PRD readiness must pass before MVP planning or technical spec.

**Done when:** `PRD READINESS` verdict is `READY` or explicit blockers are listed.

---

## Phase 3 — MVP Slice

**Goal:** Choose the smallest valuable release slice.

Load conceptually:

```text
business-value-alignment
experiment-design
product-manager
decision-making
spike
```

Produce:

```text
- MVP scope in/out
- value-aligned release slice
- deferred scope
- experiment or validation plan
- risks and assumptions
```

**Gate:** MVP scope or experiment must be smaller than the full product and must map to success metrics.

**Done when:** the user can approve one MVP slice.

---

## Phase 4 — Technical Spec

**Goal:** Translate PRD/MVP into agent-executable technical work.

Load conceptually:

```text
spec-workflow
native-ai-engineer
master-engineer
api-contract
data-modeling
```

Produce:

```text
- architecture constraints
- technical spec
- task plan
- context packs
- acceptance criterion mapping
```

**Gate:** technical spec must trace to PRD requirements.

**Done when:** every task traces to an acceptance criterion.

---

## Phase 5 — Implementation

**Goal:** Build the MVP slice.

Load conceptually:

```text
new-feature-workflow
test-driven-development
master-engineer
systematic-debugging
```

Produce:

```text
- implementation changes
- test evidence
- scope drift check
```

**Gate:** implementation must trace to acceptance criteria.

**Done when:** code changes are verified with real tool output.
