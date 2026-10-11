from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]

def test_shell_syntax():
    script = ROOT/'deploy/supervise-openai-tunnel-wsl.sh'
    r=subprocess.run(['bash','-n',str(script)],capture_output=True,text=True)
    assert r.returncode==0,r.stderr

def test_script_guards_and_recovery():
    s=(ROOT/'deploy/supervise-openai-tunnel-wsl.sh').read_text()
    for token in ('flock -n 9','GCL_COMMANDER_PROJECT_WRITE=disabled',
                  'GCL_COMMANDER_REPO_WRITE=disabled','chmod 600 "$LOG"',
                  'CONTROL_PLANE_API_KEY=','run --profile gcl-commander',
                  'trap stop TERM INT','readyz'):
        assert token in s
    assert not any(line.lstrip().startswith(('eval ', 'source ', '. ')) for line in s.splitlines() if not line.lstrip().startswith('#'))

def test_legacy_windows_task_installer_is_blocked():
    s=(ROOT/'deploy/install-chad-autostart.ps1').read_text()
    assert 'LEGACY_WINDOWS_TASK_INSTALLER_DISABLED' in s
    assert 'Register-ScheduledTask' not in s

def test_failed_supervisor_preflight_does_not_close_calling_shell(tmp_path):
    script = ROOT/'deploy/supervise-openai-tunnel-wsl.sh'
    command = f'''set -e
if bash "{script}"; then
  echo UNEXPECTED_SUCCESS
else
  echo SHELL_SURVIVED
fi
'''
    import os
    env=os.environ.copy()
    env['HOME']=str(tmp_path)
    p=subprocess.run(['bash','-c',command],env=env,capture_output=True,text=True)
    assert p.returncode==0 and 'SHELL_SURVIVED' in p.stdout
    assert 'BLOCKED:' in p.stderr

def test_accidental_source_preserves_shell():
    script = ROOT/'deploy/supervise-openai-tunnel-wsl.sh'
    p=subprocess.run(['bash','-c',f'set +e; . "{script}"; echo SHELL_SURVIVED'],capture_output=True,text=True)
    assert p.returncode==0 and 'SHELL_SURVIVED' in p.stdout

def test_publish_proposal_protects_main_and_omits_secrets():
    s=(ROOT/'deploy/publish-source-pr-wsl.sh').read_text()
    assert 'gh pr create' in s and '--draft' in s
    assert 'git push -q origin "HEAD:refs/heads/$BRANCH"' in s
    assert 'git checkout -q -b "$BRANCH"' in s
    assert 'git push origin main' not in s
    assert 'tunnel.env' not in s
