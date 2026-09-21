#!/usr/bin/env python3
import copy
import unittest
from validate_rm_dio_004 import load_package, validation_errors

class ResearchMathRouteTests(unittest.TestCase):
    def setUp(self):
        self.binding, self.screen, self.handoff = load_package()
    def test_committed_package(self):
        self.assertEqual(validation_errors(self.binding, self.screen, self.handoff), [])
    def test_rejects_source_commit_drift(self):
        binding = copy.deepcopy(self.binding); binding["dataset"]["commit"] = "0" * 40
        self.assertTrue(validation_errors(binding, self.screen, self.handoff))
    def test_rejects_missing_solution(self):
        screen = copy.deepcopy(self.screen); screen["solutions"].pop(); screen["solution_count"] -= 1
        self.assertTrue(validation_errors(self.binding, screen, self.handoff))
    def test_rejects_bound_inflation(self):
        screen = copy.deepcopy(self.screen); screen["domain"]["maximum"] += 1
        self.assertTrue(validation_errors(self.binding, screen, self.handoff))
    def test_rejects_certification_inflation(self):
        handoff = copy.deepcopy(self.handoff); handoff["requested_level"] = 5
        self.assertTrue(validation_errors(self.binding, self.screen, handoff))

if __name__ == "__main__":
    unittest.main()
