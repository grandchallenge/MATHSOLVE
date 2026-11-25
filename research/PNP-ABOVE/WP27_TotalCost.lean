import PNPAbove.WP27RawNormalizer
import MIPRE.Foundations.Halting.PolyBounded
import MIPRE.Foundations.Cost.Growth

/-! ORIGINAL cost theorem for arbitrary raw Data (including malformed). -/
namespace PNPAbove.WP27
open MIPRE MIPRE.Cost Polynomial

/-- For each original formula, the size of a formula and ANY indexed raw
Data input is bounded in the original PolyCost model. -/
theorem formula_raw_input_polyCost (f : MIPRE.SAT.Fml) :
    PolyCost (fun n d => esize (f, Data.cons (encode n) d)) := by
  let C : Nat → Nat := fun n => esize f + 4 * Nat.size n + 5
  have hC : PolyBounded C := by
    exact ((PolyBounded.size.const_mul 4).add_const (esize f + 5)).mono
      (fun n => by simp only [C]; omega)
  refine ⟨C, 1, hC, fun n d => ?_⟩
  have hn := esize_nat_le n
  have h1 : esize (f, Data.cons (encode n) d) =
      esize f + esize n + d.size + 2 := by
    calc
      esize (f, Data.cons (encode n) d) =
          esize f + (Data.cons (encode n) d).size + 1 := rfl
      _ = esize f + esize n + d.size + 2 := by
        dsimp [Data.size, esize]
        omega
  change esize (f, Data.cons (encode n) d) ≤ C n * (d.size + 1) ^ 1
  rw [h1]
  simp only [pow_one]
  change esize f + esize n + d.size + 2 ≤
    (esize f + 4 * Nat.size n + 5) * (d.size + 1)
  have h2 : 1 ≤ esize f + 4 * Nat.size n + 5 := by omega
  nlinarith

/-- The ORIGINAL polynomial formula evaluator, once the arbitrary raw
verifier data is normalized through the source parser, has a polynomial
runtime over *all* raw source data, not just typed verifier tuples.
This is a real original Prog.HasPolyCost certificate. -/
theorem robustSourceGenerator_hasPolyCost (f : MIPRE.SAT.Fml) :
    (robustSourceGenerator f).HasPolyCost := by
  let Q : Polynomial Nat := rawCore.timeBound + X + C 2
  have hP : PolyCost (fun n d => Q.eval (esize (f, Data.cons (encode n) d))) :=
    PolyCost.poly Q (formula_raw_input_polyCost f)
  apply Prog.hasPolyCost_of_polyCost hP
  intro n d
  obtain ⟨t, ht, hrun⟩ :=
    rawCore.computes (f, Data.cons (encode n) d)
  have htotal : (robustSourceGenerator f).Runs
      (Data.cons (encode n) d)
      (encode (rawCore (f, Data.cons (encode n) d)))
      (t + (encode f).size + (Data.cons (encode n) d).size + 3) := by
    rw [robustSourceGenerator_correct]
    exact Cost.hardcode_time rawCore.closed hrun
  refine ⟨_, _, ?_, htotal⟩
  dsimp [Q]
  simp only [Polynomial.eval_add, Polynomial.eval_X, Polynomial.eval_C]
  have heq : esize (f, Data.cons (encode n) d) =
      esize f + (Data.cons (encode n) d).size + 1 := rfl
  rw [heq] at ht
  change t + esize f + (Data.cons (encode n) d).size + 3 ≤
    rawCore.timeBound.eval (esize f + (Data.cons (encode n) d).size + 1) +
      (esize f + (Data.cons (encode n) d).size + 1) + 2
  omega

end PNPAbove.WP27
