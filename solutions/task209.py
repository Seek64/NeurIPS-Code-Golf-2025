def p(f):
 for s,t in enumerate(f):
  e=[(t^4,u,d)for u,t in enumerate(f)for d,t in enumerate(t)if t];h,i=sorted(e)[:4:3]
  for d,m,q in e[e.index(i)+1:]:
   x=[u*9for u in f*2];t=5
   for g,u,c in e[e.index(i)+1:]:r=e[2][1]+s*(u-m);d=e[2][2]+s*(c-q);t+=s*s*(x[r][d]==g^4)+1;exec("x[r][d:d+s]=[g^4]*s;r+=1;"*s)
   if t>len(e):return[u[h[2]:i[2]+1]for u in x[h[1]:i[1]+1]]