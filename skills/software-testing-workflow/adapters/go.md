# Go adapters

Verify `go.mod`, package boundaries, build tags, service dependencies, Make targets, and CI commands before selection.

| Adapter | Canonical capability mapping |
|---|---|
| `testing`, table-driven tests, fuzzing | unit-testing; bounded integration-testing |
| `httptest` | integration-testing or acceptance-testing at an HTTP boundary |
| Testcontainers | integration-testing with real infrastructure |
| schema or consumer-driven contract libraries | contract-testing when provider-consumer compatibility is material |
| repository-specific process harness | end-to-end-testing for justified non-browser journeys |

Prefer standard library evidence when sufficient. Helper libraries are adapters, not quality proof. Do not replace transaction, migration, concurrency, protocol, or eventual-consistency risk with mocks. Preserve race, timeout, environment, and cleanup evidence where applicable.