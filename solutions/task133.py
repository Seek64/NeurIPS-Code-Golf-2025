def p(n,*x):
 for e in n:x+=*e,0
 for e in{*x}:
  g,*o=[x.index(e)],
  for d in g:g+=[i+d for i in(~len(n[0]),-1,1,-~len(n[0]))if(i+d in g)==0<=i+d<len(x)>0<x[i+d]];o+=x[d],
  if~-len(o)==o.count(e)>1:r,={*o}-{e};t=min(d for d in g if x[d]==r);c=g
 for e in{*x}-{r}:
  g,*o=[x.index(e)],
  for d in g:g+=[i+d for i in(~len(n[0]),-1,1,-~len(n[0]))if(i+d in g)==0<=i+d<len(x)>0<x[i+d]];o+=x[d],
  for d in c:
   for i in range(o.count(r)):a=(o.count(r)^6)%6;u=min(d for d in g if x[d]==r)+d*a-t*a;n[u//-~len(n[0])+i//a][u%-~len(n[0])+i%a]=n[u//-~len(n[0])+i//a][u%-~len(n[0])+i%a]or e
 return n