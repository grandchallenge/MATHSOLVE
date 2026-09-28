import unittest
from ci.validate_openmath_cex_job_board import (
    BASE_URL, H1_AGENT_REF, H1_DISPATCH_ID, H1_ISSUE_URL, WP01, load, validate,
)

class OpenMathCEXJobBoardTest(unittest.TestCase):
    def test_preflight(self): self.assertEqual(validate(), [])

    def test_six_wp01_available_zero_leased(self):
        registry=load(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
        jobs=[x for x in registry["assignments"] if x.get("assignment_id") in WP01]
        self.assertEqual(len(jobs),6)
        self.assertTrue(all(x["state"]=="AVAILABLE_FOR_LEASE" for x in jobs))
        self.assertTrue(all(x["lease"]["state"]=="UNCLAIMED" for x in jobs))
        self.assertTrue(all(x["lease"]["dispatch_id"] is None for x in jobs))
        self.assertEqual(registry["mathematics_release_policy"]["current_math_jobs"],6)
        self.assertEqual(registry["mathematics_release_policy"]["h2_h7_leased_math_jobs"],0)

    def test_every_wp01_has_absolute_url(self):
        registry=load(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
        for item in registry["assignments"]:
            if item.get("assignment_id") in WP01:
                self.assertEqual(item["work_package_url"],BASE_URL+"/blob/main/"+item["work_package"])

    def test_h1_lease_preserved(self):
        registry=load(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
        job=next(x for x in registry["assignments"] if x.get("assignment_id")=="OM26-H1-H1-12")
        self.assertEqual(job["lease"]["dispatch_id"],H1_DISPATCH_ID)
        self.assertEqual(job["lease"]["agent_ref"],H1_AGENT_REF)
        self.assertEqual(job["lease"]["dispatch_url"],H1_ISSUE_URL)
        self.assertEqual(job["lease"]["return_url"],H1_ISSUE_URL)

    def test_available_is_not_executable(self):
        registry=load(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
        for item in registry["assignments"]:
            if item.get("assignment_id") in WP01:
                self.assertNotEqual(item["state"],"LEASED")
                self.assertIsNone(item["lease"]["agent_ref"])
                self.assertIsNone(item["lease"]["return_url"])

if __name__=="__main__": unittest.main()
