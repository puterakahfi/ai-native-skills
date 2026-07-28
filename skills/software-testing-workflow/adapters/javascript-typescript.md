# JavaScript and TypeScript adapters

Verify `package.json`, lockfile, test scripts, framework config, services, and CI before selecting tools.

| Adapter | Canonical capability mapping | Use when verified |
|---|---|---|
| Vitest or Jest | unit-testing; bounded integration-testing | repository already uses it or compatibility is proven |
| Testing Library | acceptance-testing at component-observable boundary | user-observable component behavior is the claim |
| Playwright or Cypress | end-to-end-testing; selected acceptance journeys | browser behavior is materially part of the risk |
| Cucumber.js | behavior-driven-development formulation/automation adapter | shared examples and domain collaboration justify BDD |
| Testcontainers | integration-testing | real infrastructure behavior is material and isolated execution is available |
| Pact or schema validators | contract-testing | provider-consumer compatibility is the risk |

Do not infer commands. Preserve the exact verified script and environment. A tool being installed does not justify its test level. Browser tests, Gherkin, snapshots, or coverage percentages are never mandatory by framework presence alone.