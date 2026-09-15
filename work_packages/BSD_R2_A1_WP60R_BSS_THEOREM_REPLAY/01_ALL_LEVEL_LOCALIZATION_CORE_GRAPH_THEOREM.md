# WP60R theorem I — all-level literal-2 auxiliary-prime localization and core graphs

## 1. Protected setup

Fix a selected `BSD-R2-A1` curve. For `m>=1`, put

`R_m := Z/2^m`,

`A_m := E[2^m]`.

At `m=1`, protected WP60J, WP60G, WP60H, WP60N and WP60Q provide the selected literal-`2` residual localization and core-graph interfaces.

For `m>=2`, protected WP60M defines the exact BSS auxiliary field

`F_m := K(A_m)_(2^m)`

and proves:

1. the global restriction kernel
   `H^1(Q,A_m) -> H^1(F_m,A_m)`
   has order two;
2. its unique nonzero class `z_m` violates the fixed canonical local condition at the protected odd-depth multiplicative prime `ell`;
3. every BSS canonical auxiliary modification retains that fixed local condition at `ell` on both the primal and dual side;
4. therefore restriction to `F_m` is injective on every actual modified primal and dual Selmer group;
5. BSS Lemma 3.10 coefficient reduction is available on free selected modified Selmer modules.

Protected MATHFORGE WP60R at

`grandchallenge/MATHFORGE@8c9b25fdd7dd63428a10f7d4439f5033ea890964`

also supplies the selected literal-`2` cartesian core-vertex freeness interface.

## 2. Common-span restriction injectivity

The original BSS Lemma 3.9 can be applied to a collection of classes only after their restrictions to the BSS auxiliary field are known to retain the required linear information. Formal Hypothesis 3.2(iii) is false for `m>=2`, so WP60R proves only the exact selected substitute.

### Lemma `BSD-A1-WP60R-COMMON-SPAN-RES-001`

Let `C` be any finite collection of classes in primal or self-dually identified dual `2`-torsion subspaces of selected BSS canonical modified Selmer groups for `A_m`. Assume every class in `C` satisfies the fixed canonical local condition at `ell`. Then restriction to `F_m` is injective on the `F_2`-span `<C>`.

### Proof

Protected WP60M proves that the kernel of

`H^1(Q,A_m) -> H^1(F_m,A_m)`

is `{0,z_m}` and that `z_m` violates the fixed canonical local condition at `ell`.

The canonical local condition at `ell` is an `F_2`-linear condition on the `2`-torsion classes. Therefore every element of `<C>` satisfies it. Consequently `z_m` does not belong to `<C>`, so the intersection of `<C>` with the global restriction kernel is zero. QED.

This lemma does not assert full Hypothesis 3.2(iii). It applies only to the selected classes satisfying the fixed local condition.

### Lemma `BSD-A1-WP60R-QUOTIENT-CHAR-001B`

On the same span `<C>`, the BSS quotient-character map

`j_m := f_m o Res_m`

is injective. For every nonzero class in `<C>`, `j_m(c)` is a nonzero homomorphism with image in the unique order-two subgroup of

`A_m/(tau-1)A_m ~= R_m`.

### Proof

Let `0 != c in <C>`. By Lemma `COMMON-SPAN-RES-001`, `Res_m(c)` is nonzero. Since `c` is annihilated by `2` and `F_m` contains `Q(A_m)`, its restricted cocycle is a homomorphism with image in

`A_m[2] ~= E[2]`.

The restricted class is invariant under the ambient Galois action, so its image is a nonzero `G_Q`-stable `F_2`-subspace of `A_m[2]`. Protected WP60J gives irreducibility of the selected residual module. Hence the image is all of `A_m[2]`.

Suppose `f_m(Res_m(c))=0`. Then the image of `Res_m(c)` is contained in `(tau-1)A_m`. But Hypothesis 3.2(ii), protected on the selected full-image lane, gives

`A_m/(tau-1)A_m ~= R_m`.

Since `A_m` is free of rank two and the quotient is free of rank one, `(tau-1)A_m` is a free rank-one `R_m`-module. Its `2`-torsion therefore has `F_2`-dimension one, whereas `A_m[2]` has dimension two. Thus `A_m[2]` cannot be contained in `(tau-1)A_m`, a contradiction.

Therefore `j_m(c)` is nonzero for every nonzero `c` in `<C>`, which proves injectivity on the `F_2`-span. Since `2c=0`, also `2j_m(c)=0`; under the rank-one quotient identification its image lies in `R_m[2] ~= F_2`. Nonzero then means surjective onto that order-two subgroup. QED.

This is the additional quotient step used implicitly in the original BSS Lemma 3.9 after restriction injectivity. It is recorded separately here because full Hypothesis 3.2(iii) is unavailable.

## 3. Level-m affine-fiber localization

Cartesian coefficient reduction identifies every residual modified Selmer class with a class in the `2`-torsion of the corresponding `A_m` modified Selmer group. Lemmas `COMMON-SPAN-RES-001` and `QUOTIENT-CHAR-001B` show that the finite span of any classes used below survives both restriction to `F_m` and projection to the BSS rank-one quotient.

Thus every nonzero lifted class gives a nonzero character

`G_{F_m} -> R_m[2] ~= F_2`

and a well-defined affine constant in the same order-two quotient. The finite-level Weil pairing identifies `A_m` with `A_m^*(1)` compatibly with restriction, `tau`, the quotient by `(tau-1)`, and cocycle evaluation. Hence the naturality argument of protected WP60G applies to these lifted `2`-torsion characters exactly as it does residually.

Chebotarev is applied over the full field `F_m`. Therefore the resulting primes lie in the exact BSS level-`m` auxiliary-prime set rather than merely the residual level-1 set.

### Theorem `BSD-A1-WP60R-LEVELM-PAIRWISE-002`

For every `m>=1`, every selected BSS canonical modification, every nonzero residual primal class `c`, and every nonzero residual dual class `d`, there is a positive-density set of level-`m` BSS auxiliary primes `q` such that

`loc_q(c) != 0`,

`loc_q(d) != 0`.

The primes may be chosen outside any prescribed finite set.

### Proof

For `m=1`, this is protected WP60G.

For `m>=2`, lift `c,d` by cartesian coefficient reduction to `2`-torsion classes in the corresponding `A_m` modified Selmer groups. Their `F_2` span satisfies the fixed local condition at `ell`. By Lemma `QUOTIENT-CHAR-001B`, both classes define nonzero `F_2` quotient characters and the combined span is detected injectively by the BSS quotient-character map.

After finite-level Weil self-duality identifies the primal and dual targets, the two affine bad fibers are exactly in the situation of the protected WP60G two-fiber theorem. If the characters differ, their fibers do not cover; if they agree, injectivity of the combined quotient-character map identifies the corresponding classes and naturality identifies their affine constants, so the fibers coincide rather than complement each other. In both cases their union is proper.

The original BSS Chebotarev construction over `F_m` then supplies a positive-density set of exact level-`m` auxiliary primes outside both bad fibers. QED.

Record

`BSS_LITERAL_P2_SELECTED_ALL_LEVEL_PAIRWISE_LOCALIZATION_AVAILABLE`.

For any finite collection of lifted classes, Lemma `QUOTIENT-CHAR-001B` supplies the injective linear character map and cocycle evaluation supplies the linear affine-constant map required by protected WP60H. Hence its odd-relation cover criterion also replays over `F_m`. WP60R uses only the four-class instances already required by the protected WP60N exchange proof.

## 4. Iterated injective primal localization

### Lemma `BSD-A1-WP60R-INJECTIVE-FAMILY-003`

Let `V` be a finite-dimensional residual primal modified Selmer space and let `0 != d` be a residual dual modified Selmer class. Then there are distinct level-`m` BSS auxiliary primes

`q_1,...,q_s`

outside any prescribed finite set such that:

1. every localization map `V -> H^1_f(Q_{q_i},E[2])` is nonzero;
2. `loc_{q_i}(d) != 0` for every `i`;
3. the combined map
   `V -> direct_sum_i H^1_f(Q_{q_i},E[2])`
   is injective.

One may take `s <= dim_F2 V`.

### Proof

Start with `K_0:=V`. If `K_j=0`, stop. Otherwise choose `0 != c_j in K_j`. Apply Theorem `LEVELM-PAIRWISE-002` to `c_j,d`, avoiding all previously selected primes. Choose `q_{j+1}` with both localizations nonzero and put

`K_{j+1}:=K_j intersect ker(loc_{q_{j+1}})`.

Because `loc_{q_{j+1}}(c_j) != 0`, `K_{j+1}` is a proper subspace of `K_j`. Hence the process terminates after at most `dim V` steps. At termination the intersection of the localization kernels is zero, which is the asserted injectivity. Each individual primal map is nonzero because it detects `c_j`, and each chosen prime detects `d`. QED.

This is the exact replacement for the multi-class Lemma 3.9 call in the induction step of BSS Theorem 5.20.

## 5. Iterated dual killing

### Lemma `BSD-A1-WP60R-DUAL-KILL-004`

Let `D` be a finite-dimensional residual dual modified Selmer space. Starting from any selected modification, one can enlarge the auxiliary ideal by finitely many level-`m` BSS primes so that the resulting residual dual modified Selmer group is zero.

If a fixed nonzero residual primal class `c` must localize nontrivially at every newly chosen prime, the same conclusion holds while imposing `loc_q(c)!=0` at each step.

### Proof

If `D=0`, there is nothing to prove. Otherwise choose `0 != d in D`.

Without a primal constraint, lift `d` to the corresponding `2`-torsion full-coefficient class. Lemma `QUOTIENT-CHAR-001B` makes its BSS quotient character nonzero, so its single affine bad fiber is proper. The BSS Chebotarev construction over `F_m` therefore supplies an exact level-`m` auxiliary prime with nonzero localization of `d`.

With a fixed primal constraint `c`, apply Theorem `LEVELM-PAIRWISE-002` to `c,d`.

In either case, the BSS global-duality dimension transition used in Proposition 5.7 lowers the residual dual dimension by one after imposing the corresponding auxiliary condition. Iterate. Finite dimensionality forces termination. QED.

## 6. Level-m core graph

Protected WP60N proves the characteristic-two core-graph theorem from:

- residual self-duality;
- residual restriction injectivity for the classes used;
- cartesianness;
- core rank one;
- residual coisotropy;
- the WP60G pairwise localization theorem;
- the WP60H four-class odd-relation criterion.

For the selected canonical structure, the first five structural inputs are protected by WP60J and MATHFORGE WP60O/WP60P. Sections 2–3 above supply the quotient-character and localization inputs with primes in the exact level-`m` BSS auxiliary-prime set. Therefore the WP60N exchange proof replays at every finite coefficient level.

### Theorem `BSD-A1-WP60R-ALL-LEVEL-CORE-GRAPH-005`

For every `m>=1`, the selected BSS core graph associated to `A_m=E[2^m]`, with its exact level-`m` auxiliary-prime set, is connected.

Record

`BSS_LITERAL_P2_SELECTED_ALL_FINITE_LEVEL_CORE_GRAPHS_CONNECTED`.

## 7. Finite-level Hypothesis 4.2 replacement

Choose any finite coefficient level and apply Lemma `DUAL-KILL-004` to the residual dual canonical Selmer space. At the resulting auxiliary modification, the residual dual group is zero.

Protected cartesian coefficient reduction identifies that residual group with the `2`-torsion of the full finite-level dual modified Selmer group. A nonzero finite `2`-primary module has nonzero `2`-torsion. Hence the full dual modified Selmer group is also zero.

Protected MATHFORGE WP60R then gives freeness of the primal modified Selmer group over `R_m`, of rank equal to the modified core rank.

### Theorem `BSD-A1-WP60R-HYP42-006`

At every finite selected coefficient level `R_m=Z/2^m`, the exact existence-and-freeness conclusion required from BSS Hypothesis 4.2 is available on the canonical lane.

Record

`BSS_LITERAL_P2_SELECTED_FINITE_LEVEL_HYPOTHESIS_4_2_AVAILABLE`.

## 8. Claim firewall

This theorem does not make formal higher-level BSS Hypothesis 3.2(iii) true. It does not repair the protected infinite H3 failure. It does not yet assert BSS Theorem 5.20, 5.2, 5.25, Corollary 6.15, R5-LIFT, R5-PRIM, D2d, `BSD-R2-A1`, novelty, priority, or MATHCERT certification.
