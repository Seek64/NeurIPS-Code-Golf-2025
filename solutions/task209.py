def p(f,l=2):
 m=[(r^4,a,i)for a,l in enumerate(f)for i,r in enumerate(l)if r];u,q=sorted(m)[:4:3]
 for a,b,r in m[m.index(q)+1:]:
  x=[l*9for l in f*2];t=5
  for a,o,w in m[m.index(q)+1:]:y=m[2][1]+l*(o-b);i=m[2][2]+l*(w-r);t+=l*l*(x[y][i]==a^4)+1;exec("x[y][i:i+l]=[a^4]*l;y+=1;"*l)
  if t>len(m):return[l[u[2]:q[2]+1]for l in x[u[1]:q[1]+1]]
 return p(f,l+1)