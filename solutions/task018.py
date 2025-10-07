def p(e,*h):
 def p(f):
  return *zip(*[((z,i,s),(z,-s,i))for z,s,i in f]),
 d,*r=len(e[0]),
 for u in range(len(e)*d):
  for z,s,i in(f:=[(m:=e[n:=u//d][u:=u%d],n,u)]*m):e[s][i]=0;f+=[(z,o,f)for u in range(9)if(z:=((e+e)[o:=s+u//3-1]+[0])[f:=i+u%3-1])]
  r+=f*(len(f)<5*m);h+=p((z,s-n,i-u)for z,s,i in f)
 for u in range(len(e)*d):
  for f in sum(map(p,h),h):
   for z,s,i in(f:=[(z,s+u//d,i+u%d)for z,s,i in f])*(len({*r}&{*f})>2):e[s][i]=z
 return e