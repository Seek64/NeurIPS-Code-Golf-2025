def p(g):
	x=g[3][5]%3*6
	for l in g[:3]:l[x:x+3]=l[5:2:-1]
	return g