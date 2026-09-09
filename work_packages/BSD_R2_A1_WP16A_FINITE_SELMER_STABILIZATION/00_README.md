# BSD-R2-A1-WP16A — finite-level `2^n`-Selmer stabilization

## Metadata

- Campaign: `BSD-001`.
- Work package: `BSD-R2-A1-WP16A-FINITE-SELMER-STABILIZATION`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Protected Solve baseline: `93b1348d5e4ae77ededd0b5b779780112876c3d8`.
- Protected Forge provider baseline: `118ae1b5c2fc2630f53000921b742c610c50db16`.
- Parent frontier: `BSD-R2-A1-S3-UNSQUARED-P2-LENGTH-CONTROL`.
- Parent boundary: `MISSING_UNIFORM_UNSQUARED_P2_LENGTH_CONTROL`.
- Selected claim: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.
- Certification: none; MATHCERT remains the only certification authority.

## Purpose

Replace the finite `2`-primary Tate-Shafarevich length by an exactly equivalent stabilized finite-level Selmer quantity before choosing any integral Selmer-complex, determinant-line, or Fitting-ideal formalism.

For `n >= 1`, define

` s_n(E) := ord_2 #Sel_{2^n}(E/Q) - n. `

WP16A proves, without using the BSD leading-term formula,

` s_n(E) = ord_2 #Sha(E/Q)[2^n], `

that this sequence is eventually constant, and that

` lim_n s_n(E) = len_Z2 Sha(E/Q)[2^infinity]. `

Consequently the selected unresolved equality is equivalent to

` delta_2(E) = lim_n s_n(E). `

## Material inputs

This package uses only:

1. the protected WP05 rank-one interface;
2. the protected WP05 proof that `#E(Q)_tors` is odd;
3. the protected WP05 finiteness of `Sha(E/Q)` under the selected analytic-rank-one interface;
4. the standard Kummer exact sequence recorded in the protected WP16 plan,

   `0 -> E(Q)/2^n E(Q) -> Sel_{2^n}(E/Q) -> Sha(E/Q)[2^n] -> 0`;

5. elementary finitely generated and finite abelian group algebra proved in `01_FINITE_LEVEL_STABILIZATION_THEOREM.md`.

No new external theorem premise is introduced in this tranche. The current protected MATHFORGE BSD provider manifest and admitted source audits were read before theorem mutation; their claim boundaries are unchanged.

## What is proved

- the Mordell-Weil quotient has exact order `2^n`;
- the Kummer exact sequence therefore gives the exact finite-level cardinality identity

  `#Sel_{2^n}(E/Q) = 2^n #Sha(E/Q)[2^n]`;

- taking `ord_2` gives the requested identity for `s_n(E)`;
- finiteness of Sha implies `Sha(E/Q)[2^n]` eventually equals the full `2`-primary subgroup;
- for a finite `Z_2`-module, `len_Z2` equals `ord_2` of its cardinality;
- hence `s_n(E)` stabilizes exactly to the full `2`-primary Sha length;
- the selected target is exactly reformulated as `delta_2(E) = lim_n s_n(E)`.

## What is not proved

WP16A does not prove `BSD-R2-A1`, an integral main conjecture, an Euler-system or Kolyvagin-system primitivity theorem, a determinant/Fitting equality, an explicit reciprocity law, numerical stabilization for any particular curve, novelty, priority, or MATHCERT certification.

It also deliberately does **not** choose the Selmer-complex formalism for WP16B.

## Successor

The next substantive tranche is WP16B: identify a precise integral Selmer object whose determinant/Fitting/torsion invariant realizes the stabilized length, with every local condition and `2`-power correction explicit.