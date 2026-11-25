import PNPAbove.WP23BNativeCost

/-!
Universal exact characterization of source-native satisfiable CHSH
responses, with no Cook--Levin assumption. This is a direct original
Cost.Prog theorem and is independent of its SAT presentation.
-/
namespace PNPAbove.WP23B
open MIPRE MIPRE.Cost PNPAbove.WP21 PNPAbove.WP22
set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

/-- Deterministic source-native response matching the four original
support-masked CHSH coordinates whenever winning is possible. -/
def canonicalAlice (x y : BitStr) : BitStr := [x[0]! && y[8]!]
def canonicalBob : BitStr := [false]

theorem canonical_answers_source_win (n : Nat) (hn : n ≠ 0) (x y : BitStr)
    (hx : x.length = 9) (hy : y.length = 9)
    (hx8 : x[8]! = false) (hy0 : y[0]! = false) :
    maskedParityDecider.Accepts n x y (canonicalAlice x y) canonicalBob := by
  apply (native_accepts_iff n x y (canonicalAlice x y) canonicalBob).mpr
  refine ⟨hn, hx, hy, rfl, rfl, ?_⟩
  cases h0 : x[0]! <;> cases h8 : y[8]! <;>
    simp [canonicalAlice, canonicalBob, leafRule, hx8, hy0, h0, h8]

/-- Exact support-only satisfiability of the genuine original
source-executable native CHSH predicate. An existential answer may use any
original bit string but the decider rejects all non-singleton strings. -/
theorem source_accepts_some_iff_mask (n : Nat) (x y : BitStr) :
    (∃ ap bp : BitStr, maskedParityDecider.Accepts n x y ap bp) ↔
      n ≠ 0 ∧ x.length = 9 ∧ y.length = 9 ∧
      x[8]! = false ∧ y[0]! = false := by
  constructor
  · rintro ⟨ap, bp, hacc⟩
    obtain ⟨hn, hx, hy, _, _, hleaf⟩ :=
      (native_accepts_iff n x y ap bp).mp hacc
    have hx8 : x[8]! = false := by
      cases hbit : x[8]! with
      | false => rfl
      | true => simp [leafRule, hbit] at hleaf
    have hy0 : y[0]! = false := by
      cases hbit : y[0]! with
      | false => rfl
      | true => simp [leafRule, hbit] at hleaf
    exact ⟨hn, hx, hy, hx8, hy0⟩
  · rintro ⟨hn, hx, hy, hx8, hy0⟩
    exact ⟨canonicalAlice x y, canonicalBob,
      canonical_answers_source_win n hn x y hx hy hx8 hy0⟩

end PNPAbove.WP23B
