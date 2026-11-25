import PNPAbove.WP22BitRead

namespace PNPAbove.WP22
open MIPRE MIPRE.Cost PNPAbove.WP21
set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

/-- The actual source decision tree computes the Boolean six-bit CHSH rule
in any ambient environment. There are 64 Boolean cases; all are kernel-checked. -/
theorem truthTree_six (b a y8 y0 x8 x0 : Bool) (env : Env) :
    WP12.evalValue (truthTree [0,1,2,3,4,5] [] 0)
      ([encode b, encode a, encode y8, encode y0, encode x8, encode x0] ++ env) =
      encode (leafRule [b,a,y8,y0,x8,x0]) := by
  cases b <;> cases a <;> cases y8 <;> cases y0 <;>
    cases x8 <;> cases x0 <;>
    rfl

theorem leafRule_eq_masked (b a y8 y0 x8 x0 : Bool) :
    leafRule [b,a,y8,y0,x8,x0] =
      ((!x8 && !y0) && decide (a.xor b = (x0 && y8))) := rfl

end PNPAbove.WP22
