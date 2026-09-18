# YM-D001-R002 — exact evidence audit

## 1. Governing evidence

This audit is bound to:

- MATH-PROGRAMME protected head `1f4ba5fabab01c084aefab201c5a4aa594d257fc`;
- `campaigns/yang_mills/WP02_THEOREM_LEDGER/02_THEOREM_LEDGER.json`;
- `campaigns/yang_mills/WP02_THEOREM_LEDGER/04_DEPENDENCY_DEBT_GATE.json` as historical debt evidence;
- `campaigns/yang_mills/YM_CURRENT_ROUTING_GATE.json` as the current routing authority;
- MATHFORGE protected head `267670385485b88be0556f6993dc171127139ae1`;
- `sources/YM-001/YM_WP02_SOURCE_LOCATOR_SCOPE_REVIEW.md`;
- Shen–Zhu–Zhu, CMP 400 (2023), DOI `10.1007/s00220-022-04609-1`, arXiv `2204.12737v1`.

The external primary-source inspection is corroborative. Protected Programme and Forge records remain the route and source-scope authority.

## 2. Current theorem records

### YM-T-010

Protected record:

- status: `THEOREM_REGULATED`;
- regulator: fixed lattice spacing;
- volume: finite lattice, with source extensions;
- conclusion: physical positivity of regulated Schwinger functions and a positive self-adjoint transfer matrix;
- composition: `COMPOSABLE_ONLY_AT_FIXED_REGULATOR`;
- boundary: the transfer matrix at fixed lattice spacing is not the continuum physical Hamiltonian.

### YM-T-030

Protected record:

- status: `THEOREM_REGULATED_STRONG_COUPLING`;
- regulator: fixed lattice spacing;
- volume: infinite lattice;
- coupling: explicit strong-coupling bounds;
- conclusion: unique infinite-volume measure, functional inequalities, exponential decay for a large observable class, and a positive lattice mass gap in the source sense;
- composition: `COMPOSABLE_FIXED_REGULATOR_ONLY`;
- boundary: no continuum-limit lower bound in physical units is supplied.

### YM-T-150

Protected route contract requires:

- volume-uniform regulated lower bound;
- cutoff-uniform physical scaling;
- generator convergence;
- spectral-exclusion stability;
- OS reconstruction.

R001 supplies only the abstract spectral-exclusion-stability implication once the other operator data are already present.

## 3. Primary-source facts for YM-SRC-010

The source defines a finite lattice with **unit lattice spacing** and periodic boundary conditions. The action is

`S(Q) = N beta Re sum_p Tr(Q_p)`.

Under Assumption 1.1, the allowed strong-coupling region is explicit. For `d=4`:

- `SU(N)`: `|beta| < 1/[16(d-1)] = 1/48`;
- `SO(N)`: `|beta| < (N-2)/[32(d-1)N] = (N-2)/(96N)`.

The source proves an infinite-volume measure and, in Corollary 1.6, exponential covariance decay for separated cylinder observables. The exponent multiplies lattice graph distance.

No theorem statement in the cited result introduces a physical lattice spacing `a`, a scale-setting map `s(a)`, a cutoff-indexed self-adjoint Hamiltonian `H_a`, cross-cutoff comparison maps, or strong-resolvent convergence as `a -> 0`.

## 4. Contract matching

| R001 application input | YM-T-010 | YM-T-030 | Current composition |
| --- | --- | --- | --- |
| Nonnegative self-adjoint generator at each cutoff | fixed-regulator transfer-matrix interface only | not the theorem object; covariance/measure result | not supplied as one common family |
| Explicit physical energy scaling | no | no; unit lattice spacing | missing |
| Cutoff index `a -> 0` | no | no theorem parameter; unit spacing | missing |
| Cross-regulator state-space comparison | no | no | missing |
| One physical `Delta > 0` uniform in cutoff and volume | no | lattice correlation exponent only | missing |
| Spectral exclusion `sigma(H_a) cap (0,Delta)=empty` | no current cross-regulator statement | no; correlation decay is proved | missing |
| Strong-resolvent convergence to target `H` | no | no | missing |
| Vacuum-sector control | no | no | missing if required |

The failure is not merely that a constant has not been estimated. The **operator family to which the constant would belong has not been supplied by the current evidence**.

## 5. Exact obstruction proof

Define an R001 application witness to be a tuple

`W = (a_n, H_n, J_n, H, Delta)`

where:

- `a_n -> 0` is the regulator sequence;
- each `H_n` is the physically normalized nonnegative self-adjoint regulated generator;
- `J_n` denotes the state-space identification/comparison data needed to put the resolvents in one comparison framework;
- `Delta > 0` is independent of `n`;
- the regulated spectral exclusion holds for all sufficiently large `n`;
- the identified negative-point resolvents converge strongly to the resolvent of `H`.

The protected conclusions of `YM-T-010` and `YM-T-030` do not contain values for `a_n`, the physical normalization of `H_n`, or `J_n`. `YM-T-030` additionally does not conclude the required spectral inclusion for a transfer generator.

Therefore no R001 application witness can be constructed **from the currently admitted theorem conclusions alone**.

This is a theorem-interface noncomposition result. It is not a claim that no future Yang-Mills construction can supply such a witness.

## 6. Secondary coupling-regime boundary

The source theorem is strong-coupling and its explicit `beta` domain is bounded near zero. The protected continuum route requires approach to the asymptotically free four-dimensional target.

No current evidence record gives a function `beta(a)` and scale setting for which:

1. `a -> 0`;
2. every sufficiently small `a` remains in the hypotheses of `YM-T-030`; and
3. the resulting family converges to the intended continuum theory.

The admissible statement is therefore `MISSING_TRAJECTORY_THEOREM`, not `PROVED_TRAJECTORY_IMPOSSIBLE`.

## 7. Consequence for the campaign

The abstract R001 theorem remains useful: once an actual physical regulated generator family with a common gap and strong-resolvent limit is constructed, the limiting spectral exclusion follows.

The current obstacle is earlier in the pipeline. D001 now needs a regulator-to-generator construction/interface, not another spectral-stability lemma.
