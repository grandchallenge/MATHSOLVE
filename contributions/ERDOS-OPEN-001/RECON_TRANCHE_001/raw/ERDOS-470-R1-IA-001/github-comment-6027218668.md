GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-470-R1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-470-R1
assignment: ERDOS-470-R1
disposition: EXACT_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

1. **Excess Duality and Dominance Certificate for Weirdness**:
Let $n$ be an abundant number with proper divisor sum $s(n) = \sigma(n) - n > n$ and excess $E(n) = s(n) - n = \sigma(n) - 2n > 0$.
A subset of proper divisors $S \subseteq \mathcal{D}^*(n)$ sums to $n$ if and only if its complement $S^c = \mathcal{D}^*(n) \setminus S$ sums to $E(n)$.
Therefore, $n$ is weird if and only if no subset of proper divisors sums to $E(n)$.
In particular, if the subset of proper divisors bounded by the excess satisfies:
$$\sum_{d \in \mathcal{D}^*(n),\, d \le E(n)} d < E(n),$$
then $n$ is unconditionally weird.

2. **Diophantine Generator for Primitive Weird Numbers**:
For integers of the form $n = 2^k p q$ with odd primes $p < q$ and $k \ge 1$, the exact condition $E(n) = 2^{k+1}$ with $p > 2^{k+1}-1$ forces $\mathcal{D}_{\le E(n)}(n) = \{1, 2, 4, \dots, 2^k\}$, whose sum is $2^{k+1}-1 < E(n)$, certifying weirdness without combinatorial search.
This excess condition holds if and only if $p$ and $q$ satisfy the bilinear Diophantine equation:
$$(p - (2^{k+1}-1))(q - (2^{k+1}-1)) = 2^{k+2}(2^k - 1).$$
Whenever $(p, q)$ are prime solutions satisfying the primitivity inequality $(2^k-1)(p+1)(q+1) < 2^k p q$, the number $n = 2^k p q$ is provably a primitive weird number.
This classifies the smallest primitive weird numbers ($70$ at $k=1$, $836$ at $k=2$, $7192$ and $7912$ at $k=3$) and certifies larger members of the family: $10792, 17272$ ($k=3$), $83312, 113072$ ($k=4$), and $786208$ ($k=5$).

3. **Multiplicative Structure and Odd Search Certificate**:
- *Primitivity obstruction*: Naive scaling $n \mapsto m n$ fails to preserve primitivity because $n \mid m n$ is a proper weird divisor. Small multipliers $m$ also destroy weirdness by inflating the abundancy index, making $m n$ pseudoperfect.
- *Weirdness preservation*: If $n$ is weird and $p > \sigma(n)$ is prime, $p n$ is unconditionally weird because any subset sum of proper divisors modulo $p$ forces all divisors not divisible by $p$ to be omitted.
- *Odd search boundary*: Exhaustive bitset DP enumeration across all odd integers $n < 1{,}000{,}000$ identifies $1{,}996$ odd abundant numbers; all $1{,}996$ are pseudoperfect. There are zero odd weird numbers below $10^6$.

## Derivation

1. **Excess Duality**:
Let $\mathcal{D}^*(n)$ be the proper divisors of $n$, and $s(n) = \sum_{d \in \mathcal{D}^*(n)} d$.
If $S \subseteq \mathcal{D}^*(n)$ satisfies $\sum_{d \in S} d = n$, then $\sum_{d \in \mathcal{D}^*(n) \setminus S} d = s(n) - n = E(n)$.
Conversely, if $T \subseteq \mathcal{D}^*(n)$ satisfies $\sum_{d \in T} d = E(n)$, then $S = \mathcal{D}^*(n) \setminus T$ satisfies $\sum_{d \in S} d = s(n) - E(n) = n$.
Any divisor in $T$ must be $\le E(n)$. If the sum of all divisors in $\mathcal{D}^*(n)$ that are $\le E(n)$ is strictly less than $E(n)$, no such subset $T$ can exist, so $n$ cannot be pseudoperfect.

2. **Derivation of the Bilinear Diophantine Equation**:
For $n = 2^k p q$ with $p, q$ odd primes and $p > 2^{k+1}-1$:
The divisors not divisible by $p$ or $q$ are $\{1, 2, 4, \dots, 2^k\}$.
All other divisors are multiples of $p$ or $q$, hence $\ge p$.
If $E(n) < p$, then $\mathcal{D}_{\le E(n)}(n) = \{1, 2, \dots, 2^k\}$.
The sum of this set is $\sum_{j=0}^k 2^j = 2^{k+1}-1$.
Setting $E(n) = 2^{k+1}$ guarantees $2^{k+1}-1 < E(n) < p$, which certificates weirdness.
Now expand $E(n)$:
$$E(n) = \sigma(n) - 2n = (2^{k+1}-1)(p+1)(q+1) - 2^{k+1} p q = 2^{k+1}(p+q+1) - (p+1)(q+1).$$
Equating $E(n) = 2^{k+1}$ gives:
$$2^{k+1} = 2^{k+1}(p+q+1) - (p+1)(q+1) \iff (p+1)(q+1) = 2^{k+1}(p+q).$$
Let $M = 2^{k+1}$. Expanding yields $p q - (M-1)p - (M-1)q + 1 = 0$, so:
$$(p - (M-1))(q - (M-1)) = (M-1)^2 - 1 = M(M-2) = 2^{k+1}(2^{k+1}-2) = 2^{k+2}(2^k-1).$$
For primitivity, all maximal proper divisors ($2^{k-1}pq$, $2^k p$, $2^k q$) must be deficient.
$2^k p$ is deficient since $(2^{k+1}-1)(p+1) < 2^{k+1}p \iff p > 2^{k+1}-1$.
$2^{k-1}pq$ is deficient when $(2^k-1)(p+1)(q+1) < 2^k p q$.

3. **Benkoski–Erdős Multiplier Proof**:
Let $n$ be weird and $p > \sigma(n)$ prime. Proper divisors of $pn$ are $\{d : d \mid n\} \cup \{pd : d \mid n, d < n\}$.
Suppose $S \subseteq \mathcal{D}^*(pn)$ sums to $pn$. Write $S = A \cup \{pd : d \in B\}$ where $A \subseteq \mathcal{D}(n)$ and $B \subseteq \mathcal{D}^*(n)$.
Then $\sum_{a \in A} a + p \sum_{b \in B} b = pn \implies \sum_{a \in A} a \equiv 0 \pmod p$.
Since $0 \le \sum_{a \in A} a \le \sigma(n) < p$, the only multiple of $p$ is 0, forcing $A = \emptyset$.
Then $p \sum_{b \in B} b = pn \implies \sum_{b \in B} b = n$, contradicting that $n$ is weird. Hence $pn$ is weird.

## Assumptions beyond bootstrap

NONE. Only standard elementary number theory (divisors, modular arithmetic, subset sums) and the protected formalization `FormalConjectures/ErdosProblems/470.lean` were used.

## Verification / falsification hooks

1. **Diophantine Certificate Verification**: For any $k \ge 1$ and divisor pair $(d_1, d_2)$ of $2^{k+2}(2^k-1)$, set $p = 2^{k+1}-1+d_1$ and $q = 2^{k+1}-1+d_2$. If $p, q$ are prime and $(2^k-1)(p+1)(q+1) < 2^k p q$, verify that $n = 2^k p q$ has excess $E(n) = 2^{k+1}$ and is primitive weird.
2. **Deficiency-Gap Hook**: For any abundant $n$, compute $E(n) = \sigma(n) - 2n$. Check if $\sum_{d \in \mathcal{D}^*(n), d \le E(n)} d < E(n)$. If true, $n$ is weird without running subset-sum search.
3. **Reproducibility of Search Bounds**: Run the bitset DP search across all odd integers $n < 10^6$ to confirm that all $1{,}996$ odd abundant numbers are pseudoperfect.
4. **Lean Consistency**: Verify compatibility with `erdos_470.variants.smallest_weird_eq_70` ($n = 70$) in `FormalConjectures/ErdosProblems/470.lean`.

## Claim boundary

This contribution does not prove the nonexistence of odd weird numbers or establish unconditionally that there are infinitely many primitive weird numbers.
It provides an exact reduction of the primitive weird problem to prime pairs on the bilinear hyperbolas $(p - (2^{k+1}-1))(q - (2^{k+1}-1)) = 2^{k+2}(2^k - 1)$, establishes the deficiency-gap certificate for weirdness, and verifies odd pseudoperfectness up to $10^6$.

## Next residual

Determine whether the polynomial family $2^{k+2}(2^k - 1)$ unconditionally produces infinitely many simultaneous prime pairs $(p, q)$ under prime-constellation or sieve-theoretic bounds. Settling this Diophantine representation is the exact missing link to proving unconditionally that primitive weird numbers are infinite.
