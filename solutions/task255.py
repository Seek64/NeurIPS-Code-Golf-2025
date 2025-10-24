def p(e,h=51,i=-2):
 f=h//4
 for l in e:
  i+=1
  o=[[*o]for o in e];l=0;g=lambda o,k=9,g=f:l<31*all(k>>o&1for o in e[l:l+o]for o in o[i-30:i+g])
  if g(9):
   while(l:=l+1)*(g(1,1)+g(5)):e[l-1][1+i:f-1+i]=(f-2)*[3]
   if g(5,1,f-2):e=o
   i+=5
 return e*(3-f)or p([[*o]for o in zip(*e)][::-1],h-1)