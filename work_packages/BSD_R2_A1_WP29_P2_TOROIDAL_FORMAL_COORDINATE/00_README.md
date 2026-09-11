# BSD-R2-A1 WP29 — toroidal formal norm coordinate at `2`

## Status

Candidate work package for the protected BSD-001 selected research target.

Exact protected MATHSOLVE baseline:

`3bae7e80d148adb297fc3746e4f1eb0466148354`.

Exact protected MATHFORGE source authority:

`2021db4f98da3d0df7cea2a37c9d9f6d4e9a4576`.

Programme owner:

`grandchallenge/MATHSOLVE#164`.

## Purpose

Protected WP28 reduced the remaining local D1b uncertainty to the order of one explicit formal universal-norm class

`z_form(P) in F_2^norm`,

where

`#F_2^norm = 3-a_2 in {2,4}`.

WP29 composes this protected object with the newly protected Hall/Lubin-Rosen toroidal construction. The goal is not to invent a logarithmic formula. The goal is to replace the abstract formal-group element order by an exact finite congruence-depth invariant in the source-defined Galois quotient.

## Protected inputs

WP29 uses only:

- protected WP28 for
  `0 -> F_2^norm -> U_2 -> E_tilde(F_2) -> 0`,
  the element `z_form(P)`, and
  `rho_2(P)=r_red(P)+s_form(P)`;
- protected WP26 for the odd-prime quantity `rho_bad(P)` and
  `rho_E=max(rho_2(P),rho_bad(P))`;
- protected WP24 for the exact control-defect length formula;
- protected MATHFORGE WP29 source admission for a map-level isomorphism from the height-one formal universal-norm quotient to
  `Gamma_2/(1-u)Gamma_2`, preserving element order.

No new external theorem premise is introduced in MATHSOLVE WP29.

## Main result

Let

`theta_form(P) in Gamma_2/(1-u)Gamma_2`

be the Hall/Lubin-Rosen image of `z_form(P)` under any source-compatible toroidal coordinate.

WP29 proves

`ord(theta_form(P))=ord(z_form(P))`.

Since `Gamma_2` is a free rank-one `Z_2`-module, choose any topological generator and identify

`Gamma_2 ~= Z_2`.

Put

`m_2 := ord_2(3-a_2)`.

The protected group-order identities imply internally

`ord_2(1-u)=m_2`.

Write the class `theta_form(P)` as a scalar class

`t_form(P) mod (1-u)`

under the chosen generator and define

`tau_form(P)
 := min(m_2, ord_2(t_form(P)))`,

with `tau_form(P)=m_2` for the zero class.

This value is independent of:

- the lift of the scalar class;
- the topological generator of `Gamma_2`;
- the source-compatible toroidal coordinate, because the induced finite cyclic-group automorphism preserves element order and hence the truncated valuation.

WP29 proves exactly

`s_form(P)=m_2-tau_form(P)`,

so

`rho_2(P)=r_red(P)+m_2-tau_form(P)`

and

`rho_E
 = max(r_red(P)+m_2-tau_form(P), rho_bad(P))`.

## Finite classification

Because the selected branch has `a_2 in {+1,-1}`:

- if `a_2=+1`, then `m_2=1` and `tau_form(P) in {0,1}`;
- if `a_2=-1`, then `m_2=2` and `tau_form(P) in {0,1,2}`.

Thus the remaining local D1b datum is a finite congruence-depth invariant.

## Refined boundary

WP29 replaces

`MISSING_P2_FORMAL_UNIVERSAL_NORM_ORDER_OF_REDUCTION_KILLED_GENERATOR`

with

`MISSING_P2_TOROIDAL_FORMAL_COORDINATE_CONGRUENCE_DEPTH`.

A successor must evaluate `tau_form(P)` uniformly in the selected branch, or prove an exact comparison to another already controlled arithmetic invariant.

## Claim firewall

WP29 does not prove:

- a value of `tau_form(P)` for the selected family;
- a canonical scalar representative `t_form(P)`;
- `u=alpha` or `u=alpha^(-1)`;
- a formal-logarithm formula for `t_form(P)`;
- a p-adic-height, regulator, or WP20 Bockstein identity;
- D1a `MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`;
- D1c `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2 `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`;
- `BSD-R2-A1`;
- any MATHCERT certification, novelty, priority, patentability, or commercial claim.
