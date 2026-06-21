# Lay Companion

## What Is the Object?

A family of sets is a collection whose members are themselves finite sets. In
Frankl's conjecture, the family is union-closed: whenever two sets are present,
their union is also present. The conjecture predicts that some element appears
in at least half of the sets.

An ideal family points in the opposite direction. It is downward closed: once a
set is present, all smaller sets inside it are present too. Downward closure is
often easier to count because removing elements keeps us inside the family.

WP06 studies a bridge between these two worlds. If `F` is an ideal family on a
ground set `U`, then the complements `U \ S` of its members form a union-closed
family. The checked theorem says this complement family satisfies the Frankl
half-frequency conclusion.

## Why Does This Matter?

This gives the campaign a certified corridor:

```text
ideal family
  -> average rarity
  -> complement family
  -> union-closed abundance
```

The corridor is narrow but trustworthy. It lets later work use ideal-family
structure without pretending that ideal families cover every union-closed
family.

## What Actually Changed?

Earlier, the project had an audited external ideal-family source, but the
external proof surface was not clean enough to import as trusted proof. WP06
rebuilds the needed theorem locally:

1. translate MATHCERT's finite-family representation into a predicate-style
   ideal-family surface;
2. prove an NDS nonpositivity theorem by trace and contraction;
3. derive average rarity;
4. pass through complement duality to obtain a Frankl-abundant union-closed
   family.

## What Did This Package Not Achieve?

It did not solve the full conjecture. The result applies only when the
union-closed family is presented as the complement of a local ideal family.

That boundary is the point: the package is useful because its claim is exact.

