def p(m):
 i,*o=len(m[0])+2,
 for f in m:o+=*f,0,0
 d=[o.index(1)]
 for f in d:d+=[f for f in(f-i,f-1,f+1,f+i)if(f in d)==0<f<len(o)>0<o[f]]
 j=min(f for f in d if o[f]>1);n=d
 for r in range(len(o)):
  d=[r]
  for f in d:d+=[f for f in(f-i,f-1,f+1,f+i)if(f in d)==0<f<len(o)>0<o[f]]
  l=6+26%len(d)>>2
  for e in n:
   for f in range(l*l*all(o[f]>1for f in d)):o[r+l*e-l*j+f//l*i+f%l]=o[e]
 return[o[r*i:][:i-2]for r in range(len(m))]