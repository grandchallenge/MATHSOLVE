\\ BSD R5-WIT discovery scan.
\\ Exact rational plus modular symbols via the admitted PARI/GP 2.15.4 interface.
\\ Discovery only: any nonzero candidate is replayed by a minimal certificate.

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

delta_n_mod2(M,xp,n,ells)={
  my(S=0, q, b);
  for(a=1,n-1,
    if(gcd(a,n)==1,
      b=1;
      for(i=1,#ells, b *= legbit(a % ells[i],ells[i]));
      if(b,
        q=mseval(M,xp,[oo,a/n]);
        S=(S + ratmod2(2*q)) % 2;
      );
    );
  );
  S;
};

emit_terms(M,xp,n,ells)={
  print("TERMS n=",n," primes=",ells);
  for(a=1,n-1,
    if(gcd(a,n)==1,
      my(b=1);
      for(i=1,#ells, b *= legbit(a % ells[i],ells[i]));
      if(b,
        my(q=mseval(M,xp,[oo,a/n]));
        if(ratmod2(2*q),
          print("  a=",a," symbol=",q," scaled=",2*q," parity=1");
        );
      );
    );
  );
};

scan_single(label,E,N,xp,M,plist)={
  my(found=0);
  for(i=1,#plist,
    my(l=plist[i], ap=ellap(E,l), d=delta_n_mod2(M,xp,l,[l]));
    print("SINGLE label=",label," n=",l," ap=",ap," Delta_mod2=",d);
    if(d && !found, found=l);
  );
  found;
};

scan_pairs(label,E,N,xp,M,plist)={
  my(found=0, best=0);
  for(i=1,#plist-1,
    for(j=i+1,#plist,
      my(n=plist[i]*plist[j]);
      if(!best || n<best,
        my(d=delta_n_mod2(M,xp,n,[plist[i],plist[j]]));
        print("PAIR label=",label," n=",n," primes=",[plist[i],plist[j]]," Delta_mod2=",d);
        if(d,
          found=n; best=n;
          print("FIRST_PAIR_NONZERO label=",label," n=",n," primes=",[plist[i],plist[j]]," Delta_mod2=1");
          emit_terms(M,xp,n,[plist[i],plist[j]]);
        );
      );
    );
  );
  found;
};

scan_five(label,M,xp,plist)={
  if(#plist<5, return(0));
  my(ells=vector(5,i,plist[i]), n=1);
  for(i=1,5,n*=ells[i]);
  my(d=delta_n_mod2(M,xp,n,ells));
  print("FIVE label=",label," n=",n," primes=",ells," Delta_mod2=",d);
  if(d,
    print("FIRST_FIVE_NONZERO label=",label," n=",n," primes=",ells);
    emit_terms(M,xp,n,ells);
    return(n);
  );
  0;
};

scan_quads(label,M,xp,plist)={
  my(found=0, m=min(#plist,5));
  for(i=1,m-3,
    for(j=i+1,m-2,
      for(k=j+1,m-1,
        for(h=k+1,m,
          my(ells=[plist[i],plist[j],plist[k],plist[h]], n=plist[i]*plist[j]*plist[k]*plist[h]);
          my(d=delta_n_mod2(M,xp,n,ells));
          print("QUAD label=",label," n=",n," primes=",ells," Delta_mod2=",d);
          if(d && !found,
            found=n;
            print("FIRST_QUAD_NONZERO label=",label," n=",n," primes=",ells);
            emit_terms(M,xp,n,ells);
          );
        );
      );
    );
  );
  found;
};

scan_triples(label,M,xp,plist)={
  my(found=0, m=min(#plist,5));
  for(i=1,m-2,
    for(j=i+1,m-1,
      for(k=j+1,m,
        my(ells=[plist[i],plist[j],plist[k]], n=plist[i]*plist[j]*plist[k]);
        my(d=delta_n_mod2(M,xp,n,ells), oddterms=0);
        for(a=1,n-1,
          if(gcd(a,n)==1 && ratmod2(2*mseval(M,xp,[oo,a/n])), oddterms++);
        );
        print("TRIPLE label=",label," n=",n," primes=",ells," odd_scaled_symbols=",oddterms," Delta_mod2=",d);
        if(d && !found,
          found=n;
          print("FIRST_TRIPLE_NONZERO label=",label," n=",n," primes=",ells);
          emit_terms(M,xp,n,ells);
        );
      );
    );
  );
  found;
};

symbol_parity_probe(label,M,xp,l)={
  my(odd=0);
  print("SYMBOL_PROBE label=",label," denominator=",l);
  for(a=1,l-1,
    if(gcd(a,l)==1,
      my(q=mseval(M,xp,[oo,a/l]), b=ratmod2(2*q));
      if(b, odd++; print("  ODD_SCALED a=",a," symbol=",q," scaled=",2*q));
    );
  );
  print("SYMBOL_PROBE_SUMMARY label=",label," denominator=",l," odd_scaled_count=",odd);
  odd;
};

scan(label,ainvs,N,plist)={
  my(E=ellinit(ainvs), v=msfromell(E,1), M=v[1], xp=v[2]);
  print("CURVE ",label," conductor=",N);
  for(i=1,#plist,
    if(!is_kolyvagin_prime(E,N,plist[i]), error("non-Kolyvagin prime in bound list: ",plist[i]));
  );
  my(probe=symbol_parity_probe(label,M,xp,plist[1]));
  my(s=scan_single(label,E,N,xp,M,plist));
  my(p=scan_pairs(label,E,N,xp,M,plist));
  my(t=scan_triples(label,M,xp,plist));
  my(q=scan_quads(label,M,xp,plist));
  my(f=scan_five(label,M,xp,plist));
  print("SUMMARY label=",label," probe=",probe," single=",s," pair=",p," triple=",t," quad=",q," five=",f);
  f;
};

p53=[5,7,11,31,41,43,47,59,61];
p203=[17,19,23,37,41,59,61];

f53=scan("53a1",[1,-1,1,0,0],53,p53);
f203=scan("203b1",[1,1,1,0,-2],203,p203);
print("FINAL first_five_53=",f53," first_five_203=",f203);
quit;
