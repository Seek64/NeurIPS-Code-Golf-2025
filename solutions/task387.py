def p(o):
 for q in range(4):
  r=sum(o,[]);n,q,p,*n={r.index(q):0for q in r}
  while p-q>3:q+=2;p-=2;r[p]=r[q]=5
  o=[r[q-len(o[0])::-len(o[0])]for q in range(len(o[0]))]
 for q in range(4):
  r=sum(o,[]);n,q,p,*n={r.index(q):0for q in r}
  for q in[1,3,1+len(o[0]),2+len(o[0]),3+len(o[0]),1-len(o[0]),2-len(o[0]),3-len(o[0])]:r[p-q]=r[n[0]]
  o=[r[q-len(o[0])::-len(o[0])]for q in range(len(o[0]))]
 return o