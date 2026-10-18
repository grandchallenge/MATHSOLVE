import json
import unittest
from ci.validate_gcl_erdos3_frontier import ROOT, validate

class GclErdos3FrontierTest(unittest.TestCase):
    def test_frontier_after_b02_upgrade(self):
        self.assertEqual(validate(),[])

    def test_b01_verification_remains_closed(self):
        frontier=json.loads((ROOT/'work_packages/GCL_ERDOS3/FRONTIER.json').read_text())
        rows={x['id']:x for x in frontier['nodes']}
        self.assertEqual(rows['E3-V-B01']['status'],'CLOSED')
        self.assertEqual(rows['E3-B-SCALE-LOCAL']['independent_verification'],'VERIFIED__E3-V01')

    def test_b02_exposes_exact_k4_series_frontier(self):
        frontier=json.loads((ROOT/'work_packages/GCL_ERDOS3/FRONTIER.json').read_text())
        campaign=json.loads((ROOT/'work_packages/GCL_ERDOS3/CAMPAIGN.json').read_text())
        rows={x['id']:x for x in frontier['nodes']}
        self.assertEqual(rows['E3-B-AP']['status'],'PROVED')
        self.assertEqual(rows['E3-Q4-SERIES']['status'],'OPEN')
        self.assertEqual(rows['E3-V-B02']['status'],'OPEN')
        self.assertEqual(frontier['active_frontier'],['E3-V-B02','E3-Q4-SERIES'])
        self.assertEqual(campaign['current_frontier'],['E3-V-B02','E3-Q4-SERIES'])

if __name__=='__main__':
    unittest.main()
