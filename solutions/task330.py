def p(g):
 for i in range(100):
  q=[i+i//10]
  for x in q:q+=[k for o in b"AKMW"if~-((k:=x+o-76)in q)*[*[*g,11*[0]][k//11],0][k%11]]
  g[i//10][i%10]>>=2-(6==len(q))
 return g