import PNPAbove.WP23BSuccinctBridge
import PNPAbove.WP23BMask

/-!
The original source-native Bell verifier's succinct Cook--Levin formula is
exactly characterized at a canonical, explicit sufficient time bound.
It has a *trivial* SAT predicate (two mask bits plus original input guards),
and therefore does not provide an arbitrary SAT-to-game hardness reduction.
-/
namespace PNPAbove.WP23B
open MIPRE MIPRE.Cost PNPAbove.WP21 PNPAbove.WP22
variable (K : SAT.SuccinctCookLevin)
open scoped Classical
set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

/-- A source-native Cook--Levin time bound fixed *before* any strategy
quantification, computed from the canonical answer and the question pair. -/
def canonicalTime (n : Nat) (x y : BitStr) : Nat :=
  nativeTimeParameter n x y (canonicalAlice x y) canonicalBob

/-- All validity hypotheses are discharged by the explicit source-based
time parameter. The 3SAT circuit is an actual pinned MIPRE circuit program. -/
theorem canonical_parameters_valid (n : Nat) (x y : BitStr) :
    SAT.Valid maskedParityDecider.prog n (canonicalTime n x y)
      (max x.length y.length) (esize maskedParityDecider.prog) x y := by
  unfold canonicalTime nativeTimeParameter
  refine ⟨?_, ?_, le_rfl, ?_, ?_⟩
  all_goals omega

/-- The complete original succinct Cook--Levin SAT instance is SATISFIABLE
if and only if n is positive, both native questions are exactly nine bits,
and the support mask holds. The condition is a constant-size evaluation
once the source lengths and two mask bits are inspected; this is NOT a
SAT-hard verifier. -/
theorem native_cnf_sat_iff_mask_with (n : Nat) (x y : BitStr) :
    (∃ A B : Fin (2 * canonicalTime n x y) → Bool,
      NativeSatWith K n (canonicalTime n x y) (max x.length y.length)
        (esize maskedParityDecider.prog) x y A B) ↔
      n ≠ 0 ∧ x.length = 9 ∧ y.length = 9 ∧
        x[8]! = false ∧ y[0]! = false := by
  have hV := canonical_parameters_valid n x y
  constructor
  · rintro ⟨A, B, hs⟩
    obtain ⟨ap, bp, _, _, hwithin⟩ :=
      (nativeSatWith_exists_iff_source_timed_acceptance K n (canonicalTime n x y)
        (max x.length y.length) (esize maskedParityDecider.prog) x y hV).mp
        ⟨A, B, hs⟩
    exact (source_accepts_some_iff_mask n x y).mp
      ⟨ap, bp, hwithin.accepts⟩
  · rintro ⟨hn, hx, hy, hx8, hy0⟩
    have hacc :=
      canonical_answers_source_win n hn x y hx hy hx8 hy0
    exact native_acceptance_produces_sat K n x y
      (canonicalAlice x y) canonicalBob hacc

end PNPAbove.WP23B
