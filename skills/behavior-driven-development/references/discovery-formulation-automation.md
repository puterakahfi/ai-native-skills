# Discovery, formulation, and automation

## Discovery

Bring together the people who own intent, domain meaning, implementation constraints, and quality risk. Identify rules, assumptions, unknowns, and vocabulary conflicts before writing scenarios.

## Example mapping

For each rule, capture representative examples, counterexamples, boundary cases, and questions. Examples should reveal decisions, not merely restate prose requirements.

## Formulation

Describe observable preconditions, event or action, and outcome in shared domain language. Given/When/Then can structure meaning but is not mandatory. Avoid selectors, private methods, framework hooks, database rows, and exact click timing unless those are the approved behavior.

## Automation handoff

Approved examples route to `acceptance-testing`, then to the minimum justified unit, integration, contract, or E2E surface. BDD does not automatically imply browser or E2E automation. Each handoff records the approved example identifier, selected test level, rejected alternatives, and evidence owner.

## Non-use cases

BDD is not justified when no business ambiguity exists, collaboration cannot occur, scenarios would only mirror low-level technical mechanics, or the cost exceeds the decision value.

## Evidence

Preserve participant roles, authority source, rules, examples, counterexamples, open questions, approvals, rejected formulations, and automation handoffs.