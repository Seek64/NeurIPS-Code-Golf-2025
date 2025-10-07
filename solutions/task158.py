def p(g):
 for k in range(12):
  l=3-k//4;g=[[*k] for k in zip(*g[::-1])]
  for i in range(len(g)+1-3*l):
   for j in range(len(g[0])+1-3*l):
    m=[g[i+k//(3*l)][j+k%(3*l)] for k in range(3*l*3*l)]
    if m[0]!=m[8]!=3<len({*m}):q=m
 for k in range(12):
  l=3-k//4;g=[[*k] for k in zip(*g[::-1])]
  for i in range(len(g)+1-3*l):
   for j in range(len(g[0])+1-3*l):
    m=[g[i+k//(3*l)][j+k%(3*l)] for k in range(3*l*3*l)]
    if m[:l]==m[l*3*l-3*l:][:l]==q[:1]*l!=m[-l:]==q[8:]*l!=m[~l]==m[l]:
     for k in range(3*l*3*l):g[i+k//(3*l)][j+k%(3*l)]=q[k//(3*l)//l*3+k%(3*l)//l]
 return g