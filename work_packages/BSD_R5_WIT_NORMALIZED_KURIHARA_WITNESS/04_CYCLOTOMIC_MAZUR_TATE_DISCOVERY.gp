\\ BSD R5-WIT cyclotomic Mazur-Tate discovery.
\\ Coefficient of the real-layer class {+/- a} is 2*[a/2^(n+2)]^+.
\\ Exact rational plus symbols via PARI/GP 2.15.4.

ratmod2(q)={
  my(n=numerator(q), d=denominator(q));
  if(d % 2 == 0, error("even denominator in integral real-layer coefficient: ",q));
  lift(Mod(n,2)/Mod(d,2));
};

theta_layer(label,ainvs,n)={
  my(E=ellinit(ainvs), v=msfromell(E,1), M=v[1], xp=v[2]);
  my(m=2^(n+2), half=m/2, nonzero=0, aug=0);
  print("THETA_BEGIN label=",label," layer=",n," modulus=",m);
  for(a=1,half-1,
    if(gcd(a,m)==1,
      my(q=mseval(M,xp,[oo,a/m]), c=2*q, b=ratmod2(c));
      if(b,
        nonzero++;
        print("  THETA_ODD class_pm=",a," symbol=",q," coeff=",c," mod2=1");
      );
      aug=(aug+b)%2;
    );
  );
  print("THETA_SUMMARY label=",label," layer=",n," modulus=",m,
        " nonzero_coeffs=",nonzero," augmentation_mod2=",aug,
        " group_ring_nonzero_mod2=",if(nonzero>0,1,0));
  nonzero;
};

for(n=1,4,
  theta_layer("53a1",[1,-1,1,0,0],n);
  theta_layer("203b1",[1,1,1,0,-2],n);
);
quit;
