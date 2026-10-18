GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-138-R1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-138-R1
assignment: ERDOS-138-R1
disposition: EXACT_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

For the protected two-colour van der Waerden function W, the target
W(k)^(1/k) -> infinity is equivalent (ignoring the finite k=0 prefix) to
log W(k) / k -> infinity, and equivalently to: for every A > 1, eventually
W(k) >= A^k.

W is nondecreasing in k. Hence for any strictly increasing unbounded sequence
1 <= n_1 < n_2 < ... and any lower bounds W(n_j) >= L_j >= 1, if
n_j <= k < n_{j+1}, then

    W(k)^(1/k) >= L_j^(1/n_{j+1})

and

    log W(k)/k >= log L_j / n_{j+1}.

Therefore the exact monotonicity/interpolation threshold is

    log L_j / n_{j+1} -> infinity,

or equivalently L_j^(1/n_{j+1}) -> infinity.  More precisely, if the supplied
L_j are not monotone, replace them by B_j = max_{i<=j} L_i; B_j is the
strongest lower envelope forced by monotonicity, and the threshold becomes
log B_j / n_{j+1} -> infinity.  This criterion is sharp for conclusions based
only on monotonicity plus the stated subsequence lower bounds: the piecewise
constant monotone envelope F(k)=B_j on n_j <= k < n_{j+1} realizes exactly
that worst case.

Applied to the protected Lean theorem body for primes,

    W(p+1) >= p * 2^p,

the bound cannot imply root divergence.  Indeed its own subsequence root is

    (p * 2^p)^(1/(p+1))
      = p^(1/(p+1)) * 2^(p/(p+1)) -> 2,

not infinity.  For consecutive selected primes p_j < p_{j+1}, the
interpolation exponent is even weaker:

    log(p_j * 2^p_j)/(p_{j+1}+1)
    <= (log p_j + p_j log 2)/(p_j+2) -> log 2.

Thus no prime-density improvement can make this particular lower bound cross
the required interpolation threshold.

By contrast, if the unreconciled prose assertion W(p+1) >= p^(2^p) were valid
for this exact W, then the same interpolation lemma would require exactly

    (2^p log p)/(q(p)+1) -> infinity,

where q(p) is the next selected prime.  For example q(p)=O(p) would suffice.
This is only a conditional comparison; it does not validate the prose
assertion.

The protected small-k normalization is

    W(1)=1, W(2)=3, W(3)=9.

The first two are explicit theorems in the protected Formal Conjectures
snapshot.  The third has the exact finite certificate below.

## Derivation

1. Protected normalization.

At the protected snapshot, monoAP_guarantee_set(r,k) consists of N such that
every coloring Finset.Icc 1 N -> Fin r contains a monochromatic arithmetic
progression of length k, monoAPNumber(r,k) is its natural-number infimum, and
W abbreviates monoAPNumber 2.

The imported protected AP definition represents an arithmetic progression as
a set with ENat.card exactly k and terms a+n*d for n<k.  Hence for k>1 a
zero-difference repeated point cannot masquerade as a k-term progression:
cardinality forces k distinct terms.  Thus W is the classical two-colour
van der Waerden normalization on {1,...,N}, not a zero-based or
repeated-term variant.

2. Monotonicity.

Any (k+1)-term arithmetic progression contains its first k terms as a k-term
arithmetic progression, with the same colour.  Therefore every N that
guarantees a monochromatic (k+1)-AP also guarantees a monochromatic k-AP.
Taking least such N gives W(k) <= W(k+1).

3. Logarithmic equivalence and interpolation.

For k>=1, W(k)>=1.  Taking logarithms gives

    log(W(k)^(1/k)) = log W(k)/k.

Since exp and log are increasing, W(k)^(1/k)->infinity iff
log W(k)/k->infinity.

If n_j <= k < n_{j+1}, monotonicity gives W(k)>=W(n_j)>=L_j.  Because
k<n_{j+1} and log L_j>=0,

    log W(k)/k >= log L_j/k >= log L_j/n_{j+1}.

Exponentiating gives the stated root inequality.  Replacing L_j by cumulative
maxima B_j records all lower bounds available up to n_j.  The piecewise
constant B_j envelope shows this is the best universal transfer obtainable
from those data alone.

4. Protected prime bound.

Substituting L(p)=p*2^p gives log L(p)=log p+p log 2.  Since any later selected
prime q satisfies q>=p+1, division by q+1 can remain at most asymptotically
log 2.  The lower bound therefore supplies only an exponential base near 2,
whereas the Erdős target requires bases tending without bound.

If instead L(p)=p^(2^p), then log L(p)=2^p log p and the exact transfer
condition is 2^p log p/(q(p)+1)->infinity.  The difference between the two
protected representations is therefore mathematically decisive.

5. Exact small-k ledger.

The protected file proves W(1)=1 and W(2)=3.

For k=3, enumerate a two-colouring of {1,...,8} by a bit string c_1...c_8 and
reject it if any triple (a,a+d,a+2d), a+2d<=8, is monochromatic.  There are
exactly 12 such triples and 2^8=256 colourings.  Exact exhaustive checking
leaves precisely six strings:

    00110011
    01011010
    01100110
    10011001
    10100101
    11001100.

Hence an AP-free colouring exists on 8, so W(3)>8.

None of the six extends to 9.  The obstruction can be checked without
re-enumerating 2^9 colourings:

- 00110011: positions 7,8 are 1,1, forcing c9=0 via (7,8,9), while
  positions 1,5 are 0,0, forcing c9=1 via (1,5,9).
- 01011010: positions 5,7 are 1,1, forcing c9=0 via (5,7,9), while
  positions 3,6 are 0,0, forcing c9=1 via (3,6,9).
- 01100110: positions 1,5 are 0,0, forcing c9=1, while positions 3,6
  are 1,1, forcing c9=0.
- 10011001: positions 1,5 are 1,1, forcing c9=0, while positions 3,6
  are 0,0, forcing c9=1.
- 10100101: positions 5,7 are 0,0, forcing c9=1, while positions 3,6
  are 1,1, forcing c9=0.
- 11001100: positions 7,8 are 0,0, forcing c9=1, while positions 1,5
  are 1,1, forcing c9=0.

Therefore every two-colouring of {1,...,9} has a monochromatic 3-AP, so
W(3)=9.

## Assumptions beyond bootstrap

NONE.  Only the protected Formal Conjectures snapshot, its imported protected
AP definition, exact finite enumeration, and standard elementary mathematics
were used.

## Verification / falsification hooks

1. At protected snapshot 85f863718beeec7b58a3a1926ee92e3472bc2020,
   inspect FormalConjectures/ErdosProblems/138.lean and
   FormalConjecturesForMathlib/Combinatorics/AP/Basic.lean.  Check the
   definitions of monoAP_guarantee_set, monoAPNumber, W,
   ContainsMonoAPofLength, and Set.IsAPOfLengthWith, plus the protected
   W(1)=1, W(2)=3, and prime-bound theorem body.

2. For W(3)=9, independently enumerate all 256 bit strings of length 8 and
   the 12 triples (a,a+d,a+2d) with a+2d<=8.  The survivor set should be
   exactly the six strings listed above.  Check the two contradictory
   constraints on c9 listed for each survivor.

3. For the interpolation lemma, choose any n_j<=k<n_{j+1} and verify the
   two monotonic inequalities directly.  A falsifier needs only a
   nondecreasing positive sequence satisfying the stated subsequence bounds
   but violating the claimed inequality.

4. For the protected prime body, directly evaluate
   log(p*2^p)/(p+1) and its limit log 2.  This separates the theorem body from
   the unreconciled prose annotation without importing any external source.

## Claim boundary

This result does not prove Erdős Problem 138, does not validate the prose
Berlekamp annotation, does not establish any stronger lower bound for W, and
does not use or inspect sibling returns.  It establishes a sharp conditional
subsequence-to-full-sequence reduction, proves that the protected theorem body
p*2^p is quantitatively insufficient for that reduction, and gives the exact
finite normalization check W(3)=9.

## Next residual

The remaining mathematical requirement is a lower bound L_j on an unbounded
subsequence n_j for the exact protected W such that
log L_j/n_{j+1}->infinity (with cumulative maxima if necessary), or an
alternative argument that does not rely only on monotonicity interpolation.
The protected prime theorem body p*2^p cannot supply this requirement.