def p(e):
 def p(e,o,n,i,r,l=5):
  e=[o*1for o in e]
  while 0<o<len(e)-1>n>0==(d:=e[o+i][n+r]):o+=i;n+=r;e[o][n]=3
  return p(e,o,n,r,i,l+1)or p(e,o,n,-r,-i,l+1)if d>7>l else(d==2)*e
 return max(p(e,o,n,i,r)for o in range(len(e))for n in range(len(e))for i in range(-1,2)for r in range(-1,2)if 3==e[o][n]==e[o][n-r])