def p(e):
 def p(e,u,n,a,r,i=5):
  e=[u*1for u in e]
  while 0<u<len(e)-1>n>0==(d:=e[u+a][n+r]):u+=a;n+=r;e[u][n]=3
  return p(e,u,n,r,a,i+1)or p(e,u,n,-r,-a,i+1)if d>7>i else(d==2)*e
 return max(p(e,u,n,a,r)for u in range(len(e))for n in range(len(e))for a in range(-1,2)for r in range(-1,2)if e[u][n]==3==e[u][n-r])