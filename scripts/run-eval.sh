#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CORE_REF="7fd02ff3a14f628ca5cf30a5f20a3386f046da5a"

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

  printf '%s\n' "$ROOT_DIR/.deps/ai-native-core"
}

CORE_DIR="$(resolve_core_dir)"

if [[ ! -f "$CORE_DIR/scripts/run-eval.py" ]]; then
  echo "Missing ai-native-core eval runner at $CORE_DIR/scripts/run-eval.py" >&2
  echo "Clone ai-native-core at $CORE_REF into $CORE_DIR or set AI_NATIVE_CORE_DIR." >&2
  exit 1
fi

exec python3 "$CORE_DIR/scripts/run-eval.py" "$@"
