import re
def p(g):
 m=-1;a=[max(S:=sum(g,[]),key=S.count)]
 for l in range(6,0,-1):
  if M:=[i*[c]for i in range(1%l+1,7)for c in{*S}-{*a}if re.search(f"{c}.."*i+f"[^{c}].."*(2*l-1-2*i)+f"{c}"*(i<l),f"{g,*zip(*g)}"+f"{g,*zip(*g)}"[::-1])]:
   if(m:=m+1)<1:r=[a*(2*l-1)]*(2*l-1)
   for i in(1,1,-1)*4:r=[r[::i]for*r,in zip(*r)];a+=M[0];r[m][m:m+len(M[0])]=M[0]
 return r