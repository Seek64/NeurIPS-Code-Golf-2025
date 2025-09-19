def p(g,n=59):
 w=n//4;d=c=-2
 while c<31-w:
  c+=1;i=0;h=[*map(list,g)];t=lambda J,N=9,C=c,W=w:i<31*all(N>>x&1for y in g[i:i+J]for x in y[max(0,C):C+W])
  if c<0:g=h
  if t(9):
   while(i:=i+1)*(c>d)*(t(1,1)+t(5)):g[i-1][c+1:c+w-1]=-2%w*[3]
   if t(5,1,d:=c+1,w-2):g=h
 return g*(3-w)or p([*zip(*g)][::-1],n-1)