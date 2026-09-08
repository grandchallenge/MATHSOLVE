# Corrected Disegni applicability at `p=2`

## Setup

Fix an auxiliary field `K/Q` supplied by Proposition `BSD-A1-K001`. In Disegni's notation take:

- totally real field `F=Q`;
- CM quadratic extension `E_Disegni=K`;
- `p=2`;
- `pi` the automorphic representation attached to the weight-two modular form of the selected elliptic curve `E/Q`;
- `chi=1`, the trivial Hecke character of `K`;
- `Pi = pi tensor chi`.

The letter `E` in the campaign denotes the elliptic curve; the letter `E_Disegni` above denotes Disegni's CM field. They must not be conflated.

The corrected source proves Theorem B for ordinary, locally distinguished, potentially crystalline, non-exceptional representations of trivial weight satisfying condition `(star)`. We verify these hypotheses one by one.

## 1. Trivial weight

The selected elliptic curve corresponds to a weight-two modular form. With `chi=1`, its numerical weights are the trivial-weight case used by Disegni: modular weight `2` and Hecke-character weight `0`.

**Disposition:** satisfied.

## 2. Self-dual / central-character compatibility and sign

The modular representation attached to an elliptic curve over `Q` has trivial central character. The trivial Hecke character also has trivial central character. Hence Disegni's self-duality condition `omega_pi omega_chi = 1` holds.

By `BSD-A1-K001`, the auxiliary base change has analytic rank exactly one. Its global functional-equation sign is therefore `-1`.

**Disposition:** satisfied.

## 3. Ordinary at `2`

Good ordinary reduction at `2` is a defining hypothesis of `BSD-R2-A1`. It gives the ordinary filtration required by the source.

**Disposition:** satisfied.

## 4. Potential crystallinity

Good reduction at `2` makes the elliptic-curve 2-adic Galois representation crystalline. Crystalline implies potentially crystalline. Twisting by `chi=1` changes nothing.

**Disposition:** satisfied.

## 5. Corrected condition `(star)`

The correction defines `S_{p,ns}` as the `p`-adic places of `F` that are nonsplit in the CM extension and requires an inert/unramified condition at every place in that set.

Here `F=Q`, `p=2`, and the auxiliary field was chosen so that `2` splits in `K`. Therefore

`S_{2,ns} = emptyset`.

Condition `(star)` is vacuous.

**Disposition:** satisfied.

## 6. Non-exceptionality

Disegni's Lemma 6.4.6 characterizes exceptionality at a `p`-adic place by, among other equivalent conditions, the local smooth representation being special of Steinberg type.

The selected curve has good reduction at `2`; its local automorphic representation at `2` is unramified principal series, not special/Steinberg. Therefore `Pi` is not exceptional at `2`.

**Disposition:** satisfied.

## 7. Local distinction

Disegni defines local distinction by the sign conditions `(epsilon_v)` at every place. The source records two facts that are sufficient here:

1. for a self-dual representation in the sign `-1` regime of Theorem A, there is a unique incoherent quaternion datum `B` satisfying all of the local sign conditions `(epsilon_v)`;
2. at a place `v|p`, if `pi` is ordinary, the local condition is satisfied unless `v` is nonsplit in the CM extension and the representation is exceptional.

We use the quaternion datum supplied by the first statement. The second statement verifies that its `2`-adic component is compatible with the selected ordinary lane: `2` splits in `K`, and Section 6 has already shown that the representation is non-exceptional. At infinity, the source identifies the local sign condition with the weight condition, already verified in Section 1.

The all-`N`-split auxiliary packet is also the classical Heegner packet singled out by the admitted Friedberg-Hoffstein interface. No extra local sign condition is inserted by this package beyond Disegni's source-defined quaternion datum.

Thus `Pi` is locally distinguished in the exact source sense.

**Disposition:** satisfied.

## Applicability theorem `BSD-A1-PGZ001`

For at least one auxiliary `K` supplied by `BSD-A1-K001`, the corrected Disegni Theorem B applies at `p=2` to `Pi=pi tensor 1`.

Therefore, for source-admissible test vectors `f1,f2,f3,f4` with `(f3,f4)_Pi != 0`, one has

`h_V(P_Pi(f1),P_{Pi^vee}(f2)) / (f3,f4)_Pi`

`= e_{2,infinity}(V_(pi,1))^(-1) * L'_2(V_(pi,1),0) * Q((f1 tensor f2)/(f3 tensor f4)).`

The equality is exactly the kind of p-adic height-to-p-adic-L-derivative interface admitted by MATHFORGE. The theorem does not assert that either side is nonzero.

## Normalization firewall

The symbols in the displayed formula retain Disegni's normalization. In particular:

- `h_V` is a p-adic height, not the WP00 real Neron-Tate regulator;
- `L'_2` is a derivative of the source's p-adic L-function, not the complex derivative `L'(E,1)`;
- `e_{2,infinity}` and `Q` are explicit source interpolation/test-vector factors and may carry nontrivial 2-adic valuation;
- this package does not identify those factors with the WP07 unit-root correction or with the complete WP00 local ledger without a separate comparison theorem.

No normalization is silently cancelled.