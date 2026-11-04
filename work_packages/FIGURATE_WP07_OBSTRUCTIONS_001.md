# FIGURATE WP07 — three modular obstruction dossiers

**Campaign:** [FIGURATE-PILOT-001](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3093). **Assignment:** [WP07 #3098](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3098). **Status:** exact elementary proof candidates with executable modular certificates, **not** independently certified mathematical novelty.

All three dossiers concern **positive distinct entries**, order $k\geq3$, and an integer offset $c$. The expression $P_k(t)$ refers to the polygonal sequence at positive integer index $t$. Type A requires polygonal entries and square pairwise outputs; Type B requires polygonal pairwise outputs; Type C requires polygonal entries and polygonal pairwise outputs. These types are not interchangeable.

## Dossier 1: uniform Type C and Type A obstruction

**Claim D1.** If the polygonal order $k$ is divisible by $4$, and the offset $c$ satisfies $c\equiv2\pmod4$, **no Type C pair exists**. The same hypotheses exclude Type A pairs.

**Proof.** Write $k=4h$. Then

$$
P_{4h}(t)=(2h-1)t^2-(2h-2)t.
$$

For even $t$ the expression is $0$ modulo $4$; for odd $t$ it is $1$ modulo $4$. Thus every entry of a Type A or C tuple is congruent to $0$ or $1$ modulo $4$. The product of two such entries is also $0$ or $1$ modulo $4$. Adding $c\equiv2\pmod4$ gives $2$ or $3$ modulo $4$. But every square is $0$ or $1$ modulo $4$, and every $P_{4h}(t)$ is $0$ or $1$ modulo $4$. Both Type A and Type C pair conditions are impossible. This proof is uniform over all $h\geq1$ and all offsets in the stated class.

**Adversarial boundary.** This does **not** prohibit unrestricted Type B pairs, which exist for every order and offset. Nor does it prohibit all offsets: Type C, order $4$, offset $0$ has abundant examples. The preceding observation is a routine modular obstruction; no originality asserted.

## Dossier 2: octagonal fixed-pair extension obstruction, offset 2 modulo 8

For octagonal numbers, $P_8(t)=3t^2-2t$. Its complete residue image modulo $8$ is

$$
R_{8,8}=\{0,1,5\}.
$$

**Claim D2.** Fix any integer $c\equiv2\pmod8$. If $a,b$ are positive integers with $a\equiv1\pmod8$ and $b\equiv6\pmod8$, there is **no Type B triple containing both $a$ and $b$**, regardless of whether the fixed pair itself is compatible.

**Proof.** If $d$ extends the pair, both $ad+c$ and $bd+c$ must be octagonal. The first condition implies

$$
d+2\pmod8\in\{0,1,5\},
$$

so $d\pmod8$ lies in $\{6,7,3\}$. The second condition yields $6d+2$ modulo $8$, which is respectively $6$, $4$, or $4$ for these three classes. None belongs to $R_{8,8}$. Contradiction.

**Non-vacuity for infinitely many offsets and pairs.** For each such $c$, take $a=1$ and $b=P_8(t)-c$, with $t\equiv2\pmod{16}$ sufficiently large. The period identity modulo $8$ ensures $P_8(t)\equiv0\pmod8$, hence $b\equiv6\pmod8$, and the pair itself has the exact octagonal witness $ab+c=P_8(t)$. Infinitely many indices $t$ give distinct positive $b$. Each compatible pair is globally nonextendible to a Type B triple.

**Boundary:** This excludes a residue-constrained pair family, **not** all Type B triples at octagonal order. The L240 census contains octagonal triples at offsets $-1$, $0$ and $+1$. For the specific parameter $k=8,c=2$, bounded searches are supplementary only; the proof above does not rely on them.

## Dossier 3: independent octagonal extension obstruction, offset 3 modulo 16

The complete octagonal residue image modulo $16$ is

$$
R_{8,16}=\{0,1,5,8\}.
$$

**Claim D3.** Fix any integer $c\equiv3\pmod{16}$. If $a\equiv1\pmod{16}$ and $b\equiv5\pmod{16}$, there is **no Type B triple containing both $a$ and $b$.**

**Proof.** The condition that $ad+c$ be octagonal forces $d\pmod{16}$ to lie in $\{13,14,2,5\}$. In that order, $bd+c\equiv5d+3\pmod{16}$ takes values $4,9,13,12$, none in $R_{8,16}$. Thus no integer $d$ can extend the pair.

**Non-vacuity.** Given any such offset $c$, let $a=1$, $b=P_8(t)-c$ and take sufficiently large $t\equiv2\pmod{32}$. Since $P_8(t)\equiv8\pmod{16}$, the pair has $b\equiv5\pmod{16}$ and is exactly Type B-compatible via witness $t$, while no third entry exists.

**Boundary:** This is a distinct modulus/offset family, not a theorem covering arbitrary offsets or arbitrary prescribed pairs. It may overlap known elementary congruence folklore. Do not claim novel publication-level results before source-semantic specialist review.

## Executable certificate protocol

The [WP07 residue-certificate implementation](../research/figurate_wp07_obstructions.py) calculates the **full** residue image at each modulus using all indices from $1$ through $2m$, including every possible third-entry residue $0$ through $m-1$. A certificate with an empty extension-residue set proves impossibility under the hypotheses. The implementation also enumerates Type C compatible ordered **residue pairs with repetitions allowed**; this avoids the invalid assumption that distinct integer entries must have distinct residues.

```sh
python3 -m research.figurate_wp07_obstructions --k 8 --offset 2 --modulus 8 --a 1 --b 6
python3 -m research.figurate_wp07_obstructions --k 8 --offset 3 --modulus 16 --a 1 --b 5
python3 -m research.figurate_wp07_obstructions --k 8 --offset 2 --modulus 4
python3 -m unittest discover -s tests -p 'test_figurate_wp07_obstructions.py' -v
```

Tests independently calculate residue images over eight modular periods, compare certificate outputs against independent exhaustive modular loops, verify finite representatives for positive and negative offsets in the claimed infinite classes, and search for missed triple extensions up to entry $300$.

## Prior art, proof and decision gate

The [primary-source bibliography](https://github.com/grandchallenge/MATH-PROGRAMME/blob/main/docs/campaigns/FIGURATE_SOURCES.md) distinguishes Type A from Type B; existing Filipin–Szalay/Jurasić–Togbé results exclude extensions of **specified triangular pairs**, not the octagonal congruence families here. That does **not** establish novelty: a dedicated complete literature/folklore review for polygonal modular obstructions, followed by separate specialist mathematical review, remains necessary.

**Proof state:** elementary arguments fully written and independently testable as arithmetic; source novelty **UNVERIFIED**, external mathematical certification **NOT GRANTED**. **Next proposition route:** generalize the extension-residue obstruction to an algorithmically generated family of polygonal orders and moduli, with a nontrivial structural classification, and compare against stronger global methods (simultaneous Pell systems). This is a viable target for WP08, but the three simple congruence lemmas alone do not justify a publication claim.
