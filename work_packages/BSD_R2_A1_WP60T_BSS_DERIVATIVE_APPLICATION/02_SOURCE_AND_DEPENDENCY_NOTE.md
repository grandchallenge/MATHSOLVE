# WP60T source and dependency note

## Protected provider authority

WP60T consumes the protected provider record

`grandchallenge/MATHFORGE@095b8eec0e7fe29d7e831661dfe199ec43fa0458`

at

`sources/BSD-001/BSS_P2_DERIVATIVE_WP60T_SOURCE_AUDIT.md`.

That record was admitted through MATHFORGE #217, PRs #218 and #219, exact-head Adversary/Referee passes, green Forge/GCL checks, and signed protected readback.

The provider record admits only the source/dependency surface. MATHSOLVE remains responsible for the mathematical specialization.

## Primary BSS source

David Burns, Ryotaro Sakamoto, Takamichi Sano, *On the theory of higher rank Euler, Kolyvagin and Stark systems, II: the general theory*, arXiv:1805.08448v1.

The exact source points consumed by WP60T are:

1. §3.1.2:
   - `K_M = K(mu_M,(O_K^x)^(1/M))K(1)`;
   - `K(A)_M = K(A)K_M`;
   - the auxiliary-prime set is a Frobenius conjugacy class in `Gal(K(A)_M/K)`;
   - every such prime splits completely in `K_M` and has the rank-one quotient required by Hypothesis 3.2(ii).
2. §6.1:
   - `p` is introduced as an arbitrary prime;
   - all infinite places must split completely in the chosen abelian pro-`p` extension;
   - Hypothesis 6.1 requires reflexive global `H^1` and vanishing `H^0` at every finite layer;
   - Remark 6.2 identifies reflexivity with freeness over the coefficient DVR in the present setting.
3. §6.2:
   - Hypothesis 6.7 requires every `K(q)` plus a `Z_p^d`-extension in which no finite place splits completely.
4. §6.3:
   - the derivative-prime set is defined by splitting in `K_M` and a rank-one Frobenius quotient for the induced module;
   - the source explicitly says this set contains the §3.1.2 set when Hypothesis 3.2(ii) holds for the induced module;
   - Hypothesis 6.11 requires `Fr_q^(p^k)-1` injective on `T` for every derivative prime and every `k>=0`.
5. §6.4:
   - Theorem 6.12 assumes 6.1, 6.7 and 6.11 and produces a Kolyvagin system;
   - Corollary 6.13 packages the derivative map;
   - Corollary 6.15 prints `p>3`, but its proof is a direct application of Theorem 5.2(ii),(iii) and `kappa(c)_1=c_F`;
   - Remark 6.16 permits use of a positive-density smaller derivative-prime set for the downstream Stark/Kolyvagin theory.
6. §6.5:
   - throughout the proof, the source assumes 6.1, 6.7 and 6.11;
   - in rank one it invokes the method of Mazur–Rubin Theorem 3.2.4 and states that this method applies in the BSS setting.

## Protected MATHSOLVE dependencies

### Residual representation

Protected WP12 supplies

`im(rho_bar_{E,2})=GL_2(F_2)~=S_3`.

WP60T uses this only to prove absence of residual invariants over finite abelian `2`-extensions and hence Hypothesis 6.1.

### H2/H3 determination

Protected WP60I records

`BSS_LITERAL_P2_SELECTED_H2_HOLDS_H3_FAILS`.

WP60T preserves the H3 failure. The operative derivative theorem does not assume H3.

### Finite literal-2 Kolyvagin/Fitting control

Protected WP60R supplies:

- the selected all-level restriction/localization replacement;
- the exact level-`m` BSS auxiliary-prime set;
- positive-density pairwise/family localization at literal `2`;
- dual killing;
- selected finite core-graph connectivity;
- finite Hypothesis 4.2 replacement;
- `BSS_LITERAL_P2_SELECTED_THEOREM_5_20_REPLAYED`;
- `BSS_LITERAL_P2_SELECTED_THEOREM_5_2_REPLAYED`.

This is the entire selected replacement of the `p>3` Fitting-control layer used in Corollary 6.15.

### Integral inverse limit

Protected WP60S supplies

`BSS_LITERAL_P2_SELECTED_THEOREM_5_25_REPLAYED`.

WP60T does not use this result to claim the cyclotomic Iwasawa height-one `(2)` inequality. The BSS finite application and the Iwasawa height-one statement remain separate.

## Protected Kato source status

Protected MATHFORGE WP17B distinguishes two facts:

1. Kato Theorem 12.6 supplies integral Euler-system classes at literal `2`;
2. the all-height-one main-conjecture/Fitting divisibility needed at the prime containing `2` is unavailable from Kato's cited theorem because its relevant clauses require `p != 2`.

WP60T consumes only fact 1.

## Dependency closure table

| Obligation | WP60T resolution |
| --- | --- |
| BSS 6.1(ii), `H^0(F,T)=0` | `S_3` residual image; every finite selected `F/Q` is abelian `2`, so the residual image over `F` contains `A_3`, which has no fixed vector |
| BSS 6.1(i), reflexive global `H^1` | residual invariants vanish; multiplication by `2` on global `H^1` is injective; finite generation gives `Z_2`-freeness; BSS Remark 6.2 gives reflexivity |
| BSS 6.7 | explicit real abelian pro-`2` tower containing every `Q(q)` and the cyclotomic `Z_2`-extension |
| BSS 6.11 | good-reduction Frobenius eigenvalues have Weil absolute value different from one; no `2^k`-power can have eigenvalue one |
| §6.3 prime-set compatibility | choose `E=F=K=Q`; derivative set contains the WP60R §3.1.2 set; Remark 6.16 permits the positive-density WP60R subset |
| Theorem 6.12 rank-one proof | protected provider records that §6.5 imports no additional odd-prime hypothesis beyond 6.1/6.7/6.11 |
| Corollary 6.15 `p>3` | source proof uses Theorem 5.2(ii),(iii); protected WP60R supplies the selected literal-`2` replacement |
| Kato input | protected integral Euler-system classes only; no height-one `(2)` promotion |

## Remaining boundary

After WP60T the BSS application uncertainty is no longer the active route boundary. The campaign returns directly to

`MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`.

The independent primitivity boundary remains

`MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.

Neither boundary is solved by the finite BSS derivative/Fitting replay.
