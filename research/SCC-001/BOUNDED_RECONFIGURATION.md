# SCC-001: bounded-weight partition reconfiguration and gate lifting

Status: exploratory author-derived mathematics and exact finite replay; no independent certification, Lean proof or novelty claim. Continues SUPPORT_INCIDENCE.md (#1325, protected c57abd46bb8dc55b359033cfe64e5a553e50ddb4), which already established strict nonminimum compression in a reachable state and rank-two joint gate feasibility. No multi-output demand, restricted circuit model or reflection premise.

## 1. Reconfiguration model

Use the augmented Boolean cube with n input coordinates and marker y, D=n+1, W=V+span(y), and distinct nonzero atom dictionary A. A representation is a subset S of A, with evaluation XOR(S) and weight |S|. A partition move toggles the three distinct atom coordinates {a,az,a(1+z)} for z in W if both children are nonzero. This is addition of a partition syzygy in the coefficient space, even if some of its terms are already present or absent: cancellations are XOR, not multiset union. Every such move preserves evaluation. Zero-child moves are identities and omitted. Coordinate partitions alone generate the entire kernel (COHERENT_MATCHING.md).

For same-evaluation endpoints S,T let H_W(S,T) be the minimum over finite move paths of their maximum weight (including endpoints); set M=max(|S|,|T|). For S=T height is M. The barrier H-M is nonnegative. These are costs of the auxiliary representation geometry, NOT directly the workspace of a SAT algorithm. Only fixed old endpoints are compared under gates below.

## 2. Depth-first common-refinement theorem

For all W, S,T of equal evaluation,
    M <= H_W(S,T) <= (D+1) M.
A path using only augmented coordinate partitions exists with at most (2^D-1)(|S|+|T|) moves. The upper bound may be exponentially long; no polynomial-time algorithm in n or original circuit size is claimed.

Proof: work recursively on cells defined by prefixes of the D coordinates. Restriction of a representation to a cell means replace each atom by its intersection with that cell, discard zeros and cancel duplicates. It cannot increase weight. At a leaf singleton cell the two restricted representations are equal: only the singleton atom can be nonzero and their evaluations coincide.

At an internal cell C with source S_C and destination T_C, split each source atom by the next coordinate, one partition relation at a time. The result is S_0 XOR S_1, where S_i is the restriction to child i. Intermediate weight is at most 2|S_C|: express it as the XOR of the unprocessed source atoms and the at most two children of each processed source atom. This accounting remains valid even if a processed or unprocessed term cancels against a previous one. Recursively change S_0 into T_0 while holding S_1 fixed; then change S_1 into T_1 while holding T_0 fixed. Reverse the analogous destination splitting to obtain T_C. Different cells have disjoint nonempty supports, so their representation weights add and moves in one cell do not affect the other. Induct on remaining depth d: at a leaf the bound is M, and splitting/merging uses at most 2M; a child recursion uses at most d M while the fixed sibling uses at most M. Thus maximum <=(d+1)M for d>=1. Each internal cell performs at most |S|+|T| splitting/merging moves, giving the length bound. Every intermediate has the original target evaluation, with unchanged representations in all other cells. The proof permits arbitrary available nonlinear functions in W, not just initial affine states.

In particular, for nonempty endpoints, normalized height H/M <= n+2 and normalized excess (H-M)/M <= n+1. Any claimed superpolynomial obstruction from these normalized quantities alone is impossible. Absolute excess may be large when the endpoints themselves are huge; this result does not bound it polynomially in n alone.

## 3. Exact spectator invariance for fixed endpoints

Extend the input with independent unused coordinates z_j and W with their affine span; lift S,T cylindrically. Any old path lifts with unchanged weights. Conversely restrict every atom of a padded path to z=0, cancel duplicates, discard zeros. Restriction is linear on coefficient vectors when the target dictionary identifies identical nonzero functions. Each padded partition move restricts either to the zero relation or to one valid old partition triple: its two children remain disjoint, and if both are nonzero they partition the parent by a restricted form in W. Weight does not increase. Delete identity moves. Thus the two heights are equal. This is a fixed-endpoint theorem; it makes no claim about an optimization over all new padded minimum representations.

## 4. Three-cell gate path-lifting theorem

Let g=uv, u,v in V, W'=W+span(g), and keep endpoints S,T in the old dictionary. Then
    H_W'(S,T) <= H_W(S,T) <= 3 H_W'(S,T).

First inequality follows from inclusion of moves. For the reverse, partition the augmented cube into disjoint old atom cells
    C0=1+u, C1=u(1+v), C2=uv.
Zero cells may be omitted. On each cell g is constant (0,0,1). For any successor atom b, b restricted to C_i is an old atom or zero: every factor of b is w+alpha*g, whose restriction is an old form with a constant correction, multiplied by the old atom C_i.

Define a coefficient map L by replacing each b by the XOR of its three cell restrictions, dropping zeros and cancelling equal atoms. This linear map preserves evaluation and |L R|<=3|R|. A successor partition triple based on z'=w+alpha*g restricts on each cell either to zero or to one valid old partition move based on w+alpha*g(C_i). Hence each step R->R' lifts to at most three old moves from LR to LR'. The moves have mutually disjoint cell supports. Perform the moves that decrease weight before those that increase it (each move affects only its own cell); intermediate weight never exceeds max(|LR|,|LR'|). Thus a successor path of height K lifts to a path of height <=3K.

Connect S to LS using old partitions: split by u, then split the u=1 branch by v. The same source-atom accounting as section 2 bounds width by 3|S| throughout: after splitting, each original atom contributes at most three pieces. This includes cancellations, zero cells and redundant g. Likewise connect LT back to T. Concatenate to prove the bound. Length at most 2(|S|+|T|)+3 times the successor path length.

For fixed nonempty endpoints, log2(H/M) is spectator invariant, nonincreasing under every charged gate and decreases by at most log2(3); its total initial value is at most log2(n+2). It need not vanish on target completion for arbitrary fixed endpoints. It is a gate-stable reconfiguration observable, not a new unrestricted lower bound. This theorem does not control changing endpoints, the number of path components at a given absolute threshold, or the minimal path length at fixed height.

## 5. Exact two-input barrier and completion failure

Use index i=a+2b for the two input bits, and low/high four bits for marker y=0/1. At the initial affine state V, f=ab has mask 0x8 and marked graph h=0x87. Take S={0x03,0x84}, T={0x05,0x82}. Both are minimum two-atom representations: h is not itself an old atom. Enumerate all 51 nonzero atoms and all 77 nontrivial partition triples, including partitions by every available affine form, not just coordinates. Exhaustive BFS from S at height three yields a component of 9 representations, excluding T. At height four it yields a component of 826, including T. One explicit path is
    {03,84} -> {01,02,84} -> {01,80,82,84}
            -> {01,04,82} -> {05,82}.
Every number is hexadecimal, each symmetric difference a valid partition triple. Thus H_V(S,T)=4. After the legal gate ab, H_V'(S,T)=2; one can pass through the one-atom representation {87}.

But fixed endpoints do not necessarily lose their barrier at target completion. Keep S and take U={0x0f,0x88}, another old minimum representation. After adjoining ab, h belongs to W' and rho=1. Yet U is outside S's height-two component, and the following height-three path exists:
    {03,84} -> {87} -> {07,80} -> {08,80,0f} -> {88,0f}.
Hence H_V'(S,U)=3 while M=2. This is an exact completion counterexample for fixed-endpoint normalized and absolute excess barriers. It does not disprove every endpoint-selection rule or reconfiguration invariant.

Complete census: on two inputs all eight nonaffine targets have seven two-atom marked minima each. The 168 unordered distinct-minimum pairs all have initial height four. After adjoining ab (which makes every unmarked two-input function available), 24 pairs have height two and 144 have height three. This is a bounded exact census, not an asymptotic frequency claim.

## 6. Verification and implications

Run python3 research/SCC-001/bounded_reconfiguration_replay.py. Deterministic seeded replay builds explicit depth-first paths for equal-evaluation endpoints and lifts arbitrary successor paths with successor-only partition moves. It independently checks all intermediate atoms, evaluations, partition moves, height and length bounds. Also checks padded partition retractions and the exact two-input BFS census. The old endpoints are kept fixed in every gate comparison. No assumption of optimal-only transport; strict nonminimum compression from #1325 remains in force.

The new result gives a concrete gate-coherent transport bound on an entire nonlinear representation space. However, H/M is bounded by n+2 and fixed-endpoint excess fails completion even on AND. Thus neither normalized height nor the raw fixed-endpoint barrier is a satisfactory SCC demand potential. The next viable task is to investigate path length or gate-labeled compatibility of representation changes, with a target-completing endpoint rule and a universal amortized estimate that does not identify an arbitrary auxiliary reconfiguration with actual computational necessity. Any such candidate must survive MOD3, spectator invariance, arbitrary reuse and the new completion counterexample. No superpolynomial unrestricted SAT lower bound or P/NP claim.

Boundary: RECONFIGURATION_HEIGHT_TRANSPORT_EXACT__NORMALIZED_HEIGHT_POLYNOMIALLY_BOUNDED__FIXED_ENDPOINT_COMPLETION_FAILS__TARGET_COHERENT_PATH_CAPACITY_OPEN.
