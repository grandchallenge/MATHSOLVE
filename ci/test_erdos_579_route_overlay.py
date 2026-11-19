"""Exact-provenance tests for the bounded Erdős #579 MATHCERT successor."""
import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate_vgse_activation as v


class Erdos579SuccessorRouteTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(v.ERDOS_OVERLAY_PATH.read_text())

    def _tamper(self, mutate):
        altered = copy.deepcopy(self.data)
        mutate(altered)
        with tempfile.TemporaryDirectory(prefix='gcl-erdos579-') as temp:
            path = Path(temp) / 'overlay.json'
            path.write_text(json.dumps(altered))
            return v.erdos_overlay_errors(overlay_path=path)

    def test_protected_route_expected_exactly_once(self):
        self.assertEqual(v.erdos_overlay_errors(), [])
        self.assertEqual(self.data['campaign']['route_id'], 'MC-ROUTE-ERDOS-579-DISPROOF-001')
        self.assertIs(self.data['campaign']['route_registry_entry_present'], True)

    def test_pending_cannot_certify(self):
        self.assertEqual(self.data['campaign']['route_state'], 'pending')
        self.assertIsNone(self.data['campaign']['cert_output'])
        self.assertIs(self.data['campaign']['may_issue_certificate_output'], False)
        self.assertIs(self.data['campaign']['mathematical_target_proved'], False)

    def test_no_unregistered_substitution(self):
        errors = self._tamper(lambda x: x['campaign'].__setitem__('route_registry_entry_present', False))
        self.assertTrue(any('registered-route' in e for e in errors), errors)

    def test_no_forged_certificate(self):
        errors = self._tamper(lambda x: x['campaign'].__setitem__('may_issue_certificate_output', True))
        self.assertTrue(any('prohibited authority inflation' in e for e in errors), errors)

    def test_no_handoff_hash_drift(self):
        errors = self._tamper(lambda x: x['campaign']['handoff'].__setitem__('digest', '0'*40))
        self.assertTrue(any('handoff identity drift' in e for e in errors), errors)

    def test_no_stale_route_identity(self):
        errors = self._tamper(lambda x: x['current_authority'].__setitem__('digest', '0'*40))
        self.assertTrue(any('was expected' in e or 'does not match' in e for e in errors), errors)


if __name__ == '__main__':
    unittest.main()
