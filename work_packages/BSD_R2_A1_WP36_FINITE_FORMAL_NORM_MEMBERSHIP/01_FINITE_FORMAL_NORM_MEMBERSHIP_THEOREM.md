# WP36 theorem — exact finite norm-membership criterion for the WP31 twisted-reciprocity exponent

## 1. Protected setup

Let `E/Q` lie in the protected selected `BSD-R2-A1` class and let `P` be the protected saturated generator of the rank-one free quotient.

Protected WP28 defines

`F_2^norm := Ehat(2 Z_2)/N_2^form`

and the reduction-killed class

`z_form(P) in F_2^norm`.

Protected WP29 sets

`m_2 := ord_2(3-a_2) in {1,2}`

and defines `tau_form(P)` by

`ord(z_form(P)) = 2^{m_2-tau_form(P)}`.

Protected WP31 proves that the infinite formal quotient stabilizes in the single finite layer

`n=m_2`, 

and identifies `tau_form(P)` with the truncated valuation of a finite twisted-reciprocity exponent

`c_tw(P) mod 2^{m_2}`.

For `n=1,2`, let

`L_n/Q_2`

be the degree-`2^n` layer of the local cyclotomic `Z_2`-extension, let

`G_n := Gal(L_n/Q_2)`,

and define the formal norm image

`H_n := N_{L_n/Q_2}(Ehat(m_{L_n}))
       subset Ehat(2 Z_2)`.

Here the norm is the formal-group norm

`N_{L_n/Q_2}(R)
 := bigoplus_{sigma in G_n} sigma(R)`.

Protected WP31 gives

`F_{2,n}^norm
 := Ehat(2Z_2)/H_n
 ~= G_n/(1-alpha)G_n`.

For `n>=m_2`, the natural map

`F_2^norm -> F_{2,n}^norm`

is an isomorphism.

Protected MATHFORGE WP36 at

`92fcd8596e59aa8331b2450ea66c14786581806e`

admits Silverman IV.6.4 only on the deep subgroup `Ehat(4O_L)`. On that subgroup the formal logarithm is an exact Galois-equivariant group isomorphism and converts formal norms into additive traces.

## 2. Explicit first local cyclotomic layer

Let

`theta_1 := zeta_8 + zeta_8^(-1)`.

Then

`theta_1^2=2`,

so

`L_1=Q_2(theta_1)`

is the degree-2 local cyclotomic layer. The polynomial

`X^2-2`

is Eisenstein at `2`. Hence `theta_1` is a uniformizer and

`O_{L_1}=Z_2[theta_1]`.

### Lemma `BSD-A1-WP36-TRACE-L1-001`

One has

`Tr_{L_1/Q_2}(O_{L_1})=2 Z_2`.

### Proof

The conjugates of `theta_1` are `theta_1` and `-theta_1`. Thus

`Tr(1)=2`,

`Tr(theta_1)=0`.

Every integral element has the form

`a+b theta_1`, `a,b in Z_2`,

and therefore has trace `2a`. Hence the trace ideal is exactly `2Z_2`. QED.

## 3. Explicit second local cyclotomic layer

Let

`theta_2 := zeta_16 + zeta_16^(-1)`.

The standard cyclotomic identity gives

`theta_2^4 - 4 theta_2^2 + 2 = 0`.

The polynomial

`f_2(X)=X^4-4X^2+2`

is Eisenstein at `2`. Hence

`L_2=Q_2(theta_2)`

is the degree-4 local cyclotomic layer, `theta_2` is a uniformizer, and

`O_{L_2}=Z_2[theta_2]`.

### Lemma `BSD-A1-WP36-TRACE-L2-001`

One has

`Tr_{L_2/Q_2}(O_{L_2})=4 Z_2`.

### Proof

Write the monic minimal polynomial as

`X^4 + a_1 X^3 + a_2 X^2 + a_3 X + a_4`

with

`a_1=0`, `a_2=-4`, `a_3=0`, `a_4=2`.

Newton's identities give, for the power sums of the four conjugates,

`Tr(theta_2)=0`,

`Tr(theta_2^2)=8`,

`Tr(theta_2^3)=0`.

Also `Tr(1)=4`.

Since `O_{L_2}` has the `Z_2`-basis

`1, theta_2, theta_2^2, theta_2^3`,

every integral trace lies in `4Z_2`. Conversely `Tr(1)=4`, so `4` itself occurs. Therefore

`Tr(O_{L_2})=4Z_2`. QED.

## 4. Exact deep formal norm images

Protected MATHFORGE WP36 permits use of the formal logarithm on

`Ehat(4O_{L_n})`.

It gives a commutative equality

`log_E(N_{L_n/Q_2}(R))
 = Tr_{L_n/Q_2}(log_E(R))`

for every `R in Ehat(4O_{L_n})`.

Since

`log_E:Ehat(4O_{L_n}) -> 4O_{L_n}`

is onto, the logarithm of the entire deep norm image is exactly

`Tr_{L_n/Q_2}(4O_{L_n})`.

### Theorem `BSD-A1-WP36-DEEP-NORM-001`

One has exactly

`N_{L_1/Q_2}(Ehat(4O_{L_1}))
 = Ehat(8Z_2)`

and

`N_{L_2/Q_2}(Ehat(4O_{L_2}))
 = Ehat(16Z_2)`.

### Proof

For `n=1`, Lemma `TRACE-L1-001` gives

`Tr(4O_{L_1})=4*(2Z_2)=8Z_2`.

For `n=2`, Lemma `TRACE-L2-001` gives

`Tr(4O_{L_2})=4*(4Z_2)=16Z_2`.

Silverman's admitted logarithm isomorphism also applies on the base subgroups `Ehat(8Z_2)` and `Ehat(16Z_2)`. Taking inverse logarithmic images proves both equalities. QED.

Define

`D_1:=Ehat(8Z_2)`,

`D_2:=Ehat(16Z_2)`.

Then

`D_n subset H_n`.

## 5. The shallow source quotients are finite and tiny

The residue field of each `L_n` is `F_2` because the local cyclotomic layers are totally ramified.

The coordinate of the formal group identifies its underlying set `Ehat(m_{L_n})` with `m_{L_n}` and `Ehat(4O_{L_n})` with `4O_{L_n}`. This set-theoretic coordinate identification is enough to count the finite quotient; no shallow logarithm is used.

Because `L_n/Q_2` is totally ramified of degree `e_n=2^n`,

`v_{L_n}(2)=e_n`

and

`4O_{L_n}=m_{L_n}^{2e_n}`.

Hence

`#(Ehat(m_{L_n})/Ehat(4O_{L_n}))
 = #(m_{L_n}/m_{L_n}^{2e_n})
 = 2^{2e_n-1}`.

### Corollary `BSD-A1-WP36-SHALLOW-SIZE-001`

The finite source quotient has

`8`

classes for `n=1` and

`128`

classes for `n=2`.

### Proof

For `n=1`, `e_1=2`, so `2e_1-1=3`.

For `n=2`, `e_2=4`, so `2e_2-1=7`. QED.

## 6. The finite norm-image map

Because the formal norm is a group homomorphism and

`N(Ehat(4O_{L_n}))=D_n`,

it induces a finite homomorphism

`bar N_n:
 Ehat(m_{L_n})/Ehat(4O_{L_n})
 -> Ehat(2Z_2)/D_n`.

Define its finite image

`S_n:=im(bar N_n)`.

### Theorem `BSD-A1-WP36-FINITE-IMAGE-001`

For every `Q in Ehat(2Z_2)`,

`Q in H_n`

if and only if the residue class of `Q` modulo `D_n` belongs to `S_n`.

Moreover `S_n` is exactly computable by enumerating only

- `8` source classes when `n=1`;
- `128` source classes when `n=2`.

### Proof

By definition,

`H_n=N(Ehat(m_{L_n}))`.

Reduction modulo `D_n=N(Ehat(4O_{L_n}))` therefore gives precisely the image of the induced quotient map `bar N_n`. Thus

`H_n/D_n=S_n`.

Since `D_n subset H_n`, a base point belongs to `H_n` exactly when its residue modulo `D_n` belongs to `S_n`.

The number of domain classes is given by Corollary `SHALLOW-SIZE-001`, so exhaustive enumeration terminates after the stated finite number of classes. QED.

## 7. Exact arithmetic realization of the enumeration

The preceding theorem is not merely existential.

Fix a minimal integral Weierstrass equation of `E/Q_2`. Its formal group law

`F_E(X,Y) in Z_2[[X,Y]]`

and multiplication law `[2]_E(T)` have integral coefficients.

For `n=1` use the exact ring presentation

`O_{L_1}=Z_2[theta_1]/(theta_1^2-2)`.

For `n=2` use

`O_{L_2}=Z_2[theta_2]/(theta_2^4-4theta_2^2+2)`.

Choose one representative of each class in

`m_{L_n}/4O_{L_n}`.

For a representative `t`, compute

`N_F(t)
 := F_E(
      sigma_0(t),
      F_E(sigma_1(t),
      ...))`

with one term for each element of `G_n`, reducing after each formal-group operation modulo

- `8Z_2` for `n=1`;
- `16Z_2` for `n=2`.

Only finitely many coefficients of `F_E` contribute modulo these powers of `2`, so every operation is exact finite ring arithmetic.

For `n=1`, the nontrivial automorphism is

`theta_1 -> -theta_1`.

For `n=2`, a generator may be taken with

`theta_2 -> theta_2^3-3theta_2`;

its powers give the four Galois conjugates. All reductions are performed in the displayed integral quotient ring.

### Algorithm `BSD-A1-WP36-NORM-TABLE-001`

Input:

1. the integral Weierstrass coefficients of `E` at `2`;
2. `n in {1,2}`.

Output:

`S_n=H_n/D_n`.

Procedure:

1. construct the finite quotient ring representing `m_{L_n}/4O_{L_n}`;
2. enumerate all `8` or `128` classes;
3. apply every Galois conjugate to each representative;
4. add the conjugates using the exact elliptic formal group law;
5. reduce the resulting base coordinate modulo `8` or `16`;
6. collect the resulting residue classes.

The output is independent of the chosen source representatives because changing a representative by an element of `4O_{L_n}` changes its norm by an element of `D_n`.

Thus `S_n` is an exact, reproducible finite arithmetic object.

## 8. Apply the table to the saturated generator

Protected WP28 defines

`r_red(P):=ord_2(ord(red(P)))`.

Set

`Q_P:=[2^{r_red(P)}]P`.

By definition of `r_red(P)`, `Q_P` reduces to the identity, so

`Q_P in Ehat(2Z_2)`.

Its class modulo the infinite formal universal norms is exactly protected

`z_form(P)`.

At the stabilized layer `n=m_2`, protected WP31 identifies the image of this class with the finite twisted-reciprocity class represented by `c_tw(P)`.

### Theorem `BSD-A1-WP36-CLASSIFY-001`

The WP31 exponent is determined exactly as follows.

#### Case `a_2=+1`

Then `m_2=1` and `F_{2,1}^norm` is cyclic of order `2`.

- If `Q_P mod D_1 in S_1`, then `Q_P in H_1`, hence the class is zero:
  `c_tw(P)=0 mod 2` and `tau_form(P)=1`.
- Otherwise the class is the unique nonzero class:
  `c_tw(P)=1 mod 2` and `tau_form(P)=0`.

#### Case `a_2=-1`

Then `m_2=2` and `F_{2,2}^norm` is cyclic of order `4`.

- If `Q_P mod D_2 in S_2`, then `Q_P in H_2`, so
  `c_tw(P)=0 mod 4` and `tau_form(P)=2`.
- If `Q_P notin H_2` but `[2]Q_P in H_2`, then the class has order `2`, so
  `c_tw(P)=2 mod 4` and `tau_form(P)=1`.
- If `[2]Q_P notin H_2`, then the class has order `4`, so `c_tw(P)` is odd, defined up to multiplication by an odd unit, and
  `tau_form(P)=0`.

### Proof

Protected WP31 gives, at `n=m_2`, an isomorphism

`F_2^norm ~= F_{2,m_2}^norm ~= G_{m_2}/(1-alpha)G_{m_2}`

that preserves element order, and proves

`tau_form(P)=min(m_2,ord_2(c_tw(P)))`.

Theorem `FINITE-IMAGE-001` decides exactly whether the class of `Q_P` is zero.

For `m_2=1`, the quotient has order `2`, so zero/nonzero is the complete classification.

For `m_2=2`, the quotient is cyclic of order `4`. A class has order at most `2` exactly when its double is zero. Thus the two membership tests on `Q_P` and `[2]Q_P` distinguish orders `1`, `2`, and `4`. The corresponding exponent residues are `0`, `2`, and an odd residue modulo `4`, respectively. WP31's depth formula gives the three stated values of `tau_form(P)`. QED.

## 9. Exact local and global consequences

Protected WP31 gives

`rho_2(P)
 = r_red(P)+m_2-tau_form(P)`.

The preceding theorem makes every term on the right exactly computable by finite local arithmetic.

Protected WP26 gives

`rho_E=max(rho_2(P),rho_bad(P))`.

Protected WP24 gives

`len_Z2(C_E^vee)
 = 2 ord_2(3-a_2)
   + sum_{ell|N}ord_2(c_ell)
   - rho_E`.

### Corollary `BSD-A1-WP36-CONTROL-DEFECT-001`

For every curve in the protected selected class, `rho_2(P)`, `rho_E`, and `len_Z2(C_E^vee)` are determined by a finite exact calculation from:

- the minimal integral local Weierstrass equation at `2`;
- the exact local coordinate of the saturated generator `P`;
- the literal reduction of `P` modulo `2`;
- at most `128` shallow formal classes in the degree-4 local cyclotomic layer;
- the already protected odd-prime Neron-component and Tamagawa data.

No infinite-tower computation remains in this local-control lane.

## 10. Boundary disposition

Protected WP31 left

`MISSING_P2_FINITE_TWISTED_RECIPROCITY_EXPONENT`.

WP36 closes that boundary in the exact computable-criterion sense required by WP31: the residue class controlling the exponent is determined by a bounded finite arithmetic procedure.

WP36 does **not** prove that the exponent has one uniform curve-independent value. If a closed symbolic formula is desired separately, that is an optimization of the computation, not an unresolved correctness condition for the local control defect.

## 11. Claim firewall

WP36 does not prove:

- a shallow formal-logarithm isomorphism on `Ehat(2Z_2)`;
- a curve-independent value for `c_tw(P)`;
- equality of `c_tw(P)` with a p-adic logarithm, height, regulator, or WP20 Bockstein;
- D1c `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2 `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`;
- the remaining analytic/algebraic determinant equality;
- `BSD-R2-A1`;
- theorem novelty, priority, patentability, commercial significance, or MATHCERT certification.
