# BSD-R2-A1 WP35 — literal-p=2 primitive cyclotomic square presentation

## Status

Candidate mathematical work package. No WP35 conclusion is protected until exact-head Adversary and Referee review, affected CI, protected merge, and protected-main readback complete.

## Exact protected inputs

- MATHSOLVE protected base: `9708080c76eb118232d2afb497e2c4803498224d`.
- MATHFORGE protected source authority: `4cf5f8838541fb15296619ead3aaaf298198fe65`.
- WP16B: the primitive classical Kummer dual Selmer module `X_E` is finitely generated rank one over `Z_2`, with canonical finite torsion `T_E`.
- WP19: `Fitt^1_{Z_2}(X_E)=Fitt^0_{Z_2}(T_E)`.
- WP20: exact rank-one determinant/Bockstein factorization for a square `Z_2[[T]]` presentation whose augmentation cokernel has rank one.
- WP21: exact primitive control sequence

  `0 -> C_E^vee -> (X_infty)_Gamma -> X_E -> 0`.

- WP24 and successors: `C_E^vee` is finite and its exact length is governed by the protected local-control calculation.

## New source-qualified structural input

Protected MATHFORGE WP35 admits Greenberg's literal-`p=2` classical cyclotomic Kummer Selmer interfaces:

1. `Sel_{2^infinity}^{Kum}(E/Q_infty)` is `Lambda`-cotorsion on the selected modular good-ordinary branch;
2. under protected `E(Q)[2^infinity]=0`, it has no proper finite-index `Lambda`-submodule;
3. equivalently its compact dual

   `X_infty := Sel_{2^infinity}^{Kum}(E/Q_infty)^vee`

   is finitely generated torsion over `Lambda=Z_2[[Gamma]]` and has no nonzero finite `Lambda`-submodule.

## Purpose

WP21 left D1a because it had not proved that `X_infty` was a projective-dimension-one `Lambda`-module admitting the square presentation required by WP20.

WP35 proves that structural result by regular-local commutative algebra, specializes the square presentation at augmentation, and computes the complete finite specialization discrepancy. The discrepancy is exactly the already protected module `C_E^vee`; no additional unnamed finite term occurs.

## Candidate result

After choosing a topological generator of `Gamma`, identify

`Lambda ~= Z_2[[T]]`.

Then `X_infty` admits a finite square free resolution

`0 -> Lambda^r --A(T)--> Lambda^r -> X_infty -> 0`.

At `T=0`, write

`M_0 := coker(A(0)) ~= (X_infty)_Gamma`.

The protected WP21 sequence becomes

`0 -> C_E^vee -> M_0 -> X_E -> 0`.

Moreover

`0 -> C_E^vee -> Tor_{Z_2}(M_0) -> T_E -> 0`,

so

`Fitt^1_{Z_2}(M_0)
 = Fitt^0_{Z_2}(C_E^vee) * Fitt^1_{Z_2}(X_E)`.

Since `M_0` has rank one, `A(0)` has corank one over `Q_2`, and WP20 applies:

`(coeff_T det A(T)) Z_2
 = Fitt^0_{Z_2}(C_E^vee)
   * Fitt^1_{Z_2}(X_E)
   * B_A`,

where `B_A` is WP20's intrinsic rank-one Bockstein ideal.

This closes D1a

`MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`

in its exact square-presentation plus specialization-defect-accounting form.

## Retained boundaries

WP35 does not identify `det A(T)` with an analytic `2`-adic L-function or Euler-system generator. It does not identify `B_A` with the protected WP00 regulator normalization. Therefore the following remain open:

- D1c `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2 `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`;
- WP31 `MISSING_P2_FINITE_TWISTED_RECIPROCITY_EXPONENT`.

`BSD-R2-A1` remains `SELECTED_RESEARCH_TARGET_UNPROVED`. MATHCERT remains the sole certification authority.