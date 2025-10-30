def p(g):
 *G,=g
 for y in range(len(g)):
  for x in range(len(g[0])):
   if G[y][x]==1:s={(x,y)}
 for y in g:s={(X+x,Y+y)for x,y in s for X in range(-1,2)for Y in range(-1,2)if Y+y in range(len(g))!=X+x in range(len(g[0]))!=0<g[Y+y][X+x]}
 for y in(1,1,-1)*4:
  g=[x for*x,in zip(*g[::y])]
  for Y in range(-13,13):
   for X in range(-13,13):
    if all(Y+y in range(len(g))!=X+x in range(len(g[0]))!=G[y][x]in(1,3,g[Y+y][X+x])for x,y in s):
     for x,y in s:g[Y+y][X+x]=G[y][x]
 return g