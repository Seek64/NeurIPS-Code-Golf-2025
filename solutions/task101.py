def p(g):
 w,*l=len(g[0])+2,
 for x in g:l+=*x,0,0
 q=[l.index(1)]
 for x in q:q+=[x+i for i in(-w,-1,1,w)if(x+i in q)==0<x+i<len(l)>0<l[x+i]]
 a=min(x for x in q if l[x]>1);s=q
 for i in range(len(l)):
  q=[i]
  for x in q:q+=[x+i for i in(-w,-1,1,w)if(x+i in q)==0<x+i<len(l)>0<l[x+i]]
  u=6+26%len(q)>>2
  for j in s:
   for x in range(u*u*all(l[x]>1for x in q)):l[i+u*j-u*a+x//u*w+x%u]=l[j]
 return[l[i*w:][:w-2]for i in range(len(g))]