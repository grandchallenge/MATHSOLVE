# WP60B theorem — exact Kriz–Li literal-`2` normalization transport

## 1. Protected setup

Let `E/Q` lie in the protected selected `BSD-R2-A1` class. In particular:

- `E` has good ordinary reduction at `2`;
- `a_2 in {+1,-1}` and
  `#E(F_2)=3-a_2`;
- protected WP12 gives a surjective residual representation
  `G_Q -> GL_2(F_2)`;
- protected WP38 identifies the free rank-one Mordell–Weil lattices over `Q` and the WP09 quadratic field `K`;
- protected WP56A fixes a primitive generator
  `P in E(Q)/E(Q)_tors`
  and writes the conductor-one Heegner trace for the protected parametrization as
  `P_K(f)=m_K(f)P+T`,
  with `m_K(f) != 0` and `T in E(K)_tors`;
- protected WP58A fixes the source-compatible modular parametrization
  `f:X_0(N)->E`
  and the WP00 minimal Néron differential `omega_E` with
  `f^*omega_E = eps_f C_f phi(q)dq/q`,
  where `eps_f in {+1,-1}` and
  `ord_2(C_f)=0`.

Protected MATHFORGE WP60B at

`grandchallenge/MATHFORGE@a8f72ed64755777870a300053e11659fb1dfff1b`

admits the exact Kriz–Li Assumption `(F)`. For the same modular parametrization `f`, let `omega_f^KL` be the invariant differential normalized by

`f^*omega_f^KL = phi(q)dq/q`.

The source condition is

`2 splits in K`

and

`((3-a_2)/2) log_{omega_f^KL}(P_KL(f)) != 0 mod 2`,

where the corresponding Heegner point is defined up to sign and torsion. The selected WP09 lane already requires `2` to split in `K`.

## 2. Differential transport

### Lemma `BSD-A1-WP60B-DIFF-001`

For the fixed parametrization `f`,

`omega_f^KL = eps_f C_f^(-1) omega_E`.

Consequently, for every point in the common `2`-adic logarithm domain,

`log_{omega_f^KL}(Q)
 = eps_f C_f^(-1) log_{omega_E}(Q)`.

### Proof

Protected WP58A gives

`f^*omega_E = eps_f C_f phi(q)dq/q`,

whereas the admitted Kriz–Li normalization gives

`f^*omega_f^KL = phi(q)dq/q`.

Pullback by the nonconstant modular parametrization is injective on the one-dimensional space of invariant differentials. Hence

`omega_E=eps_f C_f omega_f^KL`.

The `2`-adic logarithm is the integral of the chosen invariant differential and is therefore linear in that differential. QED.

Since `ord_2(C_f)=0`, the differential conversion is a `2`-adic unit conversion.

## 3. The fixed local logarithmic scalar is integral

Set

`q_2:=#E(F_2)=3-a_2 in {2,4}`

and define

`kappa_2(E,P)
 := (q_2/2) log_{omega_E}(P)
 = ((3-a_2)/2) log_{omega_E}(P)`.

### Lemma `BSD-A1-WP60B-KAPPA-INTEGRAL-001`

`kappa_2(E,P) in Z_2`.

### Proof

The reduction of `P` lies in the finite group `E(F_2)` of order `q_2`. Therefore

`Q:=[q_2]P`

reduces to the identity and belongs to the formal subgroup

`E_1(Q_2)=ker(E(Q_2)->E(F_2))`.

For a minimal good-reduction Weierstrass model, the formal parameter of every point of `E_1(Q_2)` lies in `2Z_2`. Write the invariant Néron differential in the formal coordinate `t` as

`omega_E=g(t)dt`,

with `g(t) in Z_2[[t]]` and unit constant term. Its formal logarithm is

`log_{omega_E}(t)
 = sum_{n>=0} g_n t^(n+1)/(n+1)`.

For `t in 2Z_2`, every summand has valuation at least

`(n+1)-ord_2(n+1) >= 1`,

and these valuations tend to infinity. Hence

`log_{omega_E}(Q) in 2Z_2`.

The logarithm is a group homomorphism, so

`log_{omega_E}(Q)=q_2 log_{omega_E}(P)`.

Therefore

`kappa_2(E,P)
 = (1/2) log_{omega_E}(Q)
 in Z_2`.

QED.

The unit/nonunit status of `kappa_2(E,P)` is invariant under replacing the primitive generator `P` by `-P`.

## 4. Exact transport of the Kriz–Li expression

The Kriz–Li Heegner point attached to the same conductor-one parametrization is the same trace point as the protected `P_K(f)`, up to the sign/torsion ambiguity explicitly allowed by the source normalization. The `2`-adic logarithm vanishes on torsion because its target is torsion-free.

Thus

`log_{omega_E}(P_KL(f))
 = +/- log_{omega_E}(P_K(f))
 = +/- m_K(f) log_{omega_E}(P)`.

Define the normalized Kriz–Li quantity

`KL_2(E,K,f)
 := ((3-a_2)/2) log_{omega_f^KL}(P_KL(f))`.

### Theorem `BSD-A1-WP60B-KL-TRANSPORT-001`

Exactly,

`KL_2(E,K,f)
 = u_f m_K(f) kappa_2(E,P)`

for some

`u_f in Z_2^x`.

More precisely one may take `u_f=+/- C_f^(-1)`.

### Proof

Combine Lemma `DIFF-001`, the Heegner-index decomposition, torsion-killing of the logarithm, and the definition of `kappa_2(E,P)`. Protected WP58A gives `C_f in Z_2^x`. QED.

## 5. Classification of Assumption `(F)`

The source expression `KL_2(E,K,f)` is the quantity required to be nonzero modulo `2`. By Lemma `KAPPA-INTEGRAL-001`, both

`m_K(f)` and `kappa_2(E,P)`

are `2`-integral, while `u_f` is a unit.

### Corollary `BSD-A1-WP60B-F-CLASSIFY-001`

On the protected selected lane,

`Assumption (F)`

is equivalent to the conjunction

`ord_2(m_K(f))=0`

and

`kappa_2(E,P) in Z_2^x`.

Equivalently,

`(F) <=> [m_K(f) is odd] AND [kappa_2(E,P) is a 2-adic unit]`.

### Proof

A product of elements of `Z_2` is a unit exactly when every factor is a unit. Apply Theorem `KL-TRANSPORT-001`; `u_f` is already a unit. QED.

This is the requested WP60B independence classification:

`MIXED_BUT_NO_INDEPENDENT_K_VARYING_ESCAPE`.

The condition consists of:

1. a fixed selected-curve local factor `kappa_2(E,P)`, independent of the auxiliary field `K`; and
2. the parity of the genuine Heegner index `m_K(f)`, which is exactly the unknown `R1` component.

Varying `K` cannot alter the fixed local factor.

## 6. Compatibility with Kriz–Li indivisibility

The protected source audit records that, under the paper's stated local hypotheses, `(F)` forces the Heegner point to be indivisible by `2`. The selected curve has good reduction at `2`, so the local Tamagawa factor there is one.

The selected residual representation also gives a direct lattice interpretation.

### Lemma `BSD-A1-WP60B-K2TORS-001`

`E(K)[2]=0` for every quadratic field `K/Q` on the selected lane.

### Proof

Protected WP12 gives image `GL_2(F_2) ~= S_3` on `E[2]`. The stabilizer of any nonzero `2`-torsion point has index three, so the field of definition of such a point has degree three over `Q`. It cannot be contained in a quadratic field. QED.

Hence the finite group `E(K)_tors` has odd order, so multiplication by `2` is an automorphism on it.

### Corollary `BSD-A1-WP60B-INDEX-PARITY-001`

`P_K(f)` is indivisible by `2` in `E(K)` if and only if `m_K(f)` is odd.

### Proof

If `m_K(f)` is even, write the torsion term `T=2T'`; then

`P_K(f)=2((m_K(f)/2)P+T')`.

Conversely, if `P_K(f)=2Q`, passage to the free quotient `E(K)/tors ~= Z[P]` makes `m_K(f)` even. QED.

Thus the source implication `(F) => Heegner 2-indivisibility` is exactly consistent with Corollary `F-CLASSIFY-001`: `(F)` forces the parity statement already isolated in protected WP56A/WP59.

## 7. Consequence for the WP59 reopening contract

Protected WP59 reopening form `R3` asks for a theorem forcing the Kriz–Li mod-`2` logarithmic condition for some WP09-compatible field for every selected curve.

Theorem `KL-TRANSPORT-001` shows that such a theorem would necessarily prove both:

1. the fixed local-unit condition
   `kappa_2(E,P) in Z_2^x`; and
2. the Heegner-index parity
   `ord_2(m_K(f))=0`
   for the produced field.

Therefore `R3` is not an independent auxiliary-field bypass of `R1`. Its `K`-varying content is exactly the parity component of `R1`, together with a fixed curve-local prerequisite.

This does not make `R3` logically useless: a new theorem proving `(F)` uniformly would still close the parity obligation. It shows only that searching for field variation to force `(F)` cannot avoid proving the same Heegner-index parity.

## 8. New exact research split

WP60B replaces the vague question “is Kriz–Li `(F)` independent?” by two explicit obligations:

### KL-LOCAL

`MISSING_UNIFORM_KRIZ_LI_FIXED_LOCAL_LOG_UNIT`

Prove for every selected curve that

`kappa_2(E,P)=((3-a_2)/2)log_{omega_E}(P)`

is a `2`-adic unit, or classify exactly when it is not.

This is a fixed local problem and is suitable for WP60C exact computation/falsification.

### KL-INDEX

`MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`

Prove that a WP09-compatible field can be chosen with

`ord_2(m_K(f))=0`.

This is the genuine auxiliary-field arithmetic problem.

Neither obligation is resolved here.

## 9. Claim firewall

WP60B does not prove:

- `kappa_2(E,P)` is always a unit;
- `m_K(f)` is odd for any or every WP09 field;
- existence of a WP09-compatible field satisfying Kriz–Li `(F)`;
- an exact value of `ord_2(lambda_D)`;
- WP59 `R1`, `R3`, or `R4` uniformly;
- D2d;
- the height-one-`(2)` Fitting divisibility or determinant primitivity from WP60A;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.
