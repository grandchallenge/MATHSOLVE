GCL-CONTRIBUTION-RESULT/1
dispatch_id: GCL-ERDOS3-E3-S03-IA-001
assignment: E3-S03
agent_ref: INDEPENDENT-AGENT-E3-S03-001
disposition: SOURCE_BLOCKED
context_class: ZERO_CONTEXT
external_sources: PRIMARY_SOURCES_REQUIRED

## Strongest exact statement

In the scoped primary-source audit I found no theorem that gives a summable averaged bound, a contracting cross-scale recurrence, or any other sequence-level estimate for

a_n := r_4(2^n)/2^n

that is strong enough to improve the protected frontier.

The strongest quantitative theorem remains Green–Tao (2017), Theorem 1.1:

r_4(N) << N (log N)^(-c)

for some absolute c>0. Therefore, at dyadic scales,

a_n << n^(-c).

The paper does not state c>1, so this does not imply sum_n a_n < infinity.

The only explicit general cross-scale relation located in the scoped sources is subadditivity,

r_k(N+N') <= r_k(N)+r_k(N'),

recorded in Green (2026), §1 item (2). For k=4, N=N'=2^n, this gives

a_{n+1} <= a_n.

This is exactly the monotonicity already present in the protected B02 packet; it supplies no quantitative decay between successive scales and no summable average.

## Derivation / evidence

1. **Green–Tao 2017, Theorem 1.1.** The theorem states r_4(N) << N(log N)^(-c) for some absolute c>0. Substituting N=2^n gives a_n = r_4(2^n)/2^n << (log 2^n)^(-c) asymp n^(-c).

2. **Green–Tao 2017, Theorem 3.1.** This is the paper's quantitative Khintchine-type recurrence statement. For one fixed prime modulus p, one fixed function f: Z/pZ -> [-1,1], and 0<eta<=1/10, it constructs random variables a,r satisfying near-uniformity (3.2), the four-term recurrence lower bound Lambda_{a,r}(f) >= (E f(a))^4 - O(eta) in (3.3), and the thickness estimate P(r=0) << exp(-eta^(-O(1)))/p in (3.4). Equations (3.5)–(3.6) and the deduction immediately following Theorem 3.1 apply this fixed-p statement to a single 4-AP-free set A subset [N], choose p asymp N, and recover Theorem 1.1. I found no statement there comparing r_4(N) with r_4(N') for distinct ambient scales.

3. **Green–Tao 2017, Proposition 3.3 and Theorems 6.6–6.7.** These are the high-level structured-approximant iteration and energy/dimension decrement machinery. Proposition 3.3 iterates vertices v_0 -> ... -> v_k for fixed p,f,eta. Theorem 6.6 gives an energy decrement for a bad approximation, equation (6.15), while Theorem 6.7 decreases the poorly distributed quadratic dimension under a bad lower bound, equation (6.19). Their iteration variable is the internal approximant v, not the ambient integer scale N. Consequently these theorems do not induce a recurrence for the extremal sequence a_n.

4. **Green 2026 survey.** Table 2 lists the progression of length-four bounds and still terminates with Green–Tao 2017, N(log N)^(-c). In the accompanying discussion Green states that improving r_k(N) for k>=4 remains a fundamental problem and that the sum-of-reciprocals conjecture for progressions of length four is still far away. The same survey explicitly records subadditivity r_k(N+N') <= r_k(N)+r_k(N'), which yields a_{n+1} <= a_n but no summable control.

Thus the word “recurrence” in the Green–Tao machinery is recurrence of arithmetic configurations inside one ambient group, not a recurrence relation for the extremal values r_4(2^n) across n.

## Adversarial checks

- **Could monotonicity plus the pointwise bound force summability?** No. A nonincreasing positive sequence can obey a_n << n^(-c) with 0<c<=1 and still have divergent sum. The source theorem supplies only “some absolute c>0”.
- **Could the energy decrement be reinterpreted as a scale decrement?** Not from the stated hypotheses or conclusions. Theorems 6.6–6.7 modify a structured local approximant while p,f,eta remain fixed; neither conclusion contains r_4(N') at a second ambient size.
- **Does Theorem 3.1 average over many scales?** No. Its averaging is over random variables a,r inside one Z/pZ.
- **Did the scoped literature reveal a post-2017 sharpening for r_4?** Green's March 2026 survey Table 2 lists no later length-four improvement and explicitly retains Green–Tao 2017 as the endpoint.
- **Absence claim scope.** This is only a source audit of the specified/prioritized primary-source line and the current author survey; it is not a proof that no such theorem can exist.

## First defect

No scoped theorem supplies a quantitative relation between distinct dyadic extremal densities a_n that is stronger than the already-known monotonicity a_{n+1} <= a_n. In particular, no located theorem gives a summable average sum_{n<=m} a_n, a contraction a_{n+h} <= q a_n + epsilon_n with useful q<1, or another recurrence sufficient to imply sum_n a_n < infinity.

## Frontier effect

`E3-Q4-SERIES` remains open and unchanged.

The source audit confirms that Green–Tao's energy/dimension-decrement machinery does not itself expose a sequence-level recurrence for a_n, and that the 2026 primary survey still reports the 2017 polylogarithmic bound as the endpoint for r_4. The only sourced cross-scale statement found is subadditivity/monotonicity already contained in B02, so no new theorem-grade source interface advances the frontier.

This result does not certify or refute the parent Erdős conjecture.

## Next residual

The residual evidence target is a genuinely inter-scale theorem for r_4: a quantitative contraction, a summable averaged estimate, or a recurrence whose iteration beats the unsummable n^(-c) pointwise envelope. None was located in the scoped primary sources.

## Sources

1. Ben Green and Terence Tao, **“New bounds for Szemerédi's theorem, III: A polylogarithmic bound for r_4(N)”**, Mathematika 63 (2017), 944–1040. Theorem 1.1; Theorem 3.1; Proposition 3.3; Theorems 6.6–6.7. arXiv:1705.01703v3. DOI: 10.1112/S0025579317000316.
   https://arxiv.org/abs/1705.01703
   https://doi.org/10.1112/S0025579317000316

2. Ben Green, **“Arithmetic progressions at the Journal of the LMS”**, Journal of the London Mathematical Society 113(3) (2026), e70483. §1 item (2); §3 and Table 2. DOI: 10.1112/jlms.70483.
   https://doi.org/10.1112/jlms.70483
