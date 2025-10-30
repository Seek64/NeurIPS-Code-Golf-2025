def p(g):
 e=[(n^4,r,o)for r,g in enumerate(g)for o,n in enumerate(g)if n]
 for o,n in enumerate(g):
  for q,j,n in e[e.index(sorted(e)[3])+1:]:
   d=[r*9for r in g*2];f=5
   for q,r,l in e[e.index(sorted(e)[3])+1:]:r=e[2][1]+o*(r-j);f+=o*o*(d[r][e[2][2]+o*(l-n)]==q^4)+1;exec(o*"d[r][e[2][2]+o*(l-n):e[2][2]+o*(l-n)+o]=o*[q^4];r+=1;")
   if f>len(e):return[r[e[0][2]:sorted(e)[3][2]+1]for r in d[e[0][1]:sorted(e)[3][1]+1]]