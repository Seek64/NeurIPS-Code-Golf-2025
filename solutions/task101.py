def p(e):
 m,*t=len(e[0])+2,
 for f in e:t+=*f,0,0
 i=[t.index(1)]
 for f in i:i+=[f for f in(f-m,f-1,f+1,f+m)if len(t)>f>(f in i)*m<t[f]]
 n=i
 for r in range(len(t)):
  i=[r]
  for f in i:i+=[f for f in(f-m,f-1,f+1,f+m)if len(t)>f>(f in i)*m<t[f]]
  l=6+26%len(i)>>2
  for a in n:
   for f in range(l*l*all(t[f]>1for f in i)):t[r+l*a-l*min(f for f in n if t[f]>1)+f//l*m+f%l]=t[a]
 return[t[r*m:][:m-2]for r in range(len(e))]