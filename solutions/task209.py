def p(i):
 e=[(n^4,d,x)for d,i in enumerate(i)for x,n in enumerate(i)if n]
 for x,n in enumerate(i):
  for d,t,n in e[e.index(sorted(e)[3])+1:]:
   f=[n*9for n in i*2];r=5
   for d,l,o in e[e.index(sorted(e)[3])+1:]:l=e[2][1]+x*(l-t);r+=x*x*(f[l][e[2][2]+x*(o-n)]==d^4)+1;exec("f[l][e[2][2]+x*(o-n):e[2][2]+x*(o-n)+x]=[d^4]*x;l+=1;"*x)
   if r>len(e):return[n[sorted(e)[0][2]:sorted(e)[3][2]+1]for n in f[sorted(e)[0][1]:sorted(e)[3][1]+1]]