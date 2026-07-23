#!/usr/bin/env python3
"""Validate a Project Instructions artifact against a runtime character budget."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def normalize(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def assess(count: int, hard_maximum: int, target_budget: int) -> str:
    if count > hard_maximum:
        return "FAIL"
    if count > target_budget:
        return "NEEDS_WORK"
    return "PASS"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="UTF-8 text file to validate")
    parser.add_argument("--hard-maximum", type=int, required=True)
    parser.add_argument("--target-budget", type=int, required=True)
    parser.add_argument("--runtime", required=True)
    parser.add_argument("--provenance", required=True)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    if args.hard_maximum <= 0:
        parser.error("--hard-maximum must be positive")
    if args.target_budget <= 0:
        parser.error("--target-budget must be positive")
    if args.target_budget > args.hard_maximum:
        parser.error("--target-budget cannot exceed --hard-maximum")
    if not args.path.is_file():
        parser.error(f"file not found: {args.path}")

    text = normalize(args.path.read_text(encoding="utf-8"))
    count = len(text)
    status = assess(count, args.hard_maximum, args.target_budget)
    payload = {
        "runtime": args.runtime,
        "character_count": count,
        "hard_maximum": args.hard_maximum,
        "target_budget": args.target_budget,
        "safety_margin": args.hard_maximum - args.target_budget,
        "remaining_hard_budget": args.hard_maximum - count,
        "remaining_target_budget": args.target_budget - count,
        "limit_provenance": args.provenance,
        "runtime_capacity": status,
    }

    if args.as_json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        for key, value in payload.items():
            print(f"{key}: {value}")

    return {"PASS": 0, "NEEDS_WORK": 2, "FAIL": 3}[status]


if __name__ == "__main__":
    raise SystemExit(main())
