def p(g,s=range(18)):
	for u in s:
		k=[]
		for v in 0,1,2:w=g[u%9//3*4+v];n=u%3*4;k+=w[n:n+3];w[n:n+3]=[s[u%9]]*3
		if len({*k})==5:s=k
	return g