import re
def p(p):
 f=-1;a=[max(e:=sum(p,[]),key=e.count)]
 for i in range(6,0,-1):
  if r:=[f*[u]for f in range(1%i+1,7)for u in{*e}-{*a}if re.search(f"{u}.."*f+f"[^{u}].."*(2*i-1-2*f)+f"{u}"*(f<i),f"{p,*zip(*p)}"+f"{p,*zip(*p)}"[::-1])]:
   if(f:=f+1)<1:n=[a*(2*i-1)]*(2*i-1)
   for u in(1,1,-1)*4:n=[a[::u]for*a,in zip(*n)];a+=r[0];n[f][f:f+len(r[0])]=r[0]
 return n