import MIPRE.Foundations.Cost.Iterates
import MIPRE.Foundations.OracularDecider
import MIPRE.Foundations.Cost.Binary
import MIPRE.Foundations.Halting.Descriptions

namespace PNPAbove.WP45
open MIPRE MIPRE.Cost MIPRE.Cost.PolyTimeFun Polynomial

theorem tail_iter_bound (n : Nat) (u : Unary) :
    esize ((List.tail : Unary → Unary)^[n] u) ≤ esize u := by
  induction n generalizing u with
  | zero => simp
  | succ n ih =>
    rw [Function.iterate_succ_apply]
    exact (ih u.tail).trans (esize_tail_le u)

theorem tail_iter_length (n : Nat) (u : Unary) :
    ((List.tail : Unary → Unary)^[n] u).length = u.length - n := by
  induction n generalizing u with
  | zero => simp
  | succ n ih =>
    rw [Function.iterate_succ_apply,ih,List.length_tail]
    omega

noncomputable def doubleU : PolyTimeFun Unary Unary :=
  append.comp ((PolyTimeFun.id Unary).pair (PolyTimeFun.id Unary))

noncomputable def countdownP : PolyTimeFun Unary (List Unary) :=
  (recordIteratesProg (tail : PolyTimeFun Unary Unary) X (by
    intro n u
    simpa using tail_iter_bound n u)).comp (doubleU.pair doubleU)

theorem countdown_length_mem (u : Unary) (n : Nat)
    (hn : 0 < n) (hb : n ≤ 2*u.length) :
    ∃ v ∈ countdownP u, v.length = n := by
  change ∃ v ∈ recordIterates List.tail (u++u) (u++u), v.length = n
  have hl : (u++u).length = 2*u.length := by simp; omega
  let i : Fin (u++u).length := ⟨2*u.length-n,by omega⟩
  refine ⟨(List.tail : Unary → Unary)^[i.val] (u++u),?_,?_⟩
  · exact List.mem_ofFn.mpr ⟨i,rfl⟩
  · rw [tail_iter_length,hl]
    change 2*u.length-(2*u.length-n) = n
    omega

theorem sentinel_bits (s : BitStr) :
    (bitsVal (s ++ [true])).bits = s ++ [true] := by
  induction s with
  | nil => simp [bitsVal]
  | cons b s ih =>
    have hn : bitsVal (s ++ [true]) ≠ 0 := by
      intro hz
      rw [hz, Nat.zero_bits] at ih
      simp at ih
    change (Nat.bit b (bitsVal (s ++ [true]))).bits = b :: (s ++ [true])
    rw [Nat.bits_append_bit _ b (by intro hz; exact False.elim (hn hz))]
    exact congrArg (List.cons b) ih

def treeIndex (d : Data) : Nat := bitsVal (d.toBitsPost ++ [true])

theorem treeIndex_size (d : Data) :
    Nat.size (treeIndex d) = d.size+1 := by
  rw [← Nat.size_eq_bits_len,treeIndex,sentinel_bits,List.length_append,
    Data.length_toBitsPost]
  simp

theorem treeIndex_decode (d : Data) :
    Data.parse (treeIndex d).bits = d := by
  rw [treeIndex,sentinel_bits]
  unfold Data.parse
  rw [Data.stackRun_toBitsPost d [true] []]
  rfl

theorem treeIndex_positive (d : Data) : 0 < treeIndex d := by
  apply Nat.size_pos.mp
  rw [treeIndex_size]
  omega

theorem treeIndex_bound (d : Data) (B : Nat) (h : 2^d.size ≤ B) :
    treeIndex d ≤ 2*B := by
  have hlt := Nat.lt_size_self (treeIndex d)
  rw [treeIndex_size,pow_succ] at hlt
  omega

noncomputable def decodeUnaryP : PolyTimeFun Unary Data :=
  MIPRE.OracleDecider.parseF.comp (natBits.comp unaryToBin)

theorem decodeUnaryP_correct (u : Unary) :
    decodeUnaryP u = Data.parse u.length.bits := rfl

noncomputable def codeListP : PolyTimeFun Unary (List Data) :=
  (PolyTimeFun.map decodeUnaryP).comp countdownP

theorem codeList_contains (u : Unary) (c : Prog)
    (h : 2^(esize c) ≤ u.length) :
    encode c ∈ codeListP u := by
  obtain ⟨v,hv,hn⟩ := countdown_length_mem u (treeIndex (encode c))
    (treeIndex_positive _) (treeIndex_bound _ _ h)
  change encode c ∈ (countdownP u).map decodeUnaryP
  refine List.mem_map.mpr ⟨v,hv,?_⟩
  rw [decodeUnaryP_correct,hn,treeIndex_decode]

end PNPAbove.WP45
