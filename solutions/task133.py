def p(g,*l):
 for a in g:l+=*a,0
 w=len(g[0])+1
 for a in{*l}:
  q,*s=[l.index(a)],
  for k in q:q+=[o for i in(-w,-1,1,w)if((o:=k+i)in q)==0<=o<len(l)>0<l[o]];s+=l[k],
  if~-len(s)==s.count(a)>1:v,={*s}-{a};n=min(k for k in q if l[k]==v);z=q
 for a in{*l}-{v,0}:
  q,*s=[l.index(a)],
  for k in q:q+=[o for i in(-w,-1,1,w)if((o:=k+i)in q)==0<=o<len(l)>0<l[o]];s+=l[k],
  u=(s.count(v)^6)%6
  for k in z:
   for i in range(u*u):x=min(k for k in q if l[k]==v)+k*u-n*u;g[x//w+i//u][x%w+i%u]+=a*(g[x//w+i//u][x%w+i%u]<1)
 return g