# WP60M source and proof-dependency note

## Protected inputs

WP60M uses only already-protected campaign facts plus an explicit finite group-cohomology argument.

1. **WP13.** At an odd multiplicative prime of odd inertia depth, the Tamagawa factor is odd and the compatible 2-adic inertia image contains the primitive upper unipotent.
2. **WP39.** At an odd bad place, `len_Z2(H^1(Q_ell,T)/H^1_ur(Q_ell,T))=ord_2(c_ell)`. Thus the protected odd-depth prime has no 2-primary local comparison defect.
3. **WP60I.** A fixed selected odd bad prime of odd inertia depth exists.
4. **WP60J.** The selected 2-adic image is `GL_2(Z_2)`.
5. **WP60K.** The mod-4 natural-module cohomology group has order two and an explicit nonzero cocycle with primitive-unipotent value `(0,2)`.
6. **WP60L.** At mod 4 the unique defect is excluded from the canonical primal and dual local conditions at the fixed odd-depth prime, and the BSS Lemma 3.10 one-class coefficient-reduction use survives.

## BSS II interfaces retained

Primary source already admitted by protected MATHFORGE: Burns–Sakamoto–Sano, *On the theory of higher rank Euler, Kolyvagin and Stark systems, II: the general theory*, arXiv:1805.08448.

WP60M uses the same protected source interfaces as WP60L:

- the finite auxiliary field `K(A)_M` and Hypothesis 3.2(iii);
- propagation of canonical local conditions to quotient coefficient modules;
- modified Selmer structures `F_a^b(n)`, which retain the original canonical condition at every original bad prime;
- Lemma 3.9, where Hypothesis 3.2(iii) supplies restriction injectivity separately from the counting condition `s+t<p`;
- Lemma 3.10, whose proof invokes Lemma 3.9 one nonzero class at a time for coefficient reduction.

No claim is made that the unchanged global Hypothesis 3.2(iii) becomes true. WP60M replaces only its restriction-injectivity role on the actual canonical modified Selmer spaces.

## New algebraic input in WP60M

For `m>=2`, put `G_m=GL_2(Z/2^m)` and `V_m=(Z/2^m)^2`. The new proof has three internal steps.

1. The central scalar `-I` normalizes every class in `H^1(G_m,V_m)` to a cocycle valued in the top 2-torsion layer `V_m[2]`.
2. Inflation-restriction for the principal congruence kernel reduces the upper bound to `G_1`-equivariant homomorphisms into the residual natural module. Squares kill the deeper congruence filtration; the only surviving first layer contributes a one-dimensional equivariant Hom space.
3. Scaling the protected WP60K cocycle gives a nonzero class at every level, detected by the same primitive upper-unipotent inertia element.

The executable certificate checks the finite residual representation-theoretic assertions used in step 2 and the scaled cocycle's primitive-unipotent value.

## Local duality boundary

At the fixed protected odd-depth multiplicative prime, odd Tamagawa depth makes the propagated canonical finite local condition equal to the finite local Kummer image. Tate local duality and the Weil pairing make this Kummer image self-annihilating. This local statement is sufficient to exclude the unique global defect from both primal and dual modified Selmer groups.

It does not identify the global primal and dual Selmer structures.

## Remaining independent obstruction

The BSS Lemma 3.9 counting condition `s+t<p` is unchanged. WP60M therefore does not supply simultaneous one-primal/one-dual localization at `p=2`, does not exclude the protected WP60H three-term relation, and does not prove core-vertex connectivity or integral BSS Fitting control.
