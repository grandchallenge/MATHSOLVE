from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from ci.validate_pnp_definition_concordance import ROOT, validate


class PNPDefinitionConcordanceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for relative in (
            "work_packages/PNP_DEFINITION_CONCORDANCE_001",
            "formal_sources/formal_conjectures",
            "contracts",
            "campaign_manifests",
            "cert_handoffs",
        ):
            source = ROOT / relative
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(source, target)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def load(self, relative: str) -> dict:
        return json.loads((self.root / relative).read_text(encoding="utf-8"))

    def save(self, relative: str, value: dict) -> None:
        (self.root / relative).write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")

    def test_complete_concordance_passes(self) -> None:
        self.assertEqual(validate(self.root), [])

    def test_source_identity_drift_fails(self) -> None:
        path = "work_packages/PNP_DEFINITION_CONCORDANCE_001/concordance.json"
        data = self.load(path)
        data["sources"]["mathlib_machine_and_cost"]["git_blob_sha1"] = "0" * 40
        self.save(path, data)
        self.assertTrue(any("pinned source identity drift" in error for error in validate(self.root)))

    def test_totality_inflation_fails(self) -> None:
        path = "work_packages/PNP_DEFINITION_CONCORDANCE_001/concordance.json"
        data = self.load(path)
        item = next(check for check in data["checks"] if check["check_id"] == "PNP-CONC-TOTALITY-001")
        item["disposition"] = "proved_terminal_claim"
        self.save(path, data)
        self.assertTrue(any("PNP-CONC-TOTALITY-001: disposition drift" in error for error in validate(self.root)))

    def test_placeholder_cannot_become_proof_evidence(self) -> None:
        path = "work_packages/PNP_DEFINITION_CONCORDANCE_001/concordance.json"
        data = self.load(path)
        item = next(check for check in data["checks"] if check["check_id"] == "PNP-CONC-PROOF-001")
        item["disposition"] = "kernel_checked"
        self.save(path, data)
        self.assertTrue(any("PNP-CONC-PROOF-001: disposition drift" in error for error in validate(self.root)))

    def test_missing_model_bridge_fails(self) -> None:
        path = "work_packages/PNP_DEFINITION_CONCORDANCE_001/concordance.json"
        data = self.load(path)
        data["open_bridges"] = [item for item in data["open_bridges"] if item["bridge_id"] != "PNP-BRIDGE-MODEL-001"]
        self.save(path, data)
        errors = validate(self.root)
        self.assertTrue(any("open bridge coverage drift" in error for error in errors))
        self.assertTrue(any("unresolved bridge reference" in error for error in errors))

    def test_statement_orientation_broadening_fails(self) -> None:
        path = "work_packages/PNP_DEFINITION_CONCORDANCE_001/concordance.json"
        data = self.load(path)
        data["exact_theorem_interface"]["admitted_use"] = "both_terminal_outcomes"
        self.save(path, data)
        self.assertTrue(any("orientation was broadened" in error for error in validate(self.root)))

    def test_certification_inflation_fails(self) -> None:
        path = "cert_handoffs/PNP-001.json"
        data = self.load(path)
        data["status"] = "qualified"
        self.save(path, data)
        self.assertTrue(any("handoff changed from pending" in error for error in validate(self.root)))

    def test_promotion_inflation_fails(self) -> None:
        path = "campaign_manifests/PNP-001.json"
        data = self.load(path)
        data["promotion"]["eligible"] = True
        self.save(path, data)
        self.assertTrue(any("cannot make promotion eligible" in error for error in validate(self.root)))

    def test_route_forgetting_concordance_fails(self) -> None:
        path = "formal_sources/formal_conjectures/MS-FC-WP01.json"
        data = self.load(path)
        route = next(item for item in data["routes"] if item["campaign_id"] == "PNP-001")
        route.pop("concordance_id")
        self.save(path, data)
        self.assertTrue(any("concordance identity missing" in error for error in validate(self.root)))


if __name__ == "__main__":
    unittest.main()
