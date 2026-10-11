"""Regression invariants for the CHAD-proven Linux-detached Windows startup."""
from pathlib import Path
import hashlib
import subprocess

ROOT = Path(__file__).resolve().parents[1]
DEPLOY = ROOT / "deploy"
ORIGINAL_SHA256 = "01f4d173613c732fa4203246f47eb1fc645d29d4677144cfd347c36e18df386a"


def test_proven_detached_launcher_bytes():
    script = DEPLOY / "gcl-chad-detached-start.sh"
    assert hashlib.sha256(script.read_bytes()).hexdigest() == ORIGINAL_SHA256
    assert subprocess.run(["bash", "-n", str(script)], capture_output=True).returncode == 0


def test_singleton_and_service_not_bypassed():
    s = (DEPLOY / "gcl-chad-detached-start.sh").read_text()
    assert 'nohup setsid -f /bin/bash "$SUP"' in s
    assert 'flock -n "$STATE/tunnel-supervisor.lock"' in s
    assert 'ALREADY_READY:' in s
    assert 'LINUX_DETACH_READY:' in s
    assert 'readyz' in s
    assert 'CONTROL_PLANE_API_KEY=' not in s
    assert 'GCL_COMMANDER_PROJECT_WRITE=enabled' not in s
    assert 'eval ' not in s


def test_windows_logon_scope_and_verified_launch():
    s = (DEPLOY / "install-chad-detached-autostart.ps1").read_text()
    for token in ("HKCU:", "Software\\Microsoft\\Windows\\CurrentVersion\\Run",
                  "READY_AFTER_WSL_RETURN", "READY_AFTER_FURTHER_DELAY",
                  "TUNNEL_CLIENT_PID_EXISTS", "SUPERVISOR_LOCK_HELD",
                  "Disable-ScheduledTask", "Validate-PS1"):
        assert token in s
    assert ORIGINAL_SHA256 in s
    assert '/home/jim/gcl-commander/deploy/gcl-chad-detached-start.sh' in s
    assert '/mnt/d/Downloads/' not in s
    assert 'New-ScheduledTaskAction' not in s
    assert 'Register-ScheduledTask' not in s
    assert 'Get-ScheduledTask' in s


def test_old_installer_disabled_and_logon_shim_short():
    old = (DEPLOY / "install-chad-autostart.ps1").read_text()
    shim = (DEPLOY / "start-at-logon.ps1").read_text()
    assert 'LEGACY_WINDOWS_TASK_INSTALLER_DISABLED' in old
    assert 'Register-ScheduledTask' not in old
    assert '/home/jim/.local/bin/gcl-chad-detached-start.sh' in shim
    assert 'CONTROL_PLANE_API_KEY' not in shim
    assert 'sk-proj-' not in shim
