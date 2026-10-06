import unittest

from ci.erdos_241_replay import (
    EXPECTED_EXTREMIZERS,
    EXPECTED_MINIMAL_SPANS,
    build_report,
    is_b3,
)


class Erdos241ReplayTests(unittest.TestCase):
    def test_minimal_spans_and_extremizers_replay_exactly(self):
        report = build_report()
        self.assertTrue(report["expected_minimal_spans_match"])
        self.assertTrue(report["expected_extremizers_match"])
        self.assertEqual(
            report["minimal_spans"],
            {str(k): v for k, v in EXPECTED_MINIMAL_SPANS.items()},
        )
        self.assertTrue(report["no_seven_element_b3_set_through_64"])
        self.assertEqual(
            report["exact_f_intervals_through_64"][-1],
            {"start": 46, "end": 64, "value": 6},
        )
        self.assertEqual(
            report["minimal_span_extremizers"],
            {
                str(k): [list(x) for x in values]
                for k, values in EXPECTED_EXTREMIZERS.items()
            },
        )

    def test_a1_small_n_counterexamples_replay(self):
        report = build_report()
        self.assertTrue(all(report["a1_small_n_checks"].values()))
        self.assertTrue(is_b3((1, 2, 5)))
        self.assertFalse(is_b3((1, 2, 3)))
        self.assertFalse(is_b3((1, 3, 4)))
        self.assertFalse(is_b3((1, 3, 5)))

    def test_structural_obstruction_sweep_finds_no_counterexample(self):
        report = build_report()
        sweep = report["structural_lemma_falsification_sweep"]
        self.assertEqual(sweep["limit"], 15)
        self.assertGreater(sweep["checked_b3_sets"], 0)
        self.assertIsNone(sweep["violation"])


if __name__ == "__main__":
    unittest.main()
