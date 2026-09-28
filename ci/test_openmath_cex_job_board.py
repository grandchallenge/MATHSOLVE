import unittest

from ci.validate_openmath_cex_job_board import (
    BASE_URL,
    ENTRYPOINT_URL,
    REGISTRY_URL,
    load,
    validate,
)


class OpenMathCEXJobBoardTest(unittest.TestCase):
    def test_preflight(self):
        self.assertEqual(validate(), [])

    def test_assignments_match_authoritative_pool(self):
        receipt = load('work_packages/OPENMATH_2026/H2_H7_AUTHORITATIVE_LIST_RECEIPT.json')
        registry = load('.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json')
        self.assertEqual(
            [x['external_hill_id'] for x in registry['assignments']],
            receipt['unresolved_source_pool'],
        )
        self.assertTrue(all(x['slot_binding'] is None for x in registry['assignments']))

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

    def test_external_workers_cannot_self_claim(self):
        registry = load('.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json')
        self.assertFalse(registry['lease_policy']['external_self_claim_allowed'])
        self.assertTrue(all(x['state'] == 'AVAILABLE_FOR_LEASE' for x in registry['assignments']))
        self.assertTrue(all(x['lease']['state'] == 'UNCLAIMED' for x in registry['assignments']))

    def test_unclaimed_lease_contains_no_hidden_locator(self):
        registry = load('.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json')
        for item in registry['assignments']:
            lease = item['lease']
            self.assertIsNone(lease['dispatch_url'])
            self.assertIsNone(lease['return_url'])

    def test_no_early_math_jobs(self):
        registry = load('.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json')
        self.assertEqual(registry['mathematics_release_policy']['current_math_jobs'], 0)
        for item in registry['assignments']:
            self.assertFalse(item['permissions']['hill_specific_mathematics'])
            self.assertIsNone(item['prerequisites']['source_lock'])


if __name__ == '__main__':
    unittest.main()
