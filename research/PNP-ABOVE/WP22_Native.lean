import PNPAbove.WP22Parser

namespace PNPAbove.WP22
open MIPRE MIPRE.Cost PNPAbove.WP21
set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

/-- A full if-and-only-if characterization of the actual original source
Decider.Accepts relation. This is not a fuel evaluator or a sampled table. -/
theorem native_accepts_iff (n : Nat) (x y a b : BitStr) :
    maskedParityDecider.Accepts n x y a b ↔
      n ≠ 0 ∧ x.length = 9 ∧ y.length = 9 ∧
      a.length = 1 ∧ b.length = 1 ∧
      leafRule [b[0]!,a[0]!,y[8]!,y[0]!,x[8]!,x[0]!] = true := by
  rw [accepts_iff_source_value, typed_value_spec]
  have henc (q : Bool) : (encode q : Data) = encode true ↔ q = true :=
    ⟨fun he => encode_injective he, fun he => congrArg encode he⟩
  have regroup :
      (n ≠ 0 ∧ x.length = 9 ∧ y.length = 9 ∧
        a.length = 1 ∧ b.length = 1 ∧
        leafRule [b[0]!,a[0]!,y[8]!,y[0]!,x[8]!,x[0]!] = true) ↔
      ((n ≠ 0 ∧ x.length = 9 ∧ y.length = 9 ∧
        a.length = 1 ∧ b.length = 1) ∧
        leafRule [b[0]!,a[0]!,y[8]!,y[0]!,x[8]!,x[0]!] = true) := by
    tauto
  rw [regroup]
  by_cases h : n ≠ 0 ∧ x.length = 9 ∧ y.length = 9 ∧
      a.length = 1 ∧ b.length = 1
  · simp only [if_pos h]
    exact (henc _).trans (by simp [h])
  · simp [h, SizedEncoding.encode, Data.ofBool]

/-- In a singleton bit list, the head is its unique answer. -/
theorem singleton_of_length_one (xs : BitStr) (h : xs.length = 1) :
    xs = [xs[0]!] := by
  cases xs with
  | nil => simp at h
  | cons a as =>
      cases as with
      | nil => rfl
      | cons b bs => simp at h

/-- A diagonal pair cannot win with distinct canonical Boolean answers. -/
theorem diag_leaf_false (a b q0 q8 : Bool) (hne : a ≠ b) :
    leafRule [b,a,q8,q0,q8,q0] = false := by
  cases a <;> cases b <;> cases q0 <;> cases q8 <;>
    simp_all [leafRule]

/-- The original native executable verifier is synchronous for all indices,
all nine-bit diagonal questions and every permitted answer format. -/
theorem native_synchronous (n : Nat) :
    cyclicVerifier.IsSynchronousAt n := by
  intro x a b hne hacc
  have h := (native_accepts_iff n x x a b).mp hacc
  rcases h with ⟨hn,hx,hy,ha,hb,haccept⟩
  have heqA := singleton_of_length_one a ha
  have heqB := singleton_of_length_one b hb
  have hhead : a[0]! ≠ b[0]! := by
    intro he
    apply hne
    rw [heqA, heqB, he]
  have hfalse := diag_leaf_false (a[0]!) (b[0]!) (x[0]!) (x[8]!) hhead
  rw [hfalse] at haccept
  cases haccept

end PNPAbove.WP22
