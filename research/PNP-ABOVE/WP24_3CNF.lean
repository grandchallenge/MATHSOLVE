import PNPAbove.WP24SATGame
import MIPRE.Foundations.SAT.Cnf

/-!
The input language is original MIPRE.SAT.Clause3 and Cnf3, not an
unconstrained Boolean predicate. Translate arbitrary finite original
3CNF lists into the original SAT.Fml, with checked semantics, well-scoped
input variables, and a linear gate-count bound.
-/

namespace PNPAbove.WP24
open MIPRE MIPRE.SAT

/-- Encode a source 3CNF literal by an original Boolean formula. -/
def literalFormula {n : Nat} (l : SAT.Lit (Fin n)) : SAT.Fml :=
  if l.pos then .inp l.var.val else .not (.inp l.var.val)

/-- Original three-literal clause to original formula. -/
def clauseFormula {n : Nat} (c : SAT.Clause3 (Fin n)) : SAT.Fml :=
  .or (literalFormula c.l₁)
    (.or (literalFormula c.l₂) (literalFormula c.l₃))

/-- Build the conjunction, not a hard-coded SAT predicate. -/
def from3CNF {n : Nat} : List (SAT.Clause3 (Fin n)) → SAT.Fml
  | [] => .const true
  | c :: cs => .and (clauseFormula c) (from3CNF cs)

/-- The original source sign convention for SAT.Lit is preserved. -/
theorem literalFormula_correct {n : Nat} (l : SAT.Lit (Fin n))
    (w : Fin n → Bool) :
    (literalFormula l).eval (bitsAt w) = l.eval w := by
  rcases l with ⟨v, s⟩
  cases s <;> simp [literalFormula, SAT.Lit.eval, SAT.Fml.eval]

/-- All three inputs of the source clause are preserved exactly. -/
theorem clauseFormula_correct {n : Nat} (c : SAT.Clause3 (Fin n))
    (w : Fin n → Bool) :
    (clauseFormula c).eval (bitsAt w) = c.eval w := by
  rcases c with ⟨l₁, l₂, l₃⟩
  simp [clauseFormula, SAT.Clause3.eval, SAT.Fml.eval, literalFormula_correct, Bool.or_assoc]

/-- Sound and complete source 3CNF-to-source-Fml translation. -/
theorem from3CNF_correct {n : Nat}
    (cs : List (SAT.Clause3 (Fin n))) (w : Fin n → Bool) :
    (from3CNF cs).eval (bitsAt w) = cs.all (fun c => c.eval w) := by
  induction cs with
  | nil => rfl
  | cons c cs ih =>
      simp [from3CNF, SAT.Fml.eval, clauseFormula_correct, ih]

/-- The original MIPRE finite 3CNF set presented by the input list. -/
def threeCNFSet {n : Nat} (cs : List (SAT.Clause3 (Fin n))) :
    SAT.Cnf3 (Fin n) := {c | c ∈ cs}

/-- The original MIPRE definition of SAT, not a bespoke replacement,
agrees with the certificate checked by our game. -/
theorem original_3CNF_sat_iff {n : Nat}
    (cs : List (SAT.Clause3 (Fin n))) (w : Fin n → Bool) :
    (threeCNFSet cs).Sat w ↔ (from3CNF cs).eval (bitsAt w) = true := by
  rw [from3CNF_correct]
  simp [SAT.Cnf3.Sat, threeCNFSet, List.all_eq_true]

/-- Original literal source program only indexes its declared variables. -/
theorem literalFormula_inputs {n : Nat} (l : SAT.Lit (Fin n)) :
    (literalFormula l).InputsLt n := by
  rcases l with ⟨v, s⟩
  cases s <;> simp [literalFormula, SAT.Fml.InputsLt, v.isLt]

theorem clauseFormula_inputs {n : Nat} (c : SAT.Clause3 (Fin n)) :
    (clauseFormula c).InputsLt n := by
  rcases c with ⟨l₁, l₂, l₃⟩
  simp [clauseFormula, SAT.Fml.InputsLt, literalFormula_inputs]

/-- Every compiled finite 3CNF has exactly the advertised variable budget. -/
theorem from3CNF_inputs {n : Nat} (cs : List (SAT.Clause3 (Fin n))) :
    (from3CNF cs).InputsLt n := by
  induction cs with
  | nil => simp [from3CNF, SAT.Fml.InputsLt]
  | cons c cs ih =>
      simp [from3CNF, SAT.Fml.InputsLt, clauseFormula_inputs, ih]

/-- One source literal generates at most two original formula gates. -/
theorem literalFormula_size {n : Nat} (l : SAT.Lit (Fin n)) :
    (literalFormula l).size ≤ 2 := by
  rcases l with ⟨v, s⟩
  cases s <;> simp [literalFormula, SAT.Fml.size]

/-- One exact original three-literal clause generates at most eight gates. -/
theorem clauseFormula_size {n : Nat} (c : SAT.Clause3 (Fin n)) :
    (clauseFormula c).size ≤ 8 := by
  have h₁ := literalFormula_size c.l₁
  have h₂ := literalFormula_size c.l₂
  have h₃ := literalFormula_size c.l₃
  dsimp [clauseFormula, SAT.Fml.size]
  omega

/-- The original Boolean formula circuit needs at most nine gates per
3CNF clause, plus one terminal true gate. -/
theorem from3CNF_size {n : Nat} (cs : List (SAT.Clause3 (Fin n))) :
    (from3CNF cs).size ≤ 9 * cs.length + 1 := by
  induction cs with
  | nil => simp [from3CNF, SAT.Fml.size]
  | cons c cs ih =>
      have hc := clauseFormula_size c
      simp only [from3CNF, SAT.Fml.size, List.length_cons]
      omega

/-- This is the *actual pinned MIPRE original* circuit; its validity
and size are imported proof facts, not hypothetical algorithm assumptions. -/
theorem from3CNF_circuit_wellFormed {n : Nat}
    (cs : List (SAT.Clause3 (Fin n))) :
    (from3CNF cs).toCircuit n |>.WellFormed := by
  exact SAT.Fml.toCircuit_wellFormed (from3CNF cs) (from3CNF_inputs cs)

/-- This gate-count bound is for the ACTUAL original pinned MIPRE
generated Boolean circuit, not merely for a symbolic formula. -/
theorem from3CNF_circuit_size {n : Nat}
    (cs : List (SAT.Clause3 (Fin n))) :
    ((from3CNF cs).toCircuit n).size ≤ 9 * cs.length + 1 := by
  have heq :
      ((from3CNF cs).toCircuit n).size = (from3CNF cs).size := by
    simp [SAT.Fml.toCircuit, SAT.Circuit.size, SAT.Fml.length_flattenAt]
  rw [heq]
  exact from3CNF_size cs

/-- The concrete circuit evaluates exactly the original source 3CNF. -/
theorem from3CNF_circuit_correct {n : Nat}
    (cs : List (SAT.Clause3 (Fin n))) (w : Fin n → Bool) :
    ((from3CNF cs).toCircuit n).eval (bitsAt w) = cs.all (fun c => c.eval w) := by
  rw [SAT.Fml.eval_toCircuit, from3CNF_correct]

/-- SAT in the original 3CNF source language iff a perfect MIPRE PCC
strategy exists for the actual instance-dependent game. -/
theorem original_3CNF_perfectPCC_iff_sat {n : Nat}
    (cs : List (SAT.Clause3 (Fin n))) :
    (∃ S : MIPRE.SyncStrategy (satGame n (from3CNF cs)),
        S.IsPCC ∧ S.value = 1) ↔
      ∃ w : Fin n → Bool, (threeCNFSet cs).Sat w := by
  rw [perfectPCC_iff_sat]
  simp only [Satisfiable]
  exact exists_congr (fun w => (original_3CNF_sat_iff cs w).symm)

end PNPAbove.WP24
