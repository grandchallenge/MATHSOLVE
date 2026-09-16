# BSD R5-PRIM reduction theorem — exact normalized Kato–Kolyvagin index

## 1. Scope

Fix a selected `BSD-R2-A1` curve `E/Q` and put `T=T_2(E)`.

Protected R5-LIFT gives the literal-`2` determinant-membership statement at the height-one prime
`(2)`. Protected WP60A-A1 gives the exact DVR criterion: if the localized Kato class is

`z = a P`

relative to a primitive basis `P` of rank-one `H^1`, and

`h := length(H^2)`,

then

- determinant membership is `v_2(a) >= h`;
- determinant-generator status is `v_2(a) = h`.

The first statement is protected as `R5_LIFT_ESTABLISHED`. The second is the entering
`R5-PRIM` frontier.

## 2. The literal-2 Kolyvagin-system line already exists

Protected WP60R and WP60S establish, on the exact selected literal-`2` lane,

`KS_infty ~= Z_2`,

together with integral regulator compatibility and the following Fitting rule. For every
`kappa in KS_infty`, the integral Kolyvagin ideals satisfy

`I_i(kappa) subset Fitt^i_Z2(X)`,

and for a basis Kolyvagin system `kappa_*` equality holds for every `i`.

Protected WP60T and R5-LIFT identify the selected Kato derivative with a compatible element

`kappa^Kato in KS_infty`

whose first component is the protected Kato class under the exact finite/inverse-limit comparison.

These are repository theorems already admitted at literal `p=2`; no odd-prime specialization is
used here.

## 3. Exact divisibility index

Because `KS_infty` is free of rank one, choose any basis `kappa_*`. There are a unique integer
`M_Kato >= 0` and a unit `u in Z_2^x` such that

`kappa^Kato = 2^(M_Kato) u kappa_*`.

The integer `M_Kato` is basis-independent. Equivalently,

`M_Kato = max{m >= 0 : kappa^Kato in 2^m KS_infty}`.

At finite level it is the common `2`-divisibility measured by the Kato-derived system before
reduction modulo sufficiently large `2^r`. This is the literal-`2` counterpart of the minimal
Kolyvagin-system divisibility index isolated by the protected Castella–Sano source audit.

### Lemma `BSD-R5-PRIM-SCALE-001`

For every `i`,

`I_i(kappa^Kato) = 2^(M_Kato) I_i(kappa_*)`.

### Proof

Each finite Kolyvagin ideal is generated functorially by the corresponding components of the
Kolyvagin system. Multiplying a system by a scalar multiplies every component, and therefore
every generated ideal, by that scalar. Passing through the protected compatible inverse system
preserves this equality. Multiplication by the unit `u` does not change an ideal of `Z_2`.
QED.

Hence, using the protected basis equality,

`I_i(kappa^Kato) = 2^(M_Kato) Fitt^i_Z2(X)`.

Thus all extra divisibility of the Kato-derived Kolyvagin system is concentrated in the single
integer `M_Kato`.

## 4. Literal-2 replay of the Castella–Sano structure dependency

The protected source audit records that Castella–Sano use a p>3 Mazur–Rubin structure theorem to
separate the index of the first Kato component into:

1. the strict-dual-Selmer/Fitting contribution; and
2. the common divisibility index of the Kato Kolyvagin system.

On the selected literal-`2` lane, the first ingredient is already supplied by WP60R/WP60S:
rank-one Kolyvagin-system freeness, core-vertex projection, and exact Fitting equality for a
basis. Lemma `SCALE-001` then supplies the same separation algebraically without importing the
p>3 theorem.

Record:

`P2_KATO_KOLYVAGIN_STRUCTURE_FORMULA_REPLAYED`.

This replay establishes the *form* of the primitivity defect. It does not evaluate `M_Kato`.

## 5. Literal-2 replay of the rigidity dependency

The protected source audit records that Castella–Sano Proposition 2.1.5 proves invariance of the
minimal divisibility index after passing to arbitrarily deep auxiliary-prime sets by replacing
prime factors one at a time, using residual localization, finite-singular relations, global
reciprocity, and a nondegenerate local Tate pairing.

Protected WP60R supplies the selected literal-`2` replacements needed for this mechanism:
pairwise localization, injective localization families, finite-singular comparison, iterative
dual killing, and connected core graphs. The same one-prime-at-a-time transport therefore does
not create an independent p>3 obstruction on this selected lane.

Record:

`P2_KATO_KOLYVAGIN_RIGIDITY_REPLAYED`.

Again, rigidity preserves a divisibility index; it does not determine its value.

## 6. Exact normalization and R5-PRIM equivalence

Let

`c_det(E) := h = length(H^2)`

denote the exact protected height-one determinant-lattice exponent in the WP60A-A1 normalization.
All real-place, strict/Kummer, bad-prime, coefficient/index, and finite comparison terms already
incorporated into the protected R5-LIFT determinant complex remain part of this `H^2`; none may
be dropped or replaced by an unspecified unit.

The Castella–Sano source architecture describes the same issue as the normalized common
divisibility of the Kato Kolyvagin system after explicit local/Selmer factors are removed.
Accordingly define the normalized excess

`epsilon_Kato(E) := v_2(a) - c_det(E) >= 0`.

By protected R5-LIFT, the inequality is known.

### Theorem `BSD-R5-PRIM-REDUCTION-002`

On the selected literal-`2` lane,

`R5_PRIM_ESTABLISHED`

is equivalent to

`epsilon_Kato(E) = 0`.

Under the protected determinant-to-Stark-to-Kolyvagin identifications, this is equivalently the
statement that the selected Kato-derived Kolyvagin system has no common factor of `2` beyond the
explicit protected determinant/Selmer normalization. In Castella–Sano terminology, it is the
exact normalized Kato–Kolyvagin minimal-divisibility-index equality.

### Proof

WP60A-A1 gives determinant-generator status iff `v_2(a)=c_det(E)`. R5-LIFT gives
`v_2(a)>=c_det(E)`. Sections 2–5 identify the only surviving integral scaling defect in the
Kato-derived Kolyvagin-system line with its common `2`-divisibility after the protected
local/Selmer determinant factors are retained. Therefore equality of the determinant coordinate
is exactly zero normalized excess, and conversely. QED.

Record:

`R5_PRIM_EQUIVALENT_TO_P2_KATO_KOLYVAGIN_PRIMITIVITY_INDEX_EQUALITY`.

## 7. Why the equality is not currently proved

No protected MATHSOLVE theorem evaluates the normalized excess `epsilon_Kato(E)`.

The newly protected MATHFORGE audit identifies two possible ways to obtain that value:

1. a direct literal-`2` proof of the normalized Kato–Kolyvagin primitivity-index equality; or
2. a literal-`2` explicit-reciprocity/refined-Kurihara bridge that computes the same index.

The source theorems used for the latter route are stated with `p>3` and are not admitted as
literal-`2` interfaces. Bare nonvanishing of the first Kato class is insufficient: a nonzero
element of a rank-one `Z_2` module may still be divisible by `2`.

Therefore the first independent missing arithmetic theorem is

`MISSING_P2_KATO_KOLYVAGIN_PRIMITIVITY_INDEX_EQUALITY`.

This is a substantive evidentiary boundary, not an infrastructure or source-discovery failure.

## 8. Disposition

Entering frontier:

`MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.

Disposition:

`BLOCKED`.

Exact successor:

`MISSING_P2_KATO_KOLYVAGIN_PRIMITIVITY_INDEX_EQUALITY`.

The reduction is material: the opaque determinant-basis question has been reduced to one scalar
integral arithmetic equality after the structural and rigidity dependencies have been replayed
at literal `2`.

## 9. Claim firewall

This theorem does not establish:

- `R5_PRIM_ESTABLISHED`;
- a literal-`2` Castella–Sano theorem;
- a literal-`2` Kurihara explicit-reciprocity theorem;
- a literal-`2` refined Kurihara equality;
- D2d;
- `BSD-R2-A1`;
- novelty or priority;
- public or MATHCERT certification.

Formal higher-level BSS Hypothesis 3.2(iii), full BSS Hypothesis 4.7/4.7(iii), and infinite BSS
H3 remain false/unavailable and are not reinstated.
