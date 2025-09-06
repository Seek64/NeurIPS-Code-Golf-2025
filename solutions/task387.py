def p(g):
 for j in range(4):
  w=len(g[0]);h=len(g);l=sum(g,[]);i,j={l.index(j):0for j in l if j%5}
  while j-i>3:l[i:=i+2]=l[j:=j-2]=5
  g=[l[j-w::-w]for j in range(w)]
 return[[g[i][j]or len(q:={*l}-{*(3*sum((g[:1]+g)[i:i+3],[0]))[j+2::h],5})%2*max(q)for j in range(h)]for i in range(w)]