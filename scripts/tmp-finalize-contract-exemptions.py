#!/usr/bin/env python3
"""One-time allowlisted completion of reviewed contract exemption records."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml

REVIEW_DATE = "2026-10-22"
SCOPES = {
    "composition": ["static_contract_ownership", "core_gap_tracking"],
    "visual-hierarchy": ["static_contract_ownership", "core_gap_tracking"],
    "design-audit": ["static_contract_ownership", "core_gap_tracking"],
    "prompt-engineer": ["static_contract_ownership", "core_gap_tracking"],
    "skill-doctor": ["static_contract_ownership", "core_gap_tracking"],
    "chatgpt-app-development": ["static_contract_ownership", "provider_specific_execution"],
    "github-profile": ["static_contract_ownership", "provider_specific_execution"],
    "ux-patterns-for-developers": ["static_contract_ownership", "third_party_delegation"],
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()

    for artifact_id, scope in SCOPES.items():
        path = root / "skills" / artifact_id / "contract.exemption.yaml"
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
        exemption = payload["contract_exemption"]
        if exemption["artifact"]["id"] != artifact_id:
            raise ValueError(f"{artifact_id}: exemption identity mismatch")
        if "scope" in exemption or "review_date" in exemption:
            raise ValueError(f"{artifact_id}: scope or review date already present")
        exemption["scope"] = scope
        exemption["review_date"] = REVIEW_DATE

        ordered = {
            "schema_version": exemption["schema_version"],
            "artifact": exemption["artifact"],
            "classification": exemption["classification"],
            "owner": exemption["owner"],
            "reason": exemption["reason"],
            "scope": exemption["scope"],
            "review_date": exemption["review_date"],
            "evidence_refs": exemption["evidence_refs"],
            "revisit": exemption["revisit"],
            "prohibited_claims": exemption["prohibited_claims"],
            "status": exemption["status"],
        }
        path.write_text(
            yaml.safe_dump({"contract_exemption": ordered}, sort_keys=False),
            encoding="utf-8",
        )
        print(f"finalized {artifact_id} review_date={REVIEW_DATE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
