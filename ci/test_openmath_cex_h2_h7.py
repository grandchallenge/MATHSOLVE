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

    def test_no_math_job_before_import_readback(self):
        campaign=load(".gcl/campaigns/OPENMATH-2026-SOURCE-ACQ/CAMPAIGN_STATE.json")
        registry=load(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
        if campaign["current_frontier"]["id"]=="PROTECTED_SOLVE_IMPORT_AND_READBACK_OM26_H2_H7":
            self.assertFalse(registry["mathematics_release_policy"]["h2_h7_solve_release"])
            self.assertEqual(registry["mathematics_release_policy"]["current_math_jobs"],0)

    def test_source_assignments_closed(self):
        registry=load(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
        source=[x for x in registry["assignments"] if x["class"]=="SOURCE_ACQUISITION"]
        self.assertEqual(len(source),6)
        self.assertTrue(all(x["state"]=="CLOSED" for x in source))

if __name__=="__main__":
    unittest.main()
