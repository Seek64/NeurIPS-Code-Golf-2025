def p(b,e=51,i=-2):
 f=e//4
 for h in b:
  i+=1
  d=[[*d]for d in b];h=0;g=lambda d,f=9,g=f:h<31*all(f>>d&1for d in b[h:h+d]for d in d[i-30:i+g])
  if g(9):
   while(h:=h+1)*(g(1,1)+g(5)):b[h-1][1+i:f-1+i]=(f-2)*[3]
   if g(5,1,f-2):b=d
   i+=5
 return b*(3-f)or p([[*d]for d in zip(*b)][::-1],e-1)