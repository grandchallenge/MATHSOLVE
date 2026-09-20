from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from ci.validate_ns_ci_independent_contribution_pilot import ROOT, validate

RELATIVE = [
    Path("contributions/NS-CI-001/C2_MIX_DIRECTION_COMPRESSION_LEDGER_CHARGE"),
    Path("handoffs/NS-CI-001/C2_MIX_DIRECTION_COMPRESSION_LEDGER_CHARGE_ZERO_CONTEXT.md"),
]


class IndependentContributionPilotTest(unittest.TestCase):
    def make_root(self) -> Path:
        temp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, temp, ignore_errors=True)
        for rel in RELATIVE:
            src = ROOT / rel
            dst = temp / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            if src.is_dir():
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)
        return temp

    def test_protected_pilot_surface_validates(self) -> None:
        self.assertEqual(validate(ROOT), [])

    def test_handoff_without_durable_return_fails(self) -> None:
        root = self.make_root()
        path = root / RELATIVE[1]
        text = path.read_text(encoding="utf-8").replace("Repository access is not required", "repository optional")
        path.write_text(text, encoding="utf-8")
        self.assertTrue(any("durable-return clause" in item for item in validate(root)))

    def test_dispatch_canonical_mutation_fails(self) -> None:
        root = self.make_root()
        dispatch_dir = root / RELATIVE[0] / "dispatches"
        dispatch_dir.mkdir(parents=True, exist_ok=True)
        payload = {
            "schema_version": "0.1-pilot",
            "dispatch_id": "TEST-BLIND-001",
            "assignment_id": "A",
            "concurrency_mode": "independent_blind",
            "blind_cohort_id": "TEST-COHORT",
            "wall_clock_limit_minutes": 22,
            "source_handoff_commit_sha": "a" * 40,
            "source_handoff_blob_sha": "b" * 40,
            "source_handoff_sha256": "c" * 64,
            "canonical_mutation_authorized": True,
            "contributor_write_authority": "none_required"
        }
        (dispatch_dir / "bad.json").write_text(json.dumps(payload), encoding="utf-8")
        self.assertTrue(any("canonical mutation" in item for item in validate(root)))

    def test_cohort_unknown_dispatch_fails(self) -> None:
        root = self.make_root()
        cohort_dir = root / RELATIVE[0] / "cohorts"
        cohort_dir.mkdir(parents=True, exist_ok=True)
        payload = {
            "schema_version": "0.1-pilot",
            "cohort_id": "TEST-COHORT",
            "mode": "independent_blind",
            "state": "OPEN",
            "dispatch_ids": ["MISSING-1", "MISSING-2"],
            "cross_disclosure_before_closure": False
        }
        (cohort_dir / "cohort.json").write_text(json.dumps(payload), encoding="utf-8")
        errors = validate(root)
        self.assertTrue(any("unknown dispatch" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
