def p(g):
	i=w=len(g[0])-1
	for l in g[::-1]:l[:]=[8]*-~w;l[abs(w-i%(2*w))]=1;i+=1
	return g