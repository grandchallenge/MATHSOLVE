# BSD-R2-A1 WP60B — Kriz–Li literal-`2` transport

## Purpose

Execute the WP60B normalization/independence test from `grandchallenge/MATHSOLVE#215` using the exact source interface protected by MATHFORGE.

## Entering protected anchors

- MATHSOLVE: `8b7ba4e5d888f68ffdaeab748d7d94d764f286fa`.
- MATHFORGE: `a8f72ed64755777870a300053e11659fb1dfff1b`.
- Tracker: `grandchallenge/MATHSOLVE#215`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.

## Result

WP60B first proves the exact normalization

`KL_2(E,K,f)=u_f m_K(f) kappa_2(E,P)`,

with

`u_f in Z_2^x`

and

`kappa_2(E,P)=((3-a_2)/2)log_{omega_E}(P)`.

It then uses the selected good-ordinary-at-`2` hypothesis to prove a stronger local theorem:

`kappa_2(E,P) in 2Z_2`

for every selected curve and primitive generator.

Hence

`KL_2(E,K,f) in 2Z_2`

for every WP09-compatible field `K`. Kriz–Li Assumption `(F)` therefore cannot hold anywhere on the selected good-ordinary branch.

Disposition:

`KRIZ_LI_F_LOCALLY_OBSTRUCTED_ON_SELECTED_GOOD_ORDINARY_LANE`.

## Consequence for WP59

Reopening form `R3` is retired for the selected branch:

`R3_RETIRED_FOR_SELECTED_GOOD_ORDINARY_LANE_BY_WP60B_LOCAL_OBSTRUCTION`.

This does not resolve `R1`, `R2`, `R4`, `R5`, or D2d. The genuine Heegner-index problem remains

`MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`.

## Why the extra factor appears

For a minimal good model at `2`, ordinary reduction forces the Weierstrass `A_1` coefficient to be odd. The formal invariant differential then gives

`log_{omega_E}(E_1(Q_2)) subset 4Z_2`.

Since `[3-a_2]P` reduces to the identity,

`kappa_2(E,P)
 = (1/2)log_{omega_E}([3-a_2]P)
 in 2Z_2`.

No shallow formal-log isomorphism is assumed.

## Files

- `01_KRIZ_LI_TRANSPORT_THEOREM.md` — exact transport and ordinary local obstruction.
- `02_CLAIM_LEDGER.yaml` — claim and boundary ledger.
- `handoffs/BSD-001/WP60B_FRONTIER.md` — successor frontier.

## Non-promotion

This work package does not determine `m_K(f)` or `lambda_D`, does not resolve D2d, does not prove `BSD-R2-A1`, and does not invoke MATHCERT. The local obstruction is specific to the protected good-ordinary-at-`2` selected lane; it is not a general impossibility claim about Kriz–Li `(F)`.
