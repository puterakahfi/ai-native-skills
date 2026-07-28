#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

revision="$(git rev-parse HEAD)"
if [[ ! "$revision" =~ ^[0-9a-f]{40}$ ]]; then
  echo "Published catalog validation failed: HEAD is not an exact lowercase 40-character SHA" >&2
  exit 1
fi

echo "[1/5] Verify canonical capability inventory"
python3 scripts/verify-capability-inventory.py

echo "[2/5] Verify canonical capability discovery documents"
python3 scripts/verify-capability-discovery.py

echo "[3/5] Run Published Catalog regression harness"
python3 scripts/test-published-capability-catalog.py

echo "[4/5] Generate Published Catalog from exact revision $revision"
python3 scripts/build-published-capability-catalog.py \
  --write \
  --source-revision "$revision"

echo "[5/5] Verify committed artifact freshness and determinism"
python3 scripts/build-published-capability-catalog.py --check

python3 - <<'PY'
import json
from pathlib import Path

catalog_path = Path("catalog/published/capability-catalog.json")
catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
counts = catalog["inventory"]["counts"]
print(
    "Published Capability Catalog local gate passed: "
    f"revision={catalog['source']['revision']} "
    f"skills={counts['skill']} workflows={counts['workflow']} "
    f"meta_skills={counts['meta-skill']} total={counts['total']}"
)
PY
