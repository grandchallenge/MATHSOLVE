from unittest.mock import patch
import pytest
from gcl_commander.queue_views import view_audit,EXPECTED,EXPECTED_PROJECT
from gcl_commander.core import Boundary


def fixture():
    return {'organization':{'projectV2':{'id':EXPECTED_PROJECT,'views':{
        'pageInfo':{'hasNextPage':False},'nodes':[
            {'id':EXPECTED['EDITORIAL'],'name':'EDITORIAL','filter':'is:open "Queue Class":Editorial'},
            {'id':EXPECTED['MATHEMATICS'],'name':'MATHEMATICS','filter':'is:open "Queue Class":Mathematics'},
            {'id':EXPECTED['AVAILABLE'],'name':'AVAILABLE','filter':'is:open "GCL State":AVAILABLE'},
        ]}}}}

@patch('gcl_commander.queue_views._graphql',return_value=fixture())
@patch('gcl_commander.queue_views.assert_identity',return_value={'login':'fyremael'})
@patch('gcl_commander.queue_views.receipt',return_value='/private/receipt')
def test_real_view_id_filter_patterns(_receipt,_auth,_api):
    r=view_audit()
    assert r['readback'] and r['mutation'] is False and len(r['views'])==3
    assert r['receipt']=='/private/receipt'

@patch('gcl_commander.queue_views.assert_identity',return_value={'login':'fyremael'})
@patch('gcl_commander.queue_views.receipt',return_value='/private/receipt')
def test_view_swapping_denied(_receipt,_auth):
    d=fixture()
    d['organization']['projectV2']['views']['nodes'][0]['id']='tampered'
    with patch('gcl_commander.queue_views._graphql',return_value=d):
        with pytest.raises(Boundary,match='IDENTITY_DRIFT'):view_audit()

a=[('pageInfo',{'hasNextPage':True}),('nodes',[])]
@pytest.mark.parametrize('field,value',a)
@patch('gcl_commander.queue_views.assert_identity',return_value={'login':'fyremael'})
def test_partial_views_denied(_auth,field,value):
    d=fixture();d['organization']['projectV2']['views'][field]=value
    with patch('gcl_commander.queue_views._graphql',return_value=d):
        with pytest.raises(Boundary):view_audit()

@patch('gcl_commander.queue_views.assert_identity',return_value={'login':'fyremael'})
def test_wrong_semantic_filter_denied(_auth):
    d=fixture()
    d['organization']['projectV2']['views']['nodes'][0]['filter']='"Queue Class":Mathematics'
    with patch('gcl_commander.queue_views._graphql',return_value=d):
        with pytest.raises(Boundary,match='FILTER_MISMATCH'):view_audit()
