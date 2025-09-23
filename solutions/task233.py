def p(g,S={}):
 for i in range(len(g)-2):
  for j in range(len(g[0])-2):
   m=[g[i+k//3][j+k%3]for k in range(9)]
   P=*[x==2for x in m],;D={P:sum(C:={*m})-2}
   if(0 in m)<1<len(C):
    for k in range(9):S[P]=D;P=*[P[k%3*3+2-k//3]for k in range(9)],;g[i+k//3][j+k%3]=0
 g=[*map(list,zip(*filter(sum,zip(*filter(sum,g)))))]
 for i in range(len(g)-2):
  for j in range(len(g[0])-2):
   m=[g[i+k//3][j+k%3]for k in range(9)]
   P=*[x!=2for x in m],;D=S.get(P)
   if D and P in D:
    v=D.popitem()[1]
    for k in range(9):g[i+k//3][j+k%3]=(v,2)[P[k]]
 for i in range(len(g)-2):
  for j in range(len(g[0])-2):
   m=[g[i+k//3][j+k%3]for k in range(9)]
   P=*[x!=2for x in m],;D=S.get(P)
   if D:
    v=D.popitem()[1]
    for k in range(9):g[i+k//3][j+k%3]=(v,2)[P[k]]
 return g