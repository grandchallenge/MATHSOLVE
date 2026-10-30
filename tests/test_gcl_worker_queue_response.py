import json
import subprocess
import unittest
from unittest.mock import patch
from ci import gcl_worker_queue_response as mod


class ResponseRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.body = mod.response_body("CLAIM ACCEPTED\n", 42)
        self.row = {"id": 99, "body": self.body}

    def test_preexisting_response_not_reposted(self):
        with patch.object(mod, "history", return_value=[self.row]), patch.object(mod, "call") as invoke:
            self.assertEqual(mod.post_once("o/r", 8, 42, "CLAIM ACCEPTED\n")["outcome"], "ALREADY_POSTED")
        invoke.assert_not_called()

    def test_lost_ack_with_remote_effect(self):
        with patch.object(mod, "history", side_effect=[[], [self.row]]), patch.object(
            mod, "call", side_effect=subprocess.TimeoutExpired("gh", 60)
        ) as invoke:
            self.assertEqual(mod.post_once("o/r", 8, 42, "CLAIM ACCEPTED\n")["comment_id"], 99)
        invoke.assert_called_once()

    def test_lost_ack_without_effect_no_duplicate(self):
        with patch.object(mod, "history", side_effect=[[], []]), patch.object(
            mod, "call", side_effect=subprocess.TimeoutExpired("gh", 60)
        ) as invoke:
            with self.assertRaises(mod.ResponseUncertain):
                mod.post_once("o/r", 8, 42, "CLAIM ACCEPTED\n")
        invoke.assert_called_once()

    def test_explicit_denial_not_retried(self):
        denied = subprocess.CompletedProcess([], 1, "", "HTTP 403 forbidden")
        with patch.object(mod, "history", return_value=[]), patch.object(mod, "call", return_value=denied) as invoke:
            with self.assertRaisesRegex(mod.ResponseUncertain, "denial"):
                mod.post_once("o/r", 8, 42, "CLAIM ACCEPTED\n")
        invoke.assert_called_once()

    def test_conflicting_response_fails_closed(self):
        with self.assertRaises(mod.ResponseUncertain):
            mod.reconcile([{"id": 10, "body": mod.response_body("RELEASE ACCEPTED", 42)}], self.body, 42)

    def test_duplicate_remote_responses_fail_closed(self):
        with self.assertRaises(mod.ResponseUncertain):
            mod.reconcile([self.row, {"id": 100, "body": self.body}], self.body, 42)

    def test_success_requires_remote_effect(self):
        success = subprocess.CompletedProcess([], 0, '{"id":99}', "")
        with patch.object(mod, "history", side_effect=[[], []]), patch.object(mod, "call", return_value=success) as invoke:
            with self.assertRaises(mod.ResponseUncertain):
                mod.post_once("o/r", 8, 42, "CLAIM ACCEPTED\n")
        invoke.assert_called_once()


if __name__ == "__main__":
    unittest.main()
