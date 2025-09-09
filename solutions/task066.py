def q(g,x,y,u,v,t=0):
 c=g=[r*1for r in g]
 while 0<x<len(g)-1>y>0==(c:=g[x+u][y+v]):x=x+u;y=y+v;g[x][y]=3
 if c==8>t+6:return q(g,x,y,v,u,t+1)or q(g,x,y,-v,-u,t+1)
 return(c==2)*g
def p(g):
 for x in range(len(g)):
  for y in range(len(g)):
   for u in-1,0,1:
    for v in-1,0,1:
     if g[x][y]==3==g[x-u][y-v]>g[x+u][y+v]:
      if r:=q(g,x,y,u,v):return r