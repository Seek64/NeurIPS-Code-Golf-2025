def p(g):
 f=min(p for p in range(8)if any(g[p]))
 for n in range(8):
  for a in range(r:=min(r for r in range(f,9)if any(g[r])-1),f-r+16):
   for p in range(5):
    if min((2*g[a+r-f][:1]+g[a+r-f])[i+4-p]==g[r][i]*(i<9-n)for r in range(f,r)for i in range(8)):g[a:a+r-f]=[[g[a+r-f][i]or(g[a+r-f][:2]+g[r]+g[r][-2:])[i+p]%7for i in range(10)]for r in range(f,r)]
 return g