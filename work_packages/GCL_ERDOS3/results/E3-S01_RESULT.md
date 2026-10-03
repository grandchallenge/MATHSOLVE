# E3-S01 — exact source and formal-library interfaces

Disposition: **SOURCE_INTERFACE_FOUND**.

## 1. Exact F01 formal replay interface

Protected D5 artifact:

- repository: `grandchallenge/MATHSOLVE`
- path: `work_packages/OPENMATH_2026/OM26_H7_ERDOS_3/H7_D5.lean`
- Git blob: `530ee6d6651e90f683dd3e3d3abd2246f8aae6de`
- last content commit: `4d2f27f8c464f00a32361e98abab398f32b8df0d`
- pinned replay run: `36990793026`
- pinned replay job: `110786278497`
- image: `ghcr.io/ottogin/lean-mathlib@sha256:964547ad81e109c78545512867bae70b710c55d833078674878faad7de0ebb85`
- Lean: 4.33.1

The job compiled the exact D5 blob and printed only:

`[propext, Classical.choice, Quot.sound]`

for:
- `Erdos3.reciprocal_divergent_diff_finite`
- `Erdos3.reciprocal_divergent_tail`
- `Erdos3.reciprocal_divergent_zmod_fiber`

The current protected D5 blob is byte-identical to the compiled blob.

## 2. Pinned Mathlib interfaces already used by D5

Pinned Mathlib commit recorded by the H7 corpus:

`0df444a360eaa60ab8c11dca51a86af692955474`

Relevant source file:

`Mathlib/Analysis/SumOverResidueClass.lean`

Exact useful identifiers:
- `Finset.sum_indicator_mod`
- `summable_indicator_mod_iff_summable`
- `summable_indicator_mod_iff`
- `summable_subtype_iff_indicator`
- `Set.Finite.summable_compl_iff`

These are sufficient for the current D5 finite-deletion/residue-fibre formalization; no missing library theorem blocks F01.

## 3. Arithmetic-progression formal interface

Public Formal Conjectures source inspected at commit:

`df3f12d7bd06feb3f71ae37abae0ca7cb798d9b1`

Relevant file:

`FormalConjecturesForMathlib/Combinatorics/AP/Basic.lean`

Exact interfaces:
- `Set.IsAPOfLength`
- `Set.IsAPOfLengthFree`
- `Set.IsAPOfLengthFree.maxCard (k : ℕ) (N : ℕ) : ℕ`

The last identifier is the direct formal analogue of the extremal function (r_k(N)) used in B01.3. This provides a clean future Lean target for the dyadic threshold reduction.

The protected Erdős-3 target remains:

`work_packages/OPENMATH_2026/AUTHORITATIVE_SOURCE_POOL/erdos-3/PUBLIC_SOURCE/statement.lean`.

## 4. Quantitative three-term source interface

Primary mathematical source:

Thomas F. Bloom and Olof Sisask,
*Breaking the logarithmic barrier in Roth's theorem on arithmetic progressions*,
arXiv:2007.03528.

The source states that a three-term-progression-free subset of ({1,ldots,N}) has size

[
ll N/(log N)^{1+c}
]

for some absolute (c>0), and explicitly notes that this proves the first non-trivial case of Erdős's arithmetic-progression conjecture.

This estimate is exactly strong enough for B01.3 because the dyadic density envelope becomes (O(j^{-1-c})), which is summable.

A later stronger three-term bound is available in Bloom–Sisask, arXiv:2309.02353, but is not needed for the bridge.

## 5. k≥4 source boundary

The protected GCL source packet does not contain a theorem supplying a summable dyadic envelope for (r_k(2^j)/2^j) for every fixed (kge4). No absence claim beyond the scoped source pass is made.

Accordingly:

- F01 source state: **SOURCE_INTERFACE_FOUND / FORMALIZATION CLOSED**.
- B01 three-term instantiation: **SOURCE_INTERFACE_FOUND**.
- B01 k≥4 threshold: **SOURCE_BLOCKED AT A NAMED ESTIMATE**, not mathematically refuted.
