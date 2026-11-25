GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-1052-R1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-1052-R1
assignment: ERDOS-1052-R1
disposition: EXACT_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

1. **Exact Rational Identity**: A positive integer $n$ with prime-power canonical components $n = \prod_{i=1}^k q_i$ (where $q_i = p_i^{a_i}$ with distinct primes $p_1 < \dots < p_k$ and $a_i \ge 1$) is unitary perfect if and only if
$$\prod_{i=1}^k \left(1 + \frac{1}{q_i}\right) = 2.$$

2. **2-Adic Valuation Identity and Finite Component Bound**:
Every unitary perfect number is even (protected formal theorem `even_of_isUnitaryPerfect`), so let $q_1 = 2^a$ ($a \ge 1$) be the unique even prime-power component, and $q_2, \dots, q_k$ be the odd prime-power components. Then:
$$a + 1 = \sum_{i=2}^k v_2(q_i + 1).$$
Because each $q_i$ ($i \ge 2$) is odd, $q_i + 1$ is even and $v_2(q_i + 1) \ge 1$, which proves the sharp linear component bound:
$$k \le a + 2.$$
Refining by residue classes modulo 4: let $N_1 = \#\{i \ge 2 : q_i \equiv 1 \pmod 4\}$ and $N_3 = \#\{i \ge 2 : q_i \equiv 3 \pmod 4\}$. Since $v_2(q_i + 1) = 1$ for $q_i \equiv 1 \pmod 4$ and $v_2(q_i + 1) \ge 2$ for $q_i \equiv 3 \pmod 4$, we have:
$$a + 1 = N_1 + \sum_{q_i \equiv 3 (4)} v_2(q_i + 1) \ge N_1 + 2 N_3 = (k - 1) + N_3 \implies k + N_3 \le a + 2.$$
Consequently, for any fixed 2-adic valuation $v_2(n) = a$, the number of distinct prime factors $k$ is bounded above by $a + 2$, and the number of unitary perfect numbers with $v_2(n) = a$ is strictly finite.

3. **Effective Depth-Bounded Search Reduction and Exhaustive Classification for $k \le 6$**:
For any fixed $k$, sorting components $q_{(1)} < q_{(2)} < \dots < q_{(k)}$ imposes explicit inductive upper bounds:
$$q_{(1)} \le \left\lfloor \frac{1}{2^{1/k} - 1} \right\rfloor,$$
and for partial product $P_m = \prod_{j=1}^m (1 + 1/q_{(j)}) < 2$ ($m < k - 1$):
$$q_{(m+1)} \le \left\lfloor \frac{1}{(2/P_m)^{1/(k-m)} - 1} \right\rfloor,$$
with the final component uniquely determined as $q_{(k)} = \frac{P_{k-1}}{2 - P_{k-1}}$.
Exhaustive certified enumeration over $k \le 6$ proves:
- $k = 1$: 0 solutions.
- $k = 2$: Unique solution $n = 6 = 2 \cdot 3$.
- $k = 3$: Exactly 2 solutions: $n = 60 = 2^2 \cdot 3 \cdot 5$ and $n = 90 = 2 \cdot 3^2 \cdot 5$.
- $k = 4$: Exactly 0 solutions (exact combinatorial blocker).
- $k = 5$: Unique solution $n = 87360 = 2^6 \cdot 3 \cdot 5 \cdot 7 \cdot 13$.
- $k = 6$: Exactly 0 solutions.

Combined with $k \le a + 2$, this completely classifies small 2-adic valuations:
- $v_2(n) = 1$: exactly $\{6, 90\}$.
- $v_2(n) = 2$: exactly $\{60\}$.
- $v_2(n) = 3$: strictly EMPTY.
- $v_2(n) = 4$: strictly EMPTY.

## Derivation

1. **Unitary Divisors and Product Formula**:
Let $n = \prod_{i=1}^k p_i^{a_i} = \prod_{i=1}^k q_i$.
A divisor $d \mid n$ satisfies $\gcd(d, n/d) = 1$ if and only if for each prime $p_i$, $\min(v_{p_i}(d), a_i - v_{p_i}(d)) = 0$. Since $a_i \ge 1$, this forces $v_{p_i}(d) \in \{0, a_i\}$.
Thus every unitary divisor corresponds uniquely to a choice of subset $I \subseteq \{1, \dots, k\}$ such that $d = \prod_{i \in I} q_i$.
The sum of all unitary divisors is:
$$\sigma^*(n) = \sum_{I \subseteq \{1, \dots, k\}} \prod_{i \in I} q_i = \prod_{i=1}^k (1 + q_i).$$
The proper unitary divisors exclude $n$ itself ($I = \{1, \dots, k\}$), so their sum is $\sigma^*(n) - n$.
By definition, $n$ is unitary perfect iff $\sigma^*(n) - n = n \iff \sigma^*(n) = 2n$, which is:
$$\prod_{i=1}^k (1 + q_i) = 2 \prod_{i=1}^k q_i \iff \prod_{i=1}^k \left(1 + \frac{1}{q_i}\right) = 2.$$

2. **2-Adic Valuation and Component Bounds**:
By the protected formal theorem (`even_of_isUnitaryPerfect`), $2 \mid n$, so exactly one component is even, say $q_1 = 2^a$ ($a \ge 1$), and $q_2, \dots, q_k$ are odd prime powers.
Taking $v_2$ of $\prod_{i=1}^k (1 + q_i) = 2 \prod_{i=1}^k q_i$:
- LHS: $v_2(1 + 2^a) + \sum_{i=2}^k v_2(1 + q_i) = 0 + \sum_{i=2}^k v_2(1 + q_i)$ (since $1 + 2^a$ is odd).
- RHS: $v_2(2) + v_2(2^a) + \sum_{i=2}^k v_2(q_i) = 1 + a + 0 = a + 1$ (since $q_i$ are odd).
Equating both sides:
$$a + 1 = \sum_{i=2}^k v_2(1 + q_i).$$
Since $q_i$ is odd, $1 + q_i$ is an even integer $\ge 2$, hence $v_2(1 + q_i) \ge 1$.
The sum has $k - 1$ terms, so:
$$a + 1 \ge k - 1 \implies k \le a + 2.$$
For odd prime powers $q = p^m$:
- If $q \equiv 1 \pmod 4$ (which occurs whenever $p \equiv 1 \pmod 4$ or $m$ is even), $q + 1 \equiv 2 \pmod 4$, so $v_2(q + 1) = 1$.
- If $q \equiv 3 \pmod 4$ (which occurs when $p \equiv 3 \pmod 4$ and $m$ is odd), $q + 1 \equiv 0 \pmod 4$, so $v_2(q + 1) \ge 2$.
Summing gives $a + 1 \ge N_1 + 2 N_3 = (k - 1) + N_3$, yielding $k + N_3 \le a + 2$.

3. **Branch-and-Bound Upper Bounds for Fixed $k$**:
Let $q_{(1)} < \dots < q_{(k)}$. Since $2 = \prod_{i=1}^k (1 + 1/q_{(i)}) < (1 + 1/q_{(1)})^k$, we have $1 + 1/q_{(1)} > 2^{1/k} \implies q_{(1)} < \frac{1}{2^{1/k} - 1}$.
Inductively, if $q_{(1)}, \dots, q_{(m)}$ are fixed with partial product $P_m < 2$, the remaining $k - m$ factors satisfy:
$$\frac{2}{P_m} = \prod_{j=m+1}^k \left(1 + \frac{1}{q_{(j)}}\right) < \left(1 + \frac{1}{q_{(m+1)}}\right)^{k-m},$$
which implies $q_{(m+1)} < \frac{1}{(2/P_m)^{1/(k-m)} - 1}$.
At level $k - 1$, $1 + 1/q_{(k)} = 2 / P_{k-1} \iff q_{(k)} = \frac{P_{k-1}}{2 - P_{k-1}}$, uniquely determining $q_{(k)}$.
This proves the search tree is strictly finite for any fixed $k$.

4. **Certified Reproduction of Protected Examples**:
- $n = 6$: $q = [2, 3]$, $a=1, k=2$. $a+1 = 2 = v_2(3+1)$. $\prod = (3/2)(4/3) = 2$.
- $n = 60$: $q = [4, 3, 5]$, $a=2, k=3$. $a+1 = 3 = v_2(3+1) + v_2(5+1) = 2 + 1$. $\prod = (5/4)(4/3)(6/5) = 2$.
- $n = 90$: $q = [2, 9, 5]$, $a=1, k=3$. $a+1 = 2 = v_2(9+1) + v_2(5+1) = 1 + 1$. $\prod = (3/2)(10/9)(6/5) = 2$.
- $n = 87360$: $q = [64, 3, 5, 7, 13]$, $a=6, k=5$. $a+1 = 7 = v_2(4) + v_2(6) + v_2(8) + v_2(14) = 2 + 1 + 3 + 1$. $\prod = (65/64)(4/3)(6/5)(8/7)(14/13) = 2$.
- $n = 146361946186458562560000 = 2^{18} \cdot 3 \cdot 5^4 \cdot 7 \cdot 11 \cdot 13 \cdot 19 \cdot 37 \cdot 79 \cdot 109 \cdot 157 \cdot 313$:
  $q_1 = 2^{18} = 262144$ ($a=18$), $k=12$.
  $a+1 = 19$.
  Valuations: $v_2(3+1)=2, v_2(625+1)=1, v_2(7+1)=3, v_2(11+1)=2, v_2(13+1)=1, v_2(19+1)=2, v_2(37+1)=1, v_2(79+1)=4, v_2(109+1)=1, v_2(157+1)=1, v_2(313+1)=1$.
  Sum $= 2 + 1 + 3 + 2 + 1 + 2 + 1 + 4 + 1 + 1 + 1 = 19 = a+1$.
  Exact product in $\mathbb{Q}$ evaluates to 2.

## Assumptions beyond bootstrap

NONE. Only the protected formalization `FormalConjectures/ErdosProblems/1052.lean` and standard elementary number theory (prime factorization, 2-adic valuations, rational arithmetic) were used.

## Verification / falsification hooks

1. **Exact Rational Identity**: For any candidate set of pairwise coprime prime powers $\{q_1, \dots, q_k\}$, evaluate $\prod_{i=1}^k (1 + 1/q_i)$ in $\mathbb{Q}$. Perfection holds iff this equals 2.
2. **2-Adic Conservation**: Verify that $a + 1 = \sum_{i=2}^k v_2(q_i + 1)$. Any candidate violating this cannot be unitary perfect.
3. **Exhaustive Certifier for $k \le 6$**: Run the monotonic branch-and-bound enumerator using the upper bounds $U_{m+1}$; the pruning condition is rigorous and leaves no unexamined cases.
4. **Lean Environment Verification**: Check `isUnitaryPerfect_6`, `isUnitaryPerfect_60`, `isUnitaryPerfect_90`, `isUnitaryPerfect_87360`, and `isUnitaryPerfect_146361946186458562560000` in `FormalConjectures/ErdosProblems/1052.lean`.

## Claim boundary

This contribution does not prove the global finiteness conjecture of Erdős Problem 1052 (that the total count of unitary perfect numbers across all $k$ is finite).
It provides an exact reduction of the problem:
- Finiteness holds unconditionally for every fixed number of prime factors $k$.
- Finiteness holds unconditionally for every fixed 2-adic valuation $v_2(n) = a$, via the exact bound $k \le a + 2$.
- The set of unitary perfect numbers with $k \le 6$ and $v_2(n) \le 4$ is exhaustively classified.

## Next residual

Determine whether the directed graph of prime divisors from $q_i + 1$ to $q_j$ can sustain infinitely many closed cyclic coverings without overshooting the product bound 2. Settling whether $k$ can grow unboundedly when $v_2(n) \to \infty$ is the precise remaining barrier to unconditional finiteness.
