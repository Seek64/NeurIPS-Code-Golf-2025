def p(r):
 f=[p*1for p in r]
 for p in range(28):
  for t in range(28):
   if r[p][t+1]==r[p][t-1]!=r[p][t]!=r[p+1][t]==r[p-1][t]!={r[p][t+1],r[p+1][t+1]}!={r[p+1][t]}:
    for e in range(28):
     for n in range(28):
      if r[p][t]==r[e][n]:
       for o in range(-1,2):
        for h in range(-1,2):
         i=1
         if r[p+o*i][t+h*i]!=r[p+1][t+2]:
          f[e+o*i][n+h*i]=r[p+o][t+h];i+=1
          if r[p][t]!=r[p+o*i][t+h*i]!=r[p+1][t+2]:
           while r[e+o*i][n+h*i]!=r[p+1][t+2]:f[e+o*i][n+h*i]=r[p+o][t+h];i+=1
    for o in range(-2,3):
     for h in range(-2,3):f[p+o][t+h]=r[p+1][t+2]
 return f