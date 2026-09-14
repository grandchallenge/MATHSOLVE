# BSD-R2-A1 WP60B — Kriz–Li literal-`2` normalization transport

## Purpose

Execute the WP60B independence test from protected `grandchallenge/MATHSOLVE#215`.

The question is not whether Kriz–Li provide a genuine literal-`2` theorem; protected MATHFORGE already confirms that they do. The question is whether their Assumption `(F)` supplies arithmetic information independent of the protected unknown Heegner-index parity.

## Entering protected anchors

- MATHSOLVE: `8b7ba4e5d888f68ffdaeab748d7d94d764f286fa`.
- MATHFORGE: `a8f72ed64755777870a300053e11659fb1dfff1b`.
- Active execution tracker: `grandchallenge/MATHSOLVE#215`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.

## Result

WP60B proves the exact factorization

`KL_2(E,K,f)=u_f m_K(f) kappa_2(E,P)`,

where

- `u_f in Z_2^x` is the protected modular-differential unit;
- `m_K(f)` is the protected Heegner index;
- `kappa_2(E,P)=((3-a_2)/2)log_{omega_E}(P) in Z_2` is a fixed selected-curve local scalar independent of `K`.

Therefore

`Assumption (F)
 <=> [m_K(f) odd] AND [kappa_2(E,P) in Z_2^x]`.

Disposition:

`MIXED_BUT_NO_INDEPENDENT_K_VARYING_ESCAPE`.

Thus WP59 reopening form `R3` is not an independent way around `R1`: its varying-field content is exactly the same unknown Heegner-index parity, together with a fixed local prerequisite.

## New split

- `KL-LOCAL`: `MISSING_UNIFORM_KRIZ_LI_FIXED_LOCAL_LOG_UNIT`.
- `KL-INDEX`: `MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`.

The fixed local factor is suitable for WP60C exact real-data reconnaissance. The index parity remains a genuine theorem boundary.

## Files

- `01_KRIZ_LI_TRANSPORT_THEOREM.md` — exact normalization, integrality, factorization, and independence classification.
- `02_CLAIM_LEDGER.yaml` — protected claim boundary.
- `handoffs/BSD-001/WP60B_FRONTIER.md` — continuation frontier.

## Non-promotion

This work package does not prove either new obligation, does not reopen D2d, does not prove `BSD-R2-A1`, and does not invoke MATHCERT.
