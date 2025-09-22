def p(e,*s):
 def p(z):
  return *zip(*[((i,m,n),(i,-n,m))for i,n,m in z]),
 d,*r=len(e[0]),
 for u in range(len(e)*d):
  for i,n,m in(z:=[(t:=e[g:=u//d][j:=u%d],g,j)]*t):e[n][m]=0;z+=[(i,o,z)for u in range(9)if(o:=n+u//3-1)//len(e)|(z:=m+u%3-1)//d==0<(i:=e[o][z])]
  r+=z*(len(z)<5*t);s+=p((i,n-g,m-j)for i,n,m in z)
 for u in range(len(e)*d):
  for z in sum(map(p,s),s):
   for i,n,m in(z:=[(i,n+u//d,m+u%d)for i,n,m in z])*(len({*r}&{*z})>2):e[n][m]=i
 return e