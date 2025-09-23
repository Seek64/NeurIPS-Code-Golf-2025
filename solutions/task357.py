def p(g,i=9):
	for l in g:w=len(l)-1;l[:]=[8]*-~w;l[abs(w-(w+i)%(2*w))]=1;i-=1
	return g