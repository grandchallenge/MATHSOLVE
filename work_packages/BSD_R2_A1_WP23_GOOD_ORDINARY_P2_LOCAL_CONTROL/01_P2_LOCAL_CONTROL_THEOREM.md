# WP23 theorem — exact primitive good-ordinary local control at `2`

## 1. Setup and protected inputs

Let `E/Q` lie in the protected selected `BSD-R2-A1` class. Put

`A := E[2^infinity]`.

Let `Q_infty/Q` be the cyclotomic `Z_2`-extension, let `w` be its unique place above `2`, and write

`Gamma_2 := Gal(Q_{infty,w}/Q_2)`.

Protected WP21 defines

`W_2 := H^1(Q_2,E)[2^infinity]`,

`W_{infty,2} := H^1(Q_{infty,w},E)[2^infinity]`,

and

`K_2 := ker(W_2 -> W_{infty,2}^{Gamma_2})`.

By protected WP21's classical Kummer quotient lemma,

`W_2 ~= H^1(Q_2,A)/H^1_Kum(Q_2,A)`

and similarly at the infinite local field, with direct limits over finite layers.

Protected MATHFORGE commit

`e6f025896532021a84edf05b54034edc9834a022`

admits Ralph Greenberg's *Iwasawa Theory for Elliptic Curves*, arXiv `math/9809206v1`, for the exact primitive good-ordinary local-control interface recorded in

`sources/BSD-001/GREENBERG_P2_PRIMITIVE_LOCAL_CONTROL_SOURCE_AUDIT.md`.

The admitted source facts used below are exactly:

1. Greenberg's local quotient is
   `H_E(M_eta)=H^1(M_eta,E[p^infinity])/Im(kappa_eta)`,
   with `kappa_eta` the classical Kummer map;
2. at a good-ordinary place above `p`, Lemma 3.4 gives
   `#ker(r_{v_n})=#E_tilde(f_{v_n})_p^2`;
3. this statement applies literally at `p=2`;
4. Greenberg's proof measures the finite Kummer-versus-connected-ordinary discrepancy rather than assuming it away.

No other external theorem premise is used in WP23.

## 2. Concordance of the local quotient

### Lemma `BSD-A1-WP23-KUMMER-CONCORDANCE-001`

At `p=2`, Greenberg's local quotient `H_E(Q_2)` is canonically the same quotient as protected WP21's `W_2`, and the infinite-level quotient is canonically the same as `W_{infty,2}`.

Under these identifications, Greenberg's local restriction map is the restriction map used in protected WP21.

### Proof

Greenberg defines

`H_E(M_eta)
 := H^1(M_eta,E[2^infinity]) / Im(kappa_eta)`,

where `kappa_eta` is the classical local Kummer homomorphism

`E(M_eta) tensor Q_2/Z_2
 -> H^1(M_eta,E[2^infinity])`.

Protected WP21 derives from the same Kummer exact sequence the canonical quotient

`H^1(F,E[2^infinity]) / H^1_Kum(F,E[2^infinity])
 ~= H^1(F,E)[2^infinity]`.

The subgroup `H^1_Kum` is, by definition, the image of the same classical Kummer homomorphism. Hence the two quotients are canonically identical at every finite local layer.

Both constructions define the infinite-level local quotient by direct limit over the finite layers inside the cyclotomic extension. The identifications therefore commute with direct limits and with restriction. Thus Greenberg's restriction map and WP21's restriction map are the same map after the canonical Kummer identifications. QED.

### Important consequence

No equality between a finite classical Kummer condition and a Greenberg/connected-etale ordinary condition has been assumed. The admitted Greenberg source itself retains their exact finite discrepancy before proving the infinite-level comparison.

## 3. Kernel with or without explicit invariants

Greenberg writes the local restriction map into the infinite local quotient itself, whereas WP21 writes its target as `Gamma_2`-invariants.

### Lemma `BSD-A1-WP23-INVARIANTS-001`

The two maps have the same kernel.

### Proof

A cohomology class obtained by restriction from `Q_2` is fixed by `Gamma_2`. Hence the image of

`W_2 -> W_{infty,2}`

lies in

`W_{infty,2}^{Gamma_2}`.

Factoring the same restriction map through its invariant image changes only its codomain, not whether an element maps to zero. Therefore

`ker(W_2 -> W_{infty,2})
 = ker(W_2 -> W_{infty,2}^{Gamma_2})
 = K_2`. QED.

## 4. Exact order of `K_2`

### Theorem `BSD-A1-WP23-P2-ORDER-001`

For every curve in the protected selected good-ordinary branch,

`#K_2 = #E_tilde(F_2)[2^infinity]^2`.

### Proof

By Lemma `BSD-A1-WP23-KUMMER-CONCORDANCE-001` and Lemma `BSD-A1-WP23-INVARIANTS-001`, WP21's `K_2` is exactly the base-level kernel in the admitted Greenberg local-control theorem with

`F=Q`, `p=2`, `n=0`, `v=2`.

The cyclotomic `Z_2`-extension is totally ramified at `2`, so the residue field at the base local place is `F_2`. The admitted Greenberg Lemma 3.4 therefore gives

`#K_2 = #E_tilde(F_2)[2^infinity]^2`.

No passage from an odd-prime theorem is involved. QED.

## 5. Selected good-ordinary specialization

Protected WP07 proves

`a_2 in {+1,-1}`

and

`#E_tilde(F_2)=3-a_2`.

Since `3-a_2` equals either `2` or `4`, the full reduction group is `2`-primary. Thus:

### Corollary `BSD-A1-WP23-P2-LENGTH-001`

One has exactly

`#K_2=(3-a_2)^2`

and

`len_Z2(K_2^vee)=2 ord_2(3-a_2)`.

Equivalently,

- if `a_2=+1`, then `#K_2=4` and `len_Z2(K_2^vee)=2`;
- if `a_2=-1`, then `#K_2=16` and `len_Z2(K_2^vee)=4`.

### Proof

Substitute the protected WP07 identity

`#E_tilde(F_2)=3-a_2`

into Theorem `BSD-A1-WP23-P2-ORDER-001`. Pontryagin duality preserves the order of the finite group, and the `Z_2`-length of a finite `2`-primary module is the `2`-adic valuation of its order. QED.

### Corollary `BSD-A1-WP23-P2-FITTING-001`

`Fitt^0_Z2(K_2^vee)=(3-a_2)^2 Z_2`.

### Proof

For every finite `Z_2`-module `M`, the zeroth Fitting ideal is

`Fitt^0_Z2(M)=2^{len_Z2(M)} Z_2`.

Apply this to `M=K_2^vee` and use the preceding corollary. QED.

## 6. Exact relation to the protected WP07 unit-root correction

Let `alpha` be the `2`-adic unit root of

`X^2-a_2 X+2`.

Protected WP07 proves

`ord_2(1-alpha^(-1))=ord_2(3-a_2)`.

Hence:

### Corollary `BSD-A1-WP23-UNITROOT-LENGTH-001`

For the normalization in which the local interpolation multiplier is

`e_2(E)=(1-alpha^(-1))^2`,

one has the exact equality of integers

`len_Z2(K_2^vee)=ord_2(e_2(E))`.

### Proof

By protected WP07,

`ord_2(e_2(E))
 = 2 ord_2(1-alpha^(-1))
 = 2 ord_2(3-a_2)`.

Corollary `BSD-A1-WP23-P2-LENGTH-001` gives the same right-hand side for the local-control length. QED.

This is only a valuation identity between two already defined local quantities. It does not assert that the future D1c analytic determinant generator contains this multiplier, nor that any local-control factor cancels analytically without a source-bound determinant comparison.

## 7. Complete ambient finite local-control length

Protected WP22 proves:

- `K_ell=0` at every odd good-reduction prime;
- for every odd bad semistable prime `ell|N`, `K_ell` is finite and
  `len_Z2(K_ell^vee)=ord_2(c_ell)`;
- the real-place kernel is already zero by protected WP21.

Define

`K_bad := product_{ell|N} K_ell`.

Protected WP22 gives

`len_Z2(K_bad^vee)
 = sum_{ell|N} ord_2(c_ell)`.

After choosing the placewise representatives used in WP21, the ambient local kernel has no other nonzero `2`-primary component. Therefore

`K_loc = K_2 x K_bad`

as the **ambient local restriction kernel**.

### Theorem `BSD-A1-WP23-AMBIENT-TOTAL-001`

The full ambient primitive local-control kernel is finite and satisfies

`len_Z2(K_loc^vee)
 = 2 ord_2(3-a_2)
   + sum_{ell|N} ord_2(c_ell)`.

Moreover

`Fitt^0_Z2(K_loc^vee)
 = (3-a_2)^2
   2^{sum_{ell|N} ord_2(c_ell)} Z_2`.

### Proof

Use the direct product decomposition above, Corollary `BSD-A1-WP23-P2-LENGTH-001`, and protected WP22's exact total bad-prime length. Length is additive under finite direct products, and zeroth Fitting ideals multiply for finite direct sums over the PID `Z_2`. QED.

## 8. What this does and does not say about the actual control defect

Protected WP21 defines the actual primitive specialization defect by

`C_E := im(loc_Q) intersect K_loc`.

Since `K_loc` is now finite, WP23 immediately implies that `C_E` is finite. Thus the protected dual control sequence

`0 -> C_E^vee
   -> (X_infty)_Gamma
   -> X_E
   -> 0`

has a finite left-hand term.

But WP23 does not determine which elements of `K_loc` are globally realized. In particular, it does not prove

`C_E=K_loc`,

nor surjectivity of the projection of `C_E` onto any local factor.

The remaining D1b problem is therefore no longer an ambient local calculation. It is a pure global-local incidence problem.

### Refined D1b boundary

`MISSING_P2_GLOBAL_HIT_SUBGROUP_OF_LOCAL_CONTROL_KERNELS`.

A future tranche must determine

`C_E = im(loc_Q) intersect (K_2 x K_bad)`

exactly, most naturally through a Poitou-Tate/global-duality calculation that retains every `2`-power and uses the primitive Kummer local condition.

## 9. Claim firewall

WP23 proves only the exact local results above. It does not prove:

- `C_E=K_loc`;
- the order, length, or Fitting ideal of `C_E`;
- global localization surjectivity;
- equality of finite classical Kummer and ordinary/Greenberg local conditions by assumption;
- a primitive cyclotomic perfect determinant realization;
- a cyclotomic main conjecture at height one `(2)`;
- an analytic determinant generator or an analytic cancellation of `e_2(E)`;
- the WP20 Bockstein-to-WP00 regulator/period normalization;
- `delta_2(E)=len_Z2 Sha(E/Q)[2^infinity]`;
- `BSD-R2-A1`;
- any MATHCERT certification, novelty, priority, patentability, or commercial claim.
