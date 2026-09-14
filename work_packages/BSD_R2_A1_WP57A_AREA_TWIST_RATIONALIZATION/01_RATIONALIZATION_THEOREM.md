# WP57A theorem — exact rationalization of the WP00 quotient

## 1. Protected starting identity

Protected WP56A proves

`(1)
 L'(E,1)/(Omega_E Reg_E)
 = 4 m_K(f)^2 A_E
   / (C_f^2 u_K^2 sqrt(|D_K|) Omega_E L(E^D,1))`.

Here every symbol has the protected WP00/CST normalization. In particular `C_f` is the positive integer defined by

`f^*omega_E = +/- C_f 2*pi*i*phi(z)dz`.

## 2. Exact area/period identity

Let

`Lambda_E = { integral_gamma omega_E : gamma in H_1(E(C),Z) }`

be the period lattice of the minimal Néron differential. Complex conjugation preserves `Lambda_E` and has rank-one plus and minus eigensublattices.

Let `a>0` generate the positive real-period eigensublattice and let

`i b`, with `b>0`,

generate the anti-invariant period eigensublattice. By definition

`b=|Omega_E^-|`.

The quotient

`Lambda_E/(Lambda_E^+ + Lambda_E^-)`

is killed by `2`, since for every `lambda in Lambda_E`,

`2 lambda=(lambda+conj(lambda))+(lambda-conj(lambda))`.

For a rank-two real elliptic lattice the quotient has order one or two. Thus, after the above primitive choices, there are exactly two normal forms.

### Case R — rectangular lattice

`Lambda_E = Z a + Z i b`.

The fixed locus of conjugation on `C/Lambda_E` has two connected circles, each with real-period length `a`. Therefore

`Omega_E=2a`.

The covolume of the lattice is `ab`. Since

`A_E=(i/2) integral_{E(C)} omega_E wedge overline(omega_E)`

is exactly this covolume,

`A_E=ab=Omega_E b/2`.

### Case H — index-two/rhombic lattice

`Lambda_E = Z a + Z((a+i b)/2)`.

The fixed locus of conjugation is connected and its real-period length is `a`. Thus

`Omega_E=a`.

The lattice covolume is `ab/2`, hence again

`A_E=ab/2=Omega_E b/2`.

We have proved:

### Lemma `BSD-A1-WP57-AREA-001`

Exactly,

`(2)
 A_E = Omega_E |Omega_E^-|/2`.

No connected-component factor is missing: the two possible real topologies are precisely what makes the same formula hold in both cases.

## 3. Exact twist-period transport

Protected MATHFORGE WP57 admits Pal's negative-twist period formula. On the protected WP09 auxiliary lane:

- `D_K` is a negative fundamental discriminant;
- `2` splits, hence `D_K == 1 (mod 8)`, in particular `D_K == 1 (mod 4)`;
- `(D_K,N)=1`;
- `E` is semistable, so the support of the minimal discriminant is the bad-prime support of `N`.

Therefore `gcd(D_K,Delta(E))=1`, and Pal Corollary 2.6 gives the minimal-model correction

`tilde u=1`.

Thus

`(3)
 Omega(E^D)
 = c_infinity(E^D) |Omega_E^-|/sqrt(|D_K|)`.

Define

`(4)
 lambda_D := L(E^D,1)/Omega(E^D)`.

Protected WP09 gives `L(E^D,1)!=0`. Protected MATHFORGE WP57 admits modular-symbol rationality after exact modular/isogeny period transport, so

`lambda_D in Q^x`.

## 4. The auxiliary unit factor is one

Recall

`u_K=[O_K^x:{+1,-1}]`.

### Lemma `BSD-A1-WP57-UNIT-001`

For the protected auxiliary field,

`u_K=1`.

### Proof

Let `epsilon` be a unit in an imaginary quadratic field. Its norm is a positive unit of `Z`, hence one. Therefore its two complex conjugates have product one and equal absolute value one. Its trace is an integer in `[-2,2]`. If `epsilon` is not `+/-1`, its minimal polynomial is one of those giving a primitive root of unity of order `3`, `4`, or `6`; hence the field is `Q(sqrt(-3))` or `Q(i)`.

In `Q(i)`, the prime `2` ramifies. In `Q(sqrt(-3))`, whose fundamental discriminant is `-3 == 5 (mod 8)`, the prime `2` is inert. Protected WP09 requires `2` to split in `K`, so neither exceptional field is possible. Thus `O_K^x={+/-1}` and `u_K=1`. QED.

## 5. Rationalization

Insert (2) into (1):

`L'(E,1)/(Omega_E Reg_E)
 = 2 m_K(f)^2 |Omega_E^-|
   / (C_f^2 u_K^2 sqrt(|D_K|) L(E^D,1))`.

From (3) and (4),

`|Omega_E^-|/(sqrt(|D_K|) L(E^D,1))
 = 1/(c_infinity(E^D) lambda_D)`.

Using `u_K=1` gives the main theorem.

### Theorem `BSD-A1-WP57-RAT-001`

Exactly,

`(5)
 L'(E,1)/(Omega_E Reg_E)
 = 2 m_K(f)^2
   / (C_f^2 c_infinity(E^D) lambda_D)`.

The right side lies in `Q^x` because

- `m_K(f)` is a nonzero integer;
- protected MATHFORGE WP55 records `C_f` as a positive integer;
- `c_infinity(E^D)` is `1` or `2`;
- `lambda_D in Q^x`.

This establishes the rational line required before applying `ord_2`.

## 6. Exact valuation ledger

Taking the ordinary 2-adic valuation of (5) is now legitimate:

### Corollary `BSD-A1-WP57-VAL-001`

`(6)
 ord_2(L'(E,1)/(Omega_E Reg_E))
 = 1
   + 2 ord_2(m_K(f))
   - 2 ord_2(C_f)
   - ord_2(c_infinity(E^D))
   - ord_2(lambda_D)`.

Therefore the protected target defect is exactly

`(7)
 delta_2(E)
 = 1
   + 2 ord_2(m_K(f))
   - 2 ord_2(C_f)
   - ord_2(c_infinity(E^D))
   - ord_2(lambda_D)
   - sum_{ell|N} ord_2(c_ell)`.

No real-period scalar remains in (6) or (7).

## 7. Refined D2d boundary

WP57A resolves the area/period algebraicity defect. D2d is now

`MISSING_P2_HEEGNER_INDEX_MODULAR_DIFFERENTIAL_AND_TWIST_LRATIO_VALUATION_CONTROL`.

The unresolved arithmetic inputs are sharply finite:

`H1 = ord_2(m_K(f))`,

`H2 = ord_2(C_f)`,

`H3 = ord_2(lambda_D)`.

The topological term `ord_2(c_infinity(E^D))` is explicit once the real connectedness of the twist is fixed, and the bad-prime Tamagawa term is already part of the protected WP13/WP52 ledger.

## 8. Claim firewall

WP57A does not prove or assume:

- `ord_2(m_K(f))=0`;
- `ord_2(C_f)=0` or `C_f=1`;
- any value of `ord_2(lambda_D)`;
- a rank-zero BSD formula for `E^D`;
- fixed-2 p-adic-height nondegeneracy;
- a height-one `(2)` analytic determinant generator;
- cancellation with WP54A by similarity of factors;
- final WP06 normalization descent;
- `BSD-R2-A1`;
- MATHCERT certification.
