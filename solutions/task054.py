def p(g):
 h=[r*1for r in g]
 for i in range(28):
  for j in range(28):
   if g[i][j+1]==g[i][j-1]!=g[i][j]!=g[i+1][j]==g[i-1][j]>0<len({g[i+1][j],g[i][j+1],g[i+1][j+1]})>1:
    for k in range(28):
     for l in range(28):
      if g[i][j]==g[k][l]:
       for m in range(-1,2):
        for n in range(-1,2):
         if g[i+m][j+n]!=g[i+1][j+2]:
          o=1;h[k+m*o][l+n*o]=g[i+m][j+n];o+=1
          if g[i][j]!=g[i+m*o][j+n*o]!=g[i+1][j+2]:
           while g[k+m*o][l+n*o]!=g[i+1][j+2]:h[k+m*o][l+n*o]=g[i+m][j+n];o+=1
    for m in range(-2,3):
     for n in range(-2,3):
      h[i+m][j+n]=g[i+1][j+2]
    return h