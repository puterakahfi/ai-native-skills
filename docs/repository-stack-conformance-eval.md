# Repository Stack-Conformance Evaluation

This repository uses the canonical artifact-aware skill-eval runner from `ai-native-core` commit `27b542c142fcbd9a7a5ad709a97489dbf190d0b0`.

The representative fixture models an existing Next.js application with source-copied shadcn/ui components, Tailwind semantic tokens, Lucide icons, and shared component conventions. It is evidence for repository-first behavior, not a universal stack recommendation.

## Fixture outcomes

```text
compliant fixture
  canonical Button/Select imports + configured shadcn registry
  + Tailwind semantic tokens + Lucide
  → APPLIED

artifact-drift fixture
  correct-sounding PASS narrative
  + second component and icon systems
  + local dialog/select behavior
  + route-local theme variables
  → GHOST

missing fixture
  review narrative exists
  + artifact root unavailable
  → INCOMPLETE
```

## Run

```bash
git clone https://github.com/puterakahfi/ai-native-core.git .deps/ai-native-core
git -C .deps/ai-native-core checkout 27b542c142fcbd9a7a5ad709a97489dbf190d0b0

AI_NATIVE_CORE_DIR="$PWD/.deps/ai-native-core" \
  ./scripts/run-stack-conformance-eval.sh
```

The script runs one positive and two expected-negative cases and validates the JSON result classifications. A negative fixture is successful only when the runner rejects it with the expected classification.

## Extension pattern

Other stacks can reuse this evaluation pattern by supplying:

- a minimal canonical implementation-context profile;
- a compliant fixture using actual accepted paths/imports;
- drift fixtures representing real bypass or parallel-system failures;
- bounded artifact assertions in the relevant behavioral test contract;
- output text that proves artifact evidence, not rhetoric, controls the result.

Keep stack-specific choices in the adapter or product fixture. Do not move Next.js, shadcn/ui, Tailwind, Lucide, or another stack into generic core policy.
