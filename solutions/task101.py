import math
e=enumerate
def p(g,m=3):
 P=[(c,x,y)for x,r in e(g)for y,c in e(r)if c];R=max(B:={p for p in P for b in P if b[0]<2>math.dist(b,p)})
 for q in P:
  G=[m*[0]+r for r in g*9];n=len(B)*m
  for c,x,y in B:
   M=s=q[1]+m*(x-R[1]);t=q[2]-m*(~y+R[2])
   while s<M+m:n-=G[s][t:t+m]==[c&2]*m;G[s][t:t+m]=[c|8]*m;s+=1
  if(q!=R*m)*n<1:g=[G[i][m:]for i,_ in e(g)]
 return[[c&7for c in r]for r in g]*(2-m)or p(g,m-1)