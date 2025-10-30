def p(r):
 a=r
 for l in range(len(r)):
  for e in range(len(r[0])):
   if a[l][e]==1:q={(e,l)}
 for l in r:q={(e+z,i+l)for z,l in q for e in range(-1,2)for i in range(-1,2)if i+l in range(len(r))!=e+z in range(len(r[0]))!=0<r[i+l][e+z]}
 for l in(1,1,-1)*4:
  r=[z for*z,in zip(*r[::l])]
  for i in range(-13,13):
   for e in range(-13,13):
    if all(i+l in range(len(r))!=e+z in range(len(r[0]))!=a[l][z]in(1,3,r[i+l][e+z])for z,l in q):
     for z,l in q:r[i+l][e+z]=a[l][z]
 return r