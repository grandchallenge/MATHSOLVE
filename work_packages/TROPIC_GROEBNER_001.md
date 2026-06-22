# Work Package: TROPIC-GROEBNER-001

## Identity

```yaml
work_package_id: MS-TG-001
programme_fixture: TROPIC-GROEBNER-001
route: TROPIC_GROEBNER_CAMPAIGN
status: route_seed
mathprogramme_reference: docs/TROPIC_GROEBNER_ROUTE.md
expected_mathcert_certificate_kind: tropical_initial_ideal
```

## Local obligation

For the ideal

```text
I = <x + y + 1> in QQ[x, y]
```

and trivial coefficient valuation, compute the weighted initial form for four sampled rational weights and classify each weight as retained or rejected under the monomial-free tropical membership predicate.

## Encoding audit

```yaml
coefficient_domain: QQ
valuation: trivial
variables: [x, y]
generators:
  - x + y + 1
laurent_domain: false
side_conditions: []
semantic_scope: sampled-weight initial-form classification only
```

The fixture is intentionally not a full tropical fan traversal. The semantic object is a bounded route decision ledger for four sampled weights.

## Candidate weights

| Weight | Source | Purpose |
| --- | --- | --- |
| `(0, 0)` | balanced probe | retained baseline |
| `(1, 0)` | normal-fan ray sample | retained two-term initial form |
| `(-1, 0)` | adversarial monomial probe | rejected monomial witness |
| `(1, 2)` | constant-term dominance probe | rejected unit witness |

## Expected route ledger

| Weight | Initial form | Contains monomial | Decision | Witness |
| --- | --- | --- | --- | --- |
| `(0, 0)` | `x + y + 1` | no | `weight_retained` | none |
| `(1, 0)` | `y + 1` | no | `weight_retained` | none |
| `(-1, 0)` | `x` | yes | `weight_rejected` | `x` |
| `(1, 2)` | `1` | yes | `weight_rejected` | `1` |

## Required artifacts

```text
reports/tropic_groebner/TROPIC_GROEBNER_001_route_report.md
reports/tropic_groebner/TROPIC_GROEBNER_001_weight_ledger.json
handoff/TROPIC_GROEBNER_001_mathcert_request.md
```

## MATHCERT handoff

MATHSOLVE should send MATHCERT a certificate request containing:

- source generator in sparse polynomial form;
- weight vector;
- valuation convention;
- initial form;
- contains-monomial flag;
- monomial witness when rejected;
- trusted boundary `external_certificate_recorded` until replay exists.

## Forbidden inference

This work package does not claim:

- the full tropical variety has been enumerated;
- unsampled weights have been classified;
- tropical membership solves the source algebraic system;
- the route scales beyond this bounded fixture.

## Exit criteria

The work package exits `route_seed` when the route report and certificate request are generated. It exits `ready_for_mathcert` only when the JSON payload is stable enough for the MATHCERT algebraic certificate validator or replay script.
