import json
import tempfile
import unittest
from pathlib import Path

from ci.openmath_lifecycle_candidate import LifecycleCandidateError, plan
from ci.validate_openmath_event_window_activation import ROOT, validate

class EventWindowActivationTests(unittest.TestCase):
    def test_terminal_concordance(self):
        self.assertEqual(validate(),[])

    def test_no_open_replay_leases_remain(self):
        registry=json.loads((ROOT/'.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json').read_text())
        scripts=list(registry['launch_contract']['current_scripts'].values())
        scripts+=list(registry['launch_contract'].get('support_scripts',{}).values())
        self.assertEqual(len(scripts),9)
        self.assertTrue(all(x['executable'] is False for x in scripts))
        self.assertEqual(registry['mathematics_release_policy']['summary']['leased_not_launched_agents'],0)

    def test_automatic_successor_generation_is_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)
            (p/'META.json').write_text(json.dumps({'comment_id':1}))
            (p/'RECEIPT.json').write_text(json.dumps({
                'assignment_id':'OM26-H7-WP06',
                'dispatch_id':'OM26-H7-WP06-IA-001'
            }))
            (p/'RAW.md').write_text('GCL-CONTRIBUTION-RESULT/1\n')
            with self.assertRaisesRegex(LifecycleCandidateError,'protected frontier disposition required'):
                plan(p,ROOT)

if __name__=='__main__':
    unittest.main()
