#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import kobon_scorer as scorer


class KobonScorerTests(unittest.TestCase):
    def solution(self, lines):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        path = Path(temporary.name) / "solution.json"
        path.write_text(json.dumps({"lines": lines}), encoding="utf-8")
        return path

    def test_three_lines_make_one_triangle(self):
        lines, _ = scorer.load_solution(
            self.solution([[1, 0, 0], [0, 1, 0], [1, 1, -1]]), 3
        )
        self.assertEqual(scorer.score(lines)["triangles"], 1)

    def test_three_concurrent_lines_make_no_triangle(self):
        lines, _ = scorer.load_solution(
            self.solution([[1, 0, 0], [0, 1, 0], [1, -1, 0]]), 3
        )
        self.assertEqual(scorer.score(lines)["triangles"], 0)

    def test_parallel_pair_makes_no_triangle(self):
        lines, _ = scorer.load_solution(
            self.solution([[1, 0, 0], [1, 0, -1], [0, 1, 0]]), 3
        )
        self.assertEqual(scorer.score(lines)["triangles"], 0)

    def test_subdivided_original_triangle_is_not_counted(self):
        lines, _ = scorer.load_solution(
            self.solution(
                [[1, 0, 0], [0, 1, 0], [1, 1, -1], [2, 0, -1]]
            ),
            4,
        )
        result = scorer.score(lines)
        self.assertEqual(result["triangles"], 1)
        supports = [face["supporting_lines"] for face in result["faces"]]
        self.assertNotIn([0, 1, 2], supports)

    def test_locked_baseline_is_sixteen_consecutive_support_triples(self):
        raw = [[2 * i, -1, -(i * i)] for i in range(18)]
        lines, _ = scorer.load_solution(self.solution(raw), 18)
        result = scorer.score(lines)
        self.assertEqual(result["triangles"], 16)
        self.assertEqual(
            [face["supporting_lines"] for face in result["faces"]],
            [[i, i + 1, i + 2] for i in range(16)],
        )

    def test_proportional_duplicate_is_rejected(self):
        with self.assertRaises(scorer.InputError):
            scorer.load_solution(
                self.solution([[1, 2, 3], [-2, -4, -6], [0, 1, 0]]), 3
            )


if __name__ == "__main__":
    unittest.main()
