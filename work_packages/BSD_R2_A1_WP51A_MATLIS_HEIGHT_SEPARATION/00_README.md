# BSD-R2-A1 WP51A — Matlis correction / first-height separation

## Operation

`BSD-R2-A1-WP51A-MATLIS-HEIGHT-SEPARATION`

## Protected inputs

- MATHSOLVE WP50A: `e078beae05252c4152787fc812e0823b14c23fac`.
- MATHFORGE WP51 duality admission: `79302cdc05f3f11c56e048f68e9095d3280872a7`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.

## Objective

WP50A proves

`D_K^vee ~= K_K^sil`

for the finite strict degree-two silent kernel

`K_K^sil subset H~^2_f(K,T;Delta_str)`.

WP51A determines what this finite module means under the exact literal-`p=2` Selmer dualities already protected, and whether it can be identified with the first p-adic height radical.

## Result

Let

`S_str^dual := H~^1_f(K,A^*(1);Delta_str^perp)`.

Protected MATHFORGE WP51 gives a perfect Pontryagin pairing

`H~^2_f(K,T;Delta_str) x S_str^dual -> Q_2/Z_2`.

If

`N_K := (K_K^sil)^perp subset S_str^dual`,

then

`0 -> N_K -> S_str^dual -> D_K -> 0`

canonically.

By contrast, the degree-(2,1) `Z_2`-valued duality used in the first Nekovar height kills every finite subgroup of strict `H^2`, hence kills `K_K^sil`. Therefore the first height factors through strict `H^2` modulo torsion and cannot see the finite WP40 correction.

The finite Matlis correction and fixed-`2` first-height nondegeneracy are distinct obligations.

## Refined D2b boundary

The former question

`MISSING_P2_STRICT_H2_SILENT_KERNEL_TO_BOCKSTEIN_HEIGHT_DUALITY`

is closed as a separation theorem, not by identifying `D_K` with a height radical.

The surviving finite-comparison debt is

`MISSING_P2_FINITE_MATLIS_CORRECTION_EVALUATION_OR_CANCELLATION_IN_DETERMINANT_NORMALIZATION`.

WP51A does not evaluate `d_K=len_Z2 D_K` and does not prove its cancellation from the final determinant ledger.

## Firewall

No claim of `D_K=0`, `K_K^sil=0`, height nondegeneracy, D1c, global `Q^ord=1`, WP00 normalization, final descent, BSD, certification, novelty, or priority.
