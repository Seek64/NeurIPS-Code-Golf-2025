def p(b,n=59):
 a=n//4;e=z=-2
 while z<31-a:
  z+=1;c=0;d=[[*b]for b in b];l=lambda n,l=9,d=z,a=a:c<31*all(l>>b&1for b in b[c:c+n]for b in b[max(0,d):d+a])
  if z<0:b=d
  if l(9):
   while(c:=c+1)*(z>e)*(l(1,1)+l(5)):b[c-1][z+1:z+a-1]=-2%a*[3]
   if l(5,1,e:=z+1,a-2):b=d
 return b*(3-a)or p([*zip(*b)][::-1],n-1)