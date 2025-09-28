def p(o):
 for q in range(4):
  r=sum(o,[]);q,p,q,p,=[r.index(q)for q in r if q%5]
  while q-p>3:p+=2;q-=2;r[p]=r[q]=5
  o=[r[q-len(o[0])::-len(o[0])]for q in range(len(o[0]))]
 return[[o[q][n]or len(p:={*r}-{*(3*sum((o[:1]+o)[q:q+3],[0]))[n+2::len(o[0])],5})%2*max(p)for n in range(len(o[0]))]for q in range(len(o))]