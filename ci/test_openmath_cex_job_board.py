import unittest
from ci.validate_openmath_cex_job_board import (
    BASE_URL, ENTRYPOINT_URL, H1_AGENT_REF, H1_DISPATCH_ID, H1_ISSUE_URL,
    REGISTRY_URL, EXPECTED_MAPPING, load, validate,
)

class OpenMathCEXJobBoardTest(unittest.TestCase):
    def test_preflight(self): self.assertEqual(validate(), [])

    def test_source_assignments_closed_and_bound(self):
        registry=load(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
        source=[x for x in registry["assignments"] if x["class"]=="SOURCE_ACQUISITION"]
        self.assertEqual(len(source),6)
        self.assertTrue(all(x["state"]=="CLOSED" for x in source))
        self.assertEqual({x["slot_binding"]:x["external_hill_id"] for x in source},EXPECTED_MAPPING)

    def test_zero_context_launch(self):
        registry=load(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
        self.assertEqual(registry["launch_contract"]["entrypoint_url"],ENTRYPOINT_URL)
        self.assertEqual(registry["discovery"]["machine_registry_url"],REGISTRY_URL)
        self.assertFalse(registry["launch_contract"]["repository_discovery_required"])

    def test_every_work_package_has_absolute_url(self):
        registry=load(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
        for item in registry["assignments"]:
            self.assertEqual(item["work_package_url"],BASE_URL+"/blob/main/"+item["work_package"])

    def test_inaugural_h1_lease(self):
        registry=load(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
        job=next(x for x in registry["assignments"] if x.get("assignment_id")=="OM26-H1-H1-12")
        self.assertEqual(job["lease"]["dispatch_id"],H1_DISPATCH_ID)
        self.assertEqual(job["lease"]["agent_ref"],H1_AGENT_REF)
        self.assertEqual(job["lease"]["dispatch_url"],H1_ISSUE_URL)
        self.assertEqual(job["lease"]["return_url"],H1_ISSUE_URL)

    def test_h2_h7_decomposition_not_instantiated_yet(self):
        registry=load(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
        self.assertEqual(registry["mathematics_release_policy"]["current_math_jobs"],0)

if __name__=="__main__": unittest.main()
