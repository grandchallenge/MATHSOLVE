# YM-D004-R001 — renormalized-observable interface gap

## Metadata

- Campaign: YM-001.
- Parent debt: YM-D004.
- Work package: YM-D004-OBSERVABLE-INTERFACE-GAP.
- Protected Solve baseline: f1716cde2477c0d11aa594f02e3e486cc116f854.
- Protected Programme authority: 7c8b351cc74bcb6ac2ccd4009eb6dff99913bc19.
- Programme theorem ledger: campaigns/yang_mills/WP02_THEOREM_LEDGER/02_THEOREM_LEDGER.json.
- Programme normalization authority: YM-WP00-source-normalization-equivalence-audit.md.
- Independent governing-source recheck: Jaffe–Witten, *Quantum Yang–Mills Theory*, official Clay problem description, section 4 and footnote 1, rechecked 2026-09-18.
- Certification: none; MATHCERT remains the sole certification authority.

## 18-field restricted-target contract

1. target_id: YM-D004-R001.
2. campaign: YM-001.
3. parent_debt: YM-D004.
4. repository: grandchallenge/MATHSOLVE.
5. solve_baseline: f1716cde2477c0d11aa594f02e3e486cc116f854.
6. programme_authority: 7c8b351cc74bcb6ac2ccd4009eb6dff99913bc19.
7. imported_source_authority: protected WP00 normalization audit plus the official Jaffe–Witten problem statement already normalized there.
8. mathematical_object: typed dependency interface between perturbative ultraviolet data, a continuum gauge-invariant observable hierarchy, and OS reconstruction.
9. dimension: four.
10. gauge_scope: the target compact simple gauge group G; this package does not construct any group-specific continuum theory.
11. regulator_volume_scope: no new regulator limit is asserted; the target bridge must eventually act on a selected regulated construction and its continuum limit.
12. imported_interfaces: YM-T-100 and YM-T-120 only, together with the WP00 local-observable and ultraviolet-concordance lock.
13. target_statement: determine whether YM-T-100 and YM-T-120, alone or sequentially, construct the renormalized local gauge-invariant curvature observables required by YM-D004; if not, identify the smallest missing theorem interface.
14. proof_method: exact interface typing, hypothesis/conclusion matching, governing-source requirement matching, and false-proof fixtures.
15. falsification_condition: a protected theorem already constructing renormalized local quantum operators from a regulated gauge-invariant observable family and proving the required short-distance perturbative normalization would falsify the claimed missing-interface diagnosis.
16. success_criterion: a proved noncomposition/dependency theorem and an explicit successor contract for the regulated-to-renormalized local-observable map.
17. forbidden_promotions: continuum Yang-Mills existence, construction of local quantum fields, complete OS reconstruction, ultraviolet concordance, physical scale setting, mass gap, confinement, novelty, priority, or certification.
18. successor_boundary: YM-D004-R002 — REGULATED_TO_RENORMALIZED_LOCAL_OBSERVABLE_CONSTRUCTION; no free-standing mechanism or numerical work.

## Governing requirement

The official problem statement requires a four-dimensional QFT with local quantum field operators corresponding, after the usual renormalization subtleties, to gauge-invariant local curvature polynomials and covariant derivatives. Their correlations must have the prescribed short-distance relation to asymptotic freedom and perturbative renormalization. The same source explicitly warns that quantization does not give a natural one-to-one map from classical differential polynomials to quantum operators because renormalization intervenes.

This is stronger than either of the currently protected interfaces supplies.

## Imported interfaces

### YM-T-100 — perturbative asymptotic freedom

Protected output:

- the leading beta function has the asymptotic-freedom sign within perturbation theory and the stated renormalization convention.

Protected exclusions include:

- no nonperturbative measure;
- no construction of a continuum observable hierarchy;
- no infrared gap.

### YM-T-120 — Osterwalder–Schrader reconstruction interface

Protected input hypotheses include:

- a continuum Schwinger hierarchy;
- a physical gauge-invariant observable hierarchy;
- Euclidean covariance, symmetry, reflection positivity, regularity/growth, and cluster/vacuum conditions.

Protected output:

- conditional reconstruction of a positive Hilbert-space QFT with translations and Hamiltonian.

Therefore the physical observable hierarchy is an input to YM-T-120, not an output manufactured by it.

## Result

YM-T-100 and YM-T-120 do not compose into a construction of the D004 observable family.

YM-T-100 supplies perturbative ultraviolet running but no map from regulated gauge-invariant observables to renormalized local quantum operator-valued distributions. YM-T-120 can reconstruct a physical theory only after the relevant continuum observable hierarchy and the rest of the selected OS profile have already been proved.

Consequently, using YM-T-120 to justify existence of the local observable hierarchy that YM-T-120 itself assumes is circular. Using YM-T-100 to fill that gap is also invalid because a beta-function theorem does not construct the nonperturbative operator family or prove convergence of its correlations.

## Smallest residual theorem object

The next D004 theorem object is not “prove asymptotic freedom again” and not “apply OS reconstruction.”

It is a construction/identification theorem for a selected regulated route. At minimum it must provide a family of regulated gauge-invariant observables and a renormalization/mixing prescription whose continuum correlations:

1. exist as local distributions on the same limiting four-dimensional theory;
2. remain gauge invariant in the admitted physical sense;
3. are identified with the intended curvature-polynomial operator classes after renormalization;
4. are nontrivial and mutually consistent across insertions;
5. satisfy the required short-distance normalization/asymptotic relation to the perturbative interface.

The theorem may realize this contract by any mathematically valid route; this package does not prescribe a regulator, renormalization scheme, or operator basis.

## Dependency consequence

D004 is therefore not discharged by the already protected pair T-100/T-120. The debt has been sharpened from a broad semantic-correspondence obligation to an explicit missing morphism:

`regulated gauge-invariant observables -> renormalized local continuum operator hierarchy`

together with its short-distance normalization theorem.

That bridge must be proved in the same selected continuum construction; it cannot be borrowed from an unrelated regulator without a comparison theorem.

## Claim boundary

This package proves only the dependency/noncomposition statement over protected interfaces.

It does not construct the missing observable map, establish a continuum Yang-Mills theory, prove the OS profile, prove asymptotic concordance for nonperturbative correlations, or prove a mass gap.
