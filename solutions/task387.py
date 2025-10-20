def p(o):
 for q in range(4):
  r=sum(o,[]);n,v,p,*n={r.index(q):0for q in r}
  for q in range(p-v>>2):r[p+~q*2]=r[v-~q*2]=5
  o=[r[q-len(o[0])::-len(o[0])]for q in range(len(o[0]))]
 for q in range(4):
  r=sum(o,[]);n,v,p,*n={r.index(q):0for q in r}
  for q in range(8):r[p-q%-3+~(q//3%-3)*len(o[0])-3]=r[n[0]]
  o=[r[q-len(o[0])::-len(o[0])]for q in range(len(o[0]))]
 return o