def p(g):
 for l in(3,2,1):
  for e in(-1,1):
   for i in range(len(g)*2-3*l+1):
    for j in range(len(g[0])-3*l+1):
     m=[r[j:j+3*l][::e]for r in(g+g[::-1])[i:i+3*l]]
     if len({*f"{m}"})>7>0<m[0][0]!=m[-1][-1]:q=m
 for l in(3,2,1):
  for e in(-1,1):
   for i in range(len(g)*2-3*l+1):
    for j in range(len(g[0])-3*l+1):
     m=[r[j:j+3*l][::e]for r in(g+g[::-1])[i:i+3*l]]
     if m[0][:l]==q[0][:1]*l!=m[-1][-l:]==m[-l][-l:]==q[-1][-1:]*l!=m[0][l]==m[-1][~l]:
      for k in range(3*l*3*l):(g+g[::-1])[i+k//(3*l)][j+k%(3*l)]=q[k//(3*l)//l][::e][k%(3*l)//l]
 return g