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
            (target / path.name).write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
        return handle, target

    def test_current_registry_passes(self) -> None:
        self.assertEqual(module.campaign_manifest_errors(), [])

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
        self.assertTrue(any("retrospective coverage requires migration debt" in error for error in errors))

    def test_commit_digest_drift_fails(self) -> None:
        _, target = self.copied_registry()
        path = target / "HC-001.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["work_packages"][0]["artifacts"][0]["digest"] = "0" * 40
        path.write_text(json.dumps(data), encoding="utf-8")
        errors = module.campaign_manifest_errors(target)
        self.assertTrue(any("digest must equal commit_sha" in error for error in errors))

    def test_computational_package_requires_resource_and_failure_ledgers(self) -> None:
        _, target = self.copied_registry()
        path = target / "UC-001.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["work_packages"][0]["ledgers"]["resource"] = None
        path.write_text(json.dumps(data), encoding="utf-8")
        errors = module.campaign_manifest_errors(target)
        self.assertTrue(any("requires resource ledger" in error for error in errors))

    def test_promotion_cannot_bypass_cert_handoff(self) -> None:
        _, target = self.copied_registry()
        path = target / "HC-001.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["promotion"] = {"eligible": True, "blockers": []}
        path.write_text(json.dumps(data), encoding="utf-8")
        errors = module.campaign_manifest_errors(target)
        self.assertTrue(any("requires ready MATHCERT handoff" in error for error in errors))
        self.assertTrue(any("requires at least one MATHCERT handoff" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
