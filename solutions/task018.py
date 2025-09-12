def T(O):return*zip(*[((u,c,r),(u,-r,c),(u,r,-c))for u,r,c in O]),
def p(d,*E):
 R,H,W,*U=range,len(d),len(d[0])
 for z in R(H*W):
  O=[(v:=d[i:=z//W][j:=z%W],i,j)]*v
  for u,r,c in O:d[r][c]=0;O+=[(u,x,y)for a in R(9)if W>(y:=c+a%3-1)>=0<H>(x:=r+a//3-1)>=0<(u:=d[x][y])]
  if len({*O})>3:E+=T((u,r-i,c-j)for u,r,c in O);E+=T(E[-3])
  else:U+=O
 for*O,in E:
  for z in R(H*W):
   S=[(u,r+z//W,c+z%W)for u,r,c in O]
   for u,r,c in(len({*U}&{*S})>2)*S:d[r][c]=u
 return d