def p(g):
 t=sum(g,[]).index(5);l=len(g[0])
 for r,a in zip(g[t//l-1:][:3],[[x for*c,x in zip(*g,r)if{*c}-{0,5}]for r in g if{*r}-{0,5}]):r[t%l-1:t%l+2]=a
 return g