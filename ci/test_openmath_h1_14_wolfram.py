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
sys.path.insert(0, str(H1))
import search_94_coordinate_sweep as wall


class H114WolframRouteTests(unittest.TestCase):
    def run_script(self, name: str, *args: str):
        return subprocess.run(
            [sys.executable, str(H1 / name), *args],
            cwd=H1,
            check=True,
            capture_output=True,
            text=True,
        )

    def test_near_miss_and_dual_cell_receipts(self):
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            atlas = td / "atlas.json"
            dual = td / "dual.json"
            coupled = td / "coupled.json"

            self.run_script("build_94_near_miss_atlas.py", "--output", str(atlas))
            a = json.loads(atlas.read_text())
            self.assertEqual(a["baseline_triangles"], 93)
            self.assertEqual(a["minimum_positive_blocker_count"], 2)
            self.assertEqual(a["two_blocker_target_count"], 60)

            self.run_script(
                "search_94_dual_cells.py",
                "--atlas", str(atlas),
                "--output", str(dual),
            )
            d = json.loads(dual.read_text())
            self.assertEqual(d["results"]["best_individual_score"], 90)
            self.assertEqual(d["results"]["best_pair_score"], 89)
            self.assertFalse(d["results"]["found_94_or_better"])

            self.run_script(
                "search_94_coupled_cells.py",
                "--atlas", str(atlas),
                "--output", str(coupled),
            )
            c = json.loads(coupled.read_text())
            self.assertEqual(c["method"]["attempted_single_mutual_event_flips"], 2040)
            self.assertEqual(c["method"]["feasible_adjacent_mutual_subcells"], 28)
            self.assertEqual(c["results"]["best_score"], 86)
            self.assertFalse(c["results"]["found_94_or_better"])

    def test_committed_receipts_match_summary(self):
        a = json.loads((H1 / "H1_14_NEAR_MISS_ATLAS_SUMMARY.json").read_text())
        d = json.loads((H1 / "H1_14_DUAL_CELL_RECEIPT.json").read_text())
        c = json.loads((H1 / "H1_14_COUPLED_CELL_RECEIPT.json").read_text())
        self.assertEqual((a["baseline_triangles"], a["two_blocker_target_count"]), (93, 60))
        self.assertEqual((d["results"]["best_individual_score"], d["results"]["best_pair_score"]), (90, 89))
        self.assertEqual((c["method"]["feasible_adjacent_mutual_subcells"], c["results"]["best_score"]), (28, 86))


    def test_strict_resolve_classification(self):
        receipt = json.loads((H1 / "H1_14_RESOLVE_CLASSIFICATION.json").read_text())
        cases = receipt["cases"]
        self.assertEqual(len(cases), 20)
        self.assertEqual(sum(bool(x["resolve"]) for x in cases), 6)
        self.assertEqual(sum(not bool(x["resolve"]) for x in cases), 14)

        listing = json.loads(
            self.run_script("h1_14_resolve_queries.py", "--top", "10").stdout
        )
        self.assertEqual([x["target"] for x in listing], [
            [3, 14, 17], [0, 4, 14], [2, 5, 15], [3, 8, 17],
            [2, 11, 15], [1, 5, 16], [1, 12, 16], [4, 15, 17],
            [0, 4, 6], [2, 14, 17],
        ])

        both = []
        for rank in range(10):
            states = [bool(x["resolve"]) for x in cases if x["rank"] == rank]
            self.assertEqual(len(states), 2)
            if states == [True, True]:
                both.append(tuple(listing[rank]["target"]))
        self.assertEqual(both, [(0, 4, 14)])

        seed = wall.load_solution(H1 / "candidates/RH_BADER_RECONSTRUCTION_093/solution.json")
        coupled = receipt["coupled_strict_cell"]["materialized_integer_lines"]
        candidate = list(seed)
        candidate[6] = tuple(coupled["line_6"])
        candidate[11] = tuple(coupled["line_11"])
        self.assertEqual(wall.exact_score(candidate), 89)
        self.assertEqual(receipt["coupled_strict_cell"]["gcl_exact_score"], 89)


if __name__ == "__main__":
    unittest.main()
