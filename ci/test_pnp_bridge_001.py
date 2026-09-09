from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from ci.validate_pnp_bridge_001 import ROOT, validate


class PNPBridge001Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for relative in ("work_packages/PNP_BRIDGE_001", "MathSolve/PNP"):
            shutil.copytree(ROOT / relative, self.root / relative)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def mutate(self, callback) -> None:
        path = self.root / "work_packages/PNP_BRIDGE_001/bridge_status.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        callback(data)
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    def test_complete_package_passes(self) -> None:
        self.assertEqual(validate(self.root), [])

    def test_machine_bridge_cannot_be_inflated(self) -> None:
        self.mutate(lambda data: data["bridges"][1].update(status="kernel_checked"))
        self.assertTrue(any("MODEL-001: status drift" in error for error in validate(self.root)))

    def test_only_carrier_bridge_can_be_closed(self) -> None:
        self.mutate(lambda data: data["closed_bridge_ids"].append("PNP-BRIDGE-MODEL-001"))
        self.assertTrue(any("only the carrier bridge" in error for error in validate(self.root)))

    def test_certification_inflation_fails(self) -> None:
        self.mutate(lambda data: data.update(certification_effect="qualified"))
        self.assertTrue(any("cannot certify" in error for error in validate(self.root)))


if __name__ == "__main__":
    unittest.main()
