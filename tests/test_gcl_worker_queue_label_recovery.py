import subprocess
import unittest
from unittest.mock import patch
from ci import gcl_worker_queue_label_recovery as m


class LabelRecoveryTests(unittest.TestCase):
    def test_already_present_no_mutation(self):
        with patch.object(m,"current_labels",return_value={"reserved"}),patch.object(m,"gh") as run:
            self.assertEqual(m.set_label("o/r",1,"reserved",True),"ALREADY_CORRECT")
            run.assert_not_called()

    def test_timeout_applied_once(self):
        with patch.object(m,"current_labels",side_effect=[set(),{"reserved"}]),patch.object(m,"gh",side_effect=subprocess.TimeoutExpired("gh",60)) as run:
            self.assertEqual(m.set_label("o/r",1,"reserved",True),"VERIFIED")
            run.assert_called_once()

    def test_timeout_without_remote_effect_fails_closed(self):
        with patch.object(m,"current_labels",side_effect=[set(),set()]),patch.object(m,"gh",side_effect=subprocess.TimeoutExpired("gh",60)) as run:
            with self.assertRaises(m.LabelUncertain):
                m.set_label("o/r",1,"reserved",True)
            run.assert_called_once()

    def test_explicit_denial_not_retried(self):
        deny=subprocess.CompletedProcess([],1,"","403 forbidden")
        with patch.object(m,"current_labels",return_value=set()),patch.object(m,"gh",return_value=deny) as run:
            with self.assertRaisesRegex(m.LabelUncertain,"denial"):
                m.set_label("o/r",1,"reserved",True)
            run.assert_called_once()

    def test_readback_unavailable_no_replay(self):
        with patch.object(m,"current_labels",side_effect=[{"reserved"},ConnectionError("offline")]),patch.object(m,"gh",side_effect=subprocess.TimeoutExpired("gh",60)) as run:
            with self.assertRaises(ConnectionError):
                m.set_label("o/r",1,"reserved",False)
            run.assert_called_once()

    def test_conflicting_labels_rejected_before_mutation(self):
        with patch.object(m,"set_label") as mutate:
            with self.assertRaises(ValueError):
                m.reconcile("o/r",1,["available"],["available"])
            mutate.assert_not_called()

    def test_scheduled_and_command_wiring(self):
        from pathlib import Path
        y=(Path(__file__).resolve().parents[1]/".github/workflows/gcl-worker-queue.yml").read_text()
        self.assertEqual(y.count("python ci/gcl_worker_queue_label_recovery.py"),5)
        self.assertNotIn('gh issue edit "$n"',y)
        self.assertNotIn('gh issue edit "$ISSUE_NUMBER"',y)


if __name__=="__main__":
    unittest.main()
