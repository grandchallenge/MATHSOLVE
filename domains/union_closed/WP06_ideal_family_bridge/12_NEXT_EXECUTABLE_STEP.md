# Next Executable Step

## Immediate Next Step

Select the next source-roadmap target that can consume the checked WP06 bridge
without weakening its hypotheses.

## Input

- MATHCERT checked theorem:

```lean
localIdealFamily_complement_frankl
```

- MATHSOLVE WP05 lattice-minimal-counterexample spine.
- WP03 source audit and known-bounds synthesis.

## Output

A short assessment file naming one of:

1. a source theorem whose hypotheses naturally produce a local ideal family;
2. a restricted class of union-closed families known to be complements of local
   ideal families;
3. a negative assessment explaining why WP06 should remain a standalone
   restricted theorem for now.

## Completion Test

The next target is ready only when its assessment includes:

- exact theorem statement;
- dependency on `UC-WP06-L008` or explicit reason not to use it;
- claim boundary;
- Lean or exact-certificate route;
- first formal lemma.

## Do Not Do Next

Do not broaden `localIdealFamily_complement_frankl` into a statement about all
union-closed families. That would erase the hypothesis that makes WP06 true.

