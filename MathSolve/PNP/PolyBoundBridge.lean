import Mathlib.Algebra.Polynomial.Eval.Degree
import Mathlib.Tactic

/-!
# PNP polynomial-bound presentation bridge

This file implements `PNP-BRIDGE-POLYBOUND-001` only.

The protected Programme contract measures a total natural-number runtime cost on
finite binary strings, uses `List Bool.length` as the exact input-size measure,
and admits an eventual worst-case bound `c * n^k` after a finite threshold.
`ProgrammePolynomialBound` records that contract together with an explicit
uniform cap for the finitely many exceptional input lengths below the threshold.
The cap is bookkeeping for finite exceptions; it does not change the asymptotic
machine or cost model.

The imported presentation is the `Polynomial Nat` evaluation bound used by the
pinned Formal Conjectures P/NP definitions.  This file proves equivalence of the
bound presentations only.  It does not define a Turing machine, simulate TM2,
or identify the imported and Programme complexity classes.
-/

namespace MathSolve.PNP

/-- Total step cost on the exact finite-binary input carrier. -/
abbrev BinaryRuntimeCost := List Bool → Nat

/-- Imported `Polynomial Nat` presentation, with exact encoded length `input.length`. -/
def ImportedPolynomialBound (cost : BinaryRuntimeCost) : Prop :=
  ∃ p : Polynomial Nat, ∀ input, cost input ≤ p.eval input.length

/--
Programme eventual-polynomial presentation.

`threshold` separates the finite exceptional prefix from the eventual regime.
`lowCap` explicitly absorbs every exceptional input length.  The eventual clause
uses the protected `c * n^k` orientation and the same exact bit-length measure.
-/
def ProgrammePolynomialBound (cost : BinaryRuntimeCost) : Prop :=
  ∃ constant exponent threshold lowCap : Nat,
    (∀ input, input.length < threshold → cost input ≤ lowCap) ∧
    (∀ input, threshold ≤ input.length →
      cost input ≤ constant * input.length ^ exponent)

/--
A natural-coefficient polynomial is dominated, from length one onward, by the
sum of its coefficients times the highest power occurring in the polynomial.
The sum of coefficients is exactly `p.eval 1`.
-/
theorem polynomial_eval_le_eval_one_mul_pow_natDegree
    (p : Polynomial Nat) {n : Nat} (hn : 1 ≤ n) :
    p.eval n ≤ p.eval 1 * n ^ p.natDegree := by
  rw [Polynomial.eval_eq_sum_range, Polynomial.eval_eq_sum_range]
  simp only [one_pow, mul_one]
  rw [Finset.sum_mul]
  apply Finset.sum_le_sum
  intro i hi
  apply Nat.mul_le_mul_left
  have hiDegree : i ≤ p.natDegree := by
    have hiRange : i < p.natDegree + 1 := Finset.mem_range.mp hi
    omega
  exact Nat.pow_le_pow_right (by omega) hiDegree

/--
Every imported `Polynomial Nat` bound yields the exact Programme presentation.
The only length below threshold `1` is length `0`, which is bounded explicitly
by `p.eval 0`; no finite exceptional length is discarded.
-/
theorem importedPolynomialBound_to_programmePolynomialBound
    {cost : BinaryRuntimeCost} (h : ImportedPolynomialBound cost) :
    ProgrammePolynomialBound cost := by
  rcases h with ⟨p, hp⟩
  refine ⟨p.eval 1, p.natDegree, 1, p.eval 0, ?_, ?_⟩
  · intro input hlen
    have hzero : input.length = 0 := by omega
    simpa [hzero] using hp input
  · intro input hlen
    exact (hp input).trans
      (polynomial_eval_le_eval_one_mul_pow_natDegree p hlen)

/--
Every Programme witness yields one natural-coefficient polynomial that bounds
all lengths.  The constant term absorbs the full finite exceptional prefix and
the monomial supplies the eventual `c * n^k` bound.
-/
theorem programmePolynomialBound_to_importedPolynomialBound
    {cost : BinaryRuntimeCost} (h : ProgrammePolynomialBound cost) :
    ImportedPolynomialBound cost := by
  rcases h with ⟨constant, exponent, threshold, lowCap, hlow, heventual⟩
  refine ⟨Polynomial.C lowCap + Polynomial.C constant * Polynomial.X ^ exponent, ?_⟩
  intro input
  have hbound : cost input ≤ lowCap + constant * input.length ^ exponent := by
    by_cases hlt : input.length < threshold
    · exact (hlow input hlt).trans (Nat.le_add_right _ _)
    · have hge : threshold ≤ input.length := Nat.le_of_not_gt hlt
      exact (heventual input hge).trans (Nat.le_add_left _ _)
  simpa using hbound

/-- The imported and Programme polynomial-bound presentations are equivalent. -/
theorem importedPolynomialBound_iff_programmePolynomialBound
    (cost : BinaryRuntimeCost) :
    ImportedPolynomialBound cost ↔ ProgrammePolynomialBound cost :=
  ⟨importedPolynomialBound_to_programmePolynomialBound,
    programmePolynomialBound_to_importedPolynomialBound⟩

#print axioms polynomial_eval_le_eval_one_mul_pow_natDegree
#print axioms importedPolynomialBound_to_programmePolynomialBound
#print axioms programmePolynomialBound_to_importedPolynomialBound
#print axioms importedPolynomialBound_iff_programmePolynomialBound

end MathSolve.PNP
