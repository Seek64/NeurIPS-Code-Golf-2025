def p(g):
	G=g
	for _ in'@@':G=[r for*r,in zip(*G)if 8in r];g=[r for*r,in zip(*g)if{*r}-{8,0}]
	for l in g[1:-1]:l[1:-1]=G.pop(0)
	for _ in'@'*4:i=0;g=[(z:=min(i,len(g)-(i:=i+1)))%1or[c%~c&r[0]for c in r[:z]]+r[z:]for*r,in zip(*g[::-1])]
	return g