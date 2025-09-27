def p(i):
 f=min(r for r in range(8)if any(i[r]))
 for d in range(8):
  for e in range(r:=min(r for r in range(f,9)if any(i[r])-1),f-r+16):
   for y in range(5):
    if min((2*i[e+r-f][:1]+i[e+r-f])[o+4-y]==i[r][o]*(o<9-d)for r in range(f,r)for o in range(8)):i[e:e+r-f]=[[i[e+r-f][o]or(i[e+r-f][:2]+i[r]+i[r][-2:])[o+y]%7for o in range(10)]for r in range(f,r)]
 return i