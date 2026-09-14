# BSD-R2-A1-WP60A-A0 — exact determinant dependency map

## Purpose

This package executes WP60A stage A0 from `grandchallenge/MATHSOLVE#215`.

It does not prove the missing literal-`p=2` analytic determinant theorem. It reconstructs the protected algebraic determinant spine, identifies exactly where the analytic class must enter, and reduces D1c to two separate arithmetic obligations that can be attacked without repeating already closed local-comparison work.

## Protected inputs

- MATHSOLVE protected baseline: `24fb349e28e4cbb5e034f4684edcc413975aed04`.
- MATHFORGE protected WP60A source audit: `e44baeeed5d508fd4e5332c883c837951e51c000`.
- Constitutional issuance anchor: `grandchallenge/INTELLECT@fc9ee5537bf07586dffcc621e753204ecd835365`.
- WP60 tracker: `grandchallenge/MATHSOLVE#215`.
- Parent programme owner: `grandchallenge/MATHSOLVE#164`.

All executing agents must re-fetch live protected state before relying on these issuance anchors.

## Exact algebraic target

Protected WP16A/WP16B/WP19 give

`v_2(Fitt^1_{Z_2}(X_E))
 = v_2(Fitt^0_{Z_2}(T_E))
 = len_{Z_2} Sha(E/Q)[2^infinity]
 = lim_n (ord_2 #Sel_{2^n}(E/Q)-n)`.

Thus the selected BSD lane requires an exact analytic identification of this primitive first-Fitting ideal, not another estimate for finite Selmer growth.

## Exact cyclotomic determinant spine

Protected WP35 supplies a square cyclotomic presentation

`0 -> Lambda^r --A(T)--> Lambda^r -> X_infty -> 0`

and the exact rank-one specialization identity

`(coeff_T det A(T)) Z_2
 = Fitt^0_{Z_2}(C_E^vee)
   Fitt^1_{Z_2}(X_E)
   B_A`.

Protected WP36 and later comparison packages compute the finite local/control terms that enter this line.

Protected WP52A closes the full strict/Kummer finite determinant correction. Therefore a new proof must not reintroduce these already computed factors as independent unknowns.

## A0 conclusion

The missing datum is not an unknown algebraic determinant or local correction. It is the integral analytic generator at the height-one prime `(2)`.

The protected provider audit at MATHFORGE `e44baeeed5d508fd4e5332c883c837951e51c000` confirms that Burns–Kurihara–Sano provide the structurally correct determinantal-zeta architecture, but the located determinant-lift proof excludes literal `p=2`, and its Stark/Kolyvagin regulator mechanism relies on a theorem requiring `p>3`.

Moreover, existence of a determinant lift and primitivity of that lift are logically distinct.

WP60A therefore splits D1c into:

1. `A1-LIFT`:
   `MISSING_P2_KATO_ZETA_DETERMINANT_LIFT_AT_RESIDUE_CHARACTERISTIC_2`;
2. `A1-PRIMITIVITY`:
   `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.

Combined refinement:

`MISSING_LITERAL_P2_KATO_ZETA_DETERMINANT_LIFT_AND_PRIMITIVITY_AT_HEIGHT_ONE_2`.

These refine, but do not replace as campaign authority, the protected parent boundary

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

## Immediate successor

Proceed to WP60A-A1 with `A1-LIFT` first.

The preferred proof route is a direct finite-level determinant lift or primitive Kummer/Fitting reciprocity argument at `p=2`, avoiding the odd-prime Stark/Kolyvagin regulator chain.

If a lift is obtained, do not declare D1c or WP59 R5 closed. Immediately attack `A1-PRIMITIVITY`: prove exact reverse divisibility/basis/primitivity at `(2)` and replay the full protected specialization line.

## Claim firewall

This package does not prove:

- a `p=2` extension of BKS/BSS;
- existence of a determinant lift at `p=2`;
- primitivity of a determinantal zeta element at `(2)`;
- the primitive first-Fitting reciprocity theorem;
- WP59 reopening condition `R5`;
- `BSD-R2-A1`;
- fixed-`2` height nondegeneracy;
- D2d or D2e;
- MATHCERT certification.
