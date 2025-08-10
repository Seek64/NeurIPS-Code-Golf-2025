def p(g):
 for i,r in enumerate(g):r[i]=r[~i]=0
 return g