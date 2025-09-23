def p(g):
 e={}
 for q in range(len(g)-2):
  for u in range(len(g[0])-2):
   r=[g[q+f//3][u+f%3]for f in range(9)]
   i=*(g<1for g in r),
   if(0 in r)<1<len({*r}):
    i=*(g==2for g in r),;p={i:sum({*r})-2}
    for f in range(9):e[i]=p;i=*(i[2+f%3*3-f//3]for f in range(9)),;g[q+f//3][u+f%3]=0
 g=[[*g]for g in zip(*g)if any(g)]
 g=[[*g]for g in zip(*g)if any(g)]
 for q in range(len(g)-2):
  for u in range(len(g[0])-2):
   r=[g[q+f//3][u+f%3]for f in range(9)]
   i=*(g<1for g in r),
   if e.get(i,{}).get(i,{}):
    l=e.get(i,{}).popitem()[1]
    for f in range(9):g[q+f//3][u+f%3]=i[f]*2 or l
 for q in range(len(g)-2):
  for u in range(len(g[0])-2):
   r=[g[q+f//3][u+f%3]for f in range(9)]
   i=*(g<1for g in r),
   if e.get(i,{}):
    l=e.get(i,{}).popitem()[1]
    for f in range(9):g[q+f//3][u+f%3]=i[f]*2 or l
 return g