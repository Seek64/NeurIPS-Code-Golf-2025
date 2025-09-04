def p(g):
 g=[*map(list,zip(*g))];m=[r.count(2)for r in g]
 for i in range(64):
  w=4-i//16;i%=16-w;l=g[i:i+w];*_,o,_,x=max((-(1in sum(g[j:j+w],l)),-len(q:={[*y,5].index(5)-x for x,y in zip(m[j:],l)}),min(q),m[j-1]+m[j+w-15],j)for j in range(16-w))
  while w*all(5in r for r in l):w-=1;c=m[b:=x+w];g[b]=[z%4for z in g[b][:c]+l.pop()[c+o:]+4*[0]][:6]+g[b][6:];g[i+w][6:]=4*[0]
 return[*zip(*g)]