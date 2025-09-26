def p(g):
 l=sum([[*x,0,0]for x in g],[])
 w=len(g[0])+2
 q=[l.index(1)]
 for x in q:q+=[x+i for i in(-w,-1,1,w)if(x+i in q)==0<=x+i<len(l)>0<l[x+i]]
 a=min(x for x in q if l[x]>1);s=q
 for i in range(len(l)):
  q=[i]
  for x in q:q+=[x+i for i in(-w,-1,1,w)if(x+i in q)==0<=x+i<len(l)>0<l[x+i]]
  if all(l[x]>1for x in q):
   u=6+26%len(q)>>2
   for j in s:
    for x in range(u*u):l[i+(j-a)*u+x//u*w+x%u]=l[j]
 return[l[i*w:][:w-2]for i in range(len(g))]