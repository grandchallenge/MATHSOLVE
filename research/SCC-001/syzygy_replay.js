// Exact finite regression; Node.js, no dependencies; n<=4.
// Run: node research/SCC-001/syzygy_replay.js
function scc2Replay(){
  const span=xs=>{let b=[];for(let x of xs){for(const y of b)x=Math.min(x,x^y);if(x){b.push(x);b.sort((a,b)=>b-a)}}return b};
  const red=(b,x)=>{for(const y of b)x=Math.min(x,x^y);return x};
  const same=(a,b)=>a.length===b.length&&a.every(x=>red(b,x)===0);
  const extend=(base,xs)=>{let b=span(base),out=[];for(const x of xs)if(red(b,x)){out.push(x);b=span([...b,x])}return out};
  const coords=n=>Array.from({length:n},(_,i)=>Array.from({length:1<<n},(_,j)=>((j>>i)&1)<<j).reduce((a,b)=>a|b,0));
  const affine=n=>span([(1<<(1<<n))-1,...coords(n)]);
  const all=v=>Array.from({length:1<<v.length},(_,i)=>v.reduce((a,b,j)=>a^(((i>>j)&1)?b:0),0));
  const filt=(v,n)=>{let f=[[(1<<(1<<n))-1]];for(let j=1;j<=n+3;j++)f.push(span([...f[j-1],...f[j-1].flatMap(x=>v.map(y=>x&y))]));return f};
  function kernel(inputs,map){let piv=[],out=[];for(const a of inputs){let x=map(a),w=a;for(const [y,z] of piv)if((x^y)<x){x^=y;w^=z}if(!x)out.push(w);else{piv.push([x,w]);piv.sort((p,q)=>q[0]-p[0])}}return span(out)}
  function need(x,msg){if(!x)throw Error(msg)}
  let transitions=0,gradeChecks=0,relations=0,linearChecks=0,squareChecks=0,nonzeroTransitions=0;
  function check(n,V,u,v){const g=u&v,F=filt(V,n),P=filt(span([...V,g]),n),f=j=>j<0?[]:F[j],p=j=>j<0?[]:P[j];
    const C=[],H=[],K=[];let rank=0;
    for(let j=0;j<=n+1;j++){
      C[j]=extend(p(j-1),f(j));
      K[j]=kernel(f(j),x=>red(f(j+1),g&x));
      need(p(j-1).every(x=>red(K[j],x)===0),"quotient base in kernel");
      H[j]=extend(p(j-1),K[j]);
      rank+=span(H[j].map(x=>red(p(j),g&x))).length;
      need(H[j].every(x=>red(f(j+1),g&x)===0),"delta degree");
      need(p(j-1).every(x=>red(p(j),g&x)===0),"delta well-defined");
      for(const a of H[j]){need(red(f(j+2),g&(g&a))===0,"delta image in annihilator");need(red(p(j+1),g&(g&a))===0,"delta square");squareChecks++}
      const actual=span([...p(j-1),...f(j),...(j?C[j-1].map(x=>g&x):[])]);
      need(same(actual,p(j)),"presentation surjectivity");
      const domain=C[j].length+(j?C[j-1].length:0),target=p(j).length-p(j-1).length;
      need(domain-target===(j?H[j-1].length:0),"presentation kernel dimension");
      if(j)for(const a of H[j-1]){
        const oldLift=all(C[j]).find(x=>red(p(j-1),x^(g&a))===0);
        need(oldLift!==undefined,"cross relation expressed in old quotient");
        need(red(p(j-1),oldLift^(g&a))===0,"cross relation in new algebra");relations++;
      }
      gradeChecks++;
    }
    for(let j=0;j<=n;j++)for(let k=0;k<=n-j;k++)for(const a of H[j])for(const b of C[k]){
      const ab=a&b;
      need(red(K[j+k],ab)===0,"H module");
      const reducedAB=red(p(j+k-1),ab),deltaA=red(p(j),g&a);
      need(red(p(j+k),(g&reducedAB)^(deltaA&b))===0,"C-linearity");
      linearChecks++;
    }
    if(rank)nonzeroTransitions++;transitions++;return rank;
  }
  let seed=90210;const rng=()=>seed=(Math.imul(seed,1664525)+1013904223)>>>0;
  for(let n=1;n<=3;n++){const V=affine(n),a=all(V);for(const u of a)for(const v of a)check(n,V,u,v)}
  for(let i=0;i<64;i++){let V=affine(4);for(let j=0;j<6;j++){const draw=()=>V.reduce((a,b)=>a^((rng()>>>31)?b:0),0);const u=draw(),v=draw();check(4,V,u,v);V=span([...V,u&v])}}
  const fixture=[];for(const n of [3,4]){const [a,b,c]=coords(n),V=span([...affine(n),a&b]);const rank=check(n,V,a,c);need(rank===2**(n-3),"spectator rank");fixture.push({n,rank})}
  return {status:"PASS",transitions,gradeChecks,relations,linearChecks,squareChecks,nonzeroTransitions,fixture,seed:90210,scope:"finite regression; no formal certification"};
}
console.log(JSON.stringify(scc2Replay(),null,2));
