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

H=List(); h=0;
h=first_hit("37a1",[0,0,1,-1,0],37,500); if(h,listput(H,["37a1",h]));
h=first_hit("43a1",[0,1,1,0,0],43,500); if(h,listput(H,["43a1",h]));
h=first_hit("53a1",[1,-1,1,0,0],53,500); if(h,listput(H,["53a1",h]));
h=first_hit("57a1",[0,-1,1,-2,2],57,500); if(h,listput(H,["57a1",h]));
h=first_hit("61a1",[1,0,0,-2,1],61,500); if(h,listput(H,["61a1",h]));
h=first_hit("77a1",[0,0,1,2,0],77,500); if(h,listput(H,["77a1",h]));
h=first_hit("79a1",[1,1,1,-2,0],79,500); if(h,listput(H,["79a1",h]));
h=first_hit("83a1",[1,1,1,1,0],83,500); if(h,listput(H,["83a1",h]));
h=first_hit("89a1",[1,1,1,-1,0],89,500); if(h,listput(H,["89a1",h]));
h=first_hit("91a1",[0,0,1,1,0],91,500); if(h,listput(H,["91a1",h]));
h=first_hit("101a1",[0,1,1,-1,-1],101,500); if(h,listput(H,["101a1",h]));
h=first_hit("123b1",[0,-1,1,1,-1],123,500); if(h,listput(H,["123b1",h]));
h=first_hit("129a1",[0,-1,1,-19,39],129,500); if(h,listput(H,["129a1",h]));
h=first_hit("131a1",[0,-1,1,1,0],131,500); if(h,listput(H,["131a1",h]));
h=first_hit("141a1",[0,1,1,-12,2],141,500); if(h,listput(H,["141a1",h]));
h=first_hit("141d1",[0,-1,1,-1,0],141,500); if(h,listput(H,["141d1",h]));
h=first_hit("143a1",[0,-1,1,-1,-2],143,500); if(h,listput(H,["143a1",h]));
h=first_hit("155c1",[0,-1,1,-1,1],155,500); if(h,listput(H,["155c1",h]));
h=first_hit("163a1",[0,0,1,-2,1],163,500); if(h,listput(H,["163a1",h]));
h=first_hit("185a1",[0,1,1,-156,700],185,500); if(h,listput(H,["185a1",h]));
h=first_hit("185b1",[0,-1,1,-5,6],185,500); if(h,listput(H,["185b1",h]));
h=first_hit("197a1",[0,0,1,-5,4],197,500); if(h,listput(H,["197a1",h]));
h=first_hit("201a1",[0,-1,1,2,0],201,500); if(h,listput(H,["201a1",h]));
h=first_hit("201b1",[1,0,0,-1,2],201,500); if(h,listput(H,["201b1",h]));
h=first_hit("201c1",[1,1,0,-794,8289],201,500); if(h,listput(H,["201c1",h]));
h=first_hit("203b1",[1,1,1,0,-2],203,500); if(h,listput(H,["203b1",h]));
print("DISCOVERY_HITS ",Vec(H));
print("R5_WIT_COHORT_DISCOVERY_COMPLETE");
quit
