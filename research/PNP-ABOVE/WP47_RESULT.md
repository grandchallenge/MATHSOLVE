# WP47 — Charged interface information and conditional decomposition

Protected WP45 e24feab62c7b86851b1d1ed157c40b2292494359 and WP46
e43add65649526c75f588e7d33568a0a8c6acf4b. Pinned upstream
MIPRE-formalization 5926bdff5db621f44682a101007ef2fe3ae8d970,
Lean 4.35.0-rc3.

## Mathematical target

Let V and W be fixed native polynomial component and joint verifiers.
A boundary b is a bit string, not a free oracle. Fixed polynomial
D(b,x) yields a list of conditioned subinstances of the joint input x;
fixed polynomial J((b,x),ws) assembles their accepted witnesses.
Require that for every b,x and every accepted aligned local witness list,
J returns a witness accepted by W for the original x. Wrong boundaries
need not possess local witnesses; the lifting premise must not be
asserted merely because each region is satisfiable separately.

If every conditioned component has a successful program of weighted
score at most B, WP46 yields a joint successful program on (b,x) with
score at most q(B+esize(b)+esize(x)+1) for one fixed polynomial q.
Hardcoding b by the upstream scoped s-m-n construction incurs exactly
esize(b)+35 nodes of extra program description and linear input copying.
The original joint input x therefore has a successful program of score
at most

    2^(esize(b)+35)*(esize(b)+esize(x)+4)*
        q(B+esize(b)+esize(x)+1).

Since esize(b)<=4*length(b)+1, the description multiplier is bounded by
2^36*(2^length(b))^4. Input and witness encodings, clock conversion,
and reassembly are accounted for. No computation of the boundary
is assumed: the description multiplier pays for it.

If a scoped program c instead produces b from x at cost s, replace the
literal advice factor with 2^(esize(c)+21)*(s+esize(x)+4). In particular
a fixed polynomial-time boundary constructor need not output a short
boundary. It can be incorporated into the decomposition and assembler.

## Consequence

If, for every witness-bearing x, there exists a boundary b with
2^length(b)<=r(esize(x)) and all conditioned components have weighted
score at most p(esize(x)), for fixed natural-coefficient polynomials p,r,
the native joint witness problem has one total polynomial solver.
WP45 removes the need to know the good boundary in advance. A polynomial
upper bound is explicitly obtained by composing q with p+4r+X+2 and
multiplying by 2^36*r^4*(4r+X+5).

Thus logarithmically many coordination bits, with polynomially cheap
conditioned components and efficient verified lifting, cannot yield
superpolynomial weighted capacity. The pointwise contrapositive says
that whenever the joint score exceeds the displayed assembly allowance,
at least one conditioned component exceeds budget B for that boundary.

## Scope and limitations

This is an upper-bound argument and a necessary condition for hardness,
not a sufficient lower-bound mechanism. A large syntactic separator
can contain highly redundant or easily computable information; its
length does not lower-bound computational difficulty. Likewise lack of
the specified decomposition or witness assembler does not prove hardness.
A pairwise consistency counterexample (x=y, y=z, x!=z) demonstrates why
local nonemptiness and pairwise compatibility are not the lifting
condition. For genuine SAT use, the split must expose all shared variables
(or another sufficient interface), enforce the boundary consistently,
and preserve the original witness encoding. A specific native SAT
splitter and a lower bound for arbitrary computational shortcuts are
not asserted. No P versus NP resolution or independent certification.

## Verification

Independent finite checks passed: 131072 conditioned formula pairs and
the pairwise consistency counterexample. These test exact gluing of
small truth tables, not asymptotic hardness. The prior Colab runtime expired and its replacement compiler download stalled. The managed CHAD workspace was expanded, the pinned toolchain and dependency import cache recovered, and the missing Halting.Serial module compiled from pinned source. No HDD compilation fallback was used.

## Strengthened generated-interface bound

Let a scoped program c actually compute the suitable boundary b from x
at cost s with weighted score 2^esize(c)*(s+1)<=C. Its output size is at
most s, by the native execution size bound. Combining the charged
computed-boundary discharge with WP46 gives a single fixed polynomial q
such that the original joint score is at most

    2^21*(esize(x)+4)*C*q(B+C+esize(x)+1).

This yields a stronger consequence than a fixed polynomial boundary
constructor: if each witness-bearing x merely has some such successful
boundary producer of polynomial weighted score, and its conditioned
components have polynomial weighted score, the whole relation has one
uniform polynomial witness solver. The producing programs may vary
with x, and the good boundary need not have logarithmic length.
No circular assumption that an efficient boundary solver is known.
This remains an upper-bound criterion; it supplies no lower bound
on finding a suitable boundary for a concrete hard family.


## Exact verification receipt, 2026-11-28

Candidate 1a12a19cf40dcbcb5d92ab5f14637e7e57c5057f.
All eleven WP47 declarations and the standard-axiom audit passed.
Freshly rebuilt the three WP45 modules and WP46 from protected locked sources.
All six compilation/audit stages passed in 30.073 seconds in total,
including 5.731 seconds for WP47 and 4.176 seconds for the audit;
two major page faults, zero filesystem input blocks in those six stages.
Managed placement validated 1760 upstream source blobs and all 15
package pins. Nine placement regression controls passed. The existing
upstream import cache is reused, not independently rebuilt in full.
Two local elaboration errors were corrected before the exact replay;
no change to theorem statements. Raw receipts are in WP47_RECEIPTS.
The temporary import namespace was removed on normal completion.
Internal kernel verification, not independent public certification.
Protected admission remains a separate gate.
