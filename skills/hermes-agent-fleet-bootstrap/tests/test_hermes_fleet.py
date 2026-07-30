from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "hermes_fleet.py"
spec = importlib.util.spec_from_file_location("hermes_fleet", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class HermesFleetTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())
        self.skills = self.tmp / "skills"
        self.home = self.tmp / "hermes-home"
        self.receipt = self.tmp / "receipt.json"
        self.preset = self.tmp / "preset.json"
        self.log = self.tmp / "hermes.log"
        self.hermes = self.tmp / "hermes"
        self.profile_specs = [
            {
                "id": "engineering-orchestrator",
                "description": "Coordinates work.",
                "gateway": "eligible",
                "skills": ["fleet-skill", "router-skill"],
            },
            {
                "id": "quality-review",
                "description": "Reviews work.",
                "gateway": "none",
                "skills": ["review-skill"],
            },
        ]
        self.write_preset()
        for skill in ["fleet-skill", "router-skill", "review-skill"]:
            path = self.skills / skill
            path.mkdir(parents=True)
            (path / "SKILL.md").write_text(
                f"---\nname: {skill}\n---\n", encoding="utf-8"
            )
        self.write_fake_hermes()

    def write_preset(self) -> None:
        self.preset.write_text(
            json.dumps(
                {
                    "id": "test-fleet",
                    "version": "1.0.0",
                    "topology": "orchestrator_with_specialists",
                    "orchestrator": "engineering-orchestrator",
                    "kanban": {"initialize": True},
                    "profiles": self.profile_specs,
                }
            ),
            encoding="utf-8",
        )

    def write_fake_hermes(self, fail_profile: bool = False) -> None:
        fail = "1" if fail_profile else "0"
        self.hermes.write_text(
            f'''#!/usr/bin/env python3
import os, pathlib, sys
home = pathlib.Path(os.environ["HERMES_HOME"])
log = pathlib.Path(os.environ["FAKE_HERMES_LOG"])
with log.open("a", encoding="utf-8") as handle:
    handle.write(" ".join(sys.argv[1:]) + "\\n")
args = sys.argv[1:]
if args == ["--version"]:
    print("Hermes Agent v-test")
    raise SystemExit(0)
if args[:2] == ["profile", "create"]:
    if {fail}:
        print("profile create failed", file=sys.stderr)
        raise SystemExit(9)
    (home / "profiles" / args[2]).mkdir(parents=True, exist_ok=True)
    raise SystemExit(0)
if args[:2] == ["kanban", "init"]:
    home.mkdir(parents=True, exist_ok=True)
    (home / "kanban.db").write_text("test", encoding="utf-8")
    raise SystemExit(0)
raise SystemExit(0)
''',
            encoding="utf-8",
        )
        self.hermes.chmod(0o755)

    def run_cli(self, *extra: str) -> int:
        previous = os.environ.get("FAKE_HERMES_LOG")
        os.environ["FAKE_HERMES_LOG"] = str(self.log)
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                return module.main(
                    [
                        "bootstrap",
                        "test-fleet",
                        "--preset-file",
                        str(self.preset),
                        "--skills-root",
                        str(self.skills),
                        "--hermes-home",
                        str(self.home),
                        "--hermes-bin",
                        str(self.hermes),
                        "--receipt",
                        str(self.receipt),
                        "--json",
                        *extra,
                    ]
                )
        finally:
            if previous is None:
                os.environ.pop("FAKE_HERMES_LOG", None)
            else:
                os.environ["FAKE_HERMES_LOG"] = previous

    def test_plan_is_non_mutating(self) -> None:
        code = self.run_cli()
        self.assertEqual(code, module.EXIT_OK)
        self.assertFalse((self.home / "profiles").exists())
        receipt = json.loads(self.receipt.read_text(encoding="utf-8"))
        self.assertEqual(receipt["mode"], "PLAN_ONLY")
        self.assertEqual(receipt["readiness"], "READY_TO_APPLY")

    def test_apply_creates_profiles_installs_skills_and_kanban(self) -> None:
        code = self.run_cli("--apply")
        self.assertEqual(code, module.EXIT_OK)
        for spec in self.profile_specs:
            profile = self.home / "profiles" / spec["id"]
            self.assertTrue(profile.is_dir())
            for skill in spec["skills"]:
                self.assertTrue((profile / "skills" / skill / "SKILL.md").is_file())
        self.assertTrue((self.home / "kanban.db").is_file())
        receipt = json.loads(self.receipt.read_text(encoding="utf-8"))
        self.assertEqual(receipt["readiness"], "READY")

    def test_apply_is_idempotent(self) -> None:
        self.assertEqual(self.run_cli("--apply"), module.EXIT_OK)
        first_log = self.log.read_text(encoding="utf-8")
        self.log.write_text("", encoding="utf-8")
        self.assertEqual(self.run_cli("--apply"), module.EXIT_OK)
        second_log = self.log.read_text(encoding="utf-8")
        self.assertIn("profile create", first_log)
        self.assertNotIn("profile create", second_log)
        receipt = json.loads(self.receipt.read_text(encoding="utf-8"))
        statuses = {item["status"] for item in receipt["actions"]}
        self.assertIn("SKIP_EXISTS", statuses)
        self.assertIn("SKIP_IN_SYNC", statuses)

    def test_missing_skill_fails_before_mutation(self) -> None:
        (self.skills / "review-skill").rename(self.skills / "removed-skill")
        code = self.run_cli("--apply")
        self.assertEqual(code, module.EXIT_PREFLIGHT)
        self.assertFalse((self.home / "profiles").exists())
        receipt = json.loads(self.receipt.read_text(encoding="utf-8"))
        self.assertEqual(receipt["readiness"], "BLOCKED")

    def test_missing_hermes_fails_apply(self) -> None:
        with contextlib.redirect_stdout(io.StringIO()):
            code = module.main(
                [
                    "bootstrap",
                    "test-fleet",
                    "--apply",
                    "--preset-file",
                    str(self.preset),
                    "--skills-root",
                    str(self.skills),
                    "--hermes-home",
                    str(self.home),
                    "--hermes-bin",
                    str(self.tmp / "missing-hermes"),
                    "--receipt",
                    str(self.receipt),
                    "--json",
                ]
            )
        self.assertEqual(code, module.EXIT_PREFLIGHT)
        self.assertFalse((self.home / "profiles").exists())

    def test_audit_reports_missing_profiles_without_mutation(self) -> None:
        with contextlib.redirect_stdout(io.StringIO()):
            code = module.main(
                [
                    "audit",
                    "test-fleet",
                    "--preset-file",
                    str(self.preset),
                    "--skills-root",
                    str(self.skills),
                    "--hermes-home",
                    str(self.home),
                    "--receipt",
                    str(self.receipt),
                    "--json",
                ]
            )
        self.assertEqual(code, module.EXIT_NEEDS_WORK)
        self.assertFalse((self.home / "profiles").exists())
        receipt = json.loads(self.receipt.read_text(encoding="utf-8"))
        self.assertEqual(receipt["readiness"], "NEEDS_WORK")

    def test_native_preset_has_one_gateway_and_unique_profiles(self) -> None:
        preset_path = (
            Path(__file__).resolve().parents[1]
            / "assets"
            / "presets"
            / "native-ai-engineering.json"
        )
        preset = json.loads(preset_path.read_text(encoding="utf-8"))
        module.validate_preset(preset)
        self.assertEqual(preset["orchestrator"], "engineering-orchestrator")
        gateways = [
            profile["id"]
            for profile in preset["profiles"]
            if profile["gateway"] == "eligible"
        ]
        self.assertEqual(gateways, ["engineering-orchestrator"])

    def test_native_preset_references_existing_repository_skills(self) -> None:
        package = Path(__file__).resolve().parents[1]
        skills_root = package.parent
        preset = json.loads(
            (package / "assets" / "presets" / "native-ai-engineering.json").read_text(
                encoding="utf-8"
            )
        )
        required = sorted(
            {skill for profile in preset["profiles"] for skill in profile["skills"]}
        )
        missing = [
            skill for skill in required if not (skills_root / skill / "SKILL.md").is_file()
        ]
        self.assertEqual(missing, [], f"Preset references missing skills: {missing}")

    def test_profile_command_failure_is_reported(self) -> None:
        self.write_fake_hermes(fail_profile=True)
        code = self.run_cli("--apply")
        self.assertEqual(code, module.EXIT_EXECUTION)
        receipt = json.loads(self.receipt.read_text(encoding="utf-8"))
        self.assertEqual(receipt["readiness"], "BLOCKED")
        self.assertTrue(
            any("profile_create_failed" in finding for finding in receipt["findings"])
        )


if __name__ == "__main__":
    unittest.main()
