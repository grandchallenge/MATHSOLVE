import json
import unittest
from pathlib import Path

from ci.validate_gcl_erdos3_frontier import ROOT, validate

class GclErdos3FrontierTest(unittest.TestCase):
    def test_frontier_tranche(self):
        self.assertEqual(validate(),[])

    def test_no_replay_successor_for_closed_f01(self):
        tranche=json.loads((ROOT/'work_packages/GCL_ERDOS3/results/E3-TRANCHE-01.json').read_text())
        self.assertEqual(tranche['results']['E3-F01']['frontier_action'],'CLOSED_NO_SUCCESSOR')

    def test_b01_requires_only_one_named_independent_verification(self):
        frontier=json.loads((ROOT/'work_packages/GCL_ERDOS3/FRONTIER.json').read_text())
        rows={x['id']:x for x in frontier['nodes']}
        self.assertEqual(rows['E3-V-B01']['status'],'OPEN')
        self.assertEqual(rows['E3-B-SCALE-LOCAL']['independent_verification'],'OPEN__E3-V01')
        self.assertEqual(frontier['active_frontier'],['E3-V-B01','E3-B-AP'])

if __name__=='__main__':
    unittest.main()
