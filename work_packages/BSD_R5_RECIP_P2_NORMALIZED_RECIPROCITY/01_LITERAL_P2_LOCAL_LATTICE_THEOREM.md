# BSD R5-RECIP — literal-`p=2` local Kummer / logarithm / dual-exponential lattice

## Record

- Campaign: `BSD-001`.
- Operation: `BSD-R5-RECIP` / `grandchallenge/MATHSOLVE#278`.
- Exact live protected operation base: `7d72d4f8aec2019a8eefb4db4fe151e4f14b1211`.
- Mathematical predecessor: protected R5-RES completion `24081fcc1b212d33dd865cc5512a837b8101faf1`.
- Protected source provider: `grandchallenge/MATHFORGE@8b16da7ec245cfef30c318518401b0f474fc1fb8`.
- Protected local predecessor: WP60B theorem `BSD-A1-WP60B-ORDINARY-LOG-001`.

The purpose of this note is to replay the good-reduction local lattice calculation underlying Kim Lemma 3.3 at literal `p=2` on the selected BSD-001 lane. It does not address the plus modular-symbol / Kurihara normalization.

## 1. Selected local setup

Let `E/Q_2` be the selected local elliptic curve. Protected hypotheses give:

- good ordinary reduction at `2`;
- `a_2 in {+1,-1}`;
- `q_2 := #E(F_2) = 3-a_2 in {2,4}`;
- a minimal Néron differential `omega_E`;
- the standard formal parameter `t=-x/y` on the formal group;
- protected WP60B:

  `log_{omega_E}(E_1(Q_2)) subset 4 Z_2`.

For `r>=1`, write `E_r(Q_2)` for the formal subgroup with parameter in `2^r Z_2`. Then

`E_1(Q_2)/E_2(Q_2) ~= 2Z_2/4Z_2 ~= F_2`

as additive groups.

Let

`T_loc := E(Q_2)[2^infinity]`,

and write

`#T_loc = 2^{t_2}`.

Because `E(F_2)` has 2-power order and `E_1(Q_2)` is pro-2, all local torsion is 2-primary; thus this is the full torsion subgroup relevant to the logarithm lattice.

## 2. The deep formal logarithm is exactly `4 Z_2`

### Lemma `BSD-R5-RECIP-LOCAL-DEEPLOG-001`

The formal logarithm restricts to an isomorphism

`log_{omega_E}: E_2(Q_2) -> 4 Z_2`.

### Proof

Write the invariant differential in the formal parameter as

`omega_E = g(t) dt`,

with `g(t) in Z_2[[t]]` and constant coefficient `1`. Hence

`L(t):=log_{omega_E}(t)=t+sum_{n>=2} b_n t^n/n`

with `b_n in Z_2` after reindexing the integral coefficients of `g`.

If `t in 4Z_2`, then for every `n>=2`,

`ord_2(t^n/n) >= 2n-ord_2(n) >= 3`.

Therefore

`L(t) congruent t (mod 8Z_2)`

on `4Z_2`, and `L'(t)=g(t)` is a 2-adic unit there. The usual successive-approximation / inverse-function argument on the complete ball `4Z_2` gives a unique solution `t in 4Z_2` to `L(t)=y` for each `y in 4Z_2`. Thus `L` is a bijective continuous homomorphism from the formal group on `4Z_2` to the additive group `4Z_2`.

QED.

## 3. The shallow anomaly is exactly one formal rational 2-torsion point

### Theorem `BSD-R5-RECIP-LOCAL-FORMAL-TORS-002`

`E_1(Q_2)[2^infinity]` has order exactly `2`.

Equivalently, the kernel of

`log_{omega_E}: E_1(Q_2) -> Q_2`

has order exactly `2`.

### Proof

Protected WP60B gives

`log(E_1(Q_2)) subset 4Z_2`.

Lemma `DEEPLOG-001` gives

`log(E_2(Q_2)) = 4Z_2`.

Since `E_2 subset E_1`, both inclusions force

`log(E_1(Q_2)) = log(E_2(Q_2)) = 4Z_2`.

For any `P in E_1(Q_2)`, choose the unique `Q in E_2(Q_2)` with

`log(Q)=log(P)`.

Then `P-Q` lies in the kernel of the logarithm. Moreover the kernel meets `E_2` trivially because `log|_{E_2}` is injective. Hence

`E_1(Q_2) = ker(log) + E_2(Q_2)`

with trivial intersection, and therefore

`ker(log) ~= E_1(Q_2)/E_2(Q_2)`.

The latter group has order `2`. The formal logarithm kills torsion, while the kernel just computed is a finite subgroup; hence the kernel is precisely the formal 2-primary torsion and has order `2`.

QED.

### Corollary `BSD-R5-RECIP-LOCAL-TEXP-003`

`t_2 >= 1`, and under the reduction map

`T_loc -> E(F_2)`

the kernel has order `2`, so the reduction image of local 2-primary torsion has order

`2^{t_2-1}`.

In particular

`2^{t_2-1} | q_2`.

## 4. Exact free logarithm lattice

Let

`G := E(Q_2)/T_loc`

and

`H := E_1(Q_2)/E_1(Q_2)[2^infinity]`.

Both are free rank-one `Z_2`-modules. The inclusion `E_1 -> E(Q_2)` induces `H -> G`.

### Lemma `BSD-R5-RECIP-LOCAL-INDEX-004`

`[G:H] = q_2 / 2^{t_2-1}`.

### Proof

Good reduction gives the exact reduction sequence

`0 -> E_1(Q_2) -> E(Q_2) -> E(F_2) -> 0`.

The torsion subgroup maps to a subgroup of `E(F_2)` of order `2^{t_2-1}` by Corollary `TEXP-003`. Quotienting by local torsion therefore gives

`[G:H] = #E(F_2) / #red(T_loc) = q_2 / 2^{t_2-1}`.

QED.

### Theorem `BSD-R5-RECIP-LOCAL-LOGLATTICE-005`

The logarithm induces an injective map on `G` with exact image lattice

`log_{omega_E}(G) = (2^{t_2+1}/q_2) Z_2`.

### Proof

By Theorem `FORMAL-TORS-002`, logarithm kills precisely the torsion on `E_1`, and by construction it kills all of `T_loc`. Thus it descends to the free rank-one quotient `G` and is injective there.

On `H`, Theorem `FORMAL-TORS-002` and Lemma `DEEPLOG-001` give

`log(H)=4Z_2`.

The submodule `H subset G` has index

`d=q_2/2^{t_2-1}`.

For rank-one `Z_2` lattices, enlarging the domain by index `d` enlarges the image lattice by the same index. Hence

`log(G) = (4/d)Z_2
        = (4 * 2^{t_2-1}/q_2)Z_2
        = (2^{t_2+1}/q_2)Z_2`.

QED.

This is exactly the logarithm lattice reciprocal to the good-reduction formula printed in Kim Lemma 3.3, now derived at literal `p=2` from the protected selected local geometry.

## 5. Literal-2 dual-exponential image

Let `T=T_2(E)`. Write `H^1_f(Q_2,T)` for the Bloch--Kato finite local condition and

`H^1_s(Q_2,T):=H^1(Q_2,T)/H^1_f(Q_2,T)`.

The Kummer map identifies the finite local condition with the 2-adic completion of `E(Q_2)`. Local Tate duality, using the Weil-pairing self-duality of `T` and the dual tangent basis paired with `omega_E`, identifies `H^1_s(Q_2,T)` with the `Z_2`-linear dual of the free Kummer lattice. Under this identification, the Bloch--Kato dual exponential is the functional paired with the formal logarithm.

Consequently the dual-exponential image lattice is the reciprocal of Theorem `LOGLATTICE-005`.

### Theorem `BSD-R5-RECIP-LOCAL-DUALEXP-006`

On the selected good-ordinary literal-2 lane,

`exp^*_{omega_E}(H^1_s(Q_2,T))
 = (q_2 / 2^{t_2+1}) Z_2
 = (#E(F_2) / #E(Q_2)[2^infinity]) * (1/2) Z_2`.

Equivalently, the good-reduction lattice formula of Kim Lemma 3.3 extends to this selected `p=2` lane with the **same normalized expression** once the unavoidable formal rational 2-torsion is retained.

### Proof

By Theorem `LOGLATTICE-005`, the free Kummer logarithm lattice is

`L=(2^{t_2+1}/q_2)Z_2`.

Its exact `Z_2`-dual lattice in `Q_2` is

`L^vee=(q_2/2^{t_2+1})Z_2`.

Bloch--Kato local duality identifies `H^1_s(Q_2,T)` with this dual lattice through `exp^*_{omega_E}`. Multiplication by a `Z_2`-unit does not alter a rank-one `Z_2` lattice, so the lattice equality is independent of basis-unit choices. This yields the displayed equality.

QED.

## 6. Torsion-coefficient extension

Let `I subset Z_2` be a nonzero Kolyvagin coefficient ideal occurring in the protected WP60T finite derivative system. The propagated finite local condition satisfies

`H^1_f(Q_2,T/IT) = image(H^1_f(Q_2,T) -> H^1(Q_2,T/IT))`.

The cohomology exact sequence gives

`0 -> H^1(Q_2,T)/(I H^1(Q_2,T)+H^1_f(Q_2,T))
   -> H^1(Q_2,T/IT)/H^1_f(Q_2,T/IT)
   -> H^2(Q_2,T)[I] -> 0`.

The left term is free rank one over `Z_2/I`: by Theorem `DUALEXP-006`, reduction of `exp^*` identifies it with

`(q_2/2^{t_2+1})Z_2 /
 I(q_2/2^{t_2+1})Z_2 ~= Z_2/I`.

Exactly as in Kim Proposition 3.10, the sequence therefore splits as `Z_2/I`-modules, and the integral dual exponential extends to torsion coefficients by projection to the free rank-one summand followed by reduction of the lattice.

### Theorem `BSD-R5-RECIP-LOCAL-TORSIONCOEFF-007`

There is a literal-2 torsion-coefficient dual-exponential map compatible with the propagated WP60T local condition,

`exp^*_{omega_E,I}:
 H^1(Q_2,T/IT)/H^1_f(Q_2,T/IT)
 -> (q_2/2^{t_2+1})Z_2 /
    I(q_2/2^{t_2+1})Z_2`,

whose restriction to the image of integral cohomology is the naive reduction of the integral dual exponential.

After fixing a lattice isomorphism

`xi_I:
 (q_2/2^{t_2+1})Z_2 /
 I(q_2/2^{t_2+1})Z_2
 ~= Z_2/I`,

this supplies the exact local map required by the protected R5-RECIP source decomposition.

## 7. Local disposition

The source obligation `R5-RECIP-LOCAL` is established on the selected lane by Theorems

- `BSD-R5-RECIP-LOCAL-DEEPLOG-001`;
- `BSD-R5-RECIP-LOCAL-FORMAL-TORS-002`;
- `BSD-R5-RECIP-LOCAL-TEXP-003`;
- `BSD-R5-RECIP-LOCAL-INDEX-004`;
- `BSD-R5-RECIP-LOCAL-LOGLATTICE-005`;
- `BSD-R5-RECIP-LOCAL-DUALEXP-006`;
- `BSD-R5-RECIP-LOCAL-TORSIONCOEFF-007`.

The old qualitative concern that WP60B's extra factor of `2` necessarily creates an additional denominator is therefore false on this selected lane: the same local geometry forces exactly one formal rational 2-torsion point, and the two effects compensate in the free logarithm lattice.

The remaining reciprocity obligation is the independent source-identified analytic layer:

`MISSING_P2_INTEGRAL_PLUS_MODULAR_SYMBOL_KURIHARA_NORMALIZATION`.

## 8. Claim firewall

This theorem does **not** establish:

- literal-2 integral plus modular-symbol / Kurihara normalization;
- the full normalized Kato/Kurihara reciprocity identity;
- a nonzero normalized finite Kurihara witness;
- residual Kato/Kolyvagin nonvanishing;
- R5-RES;
- R5-PRIM;
- D2d;
- BSD-R2-A1;
- novelty or priority;
- public certification or MATHCERT certification.
