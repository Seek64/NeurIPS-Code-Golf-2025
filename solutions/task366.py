def p(g):
 U=sum(g,g);V=U.count;C=max(U,key=V);N=M=len(g)//2;L=len(g[0]);G=g[:N];H=g[N:]
 if C in g[0]:return[r for*r,in zip(*p([r[::-1]for*r,in zip(*g)]))][::-1]
 S,T=[{(Q[x][y],x,y)for x in range(M)for y in range(L)if V(Q[x][y])<13}for Q in(G,H)]
 n=lambda _,s,t:[(G[x][y],x,y)for x in[s,s-1,s+1]for y in[t]+[t-1,t+1]*(x==s)if(M>x>-1<y<L)]
 while N:
  N-=1
  for P in S:
   for b in n(*P):
    f={P}
    while f<(f:={y for x in f for y in n(*x)if y[0]in[P[0],b[0]&15]}):1
    for Q in[*T]*(len([x for x in f if x[0]==P[0]])>N):
     h=[x*1for x in H]
     for F in f:
      x=Q[1]-P[1]+F[1];y=Q[2]-P[2]+F[2]
      if 1-(M>x>-1<y<L)or H[x][y]!=[P[0],C][F[0]==b[0]]:break
      h[x][y]=F[0]
     else:
      H=h
 return H
