def p(h):
 for e in range(8):
  h[::-1]=zip(*h)
  for e in range(len(h)):
   for i in range(len(h)):
    for q,g in(f:=[(e,i)]):*h[q],=h[q];h[q][i+i-g-1]=h[e][i-1];f+=[(p+q,g+n)for p in range(-1,2)for n in range(-1,2)if 0<h[e][i-1]!=(2*(2*h)[p+q])[g+n]==h[e][i]>0==h[p+q][i+i-g-n-1]]
 return h