# PHP adapters

Verify `composer.json`, PHPUnit/Pest configuration, framework version, database and queue services, environment files, and CI scripts before selection.

| Adapter | Canonical capability mapping |
|---|---|
| PHPUnit or Pest | unit-testing; bounded integration-testing; executable acceptance checks |
| Symfony or Laravel test utilities | integration-testing and acceptance-testing at verified framework boundaries |
| Behat | behavior-driven-development automation adapter when collaboration and examples justify BDD |
| browser drivers | end-to-end-testing only when browser behavior is material |
| Testcontainers | integration-testing with isolated real infrastructure |
| Pact or schema validators | contract-testing |

Framework convenience must not blur test ownership. A kernel boot is not automatically E2E, a browser test is not automatically acceptance, and Gherkin is not automatically BDD. Record exact commands, environment assumptions, cleanup, failures, skips, and limitations.