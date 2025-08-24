def p(g):
	*g,=zip(*g);s=i=0
	while i<len(g):
		r=g[i];g[i]=[x if x-5else max({*g[i-1],*r,*g[i+1]}-{5})for x in r*2][s%3:][:3];s+=max([*g,[1]][i+1])<1and g[i+2].index(5)-r.index(5);i+=(k:=max(g[i-1])>0)
		if k<1:del g[i-1]
	return[*zip(*g)]