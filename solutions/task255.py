def p(b,n=59):
 a=n//4;z=-2
 for l in b:
  z+=1;c=0;d=[[*b]for b in b];l=lambda n,l=9,a=a:c<31*all(l>>b&1for b in b[c:c+n]for b in b[z-30:z+a])
  if l(9):
   while(c:=c+1)*(l(1,1)+l(5)):b[c-1][1+z:a-1+z]=(a-2)*[3]
   z+=1
   if l(5,1,a-2):b=d
   z+=4
 return b*(3-a)or p([[*b]for b in zip(*b)][::-1],n-1)