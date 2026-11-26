// SCC-001 exact finite regression; Node.js, no dependencies.
// Run: node research/SCC-001/replay.js
// Theorem proof is separate from these bounded tests. Bitsets support n <= 4 here.
function replayScc(){
  function span(xs){let b=[];for(let x of xs){for(let y of b)x=Math.min(x,x^y);if(x){b.push(x);b.sort((a,b)=>b-a)}}return b}
  function contains(b,x){for(let y of b)x=Math.min(x,x^y);return x===0}
  function eq(a,b){return a.length===b.length&&a.every(x=>contains(b,x))}
  function filt(v,n,one){let f=[[one]];for(let r=1;r<=n+2;r++)f.push(span([...f[r-1],...f[r-1].flatMap(x=>v.map(y=>x&y))]));return f}
  function pop(x){let k=0;while(x){x&=x-1;k++}return k}
  let cases=0,grades=0,targets=0,ceilingChecks=0,sharpChecks=0;
  function check(n,v,u,w){let g=u&w,one=(1<<(1<<n))-1;let f=filt(v,n,one),vp=span([...v,g]),p=filt(vp,n,one),zero=[];
    const get=r=>r<0?zero:f[r];
    const Q=j=>j<0?0:span([...get(j+1),...get(j).map(x=>x&g)]).length-get(j+1).length;
    for(let r=1;r<=n+1;r++){let rhs=span([...get(r),...get(r-1).map(x=>x&g)]);if(!eq(rhs,p[r]))throw Error("filtration");if(p[r].length-p[r-1].length!==f[r].length-f[r-1].length-Q(r-2)+Q(r-1))throw Error("rank");grades++}
    const total=Array.from({length:n+1},(_,j)=>Q(j)).reduce((a,b)=>a+b,0);
    const cells=[u&w,u&(one^w),(one^u)&w,(one^u)&(one^w)].map(pop);
    if(total>Math.min(...cells)||total>Math.floor(2**(n-2)))throw Error("slice capacity");
    ceilingChecks++;
    for(let x of (n<=3?Array.from({length:1<<(1<<n)},(_,i)=>i):[0,one,g,...vp,12345&one,6789&one])){let d=f.findIndex(b=>contains(b,x)),dp=p.findIndex(b=>contains(b,x));if(d>=1){let drop=contains(span([...get(d-1),...get(d-2).map(y=>y&g)]),x);if((dp===d-1)!==drop||dp>d||dp<d-1)throw Error("target")}targets++}cases++;
  }
  let seed=90210;function rng(){seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed}
  function coords(n){return Array.from({length:n},(_,i)=>Array.from({length:1<<n},(_,j)=>((j>>i)&1)<<j).reduce((a,b)=>a|b,0))}
  function affine(n){let one=(1<<(1<<n))-1;return span([one,...coords(n)])}
  function all(v){return Array.from({length:1<<v.length},(_,i)=>v.reduce((a,b,j)=>a^(((i>>j)&1)?b:0),0))}
  for(let n=1;n<=3;n++){let v=affine(n),a=all(v);for(let u of a)for(let w of a)check(n,v,u,w)}
  for(let i=0;i<64;i++){let v=affine(4);for(let j=0;j<6;j++){let draw=()=>v.reduce((a,b)=>a^((rng()>>>31)?b:0),0);let u=draw(),w=draw();check(4,v,u,w);v=span([...v,u&w])}}
  for(let n=2;n<=4;n++){let v=affine(n),f=filt(v,n,(1<<(1<<n))-1),[u,w]=coords(n);let total=0;for(let j=0;j<=n;j++)total+=span([...f[j+1],...f[j].map(x=>x&u&w)]).length-f[j+1].length;if(total!==2**(n-2))throw Error("sharpness");sharpChecks++}
  return {cases,grades,targets,ceilingChecks,sharpChecks,seed:90210,status:"PASS",scope:"finite regression only"};
}
console.log(JSON.stringify(replayScc(),null,2));
