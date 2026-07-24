#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, separators=(",", ":"), ensure_ascii=False) + "\n", encoding="utf-8")


subprocess.run(
    ["python3", "scripts/verify-capability-inventory.py", "--write-snapshot", "--skip-docs"],
    cwd=ROOT,
    check=True,
)

inventory = load_json(ROOT / "docs/capability-inventory.json")
counts = inventory["counts"]

readme = ROOT / "README.md"
readme_text = readme.read_text(encoding="utf-8")
readme_text = re.sub(
    r"\*\*\d+ skills · \d+ workflows · \d+ meta-skills\*\*",
    f"**{counts['skill']} skills · {counts['workflow']} workflows · {counts['meta-skill']} meta-skills**",
    readme_text,
    count=1,
)
readme.write_text(readme_text, encoding="utf-8")

taxonomy = ROOT / "docs/skills.md"
taxonomy_text = taxonomy.read_text(encoding="utf-8")
replacements = {
    r"^- `skill`: \d+$": f"- `skill`: {counts['skill']}",
    r"^- `workflow`: \d+$": f"- `workflow`: {counts['workflow']}",
    r"^- `meta-skill`: \d+$": f"- `meta-skill`: {counts['meta-skill']}",
    r"^- Total executable skills: \d+$": f"- Total executable skills: {counts['total']}",
}
for pattern, replacement in replacements.items():
    taxonomy_text = re.sub(pattern, replacement, taxonomy_text, flags=re.MULTILINE)
taxonomy.write_text(taxonomy_text, encoding="utf-8")

classifications_path = ROOT / "catalog/capability-discovery/classifications.json"
classifications = load_json(classifications_path)
for group in classifications["classification_groups"]:
    if group["id"] == "engineering-quality":
        if "clean-code" not in group["capabilities"]:
            group["capabilities"].append("clean-code")
            group["capabilities"].sort()
        group.setdefault("overrides", {})["clean-code"] = {
            "lifecycle_stages": ["build", "verify"],
            "concerns": ["implementation", "code-quality", "review"],
        }
        break
else:
    raise RuntimeError("engineering-quality classification group not found")
write_json(classifications_path, classifications)

topics_path = ROOT / "catalog/capability-discovery/topics.json"
topics = load_json(topics_path)
for topic in topics["topics"]:
    if topic["id"] == "engineering-quality":
        if "clean-code" not in topic["capabilities"]:
            insert_after = "test-driven-development"
            index = topic["capabilities"].index(insert_after) + 1
            topic["capabilities"].insert(index, "clean-code")
        break
else:
    raise RuntimeError("engineering-quality topic not found")
write_json(topics_path, topics)

profiles_path = ROOT / "catalog/capability-discovery/job-profiles.json"
profiles = load_json(profiles_path)
for profile in profiles["job_profiles"]:
    if profile["id"] == "engineering-quality":
        for group in profile["capability_groups"]:
            if group["purpose"] == "Design and implement the technical solution":
                if "clean-code" not in group["optional"]:
                    group["optional"].insert(0, "clean-code")
                break
        else:
            raise RuntimeError("engineering-quality implementation group not found")
        break
else:
    raise RuntimeError("engineering-quality job profile not found")
write_json(profiles_path, profiles)

subprocess.run(["python3", "scripts/verify-capability-inventory.py"], cwd=ROOT, check=True)
subprocess.run(["python3", "scripts/verify-capability-discovery.py"], cwd=ROOT, check=True)
