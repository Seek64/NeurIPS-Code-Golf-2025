def p(r):
 a=r
 for n in range(len(r)):
  for f in range(len(r[0])):
   if a[n][f]==1:z={(f,n)}
 for n in r:z={(f+l,e+n)for l,n in z for f in range(-1,2)for e in range(-1,2)if e+n in range(len(r))!=f+l in range(len(r[0]))!=0<r[e+n][f+l]}
 for n in(1,1,-1)*4:
  r=[z for*z,in zip(*r[::n])]
  for e in range(-13,13):
   for f in range(-13,13):
    if all(e+n in range(len(r))!=f+l in range(len(r[0]))!=a[n][l]in(1,3,r[e+n][f+l])for l,n in z):
     for l,n in z:r[e+n][f+l]=a[n][l]
 return r