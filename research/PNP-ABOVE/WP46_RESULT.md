# WP46: Weighted capacity does not amplify under efficient independent decomposition

Protected predecessor: WP45 merge e24feab62c7b86851b1d1ed157c40b2292494359.
Pinned upstream MIPRE 5926bdff5db621f44682a101007ef2fe3ae8d970,
Lean 4.35.0-rc3.

## Statement

For a fixed native polynomial verifier V, LocalCheap(V,B,a) means an actual
well-scoped program returns an accepted witness for a with score
2^esize(code)*(t+1) <= B. Different inputs may have different programs.
BatchGood is the aligned list of accepted component witnesses.

WP46 establishes, for a fixed verifier V, one polynomial q such that every
list of components xs with each component locally cheap at budget B has
an accepted joint witness list constructed by a native scoped program
with weighted score at most q(B+esize(xs)). The number of components is
not fixed. No individual solver or witness is placed into the batch code.

More generally, let D decode a joint input x into its component list and J
assemble component witnesses into a joint witness. D and J are fixed
native PolyTimeFun programs. Require the explicit lifting condition:
every accepted aligned component list for D(x) is mapped by J(x,ws) to
a witness accepted by the joint verifier W. Then some fixed polynomial q
satisfies

    (forall a in D(x), LocalCheap(V,B,a))
      => LocalCheap(W,q(B+esize(x)),x).

The contrapositive shows that if the joint budget q(B+esize(x)) fails,
at least one component fails at B. A polynomial component budget
(relative to the encoded size of x), holding on every witness-bearing x,
therefore gives a single total native polynomial joint solver. The
lifting premise is essential: independently acceptable local witnesses
need not agree on shared variables or satisfy additional constraints.

## Mechanism and actual costs

The WP45 universal selector is mapped over the components under a common
unary clock B, then the witness assembler is run. To bound the weighted
cost on the original input, compile the common budget into the program
in binary, rather than hardcoding a unary string. The upstream
binary-to-unary converter has a certified bound polynomial in the
numeric budget (not its binary length). The source s-m-n theorem adds
exactly esize(B)+35 nodes to the fixed core. Since
esize(B) <= 4*size(B)+1 and 2^size(B) <= 2*(B+1), the additional
description factor is at most 32*(B+1)^4, times a fixed constant.
The compiler charges conversion, copying, composition and actual
execution. Its score bound is a natural-coefficient polynomial in
B+esize(x). The theorem is not assuming a free budget or free advice.

## Consequence and limits

Independent aggregation cannot convert polynomially affordable
component searches into a superpolynomial weighted lower bound.
This remains true when the individual cheap programs are different
and there is no known uniform method for finding them. It eliminates
a multiplication-of-capacities argument based only on the size or
number of independently solvable blocks. A genuine lower-bound route
must confront components that are themselves hard, or the failure of
efficient decomposition/assembly (including incompatible witnesses).
The theorem does not prove that either phenomenon entails hardness,
and does not cover arbitrary overlapping constraint decompositions.
For SAT it applies when the split and witness reassembly meet the
explicit native interfaces; no particular SAT splitter is claimed here.
No unrestricted lower bound or P versus NP separation is established.

## Verification

Development compilation passed on the existing authorized Colab CPU runner.
Fresh exact-source replay rebuilds all three protected WP45 modules before
checking WP46, with placement evidence and standard-axiom audit.

Exact source candidate caf8331bb91e62fed041955606aa2630083e22b2.
Fresh guarded replay passed all 18 WP46 theorem declarations and the
standard-axiom audit. The three protected WP45 modules were freshly
rebuilt from source in the same isolated replay. Total checking and audit:
15.704 seconds; WP46 module and audit 6.565 seconds. Raw receipts retained
in WP46_RECEIPTS. No proof source or lock changed after replay. Internal
kernel verification, not independent public certification. The local SSD
mounts are restored, but capacity remains constrained; this replay used
the existing authorized Colab runner without HDD fallback.
