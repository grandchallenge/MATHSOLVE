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

    def mutate_status(self, callback) -> None:
        path = self.root / "work_packages/PNP_BRIDGE_001/bridge_status.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        callback(data)
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    def mutate_poly(self, old: str, new: str) -> None:
        path = self.root / "MathSolve/PNP/PolyBoundBridge.lean"
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    def test_complete_package_passes(self) -> None:
        self.assertEqual(validate(self.root), [])

    def test_machine_bridge_cannot_be_inflated(self) -> None:
        self.mutate_status(lambda d: d["bridges"][1].update(status="kernel_checked"))
        self.assertTrue(any("MODEL-001: status drift" in e for e in validate(self.root)))

    def test_only_carrier_and_polybound_can_be_closed(self) -> None:
        self.mutate_status(lambda d: d["closed_bridge_ids"].append("PNP-BRIDGE-MODEL-001"))
        self.assertTrue(any("only carrier and polynomial-bound" in e for e in validate(self.root)))

    def test_certification_inflation_fails(self) -> None:
        self.mutate_status(lambda d: d.update(certification_effect="qualified"))
        self.assertTrue(any("cannot certify" in e for e in validate(self.root)))

    def test_threshold_omission_fails(self) -> None:
        self.mutate_poly("input.length < threshold", "True")
        self.assertTrue(any("threshold" in e for e in validate(self.root)))

    def test_low_length_cap_omission_fails(self) -> None:
        self.mutate_poly("cost input ≤ lowCap", "cost input ≤ cost input")
        self.assertTrue(any("lowCap" in e for e in validate(self.root)))

    def test_input_length_measure_drift_fails(self) -> None:
        self.mutate_poly("p.eval input.length", "p.eval (input.length + 1)")
        self.assertTrue(any("input.length" in e for e in validate(self.root)))

    def test_coefficient_class_drift_fails(self) -> None:
        self.mutate_poly("Polynomial Nat", "Polynomial Int")
        self.assertTrue(any("Polynomial" in e for e in validate(self.root)))

    def test_hidden_machine_model_fails(self) -> None:
        path = self.root / "MathSolve/PNP/PolyBoundBridge.lean"
        path.write_text(path.read_text(encoding="utf-8") + "\nabbrev TM2Runtime := Nat\n", encoding="utf-8")
        self.assertTrue(any("TM2Runtime" in e for e in validate(self.root)))

    def test_one_way_only_conversion_fails(self) -> None:
        self.mutate_poly(
            "theorem programmePolynomialBound_to_importedPolynomialBound",
            "theorem removed_reverse_conversion",
        )
        self.assertTrue(any("programmePolynomialBound_to_importedPolynomialBound" in e for e in validate(self.root)))

    def test_class_equivalence_inflation_fails(self) -> None:
        path = self.root / "MathSolve/PNP/PolyBoundBridge.lean"
        path.write_text(path.read_text(encoding="utf-8") + "\ntheorem importedPEqProgrammeP : True := trivial\n", encoding="utf-8")
        self.assertTrue(any("importedPEqProgrammeP" in e for e in validate(self.root)))

    def test_placeholder_proof_fails(self) -> None:
        path = self.root / "MathSolve/PNP/PolyBoundBridge.lean"
        path.write_text(path.read_text(encoding="utf-8") + "\ntheorem placeholder : True := by sorry\n", encoding="utf-8")
        self.assertTrue(any("sorry" in e for e in validate(self.root)))


if __name__ == "__main__":
    unittest.main()
