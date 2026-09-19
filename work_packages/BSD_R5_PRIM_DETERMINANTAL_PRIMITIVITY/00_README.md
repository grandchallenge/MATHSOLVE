# BSD R5-PRIM — height-one `(2)` determinant primitivity

## Status

Substantive theorem/reduction package for `grandchallenge/MATHSOLVE#267`.

The entering R5-LIFT operation is protected complete at

`grandchallenge/MATHSOLVE@50308cf34782f14fdb0421beea915311cef20bf3`.

The current protected source authority is

`grandchallenge/MATHFORGE@5aef30aa64730ca777329013e1e33c03f34a6e3a`,

including the Castella–Sano determinant-descent source audit admitted through MATHFORGE #223 / PR #224.

## Entering frontier

`MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2` (`R5-PRIM`).

Protected WP60A-A1 gives, over the DVR `Lambda_(2)`,

- determinant membership iff `v(a) >= length(H^2)`;
- determinant-generator status iff `v(a) = length(H^2)`.

R5-LIFT has established the first statement for the selected Kato element.

## New reduction

Put

`Lambda = Z_2[[T]]`, `T=gamma-1`, `q=(2)`, `A=Lambda_q`.

The residue field of `A` is

`k(q)=Frac(F_2[[T]])=F_2((T))`.

The protected compatible determinant-to-Stark and Stark-to-Kolyvagin isomorphisms identify the cyclotomic determinant line with a rank-one inverse-limit selected Kolyvagin-system line. Under this identification the protected determinant preimage maps to the compatible Kato-derived Kolyvagin system.

The package proves:

`R5-PRIM`

is equivalent to the residual inverse-limit Kato-derived Kolyvagin system being nonzero in the rank-one `F_2[[T]]` module obtained modulo `2`.

Equivalently, there exists a finite cyclotomic layer `n` at which the mod-`2` Kato-derived Kolyvagin system is nonzero.

This is deliberately weaker than asking that the finite-layer system be a basis over `F_2[Gamma_n]`: a factor `T^r` is a nonunit at finite level but becomes a unit after localization at `(2)`.

## Candidate disposition

The reduction theorem is proved in this package, but the protected campaign does not currently supply the required residual Kato-system nonvanishing uniformly on the selected good-ordinary `S_3` lane.

Candidate operation disposition:

`BLOCKED`.

Exact residual frontier:

`MISSING_P2_RESIDUAL_CYCLOTOMIC_KATO_KOLYVAGIN_NONVANISHING`.

This is the determinant-side height-one `(2)` excess-divisibility / `mu` question. It must not be conflated with bare nonvanishing of the base-field first Kato class or with finite-layer basis status.

## Claim firewall

This package does not establish:

- `R5_PRIM_ESTABLISHED`;
- a general Greenberg `mu_2=0` theorem;
- a literal-`p=2` Castella–Sano/Kurihara theorem;
- D2d;
- `BSD-R2-A1`;
- novelty or priority;
- MATHCERT certification.
