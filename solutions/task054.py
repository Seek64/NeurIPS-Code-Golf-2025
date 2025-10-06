def p(m):
 o=[r*1for r in m]
 for p in range(28):
  for k in range(28):
   if m[p][k+1]==m[p][k-1]!=m[p][k]!=m[p+1][k]==m[p-1][k]!={m[p+1][k],m[p][k+1],m[p+1][k+1]}!={m[p+1][k]}:
    for d in range(28):
     for b in range(28):
      if m[p][k]==m[d][b]:
       for l in range(-1,2):
        for h in range(-1,2):
         if m[p+l][k+h]!=m[p+1][k+2]:
          g=1;o[d+l*g][b+h*g]=m[p+l][k+h];g+=1
          if m[p][k]!=m[p+l*g][k+h*g]!=m[p+1][k+2]:
           while m[d+l*g][b+h*g]!=m[p+1][k+2]:o[d+l*g][b+h*g]=m[p+l][k+h];g+=1
    for l in range(-2,3):
     for h in range(-2,3):o[p+l][k+h]=m[p+1][k+2]
    return o