def p(g):
 l=sum(g,t:=[]);f=sorted(l,key=l.count)[:2]
 for i in range(len(g)):
  for j in range(len(g[i])):
   if g[i][j]in f:l[g[i][j]]=g[i][j];l[max(l,key=lambda l:([g[i][j-1],g[i][j-len(g[i])+1],g[i-1][j],g[i-len(g)+1][j]].count(l),-(len(g[i])*[l]in g)))]=g[i][j];f+=-i-j,;t+=i-j,
 for i in range(len(g)):
  for j in range(len(g[i])):
   if i-j in t or-i-j in f:g[i][j]=l[g[i][j]]
 return g