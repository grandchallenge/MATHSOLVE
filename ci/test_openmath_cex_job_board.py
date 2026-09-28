import unittest

from ci.validate_openmath_cex_job_board import load, validate


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

    def test_external_workers_cannot_self_claim(self):
        registry = load('.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json')
        self.assertFalse(registry['lease_policy']['external_self_claim_allowed'])
        self.assertTrue(all(x['state'] == 'AVAILABLE_FOR_LEASE' for x in registry['assignments']))
        self.assertTrue(all(x['lease']['state'] == 'UNCLAIMED' for x in registry['assignments']))

    def test_no_early_math_jobs(self):
        registry = load('.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json')
        self.assertEqual(registry['mathematics_release_policy']['current_math_jobs'], 0)
        for item in registry['assignments']:
            self.assertFalse(item['permissions']['hill_specific_mathematics'])
            self.assertIsNone(item['prerequisites']['source_lock'])


if __name__ == '__main__':
    unittest.main()
