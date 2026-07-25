#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT_DIR="$ROOT_DIR/contracts/fixtures/repository-stack-conformance/outputs"
REPORT_DIR="${TMPDIR:-/tmp}/repository-stack-conformance-reports"
mkdir -p "$REPORT_DIR"

assert_overall() {
  local report="$1"
  local expected="$2"
  python3 - "$report" "$expected" <<'PY'
import json
import sys

path, expected = sys.argv[1:]
with open(path, encoding="utf-8") as handle:
    report = json.load(handle)
actual = report["overall"]
if actual != expected:
    raise SystemExit(f"expected {expected}, got {actual}: {path}")
print(f"{path}: {actual}")
PY
}

AI_NATIVE_CORE_DIR="${AI_NATIVE_CORE_DIR:-}" \
  "$ROOT_DIR/scripts/run-eval.sh" \
  --skill architecture-review \
  --case repository-native-artifact-passes-conformance \
  --output-dir "$OUTPUT_DIR" \
  --artifact-root "$ROOT_DIR/contracts" \
  --report-json "$REPORT_DIR/compliant.json"
assert_overall "$REPORT_DIR/compliant.json" APPLIED

set +e
AI_NATIVE_CORE_DIR="${AI_NATIVE_CORE_DIR:-}" \
  "$ROOT_DIR/scripts/run-eval.sh" \
  --skill architecture-review \
  --case textual-pass-cannot-hide-artifact-drift \
  --output-dir "$OUTPUT_DIR" \
  --artifact-root "$ROOT_DIR/contracts" \
  --report-json "$REPORT_DIR/drift.json"
drift_exit=$?
set -e
if [[ "$drift_exit" -ne 1 ]]; then
  echo "Expected drift fixture to exit 1, got $drift_exit" >&2
  exit 1
fi
assert_overall "$REPORT_DIR/drift.json" GHOST

set +e
AI_NATIVE_CORE_DIR="${AI_NATIVE_CORE_DIR:-}" \
  "$ROOT_DIR/scripts/run-eval.sh" \
  --skill architecture-review \
  --case missing-artifact-evidence-remains-incomplete \
  --output-dir "$OUTPUT_DIR" \
  --artifact-root "$ROOT_DIR/contracts" \
  --report-json "$REPORT_DIR/missing.json"
missing_exit=$?
set -e
if [[ "$missing_exit" -ne 1 ]]; then
  echo "Expected missing fixture to exit 1, got $missing_exit" >&2
  exit 1
fi
assert_overall "$REPORT_DIR/missing.json" INCOMPLETE

echo "Repository stack-conformance artifact evals passed."
