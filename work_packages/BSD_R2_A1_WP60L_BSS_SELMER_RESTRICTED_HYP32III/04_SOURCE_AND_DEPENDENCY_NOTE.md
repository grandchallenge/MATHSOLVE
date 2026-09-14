# WP60L source and proof-dependency note

## Protected sources

WP60L uses the following already-protected campaign facts.

1. **WP13 local inertia/Tamagawa theorem.** At an odd multiplicative prime of type `I_n`, the 2-adic inertia action is `[[1,n t(sigma)],[0,1]]`; the Tamagawa factor is odd exactly when `n` is odd.
2. **WP39 local comparison theorem.** At an odd bad place locally equal to `Q_ell`,
   `len_Z2(H^1(Q_ell,T)/H^1_ur(Q_ell,T))=ord_2(c_ell)`.
3. **WP60I.** A selected curve has an odd bad prime of odd inertia depth and hence a primitive unipotent inertia element.
4. **WP60J.** The selected 2-adic image is `GL_2(Z_2)`.
5. **WP60K.** `H^1(GL_2(Z/4),(Z/4)^2)` has order `2`, with explicit nonzero cocycle value `(0,2)` at the standard primitive upper unipotent.

## Burns–Sakamoto–Sano II interface

Primary source: Burns–Sakamoto–Sano, *On the theory of higher rank Euler, Kolyvagin and Stark systems, II: the general theory*, arXiv:1805.08448.

Relevant exact interfaces:

- §3.1.1 defines a dual Selmer local condition as the annihilator of the primal local condition under local Tate duality and propagates a local condition to quotient modules by taking the image of the original condition.
- §3.1.3 defines the modified structures `F_a^b(n)`. At every place in the original set `S`, the modified structure retains the original local condition; only auxiliary primes receive the zero/full/transverse modifications.
- Lemma 3.9 uses Hypothesis 3.2(iii) to make restriction to the finite auxiliary field injective before the Chebotarev argument. The separate counting hypothesis is `s+t<p`.
- Lemma 3.10 repeatedly invokes Lemma 3.9 on a **single nonzero class at a time** to prove coefficient-reduction injectivity for a free submodule `X`.
- The displayed downstream uses of Lemma 3.10 in §§4–5 apply it to free modified-Selmer modules, including the modules `H^1_{F^n}`, `H^1_{F^n}` at adjacent coefficient levels, and `H^1_{F(n)}`.
- §6.2 defines the canonical local condition at a finite place away from `p` as
  `ker(H^1(K_v,T)->H^1(K_v^ur,T tensor Q_p))`.
- Theorem 6.12 uses the canonical Selmer structure for the Euler-to-Kolyvagin construction.

Stable source URL:

`https://arxiv.org/html/1805.08448`

## Local Kummer self-duality interface

For an elliptic curve over a nonarchimedean local field, the Kummer exact sequence gives

`E(K_v)/nE(K_v) -> H^1(K_v,E[n])`.

Tate local duality and the Weil pairing identify the Kummer image with its own annihilator for the principally polarized elliptic curve. This is the standard local self-duality underlying the classical finite Selmer condition; it is valid for `n=4` and does not require an odd coefficient prime.

In the present application no equality between the BSS canonical and Kummer conditions is assumed abstractly. It is derived at the specific protected odd-depth prime:

1. WP13 makes `c_ell` odd;
2. WP39 makes `H^1(Q_ell,T)=H^1_ur(Q_ell,T)`;
3. hence the BSS canonical condition on `T` is all of `H^1(Q_ell,T)`;
4. its propagated image in `H^1(Q_ell,E[4])` is the local Kummer image;
5. Tate local duality then identifies the dual canonical condition with the same Kummer submodule under the Weil self-duality.

This local argument does not identify the global primal and dual Selmer structures and does not resurrect the invalid global primal/dual-identification shortcut rejected before WP60I.

## Exact dependency boundary

WP60L replaces only the **global restriction-injectivity contribution** of Hypothesis 3.2(iii) for canonical modified Selmer classes at coefficient level `E[4]`.

It does not change the independent BSS Lemma 3.9 requirement `s+t<p`. Therefore:

- one-class calls needed by the proof of Lemma 3.10 are available at literal `p=2`;
- simultaneous one-primal/one-dual localization is not supplied by this result;
- all-level inverse-limit control still requires an extension beyond `E[4]` or a different integral argument.
