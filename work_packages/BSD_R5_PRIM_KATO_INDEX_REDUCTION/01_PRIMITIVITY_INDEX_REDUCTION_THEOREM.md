# BSD R5-PRIM reduction theorem — exact cyclotomic height-one Kato–Kolyvagin index

## 1. Scope and coefficient ring

Fix a selected `BSD-R2-A1` curve `E/Q` and put `T=T_2(E)`.

Let

`Lambda := Z_2[[Gamma]] ~= Z_2[[X]]`

for the cyclotomic `Z_2`-extension, with `X=gamma-1`, and let

`q=(2)`.

Then `Lambda_q` is a discrete valuation ring. Its uniformizer is `2`; `X` is a unit in
`Lambda_q`. Write `v_q` for the normalized valuation.

Protected R5-LIFT gives the literal-`2` determinant-membership statement at `q`. Protected
WP60A-A1 gives the exact DVR criterion. If the localized Kato class is

`z = a P`

relative to a primitive basis `P` of the localized rank-one `H^1` line, and if

`h := length_{Lambda_q}(H^2(C_q))`

for the exact localized perfect complex used in WP60A-A1, then

- determinant membership is `v_q(a) >= h`;
- determinant-generator status is `v_q(a) = h`.

The first statement is protected as `R5_LIFT_ESTABLISHED`. The second is the entering
`R5-PRIM` frontier.

All real-place, strict/Kummer, finite-control and local comparison terms remain governed by the
already-protected R5-LIFT normalization. This operation neither cancels nor reintroduces any such
term by analogy.

## 2. The cyclotomic Kolyvagin line supplied by R5-LIFT

For

`R_{m,n}=Z/2^m[Gamma_n]`,

protected R5-LIFT proves compatible rank-one isomorphisms

`Pi_{m,n}: D_{m,n} -> SS_1(T_{m,n})`

and

`Reg_{m,n}: SS_1(T_{m,n}) -> KS_1(T_{m,n})`,

where `D_{m,n}` is the finite inverse-determinant line. It also constructs compatible elements

`kappa^{Kato}_{m,n} in KS_1(T_{m,n})`

whose first components are the finite Kato classes.

All maps are natural in the coefficient and cyclotomic transition maps. Taking the same inverse
limit already used in protected R5-LIFT Section 10 therefore gives an isomorphism of the
compatible cyclotomic lines

`Phi_Lambda : D_Lambda -> K_Lambda`,

where

`K_Lambda := lim_{m,n} KS_1(T_{m,n})`

and `D_Lambda` is the cyclotomic inverse-determinant line. Since `D_Lambda` is a determinant line
over the local ring `Lambda`, it is free of rank one; hence so is `K_Lambda`.

The compatible Kato family determines

`kappa^Kato_Lambda in K_Lambda`,

and the protected determinant preimage

`delta_Kato in D_Lambda`

satisfies

`Phi_Lambda(delta_Kato)=kappa^Kato_Lambda`.

This is only a passage to the compatible cyclotomic inverse limit of the already-protected
finite isomorphisms. It does not identify `K_Lambda` with the different base-level
`Z_2`-module from WP60S.

Localizing at `q` gives an isomorphism of free rank-one `Lambda_q` modules

`Phi_q : D_q -> K_q`.

Record

`P2_CYCLOTOMIC_DETERMINANT_KOLYVAGIN_LINE_IDENTIFIED`.

## 3. Exact normalized scalar defect

Choose a basis `d_*` of `D_q`, and put

`kappa_* := Phi_q(d_*)`.

Then `kappa_*` is a basis of `K_q`. Because R5-LIFT proves `delta_Kato in D_q`, there is a
unique scalar

`b_Kato in Lambda_q`

such that

`delta_Kato = b_Kato d_*`

and therefore

`kappa^Kato_q = b_Kato kappa_*`.

Changing `d_*` multiplies `b_Kato` by a unit. Hence

`M_q(kappa^Kato) := v_q(b_Kato)`

is basis-independent and nonnegative.

### Lemma `BSD-R5-PRIM-COORD-001`

In the protected WP60A-A1 height-one normalization,

`M_q(kappa^Kato) = v_q(a) - h`.

### Proof

WP60A-A1 computes the image of the inverse determinant lattice under the canonical rational
determinant trivialization as

`Fitt^0(H^2(C_q)) H^1`.

Over the DVR `Lambda_q`, this lattice is

`2^h * unit * Lambda_q P`.

Thus a determinant basis `d_*` maps to `2^h * unit * P`. Since

`delta_Kato=b_Kato d_*`

maps to the Kato class `z=aP`, one has

`v_q(a)=h+v_q(b_Kato)`.

QED.

Consequently R5-LIFT is the integrality statement `M_q(kappa^Kato)>=0`, while determinant
generator status is exactly `M_q(kappa^Kato)=0`.

This is the normalized height-one Kato–Kolyvagin primitivity index used in this package. It is a
`Lambda_q` index, not the unrelated `Z_2` divisibility of an untwisted base-level Kolyvagin
system.

## 4. Literal-2 replay of the source structure formula

The protected Castella–Sano audit records that the source structure formula separates the index
of the first Kato component into:

1. the strict-dual-Selmer/determinant contribution; and
2. the common divisibility of the cyclotomic Kato-derived Kolyvagin system.

On the selected literal-`2` lane, the same separation follows without importing the source's
`p>3` theorem:

- WP60A-A1 gives the exact determinant-lattice contribution `h`;
- R5-LIFT gives the compatible cyclotomic determinant-to-Stark-to-Kolyvagin isomorphisms;
- Lemma `COORD-001` gives the exact equality

  `v_q(a) = h + M_q(kappa^Kato)`.

This is the required structural separation in the protected normalization. Before transporting
local/Selmer factors into that normalization, the source writes the target value of its own
minimal-divisibility index using explicit local terms; this package does not identify those raw
source coordinates term-by-term at `p=2`.

Record

`P2_KATO_KOLYVAGIN_STRUCTURE_FORMULA_REPLAYED`.

The replay determines the form of the primitivity defect. It does not prove
`M_q(kappa^Kato)=0`.

## 5. Literal-2 replay of the rigidity dependency

The protected source audit records that Castella–Sano Proposition 2.1.5 preserves the minimal
divisibility index after passing to arbitrarily deep auxiliary-prime sets.

At every finite `R_{m,n}` level, protected R5-LIFT supplies the literal-`2` replacement
mechanism:

- selected core vertices exist;
- the selected core graph is connected;
- along a core edge, the replayed finite-singular transition is an `R_{m,n}`-module
  isomorphism;
- fresh-prime pairwise localization and iterative dual killing produce selected core vertices
  outside any prescribed finite auxiliary set.

For a fixed finite quotient, an `R_{m,n}`-linear isomorphism preserves membership in
`2^r` times a free rank-one component. Hence the largest visible power of `2` dividing the
Kato-derived component is constant along a connected core-graph path. The fresh-prime
construction permits the same value to be tested after avoiding any fixed finite set.

Compatibility in `m,n` then identifies these finite divisibility tests with the height-one
valuation `M_q(kappa^Kato)` of the cyclotomic scalar `b_Kato`.

Record

`P2_KATO_KOLYVAGIN_RIGIDITY_REPLAYED`.

Thus the source's `p>3` rigidity proposition is not an independent final obstruction on this
selected lane. Rigidity preserves and exposes the index; it does not evaluate it.

## 6. Exact R5-PRIM equivalence

### Theorem `BSD-R5-PRIM-REDUCTION-002`

On the selected literal-`2` lane, the following are equivalent:

1. the protected Kato determinant preimage is a basis of `D_q`;
2. `v_q(a)=length_{Lambda_q}(H^2(C_q))`;
3. `M_q(kappa^Kato)=0`;
4. the localized cyclotomic Kato-derived Kolyvagin element `kappa^Kato_q` is a basis of `K_q`;
5. the scalar `b_Kato` is a unit of `Lambda_q`.

### Proof

`(1)<->(2)` is the protected WP60A-A1 DVR criterion.  
`(1)<->(4)<->(5)` follows from the rank-one isomorphism `Phi_q`.  
`(2)<->(3)` follows from Lemma `COORD-001`.

QED.

Record

`R5_PRIM_EQUIVALENT_TO_P2_KATO_KOLYVAGIN_PRIMITIVITY_INDEX_EQUALITY`.

Thus the remaining R5-PRIM question is the single arithmetic equality

`M_q(kappa^Kato)=0`

in the protected cyclotomic height-one normalization.

This is exactly the meaning of “no extra common factor of `2` beyond the already-explicit
local/Selmer determinant factors” in the protected provider audit.

## 7. Why the equality is not currently proved

No protected MATHSOLVE theorem evaluates `M_q(kappa^Kato)`.

The protected MATHFORGE audit identifies two possible routes:

1. a direct literal-`2` proof of the normalized Kato–Kolyvagin primitivity-index equality; or
2. a literal-`2` explicit-reciprocity/refined-Kurihara bridge that computes the corresponding
   source-normalized index and transports it into the protected determinant normalization.

The source theorems used for the second route are stated with `p>3` and are not admitted as
literal-`2` interfaces. Bare nonvanishing of a Kato component is insufficient: a nonzero element
of a free rank-one module over the DVR `Lambda_q` may still be divisible by `2`.

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

The reduction is material: the determinant-basis question is reduced to one scalar
height-one arithmetic equality after the structural and rigidity dependencies have been replayed
at literal `2`.

## 9. Claim firewall

This theorem does not establish:

- `R5_PRIM_ESTABLISHED`;
- a literal-`2` Castella–Sano theorem;
- a literal-`2` Kurihara explicit-reciprocity theorem;
- a literal-`2` refined Kurihara equality;
- a term-by-term identification of the raw source normalization at `p=2`;
- D2d;
- `BSD-R2-A1`;
- novelty or priority;
- public or MATHCERT certification.

Formal higher-level BSS Hypothesis 3.2(iii), full BSS Hypothesis 4.7/4.7(iii), and infinite BSS
H3 remain false/unavailable and are not reinstated.
