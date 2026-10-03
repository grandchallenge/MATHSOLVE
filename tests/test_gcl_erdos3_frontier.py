import json
import unittest
from pathlib import Path

from ci.validate_gcl_erdos3_frontier import ROOT, validate

class GclErdos3FrontierTest(unittest.TestCase):
    def test_frontier_after_e3_v01(self):
        self.assertEqual(validate(),[])

    def test_f01_has_no_replay_successor(self):
        tranche=json.loads((ROOT/'work_packages/GCL_ERDOS3/results/E3-TRANCHE-01.json').read_text())
        self.assertEqual(tranche['results']['E3-F01']['frontier_action'],'CLOSED_NO_SUCCESSOR')

    def test_b01_verification_budget_is_closed(self):
        frontier=json.loads((ROOT/'work_packages/GCL_ERDOS3/FRONTIER.json').read_text())
        campaign=json.loads((ROOT/'work_packages/GCL_ERDOS3/CAMPAIGN.json').read_text())
        rows={x['id']:x for x in frontier['nodes']}
        self.assertEqual(rows['E3-V-B01']['status'],'CLOSED')
        self.assertEqual(rows['E3-V-B01']['disposition'],'VERIFIED')
        self.assertEqual(rows['E3-B-SCALE-LOCAL']['independent_verification'],'VERIFIED__E3-V01')
        self.assertEqual(rows['E3-B-AP-THRESHOLD']['independent_verification'],'VERIFIED__E3-V01')
        self.assertEqual(frontier['active_frontier'],['E3-B-AP'])
        self.assertEqual(campaign['current_frontier'],['E3-B-AP'])
        self.assertEqual(campaign['verification_dispatches']['E3-V01']['state'],'CLOSED_VERIFIED')

if __name__=='__main__':
    unittest.main()
