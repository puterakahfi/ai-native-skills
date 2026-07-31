#!/usr/bin/env python3
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "scripts" / "hermes_fleet_migrate.py"
SPEC = importlib.util.spec_from_file_location("hermes_fleet_migrate", RUNNER)
assert SPEC and SPEC.loader
migration = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = migration
SPEC.loader.exec_module(migration)


class FakeHermes:
    def __init__(self, home: Path):
        self.home = home
        self.commands: list[list[str]] = []

    def __call__(self, command: list[str], env: dict[str, str]) -> subprocess.CompletedProcess[str]:
        self.commands.append(command)
        args = command[1:]
        stdout = ""
        stderr = ""
        code = 0

        if args == ["--version"]:
            stdout = "Hermes 0.19-test\n"
        elif args[:2] == ["profile", "show"]:
            profile = self.home / "profiles" / args[2]
            if not profile.is_dir():
                code = 2
            else:
                status_file = profile / "gateway.status"
                status = status_file.read_text().strip() if status_file.exists() else "stopped"
                stdout = f"Profile: {args[2]}\nGateway: {status}\n"
        elif len(args) == 4 and args[0] == "-p" and args[2:] == ["gateway", "stop"]:
            profile = self.home / "profiles" / args[1]
            (profile / "gateway.status").write_text("stopped", encoding="utf-8")
            stdout = "stopped\n"
        elif args[:2] == ["profile", "export"]:
            output = Path(args[args.index("-o") + 1])
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(b"profile-export")
            stdout = str(output)
        elif args[:2] == ["profile", "rename"]:
            source = self.home / "profiles" / args[2]
            target = self.home / "profiles" / args[3]
            source.rename(target)
            stdout = "renamed\n"
        elif args[:2] == ["profile", "describe"]:
            profile = self.home / "profiles" / args[2]
            description = args[args.index("--text") + 1]
            (profile / "profile.yaml").write_text(
                f"description: {description}\n", encoding="utf-8"
            )
        else:
            code = 2
            stderr = f"unsupported command: {command}"

        return subprocess.CompletedProcess(command, code, stdout, stderr)


class MigrationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.home = self.root / "hermes"
        self.skills = self.root / "skills"
        for skill in ("skill-a", "skill-b"):
            path = self.skills / skill
            path.mkdir(parents=True)
            (path / "SKILL.md").write_text(f"# {skill}\n", encoding="utf-8")

        self.preset = {
            "id": "test-fleet",
            "version": "2.0.0",
            "identity_generation": 2,
            "topology": "orchestrator_with_specialists",
            "orchestrator": "agent-orchestrator",
            "legacy_profile_ids": ["legacy-orchestrator", "legacy-worker"],
            "mixed_identity_policy": "block_outside_migration",
            "profiles": [
                {
                    "id": "agent-orchestrator",
                    "description": "Coordinates work.",
                    "gateway": "eligible",
                    "skills": ["skill-a"],
                },
                {
                    "id": "agent-worker",
                    "description": "Performs bounded work.",
                    "gateway": "none",
                    "skills": ["skill-b"],
                },
            ],
        }
        self.identity_map = {
            "schema_version": "1.1",
            "fleet": "test-fleet",
            "status": "EXECUTABLE_NATIVE_RENAME",
            "from_preset_major": 1,
            "to_preset_major": 2,
            "mappings": [
                {
                    "legacy_profile": "legacy-orchestrator",
                    "target_profile": "agent-orchestrator",
                },
                {
                    "legacy_profile": "legacy-worker",
                    "target_profile": "agent-worker",
                },
            ],
        }
        self.preset_path = self.root / "preset.json"
        self.map_path = self.root / "map.json"
        self.preset_path.write_text(json.dumps(self.preset), encoding="utf-8")
        self.map_path.write_text(json.dumps(self.identity_map), encoding="utf-8")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def make_profile(self, name: str, gateway: str = "stopped") -> Path:
        profile = self.home / "profiles" / name
        profile.mkdir(parents=True)
        (profile / "gateway.status").write_text(gateway, encoding="utf-8")
        (profile / "skills").mkdir()
        return profile

    def argv(self, *extra: str) -> list[str]:
        return [
            "test-fleet",
            "--preset-file",
            str(self.preset_path),
            "--identity-map-file",
            str(self.map_path),
            "--skills-root",
            str(self.skills),
            "--hermes-home",
            str(self.home),
            "--hermes-bin",
            "hermes-test",
            "--receipt",
            str(self.root / "receipt.json"),
            "--json",
            *extra,
        ]

    def run_main(self, fake: FakeHermes, *extra: str) -> tuple[int, dict]:
        reconcile_receipt = self.root / "reconcile.json"

        def reconcile(*args, **kwargs):
            reconcile_receipt.write_text('{"readiness":"READY"}\n', encoding="utf-8")
            return True, ["reconcile"], ""

        stream = io.StringIO()
        with mock.patch.object(migration, "resolve_executable", return_value="hermes-test"), mock.patch.object(
            migration, "run_command", side_effect=fake
        ), mock.patch.object(migration, "reconcile_skills", side_effect=reconcile), contextlib.redirect_stdout(stream):
            code = migration.main(self.argv(*extra))
        return code, json.loads(stream.getvalue())

    def test_plan_is_read_only_and_reports_state_presence_only(self) -> None:
        profile = self.make_profile("legacy-orchestrator")
        self.make_profile("legacy-worker")
        (profile / ".env").write_text("TOKEN=top-secret", encoding="utf-8")
        (profile / "memory").mkdir()
        fake = FakeHermes(self.home)

        code, receipt = self.run_main(fake)

        self.assertEqual(code, migration.EXIT_OK)
        self.assertEqual(receipt["readiness"], "READY_TO_APPLY")
        self.assertEqual(receipt["identity_state"], "LEGACY_ONLY_COMPLETE")
        self.assertTrue((self.home / "profiles" / "legacy-orchestrator").exists())
        self.assertEqual(fake.commands, [])
        rendered = json.dumps(receipt)
        self.assertNotIn("top-secret", rendered)
        self.assertTrue(receipt["actions"][0]["inventory"]["environment"])
        self.assertTrue(receipt["actions"][0]["inventory"]["memory"])

    def test_apply_renames_in_place_and_preserves_live_state(self) -> None:
        orchestrator = self.make_profile("legacy-orchestrator")
        worker = self.make_profile("legacy-worker")
        for profile in (orchestrator, worker):
            (profile / ".env").write_text("TOKEN=preserved", encoding="utf-8")
            (profile / "memory").mkdir()
            (profile / "sessions").mkdir()
            (profile / "custom.txt").write_text("keep", encoding="utf-8")
        fake = FakeHermes(self.home)

        code, receipt = self.run_main(fake, "--apply")

        self.assertEqual(code, migration.EXIT_OK)
        self.assertEqual(receipt["readiness"], "READY")
        self.assertEqual(len(receipt["profiles_renamed"]), 2)
        target = self.home / "profiles" / "agent-orchestrator"
        self.assertTrue(target.is_dir())
        self.assertFalse((self.home / "profiles" / "legacy-orchestrator").exists())
        self.assertEqual((target / ".env").read_text(), "TOKEN=preserved")
        self.assertTrue((target / "memory").is_dir())
        self.assertTrue((target / "sessions").is_dir())
        self.assertEqual((target / "custom.txt").read_text(), "keep")
        self.assertEqual(len(receipt["backup_archives"]), 2)
        self.assertFalse(receipt["credentials_copied"])
        self.assertFalse(receipt["live_state_copied"])
        self.assertTrue(receipt["live_state_preserved_in_place"])

    def test_running_gateway_requires_explicit_stop_authority(self) -> None:
        self.make_profile("legacy-orchestrator", gateway="running")
        self.make_profile("legacy-worker")
        fake = FakeHermes(self.home)

        code, receipt = self.run_main(fake, "--apply")
        self.assertEqual(code, migration.EXIT_PREFLIGHT)
        self.assertEqual(receipt["actions"][0]["status"], "BLOCKED_GATEWAY_NOT_STOPPED")
        self.assertTrue((self.home / "profiles" / "legacy-orchestrator").exists())

        code, receipt = self.run_main(fake, "--apply", "--stop-gateways")
        self.assertEqual(code, migration.EXIT_OK)
        self.assertTrue((self.home / "profiles" / "agent-orchestrator").exists())
        self.assertFalse(receipt["gateway_started"])

    def test_both_present_conflict_fails_closed(self) -> None:
        self.make_profile("legacy-orchestrator")
        self.make_profile("agent-orchestrator")
        self.make_profile("legacy-worker")
        fake = FakeHermes(self.home)

        code, receipt = self.run_main(fake)

        self.assertEqual(code, migration.EXIT_PREFLIGHT)
        self.assertEqual(receipt["identity_state"], "BLOCKED_AMBIGUOUS")
        self.assertIn(
            "both_profiles_present:legacy-orchestrator:agent-orchestrator",
            receipt["findings"],
        )

    def test_missing_both_sides_fails_closed(self) -> None:
        self.make_profile("legacy-orchestrator")
        fake = FakeHermes(self.home)

        code, receipt = self.run_main(fake)

        self.assertEqual(code, migration.EXIT_PREFLIGHT)
        self.assertIn("both_profiles_missing:legacy-worker:agent-worker", receipt["findings"])

    def test_mixed_non_conflicting_state_is_resumable(self) -> None:
        self.make_profile("agent-orchestrator")
        self.make_profile("legacy-worker")
        fake = FakeHermes(self.home)

        code, receipt = self.run_main(fake, "--apply")

        self.assertEqual(code, migration.EXIT_OK)
        self.assertEqual(receipt["identity_state"], "MIXED_RESUMABLE")
        self.assertEqual(receipt["profiles_preserved"], ["agent-orchestrator"])
        self.assertTrue((self.home / "profiles" / "agent-worker").exists())

    def test_repeated_apply_is_idempotent(self) -> None:
        self.make_profile("legacy-orchestrator")
        self.make_profile("legacy-worker")
        fake = FakeHermes(self.home)

        first_code, _ = self.run_main(fake, "--apply")
        second_code, second = self.run_main(fake, "--apply")

        self.assertEqual(first_code, migration.EXIT_OK)
        self.assertEqual(second_code, migration.EXIT_OK)
        self.assertEqual(second["identity_state"], "TARGET_ONLY_COMPLETE")
        self.assertEqual(second["profiles_renamed"], [])
        self.assertEqual(
            second["profiles_preserved"], ["agent-orchestrator", "agent-worker"]
        )

    def test_symlinked_profile_fails_closed(self) -> None:
        profiles = self.home / "profiles"
        profiles.mkdir(parents=True)
        external = self.root / "external"
        external.mkdir()
        (profiles / "legacy-orchestrator").symlink_to(external, target_is_directory=True)
        self.make_profile("legacy-worker")
        fake = FakeHermes(self.home)

        code, receipt = self.run_main(fake)

        self.assertEqual(code, migration.EXIT_PREFLIGHT)
        self.assertTrue(any("Symlinked legacy profile directory" in item for item in receipt["findings"]))

    def test_mapping_order_mismatch_is_rejected(self) -> None:
        broken = dict(self.identity_map)
        broken["mappings"] = list(reversed(self.identity_map["mappings"]))
        self.map_path.write_text(json.dumps(broken), encoding="utf-8")
        fake = FakeHermes(self.home)

        code, receipt = self.run_main(fake)

        self.assertEqual(code, migration.EXIT_PREFLIGHT)
        self.assertTrue(any("legacy order" in item for item in receipt["findings"]))


if __name__ == "__main__":
    unittest.main()
