\\ BSD R5-WIT exact mod-2 normalized Kurihara probe.
\\ Uses PARI/GP msfromell/mseval exact rational modular symbols.
\\ For 53a1 and 203b1, E(R) is connected, so protected
\\ Delta_l^(2) mod 2 is the parity sum of 2*x^+ values.

kuriparity(E,N,l,M,xp)=
{
  my(S=0, v);
  for(a=1,l-1,
    if(kronecker(a,l)==-1,
      v=mseval(M,xp,[oo,a/l]);
      if(denominator(2*v)!=1,
        error("2-adic saturation failure at l=",l,", a=",a,", value=",v)
      );
      S += 2*v;
    )
  );
  if(denominator(S)!=1,error("nonintegral normalized sum at l=",l,", S=",S));
  return(lift(Mod(S,2)));
};

run_curve(name, coeffs, N, B)=
{
  my(E=ellinit(coeffs), z=msfromell(E,1), M=z[1], xp=z[2], ap, d, r, hits=List());
  print("CURVE ",name," conductor=",N," bound=",B);
  forprime(l=3,B,
    if(N%l,
      ap=ellap(E,l);
      \\ literal p=2 Kolyvagin-prime congruence: l=1 mod2 and ap=l+1 mod2.
      if(ap%2==0,
        d=min(valuation(l-1,2),valuation(ap-l-1,2));
        if(d>=1,
          r=kuriparity(E,N,l,M,xp);
          print("WITNESS_CHECK curve=",name," l=",l," ap=",ap," v2I=",d," Delta_mod2=",r);
          if(r==1,listput(hits,l));
        )
      )
    )
  );
  print("HITS ",name," ",Vec(hits));
  if(#hits==0,error("no nonzero normalized finite witness found through bound ",B));
  return(Vec(hits));
};

h53=run_curve("53a1",[1,-1,1,0,0],53,250);
h203=run_curve("203b1",[1,1,1,0,-2],203,250);
print("PASS R5-WIT PARI PROBE 53a1=",h53," 203b1=",h203);
quit
