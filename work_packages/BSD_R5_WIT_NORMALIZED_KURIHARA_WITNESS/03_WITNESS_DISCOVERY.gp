\\ BSD R5-WIT discovery scan.
\\ Exact rational plus modular symbols via the admitted PARI/GP 2.15.4 interface.
\\ Discovery only: a nonzero candidate must be reduced to a deterministic certificate.

ratmod2(q)={
  my(n=numerator(q), d=denominator(q));
  if(d % 2 == 0, error("even denominator after protected scaling: ", q));
  lift(Mod(n,2) / Mod(d,2));
};

legbit(a,l)=if(kronecker(a,l)==-1,1,0);

is_kolyvagin_prime(E,N,l)={
  if(l==2 || N%l==0, return(0));
  if((l-1)%2 != 0, return(0));
  my(ap=ellap(E,l));
  ((ap-l-1)%2)==0;
};

delta_prime_mod2(M,xp,l)={
  my(S=0, q, b);
  for(a=1,l-1,
    if(gcd(a,l)==1,
      b=legbit(a,l);
      if(b,
        q=mseval(M,xp,[oo,a/l]);
        S=(S + ratmod2(2*q)) % 2;
      );
    );
  );
  S;
};

emit_terms(M,xp,l)={
  print("TERMS ell=",l);
  for(a=1,l-1,
    if(gcd(a,l)==1 && legbit(a,l),
      my(q=mseval(M,xp,[oo,a/l]));
      if(ratmod2(2*q),
        print("  a=",a," symbol=",q," scaled=",2*q," parity=1");
      );
    );
  );
};

scan(label,ainvs,N,bound)={
  my(E=ellinit(ainvs), v=msfromell(E,1), M=v[1], xp=v[2], found=0);
  print("CURVE ",label," conductor=",N," discr=",ellglobalred(E)[1]);
  print("PARI plus symbol initialized");
  forprime(l=3,bound,
    if(is_kolyvagin_prime(E,N,l),
      my(ap=ellap(E,l), d=delta_prime_mod2(M,xp,l));
      print("KOLYVAGIN ell=",l," ap=",ap," Delta_mod2=",d);
      if(d && !found,
        found=l;
        print("FIRST_NONZERO label=",label," n=",l," Delta_mod2=1");
        emit_terms(M,xp,l);
      );
    );
  );
  if(!found, print("NO_SINGLE_PRIME_WITNESS label=",label," bound=",bound));
  found;
};

f53=scan("53a1",[1,-1,1,0,0],53,251);
f203=scan("203b1",[1,1,1,0,-2],203,251);
print("SUMMARY first53=",f53," first203=",f203);
quit;
