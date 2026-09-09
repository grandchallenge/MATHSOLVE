# BSD-R2-A1-WP16B — exact integral Selmer/Fitting realization

## Metadata

- Campaign: `BSD-001`.
- Work package: `BSD-R2-A1-WP16B-INTEGRAL-SELMER-FITTING`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Protected Solve baseline: `3fc4567bfe2a5dfe881378f97a14576494b3a746`.
- Protected Forge provider baseline: `118ae1b5c2fc2630f53000921b742c610c50db16`.
- Parent frontier: `BSD-R2-A1-S3-INTEGRAL-SELMER-REPRESENTATION`.
- Parent boundary: `MISSING_EXACT_INTEGRAL_SELMER_INVARIANT_REALIZATION`.
- Selected claim: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.
- Certification: none; MATHCERT remains the only certification authority.

## Purpose

Realize the exact integer produced by protected WP16A as a canonical integral `Z_2`-module invariant without importing a modern Selmer-complex theorem or hiding any power of `2` behind a unit ambiguity.

WP16B chooses the primitive classical `2^infinity` Selmer tower with levelwise Kummer local conditions. Let

`Sel_{2^infinity}^{Kum}(E/Q) := colim_n Sel_{2^n}(E/Q)`

under the natural coefficient inclusions. Define its Pontryagin dual

`X_E := Hom(Sel_{2^infinity}^{Kum}(E/Q), Q_2/Z_2)`.

The package proves that `X_E` is a finitely generated rank-one `Z_2`-module and that its canonical torsion submodule satisfies

`Tor_{Z_2}(X_E) ~= Sha(E/Q)[2^infinity]^vee`.

Hence

`len_{Z_2} Tor_{Z_2}(X_E)`

is exactly the WP16A stable integer, and the zeroth Fitting ideal is exactly

`Fitt_{Z_2}^0(Tor_{Z_2}(X_E)) = 2^{lambda_E} Z_2`,

where

`lambda_E := lim_n (ord_2 #Sel_{2^n}(E/Q) - n)`.

This equality is equality of ideals. No generator is specified only up to a unit.

## Exact local-condition choice

At every level `2^n` and every place `v` of `Q`, the local condition is the image of the local Kummer map

`E(Q_v)/2^n E(Q_v) -> H^1(Q_v,E[2^n])`.

This includes:

- the real place;
- the good-ordinary place `v=2`;
- every bad semistable prime `ell | N`;
- every other finite place.

At `2`, WP16B deliberately uses the finite classical Kummer condition. Protected WP06 forbids identifying this condition with the Greenberg/ordinary condition from the connected-etale `2`-divisible group without an exact comparison theorem.

At bad primes, WP16B uses the full primitive Kummer condition. It does not replace that condition by an unramified, strict, relaxed, or imprimitive condition.

## Rank-one free direction

The direct-limit Kummer sequence and protected rank-one/odd-torsion inputs give an exact sequence

`0 -> Q_2/Z_2 -> Sel_{2^infinity}^{Kum}(E/Q) -> Sha(E/Q)[2^infinity] -> 0`.

After duality,

`0 -> Sha(E/Q)[2^infinity]^vee -> X_E -> Z_2 -> 0`.

The quotient `X_E/Tor(X_E)` is therefore the saturated rank-one free direction. No generator, Heegner point, regulator basis, or nonsaturated sublattice is selected in WP16B.

## Tamagawa and primitive/imprimitive normalization

The algebraic invariant is primitive: no bad-prime Euler factor or Tamagawa factor is removed from the Selmer local conditions.

The selected analytic defect remains

`delta_2(E) := ord_2(L'(E,1)/(Omega_E Reg_E)) - sum_{ell|N} ord_2(c_ell)`.

Protected WP13 controls the exact values `ord_2(c_ell)` and the residual-conductor drop. WP16B does not manufacture a local comparison theorem asserting that a different imprimitive Selmer condition has defect equal to this Tamagawa sum. Any WP17 source using different bad-prime local conditions must prove the exact comparison before composition.

Thus the selected target is now equivalent to the sharply specified integral equality

`delta_2(E) = v_2(Fitt_{Z_2}^0(Tor_{Z_2}(X_E)))`,

where `v_2(2^m Z_2)=m`.

## What is proved

- exact direct-limit Kummer sequence at `2^infinity`;
- exact rank-one free quotient of `X_E`;
- canonical identification of the torsion submodule with the dual finite `2`-primary Tate-Shafarevich group;
- exact equality of the torsion length with the WP16A stable integer;
- exact zeroth Fitting ideal of that torsion module;
- exact integral reformulation of the selected target in Fitting-valuation form.

## What is not proved

WP16B does not prove:

- `BSD-R2-A1`;
- equality between Kummer and Greenberg/ordinary local conditions at `2`;
- a Selmer-complex determinant theorem over the protected WP09 field `K`;
- an Euler-system or Kolyvagin-system divisibility;
- a Tamagawa-defect comparison for an imprimitive external theorem;
- an explicit reciprocity law;
- numerical stabilization for a curve;
- novelty, priority, or MATHCERT certification.

## Successor

The next substantive tranche is WP17A source reconnaissance, now narrowly constrained by the exact invariant:

> Find and admit only theorem interfaces that literally apply at `p=2` and control the primitive rank-one dual Selmer torsion/Fitting invariant over the protected WP09 imaginary quadratic field, or an explicitly comparable Selmer-complex invariant with every local comparison defect computed exactly.

WP18 may now begin against the fixed finite/integral invariant, but numerical agreement remains observational only.
