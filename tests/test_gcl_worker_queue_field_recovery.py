import subprocess
import unittest
from unittest.mock import patch
from ci import gcl_worker_queue_field_recovery as m


class FieldRecoveryTests(unittest.TestCase):
    def test_already_clear_no_write(self):
        with patch.object(m,"field_state",return_value=None),patch.object(m,"command") as call:
            self.assertEqual(m.apply_one("o/r",10,3,None),"ALREADY_CLEAR")
            call.assert_not_called()
    def test_timeout_applied_set(self):
        with patch.object(m,"field_state",side_effect=[None,{"value":"RETURNED"}]),patch.object(m,"command",side_effect=subprocess.TimeoutExpired("gh",60)) as call:
            self.assertEqual(m.apply_one("o/r",10,3,"RETURNED"),"VERIFIED_SET")
            call.assert_called_once()
    def test_timeout_no_effect_no_retry(self):
        with patch.object(m,"field_state",side_effect=[None,None]),patch.object(m,"command",side_effect=subprocess.TimeoutExpired("gh",60)) as call:
            with self.assertRaises(m.UncertainFieldMutation):
                m.apply_one("o/r",10,3,"RETURNED")
            call.assert_called_once()
    def test_explicit_denial_no_retry(self):
        denied=subprocess.CompletedProcess([],1,"","HTTP 403 forbidden")
        with patch.object(m,"field_state",return_value=None),patch.object(m,"command",return_value=denied) as call:
            with self.assertRaisesRegex(m.UncertainFieldMutation,"denial"):
                m.apply_one("o/r",10,3,"RETURNED")
            call.assert_called_once()
    def test_readback_failure_no_repeat(self):
        with patch.object(m,"field_state",side_effect=[None,ConnectionError("offline")]),patch.object(m,"command",side_effect=subprocess.TimeoutExpired("gh",60)) as call:
            with self.assertRaises(ConnectionError):
                m.apply_one("o/r",10,3,"RETURNED")
            call.assert_called_once()
    def test_already_set_no_write(self):
        with patch.object(m,"field_state",return_value={"value":"RETURNED"}),patch.object(m,"command") as call:
            self.assertEqual(m.apply_one("o/r",10,3,"RETURNED"),"ALREADY_SET")
            call.assert_not_called()
    def test_scheduled_reap_uses_recovery_helper(self):
        from pathlib import Path
        workflow = Path(__file__).resolve().parents[1] / ".github/workflows/gcl-worker-queue.yml"
        source = workflow.read_text(encoding="utf-8")
        section = source.split("name: Reconcile reservations and Issue Fields", 1)[1]
        section = section.split("name: Audit real active Mathematics reservations", 1)[0]
        self.assertIn('python ci/gcl_worker_queue_field_recovery.py', section)
        self.assertIn('--projection "$RUNNER_TEMP/projection-$n.json"', section)
        self.assertNotIn('gh api --method POST', section)
        self.assertNotIn('gh api --method DELETE', section)

    def test_scheduled_reap_multiple_projection_steps_fail_closed(self):
        import json
        import tempfile
        from pathlib import Path
        projection = {"queue_managed": True,
                      "issue_field_values": [{"field_id": 101, "value": "AVAILABLE"}],
                      "clear_field_ids": [102]}
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "projection.json"
            p.write_text(json.dumps(projection))
            with patch("sys.argv", ["field-recovery", "--repo", "o/r", "--issue", "10", "--projection", str(p)]), patch.object(m, "apply_one", side_effect=["VERIFIED_SET", m.UncertainFieldMutation("remote unknown")]) as apply:
                with self.assertRaises(m.UncertainFieldMutation):
                    m.main()
                self.assertEqual(apply.call_count, 2)

if __name__=="__main__":
    unittest.main()
