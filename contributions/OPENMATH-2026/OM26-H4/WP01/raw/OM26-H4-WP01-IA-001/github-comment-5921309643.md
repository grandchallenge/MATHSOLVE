GCL-CONTRIBUTION-RESULT/1
dispatch_id: OM26-H4-WP01-IA-001
agent_ref: INDEPENDENT-AGENT-004
assignment: OM26-H4-WP01
disposition: VALID_RULE_CATALOG
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: NO

## Strongest exact statement

Independent exact enumeration over modulus powers 2 through 8 inclusive and accelerated step depths 1 through 4 inclusive yields 309 distinct valid rules. A deterministic breadth-first containment reduction yields the 23-rule catalog below. Each rule proves strict descent for every positive integer in its residue class.

The independent affine verifier and a separate transcription of the protected evaluator's mathematical rule checks agree on all 1,016 enumerated candidate prefixes: zero validity disagreements. Both source examples replay exactly.

These are public mathematical validity statements. No private target data, scores, competition submission, or certification were used.

## Derivation

Write the affine expression after step i as

C^i(n) = (A_i n + B_i)/D_i.

Initialize (A_0,B_0,D_0)=(1,0,1). For exponent e_i, update

A_i=3A_(i-1),
B_i=3B_(i-1)+D_(i-1),
D_i=2^e_i D_(i-1).

Consequently A_s=3^s and D_s=2^E, where E=sum e_i.

For stability, let n=r+t2^k, with t a nonnegative integer. After j already stabilized steps, the difference from the representative trajectory is

C^j(n)-C^j(r)=3^j t 2^(k-E_j),

where E_j is the sum of the first j exponents. At the next numerator, the difference is 3^(j+1)t2^(k-E_j). If k>=E+1, then k-E_j>=e_(j+1)+1. Adding a multiple of 2^(e_(j+1)+1) preserves an exact valuation e_(j+1). Induction proves stability of every submitted exponent.

For descent, A_s<D_s gives a positive coefficient D_s-A_s. The inequality at the least representative is

B_s < (D_s-A_s)r.

For any n=r+t2^k, its right side is at least the right side at r. Thus A_s n+B_s<D_s n throughout the class.

The examples are:

- (k,r,exponents)=(4,9,[2]): numerator 28, valuation 2, endpoint 7. Affine coefficients (A,B,D)=(3,1,4), margin 1/4; 1<(4-3)9.
- (4,13,[3]): numerator 40, valuation 3, endpoint 5. Affine coefficients (3,1,8), margin 5/8; 1<(8-3)13.

The retained catalog is expressed as (k,r,exponents; A,B,D,endpoint,margin):

```text
(4,9,[2]; 3,1,4,7,1/4)
(4,13,[3]; 3,1,8,5,5/8)
(5,5,[4]; 3,1,16,1,13/16)
(5,17,[2]; 3,1,4,13,1/4)
(5,19,[1,3]; 9,5,16,11,7/16)
(6,3,[1,4]; 9,5,32,1,23/32)
(6,33,[2]; 3,1,4,25,1/4)
(6,43,[1,2,2]; 27,23,32,37,5/32)
(6,53,[5]; 3,1,32,5,29/32)
(6,55,[1,1,3]; 27,19,32,47,5/32)
(7,11,[1,2,3]; 27,23,64,5,37/64)
(7,21,[6]; 3,1,64,1,61/64)
(7,35,[1,5]; 9,5,64,5,55/64)
(7,65,[2]; 3,1,4,49,1/4)
(7,87,[1,1,4]; 27,19,64,37,37/64)
(8,7,[1,1,2,3]; 81,73,128,5,47/128)
(8,23,[1,1,5]; 27,19,128,5,101/128)
(8,99,[1,6]; 9,5,128,7,119/128)
(8,129,[2]; 3,1,4,97,1/4)
(8,143,[1,1,1,4]; 81,65,128,91,47/128)
(8,187,[1,2,1,3]; 81,85,128,119,47/128)
(8,203,[1,2,4]; 27,23,128,43,101/128)
(8,213,[7]; 3,1,128,5,125/128)
```

Selection orders valid candidates by increasing modulus power, increasing step count, decreasing exact contraction margin, increasing residue, and lexicographic valuation tuple. It retains a candidate only if its residue class is not contained in an already retained class. This preserves the union of public residue classes represented by the enumerated valid catalog. It does not preserve every alternative contraction margin and does not claim globally optimal rule count.

## Assumptions beyond bootstrap

Positive odd starting integers and the exact accelerated map defined in the envelope are assumed. Computation uses Python arbitrary-precision integers and reduced rational arithmetic. No random choices or seeds occur.

No additional mathematical source was used. The launch envelope was fetched from its supplied immutable GitHub URL; its embedded snapshots were the only problem evidence.

The envelope names hill.yaml and tests/test_hill.py but embeds only README.md and eval.py. Those omitted files are not execution-critical for this bounded mathematical task. Concordance here concerns the embedded rule-validity logic; it does not claim execution of omitted organizer tests or the full evaluator with private targets.

No numerical timebox was supplied, so timebox_observed is NO.

## Verification / falsification hooks

The following executable Python reconstructs the verifier, enumeration, independent comparison, catalog reduction, and digest. It requires only the standard library.

```python
from fractions import Fraction
import json
import hashlib

def v2(z):
    assert type(z) is int and z > 0
    return (z & -z).bit_length() - 1

def verify(k, r, es):
    if (type(k) is not int or not 2 <= k <= 32
        or type(r) is not int or not 0 < r < 2**k
        or r % 2 != 1):
        return None
    if (not 1 <= len(es) <= 24
        or any(type(e) is not int or not 1 <= e <= 32 for e in es)):
        return None
    E = sum(es)
    if E >= k:
        return None
    x = r
    A, B, D = 1, 0, 1
    trace = []
    for e in es:
        z = 3*x + 1
        if v2(z) != e:
            return None
        x = z // 2**e
        trace.append(x)
        A, B, D = 3*A, 3*B + D, D*2**e
    if not A < D or not B < (D-A)*r:
        return None
    assert D*x == A*r + B
    return A, B, D, x, Fraction(D-A, D), trace

# Separate transcription of the protected mathematical checks.
# Inputs in the comparison already satisfy its schema restrictions.
def protected(k, r, es):
    if k < sum(es) + 1:
        return False
    x = r
    for e in es:
        z = 3*x + 1
        c = 0
        while z % 2 == 0:
            c += 1
            z //= 2
        if c != e:
            return False
        x = z
    return 3**len(es) < 2**sum(es) and x < r

valid = []
candidates = 0
disagreements = 0

# Deterministic branch order: k ascending, r ascending, depth ascending.
for k in range(2, 9):
    for r in range(1, 2**k, 2):
        x = r
        es = []
        for s in range(1, 5):
            z = 3*x + 1
            e = v2(z)
            x = z // 2**e
            es.append(e)
            candidates += 1
            a = verify(k, r, es)
            b = protected(k, r, es)
            disagreements += bool(a) != b
            if a:
                valid.append((k, r, tuple(es)))

# Each representative has a unique exact trajectory. Thus every valid
# valuation tuple of depth <=4 in this region occurs among these prefixes.
assert len(valid) == len(set(valid))

ordered = sorted(
    valid,
    key=lambda t: (
        t[0], len(t[2]), -verify(*t)[4], t[1], t[2]
    )
)
selected = []
for t in ordered:
    if not any(
        t[0] >= q[0] and t[1] % 2**q[0] == q[1]
        for q in selected
    ):
        selected.append(t)
selected.sort()

# Digest covers the complete 309-rule catalog, in enumeration order.
# Encoding: compact JSON array of [k,r,[exponents]], UTF-8, no newline.
raw = json.dumps(
    [list(t[:2]) + [list(t[2])] for t in valid],
    separators=(",", ":")
)
digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()

print(candidates, len(valid), disagreements, len(selected))
print({k: sum(t[0] == k for t in valid) for k in range(2, 9)})
print(digest)
for t in selected:
    print(t, verify(*t)[:5])
print(verify(4, 9, [2]))
print(verify(4, 13, [3]))
for t in [
    (2, 1, [2]),    # insufficient modulus bits
    (4, 9, [3]),    # wrong observed valuation
    (3, 3, [1]),    # noncontractive
    (3, 1, [2]),    # contractive but no strict descent at r=1
]:
    print(t, verify(*t), protected(*t))
```

Observed aggregate outputs:

```text
1016 309 0 23
{2: 0, 3: 0, 4: 2, 5: 8, 6: 29, 7: 75, 8: 195}
951521f5064f0842993e895648b2b8bde2b29dda0d47c9d586ddac498bfa4f55
```

Observed source-example outputs:

```text
(3, 1, 4, 7, Fraction(1, 4), [7])
(3, 1, 8, 5, Fraction(5, 8), [5])
```

Observed negative-test outputs:

```text
(2, 1, [2]) None False
(4, 9, [3]) None False
(3, 3, [1]) None False
(3, 1, [2]) None False
```

No mathematical validity difference was found between the independent verifier and embedded protected rule checks. The independent verifier additionally exposes affine coefficients and traces; its `v2` rejects nonpositive inputs explicitly. Full submission-file validation, private-target loading, and scoring are outside this comparison.

## Claim boundary

The result proves only the listed finite residue-class descent lemmas and completeness of enumeration inside the explicitly bounded search region. It does not prove global Collatz convergence, completeness of residue coverage beyond that region, hidden-target coverage or scores, novelty, competition acceptance, or certification.

No repository mutation, pull request, competition submission, or direct GitHub intake was performed.

## Next residual

An independently authorized continuation could increase modulus power or trajectory depth, or retain structurally useful alternative margins alongside broad classes. Private-target performance remains unavailable from public evidence and must be assessed only by authorized infrastructure.
