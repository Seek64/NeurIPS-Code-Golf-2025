def T(V,R):_,x,y=V[0];return[*zip(*[R*((u,-c+y+x,r-x+y),(u,c-y+x,x+y-r))or((u,2*x-r,c),(u,r,2*y-c))for u,r,c in V])]
def p(d):
 V,U,*E=[],[];R=range;H=len(d);W=len(d[0])
 for z in R(H*W):
  O={(v:=d[i:=z//W][j:=z%W],i,j)};C=set()
  while O-{*V+U}and v:
   if{v:=O.pop()}-C:C|={v};O|={(c,x,y)for a in R(9)if W>(y:=v[2]+a%3-1)>=0<H>(x:=v[1]+a//3-1)>=0<(c:=d[x][y])}
  if len(C)>3:E+=C,;V+=C
  else:U+=C
 for O in E:
  for i in R(-H,H):
   for j in R(-W,W):
    B=T(Q:=[(v[0],v[1]+i,v[2]+j)for v in O],1)
    for(_,x,y),(u,r,c)in zip(O,[*[I for I in[Q]+B+T(Q,0)+T(B[0],0)if sum(v in U for v in I)>2],O][0]):d[r][c]=u;d[x][y]=0
 return d