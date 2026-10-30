"""Regression for fail-closed comment census in worker queue workflows."""
import subprocess
from pathlib import Path
import unittest


WORKFLOW = Path(__file__).resolve().parents[1] / ".github/workflows/gcl-worker-queue.yml"


class QueueCommentCensusTests(unittest.TestCase):
    def test_command_and_scheduled_reads_require_pipefail(self):
        content = WORKFLOW.read_text(encoding="utf-8")
        command = content.split("- name: Fetch issue comment history", 1)[1].split("- name: Evaluate queue command", 1)[0]
        scheduled = content.split("- name: Reconcile reservations and Issue Fields", 1)[1].split("- name: Audit real active Mathematics reservations", 1)[0]
        for section in (command, scheduled):
            self.assertIn("set -euo pipefail", section)
            self.assertIn("gh api --paginate", section)
            self.assertIn("jq -s 'add'", section)

    def test_upstream_failure_cannot_be_hidden_by_downstream_success(self):
        result = subprocess.run(["bash", "-c", "set -euo pipefail; false | cat >/dev/null"],
                                check=False, capture_output=True)
        self.assertNotEqual(result.returncode, 0)

    def test_empty_or_failed_input_does_not_pass_as_complete_census(self):
        result = subprocess.run(["bash", "-c", "set -euo pipefail; (exit 22) | cat >/dev/null; echo VERIFIED"],
                                check=False, capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("VERIFIED", result.stdout)


if __name__ == "__main__":
    unittest.main()
