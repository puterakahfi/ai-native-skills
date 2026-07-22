#!/usr/bin/env python3
"""Map unowned executable artifacts to exact canonical core contract candidates.

This script only produces candidate evidence. It never assigns a contract or
creates an exemption automatically.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any, Iterable

import yaml


def load_yaml(path: Path) -> dict[str, Any]:
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"{path}: YAML root must be a mapping")
    return payload


def contract_entries(node: Any) -> Iterable[dict[str, Any]]:
    if isinstance(node, dict):
        if isinstance(node.get("id"), str) and isinstance(node.get("path"), str):
            yield node
        for value in node.values():
            yield from contract_entries(value)
    elif isinstance(node, list):
        for value in node:
            yield from contract_entries(value)


def normalized(value: str) -> str:
    return "".join(char for char in value.lower() if char.isalnum())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".")
    parser.add_argument("--core-root", required=True)
    parser.add_argument("--inventory", default="docs/contract-coverage-discovery.yaml")
    parser.add_argument("--output", default="docs/unowned-contract-candidates.yaml")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    core_root = Path(args.core_root).resolve()
    inventory = load_yaml(root / args.inventory)["contract_coverage_inventory"]
    manifest = load_yaml(core_root / "contracts/manifest.yaml")

    entries = list(contract_entries(manifest.get("contracts", {})))
    by_id: dict[str, list[dict[str, Any]]] = {}
    by_normalized: dict[str, list[dict[str, Any]]] = {}
    for entry in entries:
        by_id.setdefault(entry["id"], []).append(entry)
        by_normalized.setdefault(normalized(entry["id"]), []).append(entry)

    candidates = []
    for artifact in inventory["artifacts"]:
        if artifact["classification"] != "unowned":
            continue
        artifact_id = artifact["id"]
        exact = by_id.get(artifact_id, [])
        normalized_matches = [
            entry
            for entry in by_normalized.get(normalized(artifact_id), [])
            if entry not in exact
        ]
        candidates.append(
            {
                "artifact_id": artifact_id,
                "artifact_path": artifact["path"],
                "type": artifact["type"],
                "patterns": artifact["patterns"],
                "exact_contract_candidates": [
                    {
                        "id": entry["id"],
                        "kind": entry.get("kind"),
                        "path": entry["path"],
                        "version": entry.get("version"),
                    }
                    for entry in exact
                ],
                "normalized_contract_candidates": [
                    {
                        "id": entry["id"],
                        "kind": entry.get("kind"),
                        "path": entry["path"],
                        "version": entry.get("version"),
                    }
                    for entry in normalized_matches
                ],
                "decision": "REVIEW_REQUIRED",
                "evidence_boundary": [
                    "matching identity does not prove executable implementation",
                    "no candidate may be assigned without interface and boundary review",
                    "absence of a candidate requires reviewed exemption or core gap decision",
                ],
            }
        )

    output = {
        "unowned_contract_candidate_inventory": {
            "schema_version": "0.1.0",
            "repository": "puterakahfi/ai-native-skills",
            "core_repository": "puterakahfi/ai-native-core",
            "summary": {
                "unowned_artifacts": len(candidates),
                "with_exact_candidate": sum(bool(item["exact_contract_candidates"]) for item in candidates),
                "without_exact_candidate": sum(not item["exact_contract_candidates"] for item in candidates),
            },
            "candidates": candidates,
        }
    }
    destination = root / args.output
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(yaml.safe_dump(output, sort_keys=False), encoding="utf-8")
    print(yaml.safe_dump(output["unowned_contract_candidate_inventory"]["summary"], sort_keys=False).strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
