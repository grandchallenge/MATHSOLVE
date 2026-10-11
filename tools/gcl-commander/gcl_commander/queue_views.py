"""Live, read-only Project V2 view identity/filter integrity checks.

Source identities are the protected Council Clerk #2563 record; no view creation.
"""
from __future__ import annotations
import re
from .core import Boundary, _graphql, assert_identity, receipt

EXPECTED_PROJECT = 'PVT_kwDOB9Ao_c4Blwur'
EXPECTED = {
    'EDITORIAL':'PVTV_lADOB9Ao_c4BlwurzgMAfZU',
    'MATHEMATICS':'PVTV_lADOB9Ao_c4BlwurzgMAfZY',
    'AVAILABLE':'PVTV_lADOB9Ao_c4BlwurzgL64bo',
}
QUERY = '''query { organization(login:"grandchallenge") {
  projectV2(number:2) { id views(first:100) {
    pageInfo {hasNextPage}
    nodes {id name filter}
  }}
}}'''


def view_audit() -> dict:
    actor = assert_identity()
    data = _graphql(QUERY)
    project = (data.get('organization') or {}).get('projectV2')
    if not project or project.get('id') != EXPECTED_PROJECT:
        raise Boundary('PROJECT_VIEW_IDENTITY_DRIFT')
    views = project.get('views') or {}
    if (views.get('pageInfo') or {}).get('hasNextPage') is not False:
        raise Boundary('PROJECT_VIEWS_INCOMPLETE')
    nodes = views.get('nodes') or []
    found = {}
    for name, view_id in EXPECTED.items():
        matching = [v for v in nodes if v and v.get('name','').upper()==name]
        if len(matching)!=1 or matching[0].get('id')!=view_id:
            raise Boundary(f'PROJECT_SAVED_VIEW_IDENTITY_DRIFT:{name}')
        f = matching[0].get('filter')
        if not isinstance(f,str):
            raise Boundary(f'PROJECT_VIEW_FILTER_MISSING:{name}')
        field = 'Queue Class' if name!='AVAILABLE' else 'GCL State'
        value = name.title() if name!='AVAILABLE' else 'AVAILABLE'
        # Supports both quoted multi-word field names and unquoted field names.
        pat = r'(?i)(?:"'+re.escape(field)+r'"|'+re.escape(field)+r')\s*:\s*"?'+re.escape(value)+r'"?(?:\s|$)'
        if not re.search(pat,f.strip()+' '):
            raise Boundary(f'PROJECT_VIEW_FILTER_MISMATCH:{name}')
        found[name]={'id':view_id,'filter':f}
    result={'operation':'project_queue_views_readback', 'project_id':EXPECTED_PROJECT,
            'operator':actor['login'],'views':found,'readback':True,'mutation':False}
    result['receipt']=receipt(result)
    return result
