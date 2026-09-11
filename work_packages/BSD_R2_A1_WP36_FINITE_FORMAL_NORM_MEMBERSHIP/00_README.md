# BSD-R2-A1 WP36 — finite p=2 formal norm membership

## Status

Candidate mathematical work package. No WP36 conclusion is protected until exact-head Adversary and Referee review, affected CI, protected merge, and protected-main readback complete.

## Exact protected inputs

- MATHSOLVE protected base: `757da986335a11a847bf31b396396729e1e7e983`.
- MATHFORGE protected source authority: `92fcd8596e59aa8331b2450ea66c14786581806e`.
- Protected WP28 concrete formal universal-norm filtration.
- Protected WP29 toroidal depth convention.
- Protected WP30 identity `u=alpha`.
- Protected WP31 stabilization at `n=m_2 in {1,2}` and finite twisted-reciprocity exponent `c_tw(P) mod 2^{m_2}`.

## Purpose

WP31 reduced the only remaining place-2 local structural datum to a single finite class:

`c_tw(P) mod 2` if `a_2=+1`,

or

`c_tw(P) mod 4` if `a_2=-1`.

WP36 replaces that abstract finite class by a terminating exact norm-membership computation in the degree-2 or degree-4 local cyclotomic layer.

The only new source input is Silverman IV.6.4, admitted by protected MATHFORGE WP36. It is used only on the deep subgroup `Ehat(4 O_L)`, where the strict `p=2` convergence threshold is satisfied.

## Candidate result

Let `L_n/Q_2` be the degree-`2^n` local cyclotomic layer for `n=1,2`, and write

`H_n := N_{L_n/Q_2} Ehat(m_{L_n}) subset Ehat(2 Z_2)`.

WP36 proves internally that

- `Tr_{L_1/Q_2}(O_{L_1})=2 Z_2`, hence
  `N Ehat(4O_{L_1})=Ehat(8 Z_2)`;
- `Tr_{L_2/Q_2}(O_{L_2})=4 Z_2`, hence
  `N Ehat(4O_{L_2})=Ehat(16 Z_2)`.

Therefore `H_n` is determined by a finite map

`Ehat(m_{L_n})/Ehat(4O_{L_n}) -> Ehat(2Z_2)/D_n`,

where

`D_1=Ehat(8Z_2)` and `D_2=Ehat(16Z_2)`.

The source quotient has exactly

- `8` classes for `n=1`;
- `128` classes for `n=2`.

Enumerating these classes, taking the formal-group norm, and reducing modulo `D_n` computes `H_n/D_n` exactly.

For the protected saturated generator `P`, put

`Q_P := [2^{r_red(P)}]P in Ehat(2Z_2)`.

Its class in the stabilized finite formal norm quotient is protected `z_form(P)`. Hence:

### `m_2=1`

- `Q_P in H_1` iff `c_tw(P)=0 mod 2` iff `tau_form(P)=1`;
- otherwise `c_tw(P)=1 mod 2` iff `tau_form(P)=0`.

### `m_2=2`

- `Q_P in H_2` iff `c_tw(P)=0 mod 4` iff `tau_form(P)=2`;
- `Q_P notin H_2` but `[2]Q_P in H_2` iff `c_tw(P)=2 mod 4` iff `tau_form(P)=1`;
- `[2]Q_P notin H_2` iff `c_tw(P)` is odd iff `tau_form(P)=0`.

Thus the WP31 exponent is exactly computable by a bounded finite local calculation.

## Claim boundary

WP36 closes `MISSING_P2_FINITE_TWISTED_RECIPROCITY_EXPONENT` only in the exact computable-criterion sense. It does not assert a curve-independent constant value for that exponent.

It does not close:

- D1c `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2 `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`;
- `BSD-R2-A1`;
- any MATHCERT certification claim.
