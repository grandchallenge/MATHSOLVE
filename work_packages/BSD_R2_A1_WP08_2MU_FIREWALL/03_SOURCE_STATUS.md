# Source-status audit

## Governing status

MATHFORGE BSD provider coverage remains retrospective. Every item below is therefore `EXTERNAL_RECONNAISSANCE_UNADMITTED` in this tranche. The package's algebraic theorems do not depend on these sources.

Screen date: 2026-09-08.

## Kato 2004 — primary scope

Kazuya Kato, *p-adic Hodge theory and values of zeta functions of modular forms*, Asterisque 295 (2004), 117–290.

The current primary-source screen records:

1. the main-conjecture height-one formulation has an explicit p=2 caveat excluding a height-one prime containing `2`;
2. in the ordinary theorem, the characteristic-length inequality is asserted at height-one primes not containing `p`;
3. Kato's work still supplies Euler-system/cotorsion information at p=2 in appropriate formulations, so the correct disposition is not `KATO_UNAVAILABLE_AT_2`.

**Disposition:** `P2_EULER_SYSTEM_RELEVANT_BUT_INTEGRAL_(2)_COMPONENT_NOT_SUPPLIED_BY_SCREENED_STATEMENT`.

## Current mu=0 screen

A current search for a theorem forcing the cyclotomic algebraic mu invariant to vanish under the selected hypotheses did not locate a general result for the class

- non-CM `E/Q`;
- good ordinary at `2`;
- globally irreducible `E[2]`.

The newest p=2 mu result found in the screen, work announced by Zichao Lin with Mulun Yin in 2026, assumes reducible `E[2]` and adds reducibility of `E[4]` for its classification result. This is outside the selected class.

Historical formulations of Greenberg's mu-vanishing conjecture and subsequent ordinary results predominantly impose `p>2`; they therefore do not supply the selected theorem.

Hatley–Ray's good-ordinary-at-2 twist-family work treats mu hypotheses/invariants in a bounded family setting and does not state the uniform integral rank-one leading-term theorem required here.

**Disposition:** `NO_GENERAL_SELECTED_CLASS_MU_THEOREM_FOUND_IN_CURRENT_SCREEN`.

This is a search result, not a theorem that no such result exists.

## Heegner main-conjecture lane

Published non-CM Heegner-point main-conjecture results screened in the campaign impose `p>3` or `p>2`. Eisenstein-prime results likewise impose `p>2` and concern residually reducible representations. They do not instantiate the selected p=2 globally irreducible class.

**Disposition:** `CURRENT_SCREEN_DOES_NOT_CLOSE_P2_NONCM_ROUTE`.

## Quarantine rule

An unreviewed or non-authoritative manuscript claiming a full p=2 main conjecture by citing Kato cannot be promoted merely because it states the desired conclusion. It must reconcile, theorem by theorem, the primary Kato `(2)`-height restriction and the WP07 non-distinguished local representation. Until then it is not admissible theorem authority.

## Source admission trigger

A source should be sent through MATHFORGE admission only if its exact hypotheses survive all of the following:

- p=2 allowed integrally, not only after tensoring with Q_2;
- globally irreducible E[2] allowed;
- standard residual distinguishedness not required, or replaced by an exact p=2 control theorem;
- height-one `(2)` component controlled or explicitly bypassed;
- rank-one reciprocity/height normalization reaches the complex WP00 target.

Merely discussing p=2 is insufficient.