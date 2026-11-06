# FIGURATE WP09-021 — four further exact Pell seeds in the local-positive frontier

**Result:** exact global positive-integer Type B seeds for $(k,c)=(164,2),(196,2),(228,2),(244,2) and an infinite family for each by the protected WP09-013 fixed-first-pair theorem. These are internal producer results; independent MATHCERT certification and external literature-priority review remain separate.

All four use the same simple first pair $a=1,b=k-2$ at $r=2$. Thus $ab+2=k=P_k(2)$, and $ab=k-2\equiv2\pmod{16}$ is nonsquare. For each order, the exact generalized Pell equation is

$$
X^2-(k-2)S^2=-(k-3)\Delta,\qquad
\Delta=8(k-2)\cdot2+(k-4)^2.
$$

The index lattice is $X\equiv S\equiv-(k-4)\pmod{2(k-2)}$. The following exact norm-one units and base points reach that lattice after the stated number of multiplications.

## Exact seeds

| $k$ | Base $(X_0,S_0)$ | Norm-one unit $U+V\sqrt{k-2}$ | Steps | Exact entries $(a,b,d)$ | Exact indices $(r,s,t)$ |
|---:|---:|---:|---:|---|---|
| 164 | (72416,5692) | $19601+1540\sqrt{162}$ | 10 | $(1,162,1836121501245313459201105265351598082818875949658621767286039188898783862293751029833171846480207)$ | $(2,150559512094191202263080416902498580002799945223,1916309735530931053564867150002683761037880788624)$ |
| 196 | (4828080,346636) | $195+14\sqrt{194}$ | 57 | $(1,194,1861637983352910478332422493090790557754819720194059827736039781602322511404658713751540177183098120083143518905342241076032583581843605923512027394894416748969526982684022665941082186809473450846814976522255962913193828554794179112082417778780391375417967908151141282000170817541090432836063745008545791)$ | $(2,4380883947136402700586746790958792422295427646187932484676301736278832263491460430483284850945583202509843690587848188211493815154022913478915407484929,61018652612998764549054276449065927822082955343561839406306767388371576134998015687440456690641764810756378102205851485520882945774726786004854529584936)$ |
| 228 | (10227632,680332) | $451+30\sqrt{226}$ | 20 | $(1,226,4135076004125881964081534678574280030936826509978897581237657996084488167501078896386290481361116732493241541812463627556817879)$ | $(2,191294518888718325116085513250154542769546032200994618246324203,2875787198012357090297283648222837808215328100704980620737262228)$ |
| 244 | (11376,772) | $19601+1260\sqrt{242}$ | 44 | $(1,242,47450018344721036787155891543128483176999156028998762109548545160501040074695804477514545890135739315114460797122999239048236001346664660993872431380065259126031051673515589630601691668616512134260494202370291229455892350663635486105782528376894321430827196039254726763428551070043145699501831461292915993983146916027429654517062393043447408713347871648328691981559886218373490162934671966131873706085929527)$ | $(2,19802750110523620886422909562876709287688831270665377691020462345437437471227800880131611725827348155662406201301558860059460728708283212065565050541843635291693356286838295235063190626883400844453566053,308058495564465927576011172313248943740213758117809647465817511615842005459106585517859363501213795922962354612058250760679901185870977779744448500550177643366536563947676258166298092540026347361370558264)$ |

The exact pair equations are checked directly by the independent standard polygonal polynomial $P_k(n)=n+(k-2)n(n-1)/2$. The third entries have 97, 304, 127 and 407 decimal digits, respectively.

## Pell and amplification checks

For each row, the base point satisfies

$$
X_0^2-(k-2)S_0^2=-(k-3)\Delta,
$$

and the displayed unit has norm one. The repeated unit multiplication gives positive coordinates in the required index lattice. Recover

$$
s=\frac{S+k-4}{2(k-2)},\qquad
t=\frac{X+k-4}{2(k-2)},\qquad
d=P_k(s)-2.
$$

Exact substitution verifies $P_k(2)=k=ab+2$, $P_k(s)=d+2$, and $P_k(t)=(k-2)d+2$.

Since $ab=k-2$ is nonsquare, WP09-013 Theorem A proves infinitely many exact triples with the same first pair for every row. The least identity exponents of the chosen units modulo the corresponding amplification lattice moduli are:

| $k$ | Modulus $M=2aR$ | Unit order modulo $M$ | Next family third-entry digits |
|---:|---:|---:|---:|
| 164 | 648 | 162 | 1,585 |
| 196 | 776 | 388 | 2,314 |
| 228 | 904 | 452 | 2,799 |
| 244 | 968 | 242 | 2,630 |

The modular orders are obtained by exact recurrence over every smaller positive exponent. The next family member for each row is independently reconstructed and all three pair equations are checked.

## Scope and interpretation

The protected WP09-012 classifier identifies these four parameter pairs as compatible at every positive modulus. This batch adds exact integer solutions; it does not establish that every locally compatible pair has an integer solution. Nor does it prove a universal local-to-global theorem. It is a finite set of constructive examples. WP09-018 and WP09-019 separately solved $(84,2)$ and $(100,2)$; WP09-020 separately solved $(132,2)$.

## Reproduction

- Constructor: [research/figurate_wp09_local_positive_seed_batch_021.py](https://github.com/grandchallenge/MATHSOLVE/blob/main/research/figurate_wp09_local_positive_seed_batch_021.py)
- Independent tests: [tests/test_figurate_wp09_local_positive_seed_batch_021.py](https://github.com/grandchallenge/MATHSOLVE/blob/main/tests/test_figurate_wp09_local_positive_seed_batch_021.py)
- Amplification theorem: [WP09-013 dossier](https://github.com/grandchallenge/MATHSOLVE/blob/main/work_packages/FIGURATE_WP09_GENERAL_FIRST_PAIR_PELL_013.md)

Run:

    python3 -m unittest -v tests.test_figurate_wp09_local_positive_seed_batch_021
    python3 -m research.figurate_wp09_local_positive_seed_batch_021 --order 164
    python3 -m research.figurate_wp09_local_positive_seed_batch_021 --order 196
    python3 -m research.figurate_wp09_local_positive_seed_batch_021 --order 228
    python3 -m research.figurate_wp09_local_positive_seed_batch_021 --order 244

No independent MATHCERT certification or external originality/priority claim is made.
