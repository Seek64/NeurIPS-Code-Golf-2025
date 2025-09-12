def T(V,R):_,x,y=V[0];return[*zip(*[R*((u,-c+y+x,r-x+y),(u,c-y+x,x+y-r))or((u,2*x-r,c),(u,r,2*y-c))for u,r,c in V])]
def p(d,*E):
 U=[];R=range;H=len(d);W=len(d[0])
 for z in R(H*W):
  O=[(v:=d[i:=z//W][j:=z%W],i,j)]*(v>0);d[i][j]=0
  for v in O:O+=[exec("d[x][y]=0")or(c,x,y)for a in R(9)if W>(y:=v[2]+a%3-1)>=0<H>(x:=v[1]+a//3-1)>=0<(c:=d[x][y])]
  if len(O)>3:E+=O,
  else:U+=O
 for O in E:
  for i in R(-H,H):
   for j in R(-W,W):
    B=T(Q:=[(u,r+i,c+j)for u,r,c in O],1)
    for u,r,c in[*[I for I in[Q]+B+T(Q,0)+T(B[0],0)if sum(v in U for v in I)>2],[]][0]:d[r][c]=u
 return d