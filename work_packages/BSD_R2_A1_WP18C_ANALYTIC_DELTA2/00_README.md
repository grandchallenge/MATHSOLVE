# BSD-R2-A1-WP18C — exact analytic `delta_2` on the verified A/B controls

## Purpose

WP18C closes the analytic side of the two-curve WP18 atlas under the exact WP00 normalization.

For each protected control it proves

`delta_2(E)=0`

and combines this with protected WP18B to prove the individual-control equality

`delta_2(E) = v_2(Fitt^0_{Z_2}(T_E)) = 0`.

This is an exact theorem for `53a1` and `203b1`. It is not the uniform selected-class theorem `BSD-R2-A1`, and it is not MATHCERT certification.

## Protected inputs

### MATHSOLVE

Protected baseline:

`6a9502b3a9e280b8593484f71cf4f21ff50eac97`.

From WP18A:

- `53a1`: rank one, conductor `53`, trivial rational torsion, `sum_{ell|N} ord_2(c_ell)=0`;
- `203b1`: rank one, conductor `203`, trivial rational torsion, `ord_2(c_7)=1`, `ord_2(c_29)=0`, hence `sum_{ell|N} ord_2(c_ell)=1`.

From WP18B, for both controls:

- `Sha(E/Q)[2^infinity]=0`;
- `s_n(E)=0` for every `n>=1`;
- `T_E=0`;
- `Fitt^0_{Z_2}(T_E)=Z_2`;
- therefore `v_2(Fitt^0_{Z_2}(T_E))=0`.

### MATHFORGE

Protected source admission:

`6b0bc6444bcf675c1b7774caa1f719efabdd49f6`.

Admitted audit:

`sources/BSD-001/GJPST_RANK1_ANALYTIC_SHA_WP18C_SOURCE_AUDIT.md`.

The admitted GJPST result is the exact rank-one analytic-order conclusion in the proof of Theorem 1.8 of Grigorov–Jorza–Patrikis–Stein–Tarniţă (2009):

for every rank-one elliptic curve over `Q` of conductor at most `1000`,

`#Sha(E)_an = 1`

exactly.

The source audit verifies exact concordance with WP00 for:

- the ordinary finite Hasse–Weil `L(E,s)` and `L'(E,1)`;
- `Omega_E = integral_{E(R)} |omega|` for the invariant differential on a minimal Weierstrass model;
- the Néron–Tate/canonical-height regulator;
- Néron Tamagawa numbers;
- the rational torsion-square denominator.

The known Lawson–Wuthrich correction concerns a later odd-prime Galois-cohomology/Kolyvagin argument and is explicitly excluded from this source interface.

## Source identity in WP00 notation

For rank one, the admitted exact analytic order is

`1 = L'(E,1) * (#E(Q)_tors)^2 / (Omega_E Reg_E product_{ell|N} c_ell)`.

Therefore

`L'(E,1)/(Omega_E Reg_E)
 = (product_{ell|N} c_ell)/(#E(Q)_tors)^2`

as an exact positive rational identity.

Taking `2`-adic valuations gives

`ord_2(L'(E,1)/(Omega_E Reg_E))
 = sum_{ell|N} ord_2(c_ell) - 2 ord_2(#E(Q)_tors)`.

Both protected controls have trivial rational torsion, so the torsion term vanishes.

Hence

`ord_2(L'(E,1)/(Omega_E Reg_E))
 = sum_{ell|N} ord_2(c_ell)`.

By definition,

`delta_2(E)
 := ord_2(L'(E,1)/(Omega_E Reg_E))
    - sum_{ell|N} ord_2(c_ell)`.

Therefore

`delta_2(E)=0`.

No analytic Sha value is being substituted for the arithmetic Sha group here. The admitted analytic-order theorem is used only to determine the analytic leading-term quotient; the arithmetic side was independently settled in WP18B.

## Theorem A — regime A control

For `E=53a1`,

`ord_2(L'(E,1)/(Omega_E Reg_E))=0`,

and

`delta_2(E)=0`.

### Proof

`53a1` has rank one and conductor `53<=1000`, so the admitted GJPST source gives `#Sha(E)_an=1` in the exact WP00 normalization. Protected WP18A gives trivial rational torsion and `ord_2(c_53)=0`. Substitution into the exact analytic-order identity gives

`ord_2(L'/(Omega Reg))=0`,

hence `delta_2(E)=0`. QED.

Protected WP18B gives `v_2(Fitt^0(T_E))=0`. Therefore

`delta_2(53a1)=v_2(Fitt^0(T_53a1))=0`.

## Theorem B — regime B control

For `E=203b1`,

`ord_2(L'(E,1)/(Omega_E Reg_E))=1`,

and

`delta_2(E)=0`.

### Proof

`203b1` has rank one and conductor `203<=1000`, so the admitted GJPST source gives `#Sha(E)_an=1` in the exact WP00 normalization. Protected WP18A gives trivial rational torsion and

`ord_2(c_7)=1`,

`ord_2(c_29)=0`.

Thus

`sum_{ell|203} ord_2(c_ell)=1`.

The exact analytic-order identity gives

`ord_2(L'/(Omega Reg))=1`.

Subtracting the protected Tamagawa valuation gives

`delta_2(E)=1-1=0`. QED.

Protected WP18B gives `v_2(Fitt^0(T_E))=0`. Therefore

`delta_2(203b1)=v_2(Fitt^0(T_203b1))=0`.

This is the desired exact cancellation across a genuine residual-conductor-drop / even-Tamagawa example.

## Individual-control `p=2` valuation statement

Protected WP05/WP18A establish analytic and algebraic rank one and finite Sha for these controls. WP18B establishes the actual `2`-primary Sha valuation `0`. WP18C establishes the WP00-normalized analytic predicted `2`-primary valuation `0`.

Consequently the exact `2`-adic valuation form of the rank-one leading-term BSD equality holds for each of `53a1` and `203b1`.

This is the `p=2` component selected by this campaign. It is not a claim that WP18C proves the full rational leading-term BSD identity, and it is **not** a MATHCERT certification disposition.

## What the A/B comparison establishes

The two controls now agree on the exact residual quantity:

| curve | WP13 regime | analytic leading quotient valuation | Tamagawa valuation | `delta_2` | Fitting valuation |
|---|---|---:|---:|---:|---:|
| `53a1` | A | `0` | `0` | `0` | `0` |
| `203b1` | B | `1` | `1` | `0` | `0` |

Thus the even-Tamagawa/residual-conductor-drop contribution in regime B is not missing from the analytic side: on `203b1` it appears as exactly one power of `2` in the leading quotient and cancels the one power of `2` contributed by the Tamagawa factor.

This is exact evidence for the normalization architecture. It is not a proof that the same cancellation holds uniformly for the selected class.

## Consequence for WP18

The minimal A/B atlas objective is now closed at the exact level:

- local regime classification: exact;
- finite `2`-Selmer measurement: exact and independently source-audited;
- full `2^n` tower on both controls: exact theorem consequence;
- integral Fitting valuation: exact;
- WP00-normalized analytic `delta_2`: exact;
- equality across both sides: exact for both controls.

No further numerical stabilization is needed for these two controls.

## Return to the uniform theorem frontier

The diagnostic atlas has done its job. The active mathematical frontier returns to

`BSD-R2-A1-S3-K-INTEGRAL-FITTING-CONTROL`.

The surviving provider/theorem debt remains

`P2_GOOD_ORDINARY_IRREDUCIBLE_S3_EXACT_MU_OR_PRIMITIVE_FITTING_CONTROL`.

The exact next substantive question is no longer whether the normalization can work in regime B; `203b1` proves that it can. The remaining task is to produce a uniform theorem over the protected selected class that forces the same equality

`delta_2(E)=v_2(Fitt^0_{Z_2}(T_E))`

without relying on bounded-conductor individual verification.

## Claim firewall

- `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED` remains unchanged.
- WP18C proves individual-control equalities only.
- GJPST analytic `#Sha_an` is not treated as an arithmetic computation of Sha.
- WP18B remains the independent arithmetic evidence/proof for the controls.
- The known flawed later odd-prime GJPST argument is not used.
- No floating-point recognition is used by WP18C itself.
- No uniform p=2 Iwasawa/Fitting theorem is inferred from two examples.
- No full rational leading-term BSD identity is claimed from the `p=2` valuation result.
- No MATHCERT certification is asserted.
- No novelty, priority, patentability, or commercial claim follows.
