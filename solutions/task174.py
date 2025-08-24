def p(g,i=1):
	for _ in(w:=g):k=1;w=[r for*r,in zip(*w)if(k:=k&(r==r[::-1]))<=i in r]
	return w*k or p(g,i+1)