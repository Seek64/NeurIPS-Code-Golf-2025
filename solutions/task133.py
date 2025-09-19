def p(g,*l):
 for a in g:l+=*a,0
 for a in{*l}:
  q,*s=[l.index(a)],
  for k in q:q+=[i+k for i in(~len(g[0]),-1,1,-~len(g[0]))if(i+k in q)==0<=i+k<len(l)>0<l[i+k]];s+=l[k],
  if~-len(s)==s.count(a)>1:v,={*s}-{a};n=min(k for k in q if l[k]==v);z=q
 for a in{*l}-{v,0}:
  q,*s=[l.index(a)],
  for k in q:q+=[i+k for i in(~len(g[0]),-1,1,-~len(g[0]))if(i+k in q)==0<=i+k<len(l)>0<l[i+k]];s+=l[k],
  u=(s.count(v)^6)%6
  for k in z:
   for i in range(u*u):x=min(k for k in q if l[k]==v)+k*u-n*u;g[x//-~len(g[0])+i//u][x%-~len(g[0])+i%u]=g[x//-~len(g[0])+i//u][x%-~len(g[0])+i%u]or a
 return g