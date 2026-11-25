import Init

namespace GCLFiniteOverlap

def edge012 : List (Fin 4) := [0, 1, 2]
def edge013 : List (Fin 4) := [0, 1, 3]
def color (v : Fin 4) : Fin 2 := if v.val < 2 then 0 else 1

theorem edge012_proper :
    ∃ a ∈ edge012, ∃ b ∈ edge012, color a ≠ color b := by decide

theorem edge013_proper :
    ∃ a ∈ edge013, ∃ b ∈ edge013, color a ≠ color b := by decide

theorem edges_distinct : edge012 ≠ edge013 := by decide

theorem edge_memberships_differ :
    (2 : Fin 4) ∈ edge012 ∧ (2 : Fin 4) ∉ edge013 := by decide

theorem exactly_three_distinct :
    edge012.length = 3 ∧ edge013.length = 3 ∧
    edge012.Pairwise (fun a b => a ≠ b) ∧
    edge013.Pairwise (fun a b => a ≠ b) := by decide

theorem distinct_common_vertices :
    (0 : Fin 4) ∈ edge012 ∧ (0 : Fin 4) ∈ edge013 ∧
    (1 : Fin 4) ∈ edge012 ∧ (1 : Fin 4) ∈ edge013 ∧
    (0 : Fin 4) ≠ 1 := by decide

#print axioms edge012_proper
#print axioms edge013_proper
#print axioms edges_distinct
#print axioms edge_memberships_differ
#print axioms exactly_three_distinct
#print axioms distinct_common_vertices

end GCLFiniteOverlap
