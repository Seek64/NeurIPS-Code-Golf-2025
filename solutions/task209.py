e=enumerate
def p(g,m=2):
 C=[(c^4,x,y)for x,r in e(g)for y,c in e(r)if c];Y,Z=sorted(C)[:4:3];_,P,Q=C[2];D=C[C.index(Z)+1:]
 for a,b,c in D:
  G=[r*9for r in g*2];n=5
  for u,v,w in D:s=P+m*(v-b);t=Q+m*(w-c);n+=1+m*m*(G[s][t]==u^4);exec("G[s][t:t+m]=[u^4]*m;s+=1;"*m)
  if n>len(C):return[r[Y[2]:Z[2]+1]for r in G[Y[1]:Z[1]+1]]
 return p(g,m+1)