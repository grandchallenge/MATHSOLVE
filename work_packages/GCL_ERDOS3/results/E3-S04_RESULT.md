GCL-CONTRIBUTION-RESULT/1
dispatch_id: GCL-ERDOS3-E3-S04-IA-001
assignment: E3-S04
agent_ref: INDEPENDENT-AGENT-E3-S04-001
disposition: SOURCE_INTERFACE_REQUIRES_BRIDGE
context_class: ZERO_CONTEXT
external_sources: PRIMARY_SOURCES_REQUIRED

## Strongest exact statement

An exact **four-fiber counting interface** exists, with polynomial quantitative dependence, but the audited sources do **not** supply the stability/deletion bridge needed for E3-Q4-DENSITY-LOSS.

Let (N=2^n), (m=2^L), and let a globally 4-AP-free extremizer in ([mN]) have block fibers
[
B_jsubset{0,ldots,N-1},qquad 0le j<m.
]
Write (alpha=r_4(N)/N=a_n). Then exactly
[
sum_{j=0}^{m-1}igl(r_4(N)-|B_j|igr)
   =mN(a_n-a_{n+L})=mN D_{L,n}.
]
Thus the protected target (D_{L,n}ge calpha^{1+	heta}) is a lower bound on the total mass deficit of the sibling fibers.

Now fix a valid digit/carry pattern
[
j_t=i+tq+c_t,qquad c_t=Biglfloorrac{u+tv}{N}Bigfloor,qquad t=0,1,2,3.
]
For the corresponding four fibers define translated sets
[
C_t:=c_tN+B_{j_t}.
]
Choose a prime (P) with (8N<P<16N) and regard (C_tsubsetmathbb Z/Pmathbb Z). Since (C_tsubset[0,4N)), any modular 4-AP with its (t)-th point in (C_t) is an ordinary integer 4-AP: all adjacent integer differences lie in ((-4N,4N)), and equality modulo (P>8N) forces equality as integers. If (y_tin C_t) is such a progression, then
[
x_t:=(i+tq)N+y_tin j_tN+B_{j_t}
]
is a 4-AP in the original large interval. Hence, for a genuinely cross-block compatible tuple in a globally 4-AP-free set, the mixed progression count across (C_0,C_1,C_2,C_3) is zero.

Gowers, *A new proof of Szemerédi's theorem* (2001), Theorem 3.2 and Corollary 3.3, gives an exact multilinear interface on (mathbb Z/Pmathbb Z). In the (k=4) specialization, if (C_2) is (gamma^4)-uniform of degree (1) and (C_3) is (gamma^8)-uniform of degree (2) in Gowers' terminology, and (ho_t=|C_t|/P), then
[
left|M(C_0,C_1,C_2,C_3)-ho_0ho_1ho_2ho_3P^2ight|
   le 16gamma P^2,
]
where (M) is the mixed four-function 4-AP count. Therefore (M=0) forces
[
ho_0ho_1ho_2ho_3le16gamma.
]
If the four fibers all have density at least (eta) in their length-(N) blocks, then (ho_tgeeta/16). Taking (gamma) to be a sufficiently small absolute multiple of (eta^4), the two Gowers-uniformity hypotheses cannot both hold. Equivalently: **every dense carry-compatible four-fiber tuple in an AP-free gluing must exhibit degree-1 or degree-2 nonuniformity at an explicitly polynomial scale** (the Corollary 3.3 thresholds are polynomial, of orders (eta^{16}) and (eta^{32}) up to absolute constants).

Green–Tao (2010), corrected version, Theorem 4.1 supplies the same conceptual interface in modern norm language: for the four forms (u,u+v,u+2v,u+3v), whose Cauchy–Schwarz complexity is (2), a four-separate-function correlation is controlled by the (U^3) norm of any one factor. This confirms that the correct source-level cross-fiber pseudorandomness object is (U^3)/quadratic uniformity, not ordinary Fourier uniformity.

The exact missing bridge is therefore:

**carry-compatible quadratic stability bridge:** convert the polynomial-scale (U^3)/quadratic nonuniformity forced on dense compatible sibling fibers into a total sibling mass deficit
[
sum_j(r_4(N)-|B_j|)ge c,mN,alpha^{1+	heta}
quad	ext{for some fixed }0<	heta<1.
]
No audited primary source supplies this implication.

## Derivation / evidence

### 1. Exact multilinear source interface: Gowers 2001

Gowers' Theorem 3.2 states: for (f_1,ldots,f_k:mathbb Z_N	o D), if (f_k) is (eta)-uniform of degree (k-2), then
[
left|sum_{r,s}f_1(s)f_2(s-r)cdots f_k(s-(k-1)r)ight|
 le eta^{1/2^{k-1}}N^2.
]
For (k=4), the error is (eta^{1/8}N^2), and the theorem genuinely allows four separate functions.

Corollary 3.3 packages this into a mixed-set counting lemma. For (A_1,ldots,A_ksubsetmathbb Z_N), (|A_i|=delta_iN), with (A_i) (eta^{2^{i-1}})-uniform of degree (i-2) for (ige3),
[
left|sum_r |(A_1+r)capcdotscap(A_k+kr)|
       -delta_1cdotsdelta_kN^2ight|
 le 2^keta N^2.
]
For (k=4), this is exactly the four-fiber estimate used above. Its dependence is polynomial and therefore is, at the **counting** stage, effective enough for a power-law argument.

### 2. Green–Tao 2010: four-function (U^3) control exists, but regularity is not the missing stability theorem

In the corrected arXiv version of Green–Tao, *An arithmetic regularity lemma, associated counting lemma, and applications*:

- Theorem 4.1 (Generalised von Neumann) treats separate bounded functions (f_i) on a system of linear forms. For the 4-AP system the Cauchy–Schwarz complexity is (2), hence the controlling norm is (U^3).
- Theorem 1.12 (Bergelson–Host–Kra conjecture) says that, for (kle4), (Asubset[N]) of density at least (alpha), and (arepsilon>0), there are (gg_{alpha,arepsilon}N) differences (d) for which at least ((alpha^k-arepsilon)N) (k)-APs in (A) have common difference (d).
- Theorem 5.1 is the weighted quantitative form used to prove Theorem 1.12.

The popular-difference conclusion is a **one-set** statement, not a rainbow/four-fiber statement. Moreover the authors explicitly note that the higher-order arithmetic-regularity route has tower-type quantitative behaviour. It therefore does not furnish the required power-size gluing penalty when (alpha=a_n	o0).

### 3. Green–Tao 2017: strong fixed-ambient recurrence, still one function

Green–Tao, *New bounds for Szemerédi's theorem, III*:

- Theorem 1.1: (r_4(N)ll N(log N)^{-c}) for an absolute (c>0).
- Theorem 3.1: for prime (p), (0<etale1/10), and a single (f:mathbb Z/pmathbb Z	o[-1,1]), there are coupled random variables (mathbf a,mathbf r) with
  [
  mathbb E f(mathbf a)=mathbb E_x f(x)+O(eta),
  ]
  [
  Lambda_{mathbf a,mathbf r}(f)ge(mathbb E f(mathbf a))^4-O(eta),
  ]
  and
  [
  mathbb P(mathbf r=0)ll exp(-eta^{-O(1)})/p.
  ]
- Lemma 3.2 supplies the positivity inequality underlying the fourth-power main term.
- The remark immediately after the proof of Theorem 1.1 records the earlier popular-difference form: for (gg_eta N) differences (r), the 4-AP density is at least ((|A|/N)^4-eta).

This is quantitatively powerful enough to recover the pointwise polylogarithmic bound, but it keeps all four factors equal to the same (f). It neither labels four prescribed fibers nor converts near-extremality of sibling fibers into a cross-fiber density loss.

### 4. Gowers 2020 rules out the tempting Fourier shortcut

Gowers, *A uniform set with fewer than expected arithmetic progressions of length 4*, Theorem 6: there are absolute (c>0,C) such that, for all sufficiently large (N), one can find a (CN^{-1/2}log N)-Fourier-uniform set (Asubsetmathbb Z_N) of density (1/2+o(1)) with
[
mathbb E_{x,d}1_A(x)1_A(x+d)1_A(x+2d)1_A(x+3d)
 le 2^{-4}-c.
]
Thus small nontrivial Fourier coefficients do not justify a random-model 4-AP count, even for one set. The paper's concluding Problem explicitly asks whether ordinary Fourier-uniformity at least forces a polynomial lower bound (alpha^{C}N^2) for 4-APs; it is not asserted as a theorem. Therefore a fiber argument based only on degree-1/Fourier uniformity is not source-supported.

### 5. Green 2026 confirms the present boundary

Green, *Arithmetic progressions at the Journal of the LMS*, Section 3 and Table 2, still records Green–Tao 2017,
[
r_4(N)ll N(log N)^{-c},
]
as the endpoint of the quantitative (r_4) progression. The survey explicitly states that we remain a long way from the Erdős sum-of-reciprocals conjecture for length (4) and that substantially new ideas appear necessary. No later source-level pointwise theorem in that survey supplies the required cross-fiber stability law.

### 6. Why counting/supersaturation alone does not yet have the right exponent

Even granting a random-scale four-fiber lower bound
[
Egg eta^4N^2
]
for the number of cross-fiber 4-APs, each point lies in only (O(N)) such progressions. The generic edge-count/max-degree argument therefore guarantees only an (Omega(eta^4N)) transversal/deletion cost. That is a power (4) mass penalty, while the protected frontier needs (eta^{1+	heta}N) with (1+	heta<2).

Accordingly, a raw Varnavides/counting theorem is not enough. The missing information must use the special fact that the fibers are individually near-extremal 4-AP-free sets and must control how their quadratic structures can or cannot coexist across the finite carry system.

## Adversarial checks

- **Carry mapping:** the translations (C_t=c_tN+B_{j_t}) remove the floor/carry mask exactly; no heuristic replacement of the carry cells is used.
- **Modular wrap:** choosing (P>8N) makes a modular progression with all four terms in ([0,4N)) an ordinary integer progression.
- **Degenerate progression:** for a genuinely cross-block compatible tuple, a mixed progression mapping to common difference zero would force all four original points to coincide across incompatible blocks, so it contributes nothing.
- **One-set versus four-function:** Green–Tao 2017 Theorem 3.1 and Green–Tao 2010 Theorem 1.12 are not silently promoted to four-fiber statements. The four-function authority is Gowers 2001 Theorem 3.2/Corollary 3.3 and Green–Tao 2010 Theorem 4.1.
- **Uniformity level:** ordinary Fourier uniformity is explicitly insufficient for the random 4-AP count by Gowers 2020 Theorem 6; the relevant norm level is (U^3)/degree-2 uniformity.
- **Quantitative check:** Gowers' mixed counting error is polynomial in the uniformity parameter, but no audited theorem turns the resulting nonuniformity into a deletion cost of exponent (<2).
- **Regularity correction:** Green–Tao 2010 is cited in its corrected 2020 arXiv version; the 4-AP system is translation-invariant and lies inside the corrected flag-condition regime.
- **Repository boundary:** only the immutable task and protected packet at commit 266b0857f3e13524ea9e69e2ef3bf4cd422503b5 were used from the campaign; no tranche-03 returns, intake threads, PRs, discussions, or later repository state were inspected.

## First defect

The first missing theorem is not a 4-AP counting lemma: an exact four-function counting lemma already exists. The defect is a **cross-fiber quadratic stability/transversal theorem** converting the forced (U^3)/quadratic structure of dense carry-compatible fibers into a loss of at least (calpha^{1+	heta}N) points, with (0<	heta<1), across a fixed number of sibling blocks.

## Frontier effect

E3-Q4-DENSITY-LOSS is narrowed from “find any cross-fiber theorem” to one named interface gap.

The source-supported implication now available is:
[
	ext{dense compatible fibers + sufficient }U^3	ext{ uniformity}
Longrightarrow
	ext{cross-fiber 4-AP}.
]
Consequently, global 4-AP-free gluing forces polynomial-scale quadratic nonuniformity on every sufficiently dense compatible quartet.

What is not source-supported is the next implication:
[
	ext{forced quadratic nonuniformity across the carry system}
Longrightarrow
D_{L,n}ge c,a_n^{1+	heta},qquad 	heta<1.
]
That is the precise bridge still missing. No parent theorem is proved.

## Next residual (maximum three sentences; evidence only)

Exact multi-function 4-AP counting is available at polynomial uniformity scale. The audited sources do not convert the quadratic structure forced on every dense compatible quartet into a transversal/mass deficit of order (a_n^{1+	heta}N) with (	heta<1). Green's 2026 survey still records Green–Tao 2017 as the (r_4) endpoint, consistent with this bridge lying beyond current pointwise technology.

## Sources with exact primary-source identifiers/links

1. W. T. Gowers, **“A new proof of Szemerédi's theorem,”** *Geometric and Functional Analysis* 11 (2001), 465–588. Theorem 3.2; Corollary 3.3. DOI: https://doi.org/10.1007/s00039-001-0332-9
2. Ben Green and Terence Tao, **“An arithmetic regularity lemma, associated counting lemma, and applications,”** corrected version arXiv:1002.2028v3. Theorems 1.2, 1.12, 4.1, 5.1. https://arxiv.org/abs/1002.2028 ; published chapter DOI: https://doi.org/10.1007/978-3-642-14444-8_7
3. Ben Green and Terence Tao, **“New bounds for Szemerédi's theorem, III: A polylogarithmic bound for (r_4(N)),”** arXiv:1705.01703v3. Theorems 1.1, 3.1; Lemma 3.2; remark following the derivation of Theorem 1.1. https://arxiv.org/abs/1705.01703
4. W. T. Gowers, **“A uniform set with fewer than expected arithmetic progressions of length 4,”** *Acta Mathematica Hungarica* (2020). Theorem 6 and concluding Problem. arXiv:2004.07598v2: https://arxiv.org/abs/2004.07598 ; DOI: https://doi.org/10.1007/s10474-020-01072-z
5. Ben Green, **“Arithmetic progressions at the Journal of the LMS,”** *Journal of the London Mathematical Society* 113 (2026), e70483. Section 3; Table 2. DOI: https://doi.org/10.1112/jlms.70483
