# Engineering workflow integration audit

The testing workflow is a conditional verification composition, never a competing primary lifecycle.

| Integration candidate | Decision |
|---|---|
| `workflow-router` | route one primary engineering workflow; discover `software-testing-workflow` when material testing concerns exist |
| `role-switcher` | retain one delivery owner; add testing specialists only for selected levels |
| `new-feature-workflow` | compose after implementation-context discovery and before final verification when material risks require a portfolio |
| `bugfix-workflow` | preserve reproduce/root-cause/TDD ownership; compose the minimum regression portfolio during verify |
| `spec-workflow` | expose acceptance criteria, examples, contracts, risks, and unresolved evidence needs; do not execute tests itself |
| `test-driven-development` | retain RED-GREEN-REFACTOR ownership; hand selected test boundaries to implementation |
| `refactoring` | preserve behavior and select characterization/regression evidence proportionate to affected boundaries |
| `production-code-quality-baseline` | remain the mandatory quality overlay; consume testing evidence without becoming the testing lifecycle |
| `code-review-workflow` | review risk coverage, commands, results, failures, flakiness, limitations, and traceability—not file presence |
| `architecture-review` | verify that test boundaries and doubles do not conceal architecture risks |
| release handoff | unresolved failure, flaky, skipped, unavailable, unsupported, or insufficient evidence blocks applicable PASS |

Integration is applicability-driven. A workflow may return `NOT_APPLICABLE` or `NOT_JUSTIFIED` for the testing composition when supported by evidence. Unknown required evidence is `NOT_VERIFIED`.