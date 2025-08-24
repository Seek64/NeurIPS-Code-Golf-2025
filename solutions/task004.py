def p(g,w=2):
	for r in g[::-1]:w=(w-3)*any(r)+2;del r[w<1and-~r.index(max(r))|w];r[:0]=0,
	return g