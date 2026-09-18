\\ BSD R5-WIT non-promotional ecdata cohort discovery.
\\ Models/ranks/torsion are from protected WP18A's pinned JohnCremona/ecdata
\\ commit 25cec5ecfec8b9f016eb1631ac633194c2bed39f.
\\ Candidates below are rank 1, torsion order 1, odd squarefree conductor.
\\ We further require a_2=-1 (q2=4) and negative discriminant so PARI x+
\\ uses the same connected/full real period normalization.

kuriparity_prime(E,l,M,xp)=
{
  my(S=0,v);
  for(a=1,l-1,
    if(kronecker(a,l)==-1,
      v=mseval(M,xp,[oo,a/l]);
      if(denominator(2*v)!=1,error("half-integrality failure l=",l," a=",a," v=",v));
      S += 2*v
    )
  );
  return(lift(Mod(S,2)));
};

first_hit(name, coeffs, N, B)=
{
  my(E=ellinit(coeffs),ap2=ellap(E,2),z,M,xp,ap,d,r);
  if(ap2!=-1, print("SKIP ",name," a2=",ap2); return(0));
  if(E.disc>=0, print("SKIP ",name," disc_nonnegative=",E.disc); return(0));
  z=msfromell(E,1); M=z[1]; xp=z[2];
  forprime(l=3,B,
    if(N%l,
      ap=ellap(E,l);
      if(ap%2==0,
        d=min(valuation(l-1,2),valuation(ap-l-1,2));
        if(d>=1,
          r=kuriparity_prime(E,l,M,xp);
          if(r==1,
            print("DISCOVERY_HIT curve=",name," N=",N," model=",coeffs," disc=",E.disc,
                  " l=",l," ap=",ap," v2I=",d);
            return(l)
          )
        )
      )
    )
  );
  print("NO_HIT curve=",name," through=",B);
  return(0)
};

C=[
["37a1",[0,0,1,-1,0],37],
["43a1",[0,1,1,0,0],43],
["53a1",[1,-1,1,0,0],53],
["57a1",[0,-1,1,-2,2],57],
["61a1",[1,0,0,-2,1],61],
["77a1",[0,0,1,2,0],77],
["79a1",[1,1,1,-2,0],79],
["83a1",[1,1,1,1,0],83],
["89a1",[1,1,1,-1,0],89],
["91a1",[0,0,1,1,0],91],
["101a1",[0,1,1,-1,-1],101],
["123b1",[0,-1,1,1,-1],123],
["129a1",[0,-1,1,-19,39],129],
["131a1",[0,-1,1,1,0],131],
["141a1",[0,1,1,-12,2],141],
["141d1",[0,-1,1,-1,0],141],
["143a1",[0,-1,1,-1,-2],143],
["155c1",[0,-1,1,-1,1],155],
["163a1",[0,0,1,-2,1],163],
["185a1",[0,1,1,-156,700],185],
["185b1",[0,-1,1,-5,6],185],
["197a1",[0,0,1,-5,4],197],
["201a1",[0,-1,1,2,0],201],
["201b1",[1,0,0,-1,2],201],
["201c1",[1,1,0,-794,8289],201],
["203b1",[1,1,1,0,-2],203]
];

my(H=List(),h);
for(i=1,#C,
  h=first_hit(C[i][1],C[i][2],C[i][3],500);
  if(h,listput(H,[C[i][1],h]))
);
print("DISCOVERY_HITS ",Vec(H));
print("R5_WIT_COHORT_DISCOVERY_COMPLETE");
quit
