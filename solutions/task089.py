def p(g):
 h=[g[x]*1for x in range(13)]
 for x in range(13):
  for y in range(13):
   for u in range(13):
    for v in range(13):
     if(x,y)!=(u,v)!=g[x][y]==g[u][v]in(2,3):
      for i in range(-2,3):
       for j in range(-2,3):
        if-1<u+i<13>v+j*(g[u][v]>2or-1)>-1<g[u+i][v+j*(g[u][v]>2or-1)]in{g[u+i][v+j]for i in range(-1,2)for j in range(-1,2)if-1<u+i<13>v+j>-1}-{0,2,3}:h[x+i][y+j]=g[u+i][v+j*(g[u][v]>2or-1)]
 return h