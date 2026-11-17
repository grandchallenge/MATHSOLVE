import PNPAbove.WP08
import PNPAbove.WP09

/-!
PNP-ABOVE WP10 — candidate bridge from the *source-native* WP08 decider
through the sound WP09 fuel interpreter to imported MIPRE.Decider.Accepts.

Primary upstream: vidick/MIPRE-formalization
5926bdff5db621f44682a101007ef2fe3ae8d970 (Lean 4.35.0-rc3).
GCL protected source inputs: WP08 blob 45b9fa687fad92bf1b1d4be2809473e0c4f9957d;
WP09 blob 3b64353814fd70a77810e51f2d04cbcfb4271def.
The reproducible replay stages the original GCL files as temporary Lean modules.
This file must NOT be called source-replayed until that exact import test passes.
-/

namespace PNPAbove.WP10

open MIPRE
open MIPRE.Cost

/-- A successful *WP09* interpreter computation with output true certifies
    the actual imported source-native WP08 Decider.Accepts relation.
    We intentionally evaluate WP08's original program with WP09.runFuel:
    this avoids assuming equality between two independently declared interpreters. -/
theorem accepts_of_fuel
    (n : Nat) (x y a b : BitStr) (fuel t : Nat)
    (h : WP09.runFuel fuel [WP08.sample n x y a b]
        WP08.identityDeciderProg = some (encode true, t)) :
    WP08.identityDecider.Accepts n x y a b := by
  change ∃ u, Eval [WP08.sample n x y a b]
    WP08.identityDeciderProg (encode true) u
  exact ⟨t, WP09.runFuel_sound fuel _ _ _ _ h⟩

/-- Once the *same* source-native program evaluates to the canonical false,
    determinism of upstream MIPRE.Cost.Eval precludes a true acceptance witness.
    This says nothing about timeouts or source-completeness of the interpreter. -/
theorem rejects_of_fuel
    (n : Nat) (x y a b : BitStr) (fuel t : Nat)
    (h : WP09.runFuel fuel [WP08.sample n x y a b]
        WP08.identityDeciderProg = some (encode false, t)) :
    ¬ WP08.identityDecider.Accepts n x y a b := by
  intro hacc
  change ∃ u, Eval [WP08.sample n x y a b]
    WP08.identityDeciderProg (encode true) u at hacc
  obtain ⟨u, htrue⟩ := hacc
  have hfalse : Eval [WP08.sample n x y a b]
      WP08.identityDeciderProg (encode false) t :=
    WP09.runFuel_sound fuel _ _ _ _ h
  have hneq : (encode false : Data) ≠ (encode true : Data) := by
    intro heq
    have hbool : (false : Bool) = true := encode_injective heq
    cases hbool
  exact hneq (Eval.deterministic hfalse htrue).1

/-- Concrete, typed example from WP08's successful 63-cost execution.
    Requires source-native WP09.runFuel computation, not WP08's independent guard. -/
theorem accepts_nine_bit_example :
    WP08.identityDecider.Accepts 2 WP08.zeroNine
      WP08.alternatingNine [] [] := by
  apply accepts_of_fuel (fuel := 96) (t := 63)
  decide

/-- An explicit zero-index rejection against the imported Decider.Accepts:
    the finite negative result is derived through Eval.deterministic. -/
theorem rejects_zero_index :
    ¬ WP08.identityDecider.Accepts 0 WP08.zeroNine
      WP08.zeroNine [] [] := by
  have hc :
      (WP09.runFuel 96
        [WP08.sample 0 WP08.zeroNine WP08.zeroNine [] []]
        WP08.identityDeciderProg).map Prod.fst = some (encode false) := by
    decide
  cases hr : WP09.runFuel 96
      [WP08.sample 0 WP08.zeroNine WP08.zeroNine [] []]
      WP08.identityDeciderProg with
  | none => simp [hr] at hc
  | some rt =>
      rcases rt with ⟨r, t⟩
      have hv : r = encode false := by simpa [hr] using hc
      subst r
      exact rejects_of_fuel 0 WP08.zeroNine WP08.zeroNine [] [] 96 t hr

end PNPAbove.WP10
