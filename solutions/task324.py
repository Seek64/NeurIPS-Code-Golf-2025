def p(g,*t):
 l=sum(g,[]);m={};*f,j,y=sorted({*l},key=l.count)
 for i in range(len(g)):
  for j in range(len(g[i])):
   if g[i][j]in f:m[g[i][j]]=g[i][j];m[max(l:=[g[i][j-1],g[i][j-len(g[i])+1],g[i-1][j],g[i-len(g)+1][j]],key=lambda x:(l.count(x),-(len(g[i])*[x]in g)))]=g[i][j];f+=-i-j,;t+=i-j,
 for i in range(len(g)):
  for j in range(len(g[i])):
   if i-j in t or-i-j in f:g[i][j]=m[g[i][j]]
 return g