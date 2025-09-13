def T(O):return*zip(*[((u,c,r),(u,-r,c))for u,r,c in O]),
def p(d,*E):
 R,H,W,*U=range,len(d),len(d[0])
 for z in R(H*W):
  for u,r,c in(O:=[(v:=d[i:=z//W][j:=z%W],i,j)]*v):d[r][c]=0;O+=[(u,x,y)for z in R(9)if(x:=r+z//3-1)//H|(y:=c+z%3-1)//W==0<(u:=d[x][y])]
  U+=O*(len(O)<5*v);E+=T((u,r-i,c-j)for u,r,c in O)
 for*O,in sum(map(T,E),E):
  for z in R(H*W):
   for u,r,c in(S:=[(u,r+z//W,c+z%W)for u,r,c in O])*(len({*U}&{*S})>2):d[r][c]=u
 return d