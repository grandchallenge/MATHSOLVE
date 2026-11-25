import PNPAbove.WP21Bounded
import PNPAbove.WP21Checks

namespace PNPAbove.WP22
open MIPRE MIPRE.Cost PNPAbove.WP21
set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

/-- Read an arbitrary source-encoded bit-list position, with false fallback
at and beyond the end. The proof is universally quantified over the entire
original machine environment, not restricted to the finite CHSH examples. -/
theorem readBit_value (idx k : Nat) (env : Env) (xs : BitStr)
    (he : env.get idx = encode xs) :
    WP12.evalValue (readBit idx k) env = encode (xs[k]!) := by
  induction k generalizing idx env xs with
  | zero =>
      cases xs with
      | nil =>
          change (match env.get idx with
            | .nil => .nil | .cons h _ => h) = encode false
          rw [he]
          rfl
      | cons b bs =>
          change (match env.get idx with
            | .nil => .nil | .cons h _ => h) = encode b
          rw [he]
          rfl
  | succ k ih =>
      cases xs with
      | nil =>
          change (match env.get idx with
            | .nil => .nil | .cons h t =>
              WP12.evalValue (readBit 1 k) (h :: t :: env)) = encode false
          rw [he]
          rfl
      | cons b bs =>
          change (match env.get idx with
            | .nil => .nil | .cons h t =>
              WP12.evalValue (readBit 1 k) (h :: t :: env)) = encode (bs[k]!)
          rw [he]
          exact ih 1 (encode b :: encode bs :: env) bs (by simp [Env.get])

end PNPAbove.WP22
