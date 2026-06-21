# Result Status

| Field | Status |
|---|---|
| Result status | Checked restricted theorem |
| Conditional on | Finite local family satisfying `IsIdealFamilyOn F U` |
| Strongest supported claim | Every local ideal family is average-rare; the complement family is union-closed, nontrivial, and Frankl-abundant. |
| Not claimed | This is not a proof of Frankl's conjecture for arbitrary union-closed families. It does not import the upstream ideal-family repository as a trusted dependency. |
| Computation class | `CONTINUUM_PROOF` for the finite ideal-family theorem in Lean; exact finite replay remains separate WP04/WP05 infrastructure. |
| Certification state | Formally checked in MATHCERT by Lean, with the full MATHCERT gate passing. |
| First executable step | Select the next source-roadmap target that consumes the checked ideal-family bridge without broadening its hypotheses. |

## Trust Quartet

### What Is Proved?

For a finite local family `F` over a finite ground `U`, if `F` satisfies the
local ideal-family hypotheses, then:

- `F` is average-rare;
- some ground element is rare;
- the complement family on `U` is union-closed;
- that complement family is Frankl-abundant.

### What Is Checked?

The checked Lean boundary is in MATHCERT:

- `localIdealFamily_port_nds_nonpos`
- `localIdealFamily_averageRare`
- `localIdealFamily_exists_rare`
- `complementFamilyOn_unionClosed_of_ideal`
- `complementFamilyOn_abundant_of_exists_rare`
- `localIdealFamily_complement_frankl`
- `localIdealFamily_complement_averageAbundant`

### What Remains Open?

Frankl's conjecture for arbitrary finite union-closed families remains open.
The WP06 theorem covers complements of local ideal families, not every
union-closed family.

### What Requires External Verification?

The upstream ideal-family Lean repository remains provenance only. Its audited
proof surface had placeholders at the recorded commit. The local MATHCERT proof
does not depend on importing that repository.

