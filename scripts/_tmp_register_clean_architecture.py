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
text = readme.read_text(encoding="utf-8")
text = re.sub(
    r"\*\*\d+ skills · \d+ workflows · \d+ meta-skills\*\*",
    f"**{counts['skill']} skills · {counts['workflow']} workflows · {counts['meta-skill']} meta-skills**",
    text,
    count=1,
)
readme.write_text(text, encoding="utf-8")

taxonomy = ROOT / "docs/skills.md"
text = taxonomy.read_text(encoding="utf-8")
for pattern, replacement in {
    r"^- `skill`: \d+$": f"- `skill`: {counts['skill']}",
    r"^- `workflow`: \d+$": f"- `workflow`: {counts['workflow']}",
    r"^- `meta-skill`: \d+$": f"- `meta-skill`: {counts['meta-skill']}",
    r"^- Total executable skills: \d+$": f"- Total executable skills: {counts['total']}",
}.items():
    text = re.sub(pattern, replacement, text, flags=re.MULTILINE)
taxonomy.write_text(text, encoding="utf-8")

classifications_path = ROOT / "catalog/capability-discovery/classifications.json"
classifications = load_json(classifications_path)
for group in classifications["classification_groups"]:
    if group["id"] == "domain-architecture":
        if "clean-architecture" not in group["capabilities"]:
            group["capabilities"].append("clean-architecture")
            group["capabilities"].sort()
        group.setdefault("overrides", {})["clean-architecture"] = {
            "lifecycle_stages": ["design", "build", "verify"],
            "concerns": ["architecture", "implementation", "testing"],
        }
        break
else:
    raise RuntimeError("domain-architecture classification group not found")
write_json(classifications_path, classifications)

topics_path = ROOT / "catalog/capability-discovery/topics.json"
topics = load_json(topics_path)
for topic in topics["topics"]:
    if topic["id"] == "software-architecture" and "clean-architecture" not in topic["capabilities"]:
        index = topic["capabilities"].index("architecture-review") + 1
        topic["capabilities"].insert(index, "clean-architecture")
    if topic["id"] == "engineering-quality" and "clean-architecture" not in topic["capabilities"]:
        index = topic["capabilities"].index("solid-design") + 1
        topic["capabilities"].insert(index, "clean-architecture")
write_json(topics_path, topics)

profiles_path = ROOT / "catalog/capability-discovery/job-profiles.json"
profiles = load_json(profiles_path)
for profile in profiles["job_profiles"]:
    if profile["id"] == "engineering-quality":
        for group in profile["capability_groups"]:
            if group["purpose"] == "Design and implement the technical solution":
                if "clean-architecture" not in group["optional"]:
                    anchor = group["optional"].index("solid-design") if "solid-design" in group["optional"] else 0
                    group["optional"].insert(anchor, "clean-architecture")
                break
        break
write_json(profiles_path, profiles)

subprocess.run(["python3", "scripts/verify-capability-inventory.py"], cwd=ROOT, check=True)
subprocess.run(["python3", "scripts/verify-capability-discovery.py"], cwd=ROOT, check=True)
