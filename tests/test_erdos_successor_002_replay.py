import json
import unittest

from ci.erdos_successor_002_replay import (
    BASE, ROOT, audit_evidence, build_report, finite_ramsey_replay,
    structural_replay,
)


class TestSuccessorReplay(unittest.TestCase):
    def test_expected_replay(self):
        expected = json.loads(
            (ROOT / BASE / "replays/ERDOS-SUCCESSOR-002-REPLAY-001.json").read_text(encoding="utf-8")
        )
        self.assertEqual(build_report(), expected)

    def test_finite_ramsey_boundary(self):
        r = finite_ramsey_replay()
        self.assertEqual(r["K6_two_colorings_exhausted"], 32768)
        self.assertEqual(r["K6_triangle_free_two_colorings"], 0)
        self.assertTrue(r["K5_cycle_complement_witness_no_monochromatic_triangle"])

    def test_linear_host_obstruction(self):
        r = structural_replay()
        self.assertEqual(r["K5_3_maximum_distinct_hyperedge_overlap"], 2)
        self.assertEqual(r["triangle_of_pairs_finite_samples"]["7"]["hyperedges"], 35)

    def test_receipts(self):
        self.assertEqual(len(audit_evidence()["records"]), 3)


if __name__ == "__main__":
    unittest.main()
