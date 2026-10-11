import base64
import pytest
from unittest.mock import patch
from gcl_commander.repositories import (
    repository_head, repository_read_file, repository_pull_request, repository_document_proposal)
from gcl_commander.core import Boundary

SHA = 'a'*40

def fake_json(method, url, data=None):
    if url=='repos/grandchallenge/MATHSOLVE': return {'default_branch':'main'}
    if url=='repos/grandchallenge/MATHSOLVE/git/ref/heads/main': return {'object':{'sha':SHA}}
    if '/contents/docs/test.md?' in url:
        return {'type':'file','encoding':'base64','size':5,'content':base64.b64encode(b'hello').decode(),'sha':'blob123'}
    if '/pulls/77' in url:
        return {'head':{'sha':SHA},'base':{'sha':'b'*40,'ref':'main'},'state':'open','merged':False,'user':{'login':'fyremael'},'html_url':'https://github.com/'}
    raise AssertionError(url)

@patch('gcl_commander.repositories._json_api',side_effect=fake_json)
@patch('gcl_commander.repositories.assert_identity',return_value={'login':'fyremael'})
@patch('gcl_commander.repositories.receipt',return_value='/tmp/test-receipt')
def test_exact_repo_head(_receipt,_actor,_gh):
    assert repository_head('grandchallenge/MATHSOLVE')['head_sha']==SHA
    assert repository_head('grandchallenge/MATHSOLVE')['receipt']=='/tmp/test-receipt'

@patch('gcl_commander.repositories._json_api',side_effect=fake_json)
@patch('gcl_commander.repositories.assert_identity',return_value={'login':'fyremael'})
def test_file_bound_sha(_actor,_gh):
    ret=repository_read_file('grandchallenge/MATHSOLVE','docs/test.md',SHA)
    assert ret['content']=='hello' and ret['mutation'] is False
    with pytest.raises(Boundary,match='STALE_PROTECTED_HEAD'):
        repository_read_file('grandchallenge/MATHSOLVE','docs/test.md','b'*40)

@pytest.mark.parametrize('path', ['.env','docs/../foo.md','/etc/passwd','governance/.private','docs\\foo.md','secrets/key'])
def test_reject_sensitive_path(path):
    with pytest.raises(Boundary): repository_read_file('grandchallenge/MATHSOLVE',path,SHA)

@pytest.mark.parametrize('repo',['other/repo','grandchallenge/.github','grandchallenge/INTELLECT'])
def test_reject_unknown_repo(repo):
    with pytest.raises(Boundary,match='REPOSITORY_NOT_APPROVED'):repository_head(repo)

@patch('gcl_commander.repositories._json_api',side_effect=fake_json)
@patch('gcl_commander.repositories.assert_identity',return_value={'login':'fyremael'})
@patch('gcl_commander.repositories._json_api_reviews',return_value=[{'actor':'jimsteeg','state':'APPROVED','commit_sha':SHA}])
def test_pr_readback(_reviews,_actor,_gh):
    r=repository_pull_request('grandchallenge/MATHSOLVE',77)
    assert r['head']==SHA and r['reviews'][0]['actor']=='jimsteeg' and not r['mutation']

def test_write_gated_even_with_flags(monkeypatch):
    monkeypatch.setenv('GCL_COMMANDER_REPO_WRITE','enabled')
    with pytest.raises(Boundary,match='NOT_ACTIVATED'):
        repository_document_proposal('grandchallenge/MATHSOLVE','docs/test.md',SHA,'some-change', '# Hi')
