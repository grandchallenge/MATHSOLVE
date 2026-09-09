# Chao Li Assumption 4.1 — exact selected-class matrix

Let `E/Q` satisfy the protected `BSD-R2-A1` hypotheses and let

`K = Q(sqrt(D))`

be a WP09 auxiliary field.

The admitted Chao Li source uses the following fixed hypotheses before its rank-lowering obstruction theorem. This file classifies each one against the protected Solve state.

| Source condition | Selected-class disposition | Reason |
|---|---|---|
| residual representation `rho_bar_{E,2}` is surjective | `AUTOMATIC` | WP12 eliminates the `C3` branch, so irreducibility forces image `GL_2(F_2) ~= S3` |
| `E` has good or multiplicative reduction at `2` | `AUTOMATIC` | selected hypothesis is the stronger good ordinary reduction at `2` |
| Serre conductor of `rho_bar` equals the odd part of `N` | `RESTRICTIVE` | selected `N` is odd; WP13 proves this is equivalent to every bad `c_ell` being odd |
| if `2` does not divide `N`, `rho_bar|G_Q2` is nontrivial | `RESTRICTIVE` | selected `N` is odd, but neither good ordinarity nor global surjectivity implies this local condition |
| `q` is a mod-2 level-raising prime | `CONSTRUCTIBLE` | `02_LEVEL_RAISING_Q_LEMMA.md` constructs infinitely many suitable `q` |
| every prime dividing `N` splits in the imaginary quadratic field `K` | `AUTOMATIC_EXISTENTIAL` | WP09 supplies such a `K`, in fact with `2` split as well |
| `q` is inert in `K` | `CONSTRUCTIBLE` | built simultaneously with the order-two residual Frobenius condition in `02_LEVEL_RAISING_Q_LEMMA.md` |
| Theorem 7.1 order-two residual Frobenius at `q` | `CONSTRUCTIBLE` | same Chebotarev construction |
| `s_2(E/K)=1` | `RESTRICTIVE` | `03_MINIMAL_SELMER_REDUCTION.md` proves this is equivalent here to `Sha(E/K)[2]=0` |

## The residual-conductor split

WP13 gives

`N(rho_bar_{E,2}) = product_{ell|N, c_ell odd} ell`.

Because the selected conductor is squarefree and odd,

`N(rho_bar_{E,2})=N`

if and only if

`ord_2(c_ell)=0` for every `ell|N`.

Thus Chao Li's source theorem applies, at best, to the WP13 residual-conductor-unchanged regime. It does not cover any selected curve with an even bad-prime Tamagawa factor.

## The local-at-2 condition is genuinely separate

The source itself warns that its nontrivial local restriction at `2` cannot simply be omitted. Its Remark 6.2 gives the curve labelled `2351a1`,

`y^2 + x y + y = x^3 - 5x - 5`,

with trivial residual restriction to `G_Q2`.

The elementary invariants of this model show why this is a useful structural witness for the independence of the local condition:

- the discriminant is `-2351`, so the curve has good reduction at `2`;
- direct reduction modulo `2` gives `#E(F_2)=2`, hence `a_2=1`, so the reduction is ordinary;
- the 2-division polynomial is

  `4x^3 + x^2 - 18x - 19`;

- it is irreducible over `Q` and has discriminant `-37616 = -16*2351`, which is not a square;
- hence its splitting field has Galois group `S3`, so the global mod-2 representation is surjective.

Therefore good ordinary reduction at `2` plus global residual surjectivity does not imply the source's local nontriviality condition.

This witness is used only for logical independence of source hypotheses. WP14 makes no assertion about its analytic rank and does not promote it to a `BSD-R2-A1` instance.

## Net applicability class

After WP12 and WP13, the source's surviving fixed restrictions are at least:

1. all bad-prime Tamagawa numbers are odd;
2. `rho_bar|G_Q2 != 1`;
3. after a WP09 field `K` is chosen, `Sha(E/K)[2]=0` if Theorem 7.1 is to be invoked in its `s_2(E/K)=1` rank-one form.

The auxiliary prime `q` is not an additional existential blocker: it can be constructed once the fixed data satisfy the source assumptions.
