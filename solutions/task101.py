def p(g):
 w,*l=len(g[0])+2,
 for x in g:l+=*x,0,0
 q=[l.index(1)]
 for x in q:q+=[x for x in(x-w,x-1,x+1,x+w)if(x in q)==0<x<len(l)>0<l[x]]
 a=min(x for x in q if l[x]>1);r=q
 for i in range(len(l)):
  q=[i]
  for x in q:q+=[x for x in(x-w,x-1,x+1,x+w)if(x in q)==0<x<len(l)>0<l[x]]
  u=6+26%len(q)>>2
  for x in r:
   for j in range(u*u*all(l[x]>1for x in q)):l[i+u*x-u*a+j//u*w+j%u]=l[x]
 return[l[i*w:][:w-2]for i in range(len(g))]