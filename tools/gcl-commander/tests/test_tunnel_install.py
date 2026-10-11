"""Security regression for outbound-only official Secure MCP Tunnel deployment."""
from pathlib import Path
import subprocess
import os

ROOT = Path(__file__).resolve().parents[1]
DEPLOY = ROOT / "deploy"


def script(name):
    return DEPLOY / name


def test_bash_syntax_for_all_deployment_scripts():
    for path in DEPLOY.glob("*.sh"):
        p = subprocess.run(["bash", "-n", str(path)], capture_output=True)
        assert p.returncode == 0, (path.name, p.stderr.decode())


def test_refuse_source_without_damaging_parent_shell():
    for name in ("install-openai-tunnel-client-wsl.sh", "configure-openai-tunnel-wsl.sh", "activate-openai-tunnel-wsl.sh"):
        cmd = f"set -e; . '{script(name)}'; echo SHELL_SURVIVED"
        p = subprocess.run(["bash", "-c", cmd], capture_output=True, text=True)
        assert p.returncode == 0 and "SHELL_SURVIVED" in p.stdout, (name, p.stderr)


def test_tunnel_install_is_release_checksum_verified():
    text = script("install-openai-tunnel-client-wsl.sh").read_text()
    assert 'repo openai/tunnel-client' in text
    assert "SHA256SUMS.txt" in text
    assert "sha256sum -c" in text
    assert "unzip -p" in text
    assert "platform=linux-amd64" in text
    assert "platform=linux-arm64" in text
    assert "curl | sh" not in text


def test_tunnel_uses_stdio_and_explicit_write_disable():
    unit = (DEPLOY / "gcl-commander-tunnel.service").read_text()
    assert "ExecStart=%h/.local/bin/tunnel-client run --profile gcl-commander" in unit
    assert "GCL_COMMANDER_TRANSPORT=stdio" in unit
    assert "GCL_COMMANDER_PROJECT_WRITE=disabled" in unit
    assert "127.0.0.1:8765" not in unit
    assert "0.0.0.0" not in unit
    config = script("configure-openai-tunnel-wsl.sh").read_text()
    assert "--mcp-command" in config
    assert "read -r -s" in config
    assert "--control-plane-api-key" not in config


def test_no_shell_eval_for_runtime_credential_and_no_secret_logging():
    setup = script("configure-openai-tunnel-wsl.sh").read_text()
    activate = script("activate-openai-tunnel-wsl.sh").read_text()
    assert "source \"$secret\"" not in activate
    assert "CONTROL_PLANE_API_KEY=" in setup
    assert 'chmod 0600 "$secrets"' in setup
    assert '"$client" doctor --profile gcl-commander --explain' in activate
    assert 'grep -Fxq \'GCL_COMMANDER_PROJECT_WRITE=disabled\'' in activate


def test_tunnel_activation_requires_identity_and_service_readiness():
    activate = script("activate-openai-tunnel-wsl.sh").read_text()
    assert '"$root/.venv/bin/gcl-commander" doctor' in activate
    assert "systemctl --user enable --now" in activate
    assert "systemd not running in WSL" in activate
    assert "NoNewPrivileges=true" in (DEPLOY / "gcl-commander-tunnel.service").read_text()


def test_ordinary_failure_does_not_exit_caller_shell():
    cmd = f"""set -e
if bash '{script('configure-openai-tunnel-wsl.sh')}' </dev/null; then
  printf 'unexpected-success\\n'
else
  printf 'SHELL_SURVIVED\\n'
fi
"""
    env = os.environ.copy()
    env["HOME"] = "/tmp/nonexistent-gcl-commander-tunnel-test-home"
    p = subprocess.run(["bash", "-c", cmd], capture_output=True, text=True, env=env)
    assert p.returncode == 0 and "SHELL_SURVIVED" in p.stdout
