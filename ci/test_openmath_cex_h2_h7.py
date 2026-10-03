import unittest
from ci.validate_openmath_cex_h2_h7 import EXPECTED_MAPPING, EXPECTED_SLOTS, load, validate

class OpenMathCEXH2H7Test(unittest.TestCase):
    def test_preflight(self):
        self.assertEqual(validate(), [])

    def test_exact_mapping(self):
        prep=load("work_packages/OPENMATH_2026/CEX_H2_H7_PREPARATION.json")
        self.assertEqual([x["slot"] for x in prep["lanes"]], EXPECTED_SLOTS)
        self.assertEqual({x["slot"]:x["exact_hill_id"] for x in prep["lanes"]}, EXPECTED_MAPPING)

    def test_provider_semantics_imported(self):
        prep=load("work_packages/OPENMATH_2026/CEX_H2_H7_PREPARATION.json")
        for lane in prep["lanes"]:
            self.assertTrue(lane["forge_source_lock"])
            self.assertTrue(lane["semantic_source_map"])
            self.assertTrue(lane["status_triage"])

    def test_historical_import_snapshot_preserved(self):
        registry=load(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
        historical=registry["mathematics_release_policy"]["historical_tranche_metrics"]
        self.assertTrue(historical["deprecated_for_current_state"])
        previous=historical["previous"]
        self.assertTrue(previous["h2_h7_solve_release"])
        self.assertEqual(previous["h2_h7_leased_math_jobs"],6)

    def test_source_assignments_closed(self):
        registry=load(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
        source=[x for x in registry["assignments"] if x["class"]=="SOURCE_ACQUISITION"]
        self.assertEqual(len(source),6)
        self.assertTrue(all(x["state"]=="CLOSED" for x in source))

if __name__=="__main__":
    unittest.main()
