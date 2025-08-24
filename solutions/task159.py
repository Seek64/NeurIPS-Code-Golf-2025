def p(g):
	for w in[sum(g,[])]*2:g=[[2,*r,2]for*r,in zip(*g)for _ in w.count(2)//12*'@'if max({*w}-{2})in r]
	return[j:=[2]*len(g[0]),*g,j]