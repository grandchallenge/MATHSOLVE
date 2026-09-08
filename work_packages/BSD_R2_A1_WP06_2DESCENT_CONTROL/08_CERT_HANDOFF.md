# Certification boundary and future formalization handoff

## Current disposition

`BSD-R2-A1` remains unproved and the MATHCERT route remains pending. WP06 does not modify the existing certification packet.

## Theorem-grade candidates from WP06

A future formalization can independently encode:

1. the subgroup argument in `GL_2(F_2)` proving no quadratic 2-power torsion growth;
2. the inflation-restriction eigenspace isomorphisms;
3. the Kummer-diagram identification of local descent defects;
4. the exact integral involution sequence with `I_n` and `Q_n`;
5. the resulting finite-length identity.

The first and fourth items are especially suitable for kernel-checked formalization because they require no analytic library.

## Imported mathematics boundary

The all-`n` control theorem is proved in the package. External Kramer and Morgan-Paterson results are concordance only. Standard Galois cohomology and Kummer exactness are used transparently in the proofs rather than hidden behind a BSD theorem import.

## No certification inference

Passing repository CI, review, or formalizing an algebraic sublemma would not certify `BSD-R2-A1`. MATHCERT alone may render a certification disposition.