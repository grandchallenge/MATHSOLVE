# BSD-001 native continuation handoff

## Target repository and authority

- Target repository: `grandchallenge/MATHSOLVE`.
- Current ownership issue: `grandchallenge/MATHSOLVE#158`.
- Constitutional authority remains the protected GCL authority chain already bound by the campaign.
- Mathematical certification remains MATHCERT-only.

## Protected mathematical state before WP13

Historical WP00-WP04 remain Programme-owned. Protected native Solve work contains WP05-WP12.

Protected Solve baseline for WP13 is `a9a16da8b228ee6d472f11752cf6c3bc68fda864`.

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

Current protected provider identities remain:

- MATHFORGE `c44fef1d5d235b2e496bcee9ba0f7fc54212fa0d`;
- BSD provider manifest blob `0926dd22a3c5fe474cc21347994de99d1812ae8b`;
- MATH-PROGRAMME provider-import readback `563db2b177c791135d0a26fe76229c04793c742e`.

## Closed deductions through WP12

- WP05 removes the rational-torsion `ord_2` term.
- WP06 records every quadratic p=2 descent discrepancy exactly rather than dividing by `2`.
- WP07 proves the forced good-ordinary local-at-2 interpolation corrections and standard residual non-distinguishedness.
- WP08 isolates the cyclotomic height-one `(2)` / relative-mu defect.
- WP09 supplies the all-split auxiliary imaginary quadratic lane and corrected Disegni p-adic Gross-Zagier applicability at `p=2`.
- WP10 excludes mechanical specialization of the standard odd-prime Heegner-primitivity route.
- WP11 proves exact odd-degree `C3` Selmer/Sha control conditionally on that residual branch.
- WP12 eliminates the `C3` branch entirely under the selected local hypotheses. Thus irreducible `E[2]` automatically has image `GL_2(F_2) ~= S3` throughout the selected class.

## WP13 candidate result

`BSD-R2-A1-WP13-TAMAGAWA-INERTIA-DEPTH` makes every bad-prime 2-primary Tamagawa contribution explicit.

For each odd semistable bad prime `ell|N`, set `n_ell=ord_ell(Delta_min)`. WP13 proves:

1. for every `m>=1`, `I_ell` acts trivially on `E[2^m]` iff `2^m|n_ell`;
2. `E[2]` is unramified at `ell` iff `n_ell` is even;
3. `N(rho_bar_{E,2}) = product_{ell|N, n_ell odd} ell = product_{ell|N, c_ell odd} ell`;
4. `N/N(rho_bar_{E,2})` is exactly the product of bad primes with even Tamagawa number;
5. split multiplicative: `ord_2(c_ell)=v_2(n_ell)`, equal to the full 2-power inertia-triviality depth;
6. nonsplit multiplicative: `ord_2(c_ell)=min(1,v_2(n_ell))`.

This local theorem explains exactly why Chao Li's residual-conductor condition remains restrictive after WP12: it is equivalent to requiring every bad-prime Tamagawa number to be odd.

WP13 does not import an odd-prime Tamagawa-defect theorem at `p=2` and does not prove the selected leading-term identity.

## Current frontier after WP13

`BSD-R2-A1-S3-TAMAGAWA-SATURATED-LENGTH`.

A uniform solution must cover both:

- residual conductor unchanged / all bad `c_ell` odd; and
- residual conductor dropped / one or more even Tamagawa factors, with the exact local valuations from WP13 retained.

The desired global theorem must determine

`len_Z2 Sha(E/Q)[2^infinity] + sum_{ell|N} ord_2(c_ell)`

from

`ord_2(L'(E,1)/(Omega_E Reg_E))`

without an unspecified power of `2`.

The preferred next research move is an integral `p=2` saturation/primitivity or exact Selmer-length theorem whose local defect is exactly the WP13 Tamagawa data. Odd-prime Tamagawa-defect results are diagnostic only until a genuine `p=2` theorem is proved or admitted.

## Source boundary

Further exact p=2 primitivity, saturation, or direct arithmetic-length theorem premises require Forge admission or an explicit governed waiver unless proved in-package. WP13 itself is an in-package Tate/Kummer/component-group calculation.

External reconnaissance is diagnostic only; search failure is not proof of nonexistence.

## Certification boundary

MATHCERT remains pending. WP13 does not alter the certification packet.

## Stop conditions

Stop for target or hypothesis drift, reliance on an unadmitted theorem as a proof premise, a materially new integral p=2 arithmetic theorem not established in-package, or MATHCERT certification authority. Routine bounded proof, exact falsification, source admission, review, and protected integration remain delegated.