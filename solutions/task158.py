def p(g):
 e=lambda i,j:[(a,b)for a in range(i)for b in range(j)]
 T=lambda i,j,m:[r[j:j+m]for r in g[i:i+m]];h=len(g);w=len(g[0]);[(G:=H)for i,j in e(h-2,w-2)if len({*sum(H:=T(i,j,3),[])})>3];X=0
 if G[0][0]in sum(G,[])[1:]:G=G[::-1]
 while X<12:
  X+=1;m=X%3+1;g=[*map(list,zip(*g))][::-1];h,w=w,h
  for i,j in e(h-3*m+1,w-3*m+1):
    if all(T(i+k*m,j+k*m,m)==[[G[k][k]]*m]*m for k in(0,2))*(g[i-1][j]^g[i][j]):
     for x,y in e(m*3,m*3):g[i+x][j+y]=G[x//m][y//m]
 return g