# WP60I theorem — selected literal-`p=2` BSS H2 holds and H3 fails

## 1. Protected setup

Work in the selected `BSD-R2-A1` class: `E/Q` is semistable, has odd conductor, good ordinary reduction at `2`, and irreducible `E[2]`.

Protected WP12 proves

`im(rho_bar_{E,2}) = GL_2(F_2) ~= S3`.

For an odd bad prime `ell|N`, protected WP13 writes

`n_ell := ord_ell(Delta_min)>0`

and proves, in a compatible Tate basis,

`rho_{2^m}(sigma) = [[1,n_ell*t_m(sigma)],[0,1]]`

for `sigma in I_ell`, where

`t_m:I_ell -> Z/2^m Z`

is surjective. In particular, residual inertia is nontrivial exactly when `n_ell` is odd.

Protected MATHFORGE WP60F records the BSS standard hypotheses relevant here. Formally at literal `p=2` and for the elliptic Tate module `T=T_2(E)`, they include:

- `(H2)`: there exists `tau in G_{F_{2^infinity}}` such that `T/(tau-1)T` is free of rank one;
- `(H3)`: the two residual first-cohomology groups over `F(T)_{2^infinity}/K` vanish.

We determine these conditions for the base specialization `K=F=Q` used by the selected lane.

## 2. A selected curve must have odd residual ramification

### Lemma `BSD-A1-WP60I-ODD-DEPTH-001`

Every selected curve has an odd bad prime `ell|N` with `n_ell` odd.

### Proof

Assume instead that `n_ell` is even for every odd bad prime. By WP13, `E[2]` is then unramified at every bad odd prime. At every good odd prime it is unramified by good reduction and `ell != 2`. Therefore the residual division field

`L:=Q(E[2])`

is unramified outside `2`.

WP12 gives `Gal(L/Q)=S3`. Let `M` be any cubic subfield. Then `M/Q` is also unramified outside `2`, so its absolute discriminant has the form

`|D_M|=2^a`.

We bound `a` locally. A degree-three etale `Q_2`-algebra can have:

1. no ramified factor, contributing discriminant exponent `0`;
2. a ramified cubic field factor. Its ramification index is `3`, which is prime to the residue characteristic `2`, so it is tame and contributes exponent `2`;
3. a ramified quadratic field factor together with a linear factor. A quadratic extension of `Q_2` has discriminant exponent at most `3` (equivalently, using the standard square-class representatives of `Q_2^x/(Q_2^x)^2`, the ramified quadratic discriminants have `2`-adic exponent `2` or `3`).

Hence `a<=3` and therefore `|D_M|<=8`.

Minkowski's discriminant bound for a cubic field gives

`|D_M| >= (pi/4)^(2*r_2) * 3^6/(3!)^2`,

where `r_2` is `0` or `1`. The smaller of the two bounds occurs for `r_2=1` and is

`(pi/4)^2 * 729/36 > 12`.

This contradicts `|D_M|<=8`.

Therefore some odd bad prime has `n_ell` odd. QED.

## 3. The BSS H2 condition holds

### Theorem `BSD-A1-WP60I-H2-002`

For every selected curve, the formal literal-`2` BSS condition `(H2)` holds for `K=F=Q`.

### Proof

Choose `ell` as in Lemma `BSD-A1-WP60I-ODD-DEPTH-001`. Passing to the inverse limit of the compatible WP13 Tate bases gives

`rho_2(sigma) = [[1,n_ell*t(sigma)],[0,1]]`

on inertia, with a surjective tame character

`t:I_ell -> Z_2`.

Since `n_ell` is odd, choose `tau in I_ell` with

`t(tau)=n_ell^(-1) in Z_2`.

Then, after a change of `Z_2`-basis,

`rho_2(tau)=U:= [[1,1],[0,1]]`.

Because `ell` is odd, every `2`-power root of unity is unramified at `ell`. Hence inertia at `ell` acts trivially on `Q(mu_{2^infinity})`, and

`tau in G_{Q(mu_{2^infinity})}`.

For `T=Z_2^2`,

`(U-1)(x,y)=(y,0)`.

Thus `(U-1)T=Z_2*(1,0)` and

`T/(U-1)T ~= Z_2`,

free of rank one. This is exactly `(H2)` in the protected BSS interface for `K=F=Q`, since `Q_{2^infinity}=Q(mu_{2^infinity})`: `Q` has trivial Hilbert-class contribution and adjoining compatible `2`-power roots of its units `+-1` adds no field beyond the cyclotomic `2`-power tower. QED.

## 4. The selected mod-4 image is full

Let

`G_4 := rho_4(G_Q) <= GL_2(Z/4)`

and

`H_4 := rho_4(G_{Q(mu_{2^infinity})}) <= SL_2(Z/4)`.

The determinant containment follows from the Weil pairing: `det(rho_2)` is the `2`-adic cyclotomic character.

### Lemma `BSD-A1-WP60I-MOD4-003`

For every selected curve,

`H_4 = SL_2(Z/4)`

and

`G_4 = GL_2(Z/4)`.

### Proof

The element `tau` above belongs to the restricted group and has image

`U=[[1,1],[0,1]] mod 4`.

The reduction of `H_4` modulo `2` is a normal subgroup of

`G_4 mod 2 = GL_2(F_2) ~= S3`.

It contains the nontrivial unipotent `U mod 2`, which is a transposition in `S3`. The only normal subgroup of `S3` containing a transposition is all of `S3`. Hence

`H_4 mod 2 = SL_2(F_2)=GL_2(F_2)`.

Now

`U^2 = I + 2E_12 mod 4`.

The kernel of

`SL_2(Z/4) -> SL_2(F_2)`

is

`K={I+2A : A in M_2(F_2), tr(A)=0}`.

It is an elementary abelian group under

`(I+2A)(I+2B)=I+2(A+B)`.

Because `H_4` surjects onto `SL_2(F_2)`, conjugating `U^2` by lifts in `H_4` gives every element `I+2(gE_12g^(-1))` for `g in SL_2(F_2)`. The orbit contains

`E_12`, `E_21`, and `[[1,1],[1,1]]`,

which form an `F_2`-basis of the trace-zero subspace of `M_2(F_2)`. Therefore `K subset H_4`. Since `H_4` also surjects modulo `2`,

`H_4=SL_2(Z/4)`.

Finally the determinant of the full representation is the cyclotomic character. Complex conjugation has determinant `-1=3 mod 4`, so `G_4` contains an element of determinant `3`. Since it already contains `H_4=SL_2(Z/4)`, the kernel of determinant, it follows that

`G_4=GL_2(Z/4)`. QED.

## 5. Exact nonzero cohomology at mod 4

Let

`V=F_2^2`

with the natural action of `GL_2(Z/4)` through reduction modulo `2`.

### Lemma `BSD-A1-WP60I-GL2Z4-H1-004`

`H^1(GL_2(Z/4),V) != 0`.

### Exact certificate

Set

`S=[[0,-1],[1,0]]`,

`T=[[1,1],[0,1]]`,

`D=[[-1,0],[0,1]]`

in `GL_2(Z/4)`.

The accompanying exact verifier proves that these matrices generate all `96` elements of `GL_2(Z/4)` and that the assignments

`z(S)=(0,0)`,

`z(T)=(0,1)`,

`z(D)=(1,1)`

extend consistently to a crossed homomorphism

`z(gh)=z(g)+(g mod 2)z(h)`

on the whole group. It checks this identity for all `96^2=9216` ordered pairs.

Moreover,

`T^2=[[1,2],[0,1]]`

acts trivially on `V`, while the certified cocycle satisfies

`z(T^2)=(1,0) != 0`.

Every coboundary has the form

`delta_v(g)=g*v-v`.

Since `T^2` acts trivially on `V`, every coboundary vanishes at `T^2`. Hence `z` is not a coboundary and its cohomology class is nonzero. QED.

The executable certificate is

`work_packages/BSD_R2_A1_WP60I_BSS_H2_H3_SELECTED_LANE/02_GL2Z4_H1_CERTIFICATE.py`.

## 6. The BSS H3 condition fails

### Theorem `BSD-A1-WP60I-H3-FAIL-005`

For every selected curve, the formal literal-`2` BSS condition `(H3)` fails for `K=F=Q`.

### Proof

For `K=F=Q`, the BSS field `F_{2^infinity}` is `Q(mu_{2^infinity})` as noted above. The Weil pairing gives

`Q(mu_{2^infinity}) subset Q(E[2^infinity])`.

Therefore the BSS field

`F(T)_{2^infinity}`

is simply the full `2`-power division field `Q(E[2^infinity])`.

Write

`Gamma:=Gal(Q(E[2^infinity])/Q)=im(rho_2)`.

Lemma `BSD-A1-WP60I-MOD4-003` gives a quotient

`Gamma -> GL_2(Z/4)`.

Its kernel acts trivially on the residual module `V=E[2]`. The inflation-restriction sequence therefore begins with an injection

`H^1(GL_2(Z/4),V) -> H^1(Gamma,V)`.

By Lemma `BSD-A1-WP60I-GL2Z4-H1-004`, the source is nonzero. Hence

`H^1(F(T)_{2^infinity}/Q,E[2]) != 0`.

This already contradicts `(H3)`. In addition, the Weil pairing identifies

`E[2] ~= E[2]^vee(1)`

as `G_Q`-modules, so the dual cohomology group in `(H3)` is nonzero as well. QED.

## 7. Exact disposition

Combine Theorems `BSD-A1-WP60I-H2-002` and `BSD-A1-WP60I-H3-FAIL-005`:

`BSS_LITERAL_P2_SELECTED_H2_HOLDS_H3_FAILS`.

Therefore the WP60F F2 obligation is no longer an unresolved implication boundary. It has a negative selected-lane determination:

`R5_BSS_STANDARD_HYPOTHESIS_ROUTE_BLOCKED_BY_H3_AT_LITERAL_P2`.

This means the currently screened BSS application theorem cannot be made applicable to the selected lane merely by repairing its `p>3` proof of the large-image implication. The target itself violates `(H3)` at `p=2`.

A future BSS-derived route can reopen only with a theorem that removes, weakens, or bypasses `(H3)`, or with a different Fitting-control architecture whose hypotheses are actually satisfied.

## 8. Claim firewall

WP60I does not establish:

- the WP60H F1 three-term-relation exclusion or replacement connectivity;
- a literal-`2` version of BSS Theorem 5.2, 5.20, or the elliptic application theorem;
- impossibility of every Euler/Kolyvagin/Fitting argument at `p=2`;
- R5-LIFT, R5-PRIM, D2d, or `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.
