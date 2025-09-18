def p(g):
 l=sum([[*r,0]for r in g],[]);w=len(g[0])+1
 for a in{*l}:
  q=[l.index(a)]
  for x in q:q+=[k for o in(-w,-1,1,w)if((k:=x+o)in q)==0<=k<len(l)>0<l[k]]
  e,*f=sorted(s:=[l[k]for k in q],key=s.count)
  if len(f)>1==len({*f}):v=e;z=q;n=min(k for k in q if l[k]==v)
 for a in{*l}-{v,0}:
  q=[l.index(a)]
  for x in q:q+=[k for o in(-w,-1,1,w)if((k:=x+o)in q)==0<=k<len(l)>0<l[k]]
  o=min(k for k in q if l[k]==v)
  u=l[o:o+4].count(v)
  for k in z:
   for i in range(u*u):g[o//w+(k//w-n//w)*u+i//u][o%w+(k%w-n%w)*u+i%u]+=a*(g[o//w+(k//w-n//w)*u+i//u][o%w+(k%w-n%w)*u+i%u]<1)
 return g