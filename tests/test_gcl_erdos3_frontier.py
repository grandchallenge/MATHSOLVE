import unittest
from ci.validate_gcl_erdos3_frontier import validate

class GclErdos3FrontierTest(unittest.TestCase):
    def test_frontier_reset(self):
        self.assertEqual(validate(),[])

if __name__=='__main__':
    unittest.main()
