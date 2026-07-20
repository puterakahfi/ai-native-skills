# Workflow Inventory

## .github/workflows/boundary-inventory.yml

```yaml
name: Boundary Inventory Audit

on:
  push:
    branches:
      - 25-boundary-declarations
    paths:
      - .github/workflows/boundary-inventory.yml
      - skills/**/SKILL.md
  workflow_dispatch:

permissions:
  contents: write

jobs:
  inventory:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout skills repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Checkout pinned Native AI Core
        uses: actions/checkout@v4
        with:
          repository: puterakahfi/ai-native-core
          ref: b60eb2da7d3a31ce0d539f38da58e8a70806c353
          path: .boundary-audit-core

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install audit dependency
        run: python -m pip install --disable-pip-version-check pyyaml

      - name: Generate boundary inventory
        shell: bash
        run: |
          python - <<'PY'
          from __future__ import annotations

          import json
          import re
          from collections import Counter, defaultdict
          from pathlib import Path

          import yaml

          ROOT = Path.cwd()
          CORE = ROOT / ".boundary-audit-core"
          OUT = ROOT / "audit"
          OUT.mkdir(exist_ok=True)

          FRONTMATTER = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
          SIGNAL_WORDS = {
              "boundary", "boundaries", "cover", "covers", "covered",
              "delegate", "delegates", "delegated", "handoff", "hand-off",
              "out of scope", "does not", "do not", "not cover", "not own",
              "belongs to", "responsibility", "responsibilities", "owner",
              "provider", "runtime", "product", "adapter", "specialist",
          }

          def parse_frontmatter(text: str) -> tuple[dict, str]:
              match = FRONTMATTER.match(text)
              if not match:
                  return {}, text
              data = yaml.safe_load(match.group(1)) or {}
              return data, text[match.end():].lstrip("\n")

          def contract_payload(path: Path) -> dict:
              data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
              return data.get("skill_contract", data)

          def normalize(value: str) -> str:
              return re.sub(r"_+", "_", re.sub(r"[^a-z0-9]+", "_", value.lower())).strip("_")

          def tokens(value: str) -> list[str]:
              return [t for t in normalize(value).split("_") if len(t) >= 4]

          def item_evidence(item: str, body_lower: str) -> dict:
              normalized = normalize(item)
              phrase_hit = (
                  normalized in normalize(body_lower)
                  or item.lower() in body_lower
                  or item.lower().replace("_", " ") in body_lower
              )
              item_tokens = tokens(item)
              hits = [token for token in item_tokens if token in body_lower]
              ratio = 1.0 if not item_tokens else len(hits) / len(item_tokens)
              return {
                  "item": item,
                  "phrase_hit": phrase_hit,
                  "token_hits": hits,
                  "token_total": len(item_tokens),
                  "token_ratio": round(ratio, 3),
              }

          def evidence_lines(body: str, boundary_items: list[str]) -> list[str]:
              terms = set(SIGNAL_WORDS)
              for item in boundary_items:
                  terms.update(tokens(item))
              selected = []
              for number, raw in enumerate(body.splitlines(), 1):
                  stripped = raw.strip()
                  if not stripped:
                      continue
                  lower = stripped.lower()
                  if any(term in lower for term in terms):
                      selected.append(f"L{number}: {stripped}")
              return selected[:40]

          records = []
          missing_contracts = []
          for skill_path in sorted((ROOT / "skills").glob("*/SKILL.md")):
              text = skill_path.read_text(encoding="utf-8")
              frontmatter, body = parse_frontmatter(text)
              metadata = frontmatter.get("metadata", {}) or {}
              if not isinstance(metadata, dict):
                  continue
              implements = metadata.get("ai-native-skills.implements")
              if not implements:
                  continue
              contract_rel = str(implements).replace("ai-native-core/", "")
              contract_path = CORE / contract_rel
              if not contract_path.exists():
                  missing_contracts.append({"skill": str(skill_path.relative_to(ROOT)), "contract": contract_rel})
                  continue
              contract = contract_payload(contract_path)
              boundary = contract.get("boundary", {}) or {}
              covers = boundary.get("covers", []) or []
              delegates = boundary.get("does_not_cover", []) or []
              covers = [item for item in covers if isinstance(item, str)]
              delegates = [item for item in delegates if isinstance(item, str)]
              body_lower = body.lower()
              cover_evidence = [item_evidence(item, body_lower) for item in covers]
              delegate_evidence = [item_evidence(item, body_lower) for item in delegates]
              current_covers = metadata.get("ai-native-skills.boundary.covers")
              current_delegates = metadata.get("ai-native-skills.boundary.delegates")
              has_boundary = bool(covers or delegates)
              low_evidence = [e["item"] for e in cover_evidence + delegate_evidence if not e["phrase_hit"] and e["token_ratio"] < 0.5]
              status = "NO_CONTRACT_BOUNDARY"
              if has_boundary and current_covers is None and current_delegates is None:
                  status = "REVIEW_REQUIRED"
              elif has_boundary:
                  status = "DECLARED_REVIEW_REQUIRED"
              records.append({
                  "skill": frontmatter.get("name", skill_path.parent.name),
                  "path": str(skill_path.relative_to(ROOT)),
                  "skill_type": metadata.get("ai-native-skills.type"),
                  "skill_version": metadata.get("ai-native-skills.version"),
                  "contract": contract_rel,
                  "contract_version": contract.get("version"),
                  "covers": covers,
                  "delegates": delegates,
                  "current_covers": current_covers,
                  "current_delegates": current_delegates,
                  "cover_evidence": cover_evidence,
                  "delegate_evidence": delegate_evidence,
                  "low_evidence_items": low_evidence,
                  "evidence_lines": evidence_lines(body, covers + delegates),
                  "headings": [line.strip() for line in body.splitlines() if line.lstrip().startswith("#")][:30],
                  "status": status,
              })

          summary = Counter(record["status"] for record in records)
          category_counts = defaultdict(int)
          for record in records:
              parts = Path(record["contract"]).parts
              category = parts[2] if len(parts) > 3 and parts[1] == "skills" else parts[1] if len(parts) > 1 else "unknown"
              category_counts[category] += 1

          payload = {
              "core_ref": "b60eb2da7d3a31ce0d539f38da58e8a70806c353",
              "adapter_count": len(records),
              "summary": dict(summary),
              "category_counts": dict(sorted(category_counts.items())),
              "missing_contracts": missing_contracts,
              "records": records,
          }
          (OUT / "boundary-inventory.json").write_text(
              json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
          )

          lines = [
              "# Boundary Declaration Inventory",
              "",
              "> Generated evidence for issue #25. This report is not an approval record and does not mutate skill metadata.",
              "",
              f"- Pinned core: `b60eb2da7d3a31ce0d539f38da58e8a70806c353`",
              f"- Contract-backed adapters: **{len(records)}**",
              f"- Missing contract paths: **{len(missing_contracts)}**",
              "",
              "## Status summary",
              "",
          ]
          for key, value in sorted(summary.items()):
              lines.append(f"- `{key}`: {value}")
          lines += ["", "## Contract categories", ""]
          for key, value in sorted(category_counts.items()):
              lines.append(f"- `{key}`: {value}")
          if missing_contracts:
              lines += ["", "## Missing contracts", ""]
              for item in missing_contracts:
                  lines.append(f"- `{item['skill']}` → `{item['contract']}`")

          lines += ["", "## Adapter audit", ""]
          for record in records:
              lines += [
                  f"### {record['skill']}",
                  "",
                  f"- Path: `{record['path']}`",
                  f"- Contract: `{record['contract']}` @ `{record['contract_version']}`",
                  f"- Type/version: `{record['skill_type']}` / `{record['skill_version']}`",
                  f"- Audit status: `{record['status']}`",
                  f"- Low-evidence items: `{record['low_evidence_items']}`",
                  "",
                  "**Contract covers**",
                  "",
              ]
              lines.extend([f"- `{item}`" for item in record["covers"]] or ["- _None_"])
              lines += ["", "**Contract delegates**", ""]
              lines.extend([f"- `{item}`" for item in record["delegates"]] or ["- _None_"])
              lines += ["", "**Current declarations**", ""]
              lines.append(f"- Covers: `{record['current_covers']}`")
              lines.append(f"- Delegates: `{record['current_delegates']}`")
              lines += ["", "**Evidence excerpts**", ""]
              if record["evidence_lines"]:
                  lines.append("```text")
                  lines.extend(record["evidence_lines"])
                  lines.append("```")
              else:
                  lines.append("_No boundary-related excerpt detected._")
              lines.append("")

          (OUT / "boundary-inventory.md").write_text("\n".join(lines), encoding="utf-8")
          print(json.dumps(payload["summary"], indent=2))
          print(f"Generated {len(records)} adapter records")
          PY

      - name: Commit inventory report
        shell: bash
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add audit/boundary-inventory.json audit/boundary-inventory.md
          if git diff --cached --quiet; then
            echo "Inventory unchanged"
            exit 0
          fi
          git commit -m "chore(audit): generate boundary declaration inventory [skip ci]"
          git push origin HEAD:${GITHUB_REF_NAME}
```

## .github/workflows/boundary-review-required.yml

```yaml
name: Boundary Review Queue

on:
  push:
    branches:
      - 25-boundary-declarations
    paths:
      - .github/workflows/boundary-review-required.yml
      - audit/boundary-inventory.json
  workflow_dispatch:

permissions:
  contents: write

jobs:
  extract:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Extract review-required adapters
        run: |
          python - <<'PY'
          import json
          from pathlib import Path

          root = Path.cwd()
          data = json.loads((root / "audit/boundary-inventory.json").read_text(encoding="utf-8"))
          records = [record for record in data["records"] if record["status"] == "REVIEW_REQUIRED"]

          lines = [
              "# Boundary Review Queue",
              "",
              f"Adapters requiring declaration review: **{len(records)}**",
              "",
          ]
          for record in records:
              lines += [
                  f"## {record['skill']}",
                  "",
                  f"- Path: `{record['path']}`",
                  f"- Contract: `{record['contract']}` @ `{record['contract_version']}`",
                  f"- Low-evidence items: `{record['low_evidence_items']}`",
                  "",
                  "### Covers",
                  "",
              ]
              lines += [f"- `{item}`" for item in record["covers"]] or ["- _None_"]
              lines += ["", "### Delegates", ""]
              lines += [f"- `{item}`" for item in record["delegates"]] or ["- _None_"]
              lines += ["", "### Evidence excerpts", "", "```text"]
              lines += record["evidence_lines"] or ["No boundary-related excerpt detected."]
              lines += ["```", ""]

          output = root / "audit/boundary-review-required.md"
          output.write_text("\n".join(lines), encoding="utf-8")
          print(f"Extracted {len(records)} adapters")
          PY

      - name: Commit review queue
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add audit/boundary-review-required.md
          if git diff --cached --quiet; then
            echo "Review queue unchanged"
            exit 0
          fi
          git commit -m "chore(audit): extract boundary review queue [skip ci]"
          git push origin HEAD:${GITHUB_REF_NAME}
```

## .github/workflows/skill-eval.yml

```yaml
name: Skill and Gate Contracts

on:
  push:
    branches: [main]
    paths:
      - "contracts/tests/**"
      - "skills/**"
      - "scripts/run-eval.sh"
      - "scripts/validate-eval-contracts.py"
      - "scripts/validate-design-gate-registry.py"
      - ".github/workflows/skill-eval.yml"
  pull_request:
    paths:
      - "contracts/tests/**"
      - "skills/**"
      - "scripts/run-eval.sh"
      - "scripts/validate-eval-contracts.py"
      - "scripts/validate-design-gate-registry.py"
      - ".github/workflows/skill-eval.yml"
  workflow_dispatch:

permissions:
  contents: read

concurrency:
  group: skill-and-gate-contracts-${{ github.ref }}
  cancel-in-progress: true

jobs:
  validate:
    name: Validate skill and gate contracts
    runs-on: ubuntu-latest
    timeout-minutes: 10

    steps:
      - name: Checkout ai-native-skills
        uses: actions/checkout@v6

      - name: Set up Python
        uses: actions/setup-python@v6
        with:
          python-version: "3.12"

      - name: Install validator dependency
        run: python -m pip install "PyYAML>=6,<7"

      - name: Check local validator and runner syntax
        run: |
          python -m py_compile scripts/validate-design-gate-registry.py
          python -m py_compile scripts/validate-eval-contracts.py
          bash -n scripts/run-eval.sh

      - name: Validate canonical design gate registry
        run: python scripts/validate-design-gate-registry.py

      - name: Validate repository eval contracts
        run: |
          python scripts/validate-eval-contracts.py \
            --write-smoke-outputs .tmp/eval-smoke-outputs

      - name: Checkout pinned ai-native-core runner
        uses: actions/checkout@v6
        with:
          repository: puterakahfi/ai-native-core
          ref: 5c4c6f21859636a4a143a511030879c9923b2ef1
          path: .deps/ai-native-core

      - name: Validate contracts with canonical core runner
        env:
          SKILL_EVAL_TESTS_DIR: ${{ github.workspace }}/contracts/tests
        run: |
          python .deps/ai-native-core/scripts/run-eval.py \
            --all \
            --validate-tests

      - name: Verify wrapper integration
        env:
          AI_NATIVE_CORE_DIR: ${{ github.workspace }}/.deps/ai-native-core
        run: |
          bash scripts/run-eval.sh --all --validate-tests

      - name: Run per-case runner compatibility smoke
        env:
          AI_NATIVE_CORE_DIR: ${{ github.workspace }}/.deps/ai-native-core
        run: |
          mkdir -p .tmp/eval-reports
          bash scripts/run-eval.sh \
            --all \
            --output-dir .tmp/eval-smoke-outputs \
            --report-json .tmp/eval-reports/contract-smoke.json

      - name: Upload compatibility report
        if: always()
        uses: actions/upload-artifact@v7
        with:
          name: skill-eval-contract-smoke
          path: .tmp/eval-reports/contract-smoke.json
          if-no-files-found: warn
          retention-days: 14
```

## .github/workflows/skill-packs.yml

```yaml
name: Skill Pack Contracts

on:
  push:
    branches: [main]
    paths:
      - "packs/**"
      - "docs/skill-packs.md"
      - "skills/**/SKILL.md"
      - "skills/**/references/dependencies-and-installation.md"
      - "scripts/validate-skill-packs.py"
      - "tests/test_validate_skill_packs.py"
      - ".github/workflows/skill-packs.yml"
  pull_request:
    paths:
      - "packs/**"
      - "docs/skill-packs.md"
      - "skills/**/SKILL.md"
      - "skills/**/references/dependencies-and-installation.md"
      - "scripts/validate-skill-packs.py"
      - "tests/test_validate_skill_packs.py"
      - ".github/workflows/skill-packs.yml"
  workflow_dispatch:

permissions:
  contents: read

concurrency:
  group: skill-pack-contracts-${{ github.ref }}
  cancel-in-progress: true

jobs:
  validate:
    name: Validate skill pack contracts
    runs-on: ubuntu-latest
    timeout-minutes: 10

    steps:
      - name: Checkout ai-native-skills
        uses: actions/checkout@v6

      - name: Set up Python
        uses: actions/setup-python@v6
        with:
          python-version: "3.12"

      - name: Install validator dependency
        run: python -m pip install "PyYAML>=6,<7"

      - name: Check validator syntax
        run: python -m py_compile scripts/validate-skill-packs.py tests/test_validate_skill_packs.py

      - name: Run focused validator tests
        run: python -m unittest tests/test_validate_skill_packs.py

      - name: Validate pack manifests, workflow bindings, and documentation
        run: python scripts/validate-skill-packs.py

      - name: Show reproducible Redesign Pack command
        run: python scripts/validate-skill-packs.py --pack redesign --profile complete --print-install-command
```

## .github/workflows/workflow-inventory.yml

```yaml
name: Workflow Inventory

on:
  push:
    branches:
      - 25-boundary-declarations
    paths:
      - .github/workflows/workflow-inventory.yml
  workflow_dispatch:

permissions:
  contents: write

jobs:
  inventory:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Capture workflow sources
        run: |
          mkdir -p audit
          {
            echo '# Workflow Inventory'
            echo
            for file in .github/workflows/*; do
              echo "## $file"
              echo
              echo '```yaml'
              cat "$file"
              echo '```'
              echo
            done
          } > audit/workflow-inventory.md
      - name: Commit report
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add audit/workflow-inventory.md
          git commit -m "chore(audit): capture workflow inventory [skip ci]"
          git push origin HEAD:${GITHUB_REF_NAME}
```

