\\ BSD R5-WIT exact mod-2 normalized Kurihara probe.
\\ Exact rational PARI/GP modular symbols; no floating arithmetic.

kuriparity_n(E,n,ells,M,xp)=
{
  my(S=0,v,mult);
  for(a=1,n-1,
    if(gcd(a,n)==1,
      mult=1;
      for(i=1,#ells, if(kronecker(a,ells[i])!= -1, mult=0; break));
      if(mult,
        v=mseval(M,xp,[oo,a/n]);
        if(denominator(2*v)!=1,
          error("2-adic saturation failure n=",n,", a=",a,", value=",v)
        );
        S += 2*v;
      )
    )
  );
  if(denominator(S)!=1,error("nonintegral normalized sum n=",n,", S=",S));
  return(lift(Mod(S,2)));
};

kprimes(E,N,B)=
{
  my(L=List(),ap,d);
  forprime(l=3,B,
    if(N%l,
      ap=ellap(E,l);
      if(ap%2==0,
        d=min(valuation(l-1,2),valuation(ap-l-1,2));
        if(d>=1,listput(L,l))
      )
    )
  );
  return(Vec(L));
};

run_curve(name, coeffs, N, prime_bound, product_bound)=
{
  my(E=ellinit(coeffs), z=msfromell(E,1), M=z[1], xp=z[2]);
  my(P=kprimes(E,N,prime_bound), hits=List(), r, n);
  print("CURVE ",name," conductor=",N," rootno=",ellrootno(E));
  print("KPRIMES ",name," ",P);

  \\ Rank-one controls have root number -1; inspect odd derivative orders.
  for(i=1,#P,
    r=kuriparity_n(E,P[i],[P[i]],M,xp);
    print("CHECK1 curve=",name," n=",P[i]," Delta_mod2=",r);
    if(r==1,listput(hits,P[i]))
  );

  for(i=1,#P,
    for(j=i+1,#P,
      for(k=j+1,#P,
        n=P[i]*P[j]*P[k];
        if(n<=product_bound,
          r=kuriparity_n(E,n,[P[i],P[j],P[k]],M,xp);
          print("CHECK3 curve=",name," n=",n," factors=",[P[i],P[j],P[k]]," Delta_mod2=",r);
          if(r==1,listput(hits,n))
        )
      )
    )
  );

  print("HITS ",name," ",Vec(hits));
  return(Vec(hits));
};

h53=run_curve("53a1",[1,-1,1,0,0],53,100,25000);
h203=run_curve("203b1",[1,1,1,0,-2],203,100,25000);
print("R5_WIT_PROBE_COMPLETE 53a1=",h53," 203b1=",h203);
quit
