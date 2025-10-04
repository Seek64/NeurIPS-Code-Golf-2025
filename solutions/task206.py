def p(g):
 t=sum(g,[]).index(5);l=len(g[0]);q=lambda h:[r for r in zip(*h)if{*r}-{0,5}]
 for g[t//l-1][t%l-1:t%l+2]in q(q(g)):t+=l
 return g