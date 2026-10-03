# RH-R056-CANONICAL-DETERMINANT-NORMALIZATION-001

- Campaign: RH-001
- Solve tracker: grandchallenge/MATHSOLVE#702
- Route coordination: grandchallenge/MATHSOLVE#414
- Obligation: Route C / C0 — exact canonical finite determinant normalization
- Solve base: grandchallenge/MATHSOLVE@b7adb8f59d79c58b3de915eaa5abafcbb90b009e
- Protected provider audit: grandchallenge/MATHFORGE@4904308b524bf67714d74ce5a88908d695d76ee5
- Provider artifact: reports/discovery/rh_001/rh_r056_determinant_normalization.md
- Primary source: Connes–Consani–Moscovici, *Zeta Spectral Triples*, arXiv:2511.22755v1
- Parent theorem: RH-R035-ZETA-SPECTRAL-TRIPLES-LIMIT-001
- Route-C stability theorem: RH-R053-COMPACT-TRANSFORM-STABILITY-001
- Certification status: theorem-development only; not certified
- Novelty / priority / RH claim: none

## 1. Purpose

Route C requires one exact normalized finite entire determinant before any
cofinal or convergence theorem can be stated. The CCM source fixes the raw
regularized determinant but leaves the scalar normalization toward Riemann's
Xi function unspecified in its Section 7 outlook.

The protected R056 provider audit pins the exact source boundary:

`G_(lambda,N)(z) := det_reg(D_log^(lambda,N)-z)`
`                  = -i lambda^(-i*z) xi_(lambda,N)_hat(z)`,

under the finite simple-even hypothesis and the finite source normalization
`delta_N(xi_(lambda,N))=1`.

This package closes C0 by fixing a campaign-canonical gauge without guessing
the missing CCM scalar. The construction:

1. removes the exact source-fixed phase `lambda^(-i*z)`;
2. uses the source evenness to eliminate any remaining linear exponential
   gauge;
3. fixes the remaining scalar at one explicit nonreal anchor inside the source
   convergence strip;
4. proves that the resulting normalizer is entire and zero-free;
5. proves exact preservation of the real-zero property;
6. proves that this gauge is convergence-equivalent to any successful scalar
   normalization on a domain containing the anchor.

No convergence theorem is asserted here.

## 2. Protected finite source interface

Fix `lambda > 1` and `N` for which the finite CCM hypothesis holds:

- the lowest eigenvalue of `QW_lambda^N` is simple;
- a corresponding eigenvector `xi_(lambda,N)` is even under `u -> u^(-1)`;
- it is normalized by `delta_N(xi_(lambda,N))=1`.

Write

`H_(lambda,N)(z) := xi_(lambda,N)_hat(z)`.

The protected source theorem gives:

`G_(lambda,N)(z) = -i lambda^(-i*z) H_(lambda,N)(z)`,

`H_(lambda,N)` is entire, every zero of `H_(lambda,N)` is real, and those
zeros are exactly the finite approximant spectrum.

The factor `lambda^(-i*z)=exp(-i*z*log(lambda))` is entire and zero-free.
Therefore `G_(lambda,N)` and `H_(lambda,N)` have exactly the same zeros, with
the same multiplicities.

## 3. Parity removes the linear exponential phase

### Lemma 3.1 — even transform

If `xi_(lambda,N)(u)=xi_(lambda,N)(u^(-1))`, then

`H_(lambda,N)(-z) = H_(lambda,N)(z)`

for every complex `z`.

### Proof

By the source transform convention,

`H(z) = integral_[lambda^-1,lambda] xi(u) u^(-i*z) du/u`.

Substitute `u=v^(-1)`. The multiplicative Haar measure is invariant, the
interval reverses back to itself, and source evenness gives

`H(z) = integral xi(v) v^(i*z) dv/v = H(-z)`.

Thus `H` is even. QED.

Consequently the exact phase-stripped determinant is

`i lambda^(i*z) G_(lambda,N)(z) = H_(lambda,N)(z)`,

an even entire function with only real zeros.

## 4. A fixed nonreal Xi anchor

Define

`z_* := i/4`.

This point has three useful properties:

1. it is nonreal, so no admitted finite `H_(lambda,N)` can vanish there;
2. it lies strictly inside the source strip `|Im z| < 1/2` used in Section 7;
3. the target value `Xi(z_*)` is nonzero by an elementary argument.

### Lemma 4.1 — `Xi(i/4) != 0`

Use the classical convention

`Xi(z) = xi_R(1/2 + i*z)`,

`xi_R(s) = (1/2) s(s-1) pi^(-s/2) Gamma(s/2) zeta(s)`.

At `z=i/4`, the xi-variable is `s=1/4`.

For real `0<s<1`, the alternating eta series

`eta(s) = sum_(n>=1) (-1)^(n-1) n^(-s)`

is strictly positive: pairing consecutive terms gives

`(2k-1)^(-s) - (2k)^(-s) > 0`,

and the alternating series converges. On `Re(s)>0`, `s != 1`, analytic
continuation of the standard identity gives

`eta(s) = (1 - 2^(1-s)) zeta(s)`.

At `s=1/4`, the left side is positive while
`1 - 2^(3/4) != 0`, hence `zeta(1/4) != 0`.

The other factors in `xi_R(1/4)` are finite and nonzero:
`(1/4)(-3/4) != 0`, `pi^(-1/8) != 0`, and `Gamma(1/8) != 0`.
Therefore

`Xi(i/4) = xi_R(1/4) != 0`. QED.

Because every zero of `H_(lambda,N)` is real and `z_*` is nonreal,

`H_(lambda,N)(z_*) != 0`

for every admitted finite pair `(lambda,N)`.

## 5. Canonical Route-C finite determinant

### Definition 5.1 — campaign-canonical C0 normalization

For every finite pair `(lambda,N)` satisfying the CCM simple-even hypothesis,
define

`F_(lambda,N)(z)`
`  := Xi(z_*) H_(lambda,N)(z) / H_(lambda,N)(z_*)`

with `z_*=i/4`.

Equivalently, using only the raw regularized determinant,

`F_(lambda,N)(z)`
`  = Xi(z_*) [lambda^(i*z) G_(lambda,N)(z)]`
`              / [lambda^(i*z_*) G_(lambda,N)(z_*)]`.

The scalar `i` from the source formula cancels in this ratio.

The choice `z_*=i/4` is a campaign gauge choice, not a scalar claimed to be
specified by CCM. It is frozen here so that all later Route-C statements refer
to one exact family. It uses one explicitly known nonzero value of the target
entire function and no zeta-zero ordinate or RH-dependent data.

### Theorem 5.2 — well-definedness and zero preservation

For every admitted finite pair `(lambda,N)`, `F_(lambda,N)` is:

1. an entire function;
2. even in `z`;
3. normalized by `F_(lambda,N)(z_*) = Xi(z_*)`;
4. related to the raw determinant by multiplication by a zero-free entire
   function;
5. zero-equivalent to `G_(lambda,N)` and `H_(lambda,N)`, including
   multiplicities;
6. therefore an entire function whose zeros are all real.

### Proof

`H(z_*)` is nonzero by Section 4, so Definition 5.1 is well-defined.
`H` is entire and even by the protected source theorem and Lemma 3.1. Division
by the nonzero constant `H(z_*)` and multiplication by the nonzero constant
`Xi(z_*)` preserve both properties, proving (1)-(3).

In raw-determinant form,

`F(z) = M_(lambda,N)(z) G(z)`,

where

`M_(lambda,N)(z)`
`  := Xi(z_*) lambda^(i*z)`
`       / [lambda^(i*z_*) G_(lambda,N)(z_*)]`.

The denominator is a nonzero constant and `lambda^(i*z)` is an exponential,
hence entire and nowhere zero. Since `Xi(z_*) != 0`, `M` is entire and
nowhere zero. This proves (4). A zero-free multiplier preserves the complete
zero divisor, proving (5). The protected finite source theorem then gives (6).
QED.

## 6. Uniqueness inside the source affine-exponential gauge

The CCM outlook describes a normalization of raw determinants by factors of
the affine-exponential form `exp(a+i*b*z)`. We now show that source evenness
and the frozen anchor remove that ambiguity exactly.

### Theorem 6.1 — affine-exponential uniqueness

Fix an admitted `(lambda,N)`. Let

`E(z) = C exp(beta*z) G_(lambda,N)(z)`

with `C != 0` and `beta` any complex number. Suppose:

1. `E` is even;
2. `E(z_*) = Xi(z_*)`.

Then necessarily

`beta = i log(lambda)`

and `E = F_(lambda,N)`.

Thus Definition 5.1 is the unique member of the full nonzero
affine-exponential gauge of the raw determinant satisfying evenness and the
fixed Xi anchor.

### Proof

Put `a=log(lambda)` and abbreviate `H=H_(lambda,N)`. The source identity gives

`G(z) = -i exp(-i*a*z) H(z)`.

Hence

`E(z) = (-i C) exp(kappa*z) H(z)`,

where `kappa := beta - i*a`.

Since `H` is even, evenness of `E` gives

`exp(kappa*z) H(z) = exp(-kappa*z) H(z)`

for all `z`. The entire function `H` is not identically zero: the source eigenvector is nonzero by
`delta_N(xi)=1`, it has compact support in the source interval, and injectivity
of the Fourier transform on compactly supported L1 functions forbids an
identically zero transform. Its nonzero set
therefore contains a nonempty open set. On that set,

`exp(2*kappa*z) = 1`.

By the identity theorem this equality holds everywhere. Differentiating at
`z=0` gives `2*kappa=0`, hence `kappa=0` and
`beta=i*a=i log(lambda)`.

Now `E(z)=(-i C)H(z)`. The anchor condition and `H(z_*) != 0` uniquely give

`C = i Xi(z_*) / H(z_*)`.

Substitution yields exactly

`E(z) = Xi(z_*) H(z)/H(z_*) = F_(lambda,N)(z)`.

QED.

## 7. The normalization does not assume an unknown scalar limit

The source leaves the scalar multiplying `H_lambda` toward Xi unspecified.
The anchor normalization is compatible with any successful scalar choice;
it does not assume that choice in advance.

### Lemma 7.1 — scalar-gauge transfer

Let `Omega` be a domain containing `z_*`. Let `(H_j)` be a sequence or net
of holomorphic functions on `Omega` with `H_j(z_*) != 0`. Suppose there are
nonzero scalars `c_j`, indexed by the same directed set, such that

`c_j H_j -> Xi`

locally uniformly on `Omega`.

Define

`F_j(z) := Xi(z_*) H_j(z)/H_j(z_*)`.

Then

`F_j -> Xi`

locally uniformly on `Omega`.

### Proof

At the anchor, local uniform convergence gives

`c_j H_j(z_*) -> Xi(z_*) != 0`.

Therefore

`r_j := Xi(z_*) / [c_j H_j(z_*)] -> 1`.

But

`F_j(z) = r_j [c_j H_j(z)]`.

On every compact subset of `Omega`, the second factor converges uniformly to
`Xi` and the scalar first factor tends to one. Hence `F_j -> Xi` locally
uniformly. QED.

### Consequence

If future C3/C4/C5 work proves CCM's Section 7 scalar-normalized transform
convergence on any domain containing `i/4`, the C0 family frozen here has the
same limit automatically. No formula for the source's unspecified scalars is
needed.

## 8. Affine-gauge subsequential identification

The same gauge choice simplifies the later C5 obligation.

### Corollary 8.1

Suppose a sequence or net of canonical `F_j` has a locally uniform
subsequential or subnet limit `Q` on C. Suppose separate future work identifies

`Q(z) = C exp(beta*z) Xi(z)`

for some `C != 0` and complex `beta`.

Then `Q = Xi`.

### Proof

Each `F_j` is even, so the locally uniform limit `Q` is even. The classical
`Xi` is even. On the nonzero set of Xi, evenness of
`C exp(beta*z) Xi(z)` implies `exp(2*beta*z)=1`; hence `beta=0` by the same
identity-theorem argument as in Theorem 6.1.

Also every `F_j(z_*)=Xi(z_*)`, so `Q(z_*)=Xi(z_*)`. Since Xi is nonzero there,
`C=1`. Thus `Q=Xi`. QED.

This corollary does not prove existence of a subsequential limit and does not
identify any actual subsequential/subnet limit up to an affine factor. It only removes that residual
gauge if future C4/C5 work reaches it.

## 9. Interaction with RH-R053

RH-R053 supplies compact-set stability for the raw determinant kernel
`lambda^(-i*z) f_hat(z)` and the exact rate dichotomy. The present theorem
does not improve those rates.

For the phase-stripped canonical family, later use of R053 must additionally
control the scalar

`Xi(z_*) / H_(lambda,N)(z_*)`.

Lemma 7.1 shows that such scalar control is automatic once any valid scalar
normalization is known to converge at the anchor, but C0 alone supplies no
boundedness or asymptotic estimate for it.

Therefore C4 normal-family control remains open and materially necessary under
the R053 rate dichotomy unless C3 produces extraordinary decay.

## 10. Cofinality and simple-even boundary

This theorem defines `F_(lambda,N)` only for finite pairs satisfying the source
finite simple-even hypothesis.

The protected local full-operator simple-even frontier now reaches only
`0 < log(lambda) <= 3561/20000` by RH-R055. It does not by itself provide the finite
simple-even hypothesis for every large scale and truncation needed by a
`lambda -> infinity` determinant argument.

Nothing here supplies:

- a cofinal schedule `(lambda_j,N_j)`;
- global simple-evenness at large `lambda`;
- a theorem that every sufficiently large finite pair is admissible;
- C3 eigenvector approximation;
- C4 local boundedness / Montel control;
- C5 substantive limit identification;
- C6 local uniform convergence on C.

Those remain separate obligations.

## 11. Theorem

### RH-R056-CANONICAL-DETERMINANT-NORMALIZATION-001

For each finite CCM pair `(lambda,N)` satisfying the source simple-even
hypothesis, let `G_(lambda,N)` be the source regularized determinant and set
`z_*=i/4`. Then the Route-C canonical normalized finite determinant

`F_(lambda,N)(z)`
`  := Xi(i/4) [lambda^(i*z) G_(lambda,N)(z)]`
`       / [lambda^(-1/4) G_(lambda,N)(i/4)]`

is well-defined, entire, even, and has exactly the same zero divisor as the
source finite determinant; in particular every zero is real.

Moreover it is the unique affine-exponential renormalization
`C exp(beta*z) G_(lambda,N)(z)` that is even and takes the value `Xi(i/4)` at
`z=i/4`.

Finally, on any domain containing `i/4`, convergence of any scalar-normalized
phase-stripped transforms to Xi implies local uniform convergence of this
canonical family to Xi.

Therefore Route C obligation C0 is discharged for the class of source-admitted
finite determinants. Cofinality/admissibility (C1), approximation (C3), normal
families (C4), substantive limit identification (C5), and full locally uniform
convergence (C6) remain open.

## 12. False-proof firewall

Reject:

1. attributing the anchor scalar in Definition 5.1 to CCM;
2. inferring a cofinal admissible family from this normalization theorem;
3. inferring large-scale simple-evenness from the current local theorem;
4. treating Lemma 7.1 as proof that any scalar normalization actually
   converges;
5. using the fixed anchor value as zero-location data;
6. invoking R035 Rouché/Hurwitz before C6 is proved;
7. claiming RH, certification, novelty, or priority from C0.

## 13. Admission disposition

`RH-R056_C0_CANONICAL_DETERMINANT_NORMALIZATION_PROVED__REAL_ZERO_PROPERTY_PRESERVED__C1_C3_C4_C5_C6_OPEN`
