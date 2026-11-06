# FIGURATE WP09-020 — exact 132-gonal Type B seed from a constrained Pell orbit

**Result:** exact global positive-integer Type B existence for $(k,c)=(132,2)$, with an infinite family by the protected WP09-013 fixed-first-pair theorem. This is internal producer mathematics; independent MATHCERT certification and external literature-priority review remain separate.

## 1. Exact seed

The entries are

$$
(a,b,d)=(1,130,8359584463533923231612770595169701590647797311),
$$

and the indices are

$$
(r,s,t)=(2,11340590449649248400673,129302625368040561155552).
$$

Direct substitution gives

$$
P_{132}(r)=132=130+2,
$$

$$
P_{132}(s)=8359584463533923231612770595169701590647797313=d+2,
$$

$$
P_{132}(t)=1086745980259410020109660177372061206784213650432=130d+2.
$$

The third entry has 46 decimal digits and exceeds the previous WP09-016 census bound.

## 2. Constrained Pell construction

The first pair is $a=1,b=130$ at $r=2$, because $P_{132}(2)=132=130+2$. Put $R=260$, $L=128$, and

$$
\Delta=8(k-2)c+L^2=8\cdot130\cdot2+128^2=18464.
$$

The fixed-pair norm equation is

$$
X^2-130S^2=(1)(1-130)\cdot18464=-2381856.
$$

An exact starting point is

$$
90608^2-130\cdot7948^2=-2381856.
$$

The unit $6499+570\sqrt{130}$ has norm one:

$$
6499^2-130\cdot570^2=1.
$$

After five unit multiplications,

$$
(X,S)=(33618682595690545900443392,\;
2948553516908804584174852).
$$

Both coordinates lie in the required polygonal lattice:

$$
X\equiv132\pmod{260},\qquad S\equiv132\pmod{260}.
$$

Thus $s=(S+128)/260$ and $t=(X+128)/260$ are positive integers. Set $d=P_{132}(s)-2$; exact substitution verifies $P_{132}(t)=130d+2$.

## 3. Infinite family

Since $ab=130$ is nonsquare, WP09-013 Theorem A applies. The amplification lattice modulus is

$$
M=2aR=520.
$$

The least positive exponent for which

$$
(6499+570\sqrt{130})^e\equiv1\pmod{520}
$$

in quadratic integer coordinates is $e=52$, verified by exact modular recurrence. Applying this power preserves the seed's index and divisibility classes. The next exact family member has a 474-digit third entry and is strictly larger. The protected WP09-013 theorem proves infinitely many distinct exact triples with the same first pair.

## 4. Relation to the local/global frontier

The protected WP09-012 classifier confirms $(132,2)$ is compatible at every positive modulus. WP09-013's earlier bounded scan had no seed for $(132,2)$ in its stated finite ranges; that negative result was not a global obstruction. WP09-020 supplies an actual exact integer seed and infinite family. This is a further example of everywhere-local compatibility accompanied by global existence, not a local-to-global counterexample.

## 5. Reproduction

- Constructor: [research/figurate_wp09_exact_seed_020.py](https://github.com/grandchallenge/MATHSOLVE/blob/main/research/figurate_wp09_exact_seed_020.py)
- Independent tests: [tests/test_figurate_wp09_exact_seed_020.py](https://github.com/grandchallenge/MATHSOLVE/blob/main/tests/test_figurate_wp09_exact_seed_020.py)
- Amplification theorem: [WP09-013 dossier](https://github.com/grandchallenge/MATHSOLVE/blob/main/work_packages/FIGURATE_WP09_GENERAL_FIRST_PAIR_PELL_013.md)

Run:

    python3 -m unittest -v tests.test_figurate_wp09_exact_seed_020
    python3 -m research.figurate_wp09_exact_seed_020
    python3 -m research.figurate_wp09_exact_seed_020 --next-family-member

The independent tests use the standard polygonal polynomial, separately replay the Pell orbit, verify all three exact pair equations and the lattice residues, and check the least modular unit exponent. No independent MATHCERT certification or external priority claim is asserted.
