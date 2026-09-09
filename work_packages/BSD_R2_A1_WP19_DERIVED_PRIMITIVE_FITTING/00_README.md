# BSD-R2-A1-WP19 — derived primitive first-Fitting decision gate

## Purpose

WP19 executes the decision gate required after WP16-WP18.

WP18 proved that the fixed primitive normalization works exactly on representative curves in both WP13 local regimes. The remaining obstruction is therefore uniform theorem construction, not atlas repair.

WP19 makes one further representation improvement before that deep theorem:

`Fitt^0_{Z_2}(T_E)`

is replaced by the intrinsic rank-one ideal

`Fitt^1_{Z_2}(X_E)`.

The package proves exactly

`Fitt^1_{Z_2}(X_E)=Fitt^0_{Z_2}(T_E)`.

Thus the selected target is equivalent to

`delta_2(E)=v_2(Fitt^1_{Z_2}(X_E))`.

This removes the need for a future theorem to choose or quotient by a rank-one free generator merely to name the algebraic invariant.

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED` remains unchanged.

## Protected inputs

- MATHSOLVE protected baseline: `f7f88319550881a615edbea6d3425158d20136e7`.
- MATHFORGE protected post-WP18 source diagnosis: `0fe76d81147f34a814754bf09813b699e7bbf2e2`.
- WP16A: stabilized finite-level `2^n` Selmer length.
- WP16B: primitive Kummer dual `X_E`, finite torsion `T_E`, rank-one free quotient, and exact `Fitt^0(T_E)` realization.
- WP06: exact quadratic descent and split-local defect control.
- WP07: exact good-ordinary-at-2 acceptance surface and residual non-distinguished warning.
- WP09: all-`2N`-split auxiliary imaginary quadratic field and corrected p-adic Gross-Zagier applicability.
- WP13: exact Tamagawa/residual-conductor-drop dictionary.
- WP18A-C: exact diagnostic closure in regimes A and B.

## Post-WP18 source diagnosis

Protected MATHFORGE WP19 source audit:

`sources/BSD-001/P2_FINITE_PRIMITIVE_FITTING_WP19_SOURCE_AUDIT.md`.

Its bounded result is:

- Chan-Ho Kim's modern finite-layer anticyclotomic strong Fitting theorem has the right architecture, but is literally `p>=5` and assumes the residual ramification/Tamagawa-prime-to-`p` regime;
- Kurihara's strong Mazur-Tate/Fitting template is formulated for odd `p` and Tamagawa prime to `p`;
- Matsuno supplies genuine ordinary `p=2` Iwasawa variation, but the semistable theorem assumes the base `mu_2=0` statement that remains missing.

No theorem-nonexistence claim follows. The bounded source boundary is

`P2_RANK1_DERIVED_PRIMITIVE_MAZUR_TATE_FITTING_OR_BASE_MU_ZERO_CONTROL`.

## Decision-gate disposition

WP19 nominates the **direct-over-Q primitive first-Fitting route** as the final theorem-building lane.

Reason: this route can state the target natively in the exact protected Selmer structure and therefore avoids stacking independent comparison theorems that are required by the current cyclotomic or quadratic-base-change routes.

The final new theorem is named

`BSD-R2-A1-P2-RANK1-PRIMITIVE-FIRST-FITTING-RECIPROCITY`.

It must determine

`Fitt^1_{Z_2}(X_E)`

integrally from a rank-one analytic/Euler-system/determinant object whose exact `2`-adic valuation is the WP00 quantity `delta_2(E)`.

## What WP19 proves

1. `Fitt^1_{Z_2}(X_E)=Fitt^0_{Z_2}(T_E)`.
2. `v_2(Fitt^1_{Z_2}(X_E))=lim_n s_n(E)`.
3. `BSD-R2-A1` is equivalent to

   `delta_2(E)=v_2(Fitt^1_{Z_2}(X_E))`.

4. The direct primitive first-Fitting theorem is sufficient by itself, together with already-protected inputs, to close the selected mathematical target before certification.

## What WP19 does not prove

WP19 does not prove the new uniform first-Fitting reciprocity theorem. It does not extend an odd-prime theorem to `p=2`, prove base `mu_2=0`, identify Greenberg and Kummer local conditions, or invoke MATHCERT.

## Active substantive boundary

After this representation improvement, the exact boundary is

`MISSING_P2_RANK1_PRIMITIVE_FIRST_FITTING_RECIPROCITY_THEOREM`.

This is a genuine new integral `p=2` theorem problem unless a later exact source admission supplies it.
