# BSD-R2-A1 WP41A — Bockstein versus dual-hit compatibility over `K`

## State

`PROVED_DEPENDENCY_SEPARATION`

Protected predecessor:

`grandchallenge/MATHSOLVE@af41471670639648db0aa96ed493333d2bf1536e` — WP40.

No new external theorem premise is used.

## Purpose

WP40 replaces the compact Greenberg-to-Kummer global-hit problem by the exact finite dual hit

`D_K subset R_K^dual`

with

`ann(J_K)=D_K`

and

`len J_K + len D_K = len R_K`.

WP37 independently constructs the first cyclotomic Bockstein and Nekovar height on the source-compatible strict Selmer complex over `K`.

WP41A determines whether the currently protected chain already identifies these two defects.

## Result

It does not.

The protected constructions vary different data:

- WP37 fixes the strict/ordinary Selmer structure and differentiates it in the cyclotomic augmentation direction;
- WP39-WP40 fix the base field and augmentation level and compare two different local conditions, strict Greenberg versus classical Kummer.

No protected theorem supplies a natural Iwasawa-level comparison triangle between those two Selmer structures whose augmentation is WP39's finite quotient and whose connecting morphisms commute with the WP37 Bockstein.

Therefore no equality between `D_K` and a Bockstein image, radical, kernel, or cokernel is presently justified.

This is a bounded dependency conclusion, not a theorem-nonexistence claim.

## Refined boundary

The live bridge is

`MISSING_P2_IWASAWA_STRICT_KUMMER_BOCKSTEIN_COMPATIBILITY_OVER_K`.

A successor must construct or source-qualify the missing comparison object before identifying `D_K` with a Bockstein/height defect.

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.