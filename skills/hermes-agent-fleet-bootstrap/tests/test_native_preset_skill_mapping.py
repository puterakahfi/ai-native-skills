from __future__ import annotations

import json
import unittest
from pathlib import Path


TEST_FILE = Path(__file__).resolve()
PACKAGE_ROOT = TEST_FILE.parents[1]
SKILLS_ROOT = TEST_FILE.parents[2]
REPOSITORY_ROOT = TEST_FILE.parents[3]
PRESET_PATH = PACKAGE_ROOT / "assets" / "presets" / "native-ai-engineering.json"
INVENTORY_PATH = REPOSITORY_ROOT / "docs" / "capability-inventory.json"

TARGET_IDS = [
    "agent-orchestrator",
    "agent-product",
    "agent-architecture",
    "agent-design",
    "agent-frontend",
    "agent-backend",
    "agent-review",
]

LEGACY_IDS = [
    "engineering-orchestrator",
    "product-development",
    "solution-architecture",
    "product-design",
    "frontend-engineering",
    "backend-platform",
    "quality-review",
]


class NativePresetSkillMappingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.preset = json.loads(PRESET_PATH.read_text(encoding="utf-8"))
        cls.inventory = json.loads(INVENTORY_PATH.read_text(encoding="utf-8"))
        cls.profiles = {
            profile["id"]: profile for profile in cls.preset["profiles"]
        }
        cls.skill_sets = {
            profile_id: set(profile["skills"])
            for profile_id, profile in cls.profiles.items()
        }
        cls.catalog_names = {
            item["name"] for item in cls.inventory["items"]
        }

    def test_preset_v2_identity_and_order_are_explicit(self) -> None:
        self.assertEqual(self.preset["version"], "2.1.1")
        self.assertEqual(self.preset["identity_generation"], 2)
        self.assertEqual(self.preset["topology"], "orchestrator_with_specialists")
        self.assertEqual(self.preset["orchestrator"], "agent-orchestrator")
        self.assertEqual(
            [profile["id"] for profile in self.preset["profiles"]],
            TARGET_IDS,
        )
        self.assertEqual(self.preset["legacy_profile_ids"], LEGACY_IDS)
        self.assertEqual(
            self.preset["mixed_identity_policy"],
            "block_outside_migration",
        )
        self.assertTrue(set(TARGET_IDS).isdisjoint(LEGACY_IDS))

    def test_only_orchestrator_is_gateway_eligible(self) -> None:
        gateways = [
            profile["id"]
            for profile in self.preset["profiles"]
            if profile["gateway"] == "eligible"
        ]
        self.assertEqual(gateways, ["agent-orchestrator"])
        self.assertEqual(
            self.profiles["agent-orchestrator"]["worker_mode"],
            "user_facing_front_door",
        )
        for profile_id in TARGET_IDS[1:]:
            self.assertEqual(self.profiles[profile_id]["gateway"], "none")
            self.assertEqual(
                self.profiles[profile_id]["worker_mode"],
                "headless_on_demand",
            )

    def test_every_mapped_capability_is_catalog_resolvable(self) -> None:
        mapped = set().union(*self.skill_sets.values())
        missing_from_catalog = sorted(mapped - self.catalog_names)
        missing_from_repository = sorted(
            skill
            for skill in mapped
            if not (SKILLS_ROOT / skill / "SKILL.md").is_file()
        )
        self.assertEqual(missing_from_catalog, [])
        self.assertEqual(missing_from_repository, [])

    def test_orchestrator_has_routing_and_continuity_capabilities(self) -> None:
        self.assertTrue(
            {
                "hermes-agent-fleet-bootstrap",
                "hermes-profile-bootstrap",
                "workflow-router",
                "role-switcher",
                "hermes-task-management-workflow",
                "systems-reasoning",
                "decision-provenance",
                "context-manager",
                "task-continuity",
                "delivery-work-breakdown",
                "skill-eval",
            }.issubset(self.skill_sets["agent-orchestrator"])
        )

    def test_product_profile_has_planning_and_acceptance_capabilities(self) -> None:
        self.assertTrue(
            {
                "product-development-workflow",
                "product-manager",
                "product-requirements",
                "business-value-alignment",
                "user-research",
                "experiment-design",
                "delivery-work-breakdown",
                "acceptance-testing",
                "decision-provenance",
            }.issubset(self.skill_sets["agent-product"])
        )

    def test_architecture_profile_has_boundary_and_contract_capabilities(self) -> None:
        self.assertTrue(
            {
                "implementation-context-discovery",
                "systems-reasoning",
                "systems-thinking",
                "master-engineer",
                "spec-workflow",
                "domain-driven-design",
                "ports-and-adapters",
                "clean-architecture",
                "solid-design",
                "design-patterns",
                "api-contract",
                "data-modeling",
                "adr",
                "event-driven-design",
                "service-design",
                "threat-modeling",
                "resilience-engineering",
                "observability-design",
                "architecture-review",
                "decision-provenance",
            }.issubset(self.skill_sets["agent-architecture"])
        )

    def test_design_profile_has_experience_capabilities(self) -> None:
        self.assertTrue(
            {
                "master-design",
                "design-review",
                "design-system",
                "information-architecture",
                "accessibility",
                "responsiveness",
                "ui-components",
                "ux-ui-patterns",
                "visual-hierarchy",
                "composition",
                "readability",
                "design-interaction",
                "adaptive-component-design",
                "content-strategy",
                "decision-provenance",
            }.issubset(self.skill_sets["agent-design"])
        )

    def test_implementation_profiles_have_delivery_and_quality_capabilities(self) -> None:
        shared = {
            "implementation-context-discovery",
            "master-engineer",
            "new-feature-workflow",
            "bugfix-workflow",
            "production-code-quality-baseline",
            "test-driven-development",
            "clean-code",
            "solid-design",
            "refactoring",
            "systematic-debugging",
            "git-workflow",
        }
        self.assertTrue(shared.issubset(self.skill_sets["agent-frontend"]))
        self.assertTrue(shared.issubset(self.skill_sets["agent-backend"]))
        self.assertTrue(
            {
                "ui-components",
                "design-system",
                "ux-patterns-for-developers",
                "accessibility",
                "responsiveness",
                "web-performance",
            }.issubset(self.skill_sets["agent-frontend"])
        )
        self.assertTrue(
            {
                "clean-architecture",
                "domain-driven-design",
                "ports-and-adapters",
                "design-patterns",
                "api-contract",
                "data-modeling",
                "service-design",
                "event-driven-design",
                "observability-design",
                "resilience-engineering",
            }.issubset(self.skill_sets["agent-backend"])
        )

    def test_review_profile_has_verification_without_primary_implementation(self) -> None:
        review = self.skill_sets["agent-review"]
        self.assertTrue(
            {
                "acceptance-testing",
                "software-testing-workflow",
                "code-review-workflow",
                "architecture-review",
                "security-review",
                "design-review",
                "threat-modeling",
                "accessibility",
                "web-performance",
                "decision-provenance",
                "skill-eval",
            }.issubset(review)
        )
        self.assertTrue(
            review.isdisjoint(
                {
                    "new-feature-workflow",
                    "bugfix-workflow",
                    "git-workflow",
                    "test-driven-development",
                    "refactoring",
                    "product-manager",
                    "product-requirements",
                }
            )
        )

    def test_authority_boundaries_are_not_flattened(self) -> None:
        routing_capabilities = {
            "hermes-agent-fleet-bootstrap",
            "hermes-profile-bootstrap",
            "workflow-router",
            "role-switcher",
        }
        for profile_id, skills in self.skill_sets.items():
            if profile_id == "agent-orchestrator":
                continue
            self.assertTrue(
                skills.isdisjoint(routing_capabilities),
                f"{profile_id} must not receive orchestrator-only capabilities",
            )

        product_authority = {
            "product-development-workflow",
            "product-manager",
            "product-requirements",
            "business-value-alignment",
            "user-research",
            "experiment-design",
        }
        for profile_id, skills in self.skill_sets.items():
            if profile_id == "agent-product":
                continue
            self.assertTrue(
                skills.isdisjoint(product_authority),
                f"{profile_id} must not absorb product authority",
            )

        all_mapped = set().union(*self.skill_sets.values())
        self.assertNotIn("deployment-workflow", all_mapped)

    def test_profile_ids_are_product_and_framework_neutral(self) -> None:
        forbidden_tokens = {
            "visualmate",
            "product-a",
            "react",
            "nextjs",
            "tailwind",
            "tdd",
            "ddd",
            "solid",
        }
        for profile_id in self.profiles:
            self.assertTrue(profile_id.startswith("agent-"))
            self.assertTrue(
                all(token not in profile_id for token in forbidden_tokens),
                profile_id,
            )

    def test_skill_manifests_are_curated_not_full_catalog_copies(self) -> None:
        catalog_size = len(self.catalog_names)
        for profile_id, profile in self.profiles.items():
            skills = profile["skills"]
            self.assertEqual(
                len(skills),
                len(set(skills)),
                f"{profile_id} contains duplicate skill IDs",
            )
            self.assertLess(
                len(skills),
                catalog_size / 2,
                f"{profile_id} received an overly broad catalog copy",
            )


if __name__ == "__main__":
    unittest.main()
