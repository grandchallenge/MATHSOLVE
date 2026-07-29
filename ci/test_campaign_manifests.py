from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_campaign_manifests", ROOT / "ci" / "validate_campaign_manifests.py"
)
module = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(module)


class CampaignManifestTests(unittest.TestCase):
    def setUp(self) -> None:
        self.source = ROOT / "campaign_manifests"

    def copied_registry(self) -> tuple[tempfile.TemporaryDirectory, Path]:
        handle = tempfile.TemporaryDirectory()
        self.addCleanup(handle.cleanup)
        target = Path(handle.name)
        for path in self.source.glob("*.json"):
            (target / path.name).write_text(
                path.read_text(encoding="utf-8"), encoding="utf-8"
            )
        return handle, target

    def test_current_registry_and_handoff_template_pass(self) -> None:
        self.assertEqual(module.campaign_manifest_errors(), [])
        self.assertEqual(module.mathcert_handoff_errors(), [])

    def test_missing_active_campaign_fails(self) -> None:
        _, target = self.copied_registry()
        (target / "RH-001.json").unlink()
        errors = module.campaign_manifest_errors(target)
        self.assertTrue(any("RH-001" in error and "uncovered" in error for error in errors))

    def test_retrospective_manifest_requires_migration_debt(self) -> None:
        _, target = self.copied_registry()
        path = target / "PNP-001.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["solve"]["migration_debt"] = []
        path.write_text(json.dumps(data), encoding="utf-8")
        errors = module.campaign_manifest_errors(target)
        self.assertTrue(
            any("retrospective coverage requires migration debt" in error for error in errors)
        )

    def test_artifact_identity_drift_fails(self) -> None:
        _, target = self.copied_registry()
        path = target / "HC-001.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["work_packages"][0]["artifacts"][0]["digest"] = "0" * 40
        path.write_text(json.dumps(data), encoding="utf-8")
        errors = module.campaign_manifest_errors(target)
        self.assertTrue(any("identity drift" in error for error in errors))

    def test_repository_commit_cannot_substitute_for_artifact_digest(self) -> None:
        _, target = self.copied_registry()
        path = target / "BSD-001.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        artifact = data["work_packages"][0]["artifacts"][0]
        artifact["digest"] = artifact["commit_sha"]
        path.write_text(json.dumps(data), encoding="utf-8")
        errors = module.campaign_manifest_errors(target)
        self.assertTrue(
            any("commit cannot substitute for artifact digest" in error for error in errors)
        )

    def test_distinct_ledger_roles_cannot_share_one_path(self) -> None:
        _, target = self.copied_registry()
        path = target / "UC-001.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["work_packages"][0]["ledgers"]["resource"] = dict(
            data["work_packages"][0]["ledgers"]["failed_route"]
        )
        data["work_packages"][0]["ledgers"]["resource"]["role"] = "resource_ledger"
        path.write_text(json.dumps(data), encoding="utf-8")
        errors = module.campaign_manifest_errors(target)
        self.assertTrue(any("distinct ledger roles share artifact path" in error for error in errors))

    def test_computational_package_requires_resource_and_failure_ledgers(self) -> None:
        _, target = self.copied_registry()
        path = target / "UC-001.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["work_packages"][0]["ledgers"]["resource"] = None
        path.write_text(json.dumps(data), encoding="utf-8")
        errors = module.campaign_manifest_errors(target)
        self.assertTrue(any("requires resource ledger" in error for error in errors))

    def test_partial_handoff_cannot_pass_judgment(self) -> None:
        self.assertTrue(module.provider_gate_errors("HC-001", "JUDGMENT"))

    def test_promotion_requires_positive_certification(self) -> None:
        _, target = self.copied_registry()
        path = target / "HC-001.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["promotion"] = {"eligible": True, "blockers": []}
        data["certification"] = {
            "repository": "grandchallenge/MATHCERT",
            "handoff_state": "rejected",
            "handoff_packets": [
                {
                    "handoff_id": "MC-HC-REJECTED",
                    "status": "rejected",
                    "target_claim_ids": ["HC-TARGET"],
                    "artifact": {
                        "repository": "grandchallenge/MATHCERT",
                        "commit_sha": "a" * 40,
                        "path": "handoffs/MC-HC-REJECTED.json",
                        "digest_algorithm": "git_blob_sha1",
                        "digest": "b" * 40,
                        "role": "certificate_handoff"
                    }
                }
            ]
        }
        path.write_text(json.dumps(data), encoding="utf-8")
        errors = module.campaign_manifest_errors(target)
        self.assertTrue(
            any("requires certified or qualified MATHCERT state" in error for error in errors)
        )


if __name__ == "__main__":
    unittest.main()
