# WP60T theorem — selected literal-`p=2` replay of BSS II Theorem 6.12 and Corollary 6.15

## 1. Scope and protected inputs

Let `E/Q` be a selected `BSD-R2-A1` elliptic curve. Put

`T := T_2(E)`

and for every `m>=1`

`M_m := 2^m`, `R_m := Z/2^m`, `A_m := T/M_m T = E[2^m]`.

The operation consumes the following protected interfaces.

1. WP12 gives

   `im(rho_bar_{E,2}) = GL_2(F_2) ~= S_3`.

2. WP60I proves the selected formal BSS H2 condition and proves that the formal infinite BSS H3 condition fails. The H3 failure remains in force.

3. WP60R proves, at every finite coefficient level, the selected literal-`2` replacements of BSS II Theorems 5.20 and 5.2. In particular it supplies the exact level-`m` auxiliary-prime set, positive-density literal-`2` localization on that set, connected core graphs, finite core-vertex freeness, and Theorem 5.2(ii),(iii) Fitting control.

4. WP60S protects the inverse-limit Theorem 5.25 replacement. WP60T does not need to convert that result into an Iwasawa height-one statement.

5. Protected MATHFORGE provider head

   `095b8eec0e7fe29d7e831661dfe199ec43fa0458`

   admits the exact source dependency surface of BSS II §6 at literal `2`, including the selected derivative-prime-set compatibility with WP60R and the availability of an integral Kato Euler-system input without height-one-`(2)` promotion.

The proof below establishes only the selected finite BSS derivative/Fitting application.

## 2. The selected Euler-system tower

Let `S` contain the archimedean place, `2`, and every prime at which `T` is ramified.

For every prime `q notin S`, let `Q(q)` be the BSS field: the maximal `2`-extension of `Q` inside the ray class field of finite modulus `q`. Let `Q_infty/Q` be the cyclotomic `Z_2`-extension and define

`Kcal := Q_infty * (compositum over q notin S of Q(q))`.

Each `Q(q)/Q` is abelian of `2`-power degree, and `Q_infty/Q` is abelian pro-`2`; hence `Kcal/Q` is abelian pro-`2`.

For `Q`, the ray class field of finite modulus `q` is contained in the maximal real subfield of the `q`-th cyclotomic field: the finite ray class group is the cyclotomic residue group modulo the image of the global units `+-1`. Thus every `Q(q)` is totally real. The cyclotomic `Z_2`-extension is also totally real. Therefore the unique infinite place of `Q` splits completely in `Kcal`, as required in BSS §6.1.

Protected MATHFORGE admits the integral Kato Euler-system classes at literal `2`. Restricting/corestricting those classes to the finite real abelian subextensions of `Kcal` preserves the Euler-system norm relations. Hence the selected tower supports the rank-one Euler-system input used below. No height-one-`(2)` main-conjecture divisibility is used in this construction.

## 3. Hypothesis 6.1

### Theorem `BSD-A1-WP60T-HYP61-001`

For `T=T_2(E)` and the selected tower `Kcal/Q`, BSS Hypothesis 6.1 holds.

### Proof

Let `F/Q` be any finite field in `Kcal`. Then `F/Q` is an abelian `2`-extension.

Set

`L := Q(E[2])`.

Protected WP12 gives

`Gal(L/Q) ~= S_3`.

Since `F/Q` is abelian of `2`-power degree, the intersection `L cap F` corresponds to an abelian `2`-group quotient of `S_3`. The only possibilities are the trivial quotient and the quotient `S_3 -> C_2`. Therefore

`Gal(LF/F)`

is respectively `S_3` or `A_3`.

The natural two-dimensional `F_2` representation of `S_3 ~= GL_2(F_2)` has no nonzero `S_3`-fixed vector. Its restriction to `A_3 ~= C_3` also has no nonzero fixed vector: an element of order three has minimal polynomial `x^2+x+1` on `F_2^2`. Hence

`E[2](F)=0`.

It follows that `T^{G_F}=0`. Indeed, a nonzero invariant vector of the free `Z_2`-module `T` can be divided by its maximal common power of `2` to give a primitive invariant vector, whose reduction modulo `2` would give a nonzero element of `E[2](F)`.

Thus Hypothesis 6.1(ii) holds.

Now use the exact sequence

`0 -> T --2--> T -> E[2] -> 0`

over `O_{F,S(F)}`. Since `H^0(F,E[2])=0`, the connecting segment of the long exact cohomology sequence shows that multiplication by `2` on

`H^1(O_{F,S(F)},T)`

is injective. This global cohomology group is a finitely generated `Z_2`-module, so it is `Z_2`-torsion-free and hence `Z_2`-free.

BSS Remark 6.2 identifies this `Z_2`-freeness with the reflexivity required by Hypothesis 6.1(i) in the present coefficient setting.

Since `F` was arbitrary, both clauses of Hypothesis 6.1 hold throughout `Kcal`. QED.

Record

`BSS_LITERAL_P2_SELECTED_HYPOTHESIS_6_1_AVAILABLE`.

## 4. Hypothesis 6.7

### Theorem `BSD-A1-WP60T-HYP67-002`

The selected tower `Kcal/Q` satisfies BSS Hypothesis 6.7.

### Proof

By construction, `Kcal` contains `Q(q)` for every prime `q notin S`.

It also contains the cyclotomic `Z_2`-extension `Q_infty/Q`. No finite prime of `Q` splits completely in this extension. The prime `2` ramifies. For an odd prime `ell`, complete splitting in every finite real cyclotomic `2`-power layer would force

`ell = +-1 mod 2^n`

for arbitrarily large `n`, which is impossible for a fixed positive prime `ell`.

Thus `Q_infty` is a `Z_2`-extension in which no finite place splits completely. These are exactly the two requirements of Hypothesis 6.7. QED.

Record

`BSS_LITERAL_P2_SELECTED_HYPOTHESIS_6_7_AVAILABLE`.

## 5. Hypothesis 6.11

Fix `m>=1`. Let `P_m^der` be the BSS §6.3 derivative-prime set for `M=2^m` in the selected specialization.

### Theorem `BSD-A1-WP60T-HYP611-003`

For every `q in P_m^der` and every `k>=0`,

`Fr_q^(2^k)-1`

is injective on `T`. Hence BSS Hypothesis 6.11 holds at every selected finite level.

### Proof

Every `q in P_m^der` lies outside `S`, so `E` has good reduction at `q` and `q != 2`.

Suppose `Fr_q^(2^k)-1` were not injective on `T`. After tensoring with `Q_2`, some eigenvalue `alpha` of Frobenius on `V_2(E)` would satisfy

`alpha^(2^k)=1`.

Thus `alpha` would be a root of unity, so every complex embedding would have absolute value one.

At a good prime, the Frobenius eigenvalues of an elliptic curve have Weil absolute value `sqrt(q)` for arithmetic Frobenius, or `q^(-1/2)` under the reciprocal convention. Since `q>1`, neither can have absolute value one. This is a contradiction.

Therefore `Fr_q^(2^k)-1` is injective on `V_2(E)`, hence on the lattice `T`. QED.

Record

`BSS_LITERAL_P2_SELECTED_HYPOTHESIS_6_11_AVAILABLE`.

## 6. Compatibility of derivative primes with WP60R

For `K=Q`, the BSS field `K(1)` is `Q` because `Q` has class number one. In §6.3 choose the auxiliary field

`E_aux = F = K = Q`.

Then

`Acal = A_F = A_m`.

BSS §3.1.2 defines

`K_M = Q(mu_M,(Z^x)^(1/M)) Q(1)`

and its auxiliary-prime set by a Frobenius conjugacy class in

`Gal(Q(A_m) K_M/Q)`.

BSS §6.3 defines the derivative set by splitting in the same `K_M` and the rank-one quotient

`A_m/(Fr_q-1)A_m ~= R_m`,

and explicitly states that the §6.3 set contains the §3.1.2 set whenever Hypothesis 3.2(ii) holds for the relevant module.

Protected WP60R retains this selected rank-one quotient interface at every finite level and proves positive-density pairwise and finite-family localization in its exact level-`m` §3.1.2 set.

BSS Remark 6.16 allows the Stark/Kolyvagin theory used after differentiation to be run on a positive-density smaller subset of the derivative-prime set, provided the required Chebotarev localization choices remain available. Therefore we choose exactly the protected WP60R level-`m` set.

### Proposition `BSD-A1-WP60T-PRIME-COMPAT-004`

At every selected finite level, the exact WP60R auxiliary-prime set is an admissible positive-density derivative-prime set for the selected BSS §6 construction and subsequent Theorem 5.2 control.

Record

`BSS_LITERAL_P2_SELECTED_DERIVATIVE_PRIME_SET_COMPATIBLE_WITH_WP60R`.

No new small-prime localization theorem is asserted here; the literal-`2` localization theorem is WP60R.

## 7. Theorem 6.12 and Corollary 6.13

Protected MATHFORGE records the source dependency exactly:

- operative BSS §6 is formulated for an arbitrary prime `p`;
- Theorem 6.12 assumes Hypotheses 6.1, 6.7 and 6.11;
- §6.5 states that throughout its proof those three hypotheses are assumed;
- in rank one, the citation to Mazur–Rubin Theorem 3.2.4 supplies the proof method and does not add an unstated odd-prime running hypothesis.

The selected BSD lane has rank one. Sections 3–5 above prove all three operative hypotheses at literal `2`, and §6 identifies an admissible derivative-prime set.

Therefore the BSS rank-one derivative construction applies for every `M=2^m`. For every admitted rank-one Euler system `c`, its derivative family satisfies the BSS finite-singular relation and defines

`kappa_m(c) in KS_1(A_m,Fcan)`.

### Theorem `BSD-A1-WP60T-BSS-612-005`

For every `m>=1`, the selected literal-`2` specialization of BSS II Theorem 6.12 holds for `T_2(E)` and `A_m=E[2^m]` on the selected tower and exact WP60R prime set.

Record

`BSS_LITERAL_P2_SELECTED_THEOREM_6_12_REPLAYED`.

The corresponding canonical rank-one derivative map of BSS Corollary 6.13 is therefore available at each selected finite level.

Record

`BSS_LITERAL_P2_SELECTED_COROLLARY_6_13_DERIVATIVE_AVAILABLE`.

This conclusion does not use, imply, or repair infinite BSS H3.

## 8. Corollary 6.15 replay

BSS Corollary 6.15 is printed with `p>3`. The protected WP60T provider audit records that its proof has no independent small-prime mechanism: it follows directly from BSS Theorem 5.2(ii),(iii), together with

`kappa(c)_1 = c_F`.

Protected WP60R has already proved the selected literal-`2` replacements of Theorem 5.2(ii),(iii) on the exact prime set chosen in §6 above.

Let `c` be an admitted rank-one Euler system, let `kappa_m(c)` be its selected derivative, and let `n` be a square-free product of selected level-`m` auxiliary primes. Applying protected WP60R Theorem 5.2 to this Kolyvagin system gives

`im(kappa_m(c)_n) subset Fitt^0_{R_m}(H^1_{Fcan(n)^*}(Q,A_m^*(1))^*)`.

For `n=1`, the derivative construction has

`kappa_m(c)_1 = c_Q mod 2^m`,

so

`im(c_Q mod 2^m) subset Fitt^0_{R_m}(H^1_{Fcan^*}(Q,A_m^*(1))^*)`.

For every `i>=0`, the replayed higher-Fitting conclusion gives

`I_i(kappa_m(c)) subset Fitt^i_{R_m}(H^1_{Fcan^*}(Q,A_m^*(1))^*)`.

### Theorem `BSD-A1-WP60T-BSS-615-006`

For every selected finite coefficient level `R_m=Z/2^m`, the inclusion conclusions of BSS II Corollary 6.15 hold for the selected literal-`2` derivative `kappa_m(c)`, with the source's `p>3` Fitting-control dependency replaced by protected WP60R.

Record

`BSS_LITERAL_P2_SELECTED_COROLLARY_6_15_REPLAYED`.

The theorem asserts containments for each Euler system. It does not assert that the Kato-derived Kolyvagin system is a basis, and therefore does not promote the equality/primitivity conclusions that require a basis.

## 9. Kato specialization and the remaining arithmetic boundary

Protected MATHFORGE admits Kato's integral literal-`2` Euler-system generators as an Euler-system input. Applying the preceding theorem to those classes gives the selected finite-level Kato derivative/Fitting containments.

This is not the same statement as the cyclotomic Iwasawa height-one divisibility

`MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`.

Protected WP60A-A1 identifies that latter statement over `Lambda_(2)` with the still-missing one-sided Fitting inequality required for determinant membership. Finite containments modulo `2^m`, without a separate height-one control theorem and without primitivity, do not establish it.

Thus WP60T retires only the BSS application frontier and returns the campaign directly to the pre-existing height-one `(2)` arithmetic frontier.

## 10. Exact disposition

Retire

`MISSING_LITERAL_P2_BSS_THEOREM_6_12_COROLLARY_6_15_APPLICATION_REPLAY_WITHOUT_INFINITE_H3`

with candidate disposition

`CLOSED`.

The next exact mathematical frontier is

`MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`.

The independent subsequent primitivity boundary remains

`MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.

## 11. Claim firewall

WP60T does not establish:

- formal higher-level BSS Hypothesis 3.2(iii);
- full BSS Hypothesis 4.7 or clause (iii);
- infinite BSS H3;
- Kato height-one-`(2)` Fitting divisibility;
- Kato/Kolyvagin primitivity at `(2)`;
- `R5-LIFT`;
- `R5-PRIM`;
- D2d;
- `BSD-R2-A1`;
- novelty or priority;
- MATHCERT certification.
