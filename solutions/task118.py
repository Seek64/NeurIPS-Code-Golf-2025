def p(l,e=set()):
 def p(l,e=set()):
  return [l and(p(l[1:],e)or not l[0]&e and p(l[1:],e|l[0])),e][d<e]
 d={(u,n)for u in range(len(l))for n in range(len(l[0]))if l[u][n]&2}
 for n in 2,3:
  if e:=p([e for f in range(len(l))for e in range(len(l[0]))for e in[{(u,n)for n in range(-n,1+n)for u,n in[(f+n,e),(f,e+n)]if len(l)>u>-1<n<len(l[0])}]if min(l[u][n]for u,n in e)]):
   for u,n in e:l[u][n]+=l[u][n]-2
   return l