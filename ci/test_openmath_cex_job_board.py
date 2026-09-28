import unittest

from ci.validate_openmath_cex_job_board import (
    BASE_URL,
    ENTRYPOINT_URL,
    H1_AGENT_REF,
    H1_DISPATCH_ID,
    H1_ISSUE_URL,
    REGISTRY_URL,
    load,
    validate,
)


class OpenMathCEXJobBoardTest(unittest.TestCase):
    def test_preflight(self):
        self.assertEqual(validate(), [])

    def test_source_assignments_match_authoritative_pool(self):
        receipt = load('work_packages/OPENMATH_2026/H2_H7_AUTHORITATIVE_LIST_RECEIPT.json')
        registry = load('.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json')
        source = [x for x in registry['assignments'] if x['class'] == 'SOURCE_ACQUISITION']
        self.assertEqual([x['external_hill_id'] for x in source], receipt['unresolved_source_pool'])
        self.assertTrue(all(x['state'] == 'AVAILABLE_FOR_LEASE' for x in source))
        self.assertTrue(all(x['lease']['state'] == 'UNCLAIMED' for x in source))

    def test_zero_context_launch_has_absolute_entrypoint(self):
        registry = load('.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json')
        self.assertEqual(registry['launch_contract']['entrypoint_url'], ENTRYPOINT_URL)
        self.assertEqual(
            registry['launch_contract']['required_fields'],
            ['ENTRYPOINT_URL', 'DISPATCH_ID', 'AGENT_REF'],
        )
        self.assertEqual(registry['discovery']['machine_registry_url'], REGISTRY_URL)
        self.assertFalse(registry['launch_contract']['repository_discovery_required'])

    def test_every_work_package_has_absolute_url(self):
        registry = load('.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json')
        for item in registry['assignments']:
            self.assertEqual(
                item['work_package_url'],
                BASE_URL + '/blob/main/' + item['work_package'],
            )

    def test_inaugural_h1_lease_is_executable(self):
        registry = load('.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json')
        math_jobs = [x for x in registry['assignments'] if x['class'] == 'MATHEMATICAL_RESEARCH']
        self.assertEqual(len(math_jobs), 1)
        job = math_jobs[0]
        self.assertEqual(job['state'], 'LEASED')
        self.assertEqual(job['lease']['state'], 'LEASED')
        self.assertEqual(job['lease']['dispatch_id'], H1_DISPATCH_ID)
        self.assertEqual(job['lease']['agent_ref'], H1_AGENT_REF)
        self.assertEqual(job['lease']['dispatch_url'], H1_ISSUE_URL)
        self.assertEqual(job['lease']['return_url'], H1_ISSUE_URL)
        self.assertTrue(job['permissions']['hill_specific_mathematics'])
        self.assertFalse(job['permissions']['competition_submission'])
        self.assertFalse(job['permissions']['certification'])

    def test_h2_h7_math_remains_blocked(self):
        registry = load('.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json')
        self.assertEqual(registry['mathematics_release_policy']['current_math_jobs'], 0)
        self.assertEqual(registry['slot_binding_policy']['current_mapping'], 'UNRESOLVED')


if __name__ == '__main__':
    unittest.main()
