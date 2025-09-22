def p(e,*s):
 def p(z):
  return *zip(*[((i,f,n),(i,-n,f))for i,n,f in z]),
 d,*r=len(e[0]),
 for u in range(len(e)*d):
  for i,n,f in(z:=[(t:=e[g:=u//d][o:=u%d],g,o)]*t):e[n][f]=0;z+=[(i,o,z)for u in range(9)if(o:=n+u//3-1)//len(e)|(z:=f+u%3-1)//d==0<(i:=e[o][z])]
  r+=z*(len(z)<5*t);s+=p((i,n-g,f-o)for i,n,f in z)
 for u in range(len(e)*d):
  for z in sum(map(p,s),s):
   for i,n,f in(z:=[(i,n+u//d,f+u%d)for i,n,f in z])*(len({*r}&{*z})>2):e[n][f]=i
 return e