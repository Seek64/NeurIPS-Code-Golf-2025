def p(l):
 for r in range(4):
  n=len(l[0]);m=len(l);e=sum(l,[]);r,l={e.index(l):0for l in e if l%5}
  while l-r>3:e[r:=r+2]=e[l:=l-2]=5
  l=[e[r-n::-n]for r in range(n)]
 return[[l[r][f]or len(n:={*e}-{*(3*sum((l[:1]+l)[r:r+3],[0]))[f+2::m],5})%2*max(n)for f in range(m)]for r in range(n)]