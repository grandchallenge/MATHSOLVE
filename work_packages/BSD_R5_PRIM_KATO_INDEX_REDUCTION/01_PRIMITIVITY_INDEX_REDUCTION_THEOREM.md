# BSD R5-PRIM reduction theorem — exact normalized Kato–Kolyvagin index

## 1. Scope

Fix a selected `BSD-R2-A1` curve `E/Q` and put `T=T_2(E)`.

Protected R5-LIFT gives the literal-`2` determinant-membership statement at the height-one prime
`(2)`. Protected WP60A-A1 gives the exact DVR criterion. If the localized Kato class is

`z = a P`

relative to a primitive basis `P` of rank-one `H^1`, and if

`h := length(H^2(C_(2)))`

for the exact localized perfect complex used in WP60A-A1, then

- determinant membership is `v_2(a) >= h`;
- determinant-generator status is `v_2(a) = h`.

The first statement is protected as `R5_LIFT_ESTABLISHED`. The second is the entering
`R5-PRIM` frontier.

All local, real-place, finite-control and strict/Kummer comparison terms remain governed by the
already-protected R5-LIFT normalization. This operation neither cancels nor reintroduces any such
term by analogy.

## 2. The literal-2 Kolyvagin-system line already exists

Protected WP60R and WP60S establish, on the exact selected literal-`2` lane,

`KS_infty ~= Z_2`,

together with integral regulator compatibility and the following Fitting rule. For every

`kappa in KS_infty`,

the integral Kolyvagin ideals satisfy

`I_i(kappa) subset Fitt^i_Z2(X)`,

and for a basis Kolyvagin system `kappa_*` equality holds for every `i`.

Protected WP60T and R5-LIFT identify the selected Kato derivative with a compatible element

`kappa^Kato in KS_infty`

whose first component is the protected Kato class under the exact finite/inverse-limit
comparison.

These are repository theorems already admitted at literal `p=2`; no odd-prime specialization is
used here.

## 3. Determinant coordinate equals normalized Kolyvagin divisibility

Let `D_(2)` denote the inverse determinant lattice at the height-one prime `(2)` in the protected
R5-LIFT construction.

The protected finite determinant-to-Stark maps and Stark-to-Kolyvagin regulator maps are
rank-one isomorphisms, compatible in the finite quotient system. Protected WP60S supplies the
inverse-limit Kolyvagin line. Therefore the protected R5-LIFT construction gives a rank-one
`Z_2`-linear isomorphism, unique up to a unit,

`Phi : D_(2) -> KS_infty`.

Let `delta_Kato in D_(2)` be the determinant preimage of the localized Kato class furnished by
R5-LIFT. Then

`Phi(delta_Kato) = kappa^Kato`.

Choose a basis `d_*` of `D_(2)` and put `kappa_*:=Phi(d_*)`, a basis of `KS_infty`. There are a
unique integer `M_Kato >= 0` and a unit `u in Z_2^x` such that

`delta_Kato = 2^(M_Kato) u d_*`

and hence

`kappa^Kato = 2^(M_Kato) u kappa_*`.

Thus

`M_Kato = max{m >= 0 : kappa^Kato in 2^m KS_infty}`

is basis-independent.

### Lemma `BSD-R5-PRIM-COORD-001`

In the WP60A-A1 height-one normalization,

`M_Kato = v_2(a) - h`.

### Proof

WP60A-A1 computes the image of the inverse determinant lattice under the canonical rational
determinant trivialization as

`Fitt^0(H^2(C_(2))) H^1`.

Since the coefficient ring is a DVR, a determinant basis `d_*` therefore maps to

`2^h * unit * P`.

Multiplying `d_*` by `2^(M_Kato)u` maps to

`2^(h+M_Kato) * unit * P`.

But `delta_Kato` maps to `z=aP`. Hence

`v_2(a)=h+M_Kato`.

QED.

Consequently protected R5-LIFT is exactly the statement `M_Kato>=0`, while determinant-generator
status is exactly `M_Kato=0`.

This is the normalized Kato–Kolyvagin primitivity index used below. It is the source-side common
divisibility after the protected determinant/Selmer normalization has been absorbed into
`D_(2) -> KS_infty`.

## 4. Kolyvagin ideals isolate the same scalar defect

### Lemma `BSD-R5-PRIM-SCALE-002`

For every `i`,

`I_i(kappa^Kato) = 2^(M_Kato) I_i(kappa_*)`.

### Proof

Each finite Kolyvagin ideal is generated functorially by the corresponding Kolyvagin-system
components. Multiplying a system by a scalar multiplies every component, and hence every
generated ideal, by that scalar. Protected WP60S passes these compatible equalities to the
inverse limit. Multiplication by the unit `u` does not change an ideal of `Z_2`.
QED.

Using the protected basis equality,

`I_i(kappa^Kato) = 2^(M_Kato) Fitt^i_Z2(X)`.

Thus the entire failure of the Kato-derived system to attain the basis Fitting equalities is the
single normalized scalar exponent `M_Kato`.

## 5. Literal-2 replay of the Castella–Sano structure dependency

The protected source audit records that Castella–Sano use a `p>3` Mazur–Rubin structure theorem
to separate the index of the first Kato component into the strict-dual-Selmer/Fitting
contribution plus the common divisibility index of the Kato Kolyvagin system.

On the selected literal-`2` lane, this separation is already forced by protected WP60R/WP60S and
Lemmas `COORD-001` and `SCALE-002`:

- WP60R gives finite-level Kolyvagin-system freeness and, for a basis, exact Fitting equality;
- WP60S passes rank-one freeness and Kolyvagin/Fitting ideals to `Z_2`;
- `COORD-001` identifies the determinant-basis defect with `M_Kato`;
- `SCALE-002` shows that the same exponent is the unique common Kolyvagin-ideal defect.

No `p>3` structure theorem is imported.

Record:

`P2_KATO_KOLYVAGIN_STRUCTURE_FORMULA_REPLAYED`.

The replay determines the *form* of the primitivity defect. It does not determine the value
`M_Kato`.

## 6. Literal-2 replay of the rigidity dependency

The protected source audit records that Castella–Sano Proposition 2.1.5 preserves the minimal
divisibility index while replacing auxiliary primes one at a time.

On the selected literal-`2` lane, protected WP60R gives the exact substitute:

- selected core vertices exist;
- the selected core graph is connected;
- along a core edge, the replayed BSS Lemma 5.19 finite-singular transition is an isomorphism;
- fresh-prime pairwise localization and iterative dual killing produce selected core vertices
  outside any previously fixed finite auxiliary set.

Fix `m`. Along a core edge, an `R_m=Z/2^m`-linear isomorphism preserves the largest power of `2`
dividing a component. Hence the exact component divisibility is constant along connected
core-graph paths. The fresh-prime construction permits the same value to be realized after
avoiding any prescribed finite set. Passing through the compatible finite levels by protected
WP60S preserves the integral index `M_Kato`.

Record:

`P2_KATO_KOLYVAGIN_RIGIDITY_REPLAYED`.

This replay removes the source's `p>3` rigidity theorem as an independent structural blocker.
It still does not evaluate `M_Kato`.

## 7. Exact R5-PRIM equivalence

### Theorem `BSD-R5-PRIM-REDUCTION-003`

On the selected literal-`2` lane, the following are equivalent:

1. the protected Kato determinant preimage is a basis of `D_(2)`;
2. `v_2(a)=length(H^2(C_(2)))`;
3. `M_Kato=0`;
4. the protected normalized Kato-derived Kolyvagin system is a basis of `KS_infty`;
5. its Kolyvagin ideals attain the protected basis Fitting equalities without an additional
   common factor of `2`.

### Proof

`(1)<->(2)` is WP60A-A1.  
`(1)<->(3)<->(4)` follows from the rank-one isomorphism `Phi` and `COORD-001`.  
`(3)<->(5)` follows from `SCALE-002` and the protected basis Fitting equality.
QED.

Record:

`R5_PRIM_EQUIVALENT_TO_P2_KATO_KOLYVAGIN_PRIMITIVITY_INDEX_EQUALITY`.

Thus the remaining R5-PRIM question is no longer an unspecified reverse divisibility. It is the
single arithmetic equality

`M_Kato = 0`

in the protected normalized determinant/Kolyvagin coordinate.

## 8. Why the equality is not currently proved

No protected MATHSOLVE theorem evaluates `M_Kato` for the selected Kato-derived system.

The newly protected MATHFORGE audit identifies two possible ways to obtain the corresponding
source-normalized value:

1. a direct literal-`2` proof of the normalized Kato–Kolyvagin primitivity-index equality; or
2. a literal-`2` explicit-reciprocity/refined-Kurihara bridge that computes the same index before
   transport into the protected determinant normalization.

The source theorems used for the second route are stated with `p>3` and are not admitted as
literal-`2` interfaces. Bare nonvanishing of the first Kato class is insufficient: a nonzero
element of a rank-one `Z_2` module may still be divisible by `2`.

Therefore the first independent missing arithmetic theorem is

`MISSING_P2_KATO_KOLYVAGIN_PRIMITIVITY_INDEX_EQUALITY`.

This is a substantive evidentiary boundary, not an infrastructure or source-discovery failure.

## 9. Disposition

Entering frontier:

`MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.

Disposition:

`BLOCKED`.

Exact successor:

`MISSING_P2_KATO_KOLYVAGIN_PRIMITIVITY_INDEX_EQUALITY`.

The reduction is material: the determinant-basis question has been reduced to one scalar
integral arithmetic equality after the structural and rigidity dependencies have been replayed
at literal `2`.

## 10. Claim firewall

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
