#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CORE_REF="5c4c6f21859636a4a143a511030879c9923b2ef1"

resolve_core_dir() {
  if [[ -n "${AI_NATIVE_CORE_DIR:-}" ]]; then
    printf '%s\n' "$AI_NATIVE_CORE_DIR"
    return
  fi

  if [[ -f "$ROOT_DIR/.deps/ai-native-core/scripts/run-eval.py" ]]; then
    printf '%s\n' "$ROOT_DIR/.deps/ai-native-core"
    return
  fi

  if [[ -f "$ROOT_DIR/../ai-native-core/scripts/run-eval.py" ]]; then
    printf '%s\n' "$ROOT_DIR/../ai-native-core"
    return
  fi

  return 1
}

if ! CORE_DIR="$(resolve_core_dir)"; then
  cat >&2 <<EOF
ai-native-core eval runner was not found.

Provide one of:
  AI_NATIVE_CORE_DIR=/path/to/ai-native-core ./scripts/run-eval.sh ...
  clone ai-native-core beside this repository
  clone pinned core commit into .deps/ai-native-core:

    git clone https://github.com/puterakahfi/ai-native-core.git .deps/ai-native-core
    git -C .deps/ai-native-core checkout $CORE_REF
EOF
  exit 2
fi

RUNNER="$CORE_DIR/scripts/run-eval.py"
if [[ ! -f "$RUNNER" ]]; then
  echo "Missing core eval runner: $RUNNER" >&2
  exit 2
fi

export SKILL_EVAL_TESTS_DIR="$ROOT_DIR/contracts/tests"
exec python3 "$RUNNER" "$@"
