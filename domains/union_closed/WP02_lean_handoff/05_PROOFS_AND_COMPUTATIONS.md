# Proofs and Computations

## Support and Nontriviality

Support membership simplifies to an existential family-member witness.
Nontriviality follows by unpacking or constructing such a witness.

## Top Union

Induct over finite subfamilies. Each insertion step uses union-closure to
combine the inserted member with the already-constructed subfamily union.

## Powerset Sharpness

Pair subsets containing `x` with subsets of `U.erase x`: insert `x` to move
forward and erase `x` to recover the source.

## Singleton Case

Map each set without `a` to its union with `{a}`. Union-closure places the image
inside the family, and erasing `a` recovers the source.

## Reproducibility

From `MATHCERT/`:

```powershell
.\ci\check_lean.ps1
```

or:

```bash
./ci/check_lean.sh
```
