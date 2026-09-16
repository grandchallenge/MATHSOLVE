# BSD R5-RECIP — literal-`p=2` local Kummer / logarithm / dual-exponential lattice

## 1. Protected setup

Let `E/Q_2` be the selected local curve. Protected inputs give good ordinary reduction at `2`, `a_2 in {+1,-1}`, `q_2=#E(F_2)=3-a_2 in {2,4}`, a minimal Néron differential `omega_E`, and WP60B:

`log_{omega_E}(E_1(Q_2)) subset 4 Z_2`.

For `r>=1`, let `E_r(Q_2)` be the formal subgroup with parameter in `2^r Z_2`. Then

`E_1(Q_2)/E_2(Q_2) ~= 2Z_2/4Z_2 ~= F_2`.

Let `T_loc=E(Q_2)[2^infinity]` and `#T_loc=2^t_2`.

## 2. Deep logarithm

### Lemma `BSD-R5-RECIP-LOCAL-DEEPLOG-001`

`log_{omega_E}:E_2(Q_2)->4Z_2` is an isomorphism.

### Proof

For the formal parameter `t=-x/y`, write

`log(t)=t+sum_{n>=2} b_n t^n/n`, `b_n in Z_2`.

If `t in 4Z_2`, then `ord_2(t^n/n)>=2n-ord_2(n)>=3` for `n>=2`. Hence `log(t)=t mod 8Z_2`, and the derivative is a 2-adic unit. Complete-ball inverse-function iteration gives a unique preimage in `4Z_2` for every element of `4Z_2`. QED.

## 3. The shallow anomaly is exactly one formal 2-torsion point

### Theorem `BSD-R5-RECIP-LOCAL-FORMAL-TORS-002`

`ker(log:E_1(Q_2)->Q_2)=E_1(Q_2)[2^infinity]` has order exactly `2`.

### Proof

WP60B and `DEEPLOG-001` give

`log(E_1) subset 4Z_2 = log(E_2)`.

Since `E_2 subset E_1`, equality holds. For every `P in E_1`, choose the unique `Q in E_2` with `log(Q)=log(P)`. Then `P-Q` is in the kernel. The kernel meets `E_2` trivially, so

`ker(log) ~= E_1/E_2`,

which has order two. A finite subgroup of the formal group is torsion, and logarithm kills torsion. QED.

### Corollary `BSD-R5-RECIP-LOCAL-TEXP-003`

`t_2>=1`. The reduction map on `T_loc` has kernel of order `2`, hence image of order `2^(t_2-1)` and

`2^(t_2-1) | q_2`.

## 4. Completed free local lattice

Put

`G_2 := (E(Q_2)/T_loc) completed at 2`

and let `H_2` be the image of `E_1(Q_2)/E_1(Q_2)[2^infinity]` in `G_2`. Both are free rank-one `Z_2`-modules.

### Lemma `BSD-R5-RECIP-LOCAL-INDEX-004`

`[G_2:H_2]=q_2/2^(t_2-1)`.

### Proof

The reduction sequence is

`0 -> E_1(Q_2) -> E(Q_2) -> E(F_2) -> 0`.

After quotienting by local torsion, the finite quotient has order `q_2/#red(T_loc)=q_2/2^(t_2-1)`. QED.

### Theorem `BSD-R5-RECIP-LOCAL-LOGLATTICE-005`

The logarithm descends injectively to `G_2` and

`log_{omega_E}(G_2)=(2^(t_2+1)/q_2) Z_2`.

### Proof

If `P in E(Q_2)` has `log(P)=0`, then `[q_2]P in E_1` and has zero logarithm, so `[q_2]P` is the formal torsion point from `FORMAL-TORS-002`. Hence a nonzero multiple of `P` is zero and `P` is torsion. Thus the induced map on `G_2` is injective.

On `H_2`, the image is `4Z_2`. Enlarging a rank-one domain lattice by index `d=q_2/2^(t_2-1)` enlarges its image by the same index, so

`log(G_2)=(4/d)Z_2=(2^(t_2+1)/q_2)Z_2`. QED.

## 5. Dual exponential

Local Tate duality for the Weil-pairing self-dual Tate module identifies the singular quotient with the `Z_2`-dual of the free Kummer lattice. Under the basis dual to `omega_E`, Bloch–Kato `exp^*` is paired with the logarithm.

### Theorem `BSD-R5-RECIP-LOCAL-DUALEXP-006`

`exp^*_{omega_E}(H^1_s(Q_2,T_2E)) = (q_2/2^(t_2+1)) Z_2`.

Thus Kim Lemma 3.3's good-reduction lattice expression extends to the selected literal-2 lane when the forced formal 2-torsion is retained.

## 6. Torsion coefficients

Let `I=(2^m)` be any nonzero coefficient ideal used by the protected finite derivative system and put `R=Z_2/I`. Propagation of the finite local condition gives

`0 -> H^1(Q_2,T)/(I H^1(Q_2,T)+H^1_f(Q_2,T))
   -> H^1(Q_2,T/IT)/H^1_f(Q_2,T/IT)
   -> H^2(Q_2,T)[I] -> 0`.

The left term is free rank one over `R`, by `DUALEXP-006`. The ring `R=Z/2^m` is a finite principal Frobenius ring, hence self-injective; therefore a free rank-one `R`-submodule is injective and the displayed sequence splits as `R`-modules. This is the algebraic reason behind the splitting used in Kim Proposition 3.10; it does not rely on `2` being odd.

Choose a splitting and project onto the free summand. Composing with naive reduction of integral `exp^*` defines

`exp^*_{omega_E,I}:H^1_s(Q_2,T/IT)
 -> (q_2/2^(t_2+1))Z_2 / I(q_2/2^(t_2+1))Z_2`.

For a class that is the reduction of an integral cohomology class, its projected value is the naive reduction of integral `exp^*`; hence it is independent of the chosen splitting. Protected WP60T Kato derivatives have exactly this integral-lift property.

### Theorem `BSD-R5-RECIP-LOCAL-TORSIONCOEFF-007`

For every protected finite derivative coefficient ideal `I`, the preceding map supplies the selected literal-2 torsion-coefficient dual exponential required by R5-RECIP, and it is canonical on the Kato-derived classes consumed downstream.

After a lattice isomorphism

`xi_I:(q_2/2^(t_2+1))Z_2/I(...) ~= Z_2/I`,

the selected finite Kato derivative has a well-defined normalized local regulator.

## 7. Disposition

`R5-RECIP-LOCAL` is established. The extra factor of two in the shallow formal logarithm is exactly compensated by the forced formal rational 2-torsion when the free local Kummer lattice is computed.

No modular-symbol, Kurihara nonvanishing, R5-RES, R5-PRIM, BSD, or certification claim is made here.