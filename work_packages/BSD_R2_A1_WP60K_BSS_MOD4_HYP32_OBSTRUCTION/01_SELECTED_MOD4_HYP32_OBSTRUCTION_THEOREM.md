# WP60K theorem — selected finite BSS Hypothesis 3.2(iii) fails at `E[4]`

## 1. Protected setup

Work in the protected selected `BSD-R2-A1` class.

Protected WP60J proves

`im(rho_{E,2-adic})=GL_2(Z_2)`.

Therefore reduction modulo `4` gives

`Gal(Q(E[4])/Q)=GL_2(Z/4)`

with the natural action on

`A:=E[4] ~= (Z/4)^2`.

Protected MATHFORGE WP60F/WP60G records the BSS II finite coefficient interface. Formally at literal `p=2`, Hypothesis 3.2 requires, among other clauses,

`H^1(K(A)_M/K,A)=0`

and

`H^1(K(A)_M/K,A^*(1))=0`,

where `M` is the least power of `p` annihilating the coefficient ring and

`K(A)_M=K(A)K_M`.

For the present coefficient specialization

`K=Q`, `R=Z/4`, `A=E[4]`,

one has `M=4` and

`K(A)=Q(E[4])`.

The exact internal description of `K_4` is not needed below.

## 2. Exact finite cohomology theorem

Put

`G_4:=GL_2(Z/4)`

and

`V_4:=(Z/4)^2`

with the natural left action.

### Theorem `BSD-A1-WP60K-H1-001`

`H^1(G_4,V_4)` has order `2`.

In particular,

`H^1(G_4,V_4) != 0`.

### Exact certificate

Let

`S=[[0,-1],[1,0]]`,

`T=[[1,1],[0,1]]`,

`D=[[-1,0],[0,1]]`

in `G_4`.

The executable certificate

`02_GL2Z4_Z4_H1_CERTIFICATE.py`

proves by exhaustive integer arithmetic that:

1. `S,T,D` generate all `96` elements of `G_4`;
2. there are exactly `32` crossed homomorphisms
   `z:G_4 -> V_4`;
3. there are exactly `16` distinct coboundaries;
4. every accepted crossed homomorphism satisfies
   `z(gh)=z(g)+g z(h)`
   for every one of the `96^2=9216` ordered pairs `(g,h)`;
5. hence
   `|H^1(G_4,V_4)|=32/16=2`.

The certificate also isolates the explicit nontrivial class determined on the generators by

`z(S)=(0,0)`,

`z(T)=(0,2)`,

`z(D)=(2,2)`.

This class cannot be a coboundary. Indeed, for any

`v=(x,y) in V_4`,

a coboundary satisfies

`delta_v(T)=(T-1)v=(y,0)`.

Its second coordinate is always `0`, whereas the displayed cocycle has

`z(T)=(0,2)`.

Thus the class is visibly nonzero even independently of the cardinality count.

QED.

## 3. Inflation into the BSS finite auxiliary field

Let

`F_4:=K(A)_4=Q(E[4])K_4`.

Because `Q(E[4])` is a Galois subextension of `F_4/Q`, restriction gives a surjection

`Gal(F_4/Q) -> Gal(Q(E[4])/Q)=G_4`.

Let `N` be its kernel. Every element of `N` fixes `Q(E[4])`, hence acts trivially on

`A=E[4]`.

Therefore `A^N=A`, and inflation-restriction begins with an injection

`0 -> H^1(G_4,A)
   -> H^1(Gal(F_4/Q),A)`.

By Theorem `BSD-A1-WP60K-H1-001`, the source is nonzero. Hence

### Theorem `BSD-A1-WP60K-HYP32III-FAIL-002`

For every selected curve,

`H^1(K(E[4])_4/Q,E[4]) != 0`.

Consequently the formal literal-`p=2` BSS II Hypothesis 3.2(iii) fails for

`K=Q`, `R=Z/4`, `A=E[4]`.

QED.

## 4. Dual coefficient module

The Weil pairing gives a perfect `G_Q`-equivariant pairing

`E[4] x E[4] -> mu_4`.

Therefore

`E[4] ~= E[4]^*(1)`

as `G_Q`-modules. The same nonvanishing holds for the dual cohomology group required in Hypothesis 3.2(iii).

Thus both vanishing clauses fail at the mod-`4` coefficient level.

## 5. The other finite clauses do not cause this obstruction

The failure above is specifically clause 3.2(iii).

### Residual irreducibility

Hypothesis 3.2(i) concerns the residual module. Protected WP12 gives irreducible

`E[2]`.

### Rank-one quotient element

Protected WP60I supplies an odd bad prime `ell` and an inertia element with exact `2`-adic image

`U=[[1,1],[0,1]]`.

Odd-prime inertia fixes the finite `2`-power cyclotomic/unit extension `K_4`, so the same element lies in the required restricted Galois group. On `A=E[4]`,

`A/(U-1)A ~= Z/4`.

Thus the rank-one quotient clause 3.2(ii) is available.

### Residual invariants

BSS Hypothesis 3.3 remains satisfied by the same residual irreducibility and Weil self-duality used in WP60J.

Hence the exact new obstruction at coefficient level `E[4]` is the failure of finite first-cohomology vanishing.

## 6. Relation to WP60J and WP60I

The three statements are compatible and locate the transition sharply:

1. **WP60J, residual level:**
   `H^1(K(E[2])_2/Q,E[2])=0`;
   formal BSS II Hypotheses 3.2 and 3.3 hold for `E[2]`.
2. **WP60K, mod-4 level:**
   `H^1(K(E[4])_4/Q,E[4]) != 0`;
   formal BSS II Hypothesis 3.2(iii) fails for `E[4]`.
3. **WP60I, infinite tower:**
   the BSS III infinite `(H3)` condition fails with residual coefficients on the full `2`-power division field.

Therefore the standard finite-level BSS hypothesis cannot be restored simply by iterating the successful WP60J residual verification through the `2`-power tower.

Record

`BSS_LITERAL_P2_SELECTED_FINITE_HYP32III_FAILS_AT_E4`

and

`R5_BSS_STANDARD_FINITE_HYPOTHESIS_ROUTE_BLOCKED_ALREADY_AT_MOD4`.

## 7. Consequence for the BSS Fitting-control route

Protected MATHFORGE WP60F records that BSS II Theorems 5.20 and 5.2 use Hypothesis 3.2 in the Kolyvagin-system/core-vertex control chain, and that the integral inverse-limit construction proceeds through finite coefficient quotients.

WP60K therefore rules out a reopening strategy of the form:

> verify the existing finite BSS Hypothesis 3.2 unchanged for every `E[2^m]`, then replay the standard control theorem at literal `p=2`.

That strategy fails already at `m=2`.

A valid BSS-derived reopening must instead prove a theorem that weakens, replaces, or bypasses the finite cohomology-vanishing requirement. It must also address any independent literal-`2` core-vertex/connectivity obligation actually used by the replacement theorem.

## 8. Claim firewall

WP60K does not establish:

- impossibility of every literal-`2` Euler-system, Kolyvagin-system, determinant, or Fitting argument;
- literal-`2` BSS Theorem 5.2, 5.20, 5.25, or Corollary 6.15;
- the WP60H three-term-relation exclusion or graph connectivity;
- R5-LIFT or R5-PRIM;
- D2d or `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.

It establishes only an exact applicability obstruction for the unchanged standard finite BSS Hypothesis 3.2 at coefficient level `E[4]` on the selected lane.
