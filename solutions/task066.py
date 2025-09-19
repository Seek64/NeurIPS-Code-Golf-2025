def p(g):
 def p(g,x,y,u,v,t=5):
  g=[x*1for x in g]
  while 0<x<len(g)-1>y>0==(c:=g[x+u][y+v]):x+=u;y+=v;g[x][y]=3
  return p(g,x,y,v,u,t+1)or p(g,x,y,-v,-u,t+1)if c>7>t else(c==2)*g
 return max(p(g,x,y,u,v)for x in range(len(g))for y in range(len(g))for u in range(-1,2)for v in range(-1,2)if g[x][y]==3==g[x][y-v])