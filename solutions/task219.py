def p(g):
 a=min(i for i in range(8)if any(g[i]))
 for n in range(8):
  for i in range(b:=min(i for i in range(a,9)if any(g[i])-1)+1,a-b+16):
   if j:=[4-j for j in range(5)if all([g[i+k-a][c+j-2]<1,g[k][c]==(2*g[i+k-a][:1]+g[i+k-a])[c+j]][c<9-n]for k in range(a,b)for c in range(8))]:j=j[0];g[i:i+b-a]=[[g[i+k-a][c]or(g[i+k-a][:2]+g[k]+g[k][-2:])[c+j]%7for c in range(10)]for k in range(a,b)]
 return g
