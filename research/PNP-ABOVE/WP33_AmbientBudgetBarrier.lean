import PNPAbove.WP32Threshold

/-!
WP33: exact source-native negative test for an unqualified SAT witness-budget
transfer. An arbitrary ambient Fin m variable universe can be expanded without
changing the original finite-3CNF clause list or its compiled game index.
This is not a classical lower bound or P != NP.
-/
namespace PNPAbove.WP33
open MIPRE MIPRE.SAT

/-- A genuine original three-literal clause, mentioning only variable zero. -/
def repeatedZeroClause (n : Nat) : SAT.Clause3 (Fin (n + 1)) :=
  let z : Fin (n + 1) := ⟨0, Nat.zero_lt_succ n⟩
  let lit : SAT.Lit (Fin (n + 1)) := ⟨z, true⟩
  ⟨lit, lit, lit⟩

/-- The native finite-index input has the same encoded clauses for every n. -/
theorem repeatedZeroClause_encoded (n : Nat) :
    WP29.fromOriginal3CNF ([repeatedZeroClause n]) =
      [((0, true), (0, true), (0, true))] := by
  rfl

/-- No indexer depending ONLY on the explicit clause list can furnish a
uniform bound on the ambient variable cardinality. The counterfamily is
NONEMPTY and satisfiable; increasing n introduces unused variables. -/
theorem no_uniform_budget_nonempty
    (index : WP29.Enc3CNF → Nat) (lam : Nat) :
    ∃ n : Nat,
      ¬ n + 1 ≤
        (2 ^ index (WP29.fromOriginal3CNF
          ([repeatedZeroClause n]))) ^ lam := by
  let budget := (2 ^ index
    ([((0, true), (0, true), (0, true))] : WP29.Enc3CNF)) ^ lam
  refine ⟨budget, ?_⟩
  rw [repeatedZeroClause_encoded]
  omega

/-- Instantiation to the actual native source-polynomial WP29 SAT game
index; it refutes the missing unqualified hypothesis in WP30. -/
theorem native_index_budget_not_uniform (lam : Nat) :
    ∃ n : Nat,
      ¬ n + 1 ≤
        (2 ^ WP29.source3CNFIndexProgram
          (WP29.fromOriginal3CNF
            ([repeatedZeroClause n]))) ^ lam :=
  no_uniform_budget_nonempty WP29.source3CNFIndexProgram lam


/-- This is an actual SAT yes-instance of the original MIPRE 3CNF,
not an empty-formula or unsatisfiable degeneracy. -/
theorem repeatedZeroClause_satisfiable (n : Nat) :
    ∃ w : Fin (n + 1) → Bool,
      (WP24.threeCNFSet ([repeatedZeroClause n])).Sat w := by
  refine ⟨fun _ => true, ?_⟩
  rw [WP24.original_3CNF_sat_iff]
  simp [WP24.from3CNF, WP24.clauseFormula, WP24.literalFormula,
    repeatedZeroClause, WP24.bitsAt, SAT.Fml.eval]

/-- The same genuine polynomial-time source compiler emits one constant
binary game index throughout the unbounded ambient-variable family. -/
theorem native_compiled_index_invariant (n : Nat) :
    WP29.source3CNFIndexProgram (WP29.fromOriginal3CNF
      ([repeatedZeroClause n])) =
    WP29.source3CNFIndexProgram
      ([((0, true), (0, true), (0, true))] : WP29.Enc3CNF) := by
  rw [repeatedZeroClause_encoded]

/-- Even the ACTUAL threshold-normalized, source-polynomial compressor
input of WP32 has no universal native assignment budget if the ambient
Fin m variable count is not itself part of the encoded clause input. -/
theorem normalized_index_budget_not_uniform
    (G : MIPRE.GapCompression) (lam : Nat) :
    ∃ n : Nat,
      ¬ n + 1 ≤ (2 ^ WP32.normalizedIndexProgram G.C₀
        (WP29.fromOriginal3CNF
          ([repeatedZeroClause n]))) ^ lam :=
  no_uniform_budget_nonempty (WP32.normalizedIndexProgram G.C₀) lam

/-- Stronger separation: at that counterexample the actual original
compressor's numeric minimum-index obligation DOES hold. Thus WP32's
threshold repair cannot discharge the distinct witness-budget premise. -/
theorem threshold_holds_while_budget_fails
    (G : MIPRE.GapCompression) (lam : Nat) :
    ∃ n : Nat,
      G.C₀ ≤ WP32.normalizedIndexProgram G.C₀
        (WP29.fromOriginal3CNF ([repeatedZeroClause n])) ∧
      ¬ n + 1 ≤ (2 ^ WP32.normalizedIndexProgram G.C₀
        (WP29.fromOriginal3CNF
          ([repeatedZeroClause n]))) ^ lam := by
  obtain ⟨n, hfail⟩ := normalized_index_budget_not_uniform G lam
  exact ⟨n, WP32.normalizedIndex_threshold G.C₀ _, hfail⟩

end PNPAbove.WP33
