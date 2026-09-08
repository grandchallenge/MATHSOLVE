# Failure analysis and one-prime firewall

## FR-01 — substitute `p=2` into an odd-prime theorem

**Disposition:** terminated. The protected theorem interface explicitly excludes `2`; its proof also treats powers of `2` as odd-prime units in places where `ord_2` cannot.

## FR-02 — infer the target from rank one plus finite Sha

**Disposition:** terminated. Gross-Zagier/Kolyvagin determines rank and finiteness, not the exact leading coefficient.

## FR-03 — use parity or modulo-squares information

**Disposition:** terminated. Parity and square-class information cannot determine an arbitrary exact `ord_2`.

## FR-04 — import CM or quadratic-twist-family theorems

**Disposition:** quarantined to their stated families. The selected quantifier is over every curve in a broader semistable ordinary-at-2 class.

## FR-05 — use finite curve verification or WP03 fixtures

**Disposition:** terminated as a theorem route. Such evidence can falsify or test interfaces but cannot prove the universal restricted statement.

## FR-06 — identify Selmer corank with rank without Sha control

**Disposition:** terminated in general. The Kummer exact sequence retains the `Sha[2^infinity]` term. In the selected analytic-rank-one branch, finiteness is imported, but exact 2-primary order still remains to be computed.

## FR-07 — use quadratic plus/minus splitting integrally at `2`

**Disposition:** blocked pending exact control. Division by `2` in idempotent-style decompositions is not integral over `Z_2`; restriction/corestriction kernel and cokernel lengths must be retained or the route replaced.

## FR-08 — discard period/isogeny/interpolation factors as units

**Disposition:** terminated. A power of `2` is invisible to odd-prime valuation but is target data here.

## FR-09 — assume a p-adic height is nondegenerate or identify it with the complex regulator

**Disposition:** terminated unless an exact source-backed comparison proves the required statement under the selected hypotheses.

## Reopening rule

A terminated transfer route may reopen only with an exact theorem that discharges the named 2-primary defect. A new theorem may narrow the proof path; it may not silently narrow the selected target.