"""Exact small-state regression for joint linear constraints and decomposable symbols."""
from itertools import combinations
from marked_graph_replay import initial,space,atom_set
from marked_quotient_replay import reducer
from support_incidence_replay import closure_test,feature_rows,xor

def wedge(u,v,pairs):
    return sum((((u>>i)&1)*((v>>j)&1)^((u>>j)&1)*((v>>i)&1))<<k for k,(i,j) in enumerate(pairs))

def matrix_rank(q,d,pairs):
    rows=[0]*d
    for k,(i,j) in enumerate(pairs):
        if q>>k&1:rows[i]|=1<<j;rows[j]|=1<<i
    piv={}
    for x in rows:
        while x:
            i=x.bit_length()-1
            if i not in piv:piv[i]=x;break
            x^=piv[i]
    return len(piv)

if __name__=='__main__':
    if not __debug__:raise RuntimeError('assertions required')
    n=4;k=16;M=65535;a,b,c,d=[sum(((i>>j)&1)<<i for i in range(k)) for j in range(n)]
    basis=[a,b,c,d,a&b];V=space([M,*basis]);A=atom_set(n,V)-{0};R=feature_rows(n,[a&b]);pairs=list(combinations(range(5),2))
    P=[basis[i]&basis[j] for i,j in pairs];D={wedge(u,v,pairs) for u in range(32) for v in range(32)}
    S=(0x0066ff99,0x01410141,0x00006699,0x00010001,0x00006699^0x00010001)
    assert all(s for s in S) and set(S[:2])-A==set(S[:2])
    W=[(1<<(2*k))-1]+[sum(((i>>j)&1)<<i for i in range(2*k)) for j in range(n+1)]+[(a&b)|((a&b)<<k)]
    tests=[]
    for s in S:
        C=closure_test(R,s); red=reducer(tuple(w&C for w in W))
        tests.append((s,C,red))
    def pass_one(g,t):
        s,C,red=t
        return C==s or red(((g|(g<<k))&C)^(C^s))==0
    gate_values={u&v for u in V for v in V}; checks=0
    for g in gate_values:
        T=feature_rows(n,[a&b,g])
        for t in tests:
            assert pass_one(g,t)==(closure_test(T,t[0])==t[0]);checks+=1
    rho=reducer(V); count=0;solutions=[]
    for q in range(1<<len(pairs)):
        assert (matrix_rank(q,5,pairs)<=2)==(q in D);count+=1
        g=xor(p for j,p in enumerate(P) if q>>j&1)
        if all(pass_one(g,t) for t in tests[:2]) and q in D:solutions.append(rho(g))
    assert set(solutions)=={rho(g) for g in gate_values if all(pass_one(g,t) for t in tests[:2])}
    assert rho(d&(a^b)) in solutions
    print('PASS: gate values',len(gate_values),'joint constraint comparisons',checks,'exterior symbols',count,'decomposable symbols',len(D),'joint legal gate classes',len(set(solutions)))
