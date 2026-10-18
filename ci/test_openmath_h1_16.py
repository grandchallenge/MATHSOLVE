#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
H1 = ROOT / "work_packages/OPENMATH_2026/OM26_H1_KOBON_TRIANGLES"
CI = ROOT / "ci"


class H116ObstructionTests(unittest.TestCase):
    def run_script(self, name: str, *args: str):
        return subprocess.run(
            [sys.executable, str(H1 / name), *args],
            cwd=H1,
            check=True,
            capture_output=True,
            text=True,
        )

    def test_face_loss_mining_reproduces_committed_summary(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "face-loss.json"
            self.run_script("mine_h1_14_face_losses.py", "--output", str(out))
            actual = json.loads(out.read_text())
            committed = json.loads((H1 / "H1_16_FACE_LOSS_MINING.json").read_text())
            self.assertEqual(actual, committed)
            self.assertEqual(actual["unique_required_flip_count"], 60)
            self.assertEqual(actual["single_flip"]["lost_count_histogram"], {"3": 60})
            self.assertEqual(actual["single_flip"]["gained_count_histogram"], {"0": 60})
            self.assertTrue(actual["single_flip"]["all_three_face_toll_no_gain"])
            self.assertEqual(actual["dual_flip"]["lost_count_histogram"], {"5": 60})
            self.assertEqual(actual["dual_flip"]["gained_count_histogram"], {"1": 60})
            self.assertEqual(actual["dual_flip"]["single_loss_overlap_histogram"], {"1": 60})
            self.assertEqual(actual["dual_flip"]["target_gained_count"], 60)

    def test_333344_finite_replay_matches_receipt(self):
        sys.path.insert(0, str(CI))
        import validate_openmath_h1_333344 as replay

        actual = replay.replay()
        committed = json.loads((H1 / "H1_333344_OBSTRUCTION_RECEIPT.json").read_text())
        self.assertEqual(json.loads(json.dumps(actual)), committed)
        self.assertEqual(actual["post_triangle_residual_labelings"], 126)
        self.assertEqual(actual["relaxed_equality_escape_labelings"], 6)
        self.assertEqual(actual["realizable_candidates_remaining_in_profile"], 0)
        self.assertEqual(actual["remaining_q6_profiles"], ["333333", "333334"])
        for row in actual["equality_escape"]:
            self.assertEqual(
                (row["D2"], row["D1"], row["B"], row["U"], row["slack"]),
                (8, 20, 16, 3, 4),
            )
            self.assertEqual(row["minimum_incidence_excess"], 4)
            self.assertEqual(len([b for b in row["line_cover"] if b["cost"] == 2]), 2)


if __name__ == "__main__":
    unittest.main()
