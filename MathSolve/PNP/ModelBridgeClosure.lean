import MathSolve.PNP.TM2ForwardCompiler
import MathSolve.PNP.ProgrammeTM2ReverseCompiler

/-!
# Constructive closure of the PNP machine-model bridge

This file instantiates the conditional class-equivalence theorem with the two
concrete quantitative compilers.  It closes only PNP-BRIDGE-MODEL-001.
-/

namespace MathSolve.PNP

/-- Exact class-extensional equivalence induced by the two constructive,
polynomial-overhead machine translators. -/
theorem importedTM2_iff_programmePolyTime_constructive
    (decision : List Bool → Bool) :
    ImportedTM2ComputableInPolyTime decision ↔
      ProgrammeComputableInPolyTime decision :=
  importedTM2_iff_programmePolyTime
    tm2ToProgrammeCompiler_constructive
    programmeToTM2Compiler_constructive
    decision

#print axioms importedTM2_iff_programmePolyTime_constructive

end MathSolve.PNP
