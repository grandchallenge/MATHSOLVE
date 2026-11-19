import PNPAbove.WP22Truth

namespace PNPAbove.WP22
open MIPRE MIPRE.Cost PNPAbove.WP21
set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

/-- The six source binding instructions read the four canonical
question/answer input fields at their actual de Bruijn positions. -/
theorem readAndDecide_value (env : Env) (x y a b : BitStr)
    (hx : env.get 16 = encode x) (hy : env.get 14 = encode y)
    (ha : env.get 12 = encode a) (hb : env.get 13 = encode b) :
    WP12.evalValue readAndDecide env =
      encode (leafRule [b[0]!, a[0]!, y[8]!, y[0]!, x[8]!, x[0]!]) := by
  simp only [readAndDecide, WP12.evalValue]
  rw [readBit_value 16 0 env x hx]
  rw [readBit_value 17 8 (encode (x[0]!) :: env) x (by simpa [Env.get] using hx)]
  rw [readBit_value 16 0
        (encode (x[8]!) :: encode (x[0]!) :: env) y
        (by simpa [Env.get] using hy)]
  rw [readBit_value 17 8
        (encode (y[0]!) :: encode (x[8]!) :: encode (x[0]!) :: env) y
        (by simpa [Env.get] using hy)]
  rw [readBit_value 16 0
        (encode (y[8]!) :: encode (y[0]!) :: encode (x[8]!) ::
          encode (x[0]!) :: env) a
        (by simpa [Env.get] using ha)]
  rw [readBit_value 18 0
        (encode (a[0]!) :: encode (y[8]!) :: encode (y[0]!) ::
          encode (x[8]!) :: encode (x[0]!) :: env) b
        (by simpa [Env.get] using hb)]
  exact truthTree_six (b[0]!) (a[0]!) (y[8]!) (y[0]!) (x[8]!) (x[0]!) env

end PNPAbove.WP22
