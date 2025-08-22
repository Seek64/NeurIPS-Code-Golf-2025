def p(g,i=0):
 for r in g:r[i]=r[~i]=0;i+=1
 return g