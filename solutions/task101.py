def p(r):
 t,*d=len(r[0])+2,
 for a in r:d+=*a,0,0
 f=[d.index(1)]
 for a in f:f+=[a for a in(a-t,a-1,a+1,a+t)if len(d)>a>(a in f)*t<d[a]]
 e=f
 for i in range(len(d)):
  f=[i]
  for a in f:f+=[a for a in(a-t,a-1,a+1,a+t)if len(d)>a>(a in f)*t<d[a]]
  l=58%len(f)+2>>1
  for a in e:
   for p in range(l*l*all(d[a]>1for a in f)):d[i+l*a-l*min(a for a in e if d[a]>1)+p//l*t+p%l]=d[a]
 return[d[i*t:][:t-2]for i in range(len(r))]