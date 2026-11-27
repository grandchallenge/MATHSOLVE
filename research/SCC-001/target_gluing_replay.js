// Exact bounded regression, Node.js, n<=4. No dependencies.
// Run node research/SCC-001/target_gluing_replay.js
function replay(){
  const span=xs=>{let b=[];for(let x of xs){for(const y of b)x=Math.min(x,x^y);if(x){b.push(x);b.sort((a,b)=>b-a)}}return b};
  const rem=(b,x)=>{for(const y of b)x=Math.min(x,x^y);return x};
  const eq=(a,b)=>a.length===b.length&&a.every(x=>rem(b,x)===0);
  const coords=n=>Array.from({length:n},(_,i)=>Array.from({length:1<<n},(_,j)=>((j>>i)&1)<<j).reduce((a,b)=>a|b,0));
  const one=n=>(1<<(1<<n))-1;
  const affine=n=>span([one(n),...coords(n)]);
  const all=v=>Array.from({length:1<<v.length},(_,i)=>v.reduce((a,b,j)=>a^(((i>>j)&1)?b:0),0));
  const filt=(v,n)=>{let f=[[one(n)]];for(let j=1;j<=n+1;j++)f.push(span([...f[j-1],...f[j-1].flatMap(x=>v.map(y=>x&y))]));return f};
  const need=(x,m)=>{if(!x)throw Error(m)};
  const intersectDim=(a,b)=>a.length+b.length-span([...a,...b]).length;
  const glue=(f,t)=>span([...f,...f.map(x=>x&t)]);
  let transitions=0,grades=0,composition=0,spectators=0,nonmonotone=0;
  function check(n,F,P,g,t){let N=F.map(f=>glue(f,t)),M=P.map(f=>glue(f,t));
    for(let j=0;j<=n+1;j++){
      const f=F[j],p=P[j],a=N[j],b=M[j],prior=j?N[j-1]:[],gp=j?prior.map(x=>x&g):[];
      need(eq(b,span([...a,...gp])),"M promotion");
      const d=a.length-f.length,dp=b.length-p.length;
      need(d===span(f.map(x=>x&t)).length+span(f.map(x=>x&(one(n)^t))).length-f.length,"branch formula");
      const K=intersectDim(a,p)-f.length,C=b.length-span([...a,...p]).length;
      const image=span([...a,...p,...gp]).length-span([...a,...p]).length;
      need(C===image&&dp===d-K+C,"exact sequence");
      need(K>=0&&C>=0&&C<=(j?N[j-1].length-F[j-1].length:0),"birth source");
      need(d<=Math.min(span(f.map(x=>x&t)).length,span(f.map(x=>x&(one(n)^t))).length),"branch bound");
      if(dp>d)nonmonotone++;
      grades++;
    }
    const d=F.findIndex(b=>rem(b,t)===0),dp=P.findIndex(b=>rem(b,t)===0);
    need(d>=0&&dp>=0&&dp<=d&&dp>=d-1,"marked target lifetime");
    transitions++;
  }
  let seed=90210;const rng=()=>seed=(Math.imul(seed,1664525)+1013904223)>>>0;
  for(let n=1;n<=3;n++){const v=affine(n),F=filt(v,n),a=all(v);for(const u of a)for(const w of a){const g=u&w,P=filt(span([...v,g]),n);for(let t=0;t<=one(n);t++)check(n,F,P,g,t)}}
  for(let i=0;i<64;i++){let n=4,v=affine(n),prev=null;const targets=[rng()&one(n),rng()&one(n),coords(n)[0],one(n)^1];for(let j=0;j<6;j++){
    let draw=()=>v.reduce((a,b)=>a^((rng()>>>31)?b:0),0),g=draw()&draw(),next=span([...v,g]),F=filt(v,n),P=filt(next,n);
    for(const t of targets){check(n,F,P,g,t);if(prev)for(let r=0;r<=n+1;r++){
      const old=glue(prev[r],t);
      const middle=span([...F[r],...old]),direct=span([...P[r],...old]);
      need(eq(direct,span([...P[r],...middle])),"composition of images");composition++;
    }}prev=F;v=next;
  }}
  // spectator shift formula for each grade, with every 2-bit target
  for(let t=0;t<16;t++){const F=filt(affine(2),2),P=filt(affine(3),3),T=t|(t<<4);for(let r=0;r<=4;r++){const D=j=>j<0?0:glue(F[Math.min(j,F.length-1)],t).length-F[Math.min(j,F.length-1)].length;need(glue(P[r],T).length-P[r].length===D(r)+D(r-1),"spectator convolution");spectators++}}
  // F=a already available: gate bc increases degree-one gluing dimension 2 -> 3.
  const [a,b,c]=coords(3),V=affine(3),F=filt(V,3),P=filt(span([...V,b&c]),3);const d=f=>glue(f,a).length-f.length;
  need(d(F[1])===2&&d(P[1])===3,"completed-target fixture");
  return {status:"PASS",transitions,grades,composition,spectators,nonmonotone,seed:90210,fixture:[d(F[1]),d(P[1])]};
}
console.log(JSON.stringify(replay(),null,2));
