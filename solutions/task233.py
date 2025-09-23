def p(g):
 R=range;S={}
 for i in range(len(g)-2):
  for j in range(len(g[0])-2):
   m=[g[i+k//3][j+k%3]for k in range(9)]
   if(0 in m)<1<len(C:={*m}):
    K=tuple(x==2for x in m);D={K:sum(C)-2}
    for k in range(9):S[K]=D;K=tuple(K[k%3*3+2-k//3]for k in range(9));g[i+k//3][j+k%3]=0
 g=[*map(list,zip(*filter(any,[*map(list,zip(*filter(any,g)))])))]
 for c in(0,1):
  for i in range(len(g)-2):
   for j in range(len(g[0])-2):
    m=[g[i+k//3][j+k%3]for k in range(9)]
    P=tuple(x<1for x in m);D=S.get(P)
    if D and(c or P in D):
     v=D.popitem()[1]
     for k in range(9):g[i+k//3][j+k%3]=(v,2)[P[k]]
 return g