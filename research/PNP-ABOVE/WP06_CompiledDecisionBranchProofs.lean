import MIPRE.Background.Introspection.DecisionCompiler
namespace PNPAbove.WP06
open MIPRE MIPRE.Cost MIPRE.Introspection.DecisionCompiler

theorem zero_compiler_is_actual_zeroProg (c : Nat)
    (S D : Prog) :
    compute c selfClockedUniversal ((S,D),0) = zeroProg := by
  rw [compute_apply]
  rfl

theorem positive_compiler_has_source_wrapper (c : Nat)
    (S D : Prog) :
    compute c selfClockedUniversal ((S,D),1) =
      zeroWrap (positiveCompiler c selfClockedUniversal
        (MIPRE.Introspection.SourceDescriptionCompiler.clamp ((S,D),1))) := by
  rw [compute_apply]
  rfl

theorem all_empty_answers_accepted_at_zero_lambda (c : Nat)
    (S D : Prog) (n : Nat) :
    (decider c selfClockedUniversal S D 0).Accepts n [] [] [] [] := by
  apply (accepts_zero c selfClockedUniversal S D 0 n (Or.inl rfl) [] [] [] []).2
  simp

theorem nonempty_alice_query_rejected_at_zero_lambda (c : Nat)
    (S D : Prog) (n : Nat) :
    ¬ (decider c selfClockedUniversal S D 0).Accepts n [true] [] [] [] := by
  intro h
  have hx := ((accepts_zero c selfClockedUniversal S D 0 n (Or.inl rfl)
    [true] [] [] []).1 h).1
  cases hx

theorem empty_payload_executable_at_zero_lambda (c : Nat)
    (S D : Prog) (n : Nat) :
    ∃ t, (decider c selfClockedUniversal S D 0).prog.Runs
      (.cons (encode n) (encode (([] : BitStr), ([] : BitStr),
        ([] : BitStr), ([] : BitStr))))
      (encode (zeroTest (encode (([] : BitStr), ([] : BitStr),
        ([] : BitStr), ([] : BitStr))))) t := by
  exact zero_runs c selfClockedUniversal S D 0 n (Or.inl rfl) _

end PNPAbove.WP06
