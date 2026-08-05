from __future__ import annotations

import unittest
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
FLEET_WRAPPER = PACKAGE / "scripts" / "hermes-fleet"
ACCEPTANCE_WRAPPER = PACKAGE / "scripts" / "hermes-fleet-runtime-acceptance"
ACCEPTANCE_RUNNER = PACKAGE / "scripts" / "hermes_fleet_runtime_acceptance.py"
REFERENCE = PACKAGE / "references" / "runtime-validation.md"
FIXTURE = PACKAGE / "tests" / "fixtures" / "runtime-acceptance-pass-with-limitations.json"


class RuntimeAcceptanceInvocationTests(unittest.TestCase):
    def test_standard_wrapper_dispatches_validate_runtime(self) -> None:
        wrapper = FLEET_WRAPPER.read_text(encoding="utf-8")
        self.assertIn("validate-runtime)", wrapper)
        self.assertIn(
            'exec bash "$SCRIPT_DIR/hermes-fleet-runtime-acceptance" "$@"',
            wrapper,
        )

    def test_acceptance_launcher_is_bash_and_resolves_runner(self) -> None:
        text = ACCEPTANCE_WRAPPER.read_text(encoding="utf-8")
        self.assertTrue(text.startswith("#!/usr/bin/env bash"))
        self.assertIn("hermes_fleet_runtime_acceptance.py", text)

    def test_reference_documents_standard_invocation_and_limitations(self) -> None:
        text = REFERENCE.read_text(encoding="utf-8")
        self.assertIn(
            "/hermes-agent-fleet-bootstrap validate-runtime native-ai-engineering",
            text,
        )
        self.assertIn("PASS_WITH_LIMITATIONS", text)
        self.assertIn("agent-security", text)
        self.assertIn("live Telegram round trip", text)
        self.assertIn("provider_backed_specialist_execution_not_verified", text)
        self.assertIn("It must not be called a live gateway PASS", text)

    def test_runner_rejects_secret_fields(self) -> None:
        text = ACCEPTANCE_RUNNER.read_text(encoding="utf-8")
        self.assertIn("PROHIBITED_SECRET_KEYS", text)
        self.assertIn("telegram_token_value_present", text)
        self.assertIn('"credentials_exposed": False', text)

    def test_sanitized_fixture_exists(self) -> None:
        self.assertTrue(FIXTURE.is_file())
        text = FIXTURE.read_text(encoding="utf-8")
        self.assertNotIn('"token"', text)
        self.assertNotIn('"api_key"', text)


if __name__ == "__main__":
    unittest.main()
