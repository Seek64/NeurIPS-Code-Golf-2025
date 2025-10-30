def p(f):
 k=2
 for s in range(10-k):
  for e in range(10-k):
   if all(all(f[e:e+k])for f in f[s:s+k]):p=2*s+k-1;r=2*e+k-1
 k=3
 for s in range(10-k):
  for e in range(10-k):
   if all(all(f[e:e+k])for f in f[s:s+k]):p=2*s+k-1;r=2*e+k-1
 k=0
 for s in range(10-k):
  for e in range(10-k):
   if l:=f[s][e]:g=2*s-p;e=2*e-r;g,e=-e,g;f[p+g>>1][e+r>>1]=l;g,e=-e,g;f[p+g>>1][e+r>>1]=l;g,e=-e,g;f[p+g>>1][e+r>>1]=l
 return f