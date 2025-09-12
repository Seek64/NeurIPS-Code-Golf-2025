def T(V):_,x,y=V[0];return[*zip(*[((u,x+y-c,r-x+y),(u,c-y+x,x+y-r),(u,2*x-r,c),(u,r,2*y-c))for u,r,c in V])]
def p(d,*E):
 R,H,W,*U=range,len(d),len(d[0])
 for z in R(H*W):
  O=[(v:=d[i:=z//W][j:=z%W],i,j)]*v
  for u,r,c in O:d[r][c]=0;O+=[(u,x,y)for a in R(9)if W>(y:=c+a%3-1)>=0<H>(x:=r+a//3-1)>=0<(u:=d[x][y])]
  if len({*O})>3:E+=O,
  else:U+=O
 for O in E:
  for i in R(-H,H):
   for j in R(-W,W):
    B=T(Q:=[(u,r+i,c+j)for u,r,c in{*O}])
    for u,r,c in[*[I for I in[Q]+B+T(B[0])if len({*U}&{*I})>2],[]][0]:d[r][c]=u
 return d