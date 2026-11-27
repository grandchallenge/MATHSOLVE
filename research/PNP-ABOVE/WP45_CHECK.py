#!/usr/bin/env python3
"""Independent finite controls for sentinel enumeration and accepted selection."""
from itertools import product
from functools import lru_cache

@lru_cache(None)
def trees(size):
    if size == 1:
        return (None,)
    return tuple((a,b) for i in range(1,size-1)
                 for a in trees(i) for b in trees(size-1-i))

def post(d):
    return [0] if d is None else post(d[0])+post(d[1])+[1]

def parse(bits):
    stack=[]
    for b in bits:
        if not b:
            stack.append(None)
        elif len(stack)>=2:
            right=stack.pop(); left=stack.pop()
            stack.append((left,right))
    return stack[-1] if stack else None

def index(d):
    return sum(b<<i for i,b in enumerate(post(d)+[1]))

def bits(n):
    return [(n>>i)&1 for i in range(n.bit_length())]

def select(xs):
    result=()
    for accepted,w in xs:
        if accepted:
            result=w
    return result

def check():
    ct=0
    for size in range(1,14):
        seen=set()
        for tree in trees(size):
            b=1<<size; j=index(tree)
            assert 0<j<=2*b
            assert parse(bits(j))==tree
            assert len(post(tree))==size
            assert j not in seen
            seen.add(j); ct+=1
    # Enumeration is complete at the exact 2^size boundary, including
    # noncanonical duplicates from raw input. Small sizes are exhaustive.
    for b in (0,1,2,3,4,8,16,32,64,128,256):
        raw=[parse(bits(j)) for j in range(1,2*b+1)]
        assert len(raw)==2*b
        for size in range(1,b.bit_length()):
            if (1<<size)<=b:
                assert all(d in raw for d in trees(size))
    flags=0
    for length in range(8):
        for mask in product((False,True),repeat=length):
            xs=list(zip(mask,[(i,) for i in range(length)]))
            accepted=[w for ok,w in xs if ok]
            assert select(xs)==(accepted[-1] if accepted else ())
            flags+=1
    print(f"WP45 finite controls: {ct} canonical trees; {flags} acceptance masks; 11 budget boundaries")
if __name__=="__main__":
    check()
