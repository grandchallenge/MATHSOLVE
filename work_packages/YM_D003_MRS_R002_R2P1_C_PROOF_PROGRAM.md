# YM-D003-MRS-R002-R2P1-C — native proof programme

Status: `ACTIVE__C0_FIRST`

Protected base: `grandchallenge/MATHSOLVE@1716d39a228e71b2b9f16f902dda32694d62557a`

Protected source authorities:
- `grandchallenge/MATHFORGE@90254084f3d06dcaad1a6a950039396ea85c23f9`
- `grandchallenge/MATHFORGE@9b6413a7ca5972b7d724ea8f1594c01b8f46cf45`

## Purpose

Turn the missing MRS-specific renormalized two-point theorem into a proof programme that can actually be executed without circularly assuming global polymer or Schwinger convergence.

The programme is finite-cutoff first. Every object is defined before any infinite sum or ultraviolet limit is invoked.

## C0 — exact renormalized two-point grammar

At fixed infrared regulator R, finite ultraviolet depth rho, and fixed decoupling history, define a finite combinatorial class of connected polymer/Mayer contributions with exactly two external gauge-field legs. The class must carry enough labels to record:
- scale and box support;
- horizontal and vertical decoupling links;
- background-dependent propagator insertions;
- gauge-restoring and ordinary local counterterm insertions;
- nested proper two-point subgraphs;
- the local quadratic A^2/2 projection.

A C0 object is admissible only if its 1PI predicate and subtraction forest are decidable at finite cutoff.

### C0 acceptance theorem

Prove that the class is closed under:
1. the horizontal/vertical decoupling operations used before renormalization;
2. Mayer hard-core removal;
3. contraction of a proper renormalized two-point subgraph to a local quadratic insertion;
4. extraction of the A^2/2 relevant projection;
5. composition with already-determined lower-scale counterterms.

No convergence estimate is needed for C0. Failure to obtain such closure must be returned as an exact structural obstruction.

## C1 — weakest useful norm

Only after C0 closes, define a rooted-polymer majorant. The norm must expose:
- root box;
- polymer size;
- link lengths/decay;
- scale labels;
- external-leg localization;
- one factor for the MRS anisotropic vertical expansion;
- one slot for the local relevant projection.

Do not choose exponents by analogy alone. Each weight must be tied either to MRS VII.1/power counting or to a native lemma.

## C2 — rooted link/tree summability

Use the MRS Section VII ingredients already admitted:
- strong sliced propagator decay;
- a small constant per box;
- horizontal-link decay;
- anisotropic vertical smallness/scale decay;
- irrelevance of >=5-leg vertices;
- parity pairing of the derivative trilinear vertex.

Target: a Kotecky-Preiss/tree-graph style rooted bound for the C1 majorant at finite cutoff, uniform in terminal rho.

## C3 — renormalized remainder scale gain

Prove that subtracting the local A^2/2 component from the two-point kernel leaves a remainder with the scale gain needed by the MRS induction. This is the step where a Taylor/localization operator must be specified exactly.

## C4 — mass response and simultaneous induction

Close the coupled recursion

two-point bound + running mass bound -> next-scale two-point bound + next-scale mass bound.

Derive bounded/Lipschitz or implicit-function nondegeneracy of the relevant coefficient with respect to the running quadratic counterterm. Then invoke the already-proved one-dimensional fixed-point gate.

## C5 — background/gauge/Section VI compatibility

Verify that the C0-C4 construction remains valid with the background-dependent propagator, gauge-restoring counterterms, and the Section VI quadratic normalization/stability interface.

## Anti-circularity firewall

Forbidden inputs:
- global MRS polymer convergence;
- existence of limiting Schwinger functions;
- Slavnov identities in the ultraviolet limit;
- infrared removal;
- OS reconstruction;
- mass gap.

Permitted inputs:
- finite-cutoff MRS identities and estimates from the protected source packet;
- FMRS1 as a proof-architecture template only;
- standard combinatorial/tree inequalities when all hypotheses are proved for the C0/C1 objects;
- native lemmas proved inside this programme.

## Immediate next action

Execute C0. Do not begin C1 by inventing a norm before the exact finite-cutoff object class and subtraction grammar are stable.

## Legitimate mathematical stop

A legitimate stop occurs only if C0 yields a precise structural obstruction, or later C1-C5 reduces to a named estimate whose proof requires new information not derivable from the admitted finite-cutoff MRS interfaces. “The source omits the theorem” is not by itself a stop.
