# External catalog reviewed promotion

## Authority and present state

MATHFORGE owns intake, normalization, semantic review, relation review and catalog
assurance. Programme admits exact foundry artifacts. MATHSOLVE begins a full
Chaidez dossier only when a qualified reviewer explicitly approves a bounded
promotion. The production registry is
`governance/external_catalog_promotion_registry.json`: initially zero promotions.
The full filesystem canary under `tests/fixtures/external_catalog_promotion` is
synthetic and never production evidence.

Assurance describes the source record. Review records who assessed meaning.
Promotion records a bounded Solve decision. Mathematical status records the
local claim's support and debt. Certification records a separate MATHCERT act.
None of these states may be inferred from another, from formal-language metadata,
or from green CI. Existing campaign-manifest `promotion` fields are unchanged.

## Operational gate

`schemas/external_catalog_promotion_dossier.schema.json` v2 requires all eight
result-status fields, nine ordered exposition stages, four trust answers, one
global spine, a named local node, complete dependency/debt accounting, foundation
or explicit gap, first executable step and nonclaims. Each of twelve artifact
roles binds a regular tracked file by both Git-blob and SHA-256 identity. A shared
file requires distinct explicit anchors such as `<a id="lay"></a>`.

New dossier sidecars use JSON: CLAIM_LEDGER contains `local_claims`, THEOREM_SPINE
contains `theorem_spine`, PROOF_DEBT_REGISTER contains `proof_debt`, DEPENDENCY_DAG
maps each node to its dependencies, and CERT_HANDOFF records the initial
NOT_CERTIFIED state, local claims and quartet. These are local work-package
records, not the canonical MATHCERT Claim Ledger. Other artifact roles teach and
explain the mathematics; their fidelity remains a qualified review obligation.

The quartet's claim/debt IDs must exactly reflect the structured status: PROVED
claims in WHAT_IS_PROVED; CHECKED, PROVED or REFUTED claims in WHAT_IS_CHECKED;
OPEN or CONDITIONAL claims and all open debts in WHAT_REMAINS_OPEN; explicitly
external-verification claims and open EXTERNAL_SOURCE debts in the fourth answer.
Discharged debts appear in WHAT_IS_CHECKED; superseded debts remain in the full
register. An open prerequisite debt prevents a checked/proved dependent node.
Proved here is a local assertion supported by review, never a certificate.

The gate checks exact catalog IDs, snapshot and raw/normalized digests against
the Programme-admitted MATHFORGE shard. For an exact campaign target the reviewed
relation must actually connect that entry and campaign with `same_statement` or
`formalizes`; implication, resemblance or duplicate candidacy is not identity.
Review names and qualifications are attributed evidence, not machine-verified
credentials. Protected governance must still obtain genuine qualified review.

Run local empty-registry checks and the complete synthetic canary:

```sh
python ci/validate_external_catalog_promotion_dossiers.py
python -m unittest ci.test_external_catalog_promotion_dossiers -v
```

Nonempty production registries require explicit authenticated integration roots:

```sh
python ci/validate_external_catalog_promotion_dossiers.py \
  --programme-root /path/to/MATH-PROGRAMME --forge-root /path/to/MATHFORGE
```

Fetch protected `origin/main` first. The validator reads Git objects, checks
protected ancestry, requires the admitted foundry commit, and rejects an outdated
Programme import artifact. It does not fetch credentials or run a scheduled
cross-repository workflow. A future real promotion needs this access configured
in its admission environment; missing roots fail closed rather than bypassing
source validation. No ordinary catalog entry is given a dossier.

## Separate MATHCERT handoff

The new `external_catalog_mathcert_handoff` schema supplements the unchanged
generic handoff. Its template is explicitly a synthetic example; replace all
identities and obtain real review before any production use. The supplement
binds the registered dossier, exact local claim, spine node, every applicable
debt, quartet, support route, replay evidence and independent-verification
disposition. Pending verification is not a certificate. Open debt remains visible
and cannot accompany an inflated ready/complete status.

The eleven existing generic handoff packets and schema remain byte-identical to
the approved baseline. WP06 receives documentary v2 conformance without changing
its Claim Ledger or restricted theorem. RM-DIO-004 remains a bounded historical
route: LEGACY_PRE_CATALOG_ROUTE and NOT_A_CATALOG_PROMOTION. Its evidence is
preserved, but a future catalog promotion must pass the new review and dossier gate.
