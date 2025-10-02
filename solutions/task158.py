def p(g):
 for i in range(12):
  l=3-i//4;g=[[*g]for g in zip(*g[::-1])]
  for i in range(len(g)-3*l+1):
   for j in range(len(g[0])-3*l+1):
    m=[g[j:j+3*l]for g in g[i:i+3*l]]
    if m[0][0]!=m[-1][-1]!=7<len({*f"{m}"}):q=m
 for i in range(12):
  l=3-i//4;g=[[*g]for g in zip(*g[::-1])]
  for i in range(len(g)-3*l+1):
   for j in range(len(g[0])-3*l+1):
    m=[g[j:j+3*l]for g in g[i:i+3*l]]
    if m[0][:l]==q[0][:1]*l!=m[-1][-l:]==m[-l][-l:]==q[-1][-1:]*l!=m[-1][~l]==m[0][l]:
     for k in range(3*l*3*l):g[i+k//(3*l)][j+k%(3*l)]=q[k//(3*l)//l][k%(3*l)//l]
 return g