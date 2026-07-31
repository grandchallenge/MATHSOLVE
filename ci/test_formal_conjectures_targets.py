from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

import validate_formal_conjectures_targets as target


class FormalTargetTests(unittest.TestCase):
    def write_package(self, payload: dict) -> Path:
        handle = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8")
        with handle:
            json.dump(payload, handle)
        return Path(handle.name)

    def package_errors(self, mutate) -> list[str]:
        data = copy.deepcopy(target.load())
        mutate(data)
        path = self.write_package(data)
        try:
            return target.errors(package_path=path)
        finally:
            path.unlink(missing_ok=True)

    def test_current_package_passes(self) -> None:
        self.assertEqual([], target.errors())

    def test_source_lane_drift_fails(self) -> None:
        self.assertTrue(self.package_errors(lambda d: d.__setitem__("source_lane", "FC-GDM-002")))

    def test_mathlib_drift_fails(self) -> None:
        self.assertTrue(self.package_errors(lambda d: d["target_toolchain"].__setitem__("mathlib_commit", "0" * 40)))

    def test_upstream_drift_fails(self) -> None:
        self.assertTrue(self.package_errors(lambda d: d["upstream"].__setitem__("commit", "0" * 40)))

    def test_missing_axiom_fails(self) -> None:
        self.assertTrue(self.package_errors(lambda d: d["axiom_report"]["imported_axioms"].pop()))

    def test_extra_axiom_fails(self) -> None:
        self.assertTrue(self.package_errors(lambda d: d["axiom_report"]["imported_axioms"].append("Hidden.Analytic.Axiom")))

    def test_sorry_inflation_fails(self) -> None:
        self.assertTrue(self.package_errors(lambda d: d["axiom_report"].__setitem__("sorry_count", 1)))

    def test_admit_inflation_fails(self) -> None:
        self.assertTrue(self.package_errors(lambda d: d["axiom_report"].__setitem__("admit_count", 1)))


if __name__ == "__main__":
    unittest.main()
