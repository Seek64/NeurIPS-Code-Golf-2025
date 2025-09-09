def p(u):
 i=range(9);c={};f=lambda a:[a(p,s,[u[p+a//3][s+a%3]for a in i])for p in range(len(u)-2)for s in range(len(u[0])-2)]
 def p(p,s,n):
  if len(r:={*n})==2and r&{0,2}=={2}:
   n=tuple(a==2for a in n);k={n:sum(r)-2}
   for a in range(4):c[n]=k;n=tuple(n[a%3*3+2-a//3]for a in i)
   for a in i:u[p+a//3][s+a%3]=0
 f(p);u=[*map(list,zip(*filter(any,[*map(list,zip(*filter(any,u)))])))];[f(lambda p,s,n:(t:=c.get(n:=tuple(a==0for a in n)))and(a or n in t)and(r:=t.popitem()[1],[u[p+a//3].__setitem__(s+a%3,(r,2)[n[a]])for a in i]))for a in range(2)];return u