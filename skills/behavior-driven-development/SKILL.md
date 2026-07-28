---
name: behavior-driven-development
description: Facilitate behavior discovery, example formulation, and automation handoff using shared domain language and observable examples. Gherkin and Cucumber are optional adapters, not the capability itself.
license: MIT
metadata:
  ai-native-skills.version: 0.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.requires: "product-requirements decision-provenance acceptance-testing"
  ai-native-skills.related_skills: '["end-to-end-testing","test-strategy","test-driven-development","user-research"]'
---

# Behavior-Driven Development

## Ownership

BDD owns collaborative discovery and formulation of business behavior through concrete examples, then hands approved examples to acceptance or other automation capabilities. It does not own product acceptance, E2E strategy, or a test framework.

## Applicability

Use when shared understanding across product, domain, engineering, and quality participants would materially reduce ambiguity. Return `NOT_JUSTIFIED` for ceremonial scenario writing, purely technical changes with no business-language ambiguity, or cases lacking decision participants.

## Lifecycle

```text
discovery
→ formulation
→ automation handoff
```

Load `references/discovery-formulation-automation.md` for example mapping and scenario rules.

## Procedure

1. Verify the business rule, authority, participants, and unresolved questions.
2. Map rules, examples, counterexamples, and open questions.
3. Formulate observable examples in shared domain language.
4. Use Given/When/Then semantics only when helpful; Gherkin is optional.
5. Remove selectors, private methods, framework steps, and click-script leakage.
6. Hand approved examples to acceptance-testing and the justified automation level.
7. Preserve unresolved questions as non-PASS, not invented behavior.

## Quality gates

- examples expose a rule or ambiguity;
- counterexamples and boundary cases are included;
- language is understandable to business and domain participants;
- scenarios describe observable behavior rather than implementation;
- automation level follows risk and system boundary;
- BDD is not used as a synonym for Cucumber or test automation;
- product authority remains external to the capability.

## Normalized output

```yaml
behavior_driven_development:
  applicability: APPLICABLE | NOT_JUSTIFIED | NOT_APPLICABLE
  authority: <verified source>
  rules: []
  examples: []
  counterexamples: []
  open_questions: []
  approved_examples: []
  automation_handoffs: []
  limitations: []
  verdict: PASS | NEEDS_WORK | NOT_VERIFIED
```

## Adapter boundary

Gherkin, Cucumber, Cucumber.js, Behat, SpecFlow, and framework step definitions are optional adapters. Replacing them must not alter discovery, formulation, domain-language, or authority semantics.