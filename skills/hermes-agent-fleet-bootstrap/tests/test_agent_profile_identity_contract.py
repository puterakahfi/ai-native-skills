from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

import yaml


TEST_FILE = Path(__file__).resolve()
PACKAGE_ROOT = TEST_FILE.parents[1]
SKILLS_ROOT = TEST_FILE.parents[2]
REPOSITORY_ROOT = TEST_FILE.parents[3]
CATALOG_ROOT = REPOSITORY_ROOT / "catalog"
REFERENCE_PATH = PACKAGE_ROOT / "references" / "profile-archetypes.md"
PRESET_PATH = PACKAGE_ROOT / "assets" / "presets" / "native-ai-engineering.json"
MAPPING_PATH = (
    PACKAGE_ROOT
    / "assets"
    / "profile-identity-maps"
    / "native-ai-engineering-v1-to-v2.json"
)
INVENTORY_PATH = REPOSITORY_ROOT / "docs" / "capability-inventory.json"

TARGET_IDS = {
    "agent-orchestrator",
    "agent-product",
    "agent-architecture",
    "agent-design",
    "agent-frontend",
    "agent-backend",
    "agent-review",
}
LEGACY_IDS = {
    "engineering-orchestrator",
    "product-development",
    "solution-architecture",
    "product-design",
    "frontend-engineering",
    "backend-platform",
    "quality-review",
}
REQUIRED_CONTRACT_FIELDS = {
    "id",
    "legacy_id",
    "responsibility_domain",
    "mission",
    "owns",
    "does_not_own",
    "required_inputs",
    "outputs",
    "handoffs",
    "gateway_policy",
    "worker_mode",
    "memory_scope",
    "completion_evidence",
    "skills_required",
    "skills_optional",
}


def parse_default_contracts(markdown: str) -> dict[str, dict]:
    pattern = re.compile(
        r"## `(?P<heading>agent-(?:orchestrator|product|architecture|design|frontend|backend|review))`"
        r"\n\n```yaml\n(?P<body>.*?)\n```",
        re.DOTALL,
    )
    contracts: dict[str, dict] = {}
    for match in pattern.finditer(markdown):
        heading = match.group("heading")
        contract = yaml.safe_load(match.group("body"))
        if not isinstance(contract, dict):
            raise AssertionError(f"Contract for {heading} must be a mapping")
        contracts[heading] = contract
    return contracts


def flattened(values: list[object]) -> str:
    return " ".join(str(value).lower() for value in values)


class AgentProfileIdentityContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.reference = REFERENCE_PATH.read_text(encoding="utf-8")
        cls.mapping = json.loads(MAPPING_PATH.read_text(encoding="utf-8"))
        cls.preset = json.loads(PRESET_PATH.read_text(encoding="utf-8"))
        cls.inventory = json.loads(INVENTORY_PATH.read_text(encoding="utf-8"))
        cls.catalog_names = {item["name"] for item in cls.inventory["items"]}
        cls.catalog_capabilities = {
            manifest.parent.name for manifest in CATALOG_ROOT.glob("*/manifest.yaml")
        }
        cls.active_preset_skills = {
            skill
            for profile in cls.preset["profiles"]
            for skill in profile["skills"]
        }
        cls.contracts = parse_default_contracts(cls.reference)
        cls.mappings = cls.mapping["mappings"]

    def test_target_identity_set_and_naming_contract_are_explicit(self) -> None:
        self.assertEqual(set(self.contracts), TARGET_IDS)
        self.assertEqual(
            self.mapping["naming_contract"]["form"],
            "agent-<stable-responsibility-domain>",
        )
        pattern = re.compile(self.mapping["naming_contract"]["pattern"])
        self.assertTrue(all(pattern.fullmatch(profile_id) for profile_id in TARGET_IDS))
        self.assertEqual(self.mapping["fleet"], "native-ai-engineering")
        self.assertEqual(self.mapping["from_preset_major"], 1)
        self.assertEqual(self.mapping["to_preset_major"], 2)
        self.assertEqual(self.mapping["status"], "EXECUTABLE_NATIVE_RENAME")
        self.assertEqual(
            self.mapping["migration_strategy"], "NATIVE_IN_PLACE_RENAME"
        )

    def test_legacy_mapping_is_complete_unique_and_one_to_one(self) -> None:
        legacy = [item["legacy_profile"] for item in self.mappings]
        target = [item["target_profile"] for item in self.mappings]
        self.assertEqual(set(legacy), LEGACY_IDS)
        self.assertEqual(set(target), TARGET_IDS)
        self.assertEqual(len(legacy), len(set(legacy)))
        self.assertEqual(len(target), len(set(target)))
        for item in self.mappings:
            contract = self.contracts[item["target_profile"]]
            self.assertEqual(contract["legacy_id"], item["legacy_profile"])
            self.assertEqual(
                contract["responsibility_domain"], item["responsibility_domain"]
            )
            self.assertEqual(contract["gateway_policy"], item["gateway_policy"])

    def test_every_default_agent_has_a_complete_responsibility_contract(self) -> None:
        for profile_id, contract in self.contracts.items():
            self.assertEqual(contract["id"], profile_id)
            self.assertTrue(REQUIRED_CONTRACT_FIELDS.issubset(contract))
            for field in (
                "owns",
                "does_not_own",
                "required_inputs",
                "outputs",
                "handoffs",
                "completion_evidence",
                "skills_required",
                "skills_optional",
            ):
                self.assertIsInstance(contract[field], list, f"{profile_id}.{field}")
            self.assertTrue(contract["mission"].strip())
            self.assertTrue(contract["owns"])
            self.assertTrue(contract["does_not_own"])
            self.assertTrue(contract["required_inputs"])
            self.assertTrue(contract["outputs"])
            self.assertTrue(contract["completion_evidence"])

    def test_only_orchestrator_is_gateway_eligible(self) -> None:
        self.assertEqual(
            self.mapping["default_gateway_profile"], "agent-orchestrator"
        )
        self.assertEqual(
            self.contracts["agent-orchestrator"]["gateway_policy"],
            "orchestrator_only",
        )
        self.assertEqual(
            self.contracts["agent-orchestrator"]["worker_mode"],
            "user_facing_front_door",
        )
        for profile_id, contract in self.contracts.items():
            if profile_id == "agent-orchestrator":
                continue
            self.assertEqual(contract["gateway_policy"], "none")
            self.assertEqual(contract["worker_mode"], "headless_on_demand")

    def test_orchestrator_coordinates_without_absorbing_authority(self) -> None:
        orchestrator = self.contracts["agent-orchestrator"]
        owns = flattened(orchestrator["owns"])
        exclusions = flattened(orchestrator["does_not_own"])
        for phrase in (
            "primary workflow",
            "work decomposition",
            "specialist selection",
            "evidence synthesis",
            "originating gateway",
        ):
            self.assertIn(phrase, owns)
        for phrase in (
            "product priority",
            "architecture approval",
            "primary implementation",
            "independent review verdict",
            "merge",
            "deployment",
            "product acceptance",
        ):
            self.assertIn(phrase, exclusions)

    def test_authority_is_partitioned_by_responsibility(self) -> None:
        product_owns = flattened(self.contracts["agent-product"]["owns"])
        architecture_owns = flattened(self.contracts["agent-architecture"]["owns"])
        design_owns = flattened(self.contracts["agent-design"]["owns"])
        frontend_owns = flattened(self.contracts["agent-frontend"]["owns"])
        backend_owns = flattened(self.contracts["agent-backend"]["owns"])

        self.assertIn("product acceptance criteria", product_owns)
        self.assertIn("architecture decision records", architecture_owns)
        self.assertIn("design acceptance criteria", design_owns)
        self.assertIn("component and interaction implementation", frontend_owns)
        self.assertIn("domain and application service implementation", backend_owns)

        for profile_id, contract in self.contracts.items():
            if profile_id != "agent-product":
                self.assertNotIn("product acceptance criteria", flattened(contract["owns"]))
            if profile_id != "agent-architecture":
                self.assertNotIn("architecture decision records", flattened(contract["owns"]))
            if profile_id != "agent-design":
                self.assertNotIn("design acceptance criteria", flattened(contract["owns"]))

    def test_review_agent_is_independent_from_primary_implementation(self) -> None:
        review = self.contracts["agent-review"]
        self.assertIn("normalized quality verdict", flattened(review["owns"]))
        self.assertIn(
            "primary feature or bugfix implementation",
            flattened(review["does_not_own"]),
        )
        self.assertIn(
            "reviewer-independence disclosure",
            flattened(review["completion_evidence"]),
        )
        forbidden = {
            "new-feature-workflow",
            "bugfix-workflow",
            "git-workflow",
            "test-driven-development",
            "refactoring",
            "product-manager",
            "product-requirements",
        }
        review_skills = set(review["skills_required"]) | set(review["skills_optional"])
        self.assertTrue(review_skills.isdisjoint(forbidden))

    def test_orchestrator_only_capabilities_do_not_leak_to_workers(self) -> None:
        routing = {
            "hermes-agent-fleet-bootstrap",
            "hermes-profile-bootstrap",
            "workflow-router",
            "role-switcher",
            "hermes-task-management-workflow",
        }
        orchestrator_skills = set(self.contracts["agent-orchestrator"]["skills_required"])
        self.assertTrue(routing.issubset(orchestrator_skills))
        for profile_id, contract in self.contracts.items():
            if profile_id == "agent-orchestrator":
                continue
            skills = set(contract["skills_required"]) | set(contract["skills_optional"])
            self.assertTrue(
                skills.isdisjoint(routing),
                f"{profile_id} must not absorb orchestrator-only capabilities",
            )

    def test_contract_capabilities_resolve_and_active_manifests_remain_curated(self) -> None:
        catalog_size = len(self.catalog_names)
        for profile_id, contract in self.contracts.items():
            required = set(contract["skills_required"])
            optional = set(contract["skills_optional"])
            capabilities = contract["skills_required"] + contract["skills_optional"]
            self.assertEqual(len(capabilities), len(set(capabilities)), profile_id)
            self.assertLess(len(capabilities), catalog_size / 2, profile_id)

            missing_required_catalog = sorted(required - self.catalog_names)
            missing_required_package = sorted(
                skill
                for skill in required
                if not (SKILLS_ROOT / skill / "SKILL.md").is_file()
            )
            unresolved_optional = sorted(
                optional - self.catalog_names - self.catalog_capabilities
            )
            optional_skill_packages_missing = sorted(
                skill
                for skill in optional
                if skill not in self.catalog_capabilities
                and not (SKILLS_ROOT / skill / "SKILL.md").is_file()
            )
            catalog_only_optional = optional & self.catalog_capabilities - self.catalog_names

            self.assertEqual(missing_required_catalog, [], profile_id)
            self.assertEqual(missing_required_package, [], profile_id)
            self.assertEqual(unresolved_optional, [], profile_id)
            self.assertEqual(optional_skill_packages_missing, [], profile_id)
            self.assertTrue(
                catalog_only_optional.isdisjoint(self.active_preset_skills),
                f"{profile_id} catalog-only capabilities must not be materialized as skills",
            )

    def test_product_framework_and_method_names_are_negative_examples(self) -> None:
        invalid = set(self.mapping["naming_contract"]["invalid_examples"])
        self.assertTrue(
            {
                "agent-react",
                "agent-nextjs",
                "agent-tailwind",
                "agent-tdd",
                "agent-ddd",
                "agent-solid",
                "agent-visualmate",
                "agent-product-a",
            }.issubset(invalid)
        )
        self.assertTrue(TARGET_IDS.isdisjoint(invalid))
        self.assertIn("Products and repositories remain task context", self.reference)
        self.assertIn("product: product-a", self.reference)
        self.assertIn("repository: ~/projects/product-a", self.reference)

    def test_migration_contract_prohibits_secret_and_live_state_copy(self) -> None:
        self.assertEqual(
            self.mapping["legacy_retirement"],
            "NOT_REQUIRED_AFTER_SUCCESSFUL_RENAME",
        )
        self.assertEqual(
            self.mapping["automatic_live_state_copy"], "PROHIBITED"
        )
        self.assertEqual(
            self.mapping["native_in_place_state_preservation"], "REQUIRED"
        )
        prohibited = set(self.mapping["prohibited_automatic_copy"])
        self.assertTrue(
            {
                ".env",
                "auth.json",
                "api_keys",
                "oauth_tokens",
                "telegram_tokens",
                "credentials",
                "memory",
                "sessions",
                "cron_state",
                "kanban_databases",
                "runtime_databases",
                "gateway_state",
            }.issubset(prohibited)
        )
        orchestrator_mapping = next(
            item
            for item in self.mappings
            if item["target_profile"] == "agent-orchestrator"
        )
        self.assertEqual(
            orchestrator_mapping["gateway_transition"],
            "PRESERVE_STOPPED_IN_PLACE",
        )


if __name__ == "__main__":
    unittest.main()
