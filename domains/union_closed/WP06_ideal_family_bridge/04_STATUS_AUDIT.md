# Status Audit

## Checked Locally

MATHCERT now checks the following WP06 mathematical surface:

| Claim ID | Status | Support |
|---|---|---|
| `UC-WP06-L001` | Checked | Conditional average-rarity bridge from NDS nonpositivity |
| `UC-WP06-L002` | Checked | Rare-vertex theorem for local ideal families |
| `UC-WP06-L003` | Checked | Rare vertex is not enough for average rarity |
| `UC-WP06-L004` | Checked | NDS support and summation layer |
| `UC-WP06-L005` | Checked | Trace and contraction infrastructure |
| `UC-WP06-L006` | Checked | Exact NDS trace-difference formula |
| `UC-WP06-L007` | Checked | Local NDS nonpositivity and average rarity |
| `UC-WP06-L008` | Checked | Complement duality to union-closed abundance |

## External Source Status

The external `kashiwabarakenji/frankl_lean` repository is recorded as source
provenance in:

```text
MATHSOLVE/external_audits/frankl_lean/BUILD_AUDIT.md
```

It is not a trusted dependency for WP06. The local theorem is supplied by
MATHCERT's checked Lean development.

## Certification Status

The MATHCERT gate passed after the WP06 theorem and positioning repair:

```powershell
.\ci\check_lean.ps1
```

That gate includes:

- `lake build`;
- claim-ledger validation and rejection tests;
- exact certificate replay;
- finite-lattice certificate replay;
- proof-placeholder scan.

## Claim Boundary

The strongest public sentence is:

> Complements of finite local ideal families satisfy Frankl abundance, checked
> in MATHCERT.

The sentence that must not be said is:

> Frankl's conjecture is proved.

