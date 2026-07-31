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
                "id": "agent-orchestrator",
                "description": "Coordinates work.",
                "gateway": "eligible",
                "worker_mode": "user_facing_front_door",
                "skills": ["fleet-skill", "router-skill"],
            },
            {
                "id": "agent-review",
                "description": "Reviews work.",
                "gateway": "none",
                "worker_mode": "headless_on_demand",
                "skills": ["review-skill"],
            },
        ]
        self.legacy_ids = ["engineering-orchestrator", "quality-review"]
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
                    "version": "2.0.0",
                    "identity_generation": 2,
                    "topology": "orchestrator_with_specialists",
                    "orchestrator": "agent-orchestrator",
                    "legacy_profile_ids": self.legacy_ids,
                    "mixed_identity_policy": "block_outside_migration",
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

    def run_cli(self, operation: str = "bootstrap", *extra: str) -> int:
        previous = os.environ.get("FAKE_HERMES_LOG")
        os.environ["FAKE_HERMES_LOG"] = str(self.log)
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                return module.main(
                    [
                        operation,
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

    def read_receipt(self) -> dict:
        return json.loads(self.receipt.read_text(encoding="utf-8"))

    def create_profiles(self, profile_ids: list[str]) -> None:
        for profile_id in profile_ids:
            (self.home / "profiles" / profile_id).mkdir(
                parents=True, exist_ok=True
            )

    def test_plan_is_non_mutating(self) -> None:
        code = self.run_cli()
        self.assertEqual(code, module.EXIT_OK)
        self.assertFalse((self.home / "profiles").exists())
        receipt = self.read_receipt()
        self.assertEqual(receipt["mode"], "PLAN_ONLY")
        self.assertEqual(receipt["readiness"], "READY_TO_APPLY")
        self.assertEqual(receipt["fleet_identity_state"], "EMPTY")
        self.assertEqual(receipt["preset_version"], "2.0.0")
        self.assertEqual(receipt["orchestrator_profile"], "agent-orchestrator")
        self.assertFalse(receipt["credentials_copied"])
        self.assertFalse(receipt["live_state_copied"])

    def test_apply_creates_profiles_installs_skills_and_kanban(self) -> None:
        code = self.run_cli("bootstrap", "--apply")
        self.assertEqual(code, module.EXIT_OK)
        for profile_spec in self.profile_specs:
            profile = self.home / "profiles" / profile_spec["id"]
            self.assertTrue(profile.is_dir())
            for skill in profile_spec["skills"]:
                self.assertTrue(
                    (profile / "skills" / skill / "SKILL.md").is_file()
                )
        self.assertTrue((self.home / "kanban.db").is_file())
        receipt = self.read_receipt()
        self.assertEqual(receipt["readiness"], "READY")

    def test_apply_is_idempotent(self) -> None:
        self.assertEqual(
            self.run_cli("bootstrap", "--apply"), module.EXIT_OK
        )
        first_log = self.log.read_text(encoding="utf-8")
        self.log.write_text("", encoding="utf-8")
        self.assertEqual(
            self.run_cli("reconcile", "--apply"), module.EXIT_OK
        )
        second_log = self.log.read_text(encoding="utf-8")
        self.assertIn("profile create", first_log)
        self.assertNotIn("profile create", second_log)
        receipt = self.read_receipt()
        self.assertEqual(
            receipt["fleet_identity_state"], "TARGET_ONLY_COMPLETE"
        )
        statuses = {item["status"] for item in receipt["actions"]}
        self.assertIn("SKIP_EXISTS", statuses)
        self.assertIn("SKIP_IN_SYNC", statuses)

    def test_legacy_only_bootstrap_fails_closed_without_mutation(self) -> None:
        self.create_profiles(self.legacy_ids)
        code = self.run_cli("bootstrap")
        self.assertEqual(code, module.EXIT_PREFLIGHT)
        receipt = self.read_receipt()
        self.assertEqual(
            receipt["fleet_identity_state"], "LEGACY_ONLY_COMPLETE"
        )
        self.assertEqual(receipt["readiness"], "BLOCKED")
        self.assertIn(
            "legacy_fleet_requires_migration", receipt["findings"]
        )
        self.assertFalse(
            (self.home / "profiles" / "agent-orchestrator").exists()
        )

    def test_legacy_partial_reconcile_fails_closed(self) -> None:
        self.create_profiles([self.legacy_ids[0]])
        code = self.run_cli("reconcile")
        self.assertEqual(code, module.EXIT_PREFLIGHT)
        self.assertEqual(
            self.read_receipt()["fleet_identity_state"],
            "LEGACY_ONLY_PARTIAL",
        )

    def test_mixed_bootstrap_fails_closed(self) -> None:
        self.create_profiles(
            [self.legacy_ids[0], self.profile_specs[0]["id"]]
        )
        code = self.run_cli("bootstrap")
        self.assertEqual(code, module.EXIT_PREFLIGHT)
        receipt = self.read_receipt()
        self.assertEqual(receipt["fleet_identity_state"], "MIXED")
        self.assertIn(
            "mixed_identity_fleet_requires_migration",
            receipt["findings"],
        )

    def test_target_partial_reconcile_is_allowed(self) -> None:
        self.create_profiles([self.profile_specs[0]["id"]])
        code = self.run_cli("reconcile")
        self.assertEqual(code, module.EXIT_OK)
        receipt = self.read_receipt()
        self.assertEqual(
            receipt["fleet_identity_state"], "TARGET_ONLY_PARTIAL"
        )
        self.assertEqual(receipt["readiness"], "READY_TO_APPLY")

    def test_audit_detects_empty_target_fleet(self) -> None:
        code = self.run_cli("audit")
        self.assertEqual(code, module.EXIT_NEEDS_WORK)
        self.assertFalse((self.home / "profiles").exists())
        receipt = self.read_receipt()
        self.assertEqual(receipt["fleet_identity_state"], "EMPTY")
        self.assertEqual(receipt["readiness"], "NEEDS_WORK")

    def test_audit_detects_legacy_only_fleet(self) -> None:
        self.create_profiles(self.legacy_ids)
        code = self.run_cli("audit")
        self.assertEqual(code, module.EXIT_NEEDS_WORK)
        receipt = self.read_receipt()
        self.assertEqual(
            receipt["fleet_identity_state"], "LEGACY_ONLY_COMPLETE"
        )
        self.assertIn(
            "legacy_fleet_requires_migration", receipt["findings"]
        )

    def test_audit_detects_mixed_fleet(self) -> None:
        self.create_profiles(
            [self.legacy_ids[0], self.profile_specs[0]["id"]]
        )
        code = self.run_cli("audit")
        self.assertEqual(code, module.EXIT_NEEDS_WORK)
        receipt = self.read_receipt()
        self.assertEqual(receipt["fleet_identity_state"], "MIXED")
        self.assertIn(
            "mixed_identity_fleet_requires_migration",
            receipt["findings"],
        )

    def test_audit_detects_target_partial_fleet(self) -> None:
        self.create_profiles([self.profile_specs[0]["id"]])
        code = self.run_cli("audit")
        self.assertEqual(code, module.EXIT_NEEDS_WORK)
        receipt = self.read_receipt()
        self.assertEqual(
            receipt["fleet_identity_state"], "TARGET_ONLY_PARTIAL"
        )
        self.assertIn("target_fleet_partial", receipt["findings"])

    def test_audit_detects_skill_drift(self) -> None:
        self.assertEqual(
            self.run_cli("bootstrap", "--apply"), module.EXIT_OK
        )
        target = (
            self.home
            / "profiles"
            / "agent-review"
            / "skills"
            / "review-skill"
            / "SKILL.md"
        )
        target.write_text("---\nname: changed\n---\n", encoding="utf-8")
        code = self.run_cli("audit")
        self.assertEqual(code, module.EXIT_NEEDS_WORK)
        receipt = self.read_receipt()
        self.assertEqual(
            receipt["fleet_identity_state"], "TARGET_ONLY_COMPLETE"
        )
        self.assertTrue(
            any(
                finding.startswith("skill_drift:agent-review:review-skill")
                for finding in receipt["findings"]
            )
        )

    def test_missing_skill_fails_before_mutation(self) -> None:
        (self.skills / "review-skill").rename(
            self.skills / "removed-skill"
        )
        code = self.run_cli("bootstrap", "--apply")
        self.assertEqual(code, module.EXIT_PREFLIGHT)
        self.assertFalse((self.home / "profiles").exists())
        self.assertEqual(self.read_receipt()["readiness"], "BLOCKED")

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

    def test_native_preset_has_final_identity_contract(self) -> None:
        preset_path = (
            Path(__file__).resolve().parents[1]
            / "assets"
            / "presets"
            / "native-ai-engineering.json"
        )
        preset = json.loads(preset_path.read_text(encoding="utf-8"))
        module.validate_preset(preset)
        self.assertEqual(preset["version"], "2.0.0")
        self.assertEqual(preset["identity_generation"], 2)
        self.assertEqual(preset["orchestrator"], "agent-orchestrator")
        self.assertEqual(
            [profile["id"] for profile in preset["profiles"]],
            [
                "agent-orchestrator",
                "agent-product",
                "agent-architecture",
                "agent-design",
                "agent-frontend",
                "agent-backend",
                "agent-review",
            ],
        )
        gateways = [
            profile["id"]
            for profile in preset["profiles"]
            if profile["gateway"] == "eligible"
        ]
        self.assertEqual(gateways, ["agent-orchestrator"])
        self.assertTrue(
            all(
                profile["worker_mode"] == "headless_on_demand"
                for profile in preset["profiles"][1:]
            )
        )

    def test_native_preset_references_existing_repository_skills(self) -> None:
        package = Path(__file__).resolve().parents[1]
        skills_root = package.parent
        preset = json.loads(
            (
                package
                / "assets"
                / "presets"
                / "native-ai-engineering.json"
            ).read_text(encoding="utf-8")
        )
        required = sorted(
            {
                skill
                for profile in preset["profiles"]
                for skill in profile["skills"]
            }
        )
        missing = [
            skill
            for skill in required
            if not (skills_root / skill / "SKILL.md").is_file()
        ]
        self.assertEqual(
            missing, [], f"Preset references missing skills: {missing}"
        )

    def test_preset_rejects_path_traversal_identifier(self) -> None:
        malicious = {
            "id": "test-fleet",
            "version": "2.0.0",
            "identity_generation": 2,
            "topology": "orchestrator_with_specialists",
            "orchestrator": "../escape",
            "legacy_profile_ids": [],
            "profiles": [
                {
                    "id": "../escape",
                    "description": "Unsafe profile.",
                    "gateway": "eligible",
                    "skills": ["fleet-skill"],
                }
            ],
        }
        with self.assertRaises(module.FleetError):
            module.validate_preset(malicious)

    def test_preset_rejects_duplicate_skills(self) -> None:
        duplicate = json.loads(self.preset.read_text(encoding="utf-8"))
        duplicate["profiles"][0]["skills"] = [
            "fleet-skill",
            "fleet-skill",
        ]
        with self.assertRaises(module.FleetError):
            module.validate_preset(duplicate)

    def test_preset_rejects_overlapping_legacy_and_target_ids(self) -> None:
        overlap = json.loads(self.preset.read_text(encoding="utf-8"))
        overlap["legacy_profile_ids"] = ["agent-orchestrator"]
        with self.assertRaises(module.FleetError):
            module.validate_preset(overlap)

    def test_preset_rejects_unapproved_mixed_identity_policy(self) -> None:
        invalid = json.loads(self.preset.read_text(encoding="utf-8"))
        invalid["mixed_identity_policy"] = "allow"
        with self.assertRaises(module.FleetError):
            module.validate_preset(invalid)

    def test_symlink_skill_source_is_rejected_before_mutation(self) -> None:
        source = self.skills / "review-skill"
        external = self.tmp / "external-review-skill"
        source.rename(external)
        try:
            source.symlink_to(external, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("Symlinks are unavailable on this platform")
        code = self.run_cli("bootstrap", "--apply")
        self.assertEqual(code, module.EXIT_PREFLIGHT)
        self.assertFalse((self.home / "profiles").exists())
        receipt = self.read_receipt()
        self.assertEqual(receipt["readiness"], "BLOCKED")
        self.assertTrue(
            any("Symlink" in item for item in receipt["findings"])
        )

    def test_profile_command_failure_is_reported(self) -> None:
        self.write_fake_hermes(fail_profile=True)
        code = self.run_cli("bootstrap", "--apply")
        self.assertEqual(code, module.EXIT_EXECUTION)
        receipt = self.read_receipt()
        self.assertEqual(receipt["readiness"], "BLOCKED")
        self.assertTrue(
            any(
                "profile_create_failed" in finding
                for finding in receipt["findings"]
            )
        )


if __name__ == "__main__":
    unittest.main()
