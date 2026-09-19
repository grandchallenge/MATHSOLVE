# BSD R5-CW-P2-CH15 — literal-p=2 Chapter-15 compatibility replay

## Theorem identifier

`BSD-R5-CW-P2-CH15-REDUCTION-006`.

## 1. Protected inputs

Work on the selected BSD-001 lane.

Use only:

1. protected `BSD-R5-CW-P2-HALF-WEIGHT-005`, which constructs
   `Lambda_half ~= Z_2[[S]]` over `Lambda ~= Z_2[[T]]` by
   `T=2S+S^2`;
2. protected WP12, which gives
   `im(bar rho_{E,2})=GL_2(F_2) ~= S_3`;
3. protected MATHFORGE provider
   `78c18a47f0e6bdb5886c7ecfa1ba1b4c7ffff992`,
   which audits the Colmez–Wang Chapter-15 source dependencies and records the
   current density boundary;
4. the already protected literal-2 Kato/Iwasawa source interfaces consumed by
   that provider.

No density theorem is assumed except where explicitly introduced as a
conditional hypothesis below.

## 2. Generic fibre of the half-weight cover is finite etale

Put

`A=Z_2[[T]]`, `B=Z_2[[S]]`, with `T=2S+S^2`.

Equivalently,

`B ~= A[Y]/(Y^2-(1+T))`, `Y=1+S`.

Protected half-weight theory gives that `B` is finite free of rank two over
`A`.

After inverting two, the derivative of

`F(Y)=Y^2-(1+T)`

is `2Y`.  In `B[1/2]`, both `2` and `Y=1+S` are units because
`Y^2=1+T` is a group-like unit.  Hence `F'(Y)` is a unit.

Therefore

`A[1/2] -> B[1/2]`

is finite etale.

Record:

`BSD-R5-CW-P2-CH15-ETALE-001`.

The integral ramification at the residual point is real, but it disappears on
the characteristic-zero generic fibre where the Chapter-15 classical points
live.

## 3. Base change of the full deformation algebra

Let `Tcal` denote the relevant full Colmez–Wang deformation/Hecke algebra
over the principal weight algebra `A`.  Define

`Tcal_half := Tcal completed_tensor_A B`.

Because `B` is finite free rank two over `A`, completed and ordinary base
change agree on finite modules, and

`Tcal_half`

is finite free rank two as a `Tcal`-module.

Thus the base change is faithfully flat.  After inverting two it is finite
etale.

Consequences:

- exact sequences of finite `Tcal`-modules remain exact;
- finite generation is preserved;
- if a finite torsion module is annihilated by a nonzero element of `Tcal`,
  its base change is annihilated by the image of the same element;
- the nonzero annihilator remains nonzero because a faithfully flat map is
  injective.

These are precisely the formal algebraic properties required when the
Chapter-15 Poitou–Tate sequence and its finite torsion obstruction module are
pulled to the half-weight cover.

Record:

`BSD-R5-CW-P2-CH15-FLAT-PT-002`.

This statement does not assert that a missing modular-density theorem is
created by flatness.

## 4. Conditional density pulls back

Let

`f: X_half -> X`

be the characteristic-zero rigid/algebraic generic-fibre map induced by the
half-weight cover on the relevant deformation space.

By §2, `f` is finite etale and surjective.  In particular it is open.

Let `D subset X` be Zariski dense.  Every nonempty open subset
`U subset X_half` has nonempty open image `f(U)`.  Since `D` is dense,
`f(U)` meets `D`; by definition of the image, `U` then meets
`f^{-1}(D)`.

Hence `f^{-1}(D)` is Zariski dense in `X_half`.

Local absolute irreducibility of the Galois representation is unchanged by
extension of the coefficient field.  Therefore, **conditional on** density of
the Colmez–Wang locally absolutely irreducible classical locus on `X`, its
pullback is dense on the square-root cover.

Record:

`BSD-R5-CW-P2-CH15-DENSITY-PULLBACK-003`.

This is a conditional transport theorem.  It does not prove the density
hypothesis.

## 5. Cyclotomic residual irreducibility on the selected S3 lane

Let

`L=Q(E[2])`.

Protected WP12 gives

`Gal(L/Q) ~= S_3`.

Let `Q_infty/Q` be the cyclotomic `Z_2`-extension and put
`F=L cap Q_infty`.

Because `Q_infty/Q` is abelian pro-2, `Gal(F/Q)` is a 2-power quotient
of `S_3`.  Thus it is trivial or `C_2`.

Consequently

`Gal(LQ_infty/Q_infty) = Gal(L/F)`

is respectively `S_3` or `A_3 ~= C_3`.

The natural two-dimensional `F_2` representation is irreducible for
`S_3`.  Its restriction to `A_3` is also irreducible: a generator of
order three has minimal polynomial

`X^2+X+1`,

which is irreducible over `F_2`.

Hence the selected residual representation remains irreducible after
restriction to `G_{Q_infty}`.

Record:

`BSD-R5-CW-P2-CH15-CYCLOTOMIC-IRR-004`.

This supplies the selected literal-2 replacement for the cyclotomic residual
irreducibility step used in the Chapter-15 globalization argument.

## 6. Localization injectivity and Kato source scope

The protected MATHFORGE Chapter-15 audit records that the
Proposition-15.20-type localization injectivity uses the all-prime Kato inputs

- cyclotomic `H^1_Iw` torsion-freeness;
- `X^2_Iw=0`;

and does not require the separate odd-prime integral freeness upgrade that was
previously unavailable at literal two.

Those source interfaces have already been admitted in the BSD campaign.
The half-weight base change is flat by §3, so injectivity remains injectivity
after base change.

Record:

`BSD-R5-CW-P2-CH15-LOCALIZATION-005`.

No new Kato divisibility, primitivity, or residual nonvanishing statement is
asserted.

## 7. The finite sign factor is not a generic-fibre obstruction

At literal two,

`Z_2^* = {+1,-1} x (1+4Z_2)`.

Integrally, `Z_2[C_2]` is not semisimple.  After inverting two, however,

`Q_2[C_2] ~= Q_2 x Q_2`

via the idempotents

`e_+ = (1+sigma)/2`, `e_-=(1-sigma)/2`.

The Chapter-15 globalization first constructs the family class over the
generic fraction algebra before the later integral denominator-removal step.
Therefore the integral failure of semisimple sign splitting does not create an
additional obstruction at this generic-fibre globalization stage.

It may re-enter an integral argument only together with the later
denominator-removal problem, which is kept separate.

## 8. Exact reduction

Sections 2–7 discharge the square-root-cover compatibility obligations that
can be decided from existing protected inputs.

The only Chapter-15 globalization input not supplied is the source theorem:

`MISSING_P2_FULL_DEFORMATION_LOCALLY_IRREDUCIBLE_CLASSICAL_DENSITY_ON_SELECTED_S3_LANE`.

Accordingly the entering frontier

`MISSING_P2_COLMEZ_WANG_SQUARE_ROOT_COVER_CHAPTER15_GLOBALIZATION_COMPATIBILITY`

is reduced to that single substantive source boundary.

Candidate disposition:

`BLOCKED`.

The later independent boundary remains:

`MISSING_P2_COLMEZ_WANG_DENOMINATOR_REMOVAL_WITH_NONPROCYCLIC_UNITS`.

## 9. What follows if the density theorem is later supplied

If a protected source theorem supplies the missing density in exactly the
required selected literal-2 scope, then the Chapter-15 analytic-continuation
globalization can be replayed on the half-weight cover using §§2–7.

That would construct the family comparison over the relevant fraction algebra.
It would still **not** establish the integral family Kato comparison until the
separate denominator-removal boundary is discharged.

## 10. Firewall

This theorem does not establish:

- the missing density theorem;
- literal-2 integral denominator removal;
- the full literal-2 Colmez–Wang Kato comparison;
- a nonzero residual modular-symbol component;
- `c_Q^Kato mod 2 != 0`;
- `R5_RES_ESTABLISHED`;
- `R5_PRIM_ESTABLISHED`;
- D2d;
- BSD-R2-A1;
- MATHCERT certification.
