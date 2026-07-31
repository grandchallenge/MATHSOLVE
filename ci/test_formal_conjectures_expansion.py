from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from ci.validate_formal_conjectures_expansion import ROOT, validate


class FormalConjecturesExpansionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for directory in ("campaign_manifests", "cert_handoffs", "contracts", "formal_sources/formal_conjectures"):
            source = ROOT / directory
            target = self.root / directory
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(source, target)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def load(self, relative: str) -> dict:
        return json.loads((self.root / relative).read_text(encoding="utf-8"))

    def save(self, relative: str, value: dict) -> None:
        (self.root / relative).write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")

    def test_complete_package_passes(self) -> None:
        self.assertEqual(validate(self.root), [])

    def test_missing_common_evidence_fails(self) -> None:
        path = "campaign_manifests/UC-001.json"
        manifest = self.load(path)
        manifest["forge_inputs"] = [
            item for item in manifest["forge_inputs"]
            if item["path"] != "formal_sources/formal_conjectures/source_locks/FC-GDM-002.json"
        ]
        self.save(path, manifest)
        self.assertTrue(any("incomplete FC-GDM-002 evidence" in item for item in validate(self.root)))

    def test_programme_admission_drift_fails(self) -> None:
        path = "campaign_manifests/PNP-001.json"
        manifest = self.load(path)
        manifest["programme"]["commit_sha"] = "0" * 40
        self.save(path, manifest)
        self.assertTrue(any("Programme admission commit" in item for item in validate(self.root)))

    def test_odd_zeta_scope_collapse_fails(self) -> None:
        path = "formal_sources/formal_conjectures/MS-FC-WP01.json"
        route = self.load(path)
        oz = next(item for item in route["routes"] if item["campaign_id"] == "OZ-001")
        oz["scopes"].pop()
        self.save(path, route)
        self.assertTrue(any("eight theorem scopes" in item for item in validate(self.root)))

    def test_non_route_inflation_fails(self) -> None:
        path = "formal_sources/formal_conjectures/MS-FC-WP01.json"
        route = self.load(path)
        bsd = next(item for item in route["routes"] if item["campaign_id"] == "BSD-001")
        bsd["route_class"] = "statement-correspondence"
        bsd["disposition"] = "direct"
        self.save(path, route)
        errors = validate(self.root)
        self.assertTrue(any("BSD-001: route class drift" in item for item in errors))
        self.assertTrue(any("explicit non-route was promoted" in item for item in errors))

    def test_certification_status_drift_fails(self) -> None:
        path = "cert_handoffs/OZ-001.json"
        packet = self.load(path)
        packet["status"] = "ready"
        self.save(path, packet)
        self.assertTrue(any("OZ-001: MATHCERT handoff file state changed" in item for item in validate(self.root)))

    def test_pilot_contamination_fails(self) -> None:
        path = "campaign_manifests/RH-001.json"
        manifest = self.load(path)
        contract = self.load("contracts/formal_conjectures_expanded_evidence.json")
        manifest["forge_inputs"].append(contract["common_artifacts"][0])
        self.save(path, manifest)
        self.assertTrue(any("RH-001: FC-GDM-002 contaminated" in item for item in validate(self.root)))

    def test_stale_oz_next_obligation_fails(self) -> None:
        path = "campaign_manifests/OZ-001.json"
        manifest = self.load(path)
        manifest["solve"]["migration_debt"] = ["Return to source intake."]
        self.save(path, manifest)
        self.assertTrue(any("next active T3 migration obligation" in item for item in validate(self.root)))


if __name__ == "__main__":
    unittest.main()
