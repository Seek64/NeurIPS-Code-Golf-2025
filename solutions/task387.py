def p(g):
 for _ in g*4:
  g=[*map(list,zip(*g[::-1]))];w=len(g[0]);l=sum(g,[]);i,j={l.index(x):0for x in l if x%5}
  while j-i>3:i+=2;j-=2;g[i//w][i%w]=g[i//w][j%w]=5
 return[[r[1][j]or len(q:={*l}-{*(3*sum(r,[0]))[j+2::w],5})%2*max(q)for j in range(w)]for r in zip(g[:1]+g,g,g[1:]+g[:1])]