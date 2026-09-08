# BSD-001 native continuation handoff

## Target repository and authority

- Target repository: `grandchallenge/MATHSOLVE`.
- Current ownership issue: `grandchallenge/MATHSOLVE#150`.
- Constitutional authority remains the protected GCL authority chain already bound by the campaign.
- Mathematical certification remains MATHCERT-only.

## Protected mathematical state before WP10

Historical WP00-WP04 remain Programme-owned. Protected native Solve work contains:

- `BSD-R2-A1-WP05-SOURCE-INTERFACE-001`: exact target reconstruction and torsion-valuation removal;
- `BSD-R2-A1-WP06-2DESCENT-CONTROL`: exact integral quadratic `2^n` Selmer restriction/corestriction control;
- `BSD-R2-A1-WP07-2RECIPROCITY-LENGTH`: forced local-at-2 corrections and non-distinguished route audit;
- `BSD-R2-A1-WP08-2MU-FIREWALL`: exact height-one `(2)` / Iwasawa-mu defect theorem;
- `BSD-R2-A1-WP09-DISEGNI-APPLICABILITY`: auxiliary-`K` existence and corrected Disegni p-adic Gross-Zagier applicability at `p=2`.

Protected Solve baseline for this candidate is `561ad590c45e0a4916c1b2bbb658c0ba2aed9fb8`.

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

## Protected provider authority

Current protected source identities are:

- MATHFORGE `c44fef1d5d235b2e496bcee9ba0f7fc54212fa0d`;
- BSD provider manifest blob `0926dd22a3c5fe474cc21347994de99d1812ae8b`;
- MATH-PROGRAMME provider-import readback `563db2b177c791135d0a26fe76229c04793c742e`.

Qualified native Forge audits now cover:

1. corrected Disegni p-adic Gross-Zagier at `p=2`;
2. Friedberg-Hoffstein prescribed-local auxiliary quadratic nonvanishing;
3. the bounded p=2 Heegner-primitivity route barrier in `sources/BSD-001/HEEGNER_PRIMITIVITY_P2_BARRIER_SOURCE_AUDIT.md`, blob `1b9f156447ff2bc87dfd08f413f7d22d31f5b66a`.

## Closed deductions

WP05 removes the rational-torsion `ord_2` term.

WP06 shows quadratic descent loses no unrecorded power of `2`; every discrepancy is an explicit exponent-2 defect group. For the all-split WP09 auxiliary field, local defects at `2` and every `ell|N` vanish, but the global and remaining nonsplit-place defect terms are not declared zero without proof.

WP07 proves good ordinary at `2` forces `a_2=+/-1`, computes `ord_2(1-alpha^(-1))=ord_2(3-a_2)`, and proves standard residual 2-distinguishedness is impossible.

WP08 proves that equality of cyclotomic height-one data away from `(2)` leaves exactly a relative factor `2^delta`; for characteristic elements this is the relative mu exponent.

WP09 proves existence of a suitable all-split auxiliary `K=Q(sqrt(D))`, analytic rank one over `K`, and applicability of corrected Disegni Theorem B at `p=2`. It supplies an exact source-normalized p-adic height / p-adic-L-derivative identity, not the WP00 complex leading-term identity.

## WP10 candidate result

`BSD-R2-A1-WP10-P2-HEEGNER-BARRIER` establishes, subject to ordinary protected Solve review and merge:

1. the standard odd-prime chain `rank lowering -> primitive Heegner Kolyvagin system -> sharp Sha/index equality` cannot be mechanically specialized to `p=2` from the admitted source interfaces;
2. this is a route obstruction, not a general no-go theorem for p=2 Heegner/Kolyvagin methods;
3. irreducible `E[2]` forces the residual image to be either `C_3` or `GL_2(F_2) ~= S_3`; Chao Li's admitted obstruction concerns only a stronger surjective `S_3` subcase with additional local hypotheses;
4. an exact Heegner-index theorem over the WP09 auxiliary field `K` would still not isolate the target over `Q`, because WP06 exposes the exact rank-zero twist `E^D` contribution and finite descent defects;
5. analytically the same cost is visible in `L'(E/K,1)=L'(E,1)L(E^D,1)`, so the rank-zero twist factor cannot be discarded at `2` without an exact theorem.

## Current frontier

`BSD-R2-A1-2PRIMARY-DIRECT-LENGTH`.

The preferred next theorem is a direct integral result over `Q` determining

`len_Z2 Sha(E/Q)[2^infinity] + sum_{ell|N} ord_2(c_ell)`

from

`ord_2(L'(E,1)/(Omega_E Reg_E))`

with every 2-primary correction explicit. A theorem only after inverting `2`, only up to a 2-adic unit, or only up to an unspecified power of `2` is insufficient.

A uniform proof must cover both irreducible residual-image branches `C_3` and `S_3`, or provide separate exact results whose union covers them.

An auxiliary-`K` alternative remains admissible only if it also computes the exact rank-zero twist contribution, all surviving WP06 defects, and the complete WP00 normalization ledger. The Iwasawa alternative remains separate and still owes both WP08 relative-mu control and WP09 p-adic-to-complex normalization.

## Source boundary

Further exact p=2 primitivity, Heegner-index, rank-zero-twist, complex Gross-Zagier normalization, or direct arithmetic-length theorem premises require Forge admission or an explicit governed waiver unless proved in-package.

External reconnaissance is diagnostic only. Search failure is not proof of nonexistence.

## Certification boundary

MATHCERT remains pending. WP10 does not alter the certification packet.

## Stop conditions

Stop for target or hypothesis drift, reliance on an unadmitted theorem as a proof premise, a materially new integral p=2 arithmetic theorem not established in-package, or MATHCERT certification authority. Routine bounded proof, exact falsification, source admission, review, and protected integration remain delegated.
