def p(g):
 l=sum(g,[]);w=len(g[0]);h=len(g)
 *f,c,d=sorted({*l},key=l.count)
 o=[r[:]for r in g]
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   for k in[0,1,2,3]*(v in f):
    x,y=i,j
    while h>(x:=x+1-k%2*2)>=0<=(y:=y+1-k//2*2)<w and g[x][y]in[c,d]:o[x][y]=[*{*f}-{v},v][g[x][y]==max(l:=[0,*r][j:j+3]+[g[i-1][j],g[i-h+1][j]],key=lambda x:(l.count(x),-(w*[x]in g)))]
 return o