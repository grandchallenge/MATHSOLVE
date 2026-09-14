# WP60F theorem — BSS literal-p=2 proof-boundary split

## 1. Protected setup

Let `E/Q` lie in the protected selected `BSD-R2-A1` class. Protected WP60A-A1 identifies determinant membership at the cyclotomic height-one prime `(2)` with the one-sided Fitting divisibility needed for R5.

Protected WP60E proves that the specifically screened finite-level Kato-derivative / determinantal / Fitting application theorems cannot be specialized to literal `p=2`.

Protected MATHFORGE WP60F at

`grandchallenge/MATHFORGE@eaaf7b8c660f3f07030608b3af1334ece5598586`

audits the underlying Burns–Sakamoto–Sano proof mechanism.

## 2. Admitted proof dependencies

The provider audit establishes the following source-level facts.

### 2.1 Simultaneous localization

BSS II Lemma 3.9 gives simultaneous nonzero localization of `s` primal and `t` dual classes only under

`s+t<p`.

At `p=2`, the case `s=t=1` is not covered.

### 2.2 Core-vertex connectivity

BSS II Lemma 5.15 uses

`2s<p`,

and Corollary 5.16 obtains the required core-vertex connectivity under `p>3`.

### 2.3 Kolyvagin-system and Fitting control

BSS II Theorems 5.20 and 5.2, and the Euler-system-to-Fitting consequence Corollary 6.15, are proved under `p>3` in the relevant interfaces. The proof uses the preceding core-vertex/localization mechanism.

### 2.4 Derivative construction is a distinct interface

BSS II Theorem 6.12 presents the higher derivative construction under its own hypotheses; the explicit `p>3` condition belongs to the later Fitting-control chain. The admitted source does not authorize identifying “a derivative can be formed” with “the integral Fitting containment holds.”

### 2.5 Elliptic H2/H3 verification

BSS III works under an odd-prime convention, and its elliptic application is in a `p>3` subsection. Lemma 6.17 verifies H2/H3 from a large `p`-adic image using `p>3` perfection of `SL_2(Z_p)` after restriction to the relevant pro-`p` extension.

The protected selected hypothesis of residual surjectivity

`G_Q -> GL_2(F_2)`

is not the same source hypothesis and does not, from the currently admitted interfaces, discharge H2/H3.

## 3. Barrier theorem

### Proposition `BSD-A1-WP60F-BSS-P2-BOUNDARY-001`

From the currently protected BSS interfaces, the finite-level BSS route cannot prove `R5-LIFT` for the selected literal-`p=2` class unless two logically distinct proof obligations are supplied or bypassed:

`F1 = MISSING_P2_CORE_VERTEX_SIMULTANEOUS_LOCALIZATION_FOR_BSS_FITTING_CONTROL`,

and

`F2 = MISSING_P2_ELLIPTIC_H2_H3_VERIFICATION_OVER_F2_INFINITY`.

In particular, repairing only F1 or only F2 is insufficient to derive the protected literal-`2` Fitting conclusion through the currently admitted BSS architecture.

### Proof

The Fitting-control conclusion used by the finite-level route factors through the BSS Kolyvagin-system control theorem. The admitted proof of that theorem uses the simultaneous-localization/core-vertex chain with numerical hypotheses excluding `p=2`. Therefore the Fitting-control step has an unresolved foundational literal-`2` obligation F1.

Independently, the elliptic application requires standard hypotheses H2/H3. The admitted verification of those hypotheses uses a `p>3` large-image/perfectness argument not supplied by the protected selected residual-surjectivity theorem. Therefore the selected elliptic specialization has an unresolved obligation F2.

Both layers are required by the currently admitted route. A proof of F2 does not provide the missing Fitting-control theorem; a proof of F1 does not verify the elliptic hypotheses. Hence both must be supplied, or the architecture must be bypassed by a theorem whose hypotheses and conclusion directly fit the protected selected lane. QED.

## 4. Exact route classification

Record

`BSS_LITERAL_P2_R5_ROUTE_REQUIRES_F1_AND_F2`.

This refines the WP60E subordinate boundary

`MISSING_LITERAL_P2_FINITE_LEVEL_KATO_DERIVATIVE_FITTING_THEOREM`.

It does not replace the parent obligations:

- `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`;
- `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.

## 5. Execution consequence

The next bounded theorem-construction lane is F1, because it is upstream of the Fitting conclusion independently of the elliptic H2/H3 question.

The exact F1 research question is:

> Can the BSS simultaneous-localization/core-vertex step be replaced at literal `p=2`, for the protected selected two-dimensional representation, by a theorem strong enough to recover the one-sided Fitting containment without assuming the desired containment?

A negative result must identify an actual mathematical obstruction, not merely the failure of the published `s+t<p` proof.

F2 remains a parallel lane:

> Determine the exact restricted `2`-adic image over the relevant `2`-power extension and prove or disprove the BSS H2/H3 conditions for the selected class without upgrading residual surjectivity by assertion.

## 6. Claim firewall

This proposition does not establish:

- nonexistence of a literal-`p=2` localization theorem;
- nonexistence of a literal-`p=2` Kolyvagin-system/Fitting theorem;
- failure of H2/H3 for every selected curve;
- a value of any Fitting exponent;
- `R5-LIFT`, `R5-PRIM`, D2d, or `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.
