"""Guard against regression to CHAD's unsupported system Python 3.10."""
from pathlib import Path

INSTALLER = Path(__file__).resolve().parents[1] / "deploy" / "install-wsl.sh"


def test_managed_python_and_uv_install():
    contents = INSTALLER.read_text()
    assert "uv python install 3.12" in contents
    assert "uv venv --managed-python --python 3.12 .venv" in contents
    assert "uv pip install --python .venv/bin/python" in contents
    assert "python3 -m venv" not in contents


def test_failed_legacy_environment_preserved():
    contents = INSTALLER.read_text()
    assert "mv -- .venv" in contents
    assert "pyvenv.cfg" in contents
    assert "sys.version_info[:2] == (3, 12)" in contents
    assert "GCL_COMMANDER_GITHUB_ACTOR=fyremael" in contents
