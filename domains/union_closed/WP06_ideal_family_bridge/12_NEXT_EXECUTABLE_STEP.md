# Next Executable Step

## Immediate Next Step

Selected: assess the restricted class of union-closed families that are
explicitly represented as complements of local ideal families.

Assessment:

- `COMPLEMENT_CLASS_NEXT_TARGET_ASSESSMENT.md`

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

The selected output is type **(2)**. The functional-preorder branch remains
deferred because preorder order ideals are not automatically subset-downward
closed in the sense required by `IsIdealFamilyOn`.

## Completion Test

The next target is ready only when its assessment includes:

- exact theorem statement;
- dependency on `UC-WP06-L008` or explicit reason not to use it;
- claim boundary;
- Lean or exact-certificate route;
- first formal lemma.

The assessment satisfies this test by naming:

- exact theorem statement:
  `complementOfLocalIdealFamily_frankl`;
- dependency on `UC-WP06-L008`:
  direct wrapper around `localIdealFamily_complement_frankl`;
- claim boundary:
  restricted complement class only;
- Lean route:
  one-step wrapper in MATHCERT;
- first formal lemma:
  unpack an existential complement representation and rewrite by equality.

## Do Not Do Next

Do not broaden `localIdealFamily_complement_frankl` into a statement about all
union-closed families. That would erase the hypothesis that makes WP06 true.

