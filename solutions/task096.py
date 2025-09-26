import re
def p(n):
 z=-1;c=[max(a:=sum(n,[]),key=a.count)]
 for i in range(6,0,-1):
  if r:=[f*[s]for f in range(1%i+1,7)for s in{*a}-{*c}if re.search(f"{s}.."*f+f"[^{s}].."*(2*i-1-2*f)+f"{s}"*(f<i),f"{n,*zip(*n)}"+f"{n,*zip(*n)}"[::-1])]:
   if(z:=z+1)<1:u=[c*(2*i-1)]*(2*i-1)
   for f in(1,1,-1)*4:u=[u[::f]for*u,in zip(*u)];c+=r[0];u[z][z:z+len(r[0])]=r[0]
 return u