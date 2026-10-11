import pytest
from gcl_commander.core import classify, Boundary, _targets

def test_solve_reserved_math():
    assert classify("grandchallenge/MATHSOLVE", "Proof route", ["gcl-job"])[0] == "Mathematics"

def test_erdos_direct_but_mathematics():
    assert classify("grandchallenge/MATH-PROGRAMME", "ERDOS-CATALOGUE-0041-S01", ["gcl-job", "gcl-role:source-audit", "gcl-pickup:direct-editorial"]) == ("Mathematics", "direct_editorial")

def test_critic_direct_but_mathematics():
    assert classify("grandchallenge/MATH-PROGRAMME", "ERDOS 41 — critical source and lemma review of ERDOS-041-source", ["gcl-job", "gcl-role:source-audit", "gcl-pickup:direct-editorial"])[0] == "Mathematics"

def test_typography_stays_editorial():
    assert classify("grandchallenge/MATH-PROGRAMME", "MP-MATH-TYPO-ED07 — source audit", ["gcl-job", "gcl-role:source-audit", "gcl-pickup:direct-editorial"])[0] == "Editorial"

def test_atlas_editorial():
    assert classify("grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS", "Chapter review", ["gcl-job", "gcl-pickup:direct-editorial"])[0] == "Editorial"

@pytest.mark.parametrize("repo,title,labels", [
    ("grandchallenge/MATHSOLVE", "proof", ["gcl-job", "gcl-pickup:direct-editorial"]),
    ("grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS", "Chapter", ["gcl-job"]),
    ("grandchallenge/MATH-PROGRAMME", "ERDOS-CATALOGUE-0041-S01", ["gcl-job", "gcl-pickup:direct-editorial"]),
    ("grandchallenge/OTHER", "other", ["gcl-job"]),
    ("grandchallenge/MATH-PROGRAMME", "ERDOS 41 — critical source and lemma review of ERDOS-042-X", ["gcl-job", "gcl-role:source-audit", "gcl-pickup:direct-editorial"]),
])
def test_hostile_fail_closed(repo,title,labels):
    with pytest.raises(Boundary):
        classify(repo,title,labels)

def test_plan_discrepancy_without_mutation():
    snapshot = {"items":[{"id":"PVTI_1", "content":{"number":41,"title":"ERDOS-CATALOGUE-0041-S01","repository":{"nameWithOwner":"grandchallenge/MATH-PROGRAMME"},"labels":{"nodes":[{"name":x} for x in ["gcl-job","gcl-role:source-audit","gcl-pickup:direct-editorial"]],"pageInfo":{"hasNextPage":False}}},"fieldValueByName":{"name":"Editorial"}}]}
    targets, changes = _targets(snapshot)
    assert targets["PVTI_1"]["class"] == "Mathematics"
    assert changes[0]["before"] == "Editorial"
    assert changes[0]["after"] == "Mathematics"


def test_solve_source_audit_role_is_mathematical_not_pickup():
    # Live GCL issue #843: Erdős source-audit work inside reservation Solve.
    assert classify("grandchallenge/MATHSOLVE", "[GCL-CONTRIB] ERDOS-OPEN ERDOS-593-S1-IA-001 — SOURCE-AUDIT", ["gcl-job", "gcl-role:source-audit"]) == ("Mathematics", "reservation_controlled")


def test_solve_source_audit_still_rejects_direct_pickup():
    with pytest.raises(Boundary, match="INVALID_MATHSOLVE_PICKUP_LABEL"):
        classify("grandchallenge/MATHSOLVE", "[GCL-CONTRIB] ERDOS-OPEN ERDOS-593-S1-IA-001 — SOURCE-AUDIT", ["gcl-job", "gcl-role:source-audit", "gcl-pickup:direct-editorial"])


def test_solve_source_audit_issue_inventory():
    snapshot = {"items":[{"id":"PVTI_843", "content":{"number":843,"title":"[GCL-CONTRIB] ERDOS-OPEN ERDOS-593-S1-IA-001 — SOURCE-AUDIT","repository":{"nameWithOwner":"grandchallenge/MATHSOLVE"},"labels":{"nodes":[{"name":x} for x in ["gcl-job","gcl-role:source-audit"]],"pageInfo":{"hasNextPage":False}}},"fieldValueByName":{"name":"Mathematics"}}]}
    targets, changes = _targets(snapshot)
    assert targets["PVTI_843"]["pickup_mode"] == "reservation_controlled"
    assert changes == []


def test_reconcile_error_names_offending_issue():
    snapshot = {"items":[{"id":"PVTI_843", "content":{"number":843,"title":"[GCL-CONTRIB] ERDOS-OPEN ERDOS-593-S1-IA-001 — SOURCE-AUDIT","repository":{"nameWithOwner":"grandchallenge/MATHSOLVE"},"labels":{"nodes":[{"name":x} for x in ["gcl-job","gcl-pickup:direct-editorial"]],"pageInfo":{"hasNextPage":False}}},"fieldValueByName":{"name":"Mathematics"}}]}
    with pytest.raises(Boundary, match=r"grandchallenge/MATHSOLVE#843"):
        _targets(snapshot)
