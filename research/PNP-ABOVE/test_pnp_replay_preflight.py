import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from PNP_REPLAY_PREFLIGHT import direct_runner_guard, bounded_run

class ReplayGuardTest(unittest.TestCase):
    def test_wsl_denied_even_with_no_environment_marker(self):
        with patch("platform.release",return_value="6.6.87.2-microsoft-standard-WSL2"), patch.dict(os.environ,{},clear=True):
            with self.assertRaisesRegex(SystemExit,"CHAD_SSD_REQUIRED"):
                direct_runner_guard()
    def test_wsl_environment_denied(self):
        with patch("platform.release",return_value="6.1.0"), patch.dict(os.environ,{"WSL_INTEROP":"/run/test"},clear=True):
            with self.assertRaisesRegex(SystemExit,"CHAD_SSD_REQUIRED"):
                direct_runner_guard()
    def test_native_linux_allowed(self):
        with patch("platform.release",return_value="6.1.0"), patch.dict(os.environ,{},clear=True):
            direct_runner_guard()
    def test_timeout_is_durable_and_no_retry(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)
            with self.assertRaisesRegex(SystemExit,"PNP_REPLAY_TIMEOUT"):
                bounded_run([sys.executable,"-c","import time; time.sleep(2)"],cwd=p,
                            env=os.environ.copy(),log=p/"log",receipt=p/"receipt",seconds=0.1)
            records=[json.loads(x) for x in (p/"receipt").read_text().splitlines()]
            self.assertEqual(len(records),1)
            self.assertEqual(records[0]["outcome"],"timeout")
    def test_success_receipt(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)
            bounded_run([sys.executable,"-c","print('ok')"],cwd=p,env=os.environ.copy(),
                        log=p/"log",receipt=p/"receipt",seconds=5)
            self.assertEqual(json.loads((p/"receipt").read_text())["outcome"],"passed")

if __name__ == "__main__": unittest.main()
