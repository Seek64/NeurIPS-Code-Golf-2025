def p(g):
 g=[*map(list,zip(*g))]
 for i in range(64):
  w=4-i//16;i%=16-w;*_,o,_,x=max((-(1in sum(g[j:j+w],l:=g[i:i+w])),-len(q:={[*y,5].index(5)-x.count(2)for x,y in zip(g[j:],l)}),min(q),(g[j-1]+g[j+w-15]).count(2),j)for j in range(16-w))
  for j in range(w*all(5in r for r in l)):c=g[x+j].count(2);g[x+j]=[z%4for z in g[x+j][:c]+l[j][c+o:]+4*[0]][:6]+g[x+j][6:];g[i+j][6:]=4*[0]
 return[*map(list,zip(*g))]