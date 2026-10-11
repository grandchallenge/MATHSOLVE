"""The CHAD CLI has no implicit state mutation or unguarded fallback route."""
from unittest.mock import patch
import json
import sys
import pytest
from gcl_commander import cli


def invoke(monkeypatch, argv):
    monkeypatch.setattr(sys,'argv',['gcl-commander',*argv])
    return cli.main()


def test_views_cli_readonly(monkeypatch,capsys):
    with patch('gcl_commander.queue_views.view_audit',return_value={'operation':'views','mutation':False,'receipt':'fixed'}) as read:
        invoke(monkeypatch,['views'])
    read.assert_called_once()
    r=json.loads(capsys.readouterr().out)
    assert r['operation']=='views' and r['mutation'] is False


def test_head_cli_readonly(monkeypatch,capsys):
    with patch('gcl_commander.repositories.repository_head',return_value={'head_sha':'a'*40,'mutation':False,'receipt':'fixed'}) as read:
        invoke(monkeypatch,['repo-head','grandchallenge/MATHSOLVE'])
    read.assert_called_once_with('grandchallenge/MATHSOLVE')
    assert json.loads(capsys.readouterr().out)['head_sha']=='a'*40


def test_reconcile_apply_denied_without_write(monkeypatch):
    monkeypatch.delenv('GCL_COMMANDER_PROJECT_WRITE',raising=False)
    with patch('gcl_commander.cli.reconcile') as write:
        with pytest.raises(SystemExit) as ex:
            invoke(monkeypatch,['reconcile','--expected-total','1311','--apply'])
    assert ex.value.code==2
    write.assert_not_called()


def test_pr_and_file_need_named_args(monkeypatch):
    for cmd in (['repo-file','grandchallenge/MATHSOLVE','README.md'],
                ['repo-pr','grandchallenge/MATHSOLVE']):
        with pytest.raises(SystemExit) as e: invoke(monkeypatch,cmd)
        assert e.value.code==2
